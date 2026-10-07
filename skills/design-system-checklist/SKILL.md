---
name: design-system-checklist
description: Comprehensive checklist for designing, building, and auditing design systems, foundations, and core UI components from Design System Checklist (designsystemchecklist.com). Use when creating component libraries, auditing UI completeness, or implementing any of the 28+ core UI components.
---

# Design System Checklist: Foundations & Component Specifications

Source: [Design System Checklist](https://designsystemchecklist.com) by Arda Karacizmeli

Use this skill as an authoritative specification guide when architecting, reviewing, or building design systems and UI components.

---

## 1. Foundations Checklist

### A. Color & Contrast
- [ ] **Accessibility (WCAG AA)**: Normal text ($\ge 4.5:1$), Large text/headings ($\ge 3:1$), UI components and borders ($\ge 3:1$).
- [ ] **Semantic Color Tokens**: Action/Brand, Surface/Background, Border, Danger/Error, Warning, Success, Info.
- [ ] **Dark Mode Adaptability**: Mapped semantic tokens that adapt automatically to `prefers-color-scheme`.
- [ ] **Color Independence**: Never rely on color alone to convey state; pair with icons, text badges, or assistive labels.

### B. Layout & Grid
- [ ] **Granular Units**: 4pt or 8pt baseline grid system ($4, 8, 12, 16, 20, 24, 32, 40, 48, 64$).
- [ ] **Responsive Breakpoints**: Predefined sizes for Mobile (`sm: 640px`), Tablet (`md: 768px`), Desktop (`lg: 1024px`), Wide (`xl: 1280px`).
- [ ] **Fluid Spacing Scale**: Standardized margin and padding steps.

### C. Typography
- [ ] **Type Scale**: Defined steps for Display, Headline, Title, Body, Label, and Mono/Code.
- [ ] **Readability**: Line heights ($1.1$ for large display, $1.4–1.6$ for body copy), tracking (tighter for large headlines, wider for small uppercase mono).
- [ ] **Font Fallbacks**: System font stacks to prevent Flash of Unstyled Text (FOUT) and layout shifts.
- [ ] **Tabular Figures**: `tabular-nums` enabled for data tables and financial figures.

### D. Elevation & Surfaces
- [ ] **Light Mode**: Communicated through multi-layer shadows (e.g. `shadow-sm`, `shadow-md`, `shadow-lg`).
- [ ] **Dark Mode**: Communicated through lighter surface luminance rather than blur shadows (e.g. Canvas `#0D0E0F` $\rightarrow$ Card `#151617` $\rightarrow$ Dropdown `#1E2022`).
- [ ] **Z-Index System**: Layered scale (`10` sticky nav, `20` drawer/sidebar, `30` backdrop/overlay, `40` modal dialog, `50` toast notifications).

### E. Iconography
- [ ] **Visual Bounding Box**: Uniform 16x16, 20x20, or 24x24 pixel frames.
- [ ] **Semantic Naming**: Name by purpose (`play`, `search`, `settings`), not geometry (`triangle`, `circle`).
- [ ] **Accessibility**: Purely decorative icons have `aria-hidden="true"`; functional icons have `aria-label`.

---

## 2. Core 28 Component Implementation Standards

When implementing or reviewing any component, verify its required states:

| Component | Required States & Behaviors |
|---|---|
| **Button** | `default`, `hover`, `active`, `focus-visible`, `loading` (spinner preserves width), `disabled`, `asChild` link variant. |
| **Input / Textarea** | `default`, `focus`, `error` (with error message), `disabled`, `placeholder`, `prefix/suffix icon`, clear button. |
| **Select / Dropdown** | `trigger`, `open`, `item hover`, `item selected`, `keyboard navigation (arrows, Enter, Esc)`, `focus trap`. |
| **Modal / Dialog** | `backdrop`, `open/close transition`, `focus trap to first element`, `Esc to close`, `aria-labelledby`, `aria-describedby`. |
| **Toast / Alert** | `info`, `success`, `warning`, `error`, `auto-dismiss timer`, `action button`, `accessible live region (aria-live)`. |
| **Checkbox / Radio / Switch** | `checked`, `unchecked`, `indeterminate` (checkbox), `disabled`, `label click target`, `keyboard toggle (Space)`. |
| **Tabs** | `active tab indicator`, `keyboard navigation (Left/Right arrows)`, `aria-selected`, `panel transition`. |
| **Avatar** | `image loading`, `image fallback (initials/icon)`, `sizes (sm, md, lg)`, `avatar stack group`. |
| **Badge / Tag** | `solid`, `subtle`, `outline`, `dismissible (x button)`, `status dot`. |
| **Skeleton** | `shimmer / pulse animation`, `matches final component aspect-ratio`, `respects prefers-reduced-motion`. |
| **Table** | `sticky header`, `hover row`, `selected row`, `sortable column headers`, `tabular numbers`, `empty state`. |
| **Pagination** | `active page`, `page range truncation (...)`, `prev/next controls`, `disabled boundaries`. |
