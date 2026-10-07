---
name: monad
description: Build on Monad — a high-performance EVM L1 (10,000 TPS, 400ms blocks, 800ms deterministic finality) with the Cadence consensus protocol and an encrypted mempool. Use when the user mentions Monad, Cadence consensus, MonadBFT, the BuildAnything/Spark hackathon, or is choosing what to build on a fast EVM chain. Covers the three design axes (speed, trustlessness, order-fairness), the load-bearing test, the on-chain/off-chain split, and how hackathon judges score Monad projects.
---

# Monad

A high-performance EVM-compatible L1. Everything below flows from three specs and one protocol.

## The specs

| Property | Value | What it unlocks |
|---|---|---|
| Throughput | **10,000 TPS** | Interaction layers (likes, replies, votes, ticks) fit on-chain, not just hashes |
| Block time | **400 ms** | Confirmation lands inside the human perception window |
| Finality | **800 ms deterministic** | Not probabilistic. No reorg risk to design around. |
| Mempool | **Encrypted** (via Cadence) | **Front-running and sandwiching are structurally impossible** |
| VM | **Full EVM** | Existing Solidity, tooling, and protocols compose |

The human-perception thresholds Monad designs against:
**<100 ms** = instant · **100 ms–1 s** = responsive · **>1 s** = user notices waiting · **>10 s** = user leaves.

Confirmation on programmable chains historically lived *outside* that zone. Applications adapted
(optimistic UIs, off-chain components, rollups). Sub-second deterministic finality means **the
application no longer has to adapt.** That absence-of-a-constraint is the entire thesis.

---

## THE LOAD-BEARING TEST (apply this before writing any code)

> **Would this project be impossible, or absurd, at 12-second blocks with a public mempool —
> and natural at 400 ms with an encrypted one?**

If it would work fine on Ethereum L1, **Monad is decorative** and the project is weak. Rescope.

A strong Monad project answers this in **one sentence**. Examples:

- *"You cannot gate an HTTP request on a 12-second confirmation. At 400 ms the payment settles inside the request."*
- *"A sealed-bid auction is impossible when anyone can read the mempool. Cadence encrypts bids until the order is already locked."*
- *"A 'like' that takes 12 seconds is unusable. At 400 ms the whole social graph fits on-chain."*

---

## The three axes

Monad's own material pushes three distinct unlocks. **Most builders optimize for one. The strongest
projects sit in an overlap.**

### Axis 1 — SPEED: "the constraint disappears"
The chain stops being a thing the user notices. Named unlocks:
1. **Order books as a composable primitive** — not just a DEX; a building block other contracts plug into (a lending protocol liquidating *through* the book)
2. **Games where the chain is the world** — persistent worlds that outlive the developer; shared state
3. **Social graphs on-chain** — likes, follows, reposts, replies as public utility, not company property
4. **Micropayments that compose with the EVM** — per-call API pricing, streaming payments by the second
5. **AI agents at machine speed** — non-custodial settlement at the pace agents actually transact
6. **Fast-moving markets** — oracles posting as fast as the data changes; no stale-price risk

### Axis 2 — TRUSTLESSNESS: "the code is the institution"
Value comes from the fact that **no one is in charge**:
- Anti-propaganda / AI-detection with tamper-proof public records
- Anti-censorship publishing — no platform, government, or company can remove it
- Verifiable voting — every vote on-chain, independently auditable, no black box
- Data ownership enforced by code, not a privacy policy

⚠️ **Read the qualifier: "at scale."** Censorship-resistance has existed since Ethereum. What was
*impossible* was putting **every** like/reply/vote on-chain instead of just a hash. **That's a
throughput problem** — which is the only reason Monad is the answer here and not any other L1.

### Axis 3 — ORDER-FAIRNESS: "MEV is structurally impossible" ⭐ MOST UNDER-EXPLOITED
Cadence's encrypted mempool means transactions are **unreadable until their order is already locked
in**. Consensus runs blind. You cannot front-run what you cannot read.

