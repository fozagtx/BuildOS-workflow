# KAIZEN MEGA — Complete Coding Agent Capability Report

This report catalogs every useful skill, from UI/design through backend, crypto, infrastructure, security, research, video, and agent tooling.

## Executive summary

- **Total skills**: 239

### Useful skills by layer
- **frontend/design**: 125
- **video/media**: 8
- **product/strategy**: 24
- **solana/crypto**: 15
- **agent/tools**: 27
- **security/audit**: 11
- **research/analytics**: 2
- **database/infrastructure**: 9
- **general/other**: 18

---

## 1. Absolute rules (non-negotiable)

1. **No AI co-author trailers.** Never add `Co-Authored-By: Claude/Codex/Anthropic` or `noreply@anthropic.com` to commits.
2. **No assistant mentions in artifacts.** Never mention Claude/Codex/Anthropic in PRs, issues, code comments, or committed files unless explicitly asked.
3. **Strip accidental trailers immediately.** If one lands, `git commit --amend` and `git push --force-with-lease`.
4. **No mock metrics, demo data, or fake social proof.** Empty/honest > fake-complete.
5. **Build only what is asked.** MVP first; no speculative auth/deployment/monitoring.
6. **Read before writing.** `git status` and `git branch` at session start.
7. **Parallelize by default.** Batch operations, use MCP tools for their designed purpose.

---

## 2. Default prototype workflow

1. **Capture intent** — user, problem, core loop, desired output.
2. **Plan** — TodoWrite for 3+ steps, identify parallel work, pick the right skill.
3. **Validate / research** — `validate-idea`, `competitive-landscape`, `defillama-research` if unvalidated.
4. **Design** — `brand-design`, `frontend-design-guidelines`, `design-taste` if UI.
5. **Build** — scaffold with `scaffold-project` (Solana) or project stack; `build-with-claude` for guidance.
6. **Audit** — `vibe-security`, `cso`, `review-and-iterate` before ship.
7. **Ship** — feature branch, meaningful commits, `create-readme`, pitch/grant/video if needed.

---

## 3. Skill inventory by layer

For each skill: `name` — description/triggers.

### frontend/design

**`"source-command-sc-brainstorm"`**
- Description: "Interactive requirements discovery through Socratic dialogue and systematic exploration"

**`"source-command-sc-build"`**
- Description: "Build, compile, and package projects with intelligent error handling and optimization"

**`"source-command-sc-design"`**
- Description: "Design system architecture, APIs, and component interfaces with comprehensive specifications"

**`"source-command-sc-document"`**
- Description: "Generate focused documentation for components, functions, APIs, and features"

**`"source-command-sc-troubleshoot"`**
- Description: "Diagnose and resolve issues in code, builds, deployments, and system behavior"

**`"source-command-sc-workflow"`**
- Description: "Generate structured implementation workflows from PRDs and feature requirements"

**`ai-saas-app-playbook`**
- Description: Build revenue-first AI / mobile / SaaS apps using the BusDownBonnor (Connor Burd) playbook: distribution-first ideas, competitor onboarding teardown, vibe-code core loop, frictionless onboarding + paywall, influencer/UGC then paid ads. Use when the user wants to build a consumer SaaS or subscription app with AI, mentions BusDownBonnor, vibe coding for revenue, Face Harmony-style app reviews, influencer equity apps, or "how do successful AI app founders ship."

**`ai-without-brain-rot`**
- Description: Use LLM chatbots to sharpen critical thinking instead of outsourcing it. Socratic provocator, Six Thinking Hats, metacognition before prompting, effort triage, and deep-systems project stress tests (surface vs Turnstile-depth). Use when the user mentions brain rot, AI slop, critical thinking with AI, Socratic provocator, thinking hats, hackathon ideas feeling shallow, Web3 project ideation, Turnstile-depth builds, or "use AI without rotting my brain".

**`analyzing-schema-change-storage-risk`**
- Description: Estimates storage requirements for CockroachDB online schema change backfills using SHOW RANGES WITH DETAILS, KEYS, INDEXES. Use before CREATE INDEX, ADD COLUMN with INDEX/UNIQUE, ALTER PRIMARY KEY, CREATE MATERIALIZED VIEW, CREATE TABLE AS, REFRESH, or SET LOCALITY on tables with large per-index footprints, to avoid mid-backfill disk exhaustion.

**`animation-vocabulary`**
- Description: Reverse-lookup glossary that turns a vague description of a web animation or motion effect into its exact term ("the bouncy thing when a popover opens" → Pop in; "the iOS rubber-band scroll" → Rubber-banding). Use when the user asks "what's it called when…", or describes a motion effect without knowing its name and wants the right word to prompt an AI or designer with. For naming an effect, not designing or building one.

**`apple-design`**
- Description: Apple's approach to interface design and fluid, physical motion, translated for the web. Use when building or reviewing gesture-driven UI, spring animations, drag/swipe/sheet interactions, momentum and interruptible transitions, translucent materials and depth, typography (optical sizing, tracking, leading), reduced-motion, or the design foundations (feedback, spatial consistency, restraint) behind Apple-style interfaces.

**`auditing-cis-benchmark`**
- Description: Audits a self-hosted CockroachDB cluster against the CIS CockroachDB Benchmark v1.0.0 Level 1 controls. Supports two audit depths — quick automated scans and full CIS audit procedures. Produces a structured PASS/FAIL/MANUAL report covering installation, system hardening, logging, user access, data protection, and CockroachDB settings. Use when preparing for CIS compliance assessments, hardening self-hosted deployments, or validating security posture against industry benchmarks.

**`auditing-table-statistics`**
- Description: Audits optimizer table statistics for staleness, missing coverage, and data quality issues using SHOW STATISTICS. Use when diagnosing poor query performance, unexpected plan changes, or after bulk data changes to identify stale statistics requiring refresh via CREATE STATISTICS.

**`benchmarking-transaction-patterns`**
- Description: Guides benchmarking and comparing explicit multi-statement transactions versus single-statement CTE transactions in CockroachDB, with fair test methodology, contention analysis, and performance interpretation. Use when comparing transaction formulations, benchmarking CockroachDB workloads under contention, investigating retry pressure, or deciding whether to rewrite multi-step application flows into single SQL statements.

**`better-interface`**
- Description: Combines all of the `better-*` skills into a single review across accessibility, layout, writing, typography, color and UI polish.

**`book-to-skill`**
- Description: "Converts books and documents (PDF, EPUB, DOCX, HTML, Markdown, plain text, RTF, MOBI/AZW with Calibre) into structured agent skills, extracting frameworks, mental models, principles, techniques, and anti-patterns. Use when the user wants to study a document through GitHub Copilot CLI, Amp, or Claude Code, apply an author's frameworks while working, or build a reusable knowledge base from a file."

**`bpfg-hackathon`**
- Description: Run the Billion Person Focus Group (BPFG) method for fast hackathons and sprints — living questions, full research commissions, scouts, elder councils, void language, Layer-1 pre-verbal insight, village loop (sense/synthesize/shape), multi-model triangulation, and demo spines. Use when the user mentions BPFG, billion person focus group, how to see, how to build, void language, living question, pre-verbal insight, village of agents, scout/elder council, sensors and shapers, hackathon research OS, or runs /bpfg-hackathon, /bpfg, /village, /brief-builder, /living-question. Also use for 24h/48h hackathon insight → product → pitch loops that must listen to real markets before building.

**`brand-design`**
- Description: Generate, preview, and apply a brand color palette (plus typography, gradients, and tone/voice) to a frontend project. Use when a user says "pick brand colors", "choose a color palette", "brand design", "generate a palette", "theme this project", "what colors should I use", "brand identity", "design my brand", "set up brand colors", "time to build the frontend", "let's start the UI", "make this look branded", or any time a project is about to start frontend work and has no brand.md yet. Presents 6 candidate palettes as a visual HTML preview opened in the user's browser, supports an infinite regenerate loop until the user is satisfied, then writes the chosen palette to shadcn CSS variables (light + dark), wires up typography via next/font, derives brand gradients, and writes brand.md for future reference.

**`brand-guidelines`**
- Description: Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand colors or style guidelines, visual formatting, or company design standards apply.

**`brandkit`**
- Description: Premium brand-kit image generation skill for creating high-end brand-guidelines boards, logo systems, identity decks, and visual-world presentations. Trained for minimalist, cinematic, editorial, dark-tech, luxury, cultural, security, gaming, developer-tool, and consumer-app brand systems. Optimized for intentional logo concepting, refined composition, sparse typography, strong symbolic meaning, premium mockups, art-directed imagery, and flexible grid layouts.

**`build-data-pipeline`**
- Description: Guide a developer through building a Solana data pipeline or indexer. Use when a user says "build an indexer", "data pipeline", "analytics", "track transactions", "monitor wallets", "webhook", "index accounts", or "real-time data". Reads build-context.md from a prior scaffold phase if available.

**`build-defi-protocol`**
- Description: Guide a developer through building a DeFi protocol on Solana. Use when a user says "build a DEX", "AMM", "lending protocol", "vault", "yield", "liquidity pool", "DeFi protocol", "swap program", "build a DeFi app", "perpetual futures", "perps protocol", "leverage trading", or "derivatives". Reads build-context.md from a prior scaffold phase if available.

**`build-mobile`**
- Description: Guide a developer through building a Solana mobile app. Use when a user says "build a mobile app", "React Native Solana", "Solana mobile", "mobile wallet", "mobile dApp", "Android Solana", or "iOS Solana". Reads build-context.md from a prior scaffold phase if available.

**`build-with-claude`**
- Description: Guide a developer through building their Solana MVP step by step using Claude Code. Use when a user says "help me build this", "start the MVP", "guide me through implementation", "what should I build first", or "walk me through the code". Reads build-context.md from a prior scaffold phase if available.

**`bypass-slop`**
- Description: Full-session anti-slop skill (UI + agent + auth + git + local dev) distilled from a long NairaShield-style build (~10h of corrections). Use when shipping product UI, landing pages, dashboards, Cloudflare agents, Google auth, brand marks, or configs. Blocks mock metrics, demo modes, eng-jargon copy, sticky glass nav, landing-as-dashboard scroll nav, em dashes, product-photo bento junk, AI commit trailers, env-stored product policy, stress-stack overlays, and Real Talk copy pivots (truth is / not just X / let’s break it down). Triggers: /bypass-slop, bypass-slop, anti-slop, no mocks, real metrics only, PAS copy, hero-only bg, design-promax without slop, don't invent, dashboard app not landing. Apply proactively on greenfield product work when the user values honesty and craft. Scope: multi-harness user skill (~/.agents/skills, symlinked for Claude/Codex/Cursor/Grok).

**`canvas-design`**
- Description: Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other static piece. Create original visual designs, never copying existing artists' work to avoid copyright violations.

