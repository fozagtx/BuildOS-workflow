---
name: bypass-slop
description: >
  Full-session anti-slop skill (UI + agent + auth + git + local dev) distilled from a long
  NairaShield-style build (~10h of corrections). Use when shipping product UI, landing pages,
  dashboards, Cloudflare agents, Google auth, brand marks, or configs. Blocks mock metrics,
  demo modes, eng-jargon copy, sticky glass nav, landing-as-dashboard scroll nav, em dashes,
  product-photo bento junk, AI commit trailers, env-stored product policy, stress-stack
  overlays, and Real Talk copy pivots (truth is / not just X / let’s break it down).
  Triggers: /bypass-slop, bypass-slop, anti-slop, no mocks, real metrics only,
  PAS copy, hero-only bg, design-promax without slop, don't invent, dashboard app not landing.
  Apply proactively on greenfield product work when the user values honesty and craft.
  Scope: multi-harness user skill (~/.agents/skills, symlinked for Claude/Codex/Cursor/Grok).
---

# Bypass Slop (full session canon)

You are not allowed to “look finished” by lying. Prefer empty, honest, or blocked over fake.

This skill aggregates **all major corrections** from a multi-hour product session (landing → ProMax polish → agent backend → auth → dashboard shell → logo). Use it as a gate before and during implementation.

---

## 0. Operating principles

1. **Read product truth first** — PRD, research, handoff, existing UI constraints. Match strategy (e.g. market making, not arb against consensus).
2. **User corrections are permanent law** for the session and this skill. Do not reintroduce fixed mistakes.
3. **One product root** — do not nest a new repo or parallel scaffold next to the real app.
4. **Do not invent** metrics, waitlist pressure, GitHub social proof, balances, odds, or commit essay bodies the user did not request.
5. **Measure twice** — destructive git, force-push, or deleting “extra” sections without re-reading the ask is how How-it-works/FAQ got wrongly nuked.
6. **User owns terminals** when they say so — free ports; don’t fight them for `npm run dev`.

---

## 1. Data honesty — absolute no mocks

| Forbidden | Required |
|-----------|----------|
| Mock/demo chart fallbacks | Real agent ticks only; empty state when offline |
| Invented KPIs / TVL / user counts on marketing | Copy without fake social proof |
| `chart-demo`, seeded graphs | Delete; dashboards show “-” / empty labels |
| Demo TxLINE catalogs, virtual 1000 USDC, `demo_order_*` | Real API or HOLD/Error with **specific** reason |
| Synthetic settlement PnL | Only when venue confirms settlement |
| Ephemeral wallets pretending to be funded | Real key or refuse on-chain path |
| `AGENT_DEMO_MODE` auto-on | Missing keys → `not_ready`, never fake-ready |

**Empty is a feature.** Unconnected agent = honest empty charts, not sample series.

---

## 2. Landing page (marketing) rules

### Atmosphere & background
- **Hero-only atmospheric bg** (`bg.jpg` or equivalent). Not full-page wash from under the nav; not on the dashboard.
- Background must **not** ruin text contrast (no washed-out type over photo).
- **Header / nav is not the bg layer** — chrome sits clean; hero owns the atmosphere.

### Header / nav
- Prefer **header-base** (solid chrome), **not** sticky glass glued to the top unless the user asks sticky.
- Floating bar pattern (when used): **rectangular**, **`rounded-xl`**, **visible border**, not a huge spacious pill.
- Primary CTA: **Get started** / dashboard entry — not waitlist-first unless product still wants waitlist.
- **No Product nav** junk links if the product doesn’t have a product page.
- Short hero: don’t bloat the above-the-fold with section eyebrows like “Problem”.

### Sections to keep vs kill
- **Keep** How it works, FAQ, Need help (unless user truly wants them gone).
- **Remove** waitlist when told — but **do not** delete How/FAQ/Help in the same sweep by assumption.
- **No** product-photo bento grids or decorative image spam (user oscillated: no useless SVGs → tried images → remove images again). Default: **no junk imagery**.
- **No GitHub** (or other empty social) in footer just to fill columns.