This makes a whole class of applications possible that need **commit-reveal schemes or ZK circuits
on every other chain** — and here you get them **free at the consensus layer**:

- **Sealed-bid auctions** (first-price, Vickrey) — genuinely impossible with a public mempool
- **Hidden-information games** — poker, Battleship, fog-of-war strategy, without coSNARKs
- **Order books that cannot be sandwiched** — the differentiated version of the crowded idea
- **Fair mints / launches** — no gas wars, no sniping
- **Prediction markets** where the oracle update can't be front-run
- **On-chain matching / RFQ** without the MEV tax
- **Blind voting** without a separate reveal phase

**Why this is the best axis:** an app that is impossible with a public mempool is impossible on
*every other chain*. That is the maximum possible score on the Load-Bearing Test.

### The overlap is where you build
```
   SPEED ────┐         ┌──── TRUSTLESSNESS
             │         │
             └────┬────┘
                  ▼
            ORDER-FAIRNESS
   Two axes = strong. Three = unbeatable.
```
Example hitting all three: **a sealed-bid, on-chain auction house where the bid ledger is public and
permanent, no operator can peek, and settlement clears in under a second.**

---

## The on-chain / off-chain split

Hybrid is **not** a workaround. It is how production systems are built. Sponsors test for this.

| Put ON-chain | Keep OFF-chain |
|---|---|
| Agreement, ordering, settlement | **Private data** (messages, records — visibility is the harm) |
| Ownership and permission grants | **Large files** (the hash goes on-chain; the bytes go to storage) |
| Anything needing composability | **Ultra-high-frequency events** (sensor feeds at 100k/s) |
| Anything needing permanence | **Heavy compute** (transcoding, inference) |
| Anything needing public verifiability | Anything where a **trusted operator is genuinely fine** |

**⚠️ The "data privacy" trap:** it does **not** mean putting private data on-chain — Monad's own
material explicitly says private data stays off. It means the **access-control grants** go on-chain
while the **encrypted data** stays off. Getting this backwards fails the sponsor's own stated test.

**Always write a "What we kept off-chain, and why" section.** Almost nobody does, and it is exactly
the judgment being tested.

---

## Cadence (the consensus protocol)

Monad's BFT consensus. Two jobs woven into one message flow: **agree on order** *and*
**reveal transactions only as that agreement forms.**

### The math (derive, never hardcode)
```
f       = floor((N - 1) / 3)     max Byzantine validators tolerated (~33%)
Quorum  = N - f  =  2f + 1       matching votes to finalize (any two quorums share an honest node)
Rebuild = f + 1                  chunks to reconstruct a proposal; key shares to decrypt

N = 10  →  f = 3,  Quorum = 7,  Rebuild = 4
```

### One slot
1. **Propose** — 3 rotating proposers each bundle encrypted txs from the encrypted mempool, hash to a
   Merkle-root id, erasure-code into N chunks, send one chunk per validator.
2. **First Vote** — after the deadline, each validator votes once *per proposer*: yes if the chunk
   arrived in time and verifies against the id. The vote attests **availability + integrity only** —
   *not* transaction contents, which are still encrypted. **Each vote carries the voter's key share.**
3. **Decrypt** — once **f+1 = 4 distinct key shares** land, the key reconstructs and proposals decrypt.
   *Decryption (4) happens before quorum (7). Different thresholds.*
4. **Commit Vote** — once every proposer is decided (**speculative finality**), validators broadcast a
   commit vote. **2f+1 = 7 matching** commit votes → **final**.
5. **Block** — merge included proposals, drop duplicates, append in slot order.

### Why the key shares ride on votes
If one validator held the whole decryption key, it could decrypt early and front-run everyone.
**Threshold encryption** splits it N ways via a one-time DKG; no one ever holds the whole key. Shares
are released *attached to votes* — so **transactions become readable exactly when their order becomes
irreversible, never before.** That single design choice is the anti-MEV guarantee.

