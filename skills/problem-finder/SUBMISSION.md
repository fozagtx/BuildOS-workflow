# Submission Notes

## Project

Problem Finder

## Problem

Builders are good at solutioning and weak at probleming. Startup and hackathon work collapses into obvious, feel-safe framings: delivery, education, marketplace, dashboard, "AI for X." The first sentence of an idea is treated as the problem. The person buying software is treated as the user. Workarounds are skipped. The result is a product that feels safe to pitch and does not sit on a felt pain.

## Who Uses It

- Hackathon teams
- Founders choosing what to build
- Product people handed a solution with no problem
- Mentors reviewing idea pitches
- AI agents that otherwise jump to architecture
- Operators who know the job and need the framing sharpened

## Novelty

Most idea workflows tell agents to "brainstorm solutions" or "validate the market." This skill forces the agent to name the worker, map current workarounds, score structural signals, reject obvious framings, and write one-sentence problems before any build advice. The failure mode is premature solutioning.

## Kit Fit

The repo follows a skill addon pattern:

- `skill/SKILL.md` entry point
- focused progressive-disclosure modules
- optional `agents/`
- optional `commands/`
- optional `rules/`
- installer scripts
- README
- MIT license
- local structure validator
- edge-case table and eval suites (skip attempts, buyer-only, empty pain, AI-for-X rejects)

## Safety

- No binaries
- No network calls in install scripts
- No opaque runtime behavior
- Installers copy local Markdown files only
- Clear rule against inventing pain or skipping empty workaround maps
- Validator checks for forbidden attribution strings before submission

## Demo Prompts

```text
A market woman loses money to spoilage, price hurdles, and transportation. What should we build?
```

```text
Hackathon idea: an app that helps market women reduce spoilage.
```

```text
We're building an AI dashboard for warehouse managers to cut waste. Is this a real problem?
```

## Expected Outputs

- Original messy framing
- Who does the work
- Current workarounds
- Signal scores
- Rejected obvious framings
- Ranked sharpened problems
- Live workflow demo

## Live Example

The bundled example researches this framing:

> A market woman loses money to spoilage, price hurdles, and transportation.

See [evals/canonical-market-woman.md](evals/canonical-market-woman.md). ARTICLE.md, skill/worked-example.md, and /skill-demo point at that file.
