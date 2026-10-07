# Design ProMax — Agent Skill Article

## What It Is
A self-contained agent skill containing **462 real source files** from HeroUI Pro — a premium React UI component library. Agents read actual `.js`/`.tsx` code, not summaries, so there's zero hallucination.

## Why It Matters
Coding agents that generate UI code often hallucinate component APIs, classNames, and design tokens. Design ProMax eliminates this by providing real, verified source files that agents can read and adapt directly.

## How It Works
1. User requests a UI component (pricing page, login form, chat interface)
2. `skill/SKILL.md` categorizes the request and routes to the correct source files
3. Agent reads real `.js`/`.tsx` code from `skill/sources/{Category}/`
4. Agent adapts verified patterns — no guessing, no hallucination

## Key Features
- **462 real source files** across 5 domains: AI, Application, Charts, E-commerce, Marketing
- **HeroUI design system** — semantic tokens, React.forwardRef, cn()
- **Iconify integration** — real icon imports, not guesses
- **Zero hallucination** — every pattern is backed by real code
