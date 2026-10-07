# Design ProMax — Template Router (human guide)

**Machine source of truth:** [ROUTE_REGISTRY.json](ROUTE_REGISTRY.json)  
**Harness contract:** [ARCHITECTURE.md](ARCHITECTURE.md)

**Problem:** `sources/` has 300+ files. Opening random folders produces slop.  
**Rule:** Route first via the registry. Open **2–4 primary files** only. Never load a whole category.

Path prefix for all files: `sources/` (relative to this skill folder).  
If JSON and this doc disagree, **JSON wins**.

---

## Step 0 — Classify the job (30 seconds)

Pick **exactly one** primary surface (what the user spends time looking at):

| Code | Surface | If user says… |
|------|---------|----------------|
| **A** | Marketing / landing | landing, homepage, hero, pricing, FAQ, waitlist, marketing |
| **B** | Auth | login, signup, sign in, register, forgot password |
| **C** | App shell / dashboard | dashboard, app, console, settings, sidebar, admin |
| **D** | Chat / AI | chat, AI, copilot, messages, prompt, playground |
| **E** | Commerce | product, cart, checkout, shop, reviews, filters |
| **F** | Data / charts | table, KPI, chart, graph, analytics, stats |
| **G** | Forms / wizards | multi-step, onboarding wizard, long form, stepper |
| **H** | Wallet / crypto dapp | wallet connect, vault, onchain, dapp, authenticator, DeFi UI |

Then pick **density**:

| Density | When |
|---------|------|
| **Sparse** | Landing, empty states, unlock/connect gates, marketing |
| **Medium** | Settings, forms, card grids, product pages |
| **Dense** | Tables, dashboards, chat threads, checkout |

Then pick **chrome**:

| Chrome | When |
|--------|------|
| **Marketing chrome** | Top nav + hero + sections + footer (no app sidebar) |
| **App chrome** | Sidebar and/or top bar + main content (logged-in product) |
| **Focused chrome** | Centered card only (auth, unlock, modal-like gates) |

---

## Step 1 — Intent → best template pack (read these first)

### A — Marketing / landing

| Sub-intent | Primary (read first) | Secondary (if needed) | Avoid |
|------------|----------------------|------------------------|-------|
| Full landing | `Marketing/hero-sections (4)__App.tsx` | `Marketing/faqs (4)__*.tsx`, `Marketing/footers (4)__*.tsx` | Application sidebars |
| Pricing | `Marketing/pricing (8)__pricing*.tsx` | `Marketing/pricing-comparison (8)__*.tsx` | Random cards only |
| Feature grid | `AI/features (1)__feature-card.tsx` + `AI/features (1)__App.tsx` | `Marketing/banners (8)__*.tsx` | Dense tables |
| Banner / promo | `Marketing/banners (8)__*.tsx` | — | Full dashboard layouts |

**Compose order:** Hero → features/pricing → FAQ → footer.  
**Icons:** `solar:*-bold-duotone` for feature tiles; keep marketing airy.

---

### B — Auth

| Sub-intent | Primary | Secondary | Avoid |
|------------|---------|-----------|-------|
| Login / signup | `Application/authentication (24)__App.tsx` | `Application/authentication (24)__acme.tsx` (logo) | Sidebars, tables |
| Centered gate (unlock, connect) | Same auth App shell pattern | `Application/cards (20)__action-card.tsx` for helper tips | Marketing footers full of links |

**Compose order:** Logo/title → `bg-content1 rounded-large shadow-small` form card → primary CTA full width → optional OR divider.  
**Density:** Focused chrome.  
**Do not** put contract addresses or eng jargon on auth screens.

---

### C — App shell / dashboard

| Sub-intent | Primary | Secondary | Avoid |
|------------|---------|-----------|-------|
| Sidebar app | `Application/sidebars (19)__sidebar*.tsx` (pick one complete App) | `Application/navbars (3)__*.tsx` | Marketing heroes as page body |
| Settings / profile | `Application/Layouts (2)__*-setting*.tsx` or `Application/cards (20)__security-settings.tsx` | `Application/cards (20)__account-details.tsx`, `cell-wrapper.tsx` | Landing hero |
| Notification list | `Application/cards (20)__notification-item.tsx` | `notifications-settings.tsx` | Pricing |
| Action tiles | `Application/cards (20)__action-card.tsx` | `AI/features (1)__feature-card.tsx` | Tables for 3 items |

