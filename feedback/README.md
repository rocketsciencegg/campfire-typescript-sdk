# Campfire OpenAPI spec: fixes and feedback

From Rocket Science, 2026-10-15 (second version).

## What changed since our first package

You published a new spec on the evening of 2026-10-15. We ran the same script on it. This package replaces the first one.

- Your update removed the trailing slash from 26 paths (45 operations), for example `/coa/api/v1/bill/` is now `/coa/api/v1/bill`. No path ends in `/` now.
- Your update changed the `id` path parameter of `/coa/api/v1/bill/{id}` from a string with pattern `^\d+$` to an integer.
- Neither change touched our fixes. All 8 fixes still apply with the same counts, and the patch still has 1,308 changed lines.
- The only lint count that changed is boolean `exclusiveMinimum` / `exclusiveMaximum`: 4,527 to 4,530, from the new `quantity` field on prepaid commits.

We generate our TypeScript SDK from your published spec (`https://api.meetcampfire.com/api/schema/?format=json`, OpenAPI 3.0.3). It lints with 0 errors in Speakeasy, but it has 489 warnings apart from the `exclusiveMinimum` / `exclusiveMaximum` ones. We fix most of them with a script. This package gives you those fixes as a patch, and a separate list of behavior that we use but that the spec does not document.

## Files

| File | What it is |
| --- | --- |
| `campfire.patch` | Unified diff: your published spec → our fixed spec. Only real changes (1,308 changed lines), no formatting noise |
| `campfire.published.json` | Your spec exactly as served on the evening of 2026-10-15 (SHA-256 `e3071fd53f810713de022f8fbc9349bd1df4eeef1214344f00660bbf75d0ab00`). The patch applies to this file |
| `campfire.json` | The fixed spec that we generate our SDK from |
| `fix_spec.py` | The script that makes `campfire.json` from your spec. Each fix is a named step with its reason |
| `speakeasy-lint-published.txt` | Speakeasy lint of your spec |
| `speakeasy-lint-fixed.txt` | Speakeasy lint of our fixed spec |

To apply the patch to your spec:

```sh
patch campfire.published.json campfire.patch   # result is identical to campfire.json
```

The patch keeps your file's formatting (`json.dumps(indent=4, ensure_ascii=False)`), so it also applies to a newer copy where the same lines are unchanged.

## Fixes in the patch

| # | Problem | Places | Our fix | Likely source change (drf-spectacular) |
| --- | --- | --- | --- | --- |
| 1 | Response `description` is empty. OpenAPI 3.0 requires it | 295 responses | HTTP reason phrase (`OK`, `Created`, `No Content`, `Bad Request`, ...) | Give each response a description, for example with `OpenApiResponse(description=...)` |
| 2 | Response text is in `schema.description`, and the schema has no type. So the response has no description and no body shape | 7 responses (list below) | Move the text to the response `description`. The schema becomes `{"type": "object"}` | Pass the text as `OpenApiResponse(description=...)`, not as the schema |
| 3 | Operations use tags that have no global definition: `Bank Reconciliation`, `Company Objects`, `Custom Fields`, `Integrations` | 92 operations | Add the 4 tag definitions | Add them to `SPECTACULAR_SETTINGS['TAGS']` |
| 4 | Stray `coa` tag. Every related operation uses a real tag | 2 operations | `POST /coa/api/entity/{entity_id}/attachment` → `Settings`. `POST /coa/api/fixed-asset-automation/{id}/delete` → `Core Accounting` | `tags=[...]` in `extend_schema` on those views |
| 5 | The description is a leaked Python docstring: "The type of the None singleton." | 2 operations | Real summary and description | Set a description on `POST /coa/api/fixed-asset-automation/{id}/delete` and `POST /rr/api/v1/product/{id}/delete` |
| 6 | No `summary` | 1 operation | "Preview Contract Minimum Commit" | Summary on `GET /rr/api/v1/contracts/{id}/minimum-commit-preview` |
| 7 | The request body has required fields, but the spec marks it optional | 21 operations (list below) | `requestBody.required: true` | Mark these bodies required |
| 8 | Nullable choice fields written as `oneOf: [XEnum, BlankEnum, NullEnum]` | 79 places | `allOf: [XEnum]` + `nullable: true` | `ENUM_ADD_EXPLICIT_BLANK_NULL_CHOICE = False` should give the same result |

