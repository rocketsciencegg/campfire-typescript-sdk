#!/usr/bin/env python3
"""Turn Campfire's published OpenAPI spec into the one this SDK is generated from.

    python3 scripts/fix_spec.py campfire.upstream.json campfire.json

campfire.upstream.json is Campfire's spec exactly as downloaded (`just fetch-spec`), so
`just spec-diff` (campfire.patch) is always the full list of what we changed, and is what we send
back to Campfire. Every fix below is a named step that prints how many places it touched; a step
that touches nothing on a fresh download is a fix Campfire has adopted, and can be deleted.

Python, not Node, because `json.dumps(indent=4, ensure_ascii=False)` writes Campfire's file byte
for byte (Node turns `50000.0` into `50000`). So the patch holds only real changes and applies
cleanly to Campfire's own copy.

Deliberately NOT changed:
- Boolean `exclusiveMinimum` / `exclusiveMaximum`. They are valid OAS 3.0.3 (Speakeasy warns
  because it expects the 3.1 number form) and carry real bounds from Django decimal fields.
- Optional request bodies whose schema has no required fields (PATCH, mostly). Sending no body
  there is legal, so marking it required would be a guess.
"""

import json
import sys

METHODS = ('get', 'put', 'post', 'delete', 'options', 'head', 'patch', 'trace')


