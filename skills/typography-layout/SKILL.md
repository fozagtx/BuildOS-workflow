---
name: typography-layout
description: >-
  Apply typography anatomy, best-font selection and setting (weight, tracking,
  leading, case), font classification, legibility vs readability, type-only
  visual hierarchy, font pairing recipes, and editorial layout principles
  (balance, proximity, alignment, grids). Use whenever choosing or setting
  fonts, pairing type, building type hierarchy, pairing faces, designing
  editorial/marketing/portfolio layouts, or reviewing UI that looks typographically
  weak. Trigger on: typography, fonts, which font, font pairing, type hierarchy,
  baseline grid, tracking, kerning, x-height, serif, sans, display type, editorial
  layout, letterforms, line length, "make the type better". Use proactively on any
  frontend that sets headlines, body copy, or multi-column page structure — do not
  wait to be asked.
---

# Typography & Layout Masterclass

Universal skill — callable from **any harness** that can read skills:

```bash
npx openskills read typography-layout
```

Also loads from `~/.cursor/skills/typography-layout/` (Cursor), `~/.claude/skills/typography-layout/` (Claude Code), and `~/.agents/skills/typography-layout/`.

Operational rules from a full typography + editorial layout course. Apply when building or reviewing any text-led interface.

## Quick decision flow

1. **Pick the best font for the job and set it correctly** → [best-fonts.md](references/best-fonts.md) ← start here for “which font?”
2. **Confirm classification / mood fit** → [font-classifications.md](references/font-classifications.md)
3. **Lock body for legibility**, then tune readability (size, leading, measure, contrast)
4. **Build hierarchy with type only** (size, weight, style, contrast, space, alignment, indent)
5. **Pair a second face with intent** → [font-pairing.md](references/font-pairing.md)
6. **Compose the page** (balance, proximity, alignment, grid) → [layout-principles.md](references/layout-principles.md)

Anatomy (baseline, x-height, ascenders/descenders, stroke, counter, terminal, kerning vs tracking): [fundamentals.md](references/fundamentals.md).

---

## Non-negotiables

- **Typography is the design.** Wrong face, size, leading, or pairing ruins the layout.
- **Picking a font is not enough — setting it is the craft.** Weight, tracking, leading, case, and measure decide whether a “good” font looks good.
- **Legibility ≠ readability.** Legibility ≈ the font. Readability ≈ what you set.
- **Hierarchy before decoration.** Size, weight, space, contrast first.
- **Air over clutter.** Compressed stacks look amateur.
- **1–3 type sizes, not 5–7.**
- **Industry norms are starting points, not laws.** Explore, then justify.

---

## Best fonts (compressed)

Full tables, tracking values, pairings, and web stand-ins: **[best-fonts.md](references/best-fonts.md)**.

**Serif workhorses**

| Role | Pick | Set it like this |
|------|------|------------------|
| Long copy + headlines | Caslon-like old style | Book/regular body; full family weights |
| Heritage / polished | Historic old-style (Bartok-like) | Works large and in paragraphs |
| Fashion display | Didone / Sol Display-like | Large only; prefer italic for short blocks; never small UI body |

**Sans workhorses**

| Role | Pick | Set it like this |
|------|------|------------------|
| Compact headlines | Swiss grotesque-like | Slight **negative tracking** on big heads; leave body alone |
| Long sans paragraphs | Basier-like clean sans | Course example: head **−4%**, body **−2%** tracking |
| Personality heads | Characterful sans (Ionic-like) | Keep large — weak at small sizes |

**Never for long text:** ultra-thin, ultra-black, extreme condensed, tiny-counter display, high-contrast Didone at small sizes.

**Decorative / display:** don’t retune their tracking; use for short strings, numbers, titles.

---

## Legibility (font choice)

| Factor | Prefer for body | Avoid for long text |
|--------|-----------------|---------------------|
| X-height | Taller | Tiny x-height |
| Width | Average | Extreme condensed/extended |
| Weight | Book / Regular | Ultra-thin or ultra-black |
| Stroke contrast | Moderate | Extreme Didone at small sizes |
| Counters | Open, consistent | Tiny counters in heavy faces |

Display/decorative/script attract and set mood — they do not carry articles.

---

## Readability (you control this)

- **Size:** comfortable body; smaller type needs more leading + open counters
- **Line height:** body ~1.4–1.6×; display tighter OK
- **Measure:** ~**40–70 characters** / `max-w-[65ch]`
- **Case:** all-caps for short labels, not long paragraphs
- **Contrast:** strong type-vs-background; bias higher for non-Retina
- **Tracking:** tighten display if the face wants it; never crush body; leave decorative alone
- **Kerning:** pair fixes (`AV`, `To`) ≠ tracking (uniform)

---

## Type-only visual hierarchy

1. Size / scale  
2. Weight / style (bold = importance; italic = quotes/asides)  
3. Contrast (color tone, face change, style)  
4. White space  
5. Alignment (left = long reading; center = short titles; justify = editorial long-form; right = rare)  
6. Indent (first-line, block, drop-cap style)

Same-hue tone shifts often beat loud accent colors. Quote pattern: size bump + italic + reposition.

---

## Font pairing (compressed)

Full recipes: [font-pairing.md](references/font-pairing.md) + named recipes in [best-fonts.md](references/best-fonts.md).

1. Name mood (incl. dual stories — e.g. sports + heritage)
2. Primary face + counterpart with clear roles
3. Progressive explorations: safe → shift → hybrid headline mix
4. ≤3 sizes; don’t let two divas share size/weight

---

## Layout composition

| Principle | Job |
|-----------|-----|
| Visual hierarchy | Eye path: 1st, 2nd, 3rd |
| Balance | Sym = calm; asym = editorial energy |
| Proximity | Near = related |
| Alignment + grid | Shared axes; columns/rows/gutters/baseline |

Details: [layout-principles.md](references/layout-principles.md).

---

## Implementation checklist

- [ ] Distinct display + body (or one face with clear weight roles)
- [ ] Face chosen from [best-fonts.md](references/best-fonts.md) logic — not Inter-by-default
- [ ] Weight/tracking/leading/case set per role
- [ ] ≤3 primary sizes; measure ~40–70ch
- [ ] Hierarchy clear without card chrome
- [ ] Alignment axes + proximity groups
- [ ] Air around hero type
- [ ] Contrast OK on non-Retina
- [ ] Long copy not centered; display faces not used as body

## Review mode

Report: (1) hierarchy in <2s, (2) body face fit, (3) settings, (4) pairing roles, (5) layout principles, (6) top 3 fixes.
