---
name: kaizen-mega
description: >
  Kaizen's full-stack prototype-building mega-skill. Loads the user's personal rules, workflow,
  and skill catalog, then routes to the right domain skill for fast UI/backend/crypto/video/pitch
  work. Use whenever the user says "build", "prototype", "scaffold", "design", "ship", "start working",
  "kaizen", or any product/MVP/hackathon task. Apply proactively on greenfield product work.
---

# Kaizen Mega Skill

You are operating in Kaizen's personal coding-agent environment. This skill is the master router.
It does not replace domain skills; it loads the user's context and tells you which skill to invoke.

## On every activation

1. Read `references/rules.md` first — these are non-negotiable user rules.
2. Read `references/workflow.md` — this is the default prototype-building flow.
3. Read `references/skill-router.md` if the task touches Solana, crypto, hackathons, or product launch.
4. Read `references/skill-catalog.md` to find the right skill for the user's request. If nothing fits, fall back to `references/full-catalog.md`.
5. Invoke the matched skill immediately. In Devin run `npx openskills read <skill-name>`; in Claude/Codex/Cursor the skill auto-loads if it is installed in the harness skills directory.

## How to decide which skill to use

| User intent | Look in | Likely skill |
|-------------|---------|--------------|
| Build a web UI / component / landing page | skill-catalog.md (frontend/design) | `frontend-design-guidelines`, `frontend-design`, `brand-design`, `design-taste` |
| Solana/crypto MVP, DeFi, token, mobile | skill-router.md | `scaffold-project`, `build-with-claude`, `build-defi-protocol`, `launch-token`, `build-mobile` |
| Validate or discover an idea | skill-catalog.md (product/strategy) | `validate-idea`, `find-next-crypto-idea`, `competitive-landscape` |
| Security / audit / review | skill-catalog.md (security/audit) | `vibe-security`, `cso`, `review-and-iterate`, `x-ray` |
| Video / marketing / pitch | skill-catalog.md (video/media) | `marketing-video`, `product-launch-video`, `create-pitch-deck` |
| Research / SEO / analytics | skill-catalog.md (research/analytics) | `geo-audit`, `defillama-research`, `competitive-landscape` |
| Agent / MCP / tooling | skill-catalog.md (agent/tools) | `mcp-builder`, `claude-api`, `claude-agent-sdk-expert` |
| CockroachDB / infrastructure | skill-catalog.md (database/infrastructure) | `cockroachdb-sql`, `provisioning-cluster-for-production` |

## Default workflow for "start working" / "build prototype"

Follow `references/workflow.md`:

1. **Capture intent** — ask just enough to scope the prototype (user, problem, core loop, tech stack guess).
2. **Plan** — write a todo list, identify parallel work, pick the right skills.
3. **Research / validate** — if the idea is unvalidated, run `validate-idea` or `competitive-landscape` first.
4. **Design** — if UI is needed, run `brand-design` and `frontend-design-guidelines` before coding.
5. **Build** — scaffold with `scaffold-project` (Solana) or project-appropriate stack; use `build-with-claude` for step-by-step.
6. **Audit** — run `vibe-security` and/or `cso` before shipping, plus `review-and-iterate` for Solana programs.
7. **Ship** — git branch, commit, README via `create-readme`, pitch/grant/video if requested.

## Non-negotiables

- Never add `Co-Authored-By: <AI assistant>` to commits. The user's git identity is the only author.
- Never mention "Claude", "Codex", "Anthropic", or any AI assistant in PRs, issues, code comments, or committed artifacts unless explicitly asked.
- No mock metrics, demo data, or fake social proof. Empty/honest > fake-complete.
- Build only what was asked; MVP first; no speculative auth/deployment/monitoring.
- Read before writing. Run `git status` and check the branch at session start.
- Prefer parallel tool calls; batch edits; use MCP servers for their designed purpose.

## When this skill is insufficient

If the user's request is a single well-scoped task that clearly matches one domain skill (e.g. "make a PDF", "audit my contract"), skip this mega-skill and load that domain skill directly. This skill is for orchestration, not for doing every task itself.

## Complete catalog

For the full layered bible of all 238 useful skills (UI → backend → crypto → infra → security → research → video → agent tooling), see `KAIZEN_MEGA.md` in this skill's base directory.
