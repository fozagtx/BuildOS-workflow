# Layout principles & grids

Layout principles arrange elements so the page tells a visual story — not just a stack of blocks.

## 1. Visual hierarchy

Guide what is seen first, second, third. Everything learned for type (size, weight, contrast, space) also applies to imagery and layout chrome.

Levers beyond type: image scale, color blocks, crop, overlap, position in the frame.

## 2. Balance

Distribute visual weight so nothing accidentally dominates.

### Symmetrical

Mirror or equal structure across a central axis. Calm, formal, stable.

Example pattern: centered headline, evenly spaced nav items (equal gaps), balanced bottom image.

### Asymmetrical

Unequal sides that still feel resolved — large/heavy element balanced by smaller elements, space, or strong alignment. More movement; default for modern editorial storytelling.

Do not confuse “empty” with “unbalanced.” White space is a weight.

## 3. Proximity

Elements near each other read as related; distance separates groups.

Effects:

- **Relationships** — menu cluster vs headline+image cluster vs standalone body
- **Readability** — users process one group, then jump to the next
- **Clarity** — spacing explains structure without boxes

Technique: tighten within a group, loosen between groups. Prefer proximity over cards when cards add no interaction.

## 4. Alignment

Shared edges and axes create order.

- Align headline, meta, and body to the same vertical guides
- Align captions to image edges or column lines
- One intentional break beats many accidental ones

Benefits: visual order, faster scanning, professional finish.

---

## Grids

A grid is horizontal + vertical lines that organize content into columns, rows, modules, and gutters.

**Job of a grid:** order, consistency, balanced placement — and a way to execute hierarchy, proximity, and alignment together.

### Anatomy

| Part | Role |
|------|------|
| Columns | Vertical tracks for content width |
| Rows | Horizontal tracks / modules |
| Modules | Column × row cells |
| Gutters | Space between columns |
| Margins | Outer inset from the canvas |
| Baseline grid | Vertical rhythm for type |

### Recipes from the course

**A. Custom editorial columns (halving math)**  
Start with full width → center split → symmetrical side margins → halve a column → place a narrow meta column. Align type and ornaments to those verticals; add horizontals so stars, paragraph ends, and big numerals share baselines.

**B. Square module grid**  
Equal square cells (e.g. 370×370) with large outer margin. Image fills ~50%; headline locks to a module and may overlap the image; paragraph centers on a column intersection; small codes (C1, etc.) share alignments for balance.

**C. Many-column + baseline**  
e.g. 11 columns, no gutters, 20px baseline. Headline spans six columns; meta in col 8; nav in last; body split across column spans with intentional gaps for editorial air; image + credit stabilize the bottom.

**D. Classic 8-column**  
Margins + ~16px gutters. Centered article: date → full-bleed-width headline → 4-col subline → full-width image. Proves a basic grid is enough.

**E. Two-column asymmetric (60/40)**  
Fixed max width (e.g. 1160) + 20px rhythm. Full-width image, then 60/40 split for numbers/type; repeat 20/40 spacing so whitespace feels intentional, not empty.

### Grid practice rules

- Invent the grid that serves the composition — not only Bootstrap defaults
- Once set, stay consistent across subpages
- Use the grid to allocate primary / secondary / tertiary space
- Overlap type and image for depth only when contrast holds
- Classic grids are valid; complexity is optional

---

## Putting all four together

| Need | Tool |
|------|------|
| What to look at first | Hierarchy |
| Does it feel stable or alive? | Balance (sym / asym) |
| What belongs together? | Proximity |
| Why does it feel neat? | Alignment + grid |

Maximum quality appears when all four are conscious — not when only a 12-column template is applied.

## Web mapping

- CSS Grid for page frames; `gap` as gutters
- Shared `max-width` + horizontal padding as margins
- Type `line-height` multiples that match a baseline story when possible
- Avoid centering long body copy
- Prefer alignment to a few vertical axes over card grids for editorial marketing pages
