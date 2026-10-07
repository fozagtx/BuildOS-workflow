---
name: design-promax
description: >-
  Premium React UI via HeroUI Pro + triple-axis router (theme × route × style).
  MUST ask which Pro theme first: Default | Brutalism | Glass | Mouve (unless
  user already named one). Then clean_product compose (Vault OTP / GhostKeys)
  + real Pro sources. Files: THEMES.json, STYLE_PRESETS.json, ROUTE_REGISTRY.json,
  case-studies/vault-otp.md. Showcase packs: Map navigation, Pro AI chat,
  Music player, Shopping experience. Triggers: design-promax, HeroUI, Brutalism,
  Glass, Mouve, clean_product, Vault OTP, GhostKeys, those cards, route UI.
---

# Design ProMax

Real HeroUI Pro sources. **Theme × route × style. Cap 4 source reads.**

## Theme gate (mandatory — do this first)

**Before** loading routes, reading sources, or writing UI: ask the user which HeroUI Pro theme to use, unless they already named one in the same message.

Ask exactly (or equivalent clear choice):

> Which HeroUI Pro theme should we use?
> **Default** · **Brutalism** · **Glass** · **Mouve**

| Theme | Feel | Activate (`data-theme`) | CSS import (after Pro CSS) |
|-------|------|-------------------------|----------------------------|
| **Default** | Stock HeroUI radii/shadows/type | `light` / `dark` | none |
| **Brutalism** | Sharp, thick borders, Anton + Share Tech Mono, zero radius | `brutalism-light` / `brutalism-dark` | `@heroui-pro/react/themes/brutalism` |
| **Glass** | Backdrop blur, translucent surfaces | `glass-light` / `glass-dark` | `@heroui-pro/react/themes/glass` |
| **Mouve** | Mauve/warm-purple raised accents (official spelling **Mouve**) | `mouve-light` / `mouve-dark` | `@heroui-pro/react/themes/mouve` |

Full tokens + showcase packs → **`THEMES.json`**. CSS pack → **`themes.css`** (copy into project).

**Rules:**
- Do **not** silently default a Pro theme.
- Themes **are in the skill** — apply `themes.css` + `data-theme`. Do not claim they are missing or locked behind npm when the skill pack exists.
- Import alone is not enough — set `data-theme` on `<html>` (or ancestor).
- Optional npm `@heroui-pro/react/themes/*` only if user has Pro v3 license and wants that upgrade path.
- Theme is independent of `clean_product` compose recipe (structure stays; radii/shadows/accent follow theme).

---

## Where the files are (read this first)

Agents install this skill in different layouts. **Resolve paths relative to this SKILL.md file:**

| File | Same folder as SKILL.md (flat install) | Nested repo layout |
|------|------------------------------------------|--------------------|
| **Pro themes** | `THEMES.json` + `themes.css` | `skill/THEMES.json` + `skill/themes.css` |
| Style presets | `STYLE_PRESETS.json` | `skill/STYLE_PRESETS.json` |
| Route registry | `ROUTE_REGISTRY.json` | `skill/ROUTE_REGISTRY.json` |
| Case study | `case-studies/vault-otp.md` | `skill/case-studies/vault-otp.md` |
| Routing guide | `ROUTING.md` | `skill/ROUTING.md` |
| Architecture | `ARCHITECTURE.md` | `skill/ARCHITECTURE.md` |
| HeroUI sources | `sources/` | `skill/sources/` |

**If `case-studies/vault-otp.md`, `THEMES.json`, `themes.css`, or `STYLE_PRESETS.json` is missing, the skill install is stale. Tell the user to re-run `./install.sh` from https://github.com/fozagtx/design-promax — do not invent clean_product or themes.**

### These names are real (do not claim they do not exist)

- **Pro themes:** `Default`, `Brutalism`, `Glass`, `Mouve` — **in this skill** (`THEMES.json` + `themes.css`). Copy `themes.css` into the project; set `data-theme`. Do **not** say themes require a separate npm login when the skill pack is present.
- **Style id:** `clean_product` (default), also `trust_green`, `clean_product_compact`, `marketing_campaign`, `dense_admin`, `chat_soft`
- **Case study path:** `case-studies/vault-otp.md` (layout recipe for GhostKeys / Vault OTP quality)
- **Surface H:** wallet / dapp / vault / OTP compose pack in `ROUTE_REGISTRY.json`
- **Showcase packs:** Map navigation · Pro AI chat · Music player · Shopping experience (`THEMES.json` → `showcase_packs`)