**`claude-agent-sdk-expert`**
- Description: Use when reviewing, debugging, or building AI agents with the Codex Agent SDK (TypeScript or Python). Covers the Agent class, query(), agent.stream(), tool_use, tool schemas, maxIterations, subagents, hooks (PreToolCall, PostToolCall, StopHook), MCP integration, multi-agent coordination, structured output, context window management, stop_reason handling, and agentic loop architecture. Do NOT activate for general Codex API usage without agents, simple messages.create() calls, or non-agent Anthropic SDK usage — use the Codex-api skill for those.

**`claude-api`**
- Description: "Build, debug, and optimize Codex API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Codex API code between Codex model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements). TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Codex API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Codex feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project. SKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML."

**`cockroachdb-sql`**
- Description: Use when writing, generating, or optimizing SQL for CockroachDB, designing CockroachDB schemas, or when the user asks about CockroachDB-specific SQL patterns, type mappings, and distributed database best practices. Also use when encountering CockroachDB anti-patterns like missing primary keys, sequential ID hotspots, or incorrect type usage.

**`colosseum-copilot`**
- Description: Search and analyze 5,400+ Solana hackathon projects using Colosseum Copilot. Find similar projects, discover winner patterns, identify gaps, and explore ML clusters. Use when a user says "colosseum copilot", "hackathon projects", "winner patterns", "gap analysis hackathon", "similar Solana projects", or "colosseum landscape". Requires a Colosseum Copilot token.

**`copywriting`**
- Description: When the user wants to write, rewrite, or improve marketing copy for any page — including homepage, landing pages, pricing pages, feature pages, about pages, or product pages. Also use when the user says "write copy for," "improve this copy," "rewrite this page," "marketing copy," "headline help," "CTA copy," "value proposition," "tagline," "subheadline," "hero section copy," "above the fold," "this copy is weak," "make this more compelling," or "help me describe my product." Use this whenever someone is working on website text that needs to persuade or convert. For email copy, see emails. For popup copy, see popups. For editing existing copy, see copy-editing. For the offer underneath the copy (bonuses, guarantees, value framing), see offers.

**`create-pitch-deck`**
- Description: Create a structured pitch deck for a crypto project. Use when a user says "create a pitch deck", "help me pitch", "I need slides", "prepare for demo day", "investor presentation", or "grant application". Reads idea-context.md and build-context.md from prior phases if available.

**`cua-skill`**
- Description: "MUST USE whenever the user wants to automate a real desktop or sandbox - clicking, typing, scrolling, screenshotting, running an OS shell command, or handing a high-level 'open browser and do X' task to an autonomous computer-use agent. Wraps the trycua/cua Python toolkit via its `cua` CLI - pynput-based, cross-platform (macOS / Linux / Windows). NO custom tools are registered; you call `cua` through pi's built-in bash and read screenshots back through the Read tool. Triggers: cua, computer use, computer-use, GUI automation, screenshot the desktop, click on the screen, type into the active app, scroll the page, control my computer, drive my browser, sandbox, docker sandbox, QEMU sandbox, Lume sandbox, ComputerAgent, cua do, cua sandbox, 컴퓨터 자동화, 스크린샷 찍어, 내 컴퓨터 조작, 브라우저 열어서, 샌드박스, 화면 자동화, 마우스로 클릭, 키보드 타이핑, computer use 위임, 자동으로 클릭, 자율 에이전트로 처리."

**`debug-program`**
- Description: Help a developer debug a failing Solana program or transaction. Use when a user says "debug my program", "program error", "transaction failed", "stuck", "help me fix", "why is this failing", "error code", or "instruction failed". Reads build-context.md if available.

**`deep-systems-projects`**
- Description: Alias for deep project stress-testing. Canonical skill is ai-without-brain-rot (Habit 3). Use when ideating Web3/hackathon projects, roasting shallow ideas, or asking for Turnstile-depth builds.

**`defillama-research`**
- Description: Research DeFi protocols and market opportunities using DefiLlama data. Use when a user says "show me TVL data", "which protocols are growing", "DeFi market research", "what should I build in DeFi", "find DeFi opportunities", "analyze protocol TVL", or "which chains are trending". Uses TVL as a trust metric to suggest protocols worth building on or integrating with.

**`deploy-to-mainnet`**
- Description: Guide a Solana project from devnet to mainnet production deployment. Use when a user says "deploy to mainnet", "go to production", "deployment checklist", "prepare for launch", "mainnet deployment", or "ship it". Reads build-context.md from a prior build phase if available.

**`design-promax`**
- Description: Premium React UI via HeroUI Pro + triple-axis router (theme × route × style). MUST ask which Pro theme first: Default | Brutalism | Glass | Mouve (unless user already named one). Then clean_product compose (Vault OTP / GhostKeys) + real Pro sources. Files: THEMES.json, STYLE_PRESETS.json, ROUTE_REGISTRY.json, case-studies/vault-otp.md. Showcase packs: Map navigation, Pro AI chat, Music player, Shopping experience. Triggers: design-promax, HeroUI, Brutalism, Glass, Mouve, clean_product, Vault OTP, GhostKeys, those cards, route UI.

**`design-taste`**
- Description: Design direction, judgment calls, and anti-AI-slop review for crypto UIs. Use when the user says "this looks generic", "this looks AI-generated", "anti-slop", "design judgment", "premium feel", "design direction", "what direction should this take", "make this feel more premium", "review for taste", "theme reference", "warm monochrome", "stark minimal", "gradient trust", "workstation dense", "soft consumer", "gallery editorial", "density", "page archetype", "design brief", "pitch deck style", "deck visual direction". Also use when building any new page-level component that needs aesthetic direction before implementation. Does NOT claim "make this look good" or "polish this" — those belong to frontend-design-guidelines.

**`design-taste-frontend`**
- Description: Senior UI/UX Engineer. Architect digital interfaces overriding default LLM biases. Enforces metric-based rules, strict component architecture, CSS hardware acceleration, and balanced design engineering.

**`designing-application-transactions`**
- Description: Guides application developers in designing correct and performant transaction patterns for CockroachDB, covering transaction lifetime, implicit vs explicit transactions, retry handling with exponential backoff, pushing invariants into SQL, selective pessimistic locking, set-based operations, connection pooling, prepared statements, keyset pagination, follower reads, and separating business logic from database logic. Use when building applications on CockroachDB, designing transaction workflows, handling retries, optimizing application-layer database interactions, or configuring connection pools.

**`designing-multi-region-applications`**
- Description: Guides developers in selecting and implementing multi-region patterns for CockroachDB applications, covering active-passive vs active-active architectures, REGIONAL BY ROW, GLOBAL tables, manual geo-partitioning with lease preferences, and live demo setup with validation queries. Use when designing multi-region database topologies, choosing between REGIONAL BY ROW and manual partitioning, building multi-region demos, or optimizing cross-region latency.

**`doc-coauthoring`**
- Description: Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, decision docs, or similar structured content. This workflow helps users efficiently transfer context, refine content through iteration, and verify the doc works for readers. Trigger when user mentions writing docs, creating proposals, drafting specs, or similar documentation tasks.

**`embedded-captions`**
- Description: Add captions or subtitles to an existing single-subject talking-head video without editing the footage. Use for plain verbatim captions, cinematic captions embedded behind the subject, VFX captions, “炸/特效/酷炫字幕,” or a named identity from the 35-style catalog. Route by visual identity, not by backend engine. The quiet `anchor` rail is the default; embed every word only when the user explicitly wants a fully cinematic treatment. The workflow runs locally end to end, including transcription and subject matting; split multi-shot footage before applying it.

**`emil-design-eng`**
- Description: This skill encodes Emil Kowalski's philosophy on UI polish, component design, animation decisions, and the invisible details that make software feel great.

**`enforcing-password-policies`**
- Description: Configures and enforces password policies on CockroachDB clusters including minimum length, complexity requirements, and hash cost settings. Use when strengthening authentication requirements, setting up password policies for a new cluster, or meeting compliance password standards.

**`find-animation-opportunities`**
- Description: Search a codebase or UI for places that don't animate but should, and reject everything that shouldn't. Read-only; it proposes motion with exact values, it does not implement it. Use when the user asks "what could be animated here?" or wants to "make this feel more alive". For fixing existing animations, use improve-animations or review-animations instead.

**`find-next-crypto-idea`**
- Description: Interview users sharply to discover, rank, or validate what they should build in crypto. Use when a user asks what to build in crypto, wants startup ideas in a crypto niche such as DeFi or AI x crypto, wants blunt feedback on an existing crypto idea, or wants a concrete artifact comparing the best next ideas. Treat the bundled idea datasets as inspiration, not constraints, and always combine them with fresh market research.

**`frontend-design`**
- Description: Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.

**`frontend-design-guidelines`**
- Description: Apply high-quality web interface design rules when building, reviewing, or styling frontend code. Use when the user says "build a frontend", "create a component", "style this", "review my UI", "build a landing page", "design this page", "make this look good", "add animation", "build a form", "improve the UI", "polish this", "make this feel right", "review for craft", "the interaction feels off", "make this look polished", or when generating any React/Next.js component. Defaults to Tailwind CSS and shadcn/ui. Reads brand.md at the project root (if present) and uses it as the source of truth for colors, typography, and voice. Covers interactions, layout, typography, forms, animation, states, accessibility, and a dedicated craft-and-polish layer for taste-level review. Use proactively whenever frontend code is being written — do not wait to be asked.

**`general-video`**
- Description: Author or edit a custom HyperFrames composition when no specialized workflow fits, or when BRIEF.md sets flow: companion. Use for longer or multi-scene pieces, brand and sizzle reels, montages, static loops, static title cards, footage remixes, and freeform builds. Use motion-graphics instead for a short unnarrated motion-first unit, including an animated title. Route fresh creation through hyperframes before using this skill.

**`geo`**
- Description: GEO-first SEO analysis tool. Optimizes websites for AI-powered search engines (ChatGPT, Codex, Perplexity, Gemini, Google AI Overviews) while maintaining traditional SEO foundations. Performs full GEO audits, citability scoring, AI crawler analysis, llms.txt generation, brand mention scanning, platform-specific optimization, schema markup, technical SEO, content quality (E-E-A-T), and client-ready GEO report generation. Use when user says "geo", "seo", "audit", "AI search", "AI visibility", "optimize", "citability", "llms.txt", "schema", "brand mentions", "GEO report", or any URL for analysis.

**`geo-brand-mentions`**
- Description: Brand mention and authority scanner for AI visibility. Analyzes brand presence across platforms that AI models rely on for entity recognition and citation decisions. Produces a Brand Authority Score (0-100) with platform-specific recommendations.

**`geo-report-pdf`**
- Description: Generate a professional PDF report from GEO audit data using ReportLab. Creates a polished, client-ready PDF with score gauges, bar charts, platform readiness visualizations, color-coded tables, and prioritized action plans.

**`gpt-taste`**
- Description: Elite UX/UI & Advanced GSAP Motion Engineer. Enforces Python-driven true randomization for layout variance, strict AIDA page structure, wide editorial typography (bans 6-line wraps), gapless bento grids, strict GSAP ScrollTriggers (pinning, stacking, scrubbing), inline micro-images, and massive section spacing.

**`grill-me`**
- Description: Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me".

