---
name: hackathon-readme
description: >
  Write product-forward hackathon README + TECH.md documentation in the ProofXI
  style: clear thesis, live app link, screenshot-led how-it-works, developer
  layout, honest constraints, TxLINE/endpoints tables. Use when the user says
  "readme like proofxi", "hackathon docs", "product-forward README", "TECH.md",
  "document the demo", or wants docs that win judges in 30 seconds.
  Triggers: /hackathon-readme, proofxi docs, submission README.
---

# Hackathon README (ProofXI-style)

Build **judge-scannable** docs. A proper working demo story beats a feature list.
Prefer one thesis + three steps + live links over exhaustive architecture.

## When to use

- Submitting to Superteam Earn / TxODDS / Colosseum-style hackathons
- README looks eng-dump, outdated URLs, or “NairaShield” leftovers
- Need a `TECH.md` for endpoints, on-chain addresses, and where data shows in UI

## Non-goals

- Do not invent screenshots, metrics, or “demo mode” claims that contradict code
- Do not document every half-feature; document the **core demo path**
- Do not put secrets in README

## Output files (minimum)

1. `README.md` — product-first (this skill’s main deliverable)
2. `TECH.md` — endpoints, thesis, layout, smoke checks
3. Optional: `DEMO_SCRIPT.md`, `SUBMISSION.md` with the **same live URLs**

## README template (structure)

```markdown
# {Product}

### {One-line product thesis — not a tech slogan.}

![hero](assets/screenshots/hero.png)

{2–4 sentences: who it's for, what autonomous loop does, chain + data source.}

**[Open the live app → {url}]({url})** · [Health/API]({api}) · [TECH.md](./TECH.md)

Built for the **{hackathon / track}**.

---

## {Contrast section title: what others claim vs what you show}

{Short paragraph. Table: does vs will not — honesty / fail-closed is a feature.}

---

## How it works

**1 — …** {Real data in — name the feed.}
**2 — …** {Decision / proof / action.}
**3 — …** {Settlement / execute / show UI.}

{Optional screenshots under each step if assets exist.}

---

## For developers

### Repo layout
### Run locally
### Deploy
### Quick smoke checks

---

## Links | Disclaimer
```

### ProofXI patterns to copy

| Pattern | Why |
| --- | --- |
| Thesis in the first screenful | Judges never scroll far |
| Live app link in bold above the fold | “Application access” requirement |
| How it works as 3 numbered beats | Maps to demo video beats |
| “Does vs will not” honesty | Production readiness + trust |
| `TECH.md` for endpoints + where they appear in UI | Earn “list TxLINE endpoints” field |
| Screenshots under `assets/screenshots/` | Product-forward, not eng-only |
| Explicit network (devnet/mainnet) + data caveats | Avoid overclaiming |

### Retegol / agent-specific honesty

- State **yield by default / trade only when Y_net clears**
- State **no fabricated odds, balances, order IDs**
- Unfunded dry-run is OK if labeled in product copy carefully — do not claim live Kamino NAV when capital is zero
- Policy in **code** (`AGENT_POLICY`), secrets in **env**

## TECH.md template

```markdown
# {Product} — technical overview

**{Thesis one-liner.}**

Track · Network · Data source

## The thesis in one line
{What is proven / enforced in code.}

## TxLINE (or primary data) endpoints used
| Purpose | Method | Endpoint |
| Where each endpoint shows up in the product |
{Bullet: UI component → Worker route → upstream API}

## On-chain / integrations table
## Agent policy / key math
## Runtime architecture + tick pipeline
## What “done” means for this track
→ link DEMO_SCRIPT.md
```

## Asset rules

1. Prefer real UI screenshots: hero, live feed, decision, settlement
2. Store under `assets/screenshots/` (committed, not only `web/public`)
3. If no screenshots yet, use `web/public/og.png` as temporary hero and note “replace with dashboard captures”
4. Never embed local absolute paths

## Process checklist

1. Read current README, live URLs (`wrangler.toml`, Vercel, Pages), and `SUBMISSION.md`
2. Identify **one core demo path** (the first working product loop)
3. Rewrite README to sell that path only
4. Write/refresh TECH.md with real endpoints from code (`rg` integrations)
5. Align DEMO_SCRIPT + SUBMISSION links with README (no stale pages.dev if on Vercel)
6. Commit docs + assets; push if user asked

## Anti-patterns (reject)

- Walls of env var dumps in README
- “NairaShield” / old product names after rebrand
- Documenting 12 routes before the live app link
- Claiming mainnet production when only dry-run works
- AI slop: “seamless”, “revolutionary”, “robust ecosystem”

## Quality bar

A stranger should answer in 30 seconds:

1. What is it?
2. Where do I click the live app?
3. What data does it use (TxLINE etc.)?
4. What is the autonomous loop?
5. Where is the deep technical write-up?
