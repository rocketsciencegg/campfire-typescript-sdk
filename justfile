# Per-repo configuration
sdk_name := "campfire-typescript-sdk"
spec_file := "campfire.json"
upstream_file := "campfire.upstream.json"
spec_url := "https://api.meetcampfire.com/api/schema/?format=json"

# Show available commands
help:
    @just --list

# Install system dependencies (macOS)
install:
    brew install openjdk

# Remove build output
clean:
    rm -rf dist

# Download Campfire's published spec, untouched, to campfire.upstream.json
fetch-spec:
    curl -fsSL -o {{ upstream_file }} "{{ spec_url }}"

# Apply our fixes (scripts/fix_spec.py) to the upstream spec, writing campfire.json
fix-spec:
    python3 scripts/fix_spec.py {{ upstream_file }} {{ spec_file }}

# Write campfire.patch: every change we make to Campfire's spec, as a patch they can apply
spec-diff:
    diff -u --label campfire.upstream.json --label campfire.json {{ upstream_file }} {{ spec_file }} > campfire.patch || [ $? -eq 1 ]

# Lint campfire.json with Speakeasy (brew install speakeasy-api/homebrew-tap/speakeasy)
lint-spec:
    speakeasy lint openapi --non-interactive --max-validation-warnings 0 --max-validation-errors 0 -s {{ spec_file }}

# Refresh from Campfire: download, fix, regenerate and compile
refresh: fetch-spec fix-spec spec-diff build

# Generate SDK from OpenAPI spec and compile TypeScript
build:
    #!/usr/bin/env bash
    set -euo pipefail
    if [ ! -f "{{ spec_file }}" ]; then
        echo "Error: {{ spec_file }} not found"
        exit 1
    fi
    echo "Generating {{ sdk_name }} from OpenAPI spec..."
    export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"
    npx @openapitools/openapi-generator-cli generate \
        -i {{ spec_file }} \
        -g typescript-axios \
        -o . \
        --additional-properties=npmName={{ sdk_name }},modelPropertyNaming=camelCase,useSingleRequestParameter=true
    # The generator never deletes docs for models that no longer exist.
    comm -23 <(ls docs | sed 's#^#docs/#' | sort) <(grep '^docs/' .openapi-generator/FILES | sort) | xargs rm -f
    echo "Compiling TypeScript..."
    npx tsc

# Compile TypeScript only (no regeneration)
compile:
    npx tsc
