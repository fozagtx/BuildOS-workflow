# Router

Read this file first on every request. Pick one path. Load only the files that path names. Stop. Do not solution until the path says a report exists.

If two paths match, take the earlier ID.

## Classify

| ID | Detect | Read | Then |
|---|---|---|---|
| R0 | Bugfix, types, CSS, refactor, git, pagination, translate-the-docs, already-sharpened plus "implement the API" | Nothing in this skill | Leave. Implementation work. |
| R1 | Crypto idea bank, "what should I build in crypto", DeFi vs DePIN | Nothing in this skill | Hand off to find-next-crypto-idea. |
| R2 | How this skill works, which files to read, how to apply it, install, routing | This file, then [SKILL.md](SKILL.md) | Explain the path. Do not sharpen their idea unless they also asked for a run. |
| R3 | Skip, stack, "just tell me what to build", buyer-only, empty pain, bundle, after-report follow-up | [edge-cases.md](edge-cases.md) first | Do the required edge behavior. If a full run is still needed, continue to R5. |
| R4 | Demo, walkthrough, market-woman prompt | [worked-example.md](worked-example.md) | Use the frozen report. Stay inside #1 if they ask what to build. |
| R5 | Apply the skill: startup idea, hackathon idea, "what should I build", validate this, pain with no problem | [framing-reject.md](framing-reject.md) and [signal-scores.md](signal-scores.md), then [workaround-map.md](workaround-map.md), [problem-workflow.md](problem-workflow.md), [sharpen.md](sharpen.md) | Run the obvious / non-obvious gate below. Then the six-heading report. |
| R6 | Workarounds only | [workaround-map.md](workaround-map.md) | Map current behavior. Empty map → suspect. |
| R7 | "Is this obvious?" / feel-safe / AI for X / dashboard / marketplace / education | [framing-reject.md](framing-reject.md) and [signal-scores.md](signal-scores.md) | Name obvious vs non-obvious. No stack. |

## Obvious vs non-obvious (before any solution)

Do this on R5 and R7 before [sharpen.md](sharpen.md). Help the user see the bucket. Do not commit to a product in either bucket.

**Obvious** (default-reject, keep going only as a reject line in the report):

- Can be pitched in one breath to a stranger who has never done the job
- Delivery, education, marketplace, dashboard, "AI for X", super-app, inclusion/empowerment
- No named workaround, or all four signals at 1-2
- The original sentence is already a product

**Non-obvious** (may sharpen):

- A named doer with hands on the mess
- A current workaround they already pay for in time, money, discount, or labor
- A structural reason it stays unfixed (ticket size, split ownership, incumbent incentive)
- Awkward to explain in one breath
- At least some signals at 4-5 after a split

If the framing is obvious, quote it in **Rejected obvious framings** and do not sharpen it into a build. If it is non-obvious, write the ranked sentences. If you cannot tell, ask at most 3 doer questions from [workaround-map.md](workaround-map.md), then classify again.

## Load order on a full apply (R5)

1. This file
2. [edge-cases.md](edge-cases.md) if R3 also matched
3. [framing-reject.md](framing-reject.md) + [signal-scores.md](signal-scores.md) (obvious vs non-obvious)
4. [workaround-map.md](workaround-map.md)
5. [problem-workflow.md](problem-workflow.md)
6. [sharpen.md](sharpen.md) (report template required)

Do not load [worked-example.md](worked-example.md) unless the prompt is the stall-trader spoilage + price + transport case (E26).
