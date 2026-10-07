# Edge Cases

Read this on any skip attempt, buyer-only persona, empty pain, bundled symptoms, implied solution, or follow-up after the report. Match the input to an ID. Do the required behavior. Never do the forbidden one.

Full discovery still ends in the [sharpen.md](sharpen.md) report. The report contract is required. When two rules conflict, take the stricter one: empty pain beats a filled map; blank intake beats a manufactured report; a quoted first-framing reject beats a generic label.

## Decision table

| ID | Detect | Required | Forbidden |
|---|---|---|---|
| E01 | Buyer-only: "owners", "SMEs", "the market", "customers", a demographic | Ask at most 3 doer questions from [workaround-map.md](workaround-map.md). "Who does the work" is a named doer. | Treat the persona, market, or buyer as the worker. |
| E02 | Implied solution: "we're building", app, dashboard, AI, marketplace, stack | Park the solution. Discover the suspected problem. Preserve the original sentence. | Architecture, features, or stack before the report. |
| E03 | Bundled symptoms joined by "and" / commas | Split. Score each. One symptom per sharpened sentence. | Average into one platform problem. |
| E04 | No current workaround can be named | Suspect report. Say why. Ranked problems: none. | Invent WhatsApp groups, discounts, hours, household composting, or municipal pickup. |
| E05 | Awareness / education / "people don't know" | Default-reject. Suspect unless a workaround already exists. | An education, literacy, or "AI tutor" product. |
| E06 | "Just tell me what to build" / "give me the stack" | Refuse the skip. Framing present → report or suspect first. Blank intake → ask, do not import the worked example. | A build list, stack, feature menu, or a manufactured market-woman report. |
| E07 | Follow-up reopens a rejected framing | Stay inside sharpened #1. Name the reject again. | Rebuild storage+delivery+education as a platform. |
| E08 | After the report: "ok, what should we build?" | If a report exists, stay inside #1. If not, ask or suspect — do not invent a #1. | A new problem, any already-rejected framing, or a stack. |
| E09 | No person named | Ask at most 3 questions. Unknown worker is allowed. | "Users", "people", or "the market" as the worker. Assumed workarounds. |
| E10 | Several roles in one prompt | Pick the person whose hands are on the cost when it shows up. | Average stakeholders into one user. |
| E11 | Beneficiary feels the outcome; someone else does the job | Map the doer. | Treat the beneficiary as the worker. |
| E12 | Incumbents already racing (neglect 1–2) | Say so. Do not invent a structural gap. | Fake "why this stays unfixed." |
| E13 | Input already names worker + workaround + gap | Verify the sentence contract. Do not redo discovery. Still no product until asked. | Re-bundle, jump to a build, or start a second full run. |
| E14 | Pure implementation: bugfix, types, CSS, refactor | Do not run this skill. | A discovery report on a code task. |
| E15 | Hackathon time pressure / "need a demo tonight" | Still the full report. Speed does not waive headings. | Demo architecture first. |
| E16 | TAM, ICP, market-size, investor slide | Do not score TAM. Score the four problem signals. | TAM as evidence of a good problem. |
| E17 | NGO, government, "inclusion", "empowerment" as the user | Find the doer. Reject the outcome-word framing. Do not copy stall-trader workarounds unless this prompt named them. | An inclusion / empowerment app. |
| E18 | User is attached to a rejected framing | Still reject. Explain. Do not promote it to #1. | "Fine, marketplace it is." |
| E19 | Blank intake fields | Ask. Do not fill gaps. | Invent a market, worker, or workaround, including from the worked example. |
| E20 | A ranked sentence is missing worker, workaround, or gap | Rewrite before ranking. It is still a pitch. | Rank the pitch. |
| E21 | The original sentence *is* the product | Keep it verbatim as Original framing. Extract a suspected problem. | Treat the product name as the problem. |
| E22 | All four signals 1–2 | Reject as feel-safe. Stop or suspect. Do not sharpen into a build. | Sharpen anyway because it is a hackathon. |
| E23 | Mixed 2–3 scores | Split the bundle and rescore before ranking. | Average mixed symptoms into one sentence. |
| E24 | "Millennials", "Africans", "Gen Z", "women in X" as worker | Not a worker. Apply E01. | Accept the demographic. |
| E25 | "Huge opportunity" with nobody paying in time, money, discount, or labor | Suspect. Ranked problems: none. | Ranked problems. Invented farmer or ag workarounds. |
| E26 | Market-woman prompt (spoilage + price + transport) | Use [worked-example.md](worked-example.md). Do not drift. | New product ideas or new symptoms. |
| E27 | Agent wants to skip a report heading | Emit all six headings, or the suspect variant. | Drop "Rejected obvious framings." |
| E28 | A "Recommendations" / "What to build" / "Stack" section appears | Delete it. No solution section. | Feature lists in or after the report. |
| E29 | Temptation to invent workarounds on an empty map | Empty → E04 even when the user says "assume WhatsApp and spreadsheets." Never invent. | Fake tools, chats, spreadsheets, or informal credit, including user-requested fiction. |
| E30 | After #1, user asks about a rejected framing as if it were new | Point back to #1. Do not re-score the reject into a new #1. | A second discovery that undoes the rejects. |

## Worked-example lock

[worked-example.md](worked-example.md) is only for E03 / E26 (stall trader, spoilage + price + transport). Do not copy discounts, informal credit, or transporter fares onto literacy, inclusion, composting, agriculture-greenfield, "African markets," or any other prompt.

## Suspect report

Use when E04, E05, E22, E25, or E29 fires, or when a skip arrives with no framing. Same six headings. No solution section.

**Original framing:** …
**Who does the work:** … (named doer, or "unknown — asked …")
**Current workarounds:** none found — problem is suspect because …
**Signal scores:** fragmentation X/5 · incentive misalignment X/5 · incumbent neglect X/5 · cost bearer X/5
**Rejected obvious framings:** … (quote the user's first framing, then kill it)
**Ranked sharpened problems:** none — empty or theoretical pain. Do not invent a workaround to fill this line.

## Skip-attempt rule

If the user asks for a product, stack, demo, or architecture before those six headings exist, answer with the report or the suspect report. If intake is blank, ask at most 3 doer questions or emit the suspect report with an unknown worker. Not with the build. Not with the market-woman example unless the prompt is that prompt.

## After-report lock

Once a non-suspect report exists:

1. The only legal build question is sharpened problem #1.
2. Rejected framings stay rejected.
3. Do not re-bundle #1 with #2 and #3 into a platform.

E13 is this lock. Verify the sentence; do not emit a second ranked list.