### Marquee / “Built on”
- ProMax-style **scrolling brand marquee** for stack (Solana, Kamino, BetDEX, CF, USDC…).
- Marquee sits in hero context; **transparent** — no separate colored band fighting the hero.
- Real brand SVGs in `public/brands/`; no generic icon soup.

### Copy (PAS + plain language)
- **PAS** (Problem → Agitation → Solution) without contrast-slop and without eng jargon.
- **No em dashes** (—). Rephrase with commas, periods, or parentheses.
- No shield/warrior icon metaphor spam; product is capital + yield + agent, not a video game crest.
- Light mode **default**.

### Real Talk (banned openers / pivots)
LLM “real talk” cadence. Sounds earnest; says nothing. **Ban in product UI, README, TECH.md, landing, commits, and agent chat.** State the claim. Skip the wind-up.

| Banned pattern | Why it dies |
|----------------|-------------|
| **Not… Not… Not…** (triple-neg stack) | Fake rhythm; list what *is* true instead |
| “It’s not just X. It’s Y.” | Contrast-slop dual frame |
| “This isn’t about X. It’s about Y.” | Same dual frame with moral tone |
| “But here’s the thing.” | Fake intimacy before a banal point |
| “The truth is…” | Authority cosplay |
| “The reality is…” | Same as “The truth is…” |
| “What people don’t realize is…” | Manufactured insider status |
| “What makes this interesting is…” | Meta-hype; just say the interesting fact |
| “Let’s break it down.” | Podcast host mode |
| “Let’s talk about…” | Soft pivot filler |
| “Here’s the catch.” | Clickbait hinge |
| “Think about it.” | Condescending stall |
| “With that being said…” | Empty transition |
| “This raises the question…” | Rhetorical throat-clear |
| “This underscores…” | Essay glue |
| “The bigger picture…” | Vague zoom-out without a point |

**Also ban near-variants:** “Here’s what nobody tells you…”, “At the end of the day…”, “Make no mistake…”, “If you take one thing away…”, “In a world where…”.

**Rewrite rule:** delete the opener; keep only the concrete claim, number, or product behavior.

### Typography & motion
- Prefer distinctive, product-picked fonts (session: **Sora + Plus Jakarta Sans**) — not Space Grotesk defaults.
- Card: real border, spacing, hover that is subtle (`t-card-lift` / press), not axis-tilted chart gimmicks.
- Charts: ResponsiveContainer; **no axis tilt / scale-125 wash** that makes graphs feel sloppy.
- Title FOUC: never leave permanent `opacity-0` without entrance that settles visible.

### Design ProMax usage
- **Read real ProMax sources** before inventing components.
- Adapt patterns; don’t dump an entire Acme sidebar with fake Teams/Perks onto a sports-agent product.

---

## 3. Dashboard is an APP

| Wrong (landing habits) | Right (app) |
|------------------------|-------------|
| Scroll-to-section sidebar | **View switch** (Overview / Activity / Decisions / Odds) |
| “Dashboard” link while already there | Drop it |
| Profile at top of rail | **Profile + account at bottom** |
| Run check in header **and** sidebar | **One** primary control |
| Listbox “selected section” for scroll | Active view highlight only |
| Half-height hanging sidebar | Shell: `h-dvh overflow-hidden`; rail full height; main scrolls |
| Drawer always mounted | **Unmount drawer when closed** (no stacked shadows) |

Connection / Live chip = session + agent URL (or real readiness) — not “last poll error cleared.”

---

## 4. Auth

1. Google OAuth is **sign up and sign in**. Copy must say both (nav, auth card, empty gates).
2. Same button: “Continue with Google” + one line that first visit creates the account.
3. Redirect URI and local URLs must use **one host** — prefer `http://127.0.0.1` everywhere; bind Astro to `127.0.0.1` if OAuth does.
4. Auth card uses **BrandMark**, not a black circle letter.
5. One-time exchange codes die after use — tell user to restart OAuth, don’t reuse callback URLs.

---

## 5. Agent / backend