**`high-end-visual-design`**
- Description: Teaches the AI to design like a high-end agency. Defines the exact fonts, spacing, shadows, card structures, and animations that make a website feel expensive. Blocks all the common defaults that make AI designs look cheap or generic.

**`hyperframes`**
- Description: Mandatory entry point: read this first for any request to make, create, edit, animate, or render a video, animation, or motion graphic, including a promo, explainer, captioned clip, title card, overlay, slideshow or interactive deck, Remotion port, or any HyperFrames HTML composition. Also use it to inspect, diagnose, validate, preview, publish, or batch-render an existing HyperFrames project. Inputs may be a website URL, GitHub PR, Figma design or URL, text or brief, existing footage, or music. It resumes project state, captures intent when applicable, selects and installs the owning workflow, and routes domain capabilities. HyperFrames is the default output framework unless the user explicitly chooses another framework for the deliverable or asks only to record a browser session.

**`hyperframes-animation`**
- Description: "All animation knowledge for HyperFrames — atomic motion rules, multi-phase scene blueprints, scene transitions, broader motion-design techniques, AND the seven runtime adapters (GSAP default, plus Lottie, Three.js, Anime.js, CSS keyframes, Web Animations API, TypeGPU). Use for any motion or animation task: pick 2-4 rules and compose, or load a blueprint, or look up runtime-specific API (e.g. GSAP eases / Lottie player / Three.js mixer). Also covers auditing an existing composition's choreography (animation map) and 24 named text-animation effects. HyperFrames-native: single paused timeline, seek-safe, deterministic."

**`hyperframes-cli`**
- Description: Use the HyperFrames CLI development loop: init, add, catalog, capture, lint, check, snapshot, compare, grade-compare, preview, play, present, beats, keyframes, single or batch render, publish, cloud, cloudrun, feedback, lambda, doctor, browser, info, upgrade, skills, compositions, timeline, history, clean, docs, benchmark, telemetry, transcribe, auth, tts, and remove-background. Also use when diagnosing build or render failures. validate, inspect, and layout are deprecated aliases; use check. Covers local, HeyGen-hosted cloud, AWS Lambda, and Google Cloud Run rendering.

**`hyperframes-core`**
- Description: The HyperFrames composition contract — build one renderable project. Use for composition structure, the `data-*` timing attributes, `class="clip"`, tracks, sub-compositions, variables, framework-owned media playback, deterministic-render rules, and validation. Read before writing composition HTML.

**`hyperframes-creative`**
- Description: Non-animation creative direction for HyperFrames videos. Use for design spec (frame.md / design.md) handling, palettes, typography, narration, beat planning, audio-reactive visuals, composition patterns, and brand / style decisions. For atomic motion patterns and scene blueprints, use `hyperframes-animation`.

**`hyperframes-keyframes`**
- Description: Use when a HyperFrames composition needs a punch-in, punch-out, zoom, reframe, Ken Burns treatment, camera move, visual match/whip handoff, or other seek-safe 2D/3D keyframes; also for GSAP, CSS keyframes, Anime.js, WAAPI, FLIP, paths, masks, SVG morph/draw, text trails, 3D depth, or `hyperframes keyframes` diagnostics. Don't use for broad scene strategy, brand design, media sourcing, captions, or general video planning.

**`hyperframes-registry`**
- Description: Search, install, and wire registry blocks and components into HyperFrames compositions. Use BEFORE hand-building any named visual — whenever a brief, a user, or a storyboard names a look, effect, treatment, or transition such as CRT scanlines, glitch, chromatic aberration, film grain, a shimmer sweep, a chart, a code or terminal window, a map, or a confetti burst — because roughly 400 hosted items already cover many of them and the search ranks all of them with nothing installed, no project, and no account. Also use when running hyperframes add or hyperframes catalog, installing one item or every block matching a tag, wiring an installed item into index.html, or working with hyperframes.json. Covers discovery, install locations, block sub-composition wiring, component snippet merging, and authoring a new block or component to contribute upstream (idea → scaffold → validate → PR).

**`hyperframes-studio`**
- Description: Use when working with a person on a HyperFrames project in Studio: first, whether their message asks for a change at all (questions, loose ideas and "don't change anything" get an answer and a plan, not an edit); for a new film, the plan, storyboard and build order that the HyperFrames launch films follow; and how the timeline should be laid out so it reads well (one caption track, one element kind per track, every scene a sub-composition) and where captions and key content may sit (safe zones). Don't use for how to perform an individual edit (split, trim, retime, volume, copy, swap): that is `creator-editing-recipes.md` in `/hyperframes-core`.

**`improve-animations`**
- Description: Survey a codebase's animation and motion code as a senior motion advisor, then produce a prioritized audit and self-contained implementation plans for other agents (or cheaper models) to execute. Read-only on source code — it plans improvements, it does not apply them. Use when the user asks to "improve the animations", "audit the motion", "make this app feel better", or wants a roadmap of animation fixes rather than a review of a single diff.

**`improve-ui`**
- Description: Audit an existing product surface against its own design evidence, identify verified UI problems, and write self-contained implementation plans for another agent. Strictly read-only on product source. Use when asked to review, refine, improve, or clean up an interface without replacing its identity; investigate design-system drift; or prepare a design handoff.

**`industrial-brutalist-ui`**
- Description: Raw mechanical interfaces fusing Swiss typographic print with military terminal aesthetics. Rigid grids, extreme type scale contrast, utilitarian color, analog degradation effects. For data-heavy dashboards, portfolios, or editorial sites that need to feel like declassified blueprints.

**`kaizen-mega`**
- Description: Kaizen's full-stack prototype-building mega-skill. Loads the user's personal rules, workflow, and skill catalog, then routes to the right domain skill for fast UI/backend/crypto/video/pitch work. Use whenever the user says "build", "prototype", "scaffold", "design", "ship", "start working", "kaizen", or any product/MVP/hackathon task. Apply proactively on greenfield product work.

**`landing-page-rewrite`**
- Description: Rewrite or build a high-converting SaaS landing page using a proven conversion framework. Use when the user says "rewrite my landing page", "improve landing page", "create a landing page", "make a better hero", "my landing page isn't converting", "fix the homepage", "marketing page", or asks to apply conversion principles to a marketing/product page. Triggers proactively when a generic or vague landing page is detected during frontend work.

**`launch-token`**
- Description: Guide a developer through launching a token on Solana. Use when a user says "launch a token", "create a token", "pump.fun", "bonding curve", "token launch", "create a memecoin", or "SPL token". Reads build-context.md from a prior scaffold phase if available.

**`managing-cluster-capacity`**
- Description: Manages CockroachDB cluster capacity across all tiers. Self-Hosted covers node decommissioning for permanent removal and adding nodes for expansion. Advanced/BYOC covers scaling node count and machine size via Cloud Console, API, or Terraform. Standard covers adjusting provisioned compute (vCPUs). Basic auto-scales — guidance covers spending limits and cost management. Use when scaling capacity up or down, permanently removing nodes, or managing costs.

**`mcp-builder`**
- Description: Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).

**`media-use`**
- Description: Agent Media OS, the single skill for every media need in a HyperFrames project. Resolve BGM, SFX, image, icon, brand logo, voice, color grade, or LUT into a frozen local file or paste-ready block + ledger record (one verb, `resolve`); generate via TTS / music / image models when the catalog misses; produce voiceover, transcription, captions, and background removal through one shared audio engine; operate on media (cut / reframe / transform); and reuse assets across projects. Also use for vague feedback that real footage looks dark, flat, boring, should feel retro/camcorder/print/ASCII, needs privacy, or needs a media reveal.

**`micro-interactions`**
- Description: Expert micro-interaction architect for mobile apps, web applications, and responsive websites. Use this skill when the user asks to add, build, fix, audit, or consult on micro-interactions, animations, transitions, motion design, gesture feedback, haptics, loading states, skeleton screens, pull-to-refresh, swipe actions, scroll animations, button states, form validation feedback, toast notifications, modals, dropdowns, toggles, progress indicators, shared element transitions, spring physics, easing curves, motion tokens, or any interaction that provides visual/haptic/auditory feedback to user actions. Triggers on: "micro-interaction", "animation", "transition", "motion", "easing", "spring", "gesture", "haptic", "feedback", "loading state", "skeleton", "shimmer", "pull to refresh", "swipe", "drag", "hover effect", "press state", "focus ring", "scroll animation", "parallax", "stagger", "orchestration", "reduced motion", "View Transitions", "layout animation", "shared element", "hero animation", "morphing", "Framer Motion", "GSAP", "Lottie", "Rive", "React Spring", "anime.js", or any request to make an interface "feel better", "feel alive", "feel snappy", "feel responsive", or "feel polished".

**`minimalist-ui`**
- Description: Clean editorial-style interfaces. Warm monochrome palette, typographic contrast, flat bento grids, muted pastels. No gradients, no heavy shadows.

**`molt-fetch`**
- Description: Guide for using molt fetch to migrate data from PostgreSQL, MySQL, Oracle, or MSSQL to CockroachDB. Use when running molt fetch commands, configuring storage backends, handling fetch failures/resumption, or chaining fetch with verify.

**`molt-replicator`**
- Description: Guide for using the CockroachDB replicator to continuously replicate changes from PostgreSQL, MySQL, or Oracle to CockroachDB after an initial molt fetch data load. Use when setting up CDC replication, configuring pglogical/mylogical/oraclelogminer, or managing the fetch → replicator cutover workflow.

**`molt-verify`**
- Description: Guide for using molt verify to compare source and target databases for schema and row-level consistency after a migration. Use when running verify commands, tuning concurrency/sharding, handling schema mismatches, or validating data integrity post-migration.

**`monad`**
- Description: Build on Monad — a high-performance EVM L1 (10,000 TPS, 400ms blocks, 800ms deterministic finality) with the Cadence consensus protocol and an encrypted mempool. Use when the user mentions Monad, Cadence consensus, MonadBFT, the BuildAnything/Spark hackathon, or is choosing what to build on a fast EVM chain. Covers the three design axes (speed, trustlessness, order-fairness), the load-bearing test, the on-chain/off-chain split, and how hackathon judges score Monad projects.

**`neon`**
- Description: Overview of Neon, a complete set of cloud backend primitives for apps and agents, spanning Lakebase Postgres, Auth, the Data API, Object Storage, Compute Functions, and the AI Gateway. Start here to route to the right Neon skill, set up the CLI or MCP server, and follow the branch-first workflow. Use when "Neon" or "Lakebase Postgres" is mentioned, or when any of its individual capabilities are the trigger: "object storage" or "S3", "buckets", "serverless functions", "AI gateway", "call an LLM", "logs", "branch logs", "query logs", "log export", "Loki", "Grafana", "observability", "telemetry", "postgres", "database", or "backend". Also use when there is no Neon account yet, the user cannot sign in or provide an API key right now and needs a project they can claim later, or the user asks for a throwaway DATABASE_URL, Claimable Neon, Claimable Postgres, neon.new, claimable.neon.tech, instant Postgres, a no-signup database, temporary postgres, quick postgres, a no credit card database, or npx neon-new.

