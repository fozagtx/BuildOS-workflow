# Kaizen Rules Reference

## Absolute user rules (never override)

1. **No AI co-author trailers.** NEVER include `Co-Authored-By: Claude`, `Co-Authored-By: Codex`, or any Anthropic/`noreply@anthropic.com` trailer in git commits. The user's git author identity is the only identity on commits.
2. **No assistant mentions in artifacts.** NEVER mention "Claude", "Codex", "Anthropic", or any assistant in PR descriptions, issue comments, code comments, or committed artifacts unless explicitly asked in that exact thread.
3. **Strip accidental trailers.** If a Co-Authored-By trailer somehow lands in a commit, immediately `git commit --amend` to strip it and `git push --force-with-lease`.

## SuperClaude framework references

Core framework files live in `~/.claude/` and are also mirrored in `~/.codex/AGENTS.md`:

- `BUSINESS_PANEL_EXAMPLES.md`
- `BUSINESS_SYMBOLS.md`
- `FLAGS.md`
- `PRINCIPLES.md`
- `RESEARCH_CONFIG.md`
- `RULES.md`

Behavioral modes:

- `MODE_Brainstorming.md`
- `MODE_Business_Panel.md`
- `MODE_DeepResearch.md`
- `MODE_Introspection.md`
- `MODE_Orchestration.md`
- `MODE_Task_Management.md`
- `MODE_Token_Efficiency.md`

MCP docs:

- `MCP_Context7.md`
- `MCP_Magic.md`
- `MCP_Morphllm.md`
- `MCP_Playwright.md`
- `MCP_Sequential.md`
- `MCP_Serena.md`
- `MCP_Tavily.md`

Load these when the user invokes the corresponding mode or tool.

## Claude Code behavioral rules (from ~/.claude/RULES.md)

### Priority system

- **🔴 CRITICAL**: Security, data safety, production breaks — never compromise.
- **🟡 IMPORTANT**: Quality, maintainability, professionalism — strong preference.
- **🟢 RECOMMENDED**: Optimization, style, best practices — apply when practical.

### Workflow

- **Task pattern**: Understand → Plan (with parallelization analysis) → TodoWrite(3+ tasks) → Execute → Track → Validate.
- **Batch operations**: ALWAYS parallel tool calls by default; sequential ONLY for dependencies.
- **Validation gates**: Always validate before execution, verify after completion.
- **Quality checks**: Run lint/typecheck before marking tasks complete.
- **Discovery first**: Complete project-wide analysis before systematic changes.

### Planning efficiency

- Explicitly identify parallelizable operations.
- Plan optimal MCP server combinations.
- Map dependencies (sequential vs parallel).

### Implementation completeness

- No partial features. If you start, finish to a working state.
- No TODO comments for core functionality.
- No mock objects, fake data, or stub implementations.
- Real code only.

### Scope discipline

- Build ONLY what's asked.
- MVP first; iterate based on feedback.
- No enterprise bloat (auth, deployment, monitoring unless requested).
- Simple > complex; YAGNI.

### Failure investigation

- Root-cause analysis, not symptom fixes.
- Never skip tests or validation.
- Fix, don't workaround.

### Git workflow

- Start every session with `git status` and `git branch`.
- Feature branches only; never work on main/master.
- Incremental, meaningful commits.
- Verify with `git diff` before staging.
- Create restore points before risky operations.
- Push only when asked.

### Tool optimization

- Best tool selection: MCP > native > basic.
- Parallel everything; use Task agents for >3 steps.
- Use Grep tool over bash grep; Glob over find.
- Batch operations; MultiEdit for 3+ file changes.

### Temporal awareness

- Always verify the current date from environment context.
- Never assume from knowledge cutoff.
- State sources for time/version claims.

### Professional honesty

- No marketing language ("blazingly fast", "100% secure").
- No fake metrics or time estimates without evidence.
- Provide honest trade-offs; push back respectfully when needed.
- State "untested", "MVP", "needs validation" instead of "production-ready".

## Anti-slop rules (from bypass-slop skill)

- No mock metrics, demo charts, or invented social proof. Empty/honest > fake-complete.
- Landing pages: light mode default, hero-only atmospheric background, no sticky glass nav unless asked.
- No product-photo bento grids or decorative image spam unless specifically requested.
- No "Real Talk" pivots: avoid "The truth is...", "It's not just X. It's Y.", "Let's break it down.", "But here's the thing.", etc.
- Dashboards are apps: view switcher, not scroll-spy sidebar; profile at bottom; one primary control.
- Brand and auth consistency: BrandMark component, one redirect host for OAuth (prefer `127.0.0.1`).
- Policy belongs in code (`config.ts`), secrets in env.

## TinyFish search rules

- Always use TinyFish Web Search (`tinyfish search query "<query>"`) for web search.
- Always use TinyFish Fetch (`tinyfish fetch content get "<url>"`) for web fetch.
- Only fall back to native search/fetch if TinyFish is rate-limited.
