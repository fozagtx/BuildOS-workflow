# Problem Finder

Force a problem-discovery pass on startup and hackathon ideas before anyone starts solutioning.

## What is it?

Problem Finder is an agent skill kit. The installable skill lives in `skill/`. The rest of the repo is the kit around it.

- **Router** (`skill/router.md`) classifies the request and names the files to read. It is required on every run.
- **Workflow** (`skill/problem-workflow.md`) restates the job from the person doing the work. It is required for a full apply.
- **Workaround map** (`skill/workaround-map.md`) lists what they already do today. Empty map means suspect. It is required for a full apply.
- **Framing reject + scores** (`skill/framing-reject.md`, `skill/signal-scores.md`) sort obvious vs non-obvious before any build. They are required for a full apply.
- **Sharpen** (`skill/sharpen.md`) emits the six-heading report. It is required for a full apply.
- **Edge cases** (`skill/edge-cases.md`) handles skip-to-stack, buyer-only personas, empty pain, and after-report lock. Load it when those fire.
- **Worked example** (`skill/worked-example.md`) is the frozen market-woman demo. Load it only for that prompt.

Agents, commands, rules, installers, and evals ship with the kit. They are optional once the skill files are installed.

The agent remains in charge. The router picks a path; the report is the stop condition; a product list is not a legal first output.

## How it works

```text
USER PROMPT
     |
     v
 skill/router.md
     |
     +-- implementation / crypto-idea search -----> leave this skill
     +-- "how does this skill work?" -------------> explain files
     +-- skip / buyer / empty pain ---------------> edge-cases.md
     +-- market-woman demo -----------------------> worked-example.md
     +-- apply / "is this obvious?"
            |
            v
     obvious vs non-obvious
     (framing-reject + signal-scores)
            |
            +-- obvious -----> reject line, no build
            +-- empty map ---> suspect report
            +-- non-obvious -> workaround-map
                                  |
                                  v
                           problem-workflow
                                  |
                                  v
                              sharpen.md
                         six-heading report
                                  |
                                  v
                    "what should we build?"
                         stays inside #1
```

Stop when the six headings exist (or the suspect variant). Max 3 doer questions before classifying again. Do not invent workarounds. Do not load every module.

## Why use it?

- Turns "what should I build" into a worker, a workaround, and a structural gap
- Names and kills obvious framings (delivery, education, marketplace, dashboard, AI for X) before a stack appears
- Routes each request to the smallest file set via `skill/router.md`
- Fails closed on skip attempts, buyer-only personas, and empty pain

Results depend on the model following the skill. The report headings are the contract. There is no guaranteed live-eval score for a given chat.

## Install

Clone elsewhere → install into a skills dir. Never install onto the clone.

This repository is the skill kit. The installed skill is a copy of `skill/` in a skills directory. Do not clone this repo into a skills path and then install onto that same path. `install-custom.sh` option 2 would copy `skill/` over the git repo and can eat it. The custom installer refuses if the target looks like this clone (has `.git` and `install.sh`).

Requires bash. No network calls in the installers.

### Recommended

```bash
git clone https://github.com/fozagtx/problem-finder.git
cd problem-finder
./install-custom.sh
```

Pick `~/.agents/skills/problem-finder`, `~/.claude/skills/problem-finder`, or a project `skills/` folder.

### Standard

```bash
./install.sh
./install.sh -y
```

Defaults: skill at `~/.agents/skills/problem-finder`. Standard install also copies `CLAUDE.md` onto `~/.agents/AGENTS.md`.

### GitHub Release

A `problem-finder.skill` zip is attached to [GitHub Releases](https://github.com/fozagtx/problem-finder/releases). Layout is `problem-finder/SKILL.md` plus the sibling modules (`router.md` and `edge-cases.md` included). Rebuild it with `./scripts/package_skill.sh`. Unpack into a skills directory.

Start a new agent chat after installation so the skill can load.

## Quick start

Recommended: install, then paste a messy idea.

```bash
git clone https://github.com/fozagtx/problem-finder.git
cd problem-finder
./install-custom.sh
```

```text
A market woman loses money to spoilage, price hurdles, and transportation. What should we build?
```

Expect the six-heading report (original framing, who does the work, workarounds, scores, rejected obvious framings, ranked problems). The expected demo report is frozen in `evals/canonical-market-woman.md`.

With the Release zip (omit the git clone):

```text
Download problem-finder.skill from GitHub Releases
Unpack into ~/.claude/skills/ or ~/.agents/skills/
Start a new chat and paste the market-woman prompt
```

Minimal install (omit the custom picker):

```bash
./install.sh -y
```

Buyer-only first prompt (doer interview, no stack):

```text
What should I build for small restaurant owners?
```

After setup, start another new chat and use the skill normally. It triggers on startup ideas, hackathon ideas, "what should I build," validate-this, and a solution with no problem.

## Choose your path

The router assigns one ID. If two match, it takes the earlier ID.

```text
R0  implementation work          -> leave
R1  crypto idea bank             -> find-next-crypto-idea
R2  how the skill works          -> router.md + SKILL.md
R3  skip / buyer / empty pain    -> edge-cases.md first
R4  market-woman demo            -> worked-example.md
R5  apply the skill              -> reject + scores + map + workflow + sharpen
R6  workarounds only             -> workaround-map.md
R7  "is this obvious?"           -> framing-reject.md + signal-scores.md
```

- Omit the worked example unless the prompt is stall-trader spoilage + price + transport.
- Omit workflow + sharpen on R2 (about the skill) unless they also asked for a run.
- Sharpen is required for a full apply (R5).
- Path labels are literal. Do not remap them.

You can also ask naturally:

```text
How does this skill work? Which files should you read?
```

```text
/route
```

## Useful commands

```text
/route            Classify the prompt and name the files to read
/problem-sprint   Full run to the six-heading report
/map-workaround   Map current behavior; flag empty pain
/reject-framing   Score and reject obvious framings
/skill-demo       Walk the frozen market-woman example
/check-edges      Match skip / buyer-only / empty-pain cases
```

```bash
./tests/validate_structure.sh
./scripts/package_skill.sh
```

## Important limits

- The report exists before any product, stack, or feature list.
- Obvious framings stay in **Rejected obvious framings**. They do not become the build.
- Empty workaround map → suspect report. Ranked problems stay none.
- Buyer, market, and demographic fail the worker gate. Ask at most 3 doer questions.
- After the report, "what should we build?" stays inside ranked #1.
- Pure implementation (bugfix, types, CSS, refactor, git) stays off this skill.
- Crypto-idea search belongs to find-next-crypto-idea.
- Standard `install.sh` copies `CLAUDE.md` → `~/.agents/AGENTS.md` on purpose (DMR default).
- Never install onto the git clone.
- One worked example. `skill/SKILL.md` stays under 200 lines.

## Update

In the clone:

```bash
git pull
./install-custom.sh
```

That overwrites the installed `skill/` copy. Start a new chat after updating. Rebuild the zip with `./scripts/package_skill.sh` if you ship a Release.

## Uninstall

Remove the installed skill directory. Leave the git clone alone if you still want the kit.

```bash
rm -rf ~/.agents/skills/problem-finder
rm -rf ~/.claude/skills/problem-finder
```

Standard install may have written `~/.agents/AGENTS.md`. Review that file yourself; uninstall does not revert it.

## Development

```bash
./tests/validate_structure.sh
./scripts/package_skill.sh
```

The validator checks required files, frontmatter, router links, the six report headings, the frozen market-woman report, the `.skill` zip layout, attribution hygiene, and eval suites.

## License

MIT. See [LICENSE](LICENSE).
