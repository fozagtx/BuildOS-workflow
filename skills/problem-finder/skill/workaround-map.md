# Workaround Map

Use when identifying what people do today, before any scoring.

## Why this comes first

A real problem already has messy workarounds. Building against a pain nobody is currently paying for — in time, money, discounts, or informal labor — is solutioning in a vacuum.

## Who to map

Map the person **doing the job**. The buyer comes after the doer is named.

| Role | Usually useful? | Caution |
|---|---|---|
| Doer / operator | Yes. Closest to the pain | May lack budget |
| Buyer / sponsor | Only after the doer is clear | Often names a dashboard |
| Beneficiary | Sometimes | May feel the outcome |
| Incumbent vendor | For "why unfixed" | Will defend the current product |

These fail the worker gate: "users", "people", "the market", "SMEs", "restaurant owners", "millennials", "women in X", an NGO, a government, a TAM slide. Those are E01 / E09 / E17 / E24.

## Doer interview (at most 3)

When the user names a buyer, persona, or market, ask only these, then proceed:

1. Whose hands are on the mess at the moment the cost shows up? Name a role that does a job.
2. What do they already do that day — a tool, a discount, an extra hour, a side deal, an informal network?
3. Who would have to change a rule, price, or process for that workaround to disappear — and is that the same person?

If after three answers there is still no doer, emit the suspect report. Do not invent a worker. Do not "state the assumption" that they use WhatsApp, spreadsheets, or any other tool the user did not observe (E29).

## Workaround categories

These are a search list. Only record a category if the user named it or a doer interview actually produced it. Copying "WhatsApp groups" or "spreadsheets" onto a prompt that did not name them is inventing a workaround (E29).

Do not complete this list from imagination, from [worked-example.md](worked-example.md), or because the user said "just assume they use X."

- Spreadsheets, notes, mental books
- Phone calls, WhatsApp groups, informal brokers
- Discounts, early selling, overstocking, splitting inventory
- Unpaid hours, family labor, after-hours catch-up
- Shadow tools stitched together (forms + email + calendar + chat)
- Side deals, favors, and reputation as a substitute for a missing market
- Paying a full-price incumbent for a badly-sized slice of the job

If the user says nobody does the thing (E04) or nobody is paying (E25), the map is empty. Stop. Do not hunt through this list until something looks plausible.

## Template

For each workaround, write:

- Who does it:
- What they do:
- When it happens:
- What it costs them:
- What it fails to cover:
- Who benefits from leaving it messy:

## Suspect-problem rule

If the map is empty, the framing is suspect. Either nobody feels the pain, the wrong worker was named, or the user jumped to a solution that nobody is asking for.

Do not invent workarounds to fill the map (E04, E25, E29). User-requested fiction ("assume WhatsApp and spreadsheets so we can proceed") is still invention. Emit the suspect report in [edge-cases.md](edge-cases.md). Ranked sharpened problems stay empty.
