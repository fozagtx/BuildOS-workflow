# Installing the Kaizen Mega Skill in Other Agents

The canonical source is `~/.agents/skills/kaizen-mega/`. To use it in another agent harness, symlink that directory into the harness's `skills/` folder. Then restart the agent or wait for it to rescan skills.

## Supported harnesses

| Harness | Skills directory |
|---------|------------------|
| Claude Code | `~/.claude/skills/` |
| Codex (CLI) | `~/.codex/skills/` |
| Cursor | `~/.cursor/skills/` |
| Grok | `~/.grok/skills/` |
| Devin | `~/.config/devin/skills/` or project `.devin/skills/` |
| Augment | `~/.augment/skills/` |
| Kilo | `~/.kilo/skills/` |

## Manual install

```bash
ln -s ~/.agents/skills/kaizen-mega ~/.claude/skills/kaizen-mega
ln -s ~/.agents/skills/kaizen-mega ~/.codex/skills/kaizen-mega
ln -s ~/.agents/skills/kaizen-mega ~/.cursor/skills/kaizen-mega
ln -s ~/.agents/skills/kaizen-mega ~/.grok/skills/kaizen-mega
ln -s ~/.agents/skills/kaizen-mega ~/.config/devin/skills/kaizen-mega
ln -s ~/.agents/skills/kaizen-mega ~/.augment/skills/kaizen-mega
ln -s ~/.agents/skills/kaizen-mega ~/.kilo/skills/kaizen-mega
```

## Scripted install

Run the bundled `scripts/install.sh`:

```bash
bash ~/.agents/skills/kaizen-mega/scripts/install.sh
```

This creates symlinks for all known harnesses that exist on the system.

## Verification

After installation, the skill should appear in the harness's skill list and its description should be loaded into context. In Claude/Codex/Cursor, skills are auto-discovered. In Devin, you can run:

```bash
npx openskills list | grep kaizen-mega
```

## Cloud Code / remote agents

If the target agent does not have access to your local filesystem, copy the entire `kaizen-mega/` folder into the remote agent's skills directory, or zip it and upload it. The folder is self-contained: `SKILL.md` plus `references/` and `scripts/`.

## Updating

Edit the canonical source at `~/.agents/skills/kaizen-mega/`. Because the harnesses use symlinks, all installed copies update automatically.
