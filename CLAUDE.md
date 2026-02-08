# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Auto-generated TypeScript SDK for the [Campfire API](https://api.meetcampfire.com) (accounting, AP/AR, revenue recognition, and financial reporting). Generated from an OpenAPI spec (`campfire.json`) using OpenAPI Generator v7.19.0 with the `typescript-axios` template. Uses Axios as the HTTP client. API docs at https://docs.campfire.ai/api-reference.

## Build Commands

```bash
npm install            # Install dependencies (also runs build via prepare hook)
npm run build          # Compile TypeScript to dist/
just build             # Full regeneration: generate SDK from campfire.json OpenAPI spec + compile
just compile           # Compile TypeScript only (no regeneration)
just install           # Install system dependencies (openjdk via Homebrew)
just clean             # Remove dist/ directory
```

There are **no tests, linting, or formatting** configured. Source files contain `/* tslint:disable */` / `/* eslint-disable */` markers from the generator.

## Architecture

All TypeScript source files in the root directory are **auto-generated** from the OpenAPI spec. Do not manually edit these files — changes will be overwritten on next `just build`.

| File | Purpose |
|------|---------|
| `api.ts` | 12 API classes organized by category (see below), plus all model types |
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
- `CoaApi` — fixed asset automation, bill amortization, transaction merging

**Key files that are NOT auto-generated:**
- `justfile` — build/generation orchestration
- `campfire.json` — OpenAPI spec (source of truth for the SDK, downloaded from `https://api.meetcampfire.com/api/schema?format=json` with fixes applied)
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
