---
name: ai-saas-app-playbook
description: >-
  Build revenue-first AI / mobile / SaaS apps using the BusDownBonnor (Connor Burd)
  playbook: distribution-first ideas, competitor onboarding teardown, vibe-code
  core loop, frictionless onboarding + paywall, influencer/UGC then paid ads.
  Use when the user wants to build a consumer SaaS or subscription app with AI,
  mentions BusDownBonnor, vibe coding for revenue, Face Harmony-style app reviews,
  influencer equity apps, or "how do successful AI app founders ship."
---

# AI SaaS / Mobile App Playbook (BusDownBonnor)

Source synthesis from Connor Burd (@BusDownBonnor) public playbook - including his
$4M+ ARR founder framing and app-review style breakdowns (e.g. thoughts on apps
like Face Harmony). Apply this to **any** consumer AI, utility, or SaaS mobile
app, not only climate or Graz.

Primary public references:
- https://x.com/BusDownBonnor/status/2080174335432458311
- Starter Story / Indie Hackers interviews on his vibe-code + distribution process

## When to use

- Greenfield consumer app / micro-SaaS
- "Build something that can make money fast with AI coding"
- Onboarding, paywall, or growth strategy for a subscription app
- Reviewing whether an app idea is distribution-ready

## Non-goals

- Enterprise sales motions, long B2B procurement
- Social apps that require two-sided liquidity on day one
- Perfect architecture before a paying user exists

---

## 1. Pick the game before you pick the stack

Build for **core human desires** that people already pay for:

- Make money / save money
- Look better / feel healthier
- Status / belonging / clarity on something they obsess over

Prefer **utility apps complete for a single user** (one person gets value alone).
Avoid social graphs until you have retention without them.

**Distribution test (fail = do not build yet):**

1. Who already has the audience? (influencer, niche community, SEO term)
2. Can a 15-30s short explain the value without a tutorial?
3. Is there a proven adjacent app making money you can twist, not invent from zero?

If you cannot answer all three, stop and find a better wedge.

---

## 2. Steal onboarding structure, invent the theme

Before writing product code:

1. Download ~15-20 apps in the niche + a few "beautiful" apps outside it.
2. Screenshot **every onboarding + paywall screen**.
3. Lay them in one Figma row. Tag: emotion, personalization, social proof, charts, commitment, paywall.
4. Cherry-pick the strongest pattern into **your** theme - do not copy pixels; copy the conversion sequence.

Rule of thumb: **most users never see the main app**. Onboarding + paywall are the product for acquisition.

Onboarding must:

- Invoke emotion (fear of missing out, hope, identity)
- Personalize (questions that make the result feel "about me")
- Show a chart / score / preview of value before the paywall
- Land on a paywall that prefers **yearly** (or highest LTV) with a clear weekly comparison

---

## 3. Spec data before you vibe-code

AI coding is fast only when the model knows the shape of truth.

Create a short `data-model.md` (or JSON examples) with:

- Core entities and fields
- What is computed vs stored
- What the user must complete in session 1

Then build in this order:

1. **Core loop** (the one screen that delivers the promise) - skip chrome
2. Persistence + auth enough to not lose progress
3. Onboarding + paywall last (or in parallel once the loop is real)
4. Analytics events on: install → onboarding step → paywall view → purchase → day-1 return

Stack pattern that matches this playbook (adapt freely):

- Expo / React Native for client
- Simple BaaS or serverless DB (Neon, Firebase, etc.)
- RevenueCat (or equivalent) for subscriptions
- Mixpanel / Amplitude for funnels
- AI coding agent (Cursor / Claude) with screenshots + data model in context

---

## 4. Ship a thin wedge, not a platform

Day-1 feature budget: **1-3 sharp features**.

Delete anything that does not:

- Make the core promise obvious in under 10 seconds, or
- Improve conversion / retention in the first session

Complexity is the enemy of paid UA and influencer demos.

---

## 5. Growth sequence (do not skip steps)

```
Audience / proof  →  Influencer or UGC  →  Creative winners  →  Paid ads
```

1. **Partner distribution** - build with someone who already has the niche audience (equity or rev share is fine). Analyze their content before the call; pitch ideas *they* can promote naturally.
2. **UGC pipeline** - many short creatives; keep what retains + converts.
3. **Paid ads** - only after you have creatives and a healthy paywall conversion.
4. **ASO** - title/subtitle/screenshots that match the winning ad hook.

Instrument:

- Onboarding completion rate
- Paywall conversion (trial → paid if applicable)
- D1 / D7 retention
- CAC payback

Kill or rewrite onboarding before you blame ads.

---

## 6. Founder review checklist (use on any app)

When reviewing an app (yours or a competitor), score harshly:

| Area | Pass looks like |
|------|-----------------|
| Hook | One sentence a stranger understands |
| Onboarding | Emotion + personalization + preview before pay |
| Paywall | Clear value, LTV-biased plan, no confusion |
| Core loop | Delivers promise without a manual |
| Proof | Scores, before/after, or social proof in-product |
| Distribution | Obvious who would post this and why |
| Retention | Reason to open tomorrow without a push guilt trip |

If hook or distribution fails, do not polish UI - change the wedge.

---

## 7. Agent workflow (apply in this repo or any app)

When the user asks you to execute this skill:

1. Write a 1-page **wedge brief**: desire, audience, proven comps, distribution owner.
2. Produce an **onboarding wire outline** (screen list + purpose of each).
3. Produce a **data-model.md** for the core loop.
4. Implement core loop first; resist feature creep.
5. Add analytics events before growth experiments.
6. Only then: paywall copy variants + creative brief for UGC/ads.

### Output templates

**Wedge brief**

```markdown
# Wedge
- Desire:
- Who pays:
- Comp apps:
- Twist:
- Distribution owner:
- 10-second hook:
```

**Onboarding outline**

```markdown
1. Emotion screen - …
2. Question - …
3. Personalization - …
4. Value preview / score - …
5. Social proof - …
6. Paywall - weekly vs yearly
```

---

## Anti-patterns

- Building for 6 months before a stranger sees a paywall
- "Platform for X" with empty two-sided markets
- Pretty UI with no distribution plan
- Asking AI to invent product strategy without competitor onboarding screenshots
- Optimizing backend while onboarding conversion is < a clear baseline

---

## Reminder

Speed is a feature. In an AI-build era, **validation is shipping + distribution**, not waitlists.
Keep the app simple, the onboarding sharp, and the growth loop owned by someone who already has attention.
