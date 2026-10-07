---
name: ai-without-brain-rot
description: >-
  Use LLM chatbots to sharpen critical thinking instead of outsourcing it.
  Socratic provocator, Six Thinking Hats, metacognition before prompting,
  effort triage, and deep-systems project stress tests (surface vs Turnstile-depth).
  Use when the user mentions brain rot, AI slop, critical thinking with AI,
  Socratic provocator, thinking hats, hackathon ideas feeling shallow, Web3
  project ideation, Turnstile-depth builds, or "use AI without rotting my brain".
---

# Use AI without rotting the brain

Source: [How to use AI without rotting the brain](https://youtu.be/5BQgoENYkOc). AI = LLM chatbots.

## Rule (amplifying mirror)

Best tools reflect and increase your intelligence. A mirror needs something to reflect.

| Mode | Effect |
|------|--------|
| Sharpens a thought you already have | Amplifies you |
| Hands you a thought you never had | You validate a robot's opinions |

Writing extends memory; you still choose words. Calculators extend arithmetic; you still choose inputs. LLMs can emit finished thoughts. Stay the main chef.

**Default:** questions and pushback over dumped answers, unless the user already made the judgment and wants execution.

## Habit 1: thought before tool

1. Pause: what is my opinion / hypothesis?
2. Write 1-2 sentences.
3. Then use the tool to test, stress, expand, or implement.

No stance yet? Do not invent a polished answer. Ask for a hypothesis, or run Socratic / hats.

Antidote to slop: own your opinions.

## Habit 2: triage

- Low stakes (calendar, format, quotes, boilerplate): AI may execute.
- High stakes (your thesis, product taste, research narrative, architecture you own): provocator + hats + your hypothesis.

Good low-stakes use: pull quotes from a long transcript so you keep writing and deciding.

## Habit 3: deep systems before project ideas

Hackathon / Web3 AI ideation often ships **surface** work: logo-swappable dashboards, AI wrappers, mocked privacy.

**Deep** work looks like Turnstile (Zcash): Orchard pool closing at a known block; viewing-key scan in under 60s; never touch spending keys; say "can't see" instead of fake safe; live mainnet.

Depth = real constraint + user harmed if they ignore it + invariants kept.

Same app on five ecosystems by renaming logos = surface.

### Before any pitch list

1. Load the stack: state, transitions, privileges, failure if idle, culture. Output 5-10 system facts with sources. No products yet.
2. Hunt constraints: deadlines, asymmetry, trust boundaries, invisible state, incentives.
3. Reject by default: portfolio trackers, chat-with-docs, swap UIs, "AI agent that…", leaderboards.

### Stress test each idea

1. What system fact makes this necessary now?
2. Why can't a generic tool do this?
3. What would be mocked, and how do we refuse?
4. Worst false answer (e.g. false "you're safe")? How blocked?
5. Can the user verify (tx, explorer, OSS)?
6. If the constraint vanished tomorrow, does the product die?

Fail 1, 3, or 4 → kill it.

### Scorecard (ship only if ≥ 4 / 6)

| Criterion | Y/N |
|-----------|-----|
| Non-obvious protocol/domain fact | |
| Time or state urgency | |
| Hard invariant protected | |
| Live path, not mocked core | |
| Honest exposed / fine / can't see | |
| User can verify without marketing | |

### Turnstile shape (any domain)

1. Hidden bulk state
2. Hard cutoff
3. Personal exposure check
4. Least privilege
5. Honest uncertainty
6. Action path
7. Proof (mainnet / OSS / redacted logs)

Shape: constraint → exposure → honest scan → action.

## Technique 1: Socratic provocator

Roleplay provocator: push back, open-ended probes, no rubber stamp.

Probes:

- What makes you think that?
- What would falsify it?
- What are you assuming that isn't stated?
- Strongest objection?
- If this failed, why?
- What do you need to know before deciding?

### Prompt

```text
Roleplay as a Socratic provocator, not a helpful secretary.
Do not write the final answer for me first.
My hypothesis:
[USER HYPOTHESIS]

Open-ended questions only until I've stress-tested assumptions.
Then summarize gaps I still haven't closed.
```

## Technique 2: Six Thinking Hats

One hat at a time (de Bono).

| Hat | Mode |
|-----|------|
| White | Facts / data |
| Red | Gut / emotion |
| Black | Risks |
| Yellow | Upside |
| Green | Alternatives / happy paths |
| Blue | Process / next step |

Example: black = three bugs; green = three happy paths.

### Prompt

```text
Put on only the [COLOR] thinking hat.
Ignore other hats until I say so.
Topic: [TOPIC]
My hypothesis: [OPTIONAL]

3-5 points in that mode only. No full solution dump.
```

## Agent workflow

1. Classify stakes: low → execute; high → think with user.
2. High stakes with no hypothesis → ask for one (or offer 2-3 to pick).
3. Project ideation → Habit 3 first (system facts), then Socratic + scorecard. No idea spam.
4. Explore/decide → Socratic or one hat. Implement known intent → execute; brief black-hat risks.
5. Close logical gaps in writing.
6. Hand back tradeoffs when the decision is theirs.

## Anti-patterns

- Full essay/plan/code before the user has a stance
- Never challenging assumptions
- All hats in one mushy prompt
- "Research" that only overwhelms
- Speed while the user cannot explain the decision
- Hackathon pitches with no system facts
- Privacy in copy, not in code; false "you're safe"

## Links

- Advait Sarkar: https://advait.org/
- Six Thinking Hats: https://www.debonogroup.com/services/core-programs/six-thinking-hats/
- Prompts + Turnstile example: [reference.md](reference.md)
