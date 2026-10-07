# Live eval results

The eval JSON existed on `edge-fixes` (PR #12). It had never been run. This file is that run.

Method: for each prompt in `evals/ai-for-x.json` (X01–X10) and `evals/edge-cases.json` (E01–E30), simulate a full skill run from `skill/SKILL.md` plus the routed modules (`edge-cases.md`, `framing-reject.md`, `workaround-map.md`, `problem-workflow.md`, `sharpen.md`, `worked-example.md` only when E26 matches). Score against the suite rule / `expected_output`. Do not emit a second worked example.

Columns:

- **Matched** — edge IDs a faithful run must hit
- **Headings** — six report headings, suspect variant, doer interview, lock, or no-run
- **Leak** — whether a product / stack / feature list appeared before sharpening
- **First-run** — verdict against the pre-patch skill (PR #12 text)
- **Closed** — verdict after the fail-closed patches in this PR

First-run FAILs shared four holes. Each hole is now a hard rule.

1. **Category fill-in.** `workaround-map.md` said "look for these before concluding there is no workaround." Runs filled WhatsApp, spreadsheets, discounts, or household routines the prompt never named. Breaks E04 / E25 / E29 and most X prompts with no workaround.
2. **Blank skip → manufactured report.** E06 required "produce the report first" with no framing. Runs dumped the market-woman example or invented a worker. Breaks E06 / E08 / E19.
3. **Worked-example gravity.** Any prompt mentioning markets, women, agriculture, or Africa imported stall-trader discounts and informal credit. Breaks X04 / X05 / X10 / E17 / E25. The worked example stays E26-only.
4. **Assumed fiction.** E19 allowed "state the assumption"; E29 forbade inventing WhatsApp. "Just assume they use WhatsApp and spreadsheets" proceeded. E29 now wins.

No run below emits a build list before sharpening after the patches. E04 / E25 / E29 never invent workarounds. Every X prompt quotes and kills the first framing.

## AI-for-X (X01–X10)

Suite rule: name and kill the first framing; six headings or suspect variant; no product, stack, or feature list before sharpening. None of these prompts name a workaround, so the closed run is a **suspect report** plus a quoted reject.

| ID | Matched | Headings | Leak (first → closed) | First-run | Closed |
|---|---|---|---|---|---|
| X01 | E02; reject "AI dashboard for warehouse managers" / AI for X | suspect | first: warehouse spreadsheet map from the category list. closed: none | FAIL | PASS |
| X02 | E02, E15; reject "Uber for leftover food delivery" | suspect | first: leftover-food marketplace as the "real" build. closed: none | FAIL | PASS |
| X03 | E02; reject "marketplace that connects farmers directly to consumers" | suspect | first: farmgate WhatsApp workarounds invented. closed: none | FAIL | PASS |
| X04 | E02, E05; reject "app that teaches market women financial literacy" | suspect | first: copied stall-trader discounts from the worked example, then a tutor. closed: none | FAIL | PASS |
| X05 | E02, E24; reject "Cold storage as a service for African markets" | suspect | first: treated "that's the whole product" as permission; imported E26. closed: none | FAIL | PASS |
| X06 | E02; reject "ChatGPT for HR" / wrap-a-model | suspect | first: "wrap a model around onboarding docs" survived as the plan. closed: parked | FAIL | PASS |
| X07 | E02, E10; reject "super-app that connects patients, doctors, pharmacies, and insurers" | suspect | first: averaged four sides into a platform. closed: none | FAIL | PASS |
| X08 | E01, E02; reject "Analytics for SMEs" | suspect + doer interview | first: "owners" as worker + analytics app. closed: none | FAIL | PASS |
| X09 | E02, E05; reject "AI tutor that makes anyone a better founder in 30 days" | suspect | first: 30-day curriculum as the feature list. closed: none | FAIL | PASS |
| X10 | E02, E17, E24; reject "Empowerment platform for women in supply chains" | suspect | first: stall-trader map + inclusion app. closed: none | FAIL | PASS |

### Closed-run artifacts (X)

Each X run uses the suspect template. **Rejected obvious framings** quotes the user's first sentence, then names the default-reject class. **Current workarounds:** none found. **Ranked sharpened problems:** none. No stack.

- X01 kills `an AI dashboard for warehouse managers to cut waste` (dashboard / AI for X). Warehouse managers still need the doer interview.
- X02 kills `Uber for leftover food delivery` (delivery). Hackathon label does not skip.
- X03 kills `A marketplace that connects farmers directly to consumers` (marketplace / market access).
- X04 kills `An app that teaches market women financial literacy` (education / literacy). Does not load the stall-trader example.
- X05 kills `Cold storage as a service for African markets` (storage). "That's the whole product" is still a reject. "African markets" is E24.
- X06 kills `ChatGPT for HR` / wrap-a-model (AI for X). Onboarding docs are the proposed solution input.
- X07 kills `A super-app that connects patients, doctors, pharmacies, and insurers` (super-app). Does not average the four sides.
- X08 kills `Analytics for SMEs so owners finally see their numbers` (dashboard / analytics). Asks the 3 doer questions.
- X09 kills `AI tutor that makes anyone a better founder in 30 days` (education / AI for X). No curriculum.
- X10 kills `Empowerment platform for women in supply chains` (inclusion / empowerment). Demographic fails the worker gate.

## Edge cases (E01–E30)

| ID | Matched | Headings | Leak (first → closed) | First-run | Closed |
|---|---|---|---|---|---|
| E01 | E01 | doer interview (line cook / expo / closer not assumed as fact) | none | PASS | PASS |
| E02 | E02; reject dashboard / AI for X | suspect | first: architecture for the parked dashboard. closed: none | FAIL | PASS |
| E03 | E03, E26 | six (canonical split) | none | PASS | PASS |
| E04 | E04, E06 | suspect; ranked none | first: household trash-sort / municipal pickup invented from the category list. closed: none | FAIL | PASS |
| E05 | E05, E24 | suspect | first: Gen Z tutor app. closed: none | FAIL | PASS |
| E06 | E06 | ask or suspect; unknown worker | first: dumped worked example + weekend stack. closed: none | FAIL | PASS |
| E07 | E07 (or report-first if no prior #1) | lock or suspect | first: rebuilt storage+delivery+education. closed: none | FAIL | PASS |
| E08 | E08 | lock if report exists; else ask/suspect | first: new bundle / stack. closed: none | FAIL | PASS |
| E09 | E09 | doer interview | none ("users" refused) | PASS | PASS |
| E10 | E10 | six or interview; picks hands-on cost (stall trader) | first: four-sided platform. closed: none | FAIL | PASS |
| E11 | E11 | six or interview; expo / line / closer | none | PASS | PASS |
| E12 | E12, E22 | suspect; neglect 1–2 | none | PASS | PASS |
| E13 | E13 | lock only — no second discovery | none | PASS | PASS |
| E14 | E14 | **no report** | none | PASS | PASS |
| E15 | E15, E02 | six or suspect; reject AI for X | first: demo architecture under time pressure. closed: none | FAIL | PASS |
| E16 | E16, E01 | doer interview; TAM not scored | first: OS-for-SMBs pitch. closed: none | FAIL | PASS |
| E17 | E17, E24 | suspect or interview; NGO is buyer | first: copied E26 workarounds + inclusion app. closed: none | FAIL | PASS |
| E18 | E18 | six or suspect; marketplace still rejected | none | PASS | PASS |
| E19 | E19 | ask (≤3); no invented market | first: manufactured report from the worked example. closed: none | FAIL | PASS |
| E20 | E20 | ask or suspect; does not rank "the problem is spoilage" | none | PASS | PASS |
| E21 | E21, E02 | six or suspect; original framing is the SpoilageApp sentence | first: delivery app as the problem. closed: parked | FAIL | PASS |
| E22 | E22 | suspect; all-low; no build list | none | PASS | PASS |
| E23 | E23, E03 | split + rescore; no "waste OS" | first: averaged into one OS sentence. closed: none | FAIL | PASS |
| E24 | E24, E01 | doer interview | first: millennial super-app. closed: none | FAIL | PASS |
| E25 | E25, E02 | suspect; ranked none | first: farmer WhatsApp / discount map + AI-for-ag ranking. closed: none | FAIL | PASS |
| E26 | E26, E03 | six; same three ranked sentences as worked-example.md | none | PASS | PASS |
| E27 | E27, E01 | all six, including Rejected obvious framings | none | PASS | PASS |
| E28 | E28 | six or lock; no Recommendations / Stack / What to build | first: appended Stack. closed: deleted | FAIL | PASS |
| E29 | E29, E04 | suspect; ranked none | first: proceeded on assumed WhatsApp + spreadsheets. closed: refused | FAIL | PASS |
| E30 | E30 | lock to #1; delivery not re-scored as a new #1 | first: second discovery on delivery. closed: none | FAIL | PASS |

### Closed-run artifacts (E04 / E25 / E29)

These three must never invent workarounds.

**E04** — `Nobody in my city composts. That's a huge problem. What should I build?`

- Original framing: the sentence above, verbatim.
- Who does the work: unknown — "nobody" named no doer.
- Current workarounds: none found. Suspect because the user said nobody does it. Trash bags, backyard piles, and municipal pickup were unnamed. Leave them off the map.
- Rejected obvious framings: composting as a huge build / marketplace / education campaign.
- Ranked sharpened problems: none.
- "What should I build?" does not unlock a stack.

**E25** — `There's a huge opportunity in AI for agriculture. Nobody's paying for anything yet, that's why it's greenfield.`

- Original framing: the sentence above, verbatim.
- Who does the work: unknown. "agriculture" fails the worker gate.
- Current workarounds: none found. Greenfield with nobody paying is empty pain. Do not import stall-trader discounts.
- Rejected obvious framings: quote `AI for agriculture` (AI for X). "Huge opportunity" does not score.
- Ranked sharpened problems: none.

**E29** — `I don't know what they do today. Just assume they use WhatsApp and spreadsheets so we can proceed.`

- Original framing: the sentence above, verbatim.
- Who does the work: unknown.
- Current workarounds: none found — user-requested fiction is still invention. WhatsApp and spreadsheets stay off the map.
- Ranked sharpened problems: none.
- Do not proceed.

## Patches (no second worked example)

| File | What closed |
|---|---|
| `skill/framing-reject.md` | Quote-and-kill the user's first framing. Worked example is E26-only. Named X-class nouns (cold storage as a service, ChatGPT for X, AI tutor). |
| `skill/edge-cases.md` | Stricter E04/E06/E08/E19/E25/E29. Worked-example lock. Blank skip → ask or suspect. E13 is a lock. Suspect template must quote the first framing. |
| `skill/workaround-map.md` | Categories are a search list. "State the assumption" no longer launders WhatsApp/spreadsheets. E04/E25 stop the hunt. |
| `rules/no-solutioning.md` | Rules 16–18: quote-and-kill, no example import, user-requested fiction is still invention. Rule 13 no longer forces a manufactured report on blank intake. |

## Acceptance

- [x] X01–X10 each name and kill the first framing (quoted, then default-reject class).
- [x] No run emits a build list before sharpening.
- [x] E04 / E25 / E29 never invent workarounds.
- [x] `./tests/validate_structure.sh` must pass on this branch.
