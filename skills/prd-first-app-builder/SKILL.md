---
name: prd-first-app-builder
description: Use when building or modifying any user-facing app, dashboard, landing page, wallet/auth-gated product, frontend routes, or demo UI; especially when the task mentions PRD, permissions, protected routes, shadcn/ui, route gating, no fake demos, no gradients, large icons, or avoiding mock/simulation lies.
---

# PRD First App Builder

## Core Rule

Create or update the project PRD before implementing user-facing app changes.

Do not start page/component work until the PRD defines:

- users and roles
- route map
- page permissions
- protected vs public routes
- app shell/navigation model
- required user flows
- UI component system
- no-fake-demo rules
- strict no-fixture-live-action rules
- acceptance criteria

If the repo lacks a PRD, create `docs/PRD.md`. If it exists, update it before coding.

## Workflow

1. Read existing product docs and app routes.
2. Write/update `docs/PRD.md`.
3. Build a permission matrix before adding routes.
4. Define the app shell before building protected pages.
5. Use shadcn/ui as the default UI component system for React/Next projects unless the repo already has a stronger local system.
6. Define icons from the project/user design system before implementation. If the user rejects lucide or asks for huge/custom icons, do not use lucide; use the requested icon treatment consistently.
7. Avoid decorative gradients unless the PRD explicitly approves exact gradient tokens from the supplied design system.
8. Implement only after the PRD gates are clear.
9. Validate build/typecheck.
10. Report what is real, what is gated, and what is still unimplemented.

## Route And Permission Standard

Every app must separate:

- public landing/marketing pages
- unauthenticated wallet/login gate
- protected dashboard/app pages
- API routes that reject unauthorized or incomplete requests

Public landing pages must not expose protected route links like dashboard, account, transfer, or activity unless the PRD explicitly allows them. A visitor who directly opens a protected route should see a full-page auth/wallet gate only, not the app shell/sidebar with protected content hidden inside it.

For every route, define:

```text
route
purpose
allowed roles/states
blocked roles/states
data shown
actions allowed
failure behavior
```

Browser route gates are UX only. Backend contracts, APIs, and chain logic must enforce actual authority.

## UI Standard

For Next/React apps:

- Prefer shadcn/ui components for buttons, cards, forms, inputs, sidebars, dialogs, tabs, badges, sheets, toasts, and tables.
- Use the icon system defined in the PRD. Do not default to lucide when the user supplied or requested a different icon direction.
- Use familiar controls: sidebar navigation, segmented controls, tabs, toggles, inputs, tables, dialogs.
- Use restrained product UI for financial/security tools.
- Avoid custom “vibe-coded” controls when shadcn/ui has the component.
- Avoid decorative gradients and gradient blobs.
- Do not expose internal scaffold/status language to end users.
- Do not put protocol/proving-system jargon on public landing pages unless the user explicitly asks for technical marketing copy.

## No Fake Demo Standard

Never present mocks, simulations, local fixtures, or hardcoded states as real deployed behavior.

Never use fixture keys, demo wallets, generated test accounts, mock accounts, or simulation-only identities to exercise user-facing live flows on testnet, mainnet, production, or deployed preview URLs unless the user explicitly approves that exact action in the current turn.

Do not POST account setup, submit transactions, deploy contracts, create proof records, or create explorer-visible state from fixture/demo data as a substitute for a real connected user wallet. If live verification needs a wallet-controlled action and no real user wallet is available, stop and ask for approval or show the feature as unavailable.

Allowed only when clearly labeled:

- unit-test mocks
- localnet fixtures
- transaction simulation output
- placeholder IDs

Never allowed:

- fake proof success
- fake transaction hashes
- fake explorer links
- mock balances labeled as real balances
- hardcoded deploy/transfer success
- local-only behavior described as testnet/mainnet behavior
- fixture-created contracts, hashes, explorer links, balances, proofs, or activity presented as product/user state
- fixture/demo/test-wallet live actions without same-turn explicit user approval

If a feature is incomplete, show a blocked/pending state and explain the next real requirement. Do not invent success.

## PRD Template

Use `references/prd-template.md` when creating a new PRD.

## Completion Checklist

Before final response:

- PRD exists or was updated.
- Route permission matrix exists.
- Protected routes are gated in UI.
- shadcn/ui usage is planned or implemented for React/Next UI.
- No decorative gradients were introduced unless explicitly approved.
- No fake demo/simulation success was introduced.
- No fixture/demo/test-wallet live action was run without same-turn explicit user approval.
- Build/typecheck results are reported.
