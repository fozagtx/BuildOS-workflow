---
name: create-readme
description: "Create or rewrite a project README.md using a selectable template. Use when the user asks to write a README, create README.md, rewrite the readme, or pick a README style/template. Templates: classic open-source and product-orchestration (Codex Orchestration style). Works via npx openskills read create-readme in any harness."
---

# Create README

Universal skill (Claude Code, Cursor, Codex, Grok, Continue, and any agent that reads `AGENTS.md` / `npx openskills read create-readme`).

Write a clear, scannable README. Always choose a template first, then draft.

## Step 0 — Choose a template

If the user has not named a template, ask which one they want:

1. **classic** — Concise open-source README (Azure Samples / sinedied style)
2. **product-orchestration** — Product/plugin README with pitch, roles, flow
   diagram, why/benefits, install, quick start, commands, limits (Codex
   Orchestration style)

If they say "like Codex Orchestration", "orchestration readme", "product
readme", or paste that structure, use **product-orchestration**.

If they say "normal", "simple", "open source", or "classic", use **classic**.

Then read the matching file under `templates/` and follow it.

- [templates/classic.md](templates/classic.md)
- [templates/product-orchestration.md](templates/product-orchestration.md)

## Shared rules (all templates)

1. Review the project/workspace before writing. Prefer real commands, real
   model/role names, and real constraints from the repo.
2. Use GFM (GitHub Flavored Markdown). Use GitHub admonitions sparingly when
   a warning or tip matters: https://github.com/orgs/community/discussions/16925
3. Do not overuse emojis. Prefer plain headings and short paragraphs.
4. Keep the README concise. Prefer examples over long prose.
5. If a logo or icon exists, put it in the header for **classic**. For
   **product-orchestration**, lead with title + one-line pitch; logo optional.
6. Do not invent install commands, version numbers, or limits. If unknown,
   omit or mark as TODO for the user.
7. Match tone to the template (see that template file). Do not mix styles.

## Workflow

1. Pick template (ask if needed).
2. Read the template file from this skill's `templates/` directory (resolve
   relative to the skill base directory reported by openskills / the harness).
3. Gather project facts: name, what it does, install, quick start, commands,
   limits, update/uninstall if applicable.
4. Write or rewrite `README.md` in the project root (or path the user gives).
5. Show the user which template was used.

## Harness access

Canonical path: `~/.agents/skills/create-readme/`

Symlinked for:

- `~/.claude/skills/create-readme` (Claude Code)
- `~/.agent/skills/create-readme` (OpenSkills universal)
- `~/.codex/skills/create-readme` (Codex)
- `~/.cursor/skills/create-readme` (Cursor)
- `~/.grok/skills/create-readme` (Grok)
- `~/.continue/skills/create-readme` (Continue)

Any AGENTS.md harness:

```bash
npx openskills read create-readme
```
