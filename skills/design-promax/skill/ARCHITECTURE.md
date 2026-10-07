# Design ProMax — Harness Architecture v2

## Problem this solves

| Failure mode | Cause | Fix |
|--------------|--------|-----|
| Agent opens 20 random source files | Flat lookup table + huge FILE_INDEX | **Route registry** → max 5 merged reads |
| UI looks random across projects | No shared “feel” | **STYLE_PRESETS** default `clean_product` |
| Wrong Pro aesthetic | Silent Default | **THEMES.json** gate — ask Default/Brutalism/Glass/Mouve |
| Wrong template for the product | Keyword match only on category (AI/App/Marketing) | **Surface A–H** + **route id** |
| Glob paths that don’t resolve | `sidebar*.tsx` in docs | **Exact paths** in JSON |
| Eng jargon in UI | No copy rule | Quality bar + surface H avoid list |
| Harness can’t machine-route | Markdown-only tables | `ROUTE_REGISTRY.json` |
| Install layout differs | Root vs `skill/` entry | Protocol uses paths relative to `skill/` |

## Layers

```
┌─────────────────────────────────────────────────────────┐
│  SKILL.md          Trigger + short protocol (always)    │
├─────────────────────────────────────────────────────────┤
│  THEMES.json           Pro theme gate (Default/Brutalism│
│                        /Glass/Mouve) + showcase packs   │
│  ROUTE_REGISTRY.json   Machine routes (what)             │
│  STYLE_PRESETS.json    Compose feel — clean_product     │
│  ROUTING.md            Human narrative / examples       │
│  ARCHITECTURE.md       This file — harness contract     │
├─────────────────────────────────────────────────────────┤
│  sources/**            Real HeroUI Pro code (read-only) │
├─────────────────────────────────────────────────────────┤
│  rules/ + commands/    Integrity + build-ui workflow    │
└─────────────────────────────────────────────────────────┘
```

## Harness contract (any agent runtime)

### 1. Entry

On UI work, load:

1. `skill/SKILL.md` (or installed copy of SKILL.md)
2. **Ask Pro theme** (Default · Brutalism · Glass · Mouve) unless already named → load `THEMES.json`
3. `skill/ROUTE_REGISTRY.json`

Do **not** start by listing all of `sources/`.

**Also load** `STYLE_PRESETS.json`. Default compose = **`clean_product`** (Vault OTP cards).
Merge route primaries with `style.must_read` (cap 5). Surface **H** locks clean_product.
See STYLE_PRESETS `compose_recipe` for the topbar → action cards → gate → content order.
Apply locked Pro theme (`data-theme` + CSS import or `oss_approx`).

### 2. Classify

```
user_utterance
  → keyword_index match (first hit wins)
  → OR classify surface A–H from surfaces.*.keywords
  → pick default route under that surface if multi-route
```

Output a **route plan** (even if only internal):

```json
{
  "surface": "H",
  "route": "vault_or_dapp_shell",
  "style": "clean_product",
  "files_to_read": ["… max 5 …"],
  "compose_recipe": ["topbar", "hero", "3 action cards", "gate", "content"],
  "avoid": ["…"]
}
```

### 3. Read

- Merge `route.primary` ∪ `style.must_read` (dedupe, prefer `.tsx`)
- Cap at **5** files
- Open `secondary` only if still missing an atom

### 4. Adapt

- Follow **style.compose_recipe** (Vault OTP layout order)
- Copy structure, tokens, icon names from opened files
- Enforce `quality_bar[]` + style `copy_rules`

### 5. Refuse

If asked to “use all components” or dump FILE_INDEX into one page: refuse, re-route.

## File responsibilities

| File | Consumer | Mutable |
|------|----------|---------|
| `ROUTE_REGISTRY.json` | Harness / scripts | Yes (versioned) |
| `STYLE_PRESETS.json` | Feel / Vault quality | Yes |
| `ROUTING.md` | Humans / long reasoning | Yes |
| `SKILL.md` | Skill trigger | Yes (keep thin) |
| `sources/**` | Pattern library | Rarely |
| `scripts/validate-routes.mjs` | CI / local | Yes |

## Install layout

Repo layout:

```
design-promax/
  skill/
    SKILL.md
    ROUTING.md
    ARCHITECTURE.md
    ROUTE_REGISTRY.json
    STYLE_PRESETS.json
    sources/
```

Claude installers may flatten to `~/.claude/skills/design-promax/`.  
**Paths in the registry stay relative to `sources/`**, not the install root.  
Harness should resolve: `join(skillRoot, "sources", registryPath)` or `join(skillRoot, registryPath)` if already under sources.

## Validation

```bash
node skill/scripts/validate-routes.mjs
# or from repo root:
node scripts/validate-routes.mjs
```

Fails if any `primary` / `secondary` / `field_router` path is missing.

## Versioning

- Bump `ROUTE_REGISTRY.json` `version` on route changes
- Keep SKILL description in sync with new surfaces
