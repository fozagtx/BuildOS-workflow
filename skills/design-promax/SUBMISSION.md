# Design ProMax — Submission

## Overview
A skill that gives coding agents access to 462 real HeroUI Pro React source files for building production-ready UIs without hallucination.

## Repository Structure
```
design-promax/
├── .gitignore
├── ARTICLE.md
├── README.md
├── LICENSE
├── CLAUDE.md
├── SUBMISSION.md
├── install.sh
├── install-custom.sh
├── skill/
│   ├── SKILL.md          # Main skill — lookup table + patterns
│   └── sources/           # 462 real source files
│       ├── AI/
│       ├── Application/
│       ├── Charts/
│       ├── E-commerce/
│       └── Marketing/
├── agents/                # Agent role definitions
├── commands/              # Command definitions
├── rules/                 # Design integrity rules
└── tests/                 # Structure validation
```

## Installation
```bash
git clone https://github.com/fozagtx/design-promax.git
cd design-promax
./install.sh -y
```

## Usage Example
Ask your agent: *"Build me a pricing page with HeroUI"*
The agent will read real source patterns from `skill/sources/Marketing/pricing (8)__*.js` and adapt them.
