// Offline proof that the built SDK authenticates. Runs in CI on the committed dist/.
//
// From v2.0.0 to v5.0.0 Campfire's spec declared no security scheme, so the generator wrote no
// Authorization header anywhere and `Configuration.apiKey` was silently ignored. Nothing failed
// until a real call came back 401. This check fails the build instead.
//
//   node scripts/check-auth.mjs

import { readFileSync } from 'node:fs';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const { CompanyObjectsApi, Configuration } = require('../dist/index.js');

const failures = [];

// 1. Every generated request builder sets the Authorization header.
const api = readFileSync(new URL('../dist/api.js', import.meta.url), 'utf8');
const builders = api.match(/const localVarHeaderParameter = \{\};/g)?.length ?? 0;
const authed = api.match(/setApiKeyToObject\)\(localVarHeaderParameter, "Authorization", configuration\)|setApiKeyToObject\(localVarHeaderParameter, "Authorization", configuration\)/g)?.length ?? 0;
if (builders === 0) failures.push('found no request builders in dist/api.js');
if (authed !== builders) failures.push(`${authed} of ${builders} request builders set the Authorization header`);

// 2. A real call through the SDK puts the key on the wire. A stub adapter answers instead of
//    the network, so this needs no credentials.
let sent;
const axios = require('axios').create({
  adapter: async (config) => {
    sent = config.headers;
    return { data: [], status: 200, statusText: 'OK', headers: {}, config };
  },
});
const client = new CompanyObjectsApi(new Configuration({ apiKey: 'Token check-auth' }), undefined, axios);
await client.coaApiDepartmentList();
const header = sent?.Authorization ?? sent?.authorization;
if (header !== 'Token check-auth') failures.push(`request carried Authorization=${JSON.stringify(header)}, expected "Token check-auth"`);

if (failures.length) {
  for (const f of failures) console.error(`check-auth: ${f}`);
  process.exit(1);
}
console.log(`check-auth: all ${builders} request builders set Authorization, and a call sends it.`);