**`neon-postgres`**
- Description: Guides and best practices for working with Lakebase Postgres, the database behind Neon. Covers setup, connection methods and drivers, pooled vs direct connections, branching, schema migrations, autoscaling, scale-to-zero, instant restore, read replicas, connection pooling, IP allow lists, and logical replication. Use when users ask about "Lakebase Postgres", "Neon setup", "connect to Neon", "Neon project", "DATABASE_URL", "serverless Postgres", "Neon CLI", "neon", "Neon MCP", "Neon Auth", "@neondatabase/serverless", "@neondatabase/neon-js", "scale to zero", "Neon autoscaling", "Neon read replica", "Neon connection pooling", or "schema migrations".

**`number-formatting`**
- Description: Apply consistent number formatting across crypto/Solana UIs. Use when the user says "format numbers", "number display", "token amounts", "price formatting", "zero subscript", "abbreviate numbers", "format currency", "format percent", "how should I display this number", "number formatting spec", or when generating any UI component that displays prices, balances, percentages, ratios, or token amounts. Use proactively whenever writing frontend code that renders numeric values — do not wait to be asked.

**`okx-agent-payments-protocol`**
- Description: "Use when an agent hits HTTP 402 / payment-required, or the user mentions x402, x402Version, X-PAYMENT, PAYMENT-REQUIRED, PAYMENT-SIGNATURE, WWW-Authenticate: Payment, permit2, upto, metered billing, a payment channel / voucher / session, channelId / channel_id, opening / closing / topping up / settling / refunding a channel, a paymentId or a2a_ link, creating / checking a payment link, A2MCP / an A2MCP endpoint, or sending a request to / calling an Agent's endpoint with a concrete endpoint URL. Covers x402 (exact, exact+Permit2, upto, aggr_deferred), MPP (charge / session), and a2a-pay paymentId flows. Any close / topup / settle / voucher / refund near a channel_id or session is an MPP mid-session op. Two-phase quote/pay: `payment quote`, `payment pay --payment-id`, `decode-receipt`. The full bilingual trigger list (including Chinese) lives in the skill body."

**`okx-dapp-discovery`**
- Description: Plugin router for 20 third-party DeFi protocols (Polymarket, Aave, Hyperliquid, PancakeSwap, Morpho, Raydium, Curve, Compound, Pendle, Lido, ether.fi, GMX, Kamino, Orca, Meteora, Clanker, pump.fun, Uniswap) and their protocol-native tokens (HYPE, HLP, eETH, weETH, stETH, wstETH, LDO, GHO, CAKE, CRV, COMP, RAY, ETHFI, GLP, kToken, PT-* / YT-*, $CLANKER). Resolves DApp/token → plugin → confirm-install → re-apply request. Routing only — never signs or broadcasts; every on-chain write needs explicit user approval. Fires on: (1) named DApp + action verb (swap/deposit/stake/long/borrow/buy/sell/snipe/farm/claim, EN or ZH 买/卖/换/存/质押/借/做多/做空/狙击); (2) 2+ DApp comparison ("Aave vs Compound", "Lido vs ether.fi"); (3) Polymarket UpDown (`<COIN> 5min updown`, `5 分钟涨跌`, `预测市场`); (4) protocol-native token + action verb ("deposit USDC into HLP", "PT-stETH on Pendle"); (5) pump.fun WRITE verbs (buy/sell/snipe/ape/swap or 买/卖/狙击/梭哈/帮我买). See body for full rules.

**`okx-defi`**
- Description: "OKX-aggregated DeFi (no specific DApp named) — product discovery, deposit/withdraw/claim execution, AND positions viewing. **If the user names ANY third-party protocol/DApp (Aave, Lido, PancakeSwap, Uniswap, Curve, Compound, Morpho, Pendle, Kamino, Raydium, Hyperliquid, Polymarket, …), route to okx-dapp-discovery — NOT here, even for 'show my Aave positions'.** INVEST triggers: 'invest in DeFi', 'earn yield', 'find best APY', 'deposit/stake for yield', 'search DeFi products', 'redeem/withdraw position', 'claim DeFi rewards', 'borrow against asset', 'repay loan', 'add/remove CLMM liquidity', 'APY/TVL history', 'depth chart', yield farming, lending, staking, liquidity pools. PORTFOLIO triggers: 'check my DeFi positions', 'view DeFi holdings/portfolio', 'my staking/lending positions', 'DeFi balance', 'DeFi 持仓', '我的DeFi资产'. Do NOT use for: DEX swaps (okx-agentic-wallet), token prices (okx-dex-market), wallet token balances (okx-agentic-wallet)."

**`okx-dex-market`**
- Description: "HARD BLOCK — never use for prediction-market/Polymarket UpDown queries; route to okx-dapp-discovery when a named DApp (Polymarket/Aave/Hyperliquid/PancakeSwap/Morpho) appears with a timeframe, or 涨跌/updown for BTC/ETH/SOL/XRP/BNB/DOGE/HYPE. Otherwise, read-only on-chain DEX data, 6 groups: TOKEN (search, hot/热门, liquidity, holders/whale, risk metadata, cluster/持仓集中度, trade history, top traders); MARKET (price/价格, K线/OHLC, index price, wallet PnL/胜率, trade history); SIGNAL (smart money/KOL/whale tracking, buy signals/信号, leaderboard/牛人榜); SOCIAL (news/新闻, sentiment/情绪, token vibe/热度, KOL leaderboard); TRENCHES (pump.fun/meme launches/新盘/扫链, dev reputation, bundle/sniper detection/捆绑狙击者, co-investor — read-only; buy/snipe → okx-dapp-discovery); WS (onchainos ws CLI, or custom WebSocket script/脚本). Also owns Market API payment/x402, quota/额度, and MARKET_API_*_OVER_QUOTA/confirming:true for all 6 groups."

**`okx-guide`**
- Description: "Onchain OS onboarding hub. Classify first-time, how-to-use, OKX.AI, and support intents, then route via the Intent Routing table. Covers: (1) onboarding and welcome — what is onchainos, how do I use this, getting started, tutorial, I'm new; (2) OKX.AI intro and role registration (User / ASP / Evaluator), including spelling variants; (3) customer support, help center, FAQ, bugs, talk to a human. NOT for swap, wallet, balance, or Agent task lifecycle — those have their own skills."

**`page-load-animations`**
- Description: Fix janky page loads where everything appears at once. Production framer-motion recipes for choreographed page entrances, staggered lists, modal transitions, filter cross-fades, live data animations, and micro-interactions. Use when building or reviewing any page that loads content, when animations feel broken or janky, when framer-motion code needs production patterns, or when the user says "page load animation", "entrance choreography", "stagger animation", "framer-motion recipe", "page feels janky", "everything appears at once", "spring animation", "modal animation", "dropdown animation", "rolling numbers", "chart morph", "donut reveal", "filter transition", "tab animation", "micro-interaction", "hover animation", "button feedback", "AnimatePresence", or "framer-motion pattern". Use proactively whenever writing page-level components or reviewing animation code.

**`pick-ui-library`**
- Description: Pick the right library for a given frontend task from a curated, opinionated list — numbers, OTP inputs, charts, command menus, virtualization, drag and drop, toasts, state, styling, and more. Only runs when explicitly invoked; it does not trigger on its own.

**`prd-first-app-builder`**
- Description: Use when building or modifying any user-facing app, dashboard, landing page, wallet/auth-gated product, frontend routes, or demo UI; especially when the task mentions PRD, permissions, protected routes, shadcn/ui, route gating, no fake demos, no gradients, large icons, or avoiding mock/simulation lies.

**`preparing-compliance-documentation`**
- Description: Guides preparation of compliance documentation for CockroachDB Cloud deployments, covering SOC 2, PCI DSS, ISO 27001, HIPAA, and GDPR certifications. Use when responding to compliance questionnaires, preparing for audits, locating certification documents, or assessing cluster configuration for compliance readiness.

**`presigned-urls-security`**
- Description: "Design, review, and implement S3/Tigris/SigV4 presigned URLs as intentional capability grants with correct expiry, scope, and revocation tradeoffs. Use when the user mentions presigned URLs, signed URLs, X-Amz-Signature, SigV4 object storage auth, temporary download/upload links, hotlink protection, or object-storage access control without sharing long-lived credentials. Works via npx openskills read presigned-urls-security in any harness."

**`problem-finder`**
- Description: Force a problem-discovery pass before any solutioning. Decompose startup and hackathon ideas into the worker, their current workaround, and the structural gap that keeps the pain unfixed; reject obvious, feel-safe framings by default. Use when the user mentions a startup idea, hackathon idea, "what should I build," validating an idea, finding problems, user pain points, or presents any solution without a validated problem — even if they do not ask for problem discovery explicitly.

**`prototype`**
- Description: Build a throwaway prototype to flush out a design before committing to it. Routes between two branches — a runnable terminal app for state/business-logic questions, or several radically different UI variations toggleable from one route. Use when the user wants to prototype, sanity-check a data model or state machine, mock up a UI, explore design options, or says "prototype this", "let me play with it", "try a few designs".

**`provisioning-cluster-for-production`**
- Description: Guides initial CockroachDB cluster provisioning and production deployment. Self-Hosted covers cockroach start/init, Kubernetes deployment (Operator, Helm), hardware sizing, and production configuration. Advanced/BYOC covers Cloud Console, API, and Terraform provisioning with production settings. Standard covers cluster creation and provisioned compute selection. Basic covers cluster creation and spending limits. Use when creating a new cluster, preparing for production go-live, or validating deployment configuration.

**`rare-ui`**
- Description: Rare UI (rareui.com) — a shadcn-style registry of ~21 rare, single-file React components you copy into your project, not a dependency you install. Use when the user wants a distinctive/unique animated UI component, mentions "rare ui" / "rareui", or asks for any of these components: animated folder, bounce sidebar, hook sidebar, family drawer, proximity sidebar, duration picker, fluid orb, scroll progress pill, code block, OTP input, gravity letters, GitHub activity heatmap, emoji reaction, notification bell, step player, grid reveal, gooey nav, delete button with inline confirm, animated counter / odometer digits, matrix orb, task list. Also use when looking for ChatGPT-voice-mode-style orbs, AI loading states, spring-animated nav, or iOS-style controls.

**`redesign-existing-projects`**
- Description: Upgrades existing websites and apps to premium quality. Audits current design, identifies generic AI patterns, and applies high-end design standards without breaking functionality. Works with any CSS framework or vanilla CSS.

**`review-animations`**
- Description: Reviews animation and motion code against a high craft bar derived from Emil Kowalski's design engineering philosophy. Default to flagging; approval is earned.

**`slack-gif-creator`**
- Description: Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for Slack like "make me a GIF of X doing Y for Slack."

**`spyzer-memecoin-guide`**
- Description: "Knowledge base from \"A Complete (Meme)coin Guide\" by Spyzer. Use when applying Spyzer's frameworks for memecoin trading, attention markets, on-chain research, risk management, trade psychology, crypto safety, and beginner onboarding."

