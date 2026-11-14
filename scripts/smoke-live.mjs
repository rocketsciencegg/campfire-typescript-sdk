// Live check against Campfire's real API before a release. Read-only: one GET with the key,
// one GET without it. Needs CAMPFIRE_API_KEY (the bare key, without the "Token " prefix).
//
//   CAMPFIRE_API_KEY=... node scripts/smoke-live.mjs

import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const { CompanyObjectsApi, Configuration } = require('../dist/index.js');

const key = process.env.CAMPFIRE_API_KEY;
if (!key) {
  console.error('smoke-live: CAMPFIRE_API_KEY is not set');
  process.exit(2);
}

async function status(configuration) {
  try {
    const res = await new CompanyObjectsApi(configuration).coaApiDepartmentList();
    const rows = Array.isArray(res.data) ? res.data.length : (res.data?.results?.length ?? '?');
    return { status: res.status, rows };
  } catch (err) {
    return { status: err.response?.status ?? err.code ?? String(err) };
  }
}

const withKey = await status(new Configuration({ apiKey: `Token ${key}` }));
const withoutKey = await status(new Configuration({}));
console.log(`smoke-live: with key -> ${withKey.status} (${withKey.rows ?? 0} departments); without key -> ${withoutKey.status}`);

if (withKey.status !== 200) {
  console.error('smoke-live: FAIL — the SDK did not authenticate');
  process.exit(1);
}
if (withoutKey.status !== 401 && withoutKey.status !== 403) {
  console.error('smoke-live: FAIL — a call without a key was not rejected, so this check proves nothing');
  process.exit(1);
}
console.log('smoke-live: pass');
