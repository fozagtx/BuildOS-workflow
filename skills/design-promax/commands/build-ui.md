# Build UI Component

## Command
`build-ui`

## Description
Build a React UI component or page using Design ProMax. **Routes first** via `ROUTE_REGISTRY.json`, then reads only the listed primary sources.

## Usage
```
build-ui --intent <keyword> --name <component-name> [options]
# or legacy:
build-ui --type <category> --name <component-name>
```

### Options
- `--intent` — Product intent keyword: `landing`, `login`, `dashboard`, `chat`, `checkout`, `wallet`, `vault`, `pricing`, …
- `--type` — Legacy category: `ai`, `application`, `charts`, `ecommerce`, `marketing` (mapped via registry surfaces)
- `--name` — Component name (e.g. `pricing-page`, `login-form`, `vault-otp`)
- `--output` — Output file path (optional)

## Workflow
1. Open `skill/ROUTE_REGISTRY.json`
2. Resolve `keyword_index[intent]` → surface + route (or classify from keywords)
3. Read **only** that route’s `primary[]` files under `skill/sources/`
4. Extract patterns: structure, tokens, icon names from opened files
5. Build component; enforce `quality_bar`
6. Output React with `"use client"`, `forwardRef`, `cn()` where reusable

## Examples
```
build-ui --intent pricing --name pricing-page --output ./components/pricing.tsx
build-ui --intent login --name login-form --output ./components/auth/login.tsx
build-ui --intent wallet --name vault-shell --output ./components/VaultApp.tsx
```

## Validate
```
node scripts/validate-routes.mjs
```
