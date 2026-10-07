# BuildOS-workflow

Kaizen's portable coding-agent workflow repository. Contains 239 agent skills spanning UI/design, backend, Solana/crypto, infrastructure, security, research, video, and agent tooling.

## What's inside

```
BuildOS-workflow/
├── README.md              # this file
├── KAIZEN_MEGA.md         # complete skill catalog (1,450+ lines)
├── ANALYSIS.md            # condensed analysis by category
├── install.sh             # symlink all skills into agent harnesses
└── skills/                # every skill as a self-contained directory
    ├── kaizen-mega/       # master router skill
    ├── frontend-design-guidelines/
    ├── bypass-slop/
    ├── scaffold-project/
    └── ... (239 total)
```

## Quick install

```bash
cd ~/BuildOS-workflow
bash install.sh
```

This symlinks every skill in `skills/` into the supported agent harness directories:

- `~/.agents/skills`
- `~/.claude/skills`
- `~/.codex/skills`
- `~/.cursor/skills`
- `~/.grok/skills`
- `~/.config/devin/skills`
- `~/.devin/skills`
- `~/.augment/skills`
- `~/.pi/skills`

## How to use

In any agent harness, activate the `kaizen-mega` skill. It loads your rules, workflow, and routes to the correct domain skill.

You can also invoke individual skills directly by name, e.g.:

- `frontend-design-guidelines` for web UI
- `build-with-claude` for Solana MVP guidance
- `vibe-security` for a security audit
- `brand-design` for brand palette + typography

## Migrating to a new machine / Cloud Code

1. Clone or copy this repository.
2. Run `bash install.sh` on the target machine.
3. Restart the agent harness.

## Updating

Edit the canonical copy in `~/BuildOS-workflow/skills/`. Because harnesses use symlinks, installed copies update automatically.
