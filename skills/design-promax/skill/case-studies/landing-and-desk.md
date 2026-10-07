# Case study: landing + desk (reference split)

**Status:** Canonical when a product has a public story **and** a work surface.  
**Surfaces:** A (`marketing` / landing) **and** H or C (desk / dashboard)  
**Styles:** `marketing_campaign` on `/` · `clean_product` on `/desk`  
**Theme:** Any (Default, Brutalism, Glass, Mouve, or product palette). Theme retokens. It does not collapse the split.

When the user says “landing and dashboard”, “homepage and app”, “hero + how it works + the actual tool”, or hates a jammed one-pager → **replay this**, not Vault OTP stacked on a marketing page.

---

## What made it feel good

| Layer | What we did |
|-------|-------------|
| **Two routes** | `/` tells the story. `/desk` does the job. Distinct chrome. |
| **Landing nav** | HeroUI `Navbar` from `basic-navbar.tsx`. Icon + **name only**. Links: **Features**, How it works, Questions. CTA is the product verb, not Connect. |
| **Hero** | Clamp 40–64px, bold, tight tracking, **solid** foreground, **`text-balance`**, **no `<br />`**. The **full** locked job line. One lede. Two pills. |
| **Features** | `AI/features (1)__App.tsx` pattern: three **category** FeatureCards (what you already did / what it does / what it will not). Required. `#features`. |
| **How it works** | Three **step** FeatureCards. `#how`. Not a substitute for Features. |
| **Questions** | Accordion. Three human answers. |
| **Footer** | Brand + one line + Product / Help. Links include Features. |
| **Desk nav** | `Application/navbars (3)__App.tsx`. Brand links home. **One** Connect on the right. |
| **Desk headline** | **Same full job line as the landing.** `text-balance`. Never a 3-word stub. |

---

## Connect rule (non-negotiable)

| Page | Connect |
|------|---------|
| Landing `/` | **None.** CTA is Finish mint / Claim default / Open the desk. |
| Desk `/desk` | **Once**, in the navbar. Label: **Connect**. |
| Wrong network | Switch network button. Not a second Connect. |
| Disconnected desk | Navbar Connect is enough. No duplicate gate card. |

---

## Copy rule

Human product language. The job line is the headline, not the protocol.

**Use:** Paste the payment you already sent. / Load the request you already made.  
**Do not use in chrome:** Pre-flight, Coston2 chips, truncated vault addresses, Core Vault mint beside the logo, executor fee, XRPL transaction hash as the page title, attestation, calldata.

Keep live values (min fee, vault copy) **inside the form** where they are needed to finish the job.

---

## Hero type (do not fade, do not chop)

From `Marketing/hero-sections (4)__App.tsx` take size and weight.

**Keep:** `text-balance text-[clamp(40px,8vw,64px)] font-bold leading-[1.1] tracking-tighter text-foreground`  
**Drop:** `bg-hero-section-title bg-clip-text text-transparent` and the white-to-gray fade.  
**Drop:** `<br />` that parks three leftover words on line two.  
**Drop:** shortening the locked line (“The agent missed the window.” / desk h1 “Claim the collateral”).

Paste the **whole** job line. Use `text-balance` so it wraps as one headline. **Landing and desk use the same sentence.**

Wrong: `The agent missed the window.<br />Claim the collateral.`  
Right: `The agent missed the payment window. Claim the collateral.`

---

## Footer (do not ship ACME)

From `Marketing/footers (4)__App.tsx` take the layout (brand block + columns + bottom line).

**Keep:** Brand, one sentence, two columns of **real** links (Features, How it works, Open the desk, Questions).  
**Drop:** Newsletter, fake Services/Legal/social to `#`, lorem, contract addresses.

---

## Desk compose (when a landing exists)

```
1. Navbar (icon + name → `/`, Connect once)
2. The same full job line as the landing (`text-balance`, no `<br />`)
3. Wrong-network card only if connected on the wrong chain
4. Form card if unlocked
5. Session / status cards if work happened
6. STOP — no features row, no how-it-works row, no marketing footer, no eng chips
```

If there is **no** landing, fall back to `vault-otp.md` (chips + three ActionCards on the desk).

---

## HeroUI sources to open (4 per route)

**Landing**

1. `Marketing/hero-sections (4)__App.tsx`  
2. `Marketing/hero-sections (4)__basic-navbar.tsx`  
3. `AI/features (1)__feature-card.tsx`  
4. `Marketing/footers (4)__App.tsx`  

**Desk**

1. `Application/navbars (3)__App.tsx`  
2. `Application/authentication (24)__App.tsx`  
3. `Application/cards (20)__action-card.tsx`  
4. Optional: `Application/cards (20)__security-settings.tsx`  

---

## Anti-patterns (this split failed before)

- Hero + how it works + Connect + form on one scroll  
- Two Connect MetaMask buttons  
- Job subtitle under the logo  
- Gradient-clipped hero that fades to unreadable  
- Skinny homemade cards instead of FeatureCard / Navbar  
- Coston2 / vault-address / Pre-flight chips as “status”  
- Fake ACME footer and newsletter  
- Repeating how-it-works on the desk after it already lives on the landing  
- Glass blobs / IBM Plex / motion wallpaper when the user asked for the primitives, not a theme costume  
- `<br />` that leaves a three-word second line  
- Desk h1 shortened to three words while the landing has the full job line  
- Landing with How it works but **no Features section** (Features is required and distinct)  
