# campfire-typescript-sdk

> **This is a public, open source repository.** Contributions and issues welcome.

TypeScript SDK for the [Campfire API](https://api.meetcampfire.com) (accounting, AP/AR, revenue recognition, and financial reporting), auto-generated from OpenAPI spec.

## Installation

Requires Node.js **>= 22.13.0** — the oldest non-EOL Node this package supports, enforced by
`engines` in `package.json`. That is a compatibility floor for consumers; the SDK itself is built
and released on the exact Node version pinned in `.node-version`.

```bash
pnpm add github:rocketsciencegg/campfire-typescript-sdk
```

Pin a specific version:

```bash
pnpm add github:rocketsciencegg/campfire-typescript-sdk#v1.0.0
```

## Quick Start

```typescript
import { CashManagementApi, Configuration } from 'campfire-typescript-sdk';

const config = new Configuration({ apiKey: `Token ${process.env.CAMPFIRE_API_KEY}` });
const cashMgmt = new CashManagementApi(config);

const accounts = await cashMgmt.listAccounts({ limit: 50 });
console.log(accounts.data);
```

## Authentication

All API calls require an API key passed via `Configuration.apiKey` with the `Token` prefix (e.g. `Token your-api-key-here`). The key is sent in the `Authorization` header.

## API Classes

The SDK is organized into 11 API classes by category:

| Class | Description |
|-------|-------------|
| `CashManagementApi` | Bank accounts and bank transactions |
| `AccountsPayableApi` | Bills, debit memos, bill payments |
| `AccountsReceivableApi` | Invoices, credit memos, invoice payments |
| `CoreAccountingApi` | Journal entries, budgets, fixed assets, vendor contacts |
| `CompanyObjectsApi` | Chart of accounts, departments, vendors, tags, cost allocations |
| `RevenueRecognitionApi` | Contracts, subscriptions, milestones, products |
| `FinancialStatementsApi` | Balance sheet, income statement, cash flow, trial balance, general ledger |
| `BankReconciliationApi` | Reconciliation reports and transaction matching |
| `SettingsApi` | Entities, currencies, files, chart account settings |
| `IntegrationsApi` | Webhooks |
| `CustomFieldsApi` | Custom field definitions |

All methods follow the pattern `api.methodName(params?, axiosOptions?)` returning `Promise<AxiosResponse<T>>`.

## API Reference

See the [generated docs](docs/) for all available methods and models, or the [Campfire API reference](https://docs.campfire.ai/api-reference).

## Contributing

This repo uses pnpm. Install dependencies from the lockfile, then compile:

```bash
pnpm install --frozen-lockfile
pnpm run build
```

## How This SDK Is Generated

Generated from `campfire.json` using [OpenAPI Generator](https://openapi-generator.tech/) v7.19.0 (`typescript-axios`).

```bash
just install     # System deps (Java)
just refresh     # Download Campfire's spec, apply our fixes, regenerate + compile
just build       # Regenerate + compile from campfire.json
just lint-spec   # Lint campfire.json with Speakeasy
just compile     # TypeScript only
```

`campfire.upstream.json` is Campfire's published spec exactly as downloaded. `campfire.json` is that spec after `scripts/fix_spec.py`, which fixes validation problems (empty response descriptions, undefined tags, nullable enums) and fills a few missing summaries. Each fix in the script says why it exists, and `campfire.patch` (`just spec-diff`) is the full set of changes, as a patch Campfire can apply to their own copy.

## Generated Files

All `.ts` source files and `docs/` are auto-generated. Do not edit manually.
Custom files (README, justfile, .github/, CLAUDE.md) are protected via `.openapi-generator-ignore`.

## License

[MIT](LICENSE)
