# Trigger eval results

`evals/triggers.json` existed after PR #12. It had not been scored against the skill description. This file is that run.

Method: for each `should_trigger` prompt, ask whether `skill/SKILL.md` frontmatter would load this skill even if the user never said "problem discovery". For each `near_miss`, ask whether the skill's boundaries refuse the run or hand it off. Description must stay pushy and under 1024 characters.

## Description

Current frontmatter description is 468 characters. It already names startup idea, hackathon idea, "what should I build," validating an idea, finding problems, user pain points, and a solution without a validated problem — even if they do not ask.

No description rewrite. It was not under-triggering on T01–T10. Boundaries were tightened so N04 / N05 / N06 / N08 cannot steal the run.

## Should trigger (T01–T10)

| ID | Prompt class | Hits description | Verdict |
|---|---|---|---|
| T01 | Hackathon idea + app | hackathon idea, implied solution | PASS |
| T02 | "What should I build" | what should I build | PASS |
| T03 | "We're building" + dashboard | solution without a validated problem | PASS |
| T04 | "Validate this idea" | validating an idea | PASS |
| T05 | "User pain" | user pain points | PASS |
| T06 | "Startup idea" | startup idea | PASS |
| T07 | "What should we build" + messy framing | what should I build | PASS |
| T08 | "Is this a real problem or am I solutioning?" | finding problems | PASS |
| T09 | "Find problems worth building" | finding problems | PASS |
| T10 | "I have a solution and no problem" | solution without a validated problem | PASS |

## Near miss (N01–N08)

| ID | Why | Skill behavior | Verdict |
|---|---|---|---|
| N01 | TypeScript error | E14 / pure implementation. Do not run. | PASS |
| N02 | React useMemo refactor | Pure implementation. Do not run. | PASS |
| N03 | CSS hover state | Pure implementation. Do not run. | PASS |
| N04 | Already-sharpened sentence + "implement the API" | Implementation wins. Do not redo discovery as a pitch. | PASS |
| N05 | "What should I build in crypto? Search the idea bank" | Hand off to find-next-crypto-idea. Do not steal the run. | PASS |
| N06 | git rebase / lockfile conflict | Pure implementation. Do not run. | PASS |
| N07 | Translate the README | Not problem discovery. Do not run. | PASS |
| N08 | Add pagination to an endpoint | Pure implementation. Do not run. | PASS |

Skill wins on idea / hackathon / what-to-build / unvalidated-solution. Loses on pure implementation, already-sharpened-plus-build, and crypto-idea search.