**`stitch-design-taste`**
- Description: Semantic Design System Skill for Google Stitch. Generates agent-friendly DESIGN.md files that enforce premium, anti-generic UI standards — strict typography, calibrated color, asymmetric layouts, perpetual micro-motion, and hardware-accelerated performance.

**`svelte-code-writer`**
- Description: CLI tools for Svelte 5 documentation lookup and code analysis. MUST be used whenever creating, editing or analyzing any Svelte component (.svelte) or Svelte module (.svelte.ts/.svelte.js). If possible, this skill should be executed within the svelte-file-editor agent for optimal results.

**`tdd`**
- Description: Test-driven development with red-green-refactor loop. Use when user wants to build features or fix bugs using TDD, mentions "red-green-refactor", wants integration tests, or asks for test-first development.

**`theme-factory`**
- Description: Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can apply to any artifact that has been creating, or can generate a new theme on-the-fly.

**`threejs-3d-generator`**
- Description: "Generate, texture, rig, animate, stylize, convert, and download 3D assets for Three.js games using the Tripo API. Use for text-to-3D, image-to-3D, 2D concept to 3D conversion, game-ready GLB/FBX assets, characters, creatures, buildings, props, weapons, terrain pieces, auto-rigging, animation retargeting, model texturing, LEGO/voxel/Minecraft-style stylization, low-poly/quad conversion, and browser asset pipelines. Pair with threejs-image-generator for concepts, texture references, sky/background/terrain textures, logos, icons, and GUI art before image-to-3D generation."

**`threejs-aaa-graphics-builder`**
- Description: "Upgrade Three.js games from basic/prototype visuals to premium AAA-inspired browser graphics. Combines art-direction critique, procedural model building, technical art, mandatory external asset sourcing decisions, threejs-3d-generator assets, threejs-image-generator concept/texture workflows, scene visual polish, material/texture libraries, world prop kits, shaders, VFX readability, render budgets, LOD/instancing, render pipeline, and visual scorecard gates. For premium games with characters, vehicles, ships, weapons, buildings, signature props, skies, textures, decals, logos, icons, or GUI art, load the relevant generator skills before deciding procedural assets are enough."

**`threejs-audio-generator`**
- Description: "Generate, convert, clean, and prepare audio assets for Three.js browser games using ElevenLabs. Use for sound effects, looping ambience, UI sounds, impact/weapon/vehicle audio, creature or boss stingers, announcer/dialogue TTS, scratch-performance voice conversion, voice cleanup/isolation, audio manifests, and game-ready web audio integration."

**`threejs-debug-profiler`**
- Description: "Debug and profile Three.js browser games. Combines scene debugging, render/runtime/loading/animation/resize/mobile input fixes, performance profiling, draw calls, triangles, textures, memory, shader/post-processing cost, bundle size, and mobile DPR/input issues."

**`threejs-game-director`**
- Description: "Primary entrypoint for complete Three.js browser game creation and premium iteration. Use by default for build-a-game, upgrade, polish, premium, AAA, high-fidelity, showcase, from-scratch, endless runner, arcade, action, or release-ready requests. Orchestrates sibling skills for gameplay, AAA graphics, UI, debug/profile, and QA/release, plus 3D/image/audio generators for characters, vehicles, weapons, buildings, props, skies, textures, logos, icons, GUI art, and SFX/voice. Keeps skill-loading, reference, asset-sourcing, and phase ledgers so users never choose skills manually."

**`threejs-game-ui-designer`**
- Description: "Design premium Three.js game UI. Use for HUDs, menus, overlays, pause/win/lose screens, settings, icon controls, touch UI, typography, responsive layout, safe areas, text fit, and UI/world cohesion."

**`threejs-gameplay-systems`**
- Description: "Build and iterate playable Three.js game systems. Combines starter scaffold creation, architecture, game design, level design, gameplay implementation, combat/encounter design, and game-feel tuning (hitstop, screenshake, easing, impact feedback). Use for first playable slices, new Vite/TypeScript/Three.js game setup, design briefs, core loops, level/arena/track/wave/hole/puzzle design, game loops, entity systems, input, collision/physics, scoring, objectives, audio hooks, camera, controls, difficulty, feedback, juice, and maintainable structure."

**`threejs-image-generator`**
- Description: "Generate and edit 2D image assets for Three.js games using Google's Gemini image API. Use for concept sheets, image-to-3D inputs, texture references, sky/background plates, decals, logos, icons, GUI art, title/menu art, thumbnails, marketing stills, and source images that feed threejs-3d-generator. Also use for direct image editing when the user provides an image path."

**`threejs-qa-release`**
- Description: "Verify and release Three.js browser games. Combines playtest QA, automated bot playtests, mobile/responsive checks, production builds, preview verification, static-hosting base paths, debug gating, bundle review, screenshots, visual test harness decisions, packaged canvas-pixel inspection with measured metrics, console checks, and release risk reports."

**`transitions-dev`**
- Description: Production-ready CSS transitions for web apps. Use when implementing notification badges, dropdowns, modals, panel reveals, page transitions, card resizes, number pop-ins, text swaps, icon swaps, success checks, avatar group hovers, error state shakes, search/input clear, skeleton loaders, shimmer text, sliding tabs, tooltips, staggered text reveals, card hover tilt, plus-to-menu morph, accordions, toasts, like buttons, learn-more hovers, checkbox checks, spinning counters, toggles, AI thinking states, reasoning streams, streaming text, matrix dot loaders, or banner stacking. Triggers on "add a transition", "animate the dropdown", "make the modal open smoothly", "swap icon", "page slide", "stagger animation", "open / close transition", "make it animate", "fade between", "success animation", "form error", "shake on invalid", "hover lift", "avatar stack hover", "clear the search", "skeleton loader", "loading shimmer", "shimmer text", "sliding tabs", "segmented control", "tooltip", "reveal text", "tilt card", "3D hover tilt", "cursor glare", "plus to menu", "FAB morph", "accordion", "collapsible", "expand / collapse", "disclosure", "toast", "snackbar", "like button", "heart animation", "learn more arrow", "checkbox", "check animation", "spinning counter", "odometer", "slot machine digits", "toggle", "switch", "thinking states", "AI status line", "agent reasoning", "reasoning stream", "streaming text", "stream words in", "matrix loader", "dot loader", "banner stack", "stacked toasts". Also "motion tokens", "scan for ad-hoc transitions", "replace hardcoded durations with motion tokens", "tokenize my animations", and the commands transitions reveal, transitions review, transitions apply, transitions refine.

**`transitions-polish`**
- Description: Polish and refine existing motion against the transitions.dev motion-token scale — duration, distance, scale, blur, and easing — plus the rules for WHEN each token applies (open/close asymmetry, hover-in vs hover-out, stagger offsets, and intent delays). An add-on to the transitions-dev skill, focused on tuning what already animates rather than adding new transitions. Use when the user asks to "polish my transitions", "refine the motion", "tune the timing / easing", "make the animation feel better / less janky", "tighten the durations", "fix the stagger", "align to the motion tokens", "audit the motion", "review my animations", "scan for ad-hoc transitions", "tokenize my animations", or runs the commands transitions review or transitions polish. Also drives the Refine panel's Small refinement feature. Triggers on "motion polish", "transition polish", "refine motion", "timing feels off", "too slow / too fast", "stagger", "delay", "open close timing", "hover in out".

**`typography-layout`**
- Description: Apply typography anatomy, best-font selection and setting (weight, tracking, leading, case), font classification, legibility vs readability, type-only visual hierarchy, font pairing recipes, and editorial layout principles (balance, proximity, alignment, grids). Use whenever choosing or setting fonts, pairing type, building type hierarchy, pairing faces, designing editorial/marketing/portfolio layouts, or reviewing UI that looks typographically weak. Trigger on: typography, fonts, which font, font pairing, type hierarchy, baseline grid, tracking, kerning, x-height, serif, sans, display type, editorial layout, letterforms, line length, "make the type better". Use proactively on any frontend that sets headlines, body copy, or multi-column page structure — do not wait to be asked.

**`upgrading-cluster-version`**
- Description: Guides CockroachDB version upgrades with tier-appropriate procedures. Self-Hosted covers manual rolling binary replacement with finalization control. Advanced/BYOC covers Console-initiated major upgrades, maintenance windows for patches, and release channel selection. Standard and Basic upgrades are fully automatic with no customer action required. Use when planning, executing, or monitoring a version upgrade.

**`validate-idea`**
- Description: Run a structured validation sprint on a crypto startup idea. Use when a user says "validate this idea", "is this worth building", "run a validation sprint", "help me test demand", or "should I build this". Reads idea-context.md from a prior idea phase if available.

**`veo-camera-movement`**
- Description: Transform natural language camera movement descriptions into professional Veo 3.1 video prompts using industry-standard cinematography terminology. Use when users request video generation with camera movements, describe shots using vague language (e.g., "camera gets closer", "camera spins"), need guidance on which camera movement serves their creative intent, or want to learn film terminology. Handles all movement types from static shots to complex movements like dolly zoom, FPV drone, snorricam, and bullet time. Outputs complete paste-ready Veo prompts following the five-part formula: [Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance].

**`video-craft`**
- Description: Frame-level visual composition and product demo presentation for Remotion videos. Use when the user says "video looks generic", "make video frames look better", "video frame design", "device frame", "product demo video craft", "video CTA", "end card", "video composition", "video craft", "screenshot in video", "frame quality", or when reviewing Remotion compositions for visual quality. Sits on top of marketing-video — adds the visual design layer for each frame. Does NOT claim "create a video" or "marketing video" — those route to marketing-video.

**`web-animation-guidelines`**
- Description: Production-tested web animation reference — easing curves, timing tables, copy-paste CSS/Framer Motion patterns, accessibility, and a pre-ship checklist. Use when the user says "animate this", "add animation", "animation timing", "easing curve", "spring animation", "fade in", "slide in", "stagger", "hover animation", "button press", "modal entrance", "loading spinner", "page transition", "animation feels off", "animation best practices", "prefers-reduced-motion", "60fps animation", "animation performance", "what duration should I use", "what easing", or when writing/reviewing any web animation code (CSS transitions, keyframes, Framer Motion, GSAP, Motion One, React Spring). Use proactively whenever generating animated UI components.

**`web-artifacts-builder`**
- Description: Suite of tools for creating elaborate, multi-component Codex.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.

**`webapp-testing`**
- Description: Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs.

**`write-a-skill`**
- Description: Create new agent skills with proper structure, progressive disclosure, and bundled resources. Use when user wants to create, write, or build a new skill.


### video/media

**`clipify`**
- Description: Find the funniest moments in a video, cut them as standalone clips, optionally reformat 16:9 → 9:16 (face-pan or split-screen), and burn opus-style word-by-word captions. Use when the user mentions "clipify," "cut clips from this video," "make shorts from this," "find funny moments," "reframe to 9:16," "vertical clips," or pastes a video file path and wants social-ready cuts.

