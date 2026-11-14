# Campfire OpenAPI spec: fixes and feedback

From Rocket Science, 2026-11-14.

## What changed since our last package

Our last package used your spec of 2026-10-21. This package uses your spec of 2026-11-14.

**Most important: your spec no longer says how to authenticate (new Fix 1).** Since your spec of 2026-10-15, it has no `securitySchemes` and no `security` block. Before, every operation required `knoxApiToken`. Code generators add the `Authorization` header only where the spec asks for it, so every client generated from your spec since then sends no credentials, and every call returns 401. Our SDK shipped this way in four releases before we found it. We missed it in our earlier packages, because we compared each spec only with the one before it. Our patch now restores the scheme.

- **New operations.** Your spec has 22 new operations (395 → 417). You removed none and renamed no operationId.
  - A `POST …/{id}/delete` endpoint for accounts, bills, invoices, credit and debit memos, journal entries, intercompany journal entries, fixed assets, vendors, and revenue-recognition contracts, milestones, subscriptions, usage, prepaid commits and transactions. The matching `DELETE` endpoints are now `deprecated`.
  - Audit log (list and get), bank-account totals, transaction allocation, contract subledger accounts, and the invoice CSV revenue preview.
  - New query parameters: `revenue_linkable_for`, `expense_billing_attachable`, `new_account` and `new_product`.
- **Schemas.** 25 schemas are new and 42 changed, mostly with new fields. `Type4aaEnum` is now `TypeB9aEnum` and adds `migration_offset`. The rename of a generated enum breaks every typed client. A stable name (an `ENUM_NAME_OVERRIDES` entry in drf-spectacular) prevents that.
- **Fixes you adopted.** Thank you:
  - `POST /coa/api/fixed-asset-automation/{id}/delete` now has a real tag (our old Fix 4), a summary and a description.
  - `POST /rr/api/v1/product/{id}/delete` now has a summary and a description.
  - No description is a leaked Python docstring any more, so we removed the old Fix 5.
- **The rate limit did not change.** It is still 10 requests per second.
- **Counts that grew with the spec.** Fix 2 now covers 302 responses (was 296). Fix 8 covers 81 places (was 79). The patch has 1,336 changed lines.

**Read-only fields in request bodies (repeated from our last package).** 1,214 properties in your spec are both `readOnly` and `required` (was 1,177). This release made `tag_ids` and `tag_group_ids` read-only and required on `Department`, `Product` and `AccountingInvoiceLine`, so our generated request types now ask callers to send them. drf-spectacular's `COMPONENT_SPLIT_REQUEST = True` makes separate request schemas without them. We did not put this in the patch, because it changes the shape of the spec.

We generate our TypeScript SDK from your published spec (`https://api.meetcampfire.com/api/schema/?format=json`, OpenAPI 3.0.3). It lints with 0 errors in Speakeasy, but it has 518 warnings apart from the `exclusiveMinimum` / `exclusiveMaximum` ones. We fix most of them with a script. This package gives you those fixes as a patch, and a separate list of behavior that we use but that the spec does not document.

## Files

