---
name: coss-ui
description: Design engineering guidelines, design token architecture, and open-source enterprise UI component specifications from COSS UI (coss.com/ui). Use when architecting design systems, building commercial open-source SaaS interfaces, standardizing tokens, or implementing clean developer-first UI components.
---

# COSS UI: Enterprise Design Engineering & Tokens

Source: [COSS UI](https://coss.com/ui)

COSS UI provides production-ready design engineering standards, token hierarchies, and component architecture for modern developer-focused software, SaaS dashboards, and commercial open-source web applications.

---

## 1. Design Token Hierarchy

COSS UI organizes tokens into a 3-layer architecture:

```
┌──────────────────────────────────────────────┐
│ Global Tokens (Primitives)                   │
│ e.g. blue-500, gray-900, radius-12px, font-sans│
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│ Semantic Tokens (Context & Roles)            │
│ e.g. surface-canvas, surface-card, border-subtle,│
│ text-primary, text-muted, accent-brand       │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│ Component Tokens (Scoped)                    │
│ e.g. button-height, table-row-padding        │
└──────────────────────────────────────────────┘
```

### Semantic Token Specifications

| Token | Light Value | Dark Value | Usage |
|---|---|---|---|
| `surface-canvas` | `#FFFFFF` / `#FAFAF9` | `#0B0D0E` / `#0D0E0F` | Main background |
| `surface-panel` | `#FFFFFF` | `#151617` / `#16181A` | Cards, modals, sidebars |
| `surface-elevated` | `#F5F2F0` | `#1C1E21` | Popovers, dropdown menus |
| `border-subtle` | `#E4E6EE` / `rgba(0,0,0,0.08)` | `rgba(255,255,255,0.08)` | Dividers, card borders |
| `border-strong` | `#151617` / `#CBD0DF` | `rgba(255,255,255,0.18)` | Form inputs, active borders |
| `text-primary` | `#151617` / `#0F172A` | `#FAFAF9` / `#F8FAFC` | Headings, primary body |
| `text-secondary`| `#475569` / `#64748B` | `#94A3B8` | Subtitles, labels |
| `text-muted` | `#94A3B8` | `#64748B` | Timestamps, placeholders |

---

## 2. Density & Layout Modes

COSS UI supports 3 standard interface densities:

1. **Compact (`density-compact`)**:
   * Row heights: 32px
   * Font size: 12px / 13px
   * Best for: Data tables, code editors, log viewers, metrics grids.

2. **Standard (`density-standard`)**:
   * Row / Control heights: 40px
   * Font size: 14px
   * Best for: SaaS dashboards, settings pages, form inputs, tool studios.

3. **Comfortable (`density-comfortable`)**:
   * Control heights: 48px–52px
   * Font size: 16px
   * Best for: Marketing landing pages, auth screens, public checkouts.

---

## 3. Data Attribute Styling Convention

Style interactive component states using HTML5 `data-*` attributes for seamless headless UI integration:

```tsx
// Using data-state for dropdowns, accordions, and dialogs
<button
  data-state={isOpen ? "open" : "closed"}
  className="px-3 py-1.5 rounded-lg border border-subtle transition-colors data-[state=open]:bg-neutral-100 dark:data-[state=open]:bg-neutral-800"
>
  Menu
</button>
```

---

## 4. Engineering Principles
* **Zero Runtime Overhead**: Prefer Tailwind utility classes and CSS variables over CSS-in-JS runtimes.
* **Radix / Headless Primitives**: Use unstyled accessible building blocks for complex widgets (Dropdowns, Dialogs, Tooltips, Tabs).
* **Keyboard First**: Every action reachable via mouse must be accessible via Tab, Shift+Tab, Enter, Space, and Escape.
