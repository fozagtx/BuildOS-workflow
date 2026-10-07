# BuildOS-workflow Analysis

## Discovery
- Initial audit found 390 SKILL.md files in main harness directories.
- Deep research across the entire filesystem found **2,842 SKILL.md files**.
- Most extra files are in `node_modules`, caches, `.codex/.tmp` marketplace plugins, and temporary session directories.
- After excluding caches/node_modules, **1,173 user-owned/project-specific/agent skills** were missing from the repo.

## What was added
- **923** missing skill directories were copied into `BuildOS-workflow/skills/`.
- **426** were duplicates of already-retained skills (same frontmatter `name`) and were removed.
- Final repository now contains **736** unique skill directories.

## Sources added
- Main harness skills (`.agents`, `.claude`, `.codex`, `.cursor`, `.grok`, `.devin`)
- Disabled skills (`.agents/disabled-skills/`)
- Project-specific skills (`Desktop/*`, `Projects/*`)
- Other agent harnesses (`.hermes`, `.minimax`, system skills)

## Exclusions
- `node_modules` and package-manager caches
- `.codex/.tmp` and `.codex/plugins/cache` marketplace plugin copies
- Claude local-session plugin caches
- Devin plugin caches
- Test fixture skills (`pi-sec/packages/coding-agent/test/fixtures/`)
- Build artifacts and `.git` subdirectories

## Portability
- All copied skills are self-contained; nested `.git` directories were stripped.
- `install.sh` symlinks the `skills/` tree into supported agent harness directories.
- To migrate to a new machine, clone the repo and run `install.sh`.