**`hyperframes-audio`**
- Description: Use when audio already placed in a HyperFrames composition needs to be mixed: fade-in/fade-out, crossfade, track gain or volume, volume automation, ducking, a music bed that fights a voiceover (voiceover carve), effects on a track (EQ, compressor, limiter, gate, saturation, delay, reverb, chorus, phaser, bitcrush), automation envelopes drawn on a track's volume or any effect parameter, or one submix bus carrying a chain, a fader and an automation clock for several tracks at once (`<hf-audio-group>`). Don't use for sourcing or generating audio — finding BGM, SFX, or making a voiceover is `/media-use`. Don't use for clip timing or track layout, which is `/hyperframes-core`.

**`investigative-video-strategy`**
- Description: Write, structure, audit, and ideate long-form investigative/documentary YouTube videos using the retention playbooks of Neo, Cipher, Blackfiles, Fern, and Hoog. Use when the user wants to draft a documentary script, plan video acts and retention beats, audit a script for weak points, or brainstorm investigative video ideas. Triggers on "documentary script", "investigative video", "retention strategy", "video structure", "Fern style", "Cipher style", "Hoog style", "Blackfiles style", "Neo style", "cold open", "hook strategy", "retention audit".

**`marketing-video`**
- Description: Create marketing videos for Solana projects using Remotion (code-driven) and Renoise (AI-generated). Use when a user says "marketing video", "product video", "promo video", "deck review", "video pitch", "create a video", or "Remotion project".

**`product-launch-video`**
- Description: "Turn a product or marketing URL, pasted script, or brief into a product launch / promo video — SaaS promos, feature reveals, product demos, app and company launches. Use when the user wants to market, launch, promote, or reveal a product; the default for any commercial URL. Site tours / showcases of a website route here too — the brief carries the show-it-as-is intent. Unclear → /hyperframes."

**`script-forensics`**
- Description: Forensic cleanup gate for scripts. Use this skill whenever the user asks to audit, clean, de-slop, de-repeat, tighten, polish, or prepare a YouTube script, content script, voiceover, VSL, narration, hook, intro, outline, or transcript before it moves to thumbnails, voiceover, captions, image prompts, or media production. It finds and removes useless repetition, repeated sentence shapes, repeated beats, filler loops, and AI-slop contrast patterns like "not just X, but Y", "it is not X, it is Y", and "more than just X".

**`submit-to-hackathon`**
- Description: Prepare and optimize a hackathon submission for a Solana project. Use when a user says "submit to hackathon", "prepare my submission", "hackathon entry", "write project description", "demo video", or "help me win the hackathon". Reads all prior phase context if available.

**`youtube-content-studio`**
- Description: Master workflow for YouTube video creation. Use this skill whenever the user wants a YouTube script, content script, retention-backed script, video idea, outline, hook, intro, documentary structure, thumbnail concept, high-CTR thumbnail, voiceover, sound effect, image prompt, AI33 Pro media generation, or a full YouTube production workflow. This skill combines script writing, retention strategy, investigative/documentary structure, originality checks, blocked-name checks, script-forensics cleanup, Thumbnail Architect, and AI33 Pro media tooling.


### product/strategy

**`ad-variation-generator`**
- Description: Generate ad headline variations from winning ads in Figma. Reads your product marketing context, identifies winning ad frames, and creates cloned variations with new headlines directly in your Figma file.

**`apply-grant`**
- Description: Prepare an Agentic Engineering Grant application by gathering project data, git history, and context files, then presenting all fields needed to fill the Solana Earn grant form. Use when the user says "apply for grant", "agentic engineering grant", "apply-grant", "grant application", "fill grant form", "200 USDG grant", "ST earn", "Superteam earn", "Superteam grant", "earn grant", "help me apply for grant", "solana earn grant", or "submit grant".

**`auditing-cloud-cluster-security`**
- Description: Audits the security posture of a CockroachDB cluster (Cloud or self-hosted) across network, authentication, authorization, encryption, audit logging, and backup dimensions. Use when assessing cluster security readiness, preparing for compliance reviews, or investigating security configuration gaps.

**`base44-remote-dev`**
- Description: Develop a Base44 app remotely from your own coding agent by connecting it to the Base44 sandbox over MCP or the `base44 sandbox` CLI. Covers auth, sandbox tools, the edit-preview-verify loop, persistence, concurrency, and Send to Coding Agent. Triggers on "develop my Base44 app remotely", "connect Claude Code to Base44", "bring my own agent", "edit a Base44 app over MCP", or "Base44 sandbox MCP".

**`base44-troubleshooter`**
- Description: Troubleshoot production issues using backend function logs. Use when investigating app errors, debugging function calls, or diagnosing production problems in Base44 apps.

**`competitive-landscape`**
- Description: Map the competitive landscape for a crypto product idea. Use when a user says "who are my competitors", "map the competitive landscape", "what exists in this space", "show me similar projects", or "competitive analysis". Leverages solana-new's catalogs of 106 repos, 78 skills, and 36 MCPs.

**`create-readme`**
- Description: "Create or rewrite a project README.md using a selectable template. Use when the user asks to write a README, create README.md, rewrite the readme, or pick a README style/template. Templates: classic open-source and product-orchestration (Codex Orchestration style). Works via npx openskills read create-readme in any harness."

**`cso`**
- Description: Chief Security Officer mode. Infrastructure-first security audit: secrets archaeology, dependency supply chain, CI/CD pipeline security, LLM/AI security, skill supply chain scanning, plus OWASP Top 10, STRIDE threat modeling, and active verification. Two modes: daily (zero-noise, 8/10 confidence gate) and comprehensive (monthly deep scan, 2/10 bar). Use when a user says "security audit", "threat model", "pentest review", "OWASP", "CSO review", "check for vulnerabilities", or "is my code secure".

**`geo-llmstxt`**
- Description: Analyzes and generates llms.txt files -- the emerging standard for helping AI systems understand website structure and content. Can validate existing llms.txt files or generate new ones from scratch by crawling the site.

**`geo-schema`**
- Description: Schema.org structured data audit and generation optimized for AI discoverability — detect, validate, and generate JSON-LD markup

**`hackathon-readme`**
- Description: Write product-forward hackathon README + TECH.md documentation in the ProofXI style: clear thesis, live app link, screenshot-led how-it-works, developer layout, honest constraints, TxLINE/endpoints tables. Use when the user says "readme like proofxi", "hackathon docs", "product-forward README", "TECH.md", "document the demo", or wants docs that win judges in 30 seconds. Triggers: /hackathon-readme, proofxi docs, submission README.

**`hardening-user-privileges`**
- Description: Hardens CockroachDB user privileges by auditing and tightening role-based access control, reducing admin grants, restricting PUBLIC role permissions, and applying least-privilege principles. Use when reducing excessive privileges, cleaning up admin access, or implementing RBAC best practices.

**`learn`**
- Description: Manage project learnings across sessions. Review, search, prune, and export what superstack has learned. Use when asked to "what have we learned", "show learnings", "prune stale learnings", "export learnings", or "remember this". Proactively suggest when the user asks about past patterns or wonders "didn't we fix this before?"

**`managing-cluster-settings`**
- Description: Reviews, audits, and modifies CockroachDB cluster settings. Self-Hosted has full control over all settings and start flags. Advanced/BYOC can modify most SQL-level settings but infrastructure settings are managed by CRL. Standard has limited settings access — session variables are the primary tuning mechanism. Basic has minimal settings — use session variables and Cloud Console. Use when auditing configuration, tuning performance, or troubleshooting settings-related issues.

**`pptx`**
- Description: "Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates, layouts, speaker notes, or comments. Trigger whenever the user mentions \"deck,\" \"slides,\" \"presentation,\" or references a .pptx filename, regardless of what they plan to do with the content afterward. If a .pptx file needs to be opened, created, or touched, use this skill."

**`product-naming`**
- Description: Expert naming process for products, companies, and features based on David Placek's methodology. Use when the user says "name this", "brainstorm names", "naming process", or needs to find a name for a product, feature, company, or project.

**`product-review`**
- Description: Product quality review — UX flows, onboarding, feature completeness, and user value. Use when a user says "product review", "review my product", "UX review", "is my product good", "product quality", "user experience review", "onboarding review", or "feature audit". Different from code review (review-and-iterate) and product roast (roast-my-product) — this is structured, balanced evaluation.

**`review-and-iterate`**
- Description: Review Solana project code for quality, security, and production readiness. Use when a user says "review my code", "is this production ready", "audit my program", "what should I fix", "code review", or "check for security issues".

**`reviewing-cluster-health`**
- Description: Performs a comprehensive health check of a CockroachDB cluster. Gathers deployment context first, then provides tier-appropriate diagnostics. Self-Hosted uses SQL against node-level system tables and CLI. Advanced/BYOC use Cloud Console and SQL with node visibility. Standard monitors provisioned compute and workload via Cloud Console. Basic monitors Request Unit consumption and connectivity. Use for daily checks, pre-maintenance validation, post-incident verification, or production readiness assessment.

**`roast-my-product`**
- Description: Harsh, honest product critique — find every weakness before users do. Use when a user says "roast my product", "harsh feedback", "be brutal", "what sucks", "find weaknesses", "product critique", "tear it apart", or "what would kill this". Deliberately harsh but constructive — scores each dimension and explains exactly what to fix.

**`scaffold-project`**
- Description: Set up a complete Solana project workspace from a validated idea. Use when a user says "scaffold my project", "set up my workspace", "what stack should I use", "create the project structure", or "initialize my project". Reads idea-context.md from a prior idea phase if available. Leverages solana-new's catalogs of 106 repos, 77 skills, and 36 MCPs.

**`solidity-auditor`**
- Description: Security audit of Solidity code while you develop. Trigger on "audit", "check this contract", "review for security". Modes - default (full repo) or a specific filename.

**`triage`**
- Description: Triage issues through a state machine driven by triage roles. Use when user wants to create an issue, triage issues, review incoming bugs or feature requests, prepare issues for an AFK agent, or manage issue workflow.

**`vibe-security`**
- Description: Audits codebases for common security vulnerabilities that AI coding assistants introduce in "vibe-coded" applications. Checks for exposed API keys, broken access control (Supabase RLS, Firebase rules), missing auth validation, client-side trust issues, insecure payment flows, and more. Use this skill whenever the user asks about security, wants a code review, mentions "vibe coding", or when you're writing or reviewing code that handles authentication, payments, database access, API keys, secrets, or user data — even if they don't explicitly mention security. Also trigger when the user says things like "is this safe?", "check my code", "audit this", "review for vulnerabilities", or "can someone hack this?".


### solana/crypto

**`"source-command-sc-index"`**
- Description: "Generate comprehensive project documentation and knowledge base with intelligent organization"

**`analyzing-range-distribution`**
- Description: Analyzes CockroachDB range distribution across tables and indexes using SHOW RANGES to identify range count, size patterns, leaseholder placement, and replication health. Use when investigating hotspots, uneven data distribution, range fragmentation, or validating zone configuration effects without DB Console access.