Fix 8 is optional. With the `oneOf` form, Speakeasy cannot check a `default` value. For example, `vendor_type` defaults to `"vendor"` and gets a warning. Generators also turn the form into three-way union types. Our change removes `""` as an allowed value, so you decide if it fits your API.

**Fix 2, the 7 responses:**

- `DELETE /coa/api/journal_entry/{id}`: 400 and 409
- `GET /coa/api/transaction/merge`: 400
- `POST /coa/api/transaction/merge`: 400
- `GET /coa/api/v1/bill/{bill_id}/empty-transaction-default-department-tags`: 404
- `POST /coa/api/v1/credit-memo/{credit_memo_id}/mark-used`: 200
- `POST /coa/api/v1/debit-memo/{debit_memo_id}/mark-used`: 200

**Fix 7, the 21 request bodies:**

- `POST` and `PUT` on each of these paths (the collection and `{id}`):
  - `/ca/api/user_currency`
  - `/coa/api/budgets/{budget_pk}/accounts`
  - `/coa/api/entity`
  - `/coa/api/intercompany-journal-entry`
  - `/coa/api/vendor_custom_field_1`
  - `/rr/api/v1/contracts`
  - `/rr/api/v1/product`
  - `/rr/api/v1/transactions`
- `PUT /coa/api/chart-account-settings`
- `PUT /coa/api/vendor-contact/{id}`
- `POST /coa/api/vendor/{id}/contacts`
- `POST /coa/api/intercompany-journal-entry/balance`
- `POST /coa/api/transaction/merge`

## Warnings we left as they are

After the fixes, Speakeasy still gives 0 errors, and the 489 other warnings go down to 68. These remain, and we do not think that they need a change:

| Warning | Count | Why we keep it |
| --- | --- | --- |
| Boolean `exclusiveMinimum` / `exclusiveMaximum` | 4,530 | Valid OpenAPI 3.0.3. Speakeasy expects the 3.1 number form. The bounds come from Django decimal fields and are real |
| Request body is optional | 61 operations | Their schemas have no required field (mostly `PATCH`), so an empty body is valid |
| Error responses with non-object content | 7 responses | They are free-form objects (`additionalProperties: {}`), which Speakeasy does not support. This is not a spec defect |

## Behavior the spec does not document

We use these items, or you told us about them, but the published spec does not describe them. We did not add them to our copy of the spec.

| Area | What we know | What is missing |
| --- | --- | --- |
| `GET /coa/api/payment-term` | It exists. Pedro Rodrigues named it on Slack | Not in the spec |
| `GET /coa/api/v1/amortization` | It exists. Pedro Rodrigues named it on Slack | Not in the spec. Since February 2026, the spec also no longer has `/coa/api/v1/bill/amortization` or `/coa/api/v1/bill/{bill_id}/amortization` |
| `GET /coa/api/general-ledger` parameters | It filters on `start_date` / `end_date`. `account_ids` takes one account: a comma list or a repeated parameter is ignored. It pages on `limit` / `offset`. It silently ignores `page`, `date_from` and `date_to` | The operation has no parameters in the spec |
| Rate limits | A 429 comes with `retry-after: 1` and the body `{"detail": "Request was throttled. Expected available in 1 second."}`. One sequential client at about 4 requests per second gets 429s. 10 concurrent requests got four 429s. Successful responses have no `x-ratelimit-*` headers | No published limit. No operation lists a 429 response |
| `GET /ca/api/draft_queue` and `/ca/api/draft_queue/{id}` | We use them to read draft invoices and journal entries (filter `created_by`, `limit` / `offset`) | Not in the spec |
| `GET /coa/api/tax_rate` | We use it to list tax rates | Not in the spec |

## Questions

1. Did the bill amortization endpoints move to `/coa/api/v1/amortization`, or did you remove them?
2. Is there a published rate limit that we should pace against?

## When you publish an update

We run `fix_spec.py` on each new version of your spec, and we send you the new patch. A fix that you adopt disappears from the patch.
