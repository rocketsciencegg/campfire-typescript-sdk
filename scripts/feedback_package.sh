#!/usr/bin/env bash
# Build the zip we send Campfire: our patch, both specs, the fix script, both
# Speakeasy lint reports, and feedback/README.md. Prints the counts the README
# quotes, so you can update it before you send the zip.
#
# Usage: scripts/feedback_package.sh [out_dir]   (default: ~/Desktop)
set -euo pipefail

root=$(cd "$(dirname "$0")/.." && pwd)
out_dir=${1:-$HOME/Desktop}
name="campfire-spec-feedback-$(date +%Y-%m-%d)"
work=$(mktemp -d)
pkg="$work/$name"
mkdir -p "$pkg"

cp "$root/campfire.json" "$root/campfire.patch" "$root/scripts/fix_spec.py" "$root/feedback/README.md" "$pkg/"
cp "$root/campfire.upstream.json" "$pkg/campfire.published.json"

# The patch must turn their file into ours, byte for byte
cp "$pkg/campfire.published.json" "$work/check.json"
patch -s "$work/check.json" "$pkg/campfire.patch"
cmp -s "$work/check.json" "$pkg/campfire.json" || { echo "campfire.patch does not reproduce campfire.json" >&2; exit 1; }

# Speakeasy caps output at 1000 warnings and colours it; lift the cap, strip the colour
lint() {
    speakeasy lint openapi --non-interactive --max-validation-warnings 0 --max-validation-errors 0 -s "$1" 2>&1 \
        | sed -E $'s/\x1b\\[[0-9;]*m//g' \
        | grep -E '^(INFO|WARN|ERROR) |linting complete' || true
}
lint "$pkg/campfire.published.json" > "$pkg/speakeasy-lint-published.txt"
lint "$pkg/campfire.json" > "$pkg/speakeasy-lint-fixed.txt"

echo "SHA-256 of campfire.published.json: $(shasum -a 256 "$pkg/campfire.published.json" | cut -d' ' -f1)"
echo "patch changed lines: $(grep -E '^[+-]' "$pkg/campfire.patch" | grep -cvE '^(\+\+\+|---) ')"
for n in published fixed; do
    f="$pkg/speakeasy-lint-$n.txt"
    total=$(sed -nE 's/.*([0-9]+) errors, ([0-9]+) warnings.*/\2/p' "$f")
    excl=$(grep '^WARN' "$f" | grep -ciE 'exclusiveM(in|ax)imum' || true)
    echo "$n: $(tail -1 "$f" | sed 's/OpenAPI document linting complete. //') | exclusive=$excl | other warnings=$((total - excl)) | optional bodies=$(grep -c 'request body is optional' "$f" || true)"
done

(cd "$work" && zip -qr -X "$name.zip" "$name")
mv "$work/$name.zip" "$out_dir/"
echo "wrote $out_dir/$name.zip"
