---
name: ui-skills
description: Design-engineering skills for interface craft, accessibility, micro-interactions, layout shift prevention, and polished UI details from UI Skills (ui-skills.com). Trigger when building or refining UI components, styling web surfaces, improving perceived polish, or applying design engineering best practices.
---

# UI Skills: Design Engineering Principles & Playbook

Source: [UI Skills](https://ui-skills.com) by Interface Office & @ibelick

UI Skills is a curated set of design-engineering guidelines, techniques, and playbook rules for building distinctive, production-grade, and highly accessible user interfaces.

---

## 1. Core Playbook Rules

### Rule 1: Prevent Layout Shifts with Aspect Ratio
Never let images or media jump the layout while loading. Always reserve space using `aspect-ratio` or explicit width/height containers.
```tsx
// Good: Zero layout shift
<div className="relative aspect-video w-full overflow-hidden rounded-xl bg-neutral-100 dark:bg-neutral-900">
  <img src="/hero.jpg" alt="Preview" className="object-cover w-full h-full" loading="lazy" />
</div>
```

### Rule 2: Balance Heading Text & Prevent Widows
Use `text-wrap: balance` (`text-balance` in Tailwind) for headlines and `text-wrap: pretty` (`text-pretty`) for body copy to prevent single-word dangling orphans.
```tsx
<h1 className="text-4xl font-bold tracking-tight text-balance">
  Make Any Website 100x Agent Ready
</h1>
<p className="mt-4 text-base text-neutral-600 text-pretty">
  Stop letting AI coding assistants struggle with unstructured HTML scrapers and stale documentation.
</p>
```

### Rule 3: Align Numbers with Tabular Figures
In data tables, counters, timers, price tags, and dashboard stats, use `font-variant-numeric: tabular-nums` (`tabular-nums` in Tailwind) so numbers don't jitter or jump when values change.
```tsx
<span className="font-mono text-sm tabular-nums tracking-tight font-medium">
  $1,482.50
</span>
```

### Rule 4: 44px Minimum Touch Targets
All interactive controls, buttons, toggles, and icon links must have a touch target of at least 44x44px on mobile/touch viewports, even if the visible icon is 16px.
```tsx
<button
  type="button"
  aria-label="Close dialog"
  className="flex h-11 w-11 items-center justify-center rounded-lg hover:bg-neutral-100"
>
  <X className="h-4 w-4 text-neutral-700" />
</button>
```

### Rule 5: Concentric (Nested) Border Radius
When nesting rounded elements inside a parent container, match the inner border-radius mathematically so curves align seamlessly:
$$\text{Radius}_{\text{inner}} = \max(0, \text{Radius}_{\text{outer}} - \text{Padding})$$
* If parent has `rounded-2xl` (16px) and `p-3` (12px padding), child should have `rounded-[4px]`.
* If parent has `rounded-xl` (12px) and `p-2` (8px padding), child should have `rounded-[4px]`.

### Rule 6: Scale Feedback on Press
Provide immediate, tactile visual feedback when interactive buttons are pressed using subtle active scaling.
```tsx
<button className="px-4 py-2 rounded-xl bg-neutral-900 text-white transition-[transform,background-color] active:scale-[0.97] hover:bg-neutral-800">
  Confirm Action
</button>
```

### Rule 7: Optical Alignment vs Mathematical Centering
* **Play Icons**: A triangular play icon has visual weight shifted left; offset it slightly to the right (`translate-x-0.5`) to make it look truly centered inside a circle.
* **Badges & Dots**: Align status dots to the cap-height of uppercase text, not baseline.

### Rule 8: Subtle Image Outlines
Light or white images placed on light backgrounds blend into the canvas. Apply a subtle 1px translucent inset ring or border to give them clean definition:
```tsx
<img src="/screenshot.png" className="rounded-xl ring-1 ring-black/5 dark:ring-white/10" />
```

---

## 2. Design Craft Audit Checklist

When reviewing or building any UI component:
- [ ] Is there keyboard focus visibility (`focus-visible:ring-2`)?
- [ ] Are colors checking WCAG AA 4.5:1 contrast for normal text and 3:1 for large text/icons?
- [ ] Does interactive state provide `hover`, `active`, and `disabled` visual treatments?
- [ ] Are animations kept purposeful and under 300ms?
- [ ] Is dark mode supported with proper surface elevation tokens?
