# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Auto-generated TypeScript SDK for the [Campfire API](https://api.meetcampfire.com) (accounting, AP/AR, revenue recognition, and financial reporting). Generated from an OpenAPI spec (`campfire.json`) using OpenAPI Generator v7.19.0 with the `typescript-axios` template. Uses Axios as the HTTP client. API docs at https://docs.campfire.ai/api-reference.

## Build Commands

```bash
npm install            # Install dependencies (also runs build via prepare hook)
npm run build          # Compile TypeScript to dist/
just refresh           # Download Campfire's spec, apply scripts/fix_spec.py, write campfire.patch, regenerate + compile
just build             # Full regeneration: generate SDK from campfire.json OpenAPI spec + compile
just lint-spec         # Speakeasy lint of campfire.json
just compile           # Compile TypeScript only (no regeneration)
just install           # Install system dependencies (openjdk via Homebrew)
just clean             # Remove dist/ directory
```

There are **no tests, linting, or formatting** configured. Source files contain `/* tslint:disable */` / `/* eslint-disable */` markers from the generator.

## Architecture

All TypeScript source files in the root directory are **auto-generated** from the OpenAPI spec. Do not manually edit these files — changes will be overwritten on next `just build`.

| File | Purpose |
|------|---------|
| `api.ts` | 11 API classes organized by category (see below), plus all model types |
| `configuration.ts` | `Configuration` class for auth setup (API key) |
| `base.ts` | `BaseAPI` base class, `RequiredError`, server config |
| `common.ts` | Internal utilities (auth, serialization, request helpers) |
| `index.ts` | Re-exports from `api.ts` and `configuration.ts` |

**API classes in `api.ts`:**
- `CashManagementApi` — bank accounts and bank transactions
- `AccountsPayableApi` — bills, debit memos, bill payments
- `AccountsReceivableApi` — invoices, credit memos, invoice payments
- `CoreAccountingApi` — journal entries, budgets, fixed assets, vendor contacts
- `CompanyObjectsApi` — chart of accounts, departments, vendors, tags, cost allocations
- `RevenueRecognitionApi` — contracts, subscriptions, milestones, products
- `FinancialStatementsApi` — balance sheet, income statement, cash flow, trial balance, general ledger
- `BankReconciliationApi` — reconciliation reports and transaction matching
- `SettingsApi` — entities, currencies, files, chart account settings
- `IntegrationsApi` — webhooks
- `CustomFieldsApi` — custom field definitions

**Key files that are NOT auto-generated:**
- `justfile` — build/generation orchestration
- `campfire.upstream.json` — Campfire's published spec, untouched (`just fetch-spec`, from `https://api.meetcampfire.com/api/schema/?format=json`)
- `campfire.json` — the spec the SDK is generated from: `campfire.upstream.json` after `scripts/fix_spec.py`. Never hand-edit it; add a named step to the script, so the next refresh keeps the fix
- `campfire.patch` — `diff -u campfire.upstream.json campfire.json`, written by `just spec-diff`. This is what we send Campfire
- `scripts/fix_spec.py` — every fix we apply to Campfire's spec, each with its reason and a count of what it touched. A step that touches nothing after a refresh is a fix Campfire adopted; delete it

Speakeasy lint (`just lint-spec`) gives 0 errors. The warnings left are expected: boolean `exclusiveMinimum`/`exclusiveMaximum` (valid OAS 3.0.3; Speakeasy wants the 3.1 form), optional request bodies whose schema has no required field, and free-form error objects Speakeasy does not support.
- `.openapi-generator-ignore` — controls which files the generator preserves
- `.github/` — CI/CD workflows and Dependabot config
- `LICENSE` — MIT license

## SDK Usage Patterns

Authentication uses API key via `Configuration.apiKey` with the `Token` prefix. The key is sent in the `Authorization` header.

```typescript
import { CashManagementApi, CoreAccountingApi, Configuration } from 'campfire-typescript-sdk';

const config = new Configuration({ apiKey: `Token ${process.env.CAMPFIRE_API_KEY}` });

const cashMgmt = new CashManagementApi(config);
const accounts = await cashMgmt.listAccounts({ limit: 50 });

const accounting = new CoreAccountingApi(config);
const entries = await accounting.coaApiJournalEntryList({ limit: 20 });
```

All methods follow the pattern: `api.methodName(params?, axiosOptions?)` returning `Promise<AxiosResponse<T>>`.

## Key Conventions

- Entity IDs are numbers, dates are ISO 8601 `YYYY-MM-DD`
- Most list endpoints support `include_deleted=true` for soft-deleted records (returns ONLY deleted records with minimal data)
- Bulk search endpoints (POST) accept exact-match arrays optimized for performance; some support upsert
- Double-entry bookkeeping: journal entry endpoints validate that total debits equal total credits
- Multi-currency: bills, invoices, credit/debit memos, and journal entries support exchange rate handling
- Void/reopen workflow: bills, invoices, credit memos, debit memos all support void (creates reversing JE) and reopen
- Closed book periods: journal entries cannot be created/updated/deleted before closed book dates
- See `docs/` for the full method reference