**Compose order:** Shell (nav/sidebar) → page title + short lede → content cards/list.  
**Density:** Medium unless data-heavy (then F).

---

### D — Chat / AI

| Sub-intent | Primary | Secondary | Avoid |
|------------|---------|-----------|-------|
| Full chat app | `AI/prompt-containers (11)__App.tsx` | `conversation.tsx`, `message-card.tsx`, `prompt-input*.tsx`, `sidebar*.tsx` | Marketing heroes |
| Message bubble only | `AI/prompt-containers (11)__message-card.tsx` | `AI/messages (6)__message-card.tsx` | Checkout |
| Prompt box | `AI/prompt-inputs (11)__prompt-input*.tsx` | `prompt-containers … prompt-input-with-bottom-actions*.tsx` | Auth form layout |
| Playground | `AI/playgrounds (1)__App.tsx` | conversation + prompt-input | Pricing |

**Compose order:** Sidebar (history) optional → messages column → sticky prompt input.  
**Density:** Dense in thread; sparse empty state.

---

### E — Commerce

| Sub-intent | Primary | Secondary | Avoid |
|------------|---------|-----------|-------|
| Product grid | `E-commerce/product-list (9)__products-grid.tsx` + `product-list-item.tsx` | `filters (9)__*.tsx` | AI chat shell |
| Product detail | `E-commerce/product-view (1)__product-view-item.tsx` | rating radio groups | Sidebars full app |
| Filters | `E-commerce/filters (9)__filters-wrapper.tsx` | price-slider, tag-group | Auth |
| Checkout | `E-commerce/checkouts (4)__App.tsx` | payment-form, order-summary, shipping-form | Chat |
| Reviews | `E-commerce/reviews (6)__reviews.tsx` + `card-review.tsx` | summary-rating-card | — |

**Compose order:** Grid or detail first; filters as rail/drawer; checkout multi-column summary + form.

---

### F — Data / charts

| Sub-intent | Primary | Secondary | Avoid |
|------------|---------|-----------|-------|
| KPI row | `Charts/KPI-stats (9)__App.tsx` | individual stat patterns in same folder | Hero marketing |
| Bar / donut | `Charts/Bars-and-Circles (10)__App.tsx` | — | Auth cards |
| Line / area | `Charts/Graphs (2)__App.tsx` | — | — |
| Data table | `Application/tables (1)__*.tsx` | Command Menus for search | Feature cards only |

**Compose order:** KPI row → chart → table.  
**Density:** Dense; keep cards `shadow-small border-default-200`.

---

### G — Forms / wizards

| Sub-intent | Primary | Secondary | Avoid |
|------------|---------|-----------|-------|
| Multi-step form | `Application/forms (1)__*.tsx` (all) | `Application/steppers (7)__*.tsx` | Single huge unsectioned form |
| Step indicator only | `Application/steppers (7)__*.tsx` | forms folder for fields | — |
| Calendar booking | `Application/calendar (3)__App.tsx` | booking-form, calendar-time-select | Checkout copy-paste |

**Compose order:** Stepper → one step card → primary continue.  
**Density:** Medium; one primary CTA per step.

---

### H — Wallet / crypto dapp (not in original HeroUI packs — **compose**)

There is no `Wallet/` folder. **Compose** from these only:

| UI piece | Route to |
|----------|----------|
| Connect / unlock gate | `Application/authentication (24)__App.tsx` (centered card) |
| Top bar + brand + wallet chip | `Application/navbars (3)__*.tsx` + Chip/Button patterns from auth |
| Feature explainer tiles | `Application/cards (20)__action-card.tsx` |
| Security / settings rows | `Application/cards (20)__security-settings.tsx` + `cell-wrapper.tsx` |
| Code / secret list rows | Security cells OR notification-item spacing; Progress for timers |
| Status banners (wrong network) | Action-card **warning** / **danger** color variants |
| Form fields | Auth `Input variant="bordered"` |
| Icons | `@iconify/react` `solar:*-bold-duotone` (lock, wallet, shield, key) |

