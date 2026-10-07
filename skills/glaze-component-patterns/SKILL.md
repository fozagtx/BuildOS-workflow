---
name: glaze-component-patterns
description: Build or modify native macOS-style Glaze renderer UI with the design system. Use for layouts, sidebars, toolbars, forms, dialogs, lists, grids, tables, component selection, semantic styling, scrolling, sticky regions, overlays, or any custom UI markup.
---

# Glaze Component Patterns

Glaze apps should resemble native macOS applications: flat surfaces, separation by structure, design-system components over custom markup, and semantic tokens over raw values.

## Component-first gate

1. Find the pattern in [component-catalog.md](references/component-catalog.md).
2. Before writing it, use `glaze-component-docs-reader` to read the component's exact props, variants, composition, and pitfalls.
3. If it is absent, search the runtime `SDK Symbol Lines` for the component name. Only write custom markup after confirming the design system has no equivalent.

## Non-negotiable rules

- Import UI, hooks, and utilities only from their public `@glaze/core/{components,hooks,utils}` entrypoints.
- Do not hand-roll raw controls or layout primitives when a Glaze component exists.
- Every movable app-owned window needs a `Toolbar`, a `Sidebar`, or an explicit top drag region.
- Use `SplitView` only for sidebar/list/primary/inspector app shells; use `PanelGroup` for other resizable layouts.
- Keep one visible `variant="accent"` primary action per screen or dialog.
- Render text with `Text` variants or matching semantic utilities; never use raw palette colors or web-card styling.
- Prefer component props before `className` overrides. Components own their native sizing, radius, focus, and interaction behavior.

## Read only the file(s) for the task

- Choosing a component, import, hook, or utility; replacing raw HTML; or locating its usage doc: read [component-catalog.md](references/component-catalog.md).
- Building an app shell, panels, toolbars, sidebars, dialogs, selection UI, settings rows, or forms: read [layout-and-forms.md](references/layout-and-forms.md) plus the selected component docs.
- Writing custom markup, typography, colors, radii, spacing, sticky regions, or overlays; debugging paint order or stacking: read [custom-styling-and-overlays.md](references/custom-styling-and-overlays.md).

## Verification gate

- No raw HTML where a design-system component exists.
- Every used component was checked against its current documentation.
- The window has a drag affordance.
- `SplitView`, dialogs, fields, and primary actions match their decision rules.
- Custom markup uses semantic typography, colors, radii, and spacing.
- Flexible text has `min-w-0`; fixed icons have `shrink-0`; changing numbers use `tabular-nums`.
- Overlays portal or otherwise avoid ancestor clipping and stacking traps.

Use `glaze-icon-usage` for icon coloring, `glaze-theming` for app-wide colors, and `glaze-browser-window-recipes` for window surfaces.
