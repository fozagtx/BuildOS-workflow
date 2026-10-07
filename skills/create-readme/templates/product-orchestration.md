# Template: product-orchestration

Product / plugin README in the **Codex Orchestration** style. Tone: plain,
confident, instructional. Short paragraphs. Exact commands. Honest limits.
No hype adjectives. No emoji clusters. No marketing fluff.

Use this when the project is a workflow, plugin, CLI, or multi-role system
that needs: pitch → what → how (ASCII flow) → why → install → quick start →
configuration → commands → limits → update/uninstall.

## Canonical structure (follow this order)

Adapt section titles to the product, but keep this narrative shape:

1. **Title** — product name as `#` heading
2. **One-line pitch** — what it enables, in one sentence under the title
3. **What is it?** — numbered or labeled roles/parts; mark optional vs required
4. **How it works** — ASCII flowchart + short process notes (loops, stop
   conditions, safety limits)
5. **Why use it?** — benefit bullets; end with a caveat that results depend on
   inputs and that any speed/limit figures are targets, not guarantees
6. **Install** — exact install commands; note runtime requirements
7. **Quick start** — 2–4 concrete command recipes (full / with optional roles /
   minimal). Show the happy path first.
8. **Choose your roles / configuration** — how to name roles, what may be
   omitted, what is required, independence rules, activation confirmation
9. **Bring another model / extend** (if applicable) — external providers,
   security staging (never paste keys into chat), sealed exceptions
10. **Use it with Goals / larger workflows** (if applicable)
11. **Useful commands** — status, repair, update, setup, disable, etc.
12. **Important limits** — root authority, who talks to whom, what the tool
    never does (credentials, picker changes, etc.)
13. **Update** — self-update vs native upgrade path; version gates
14. **Uninstall** — disable first, then remove; note what is not deleted
15. **Development** — install, lint, test, release check commands from the repo
16. **License** — short line (e.g. MIT) when the project has one

## Style rules (match the reference closely)

### Voice

- Lead with capability, not adjectives: "adds four simple roles", not
  "powerful next-gen orchestration".
- Prefer "is optional" / "is required" over vague optionality.
- Prefer "Codex remains in charge" / "reports only to …" clarity over slogans.
- State safety boundaries plainly: never paste API keys; disable before
  uninstall; figures are targets not guarantees.

### Formatting

- `#` title, then bare pitch line (no subtitle heading).
- `##` for major sections; keep headings short: `What is it?`, `How it works`,
  `Why use it?`, `Install`, `Quick start`, `Useful commands`, `Important limits`.
- Use a monospaced ASCII diagram for the workflow. Center with spaces if needed.
  Keep arrows as `|`, `v`, `-- yes --+`, etc.
- Put example invocations in fenced `text` or bare indented command blocks.
- Use bullet lists for roles, benefits, limits, and command catalogs.
- Call out literal labels: role names after `planner:`, `advisor:`, etc. mean
  exactly that role—never remap because of older versions.
- When listing activation output, show the exact confirmation shape the tool
  prints (e.g. `Planner — Fable 5 high: Activated`).

### Content discipline

- Every install/setup/update command must be copy-pasteable and real for this
  project.
- Include at least one "omit optional parts" recipe and one full recipe.
- If parallel speedups or limit reductions are claimed, add the caveat paragraph.
- Document stop conditions (e.g. approval reached, max review rounds).
- Document what disable/repair/update do **not** touch (credentials, chats,
  sessions, picker, etc.) when those concepts exist.
- Prefer "ask naturally" examples for status questions when the product
  supports them.

## Skeleton to fill (replace bracketed parts)

```markdown
# [Product Name]
[One sentence: bring X into Y, assign roles, let Y coordinate.]

## What is it?
[Product] adds [N] simple roles to a [task type]:

[Role A] [does X]. It is optional; when omitted, [fallback].
[Role B] [does Y]. It is optional.
[Role C] [does Z]. It is optional.
[Role D] [implements / executes]. It is required for setup.

The [root orchestrator] remains in charge. It passes work between the roles,
checks every result, and gives you the final answer.

## How it works
[ASCII flowchart of YOUR TASK → COORDINATOR → PLAN → REVIEW loop → DESIGN
(optional) → EXECUTE → TEST & DELIVER]

[1–3 sentences on revision loops, approval stop condition, and safety limit.]

## Why use it?
- [Benefit 1]
- [Benefit 2]
- [Benefit 3]
- [Parallel / speed / limit benefit if real]

Results depend on [models, task, context, retries, available parallel work].
The speed and limit figures are targets, not guarantees.

## Install
```bash
[exact install commands]
```
Start a new [task/session] after installation. Setup requires [runtime].

## Quick start
[Recipe A — recommended full setup]

```text
[exact setup command]
```

[Recipe B — with optional design/extra role]

```text
[exact setup command]
```

[Recipe C — minimal / omit planner or advisor]

```text
[exact setup command]
```

After setup, start another new task and use [product] normally. The saved
workflow applies automatically.

[Effort / model notes if relevant.]

## Choose your roles
```text
[setup grammar with placeholders]
```

- Omit [role] to …
- Omit [role] when …
- [required role] is required.
- [Independence rule, e.g. planner and advisor must differ.]
- Role labels are literal. …

When every requested route is ready, confirm only the roles supplied, in order:

```text
[Role] — [Model] [effort]: Activated
```

Activated means ready and callable. If auth/qualification is still needed,
report that exact state instead of claiming activation.

You can also ask naturally:

[example status question]

## Useful commands
```text
[status]
[repair]
[update]
[setup …]
[disable]
```

## Important limits
- [Root] remains the final authority.
- Roles report only to [root]; they do not contact one another directly.
- [What designer/planner may and may not edit.]
- [Approval is a gate, not a success guarantee.]
- [Credentials / permissions / picker boundaries.]
- If the user says no subagents / no delegation, do not delegate.

## Update
[Self-update command and what it refuses.]
[Migration path from older versions.]
[Restart / new task guidance.]

## Uninstall
First run disable, then remove:

```bash
[disable]
[remove plugin / package]
```

Review and remove user-owned custom roles/config separately.

## Development
```bash
[install dev deps]
[compile / typecheck]
[lint]
[tests]
[release check]
```

## License
[SPDX or short name]
```

## Reference shape (Codex Orchestration)

When writing for Codex Orchestration itself—or when the user wants a near-
verbatim structure—mirror this section order and density from the live product
README:

1. Title + pitch ("Bring models like Claude Fable 5 into Codex…")
2. What is it? — Planner / Advisor / Designer / Executor (optional vs required)
3. How it works — ASCII flow with PLANNER → ADVISOR loop → DESIGNER → EXECUTORS
4. Why use it? — Fable/other models, stronger plan, parallel executors, limit
   relief + caveat
5. Install — marketplace add + plugin add; Python 3.11+
6. Quick start — full setup, designer variant, advisor-only variant
7. Choose your roles — omit rules, literal labels, Activated confirmation,
   natural-language status questions
8. Bring another model into Codex — External Models, staged secure setup,
   never paste keys; OpenRouter/Kimi notes; project vs personal roles
9. Use it with Codex Goals
10. Useful commands — status, repair, --update, setup, disable
11. Important limits — root Codex, no role-to-role contact, Fable tool policy,
    credentials, "no subagents"
12. Update — `/codex-orchestration --update` and 0.6→0.7 migration
13. Uninstall — disable then remove marketplace/plugin
14. Development — pip, compileall, ruff, unittest, smoke, release_check
15. License — MIT

Fill every command and model name from the actual repo; do not invent versions.