**Never** put README/architecture copy in the UI. Product language only.

**Compose order (Vault OTP quality bar):**  
1. Top bar (logo + connect)  
2. Short hero (1 headline + 1 line)  
3. 3 action cards  
4. Gate card (connect / network / unlock)  
5. Main form + list cards  
6. No tech footer  

---

## Step 2 — Form component router (fields, not full pages)

When building **forms**, pick field patterns from the **same surface** as the page:

| Field need | Best source |
|------------|-------------|
| Email / password / bordered inputs | `authentication (24)__App.tsx` |
| Settings toggles / row actions | `cards (20)__security-settings.tsx`, `switch-cell` if present |
| Address / shipping / payment | `checkouts (4)__*-form.tsx` |
| Filters / chips / price | `filters (9)__*.tsx` |
| Chat composer | `prompt-input*.tsx` |
| Booking date/time | `calendar (3)__*.tsx` |
| Rating | `reviews (6)__rating-radio-*.tsx` |

**Rule:** Do not mix checkout field chrome with marketing hero spacing. Match the page density.

---

## Step 3 — Anti-slop routing (reject these defaults)

| Temptation | Instead route to |
|------------|------------------|
| Generic “3 feature cards with Lorem” | `action-card.tsx` or `feature-card.tsx` + real product copy |
| Purple gradient AI landing for a dapp | H compose pack (auth + action-card) |
| Dashboard sidebar on a marketing page | Marketing pack only |
| Sticky glass nav + fake metrics | Real empty states; no invented KPIs |
| Dumping 10 source files into one screen | Max 1 shell + 2 content patterns |
| Eng jargon in UI (ciphertext, calldata, Polybase) | User verbs: unlock, connect, copy code, add account |

---

## Step 4 — Quality bar (Vault OTP / GhostKeys / `clean_product`)

**Full layout recipe (not just a checklist):**  
`case-studies/vault-otp.md` + style id **`clean_product`** in `STYLE_PRESETS.json`.

That case study defines:

- Top bar + chips + short hero  
- Exactly **3 ActionCards**  
- Gate cards (connect / wrong network / unlock) with **one pill CTA** each  
- Form card + stacked content cards  
- Button matrix: primary full / secondary bordered / danger flat  
- Solar icons; human copy; **no** eng footers  

Before shipping UI, checklist:

1. **Routed** via `ROUTE_REGISTRY.json` (surface A–H)  
2. **Styled** via `STYLE_PRESETS.json` (default `clean_product`)  
3. **Read** `case-studies/vault-otp.md` when user wants that feel  
4. **Read 3–4 real source files** (not invented classNames)  
5. **Icons:** `@iconify/react` + `solar:` / `gravity-ui:`  
6. **Tokens:** `bg-content1`, `text-default-500/900`, `border-default-200`, `shadow-small`, `rounded-large/medium` (recolor primary to product theme if asked)  
7. **Components:** `forwardRef` + `cn` + `displayName` for reusable pieces  
8. **Copy:** human product language; no architecture footnotes  
9. **States:** empty / loading / error / wrong-network each have a card  
10. **One primary CTA** per viewport region  

---

## Step 5 — Quick decision tree (paste into agent thought)

```
What is the main screen?
  marketing → A + hero App.tsx
  login/signup/unlock → B + authentication App.tsx
  logged-in product → C + sidebar OR navbar App
  chat/AI → D + prompt-containers App.tsx
  shop → E + product-list or checkout App
  analytics → F + KPI + graphs
  multi-step → G + forms + steppers
  wallet/crypto dapp → H compose (auth + action-card + security-settings)
Then: open ONLY the Primary files → adapt → stop.
```

---

## Preferred file extensions

Prefer **`.tsx`** sources when both exist. Fall back to `.js` if needed.  
`__App.tsx` / `__App.js` = full composition reference.  
`__*-card.tsx` = extractable atom.  
`__data.js` / `__messages.js` = data separation pattern only.
