---
name: campfire-refresh
description: Check Campfire for a new OpenAPI spec, regenerate the SDK, cut a release, and rebuild the feedback zip for Campfire (Pedro). Use when asked "is there a new spec", "refresh", "bump the SDK", "cut a release", or "update the package for Campfire/Pedro".
---

# Campfire spec refresh → release → feedback package

Campfire republishes its spec often (twice on 2026-10-15) and `info.version` stays `1.0.0`, so compare content, never the version field.

## 1. Check for a new spec (no repo changes)

Download `https://api.meetcampfire.com/api/schema/?format=json` to the scratchpad and diff it against `campfire.upstream.json`: operations added/removed (path + method), operationIds added/removed, schemas added/removed/changed, operations changed, and every other top-level key and `components` section — `info.description` carries the published rate limit (5 → 10 requests per second on 2026-10-21) and lands in the header of every generated file. Then run `python3 -I scripts/fix_spec.py <new> <out>` and compare its counts with a run on the current `campfire.upstream.json`. A step whose count drops is a fix Campfire adopted (delete that step from the script; see CLAUDE.md).

Also check the things a diff against the last spec cannot show, because they may have gone missing earlier: the new spec has `components.securitySchemes` and a `security` requirement (Campfire dropped both on 2026-10-15, and four releases sent no `Authorization` header; `fix_spec.py` step 0 now restores them). If Campfire ships its own scheme again, step 0 prints 0: delete it.

Report to the user before you change anything. Call out anything that changes SDK signatures (parameter types, operationIds → method names): that makes the release a major bump.

## 2. Regenerate and open the PR

1. `git checkout -b <branch>` off an up-to-date `main`.
2. `just refresh` (download → fix → `campfire.patch` → generate → compile). It must compile clean.
   Then `just check-auth`: every request must set the `Authorization` header (CI runs it too).
3. `git diff api.ts` to find breaking signature changes.
4. `npm version <x.y.z> --no-git-tag-version`. Major for a breaking signature change, minor for additions only.
5. Commit with `feat!:` (breaking) or `feat:`, listing what Campfire changed. Push, `gh pr create`, `gh pr checks <n> --watch`.

## 3. Merge and release

Before the merge, test against the real API: `CAMPFIRE_API_KEY=<key> just smoke-live` (read-only; it needs 200 with the key and 401 or 403 without). The user runs it, or provides the key; do not go looking for it.

The auto-mode classifier blocks `gh pr merge` ("Merge Without Review") even when the user approves in chat. Do not retry it. Ask the user to run `! gh pr merge <n> --squash --delete-branch` themselves.

After the merge: `gh workflow run release.yml -f release_notes="..."`, then `gh run watch <id> --exit-status` and `gh release view v<x.y.z>`. The workflow tags `v<package.json version>` and creates a GitHub release; it does not publish to npm.

## 4. Rebuild the feedback package for Campfire

The audience is Pedro Rodrigues at Campfire. He receives a zip, not a link.

1. Run `scripts/feedback_package.sh [out_dir]` (default `~/Desktop`). It copies `campfire.json`, `campfire.patch`, `fix_spec.py`, `campfire.upstream.json` (as `campfire.published.json`) and `feedback/README.md`, checks that the patch reproduces `campfire.json`, runs both Speakeasy lints, and prints the counts the README quotes (SHA-256, patch changed lines, `exclusiveMinimum`/`exclusiveMaximum` warnings, other warnings, optional bodies).
2. Update `feedback/README.md` with those numbers and with a "What changed since our last package" section that says what Campfire changed and which of our fixes they adopted. Rerun the script so the zip carries the new README. Commit the README.
3. Also update the Claude Doc "Campfire OpenAPI spec feedback" (https://claude.ai/code/artifact/6b2cd4f6-b741-4ab5-96a0-847cd0a36205) with the same facts. It links to `campfire.patch` and `campfire.json` on `main`, so it is only correct after the merge.