def main(src, dst):
    with open(src, encoding='utf-8') as f:
        spec = json.load(f)

    def operations():
        for path, item in spec['paths'].items():
            for method in METHODS:
                if method in item:
                    yield path, method, item[method]

    def resolve(schema):
        ref = (schema or {}).get('$ref', '')
        prefix = '#/components/schemas/'
        return spec['components']['schemas'].get(ref[len(prefix):]) if ref.startswith(prefix) else schema

    def walk(node, visit):
        if isinstance(node, list):
            for item in node:
                walk(item, visit)
        elif isinstance(node, dict):
            visit(node)
            for value in list(node.values()):
                walk(value, visit)

    steps = []

    def step(name):
        def run(fn):
            steps.append((name, fn()))
        return run

    # 1. A few responses put their text in `schema.description` and give the schema no type, so
    #    the response has no description and the body has no shape. Move the text to the
    #    response; the body becomes an object (DRF bodies are JSON objects).
    @step('response text moved out of schema')
    def _():
        n = 0
        for _, _, op in operations():
            for response in op.get('responses', {}).values():
                for media in response.get('content', {}).values():
                    s = media.get('schema')
                    if isinstance(s, dict) and list(s) == ['description'] and isinstance(s['description'], str):
                        if not response.get('description'):
                            response['description'] = s['description']
                        media['schema'] = {'type': 'object'}
                        n += 1
        return n

    # 2. OpenAPI 3.0 requires a description on every response. Fill the empty ones with the HTTP
    #    reason phrase, which says nothing false.
    reasons = {
        '200': 'OK', '201': 'Created', '202': 'Accepted', '204': 'No Content', '206': 'Partial Content',
        '301': 'Moved Permanently', '302': 'Found', '304': 'Not Modified',
        '400': 'Bad Request', '401': 'Unauthorized', '403': 'Forbidden', '404': 'Not Found',
        '405': 'Method Not Allowed', '409': 'Conflict', '413': 'Payload Too Large', '422': 'Unprocessable Entity',
        '429': 'Too Many Requests', '500': 'Internal Server Error', '502': 'Bad Gateway', '503': 'Service Unavailable',
        'default': 'Default response',
    }

    @step('empty response descriptions filled')
    def _():
        n = 0
        for path, method, op in operations():
            for code, response in op.get('responses', {}).items():
                if '$ref' in response or response.get('description'):
                    continue
                if code not in reasons:
                    raise SystemExit(f'no reason phrase for {code} on {method.upper()} {path}')
                response['description'] = reasons[code]
                n += 1
        return n

    # 3. Two operations carry a stray `coa` tag where every sibling uses a real one. The tag also
    #    decides which SDK class an operation lands in.
    retag = {
        'POST /coa/api/entity/{entity_id}/attachment': 'Settings',
        'POST /coa/api/fixed-asset-automation/{id}/delete': 'Core Accounting',
    }

    @step('stray `coa` tags replaced')
    def _():
        n = 0
        for path, method, op in operations():
            to = retag.get(f'{method.upper()} {path}')
            if to and 'coa' in op.get('tags', []):
                op['tags'] = [to if t == 'coa' else t for t in op['tags']]
                n += 1
        return n

    # 4. Every tag an operation uses must be defined globally.
    tag_descriptions = {
        'Bank Reconciliation': 'Operations related to bank reconciliation and transaction matching.',
        'Company Objects': 'Operations related to company entities and organizational objects.',
        'Custom Fields': 'Operations related to custom field definitions and management.',
        'Integrations': 'Operations related to third-party integrations and webhooks.',
    }

    @step('missing global tags defined')
    def _():
        tags = spec.setdefault('tags', [])
        defined = {t['name'] for t in tags}
        n = 0
        for _, _, op in operations():
            for name in op.get('tags', []):
                if name in defined:
                    continue
                if name not in tag_descriptions:
                    raise SystemExit(f'tag "{name}" is used but has no definition and no description here')
                tags.append({'name': name, 'description': tag_descriptions[name]})
                defined.add(name)
                n += 1
        return n

    # 5. Operations with no summary, or whose description is a leaked Python docstring.
    docs = {
        'POST /coa/api/fixed-asset-automation/{id}/delete': {
            'summary': 'Delete Fixed Asset Automation',
            'description': 'Delete a fixed asset automation. Replaces the deprecated DELETE /coa/api/fixed-asset-automation/{id}/.',
        },
        'POST /rr/api/v1/product/{id}/delete': {
            'summary': 'Delete Product',
            'description': 'Delete a product.',
        },
        'GET /rr/api/v1/contracts/{id}/minimum-commit-preview': {
            'summary': 'Preview Contract Minimum Commit',
        },
    }
    leaked_docstrings = {'The type of the None singleton.'}

    @step('missing summaries and leaked docstrings fixed')
    def _():
        n = 0
        for path, method, op in operations():
            d = docs.get(f'{method.upper()} {path}')
            if not d:
                continue
            if 'summary' in d and not op.get('summary'):
                op['summary'] = d['summary']
                n += 1
            if 'description' in d and (not op.get('description') or op['description'] in leaked_docstrings):
                op['description'] = d['description']
                n += 1
        return n

    # 6. drf-spectacular writes a nullable/blankable choice field as
    #    `oneOf: [XEnum, BlankEnum, NullEnum]`. Speakeasy cannot check a `default` against that
    #    union, and generators turn it into a three-way union type. Write it as the enum plus
    #    `nullable`. This drops the explicit "" member; no consumer relies on it. drf-spectacular's
    #    ENUM_ADD_EXPLICIT_BLANK_NULL_CHOICE = False is the upstream switch for the same result.
    @step('Blank/Null enum unions collapsed to nullable enums')
    def _():
        wrappers = {'#/components/schemas/BlankEnum', '#/components/schemas/NullEnum'}
        count = [0]

        def visit(node):
            one_of = node.get('oneOf')
            if not isinstance(one_of, list):
                return
            real = [s for s in one_of if s.get('$ref') not in wrappers]
            if len(real) != 1 or len(real) == len(one_of):
                return
            has_null = any(s.get('$ref') == '#/components/schemas/NullEnum' for s in one_of)
            # Rebuild in place so `allOf` takes oneOf's position and the diff stays local.
            items = [('allOf', real) if k == 'oneOf' else (k, v) for k, v in node.items()]
            node.clear()
            node.update(items)
            if has_null:
                node['nullable'] = True
            count[0] += 1

        walk(spec, visit)
        text = json.dumps(spec)
        for name in ('BlankEnum', 'NullEnum'):
            if f'"#/components/schemas/{name}"' not in text:
                spec['components']['schemas'].pop(name, None)
        return count[0]

    # 7. A request body whose schema has required fields cannot be omitted; say so.
    @step('request bodies with required fields marked required')
    def _():
        n = 0
        for _, _, op in operations():
            body = op.get('requestBody')
            if not body or body.get('required'):
                continue
            if any((resolve(m.get('schema')) or {}).get('required') for m in body.get('content', {}).values()):
                body['required'] = True
                n += 1
        return n

    with open(dst, 'w', encoding='utf-8') as f:
        f.write(json.dumps(spec, indent=4, ensure_ascii=False))
    for name, n in steps:
        print(f'{n:5}  {name}')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit('usage: fix_spec.py <upstream.json> <out.json>')
    main(sys.argv[1], sys.argv[2])
