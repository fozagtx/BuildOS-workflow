---
name: rare-ui
description: >
  Rare UI (rareui.com) — a shadcn-style registry of ~21 rare, single-file React components
  you copy into your project, not a dependency you install. Use when the user wants a
  distinctive/unique animated UI component, mentions "rare ui" / "rareui", or asks for any of
  these components: animated folder, bounce sidebar, hook sidebar, family drawer, proximity
  sidebar, duration picker, fluid orb, scroll progress pill, code block, OTP input, gravity
  letters, GitHub activity heatmap, emoji reaction, notification bell, step player, grid
  reveal, gooey nav, delete button with inline confirm, animated counter / odometer digits,
  matrix orb, task list. Also use when looking for ChatGPT-voice-mode-style orbs, AI loading
  states, spring-animated nav, or iOS-style controls.
---

# Rare UI

Catalog + installer for [rareui.com](https://www.rareui.com/components). Every component is a
single file added through the shadcn CLI into the project's own `components/ui/` directory —
the user owns the code.

## Requirements

- React + Tailwind CSS project already configured for shadcn (`components.json` present). If
  the project isn't set up, run `npx shadcn@latest init` first.
- Most components depend on `motion` (framer-motion's successor package) — the CLI installs
  declared npm deps automatically.
- All components registry-depend on `utils` (`cn` helper → `clsx` + `tailwind-merge`), which
  the CLI resolves on its own.

## Install

```bash
npx shadcn@latest add swamimalode07/rare-ui/<component-name>
```

Component files land in `@/components/ui/<component-name>.tsx` (kebab-case). Import as a
default export:

```tsx
import FluidOrb from "@/components/ui/fluid-orb"
```

Docs/usage/props per component: `https://www.rareui.com/components/<slug>` (slugs are the
names below, concatenated — e.g. `fluidorb`, `bounce-sidebar` → `bouncesidebar`).

## Catalog

| Component | Install name | What it is | Extra deps |
|---|---|---|---|
| Folder Component | `folder-component` | Animated folder; cards fan out on hover, lift open on click, 3D-tilted flap. `color`, `size` (sm/md/lg) props. | motion |
| Code Block | `code-block` | Code block that builds its entire syntax theme from one accent hex. Pass `code` + color. | motion, prism-react-renderer, lucide-react |
| Gravity Letters | `gravity-letters` | Physics gravity field — letters, numbers, emoji, or arbitrary components fall and pile up. | — |
| GitHub Activity | `github-activity` | Contribution heatmap; footer panel expands over the grid ranking top repos. | motion |
| Step Player | `step-player` | iOS-style stepped progress track with play/pause/replay; active step stretches into a filling bar. | motion, flubber |
| Animated Counter | `animated-counter` | Odometer-style number that rolls a wheel of digits to its new value. | motion |
| Fluid Orb | `fluid-orb` | WebGL orb with drifting fluid shading (ChatGPT voice-mode vibe). `size`, `color` props. Ambient, honors reduced-motion. | — |
| Grid Reveal | `grid-reveal` | Loading state for AI-generated images that resolves into the real picture on arrival. | motion |
| Matrix Orb | `matrix-orb` | Dot-matrix orb animating through idle / listening / thinking states. | — |
| Bounce Sidebar | `bounce-sidebar` | Vertical nav list with a spring-animated bouncy active indicator. | motion |
| Hook Sidebar | `hook-sidebar` | Vertical nav list with a dashed rail marking the active item. | motion |
| Proximity Sidebar | `proximity-sidebar` | macOS-dock-style scroll sidebar; items expand as the pointer approaches. | motion |
| Scroll Progress | `scroll-progress` | Reading-progress pill that expands into a squircle menu of jump-to sections. | motion |
| Gooey Nav | `gooey-nav` | Gooey nav bar that visually separates the selected item from the group. | motion |
| Family Drawer | `family-drawer` | Bottom drawer with morphing transitions between stacked views (Family-app style). Built on Vaul. | motion, vaul |
| Duration Picker | `duration-picker` | Gooey spring-animated hours/minutes duration input. | motion, figma-squircle, flubber, react-use-measure, @radix-ui/react-slot |
| OTP Input | `otp-input` | One-time-code input; characters roll into place behind a caret that slides slot to slot. | motion |
| Delete Button | `delete-button` | Delete button that asks for confirmation in place — no dialog. | motion |
| Task List | `task-list` | Checklist that strikes out completed tasks and moves them to the bottom. | motion |
| Emoji Reaction | `emoji-reaction` | iMessage-tapback-style reaction button; opens an Apple-emoji bar, sends floating copies of the pick upward. | motion, react-apple-emojis, lucide-react, @radix-ui/react-slot |
| Notification Bell | `notification-bell` | iOS-style bell with unread-count badge. | motion, @radix-ui/react-slot |

## Notes

- Components are recreations of well-known interactions (Apple/iOS, ChatGPT, Family app) —
  free for personal and commercial use; attribution appreciated; don't resell as a kit.
- Source repo: `github.com/swamimalode07/rare-ui`. Registry JSON: `public/r/registry.json` —
  fetch it to check for new components: `https://www.rareui.com/r/registry.json`.
- When a requested interaction isn't covered here, check the `transitions-dev` /
  `transitions-polish` skills for bespoke CSS transitions instead of a full component.