1. Match research: **TxLINE fair value → maker quotes → Kamino withdraw → BetDEX → settlement redeposit**.
2. **Y_net / opportunity cost** in code with hard guardrails; LLM cannot override min edge.
3. Safe abort if withdraw fails; redeposit attempt if order fails after withdraw.
4. **Policy in `config.ts`** (`AGENT_POLICY`): yield APY, trade size, min edge, maker margin, horizons.
5. **Env only for secrets + URLs**: Google, session secret, Solana key, TxLINE/BetDEX keys, `WORKER_URL` / `FRONTEND_URL`.
6. Cron unauthenticated; user tick endpoints require session.
7. Surface root-cause reasons (“TxLINE not configured…”) not “Tick failed.”

---

## 6. Brand

1. Single logo family: raster mark + SVG favicon + apple-touch.
2. BrandMark component everywhere (nav, footer, auth, sidebar).
3. After logo change, update `public/` and any `dist/` copies; hard-refresh for tab icons.
4. Don’t leave stock framework favicons (e.g. Astro A) in the tree.

---

## 7. Stress / concurrency

1. In-flight lock on poll / Run check.
2. Dedupe identical HOLD reasons so intervals don’t flood the feed.
3. AbortError is abort — not “can’t reach.”
4. Unmount modals/drawers when closed.
5. Don’t map every error into “needsAuth” unless truly unauthorized.

---

## 8. Git

1. No `Co-Authored-By: Claude|Cursor|Anthropic` or AI trailers unless user demands.
2. No essay commit bodies they didn’t ask for.
3. Author = user git identity only.
4. Push only when asked.

---

## 9. Local / deploy mental model

| Surface | Local | Prod |
|---------|-------|------|
| Agent | Wrangler Worker | `wrangler deploy` |
| Web | Astro | Pages / static |
| Secrets | `.dev.vars` | `wrangler secret` |
| Policy | `config.ts` | same code |

- App may live in a subfolder (`nairashield/`); parent folder without `package.json` is not the npm root.
- Port busy ≠ broken; kill or reuse deliberately.

---

## 10. Pre-flight (full)

**Product / data**
- [ ] No mock metrics, demo charts, or invented social proof
- [ ] Empty states honest
- [ ] Agent strategy matches PRD/research

**Landing**
- [ ] Light default; hero-only bg; header-base (not sticky glass unless asked)
- [ ] Floating nav: rounded-xl + border if that pattern is in play
- [ ] How it works / FAQ / help kept when product still needs them
- [ ] No waitlist unless asked; no Product nav fluff; no em dashes
- [ ] No Real Talk openers (truth is / here’s the thing / not just X / let’s break it down…)
- [ ] Marquee transparent on hero; no junk bento photos
- [ ] Plain product language

**Dashboard**
- [ ] View switcher, not scroll map
- [ ] Profile bottom; one Run check; no current-page nav item
- [ ] Full-height shell; drawer unmounts when closed

**Auth / brand**
- [ ] Sign up + sign in language
- [ ] BrandMark + favicon consistent; 127.0.0.1 discipline for OAuth

**Config / git / stress**
- [ ] Policy in code; secrets in env
- [ ] Poll locked; no overlay stack
- [ ] Commit message user-shaped

---

## 11. Anti-patterns library (do not reintroduce)

1. Chart demo fallbacks “so the graph isn’t empty”
2. Full-page background under dashboard chrome
3. Sticky translucent nav against user “header base” request
4. Deleting How it works/FAQ/Help when only waitlist was cancelled
5. Em dashes in marketing copy
6. Eng-jargon landing (CPI chains, over-explaining stack)
7. Sidebar scroll-spy like a one-page site
8. Multiple Run check buttons
9. Demo agent mode after “no mocks”
10. Policy vars in `.dev.vars`
11. AI co-author trailers
12. Letter-circle logo next to a real BrandMark
13. “Sign in only” when Google also signs up
14. Always-mounted Drawer stacking backdrops under stress
15. Real Talk pivots (“The truth is…”, “It’s not just X…”, “Let’s break it down…”)

---

## 12. Invoke

- `/bypass-slop` at session start or mid-feature.
- Or: “apply anti-slop / no mocks / real metrics only / dashboard not landing.”

**Default stance:** Sparse honest product > complete-looking fake.