| File | What it is |
| --- | --- |
| `campfire.patch` | Unified diff: your published spec → our fixed spec. Only real changes (1,336 changed lines), no formatting noise |
| `campfire.published.json` | Your spec exactly as served on 2026-11-14 (SHA-256 `fa138d2e57b4a9797270637e73e1aa2ad39f35b2d931d2881187db4155b03000`). The patch applies to this file |
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
| 1 | **The spec declares no authentication.** It has no `components.securitySchemes` and no `security`, on any operation. Until 2026-10-15 it declared `knoxApiToken` on all of them | Every operation (417) | Add `knoxApiToken` (`apiKey` in the `Authorization` header, prefix `Token`) and require it globally | Restore the Knox authentication extension or `SPECTACULAR_SETTINGS['SECURITY']`, so the authentication classes the views use appear in the spec |
| 2 | Response `description` is empty. OpenAPI 3.0 requires it | 302 responses | HTTP reason phrase (`OK`, `Created`, `No Content`, `Bad Request`, ...) | Give each response a description, for example with `OpenApiResponse(description=...)` |
| 3 | Response text is in `schema.description`, and the schema has no type. So the response has no description and no body shape | 7 responses (list below) | Move the text to the response `description`. The schema becomes `{"type": "object"}` | Pass the text as `OpenApiResponse(description=...)`, not as the schema |
| 4 | Operations use tags that have no global definition: `Bank Reconciliation`, `Company Objects`, `Custom Fields`, `Integrations` | 93 operations | Add the 4 tag definitions | Add them to `SPECTACULAR_SETTINGS['TAGS']` |
| 5 | Stray `coa` tag. Every related operation uses a real tag | 1 operation | `POST /coa/api/entity/{entity_id}/attachment` → `Settings` | `tags=[...]` in `extend_schema` on that view |
| 6 | No `summary` | 1 operation | "Preview Contract Minimum Commit" | Summary on `GET /rr/api/v1/contracts/{id}/minimum-commit-preview` |
| 7 | The request body has required fields, but the spec marks it optional | 21 operations (list below) | `requestBody.required: true` | Mark these bodies required |
| 8 | Nullable choice fields written as `oneOf: [XEnum, BlankEnum, NullEnum]` | 81 places | `allOf: [XEnum]` + `nullable: true` | `ENUM_ADD_EXPLICIT_BLANK_NULL_CHOICE = False` should give the same result |

Fix 8 is optional. With the `oneOf` form, Speakeasy cannot check a `default` value. For example, `vendor_type` defaults to `"vendor"` and gets a warning. Generators also turn the form into three-way union types. Our change removes `""` as an allowed value, so you decide if it fits your API.

**Fix 3, the 7 responses:**

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

After the fixes, Speakeasy still gives 0 errors, and the 518 other warnings go down to 88. These remain, and we do not think that they need a change:

| Warning | Count | Why we keep it |
| --- | --- | --- |
| Boolean `exclusiveMinimum` / `exclusiveMaximum` | 4,554 | Valid OpenAPI 3.0.3. Speakeasy expects the 3.1 number form. The bounds come from Django decimal fields and are real |
| Request body is optional | 77 operations | Their schemas have no required field (mostly `PATCH`), so an empty body is valid |
| Error responses with non-object content | 7 responses | They are free-form objects (`additionalProperties: {}`), which Speakeasy does not support. This is not a spec defect |

## Behavior the spec does not document

We use these items, or you told us about them, but the published spec does not describe them. We did not add them to our copy of the spec.

| Area | What we know | What is missing |
| --- | --- | --- |
| `GET /coa/api/payment-term` | It exists. Pedro Rodrigues named it on Slack | Not in the spec |
| `GET /coa/api/v1/amortization` | It exists. Pedro Rodrigues named it on Slack | Not in the spec. Since February 2026, the spec also no longer has `/coa/api/v1/bill/amortization` or `/coa/api/v1/bill/{bill_id}/amortization` |
| `GET /coa/api/general-ledger` parameters | It filters on `start_date` / `end_date`. `account_ids` takes one account: a comma list or a repeated parameter is ignored. It pages on `limit` / `offset`. It silently ignores `page`, `date_from` and `date_to` | The operation has no parameters in the spec |
| Rate limits | Your spec says 10 requests per second for each API user (it still said 5 on 2026-10-20). Before that change, we measured this: a 429 comes with `retry-after: 1` and the body `{"detail": "Request was throttled. Expected available in 1 second."}`. One sequential client at about 4 requests per second got 429s. 10 concurrent requests got four 429s. Successful responses have no `x-ratelimit-*` headers | No operation lists a 429 response or the `Retry-After` header |
| `GET /ca/api/draft_queue` and `/ca/api/draft_queue/{id}` | We use them to read draft invoices and journal entries (filter `created_by`, `limit` / `offset`) | Not in the spec |
| `GET /coa/api/tax_rate` | We use it to list tax rates | Not in the spec |

## Questions

1. Did the bill amortization endpoints move to `/coa/api/v1/amortization`, or did you remove them?
2. Your spec now says 10 requests per second. Before, it said 5, but one sequential client at about 4 requests per second already got 429s. Which limit applies in practice, and can the 429 response and the `Retry-After` header go into the spec?

## When you publish an update

We run `fix_spec.py` on each new version of your spec, and we send you the new patch. A fix that you adopt disappears from the patch.
