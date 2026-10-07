---
name: purposeful-ui-motion
description: Emil Kowalski's motion design engineering principles (from emilkowal.ski/ui/you-dont-need-animations) on deciding when to animate, when NOT to animate, optimizing perceived speed, and building purposeful UI micro-interactions. Use when adding animations, transitions, Framer Motion, CSS transitions, hover/active states, toasts, dialogs, or auditing animation performance.
---

# Purposeful UI Motion: When and How to Animate

Source: [You Don't Need Animations](https://emilkowal.ski/ui/you-dont-need-animations) by Emil Kowalski

When done right, animations make an interface feel predictable, faster, and more enjoyable to use. But when overdone, they make an app feel sluggish, delayed, and annoying.

---

## 1. The Core Motion Rules

### Rule 1: Never Animate High-Frequency Actions
If a user interacts with a feature dozens or hundreds of times a day (like Raycast command palettes, search bars, rapid menu toggles, or list item hovers in daily tools), **do not animate it**. The optimal experience is an **instant 0ms response**.

### Rule 2: Never Animate Keyboard-Initiated Navigation
Arrow key navigation through a command palette, dropdown list, or search results must move the focus highlight **instantly**. Transitioning a highlight bar across list items with a 200ms delay feels disconnected from the user's keystrokes.

### Rule 3: Keep UI Animations Fast (< 300ms)
Unless you are building marketing hero storytelling, all product UI animations must stay under **300ms**:
* **Dropdowns & Menus**: ~150ms–180ms
* **Dialogs & Modals**: ~200ms
* **Toasts**: ~200ms–250ms
* **Hover State Fades**: ~100ms–150ms

### Rule 4: Every Animation Must Have a Defined Purpose
1. **Explain Functionality**: Visually illustrating what a complex feature does (e.g. Linear's Product Intelligence demo).
2. **Tactile Feedback**: Subtle active scaling (`active:scale-[0.97]`) so the button feels physical and responsive.
3. **Spatial Continuity**: Toasts and drawers entering and exiting in the same direction so swipe-to-dismiss gestures feel natural.
4. **Infrequent Delight**: Morphing shapes (e.g. feedback widget) work well only because users interact with them rarely.

### Rule 5: Perceived Performance & Illusions
* A faster-spinning loading spinner makes the application feel like it's loading quicker, improving perceived performance.
* Faster opening menus make the entire application feel lighter.

### Rule 6: Tooltip Delay & Chaining
* **Initial Tooltip**: Add a slight delay (~300ms) before opening to prevent accidental triggers while moving the mouse across the screen.
* **Chained Tooltips**: Once any tooltip is active, moving the mouse to adjacent tooltips must display them **instantly with 0ms delay**.

### Rule 7: Always Support Reduced Motion
Respect `prefers-reduced-motion: reduce` by replacing spatial slide/scale animations with instant appearances or simple opacity fades:
```css
@media (prefers-reduced-motion: reduce) {
  *, ::before, ::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```