**`caveman`**
- Description: Ultra-compressed communication mode. Cuts token usage ~75% by dropping filler, articles, and pleasantries while keeping full technical accuracy. Use when user says "caveman mode", "talk like caveman", "use caveman", "less tokens", "be brief", or invokes /caveman.

**`deep-mantle-researcher`**
- Description: Decomposes high-stakes Mantle and onchain finance questions into source maps, evidence grids, confidence levels, and publishable theses. Use when researching Mantle, RWAs, tokenized assets, DeFi protocols, market moves, hackathon articles, or AI research-agent workflows.

**`geo-citability`**
- Description: AI citability scoring and optimization. Analyzes web page content to determine how likely AI systems (ChatGPT, Codex, Perplexity, Gemini) are to cite or quote passages from the page. Provides a citability score (0-100) with specific rewrite suggestions.

**`geo-content`**
- Description: Content quality and E-E-A-T assessment for AI citability — evaluate experience, expertise, authoritativeness, trustworthiness, and content structure

**`geo-technical`**
- Description: Technical SEO audit with GEO-specific checks — crawlability, indexability, security, performance, SSR, and AI crawler access

**`git-guardrails-claude-code`**
- Description: Set up Codex hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute. Use when user wants to prevent destructive git operations, add git safety hooks, or block git push/reset in Codex.

**`hackathon-project-social-playbook`**
- Description: Generate a complete X (Twitter) social strategy for newly submitted hackathon projects. Based on analysis of breakout Colosseum winners, this skill creates a personalized 30-day playbook with narrative angles, content calendars, engagement tactics, and ready-to-post example tweets.

**`internal-comms`**
- Description: A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Codex should use this skill whenever asked to write some sort of internal communications (status reports, leadership updates, 3P updates, company newsletters, FAQs, incident reports, project updates, etc.).

**`navigate-skills`**
- Description: Meta skill — browse all installed solana-new skills, repos, and MCPs to find the right tool for any task

**`okx-agentic-wallet`**
- Description: "OKX Agentic Wallet — the single skill for the user's wallet and on-chain execution. Use it whenever the user wants to operate their wallet or execute an on-chain action, including: login & accounts, balance / holdings, wallet address / deposit / receive, send / transfer, contract calls (approve / deposit / withdraw), transaction history & status, message signing, wallet export & policy; pay gas with a stablecoin (Gas Station, Solana); swap / trade / buy / sell / convert, get a quote; cross-chain bridge & track arrival; limit orders (buy dip / take profit / stop loss / buy above) plus cancel / list / resume them; broadcast / gas / simulate / track a transaction; look up any public address's holdings; security scanning (token / honeypot 蜜罐 / 貔貅, DApp phishing, tx & signature checks, approvals); audit log. Once matched, follow this skill's Intent Routing to dispatch to the exact action."

**`okx-growth-competition`**
- Description: "List OKX Agentic Wallet exclusive trading competitions, register users for contests, track participation and leaderboard rankings, and claim won rewards. Use when users want to list available trading competitions or trading cups, view competition rules / prize pool / total prizes, register or sign up or enroll or join a contest, check the leaderboard (who is winning) or their own rank (am I in the prize zone, what is my place), ask did I win or query participation / claim status, claim won rewards or prizes from completed competitions, see which wallet account they registered with, or submit Telegram / WeChat / Email / Twitter contact for prize delivery to top-tier winners."

**`solana-beginner`**
- Description: Teach Solana fundamentals to developers new to the ecosystem. Use when a user says "what is Solana", "why Solana", "new to Solana", "explain Solana to me", "Solana basics", "EVM to Solana", "getting started with Solana", or "Solana fundamentals". Adapts to user's background — EVM devs, backend devs, or complete beginners.

**`virtual-solana-incubator`**
- Description: Deep technical Solana bootcamp — SVM architecture, Rust patterns, program development. Use when a user says "Solana incubator", "teach me Rust for Solana", "SVM deep dive", "Solana bootcamp", "learn Solana development", "deep dive Solana", "PDA tutorial", "CPI tutorial", or "Anchor tutorial". Structured curriculum that assesses level and assigns exercises.


### agent/tools

**`"source-command-sc-implement"`**
- Description: "Feature and code implementation with intelligent persona activation and MCP integration"

**`"source-command-sc-load"`**
- Description: "Session lifecycle management with Serena MCP integration for project context loading"

**`"source-command-sc-pm"`**
- Description: "Project Manager Agent - Default orchestration agent that coordinates all sub-agents and manages workflows seamlessly"

**`"source-command-sc-reflect"`**
- Description: "Task reflection and validation using Serena MCP analysis capabilities"

**`"source-command-sc-save"`**
- Description: "Session lifecycle management with Serena MCP integration for session context persistence"

**`"source-command-sc-select-tool"`**
- Description: "Intelligent MCP tool selection based on complexity scoring and operation analysis"

**`"source-command-sc-spawn"`**
- Description: "Meta-system task orchestration with intelligent breakdown and delegation"

**`base44-cli`**
- Description: "The base44 CLI is used for EVERYTHING related to base44 projects: resource configuration (entities, backend functions, ai agents), initialization and actions (resource creation, deployment). This skill is the place for learning about how to configure resources. When you plan or implement a feature, you must learn this skill"

**`base44-sandbox`**
- Description: "Develop a Base44 app remotely inside Base44's cloud sandbox using your own agent — no local checkout and no deploy/push commands. The implementation is remote: writing a resource file into the sandbox is what ships it (backend functions, entities, and agents all auto-sync from the file you write), and OAuth connectors are set up against the remote app via MCP tools or the projectless `base44 connectors` CLI. This skill is the place for learning what you can author in the sandbox, how backend functions, entities, and agents are structured, and how to connect a connector without a local filesystem. Triggers on 'develop my Base44 app remotely', 'no local files', 'cloud sandbox', 'create an entity/agent remotely', 'connect a connector remotely', 'bring my own agent', or any work editing a Base44 app inside a sandbox."

**`base44-sdk`**
- Description: "The base44 SDK is the library to communicate with base44 services. In projects, you use it to communicate with remote resources (entities, backend functions, ai agents) and to write backend functions. This skill is the place for learning about available modules and types. When you plan or implement a feature, you must learn this skill"

**`calle`**
- Description: Use CALL-E from skills.sh compatible agents through the calle CLI. Use for CALL-E setup checks, authentication recovery, phone call planning, placing real outbound calls, call status polling, summaries, details, and transcripts.

**`docx`**
- Description: "Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of 'Word doc', 'word document', '.docx', or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks unrelated to document generation."

**`find-skills`**
- Description: Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express interest in extending capabilities. This skill should be used when the user is looking for functionality that might exist as an installable skill.

**`geo-audit`**
- Description: Full website GEO+SEO audit with parallel subagent delegation. Orchestrates a comprehensive Generative Engine Optimization audit across AI citability, platform analysis, technical infrastructure, content quality, and schema markup. Produces a composite GEO Score (0-100) with prioritized action plan.

**`geo-update`**
- Description: Pull the latest GEO-SEO skill updates from the upstream repository. Compares installed files against the latest release, shows what changed, and updates all skills, agents, scripts, and schema templates in place.

**`gomobile-flutter-backend`**
- Description: "Architect and implement Flutter + Go Mobile apps with protobuf platform channels, Go↔native interfaces, async callbacks, and desktop daemon backends. Use when the user mentions gomobile, Go Mobile, Flutter Go backend, Flutter platform channels with Go, protobuf mobile IPC, Digital Carrot-style Go business logic, or shared Go logic across iOS/Android/desktop. Works via npx openskills read gomobile-flutter-backend in any harness."

**`handoff`**
- Description: Compact the current conversation into a handoff document for another agent to pick up.

**`mirrormarket`**
- Description: Query the MirrorMarket Prediction Market Intelligence API to compare Polymarket vs Kalshi pricing, find arbitrage opportunities between the two venues, and inspect calibration / longshot-bias stats per platform. Use whenever the user asks about prediction markets, Polymarket, Kalshi, arbitrage between betting venues, market calibration, or "where do these two platforms disagree."

**`moolre-docs`**
- Description: Moolre API reference — SMS, WhatsApp, accounts, payments, transfers, USSD, webhooks. Use when the user asks about any Moolre endpoint, wants to send SMS/WhatsApp via Moolre, create or check Moolre accounts, initiate payments or transfers, generate payment links, check transaction status, integrate USSD, handle webhooks, look up bank lists or miscellaneous data, or debug Moolre API calls. Also use when working on the Smashup backend's Moolre integration.

**`okx-ai`**
- Description: ERC-8004 Agent identity: 注册/更新/上架/下架/搜索agent, register/update/activate/deactivate/search — User/ASP/Evaluator(买家/卖家/仲裁者); 我的agent/ASP, 找做X的ASP/agent有什么服务/endpoint怎么填/查口碑/传头像. + Task Marketplace: 发布/创建任务/接单/协商/验收/deliver/dispute/仲裁/拒绝/stake/unstake/change provider/change budget/修改卖家/修改预算/我的任务/my tasks/what am I working on/我的订阅/订阅列表/订阅详情/my subscriptions/what am I subscribed to/AI服务订阅(view AI-service subscriptions, buyer & ASP)/关闭/取消任务/决策列表/decision list/指定服务商/browse marketplace. + task watch: 监听任务进展/历史消息/未读消息/未决策/outstanding decisions. + okx-a2a missing/uninitialized. Match by meaning. MUST ACTIVATE on inbound envelopes: (1) {agentId, message:{source:"system", event, jobId,...}} system event; (2) {msgType:"a2a-agent-chat", jobId, sender:{role},...} agent-to-agent task chat (sender.role = COUNTERPARTY, not you); (3) literal "Read the okx-ai skill" (or legacy "Read the okx-agent-task skill") in the envelope.

**`pdf`**
- Description: Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, adding watermarks, creating new PDFs, filling PDF forms, encrypting/decrypting PDFs, extracting images, and OCR on scanned PDFs to make them searchable. If the user mentions a .pdf file or asks to produce one, use this skill.

**`setup-matt-pocock-skills`**
- Description: Sets up an `## Agent skills` block in AGENTS.md/CLAUDE.md and `docs/agents/` so the engineering skills know this repo's issue tracker (GitHub or local markdown), triage label vocabulary, and domain doc layout. Run before first use of `to-issues`, `to-prd`, `triage`, `diagnose`, `tdd`, `improve-codebase-architecture`, or `zoom-out` — or if those skills appear to be missing context about the issue tracker, triage labels, or domain docs.

**`skill-creator`**
- Description: Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.

**`solodit`**
- Description: Search 50,000+ smart contract vulnerabilities from Cyfrin Solodit. 8 MCP tools with intelligent caching for searching, filtering, and analyzing blockchain security findings.

