# Case study: Vault OTP (reference quality)

**Status:** Canonical product UI for Design ProMax **`clean_product`** style.  
**Surface:** H (`wallet_dapp` / vault_or_dapp_shell)  
**Style:** `clean_product` (locked)  
**Repo (example):** Monad Vault OTP — Astro + React + HeroUI v2 + Iconify Solar  

When the user says “like Vault OTP”, “those cards”, “that button feel”, or “same style as before” → **replay this case study**, not a random marketing theme.

---

## What made it feel good

| Layer | What we did |
|-------|-------------|
| **Layout** | `max-w-3xl mx-auto`, vertical `gap-6`, airy page padding |
| **Top bar** | One card-like bar: icon tile + name + wallet controls |
| **Hero** | Chips → one headline → one lede (no paragraphs of tech) |
| **Features** | Exactly **3** ActionCards, grid on sm |
| **Gates** | Connect / wrong network / unlock each = **one Card + one primary Button** |
| **Work** | Form Card + stacked content Cards (not raw lists) |
| **Buttons** | Almost all `radius="full"`; clear primary / bordered / flat danger / light |
| **Icons** | Solar bold-duotone for tiles; linear for small actions |
| **Color** | Soft green primary (`#0F8A52` family); light zinc background |
| **Copy** | Human. No “ciphertext / Polybase / on-chain storage” footers |

---

## Button matrix (copy this)

| Role | HeroUI props | Example label |
|------|----------------|---------------|
| **Primary CTA** | `color="primary" radius="full"` + optional `startContent` bold solar icon | Connect wallet, Sign to unlock, Encrypt & store |
| **Primary loading** | same + `isLoading` — drop startContent while loading | Confirm in wallet… |
| **Secondary** | `variant="bordered" radius="full" size="sm"` + linear icon | Copy, Refresh |
| **Danger** | `color="danger" variant="flat" radius="full" size="sm"` + trash linear | Delete |
| **Warning action** | `color="warning" radius="full"` or `variant="flat"` | Switch network |
| **Ghost / light** | `variant="light" radius="full" size="sm"` | Disconnect |
| **Icon-leading** | Always `startContent={<Icon icon="solar:…" width={16\|18} />}` | — |

**Rules:**
- Prefer **full pills** (`radius="full"`) over default medium radius for product CTAs  
- One **primary filled** button per card/region  
- Secondary actions never compete with primary (bordered/flat, smaller)  
- `onPress` (HeroUI) not only raw `onClick` for Buttons  

---

## Card matrix

| Kind | Classes / pattern |
|------|-------------------|
| **Default card** | `border-small border-default-200 shadow-sm` + `CardBody p-4` or `p-6` |
| **Top bar** | same as card, horizontal flex, brand left / actions right |
| **Action / feature** | From `action-card.tsx`: icon wrapper `bg-primary-50 border-primary-100`, title + `text-small text-default-400` |
| **Gate (neutral)** | Default card; icon tile default-50; CTA right (stack on mobile) |
| **Gate (warning)** | `border-warning-500`; icon `bg-warning-50 text-warning-600` |
| **Error** | `border-danger-300`; danger icon + `text-small text-danger` |
| **Empty** | `border-dashed border-default-200 shadow-none`; centered duotone icon |
| **List row** | Full card per item (SecretCodeCard pattern): icon + titles left, hero metric right, Progress, action row |

---

## Icon matrix (Solar)

| Use | Style | Examples |
|-----|--------|----------|
| Brand / feature tiles | `*-bold-duotone` | shield-keyhole, lock-keyhole, wallet, cloud-storage, smartphone-2, key |
| Primary CTA | `*-bold` or bold-duotone | wallet-bold, pen-new-square-bold, cloud-upload-bold |
| Inline field | `*-linear` default-400 | global-linear, user-linear, lock-password-linear, qr-code-linear |
| Small actions | `*-linear` | copy-linear, trash-bin-trash-linear, refresh-linear |
| Alerts | bold | danger-triangle-bold, danger-circle-bold, transfer-horizontal-bold |

Source library: `@iconify/react` → https://icon-sets.iconify.design/solar/

---

## Compose order (fixed)

```
1. Top bar (logo tile + title + ConnectButton cluster)
2. Status chips (2–3 max)
3. Hero title + one lede
4. Three ActionCards
5. Exactly one gate card for current state
6. Main form card (if unlocked)
7. Section header + list of content cards / empty card
8. Error card if needed
9. STOP — no tech footer
```

---

## HeroUI sources to open (efficient = 3 files)

For this feel, **do not** open the whole Application tree. Only:

1. `Application/cards (20)__action-card.tsx`  
2. `Application/authentication (24)__App.tsx`  
3. `Application/cards (20)__security-settings.tsx`  

Optional 4th: `Application/navbars (3)__App.tsx` if you need a denser top nav.

---

## Theme tokens (green trust)

```js
// tailwind heroui theme sketch
primary.DEFAULT = "#0F8A52"
background = "#F4F4F5"
// soft radial green washes on body — never full-page purple AI gradient
```

Fonts: **IBM Plex Sans** + **IBM Plex Mono** for codes/addresses.

---

## Flavors of the same family

| Flavor id | When | Differs from vault by… |
|-----------|------|-------------------------|
| `clean_product` | Default product / dapp / vault | This case study |
| `clean_product_compact` | Mobile-first / dense phone UI | Tighter gap-4, hide feature row |
| `trust_green` | Finance / security products | Same structure; force green primary tokens |
| `marketing_campaign` | Landing only | More sections + footer; still action/feature cards |
| `dense_admin` | Tables / analytics | Sidebar + KPIs; keep card borders |

All flavors share: **full-radius CTAs, bordered inputs, solar icons, no eng footers.**

---

## Anti-patterns (this case study failed before)

- Homemade CSS buttons instead of HeroUI `Button`  
- Architecture paragraphs in the UI  
- Contract address footer  
- Wrong-network as plain text without Switch CTA  
- Feature wall of 6+ cards  
- Mixing checkout field chrome with chat shells  
