# campfire-typescript-sdk

> **This is a public, open source repository.** Contributions and issues welcome.

TypeScript SDK for the [Campfire API](https://api.meetcampfire.com) (accounting, AP/AR, revenue recognition, and financial reporting), auto-generated from OpenAPI spec.

## Installation

```bash
npm install github:rocketsciencegg/campfire-typescript-sdk
```

Pin a specific version:

```bash
npm install github:rocketsciencegg/campfire-typescript-sdk#v1.0.0
```

## Quick Start

```typescript
import { DefaultApi, Configuration } from 'campfire-typescript-sdk';

const config = new Configuration({ apiKey: `Token ${process.env.CAMPFIRE_API_KEY}` });
const api = new DefaultApi(config);

const accounts = await api.listAccounts({ limit: 50 });
console.log(accounts.data);
```

## Authentication

All API calls require an API key passed via `Configuration.apiKey` with the `Token` prefix (e.g. `Token your-api-key-here`). The key is sent in the `Authorization` header.

All methods follow the pattern `api.methodName(params?, axiosOptions?)` returning `Promise<AxiosResponse<T>>`.

## API Reference

See the [generated docs](docs/) for all available methods and models.

## How This SDK Is Generated

Generated from `campfire.json` using [OpenAPI Generator](https://openapi-generator.tech/) v7.19.0 (`typescript-axios`).

```bash
just install   # System deps (Java)
just build     # Regenerate + compile
just compile   # TypeScript only
```

## Generated Files

All `.ts` source files and `docs/` are auto-generated. Do not edit manually.
Custom files (README, justfile, .github/, CLAUDE.md) are protected via `.openapi-generator-ignore`.

## License

[MIT](LICENSE)