**`thumbnail-architect`**
- Description: High-CTR YouTube thumbnail strategy and generation prompt workflow. Use this skill whenever the user asks for YouTube thumbnail ideas, thumbnail prompts, CTR thumbnails, mobile-readable thumbnails, 1280x720 artwork, title-to-thumbnail concepts, or 5 thumbnail concepts. Especially use it for story channels, Afro-Korean mafia romance/drama, faceless narration, revenge stories, betrayal hooks, documentary thumbnails, and any niche where the thumbnail must stop scrolling. Outputs 5 concepts, chooses the strongest, and prepares AI33 Pro image-generation prompts.

**`xlsx`**
- Description: "Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user references a spreadsheet file by name or path — even casually (like \"the xlsx in my downloads\") — and wants something done to it or produced from it. Also trigger for cleaning or restructuring messy tabular data files (malformed rows, misplaced headers, junk data) into proper spreadsheets. The deliverable must be a spreadsheet file. Do NOT trigger when the primary deliverable is a Word document, HTML report, standalone Python script, database pipeline, or Google Sheets API integration, even if tabular data is involved."

**`zoom-out`**
- Description: Tell the agent to zoom out and give broader context or a higher-level perspective. Use when you're unfamiliar with a section of code or need to understand how it fits into the bigger picture.


### security/audit

**`"source-command-sc-analyze"`**
- Description: "Comprehensive code analysis across quality, security, performance, and architecture domains"

**`configuring-audit-logging`**
- Description: Configures SQL audit logging on CockroachDB clusters to capture security-relevant events including authentication, privilege changes, and sensitive data access. Use when enabling audit logging for compliance, setting up role-based audit policies, or verifying audit configuration.

**`configuring-ip-allowlists`**
- Description: Configures and hardens IP allowlists for CockroachDB Cloud clusters to restrict network access to authorized CIDR ranges. Use when tightening network security, removing overly permissive allowlist entries like 0.0.0.0/0, or setting up allowlists for a new cluster.

**`configuring-log-export`**
- Description: Configures log and metric export for CockroachDB Cloud clusters to external monitoring services including AWS CloudWatch, GCP Cloud Logging, and Datadog. Use when setting up log export for audit compliance, configuring metric export for monitoring, or troubleshooting log delivery issues.

**`enabling-cmek-encryption`**
- Description: Enables Customer-Managed Encryption Keys (CMEK) on CockroachDB Cloud clusters with the Advanced plan and Advanced Security Add-on to give organizations control over data-at-rest encryption keys via their cloud provider's KMS. Use when enabling CMEK for compliance, rotating encryption keys, or verifying CMEK configuration.

**`geo-compare`**
- Description: Monthly delta tracking and progress reporting for GEO clients. Compares two GEO audits (baseline vs. current), calculates score improvements across all categories, tracks action item completion, and generates a "here's your progress" client report. Use when user says "compare", "delta", "monthly report", "progress", "confronta", "progressi", "report mensile", or when running a monthly client check-in.

**`geo-platform-optimizer`**
- Description: Platform-specific AI search optimization — audit and optimize for Google AI Overviews, ChatGPT, Perplexity, Gemini, and Bing Copilot individually

**`geo-proposal`**
- Description: Auto-generate a professional, client-ready GEO service proposal from audit data. Creates a full proposal in markdown and PDF including executive summary, findings, recommended service packages (Basic/Standard/Premium), pricing, timeline, and terms. Use when user says "proposal", "proposta", "offerta", "preventivo", "generate proposal", or after completing a GEO audit for a prospect.

**`geo-prospect`**
- Description: CRM-lite for managing GEO agency prospects and clients. Track leads through the full sales pipeline: Lead → Qualified → Proposal Sent → Won → Lost. Store audit history, notes, deal values, and generate pipeline summaries. Use when user says "prospect", "lead", "client", "pipeline", "crm", "nuovo prospect", "aggiungi cliente", or when managing the business side of GEO services.

**`geo-report`**
- Description: Generate a professional, client-facing GEO report combining all audit results into a single deliverable with scores, findings, and prioritized actions

**`x-ray`**
- Description: "Generates an x-ray.md pre-audit report covering overview, enhanced threat model (protocol-type profiling, git-weighted attack surfaces, temporal risk analysis, composability dependency mapping), invariants, integrations, docs quality, test analysis, and developer/git history. Triggers on 'x-ray', 'audit readiness', 'readiness report', 'pre-audit report', 'prep this protocol', 'protocol prep', 'summarize this protocol'."


### research/analytics

**`"source-command-sc-research"`**
- Description: "Deep web research with adaptive planning and intelligent search"

**`geo-crawlers`**
- Description: AI crawler access analysis. Checks robots.txt, meta tags, and HTTP headers to determine which AI crawlers can access the site. Provides a complete access map and recommendations for maximizing AI visibility while maintaining appropriate control.


### database/infrastructure

**`configuring-private-connectivity`**
- Description: Configures private network connectivity for CockroachDB Cloud clusters including AWS PrivateLink, GCP Private Service Connect, Azure Private Link, egress private endpoints, and VPC peering. Use when setting up private endpoints to eliminate public internet exposure, configuring egress to external services like Kafka, or establishing VPC peering.

**`configuring-sso-and-scim`**
- Description: Configures SSO authentication and SCIM 2.0 provisioning for CockroachDB across four distinct layers — Cloud Console SSO (SAML/OIDC), DB Console SSO (OIDC), SQL/Cluster SSO (JWT or LDAP/AD), and SCIM 2.0 automated provisioning. Use when enabling centralized identity management, setting up SSO for compliance, or automating user lifecycle management.

**`managing-certificates-and-encryption`**
- Description: Manages TLS certificate and encryption key lifecycle across all tiers. Self-Hosted covers certificate expiry monitoring, node/CA/client cert rotation, and Kubernetes cert management. Advanced/BYOC covers managed TLS (no action) and CMEK (Customer-Managed Encryption Key) rotation in your KMS. Standard and Basic have fully managed TLS and encryption with no customer action. CMEK is only available on Advanced. Use when monitoring cert health, performing rotation, managing CMEK, or responding to key compromise.

**`managing-tls-certificates`**
- Description: Manages TLS certificates for CockroachDB clusters including CA certificate configuration, client certificate authentication, certificate rotation, and troubleshooting SSL/TLS connection errors. Use when setting up client certificate auth, resolving SSL connection failures, rotating certificates, or configuring mTLS for CDC changefeeds.

**`monitoring-background-jobs`**
- Description: Monitors CockroachDB background job health by identifying failed, paused, and long-running jobs using SHOW JOBS and SHOW AUTOMATIC JOBS. Surfaces schema changes, backups/restores, automatic statistics collection, and SQL stats compaction jobs without DB Console access. Use when investigating schema change delays, failed backups, or automatic job issues.

**`performing-cluster-maintenance`**
- Description: Manages planned cluster maintenance across all tiers. Self-Hosted covers node drain procedures for OS patching, hardware changes, and configuration updates. Advanced/BYOC covers maintenance window configuration, patch scheduling, deferral policies, and monitoring during CRL-managed maintenance. Standard and Basic maintenance is fully managed with no customer action. Use when planning maintenance, configuring maintenance windows, or preparing applications for maintenance events.

**`profiling-statement-fingerprints`**
- Description: Ranks and analyzes statement fingerprints using aggregated SQL statistics from crdb_internal.statement_statistics to identify slow, resource-intensive, or error-prone query patterns. Use when investigating historical performance trends, identifying optimization opportunities, or diagnosing recurring slowness without DB Console access.

**`setting-up-local-cluster`**
- Description: Downloads and starts a local CockroachDB cluster for development using the official binary. Use when a developer needs a local CockroachDB instance, when no cluster is available, or when setting up a new development environment.

**`triaging-live-sql-activity`**
- Description: Diagnoses live CockroachDB cluster performance issues by identifying long-running queries, busy sessions, and active transactions using SQL-only interfaces. Use when users report cluster slowness, high CPU, or need to find runaway queries and their source applications without DB Console access.


### general/other

**`"source-command-sc-cleanup"`**
- Description: "Systematically clean up code, remove dead code, and optimize project structure"

**`"source-command-sc-estimate"`**
- Description: "Provide development estimates for tasks, features, or projects with intelligent analysis"

**`"source-command-sc-explain"`**
- Description: "Provide clear explanations of code, concepts, and system behavior with educational clarity"

**`"source-command-sc-git"`**
- Description: "Git operations with intelligent commit messages and workflow optimization"

**`"source-command-sc-help"`**
- Description: "List all available /sc commands and their functionality"

**`"source-command-sc-improve"`**
- Description: "Apply systematic improvements to code quality, performance, and maintainability"

**`"source-command-sc-task"`**
- Description: "Execute complex tasks with intelligent workflow management and delegation"

**`"source-command-sc-test"`**
- Description: "Execute tests with coverage analysis and automated quality reporting"

**`algorithmic-art`**
- Description: Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generative art, algorithmic art, flow fields, or particle systems. Create original algorithmic art rather than copying existing artists' work to avoid copyright violations.

**`diagnose`**
- Description: Disciplined diagnosis loop for hard bugs and performance regressions. Reproduce → minimise → hypothesise → instrument → fix → regression-test. Use when user says "diagnose this" / "debug this", reports a bug, says something is broken/throwing/failing, or describes a performance regression.

**`grill-with-docs`**
- Description: Grilling session that challenges your plan against the existing domain model, sharpens terminology, and updates documentation (CONTEXT.md, ADRs) inline as decisions crystallise. Use when user wants to stress-test a plan against their project's language and documented decisions.

**`improve-codebase-architecture`**
- Description: Find deepening opportunities in a codebase, informed by the domain language in CONTEXT.md and the decisions in docs/adr/. Use when the user wants to improve architecture, find refactoring opportunities, consolidate tightly-coupled modules, or make a codebase more testable and AI-navigable.

**`migrate-to-shoehorn`**
- Description: Migrate test files from `as` type assertions to @total-typescript/shoehorn. Use when user mentions shoehorn, wants to replace `as` in tests, or needs partial test data.

**`profiling-transaction-fingerprints`**
- Description: Analyzes transaction fingerprints using aggregated statistics from crdb_internal.transaction_statistics to identify high-retry transactions, contention patterns, and commit latency issues. Provides historical transaction-level analysis to understand which statement combinations are causing retries, contention, or performance degradation. Use when investigating transaction retry storms, analyzing commit latency trends, or understanding statement composition of problematic transactions without DB Console access.

**`scaffold-exercises`**
- Description: Create exercise directory structures with sections, problems, solutions, and explainers that pass linting. Use when user wants to scaffold exercises, create exercise stubs, or set up a new course section.

**`setup-pre-commit`**
- Description: Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. Use when user wants to add pre-commit hooks, set up Husky, configure lint-staged, or add commit-time formatting/typechecking/testing.

**`to-issues`**
- Description: Break a plan, spec, or PRD into independently-grabbable issues on the project issue tracker using tracer-bullet vertical slices. Use when user wants to convert a plan into issues, create implementation tickets, or break down work into issues.

**`to-prd`**
- Description: Turn the current conversation context into a PRD and publish it to the project issue tracker. Use when user wants to create a PRD from the current context.


---

## 4. Installing this workflow

Use the `kaizen-mega` skill to route to the correct domain skill from this catalog.