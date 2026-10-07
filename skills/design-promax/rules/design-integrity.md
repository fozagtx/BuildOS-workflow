# Design Integrity Rules

These rules enforce consistency between the agent's generated code and the real source files in `skill/sources/`.

## Rule 1: Source-First
Always read the actual `.js`/`.tsx` source file from `skill/sources/{Category}/` before generating any UI code. Never guess or hallucinate component APIs, classNames, or icon names.

## Rule 2: Pattern Fidelity
Generated code must match the structural patterns found in the source files:
- `React.forwardRef` wrapping
- `cn()` utility for class merging
- `"use client"` directive at the top
- `displayName` assignment

## Rule 3: Token Integrity
Use only HeroUI semantic design tokens found in the source files:
- Backgrounds: `bg-content1`, `bg-content2`, `bg-content3`, `bg-content4`
- Text: `text-default-500`, `text-default-900`, `text-foreground`
- Borders: `border-default-200`, `border-foreground/10`
- Semantic: `text-warning`, `text-success`, `text-danger`, `text-primary`
- Shadows: `shadow-small`, `shadow-medium`, `shadow-large`

Never use raw Tailwind color classes like `bg-gray-100` or `text-blue-500`.

## Rule 4: Icon Sourcing
All icons must use `@iconify/react` `Icon` component with `solar:` or `gravity-ui:` prefixes. Icon names must be verified against real source file imports — never invented.

## Rule 5: Data Separation
Component state, mock data, and configuration must be in separate data files/modules. Never inline large data structures inside component render logic.

## Rule 6: Source Verification
If a generated component's pattern is uncertain, re-read the relevant source file. The answer is always in `skill/sources/`.

## Rule 7: Landing and desk are not one page
If the product has a public story and a work surface, ship `/` (Navbar + solid full job-line hero + **Features** + How it works + FAQ + human footer) and `/desk` (app Navbar + one Connect + **the same full job line** + form). Never stack them. Theme does not collapse this split. See `case-studies/landing-and-desk.md`.

## Rule 8: One Connect
Landing has zero Connect. Desk has Connect once, in the navbar, labeled Connect. Wrong network is Switch, not a second Connect. Never duplicate the wallet button.

## Rule 9: Use the primitives
Navbar from `basic-navbar.tsx` / `navbars (3)__App.tsx`. Features from `AI/features (1)__App.tsx` + `feature-card.tsx`. How it works from the same FeatureCard as **steps**. Hero size from `hero-sections (4)__App.tsx` with **solid** type (no `bg-clip-text` fade, no chopping `<br />`). Footer from `footers (4)__App.tsx` stripped of ACME newsletter and fake `#` columns. Do not vibe-code substitutes.

## Rule 10: Human chrome
Logo is icon + name only. No job subtitle beside the mark. No chain-name chips, truncated vault addresses, or Pre-flight in the chrome. Live values that the user must copy live inside the form.

## Rule 11: Full job line, every page
If the product has a locked job line, paste it whole on landing **and** desk. Use `text-balance`. Never `<br />` so the second line is three leftover words. Never shorten the desk h1 to the last three words.

## Rule 12: Features is not How it works
Landing compose is hero → Features (`AI/features (1)__App.tsx` category cards) → How it works (steps) → FAQ → footer. Nav includes Features. Skipping Features is a fail.