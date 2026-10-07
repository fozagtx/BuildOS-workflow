# Full-session lesson log (~10h NairaShield)

Source: compaction summaries + live corrections across landing polish, agent build, auth, dashboard shell, logo.

## Phase A — Landing / ProMax UI

| User intent | Failure mode | Rule |
|-------------|--------------|------|
| Light mode default | Dark/default chaos | Force light default |
| Design ProMax | Hallucinated components | Read ProMax sources |
| No eng jargon | Stack lectures on landing | Plain product language |
| Real metrics only | Mock charts / demo series | Delete chart-demo; empty states |
| Keep dashboard CTA | Dashboard felt like login-only | Restore Open dashboard / Get started |
| bg.jpg premium | Applied wrong surface | Atmosphere on marketing, not dashboard |
| No GitHub footer | Social filler | Remove empty social |
| Fonts | Generic AI fonts | Sora + Plus Jakarta (or product pick) |
| Built on marquee | Static “Works with” | ProMax scrolling marquee |
| Odds on dashboard | Missing real tick fields | Show team/spread from real ticks |

## Phase B — Landing refinements

| User intent | Failure mode | Rule |
|-------------|--------------|------|
| BG only on landing | BG on dashboard | Scope bg to landing/hero |
| Header base not sticky | Sticky glass nav | header-base, not glued top |
| Hero-only bg | Bg from under header/full page | Hero owns atmosphere; text contrast intact |
| Floating nav compact | Spacious pill | rounded-xl + border, denser |
| No useless SVGs then images then remove | Image thrash | Default no junk product photos |
| Remove Product nav | Extra marketing links | Only real destinations |
| Short hero + N logo | Long hero, shield icons | Compact hero; N mark |
| Get started CTA | Waitlist-first forever | Get started → auth/dashboard |
| Remove waitlist only | Also killed How/FAQ/Help | Read narrowly; keep required sections |
| PAS anti-slop | Contrast-slop, em dashes | PAS copy; no em dashes |
| Real Talk ban | “The truth is…”, “not just X”, “let’s break it down” | Delete openers; state the claim |
| Marquee blend | Separate bg band | Transparent marquee on hero |
| Card border/hover/animation | Sloppy charts, tilt | Real borders; no axis gimmicks |

## Phase C — Agent backend

| User intent | Failure mode | Rule |
|-------------|--------------|------|
| Build agents fully | Half stubs | Full pipeline + routes |
| Comply with handoff/research | Arb-style brain | Market make + Y_net + settlement |
| No mocks | Demo odds/vaults/orders | Fail closed |
| Policy in config.ts | Policy in .dev.vars | Secrets vs policy split |
| Google OAuth | Incomplete auth story | Full OAuth + exchange |
| Generate secrets | Left SESSION empty | Generate SESSION_SECRET / keys; never invent Google client secrets |

## Phase D — Local + OAuth + dashboard app

| User intent | Failure mode | Rule |
|-------------|--------------|------|
| Local dev works | Wrong folder npm | Correct package roots |
| Port already in use | Panic restart loops | Kill or reuse deliberately |
| OAuth callback unreachable | IPv6 vs 127.0.0.1 | One host; bind 127.0.0.1 |
| Ticks spam “failed” | Vague error + no TxLINE | Explicit HOLD reasons |
| Sidebar “hanging” | Bad flex shell | h-dvh full-height rail |
| Scroll nav on dashboard | Landing pattern | View switcher |
| Profile on top | Wrong chrome | Profile bottom |
| Run check × N | Duplicate CTAs | One primary action |
| Sign in only | Blocks mental model of signup | Sign up / Sign in |
| Stress shadow recursion | Always-mounted drawer/modal | Unmount when closed; poll lock |
| Old logo remains | Auth circle N, stale favicon | BrandMark + favicon family |
| Commit description / AI trailers | Invented body | Short subject; user author only |

## Chronological intent (compressed)

1. Fix UI (frontend-design + design-promax)  
2. White/light mode default  
3. ProMax fix UI  
4. Stop eng jargon  
5. Hierarchy, cards, animation, charts  
6. bg.jpg premium  
7. No mock metrics; keep dashboard + odds; marquee; fonts; no GitHub  
8. BG landing not dashboard  
9. Header base not sticky  
10. Wrangler agent + Google auth  
11. Hero-only bg; marquee quality; floating nav  
12. No useless images; remove Product; short hero; N logo; Get started  
13. Keep How/FAQ/Help after waitlist removal  
14. PAS anti-slop; typography; marquee blend; rounded header; cards  
15. Build agents everything  
16. No mocks; PRD compliance; config.ts policy  
17. OAuth guide; local worker; secrets  
18. Dashboard shell; views not scroll; profile bottom; one Run check  
19. Sign up + sign in; logo/favicon  
20. Capture skill for reuse  

## Reuse prompt

```
Apply /bypass-slop for this whole product pass.
Landing: hero-only bg, header-base, rounded-xl bordered nav, PAS no em dashes,
real metrics only, keep How/FAQ/Help if product needs them, transparent marquee.
Dashboard: view switcher, profile bottom, one primary CTA, full-height shell.
Agent: no mocks, policy in config.ts, secrets in env, PRD strategy, clear HOLD reasons.
Auth: Sign up / Sign in (Google). Brand: one BrandMark + favicon family.
Git: short message, no AI trailers. Stress-safe poll and unmounted overlays.
```
