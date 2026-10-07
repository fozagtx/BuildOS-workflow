# Kaizen Prototype-Building Workflow

Use this whenever the user asks to "build", "prototype", "start working", or "ship" something. Adapt phases to the request; skip phases that do not apply.

## Phase 0 — Capture intent (1–3 questions)

Before doing anything, resolve ambiguity:

1. Who is the user / target user?
2. What is the one-sentence problem or core loop?
3. What is the desired output (landing page, dashboard, Solana program, video, pitch deck)?

## Phase 1 — Plan

1. Run `git status` and `git branch`.
2. Write a todo list for 3+ tasks if the work is non-trivial.
3. Identify operations that can run in parallel.
4. Pick the right skill from `references/skill-router.md` (Solana/crypto) or `references/skill-catalog.md` (general).

## Phase 2 — Validate / research (optional)

If the user has an unvalidated idea:

- `validate-idea` — structured validation sprint.
- `competitive-landscape` — map existing players.
- `defillama-research` — DeFi market data.
- `colosseum-copilot` — hackathon winner patterns (requires token).
- `find-next-crypto-idea` — discovery interview.

## Phase 3 — Design (if UI is involved)

1. `brand-design` — generate and apply brand palette, typography, tone.
2. `frontend-design-guidelines` — high-quality web UI rules (Tailwind + shadcn defaults).
3. `design-taste` — anti-AI-slop design direction for crypto UIs.
4. `typography-layout` — type hierarchy, pairing, editorial layout.
5. `web-animation-guidelines` or `page-load-animations` — motion patterns.

## Phase 4 — Build

### Web / full-stack prototype

- `scaffold-project` for Solana workspaces.
- `build-with-claude` for step-by-step MVP guidance.
- `frontend-design` for polished components/pages.
- `web-artifacts-builder` for complex multi-component HTML artifacts.
- `rare-ui` for distinctive single-file React components.
- `transitions-dev` / `transitions-polish` / `micro-interactions` for motion.

### Solana / crypto

- `build-defi-protocol` for DEX/AMM/lending/vaults.
- `launch-token` for token creation.
- `build-mobile` for React Native dApps.
- `build-data-pipeline` for indexers/webhooks.
- `base44-sandbox` / `base44-sdk` / `base44-cli` for Base44 apps.
- `okx-agentic-wallet` / `okx-defi` for OKX on-chain actions.

### Video / media

- `marketing-video` / `product-launch-video` for promo videos.
- `clipify` for cutting clips.
- `hyperframes-*` for HyperFrames compositions.
- `video-craft` for frame-level polish.

### Documents / pitch

- `create-pitch-deck` for investor decks.
- `apply-grant` for Solana Earn grants.
- `create-readme` for READMEs.
- `docx` / `pdf` / `pptx` / `xlsx` for file deliverables.

## Phase 5 — Audit before ship

1. `vibe-security` — common AI-coding vulnerabilities.
2. `cso` — infrastructure-first security audit.
3. `review-and-iterate` — Solana code review.
4. `x-ray` — pre-audit report.
5. `diagnose` — if something is broken.

## Phase 6 — Ship

1. Git: feature branch, meaningful commits, `git diff` review.
2. `create-readme` if the repo needs a README.
3. `submit-to-hackathon` if applicable.
4. `deploy-to-mainnet` for Solana mainnet launches.
5. Hand off to the user with a short summary and next steps.

## Efficiency reminders

- Parallelize reads, searches, and independent edits.
- Use `MultiEdit` for 3+ file changes.
- Read before writing; never edit without seeing the file.
- Remove temporary files before ending the session.
- Commit restore points before risky operations.