---

## Efficient protocol (mandatory)

```
0. THEME GATE — ask Default | Brutalism | Glass | Mouve (skip only if user already named one)
   Load THEMES.json + themes.css (skill pack). Copy themes.css into project. Set data-theme.
1. Load STYLE_PRESETS.json + ROUTE_REGISTRY.json (see path table above)
2. keyword_index → surface.route (also match showcase packs if user names them)
3. style → clean_product by default
   - User says like Vault OTP / GhostKeys / those cards/buttons → clean_product + read case-studies/vault-otp.md
   - Surface H → clean_product or trust_green only
4. efficient_merge (cap 4):
   core = sources/Application/cards (20)__action-card.tsx
         + sources/Application/authentication (24)__App.tsx
         + sources/Application/cards (20)__security-settings.tsx
   + optional 1 shell App from registry shell_apps
   Surface H: core only (3)
   Showcase: prefer source_hints from THEMES.json showcase_packs for that pack
5. Apply button_matrix + compose_recipe from clean_product
   — then adapt radii/shadows/accent to locked pro_theme (Brutalism ≠ pill-everything)
6. If user already has brand colors: keep them unless theme is Mouve/Brutalism and they asked for the full Pro look
7. Human copy only. No eng footnotes. No em dashes.
```

### Button matrix (from case study — Default / Glass / Mouve)

| Role | Props |
|------|--------|
| Primary | `color="primary" radius="full"` + solar bold icon |
| Secondary | `variant="bordered" radius="full" size="sm"` + linear icon |
| Danger | `color="danger" variant="flat" radius="full" size="sm"` |
| Warning | `color="warning" radius="full"` |
| Ghost | `variant="light" radius="full" size="sm"` |

**Brutalism override:** prefer sharp / `radius="none"` CTAs and thick borders; do not force soft pills.

### Compose recipe (clean_product)

Top bar → chips → hero → **3 ActionCards** → one gate card → form card → list cards → stop.

When adapting to an **existing product theme**: keep this structure; recolor using the product’s primary/bg/fonts — do not invent a new palette and do not drop the recipe. Pro theme (Brutalism/Glass/Mouve) still applies on top when chosen.

---

## Product split (mandatory — any theme)

If the product has a public story **and** a place to do the work, ship **two routes**. Do not jam them onto one page. Theme only changes radii, shadows, blur, and accent. **The split and the primitives stay.**

Read **`case-studies/landing-and-desk.md`**.

| Route | Style | Job |
|-------|-------|-----|
| `/` landing | `marketing_campaign` | Navbar (Features · How it works · Questions, no Connect) → **full** job-line hero (`text-balance`, no `<br />`) → **Features** → How it works → FAQ → footer. CTA is the product verb to `/desk`. |
| `/desk` | `clean_product` | Navbar (one Connect) → **the same full job line** → wrong-network only → form. No features/how-it-works row. |

**Hard bans in any theme:** second Connect; logo subtitle; faded `bg-clip-text` hero; chopped `<br />` that leaves three leftover words; desk h1 shortened to a 3-word stub; missing Features (Features ≠ How it works); engineering chips; fake ACME footer; invented cards.

Landing CTA is the product verb, not Connect. Desk Connect is once, labeled **Connect**. Same locked job line on every page that has a hero.

---

## Showcase packs (quality targets)

When the user points at heroui.pro demos, map intent → pack → sources (`THEMES.json`):

| Pack | What it looks like |
|------|--------------------|
| **Map navigation** | Near/distance, Open/Closed hours, Pick-up / Delivery place cards |
| **Pro AI chat** | Structured answer, Sources / Deep search, Ask-anything composer |
| **Music player** | Artwork queue, now playing, track rows |
| **Shopping experience** | Product, price, size selector, PDP |

Still run the **theme gate** before building.

---

## Stack

React 18 + `@heroui/react` v2 (+ `@heroui-pro/react` when available) + Tailwind 3 + Framer Motion + `@iconify/react` (`solar:`)

---

## Rules

1. **Theme gate first** — ask Default / Brutalism / Glass / Mouve before composing  
2. Dual-axis route + style after theme is locked  
3. Max **4** source reads  
4. Prefer **clean_product** compose unless campaign landing or dense admin  
5. Read `case-studies/vault-otp.md` when user wants that feel  
6. Never invent icons; never claim clean_product / themes / case-studies are missing without checking both path layouts  
7. Never put architecture notes in product UI  
