# AI without brain rot reference

Source: https://youtu.be/5BQgoENYkOc

## Why AI feels different

Cognition already runs through tools and other people (extended mind). Most tools extend a capacity while you choose. LLMs can also replace thinking by emitting finished thoughts. Rot risk: nothing for the mirror to amplify.

## Prompts

### Socratic

```text
You are a Socratic provocator.
Rules:
- Ask one probing question at a time.
- No solutions until I say "solve".
- Call out unspoken assumptions.
- Prefer what / why / how would we know over yes/no.

Domain: [DOMAIN]
My draft belief: [BELIEF]
```

### Hat sequence

User answers between hats:

1. White: evidence we have / lack
2. Red: gut in one sentence
3. Yellow: best-case value
4. Black: top 3 failure modes
5. Green: 3 alternatives
6. Blue: next concrete step

### Code review

```text
Black hat only: list 5 realistic bugs or security holes.
Do not rewrite yet.
Ask which risks I accept before any patch.
```

### Writing

```text
I wrote this:
[PASTE]

Challenge it Socratically. Do not rewrite unless I ask.
Mark every claim that needs a source or example.
```

## Low vs high stakes

AI OK: format, regex, quote search, boilerplate, rename, summarize a doc you already read.

Human-led: thesis, taste, architecture you own, research narrative, anything with your name on it.

## Checklist

- [ ] Stakes classified
- [ ] Hypothesis stated (high stakes)
- [ ] Mode chosen (execute / Socratic / one hat)
- [ ] User can explain the decision in their own words

## Habit 3: Turnstile example (Zcash)

**Facts**

- Shielded ZEC in pools (Orchard, Sapling).
- Unified full viewing key observes; does not spend.
- Ironwood closes Orchard to new deposits at block ~3,428,143.
- Large Orchard balance; many users may not know they are in it.

**Shape**

| Piece | Choice |
|-------|--------|
| Question | Is my ZEC in the closing pool? |
| Input | Viewing key only |
| Output | Orchard = action / else fine / can't see = say so |
| Invariant | No spending key path; memory-only; redacted logs |
| Proof | Live mainnet; OSS CLI; on-chain memo signup |

- Product: https://turnstile-xi.vercel.app
- Repo: https://github.com/Enoch208/Turnstile

### Prompt: deep candidates

```text
Domain: […]
I already read: [URLs + 5-10 system facts]

No generic dashboards.
1. List 5 constraints.
2. One Turnstile-shaped wedge each.
3. Score 0-6.
4. Socratic-challenge the top 2.
I pick. You do not declare a winner.
```

### Prompt: roast pitch

```text
Pitch:
[PASTE]

Socratic + black hat.
Logo-swappable, mocked-core, or Turnstile-depth?
List system facts I must learn first.
```