### Chorus vs Conductor
- **Chorus** = the slot itself (propose → vote → commit → block)
- **Conductor** = the scheduler; opens a new slot every `tau` **whether or not the previous one
  finished**. Many slots run concurrently — *"extreme pipelining."* This is where the throughput comes
  from.

Full protocol reference, including the simulator build: `references/cadence.md`

---

## Hackathon guidance (BuildAnything / Spark)

**What judges are scoring** — from Monad's own words: *"The chain keeping up isn't a feature you think
about once you're building. It's the absence of a constraint you would otherwise be designing around.
That absence is the point."*

They are asking for **composable primitives, not apps.** Count how often their material says
*"other contracts can plug into it"*, *"a new building block the EVM didn't have"*, *"any app can read
and build on"*, *"composes with the rest of the EVM."*

### Do
- Ship a **primitive + an SDK/consumer contract** that proves other contracts can build on it
- **Deploy the contract on day one.** Put the address and an explorer link in the submission
- Make the proof **visible**: a live **latency counter** in ms; or a **sealed-bid auction where the
  demo shows bids are unreadable pre-finality**; or **two independent frontends reading the same
  on-chain graph**
- Add a **guardrail** if it touches money or autonomy (spend cap, kill switch, human approval)
- Lead with an **adoption-friction number**: *"one line turns any endpoint into a paid endpoint"*
- Write the **"What we kept off-chain, and why"** section
- Name it like a **company** (Arcana, Credence, Recon, Helm) — never `MonadPay` or `AI-DeFi Optimizer`

### Don't
- Don't build a plain **perps/order-book DEX** — the most crowded idea in the event.
  *(Unless it's the sandwich-proof version — that's a different project.)*
- Don't build **"an AI trading agent."** Build the **rail agents pay on**. In the only comparable
  agent-payments hackathon, **0 of 5 winners built an agent**; all five built what agents *pay*.
- Don't put private data, large files, or heavy compute on-chain — it fails their own stated test
- Don't write a **manifesto**. The trustlessness categories attract 1,000-word pitch essays with zero
  deployed contracts. **Deploy first, write last.**

---

## Chain gotchas that differ from Ethereum

### ⚠️ Gas is charged on `gas_limit`, NOT gas used
On Ethereum you overestimate the limit and get refunded the difference. **On Monad you pay for what
you asked for.** A sloppy gas limit costs your users real money on **every** transaction.

- **Estimate properly.** Do not pad the limit "to be safe" — padding is now a direct user cost.
- **Display honestly** in the frontend: show the real expected cost, not the limit.
- Judges from the Monad team will notice this. Getting it right is a cheap, visible signal that you
  read the docs; getting it wrong signals you didn't.

**Base fee controller:** rises slowly, falls quickly (the inverse of Ethereum's symmetry).

**Opcode pricing:** **cold state access is 3–4× more expensive**; **precompiles are 2–5× more
expensive**. Design for warm access; batch reads.

### Other differences worth knowing
- **Contract size limit: 128 KB** (vs Ethereum's 24 KB). You can ship far bigger contracts.
- **`eth_sendRawTransactionSync`** — send and get the receipt in one round trip. With 400ms blocks
  this collapses submit-then-poll into a single call. Use it; it's a Monad-specific UX win.
- **Async / parallel execution** — execution is decoupled from consensus. Understand **block states**
  (proposed / voted / finalized) before you read state in a frontend.
- **Reserve balance** and **EIP-7702** are supported — relevant for account-abstraction flows.
- **Never hallucinate a contract address.** Wrong address = lost funds. Verify code exists at the
  address on the target network before using it.
- **Verify your contracts** via the verification API after deploying. An unverified contract is a
  judge who can't read your code.

---

## Quick reference

```
f = floor((N-1)/3)          Quorum = N - f = 2f+1          Rebuild = f + 1
400ms blocks · 800ms deterministic finality · 10,000 TPS · full EVM · encrypted mempool
Perception: <100ms instant | 100ms-1s responsive | >1s noticed | >10s abandoned
```

**The one question:** *would this break at 12-second blocks with a public mempool?*
If not, rescope.
