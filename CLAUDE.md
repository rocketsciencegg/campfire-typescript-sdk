# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Auto-generated TypeScript SDK for the [Campfire API](https://api.meetcampfire.com) (accounting, AP/AR, revenue recognition, and financial reporting). Generated from an OpenAPI spec (`campfire.json`) using OpenAPI Generator v7.19.0 with the `typescript-axios` template. Uses Axios as the HTTP client.

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
| `api.ts` | `DefaultApi` class with all API methods (the main SDK surface) |
| `configuration.ts` | `Configuration` class for auth setup (API key) |
| `base.ts` | `BaseAPI` base class, `RequiredError`, server config |
| `common.ts` | Internal utilities (auth, serialization, request helpers) |
| `index.ts` | Re-exports from `api.ts` and `configuration.ts` |

**Key files that are NOT auto-generated:**
- `justfile` — build/generation orchestration
- `campfire.json` — OpenAPI spec (source of truth for the SDK)
- `.openapi-generator-ignore` — controls which files the generator preserves
- `.github/` — CI/CD workflows and Dependabot config
- `LICENSE` — MIT license

## SDK Usage Patterns

Authentication uses API key via `Configuration.apiKey` with the `Token` prefix. The key is sent in the `Authorization` header.

```typescript
import { DefaultApi, Configuration } from 'campfire-typescript-sdk';

const config = new Configuration({ apiKey: `Token ${process.env.CAMPFIRE_API_KEY}` });
const api = new DefaultApi(config);

const accounts = await api.listAccounts({ limit: 50 });
```

All methods follow the pattern: `api.methodName(params?, axiosOptions?)` returning `Promise<AxiosResponse<T>>`.

## Key Conventions

- Entity IDs are numbers
- API categories: Cash Management (accounts, bank transactions), Core Accounting (chart of accounts, journal entries, entities, departments, tags, general ledger), Accounts Payable (bills, vendors, credit/debit memos), Accounts Receivable (invoices), Revenue Recognition (contracts, subscriptions, milestones, products), Financial Statements (balance sheet, income statement, cash flow, trial balance), Bank Reconciliation, Integrations (webhooks), Custom Fields, Fixed Assets
- See `docs/` for the full method reference
