# MirrorMarket Skill for Claude Code

A Claude Code skill that lets Claude query the [MirrorMarket Prediction Market Intelligence API](https://mirrorcheck.hub.zerve.cloud/) — a live comparison layer between **Polymarket** and **Kalshi**.

When installed, you can ask Claude things like:

- *"Where are Polymarket and Kalshi disagreeing the most right now?"*
- *"Which platform has stronger longshot bias today?"*
- *"Top 5 Polymarket markets by 24h volume"*
- *"Find tradeable arbitrage with both sides liquid"*

Claude will pick the right endpoint, filter, and return the answer.

---

## What it does

The skill teaches Claude:

- The base URL and every endpoint (`/arbitrage`, `/calibration`, `/markets/polymarket`, `/markets/kalshi`, `/refresh`)
- The schema of every response object
- How to filter noisy matches (similarity threshold, both-sides-liquid)
- Sensible `jq` recipes for the most common questions
- The known limitations (snapshot-only, fuzzy matching, no resolution data)

---

## Installation

### 1. Clone this repo

```bash
git clone https://github.com/fozagtx/mirrormarkets.git
```

### 2. Move the skill into your Claude Code skills folder

Claude Code reads user-level skills from `~/.claude/skills/`. Each skill lives in its own subfolder.

```bash
mkdir -p ~/.claude/skills
mv mirrormarkets ~/.claude/skills/mirrormarket
```

The folder name (`mirrormarket`) becomes the slash command — `/mirrormarket`.

> **Project-scoped install instead?** Drop the folder at `<project-root>/.claude/skills/mirrormarket` and it'll only load inside that project.

### 3. Restart Claude Code

Skills are picked up at startup. Quit and reopen Claude Code (or run `/reload` if your version supports it).

### 4. Verify

In any Claude Code session, type:

```
/mirrormarket
```

…or just ask a natural-language question:

```
Are there any arbitrage opportunities between Polymarket and Kalshi today?
```

Claude should invoke the skill automatically.

---

## File layout

```
mirrormarkets/
├── README.md     ← this file
└── SKILL.md      ← the skill definition Claude reads
```

`SKILL.md` is the only file Claude needs. The YAML frontmatter (`name`, `description`) tells Claude when to invoke it; everything below is the playbook.

---

## Configuration

No API key required — the MirrorMarket API is currently public.

If the API URL changes, edit `SKILL.md` and update the `Base URL` line.

---

## Updating

```bash
cd ~/.claude/skills/mirrormarket
git pull
```

Restart Claude Code to pick up changes.

---

## Uninstalling

```bash
rm -rf ~/.claude/skills/mirrormarket
```

---

## Disclaimer

The API and this skill output **are not financial advice**. Match-quality is fuzzy — always check the `similarity` score on arbitrage rows before acting on them.
