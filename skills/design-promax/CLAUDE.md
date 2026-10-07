# CLAUDE.md

## About This Repo

Design ProMax — HeroUI Pro **real sources** + **Pro themes** + **route registry** + **style presets**.  
Canonical product quality: **clean_product** / **Vault OTP** case study (GhostKeys-class UI).

## Files agents must find

Relative to skill root (after install, files are **also flattened** to skill root):

| What | Path |
|------|------|
| Entry | `SKILL.md` |
| **Pro themes** | `THEMES.json` + `themes.css` → Default · Brutalism · Glass · Mouve |
| Styles | `STYLE_PRESETS.json` → id **`clean_product`** |
| Routes | `ROUTE_REGISTRY.json` |
| Case study | `case-studies/vault-otp.md` |
| Sources | `sources/` or `skill/sources/` |

If any of those are missing, **reinstall** with `./install.sh ~/.claude/skills` — do not invent them.

## How Agents Use This

1. Load `SKILL.md`
2. **THEME GATE** — ask **Default · Brutalism · Glass · Mouve** (unless user already named one). Load `THEMES.json` + copy **`themes.css`** into the project.
3. Load `STYLE_PRESETS.json` + `ROUTE_REGISTRY.json`
4. Match intent → surface + route (showcase packs: Map navigation, Pro AI chat, Music player, Shopping)
5. Style → **`clean_product`** by default (or `trust_green` / `chat_soft` / …)
6. For “like Vault OTP / GhostKeys / those cards”: read **`case-studies/vault-otp.md`**
7. Efficient merge: 3 core files (+ 1 shell App max) = **4 reads**
8. Apply **button_matrix** (pill primary / bordered secondary / flat danger) — Brutalism uses sharp corners
9. Wire `data-theme` from `THEMES.json` using skill **`themes.css`**
10. If user has brand colors: keep them unless they asked for full Brutalism / Glass / Mouve look

## Do not

- Pick a Pro theme silently — always ask first  
- Claim themes are missing / need npm login when `THEMES.json` + `themes.css` exist in the skill  
- Claim `clean_product`, `THEMES.json`, or `case-studies/` do not exist without checking both root and `skill/` paths  
- Browse all of `sources/` randomly  
- Put eng jargon in product UI  
