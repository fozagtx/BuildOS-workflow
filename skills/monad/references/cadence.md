# Cadence — Protocol Reference

Monad's BFT consensus protocol (from Category Labs). Byzantine-fault-tolerant: correct as long as
**no more than ~33% of validators misbehave**.

Cadence solves **two problems in one message flow**:
1. **Consensus** — agree which proposals go in the block
2. **Anti-MEV** — reveal transactions only *as* that agreement forms

The elegance is that both jobs ride on the same messages. **A vote is simultaneously *"I include this
proposal"* and *"here's my piece of the decryption key."***

---

## Vocabulary

| Term | Meaning |
|---|---|
| **Validator** | A node participating in consensus. N of them. |
| **Proposer** | A validator proposing this slot. **Cadence picks 3, not 1.** They rotate by one each slot. Each submits its own tx list; the block merges all of them. |
| **Slot** | One round of the protocol. Produces at most one block. |
| **Deadline** | Validators have **synchronized clocks**. The moment by which a slot's proposals must arrive. |
| **Quorum** | Minimum matching votes to finalize: **more than two-thirds** of validators. |
| **f** | Max tolerated Byzantine validators. |
| **Rebuild** | Chunks needed to reconstruct a proposal — and key shares needed to decrypt. |
| **Chunk** | One erasure-coded slice of a proposal, one per validator, carrying the proposal id. |
| **Merkle root / id** | A proposal's fingerprint. Lets a validator verify its chunk belongs to that proposal, unaltered. |
| **Key piece** | One validator's share of the decryption key, released **by attaching it to a vote**. |
| **Speculative finality** | Every proposer decided. Confident, but not yet committed. |
| **Finality** | Irreversible. The block is produced. |
| **tau** | The block interval / propose-to-deadline window. |

---

## The thresholds — derive, never hardcode

```
f       = floor((N - 1) / 3)
Quorum  = N - f  =  2f + 1
Rebuild = f + 1
```

| N | f | Quorum | Rebuild |
|---|---|---|---|
| 4 | 1 | 3 | 2 |
| 7 | 2 | 5 | 3 |
| **10** | **3** | **7** | **4** |
| 22 | 7 | 15 | 8 |

**Why Quorum = 2f+1 gives safety:** any two quorums of that size **must overlap in at least one honest
validator**. That overlapping honest node cannot vote two ways, so two conflicting blocks can never
both finalize.

**Why Rebuild = f+1:** a proposal splits into N chunks. Any f+1 reconstruct it. Since at most f
validators are faulty, **at least one honest chunk is always present** in any f+1 you collect.

**The two thresholds are different and that matters:** decryption needs **f+1 = 4**;
finalization needs **2f+1 = 7**. Decryption happens *first*.

---

## Threshold encryption (the anti-MEV core)

**The problem.** Transactions sitting in a public mempool are readable. Anyone can front-run trades,
sandwich swaps, or reorder for profit.

**The naive fix and why it fails.** One decryption key → whoever holds it holds *all* the MEV power.
They could decrypt early, peek at what's coming, and front-run everyone.

**The real fix.** The key is split into **N shares** — one per validator — in a one-time
**Distributed Key Generation (DKG)** ceremony. **No one ever holds the whole key.** Any **f+1** shares
reconstruct it; fewer cannot.

**The clever part — shares ride on votes.** A validator does not release its share whenever it likes.
It **attaches the share to its vote**. So shares only become available *as validators vote* — meaning:

> **Transactions become readable exactly when their order becomes irreversible. Never before.**

Consensus runs **blind**. You cannot front-run what you cannot read.

---

## One slot, step by step

**Setup:** N validators. **3 are proposers** this slot; they rotate by one each slot
(`proposersForSlot(slot, n)` → slot 1 = `[0,1,2]`, slot 2 = `[1,2,3]`, wrapping mod N).

### 1. Propose
Each proposer:
- Bundles encrypted transactions from the **encrypted mempool**
- Hashes them into a **Merkle-root id** (the proposal's fingerprint)
- **Erasure-codes** the proposal into N chunks
- Sends **each validator one chunk**

Each validator verifies its chunk against the id — proving integrity **without reading the contents**.
No single sender is a bottleneck, and any f+1 chunks rebuild the whole proposal.

### 2. First Vote
When the **deadline** passes, every validator casts **one vote per proposer**:
- **yes** — if that proposer's chunk arrived before the deadline and verifies against the id
- **no** — otherwise

**What a first vote attests:** *availability* ("I saw it in time") and *integrity* ("the chunk verifies").
**It is NOT a check of transaction contents** — those are still encrypted.

**Every vote carries the voter's key piece.**

### 3. Decrypt
Once **f+1 (= 4 at N=10) distinct key pieces** have arrived, the decryption key reconstructs and the
proposals decrypt. Transaction ids are revealed.

> **Decryption (4 pieces) happens BEFORE quorum (7 votes). Different thresholds.**

### 4. Commit Vote → Finality
- **Speculative finality**: every proposer is decided (quorum-yes = *included*, or
  can't-reach-quorum = *out*). A validator is confident, not committed.
- Each validator then broadcasts a **commit vote** carrying a digest of its recorded result.
- **2f+1 (= 7) matching commit votes → the slot is FINAL.** Irreversible.

### 5. The block
Merge the transactions of all **included** proposals, drop duplicates, skip the **OUT** ones. Append
to the chain **in slot order**. Rotate proposers. Next slot.

---

## Chorus vs Conductor

- **Chorus** = steps 2–5. One slot: propose → first vote → commit vote → block.
- **Conductor** = the scheduler. It **opens a new slot every `tau`, whether or not the previous slot
  has finished.** Several slots run at once.

This is **extreme pipelining**, and it is where the throughput comes from. Finalization can take
*longer* than `tau` while blocks still land *every* `tau`.

**Back-pressure (the brake):** the Conductor stops scheduling when too many slots are unfinalized
(e.g. bounded at 10 in flight). When blocked it **stalls**; on resume it schedules *from now* rather
than catching up — which leaves a visible **gap** in the deadline schedule.

---

## Failure modes

**Faulty proposer.** A proposer goes silent; its proposal is never sent, so that slot cannot finalize
normally. After the deadline plus a timeout (~2× tau), validators give up and finalize it as an
**empty SKIPPED block**. Meanwhile later slots keep finalizing — their blocks sit **pending**
("waiting for slot X") until the skipped block lands and the chain drains in a burst.

**Outage.** No messages deliver; they queue. But **the clock keeps advancing** — wall time passes even
while messages sit queued. Slots still pass their deadlines, and the Conductor still schedules up to
the brake cap. On recovery: a burst of blocks, one visible gap, then the steady beat resumes.

---

## Building a simulator

Monad's own lesson has you vibecode a browser simulator. The shape:

**Data model**
```ts
Validator  { id, inbox: [] }
Proposal   { proposerId, txIds[], id /* 4-hex Merkle root */, locked: boolean }
Chunk      { proposerId, chunkIndex, id }
Vote       { type: "yes" | "no", id?, chunk?, keyPiece /* = voter id */ }
Message    { from, to, type, payload, sentAt, arrivesAt, slot }
SlotState  { slot, proposers, deadlineAt, proposals, votes, commitVotes,
             speculativeAt, finalAt, proposed, firstVoted, committed }
SimState   { clock, tau, autoRun, outage, validators, slots[], chain,
             pending, nextChainSlot, inFlight, log, nextSlotNumber, nextProposeAt }
```

**Build order** (each step must work before the next):
1. Scaffold + validators slider (N: 4–22). **Derive f / Quorum / Rebuild from N — never hardcode.**
2. Simulated network + clock. Delivery latency **60 ms ± 30 ms** (so [30, 90]). Ticker advances the
   clock and delivers messages whose `arrivesAt <= clock`.
3. **Propose** — 3 proposers, encrypted bundles, Merkle id, N chunks, deadline `clock + tau` (150 ms).
4. **First Vote** — one vote per proposer; key pieces attached; decrypt at **f+1** distinct pieces.
5. **Commit Vote** — speculative finality → commit round → **2f+1 matching** → block.
6. **Concurrency** — per-slot state; the **Conductor** opens a slot every `tau` without waiting.
7. **Ordered chain + brake + faulty proposer + outage.**

**Gotchas**
- Keep the reducer **pure** through step 5 (roll randomness in action creators). Move randomness into
  the tick only at step 6 — and then **disable React StrictMode** (`reactStrictMode: false`) so its
  double-invoke doesn't double-roll.
- Base each slot's tally on **one representative "observer" validator's inbox**, so quorum forms after
  a real network round rather than an artificially fast global first-arrival.
- **Speculative finality = all first votes delivered to the observer.** This correctly makes
  finalization take *longer* than one tau.
- Chunks all arrive before a 150 ms deadline (delivery ≤ 90 ms), so tallies should reach yes N / no 0.
- Append blocks in **slot order** even when finalization is out of order — hold out-of-order blocks in
  `pending`, render them dimmed, drain when the gap fills.

**Expected behavior**
- `tau = 150` → a block every ~150 ms; in-flight hovers at 1–2
- `tau = 50` → a block every ~50 ms (**faster than one 60 ms delivery** — that's the pipelining)
- Faulty proposer → one slot skipped, a few dimmed pending blocks, then a drain burst
- Outage → in-flight climbs and **stops at the brake cap**, then a burst + one visible gap on recovery

---

## Simulator vs production

| | Simulator | Production Cadence |
|---|---|---|
| Crypto | `locked` flag, `keyPiece` = validator id, fake 4-char hash | **Real BLS signatures, real DKG, real threshold encryption, real erasure coding with Merkle proofs per chunk** |
| Network | Random-latency delivery model | Real p2p gossip, real partitions, real adversaries |
| Pipeline | Optional Auto-Run | Full concurrent scheduler with back-pressure |
| Transactions | Tiny fake tx ids encrypted directly | A symmetric key encrypted inside the threshold ciphertext, used to lock full tx bytes |
| Adversaries | Everyone assumed honest | Equivocation and invalid shares are **detected and slashed** |

**What is identical:** the protocol logic. Proposers, quorum-based finality,
**encrypted-then-decrypt-on-vote**, ordered chain assembly. *Only the cryptography is faked — the
reveal-after-f+1 rule is exactly the real thing.*

---

## What this means for what you build

The encrypted mempool is not a footnote — it is a **product primitive**, and it is the least-exploited
thing about Monad.

**Applications that are impossible with a public mempool** (and therefore impossible on essentially
every other chain), which Cadence gives you **free at the consensus layer** — no commit-reveal, no ZK
circuit:

- **Sealed-bid auctions** (first-price, Vickrey)
- **Hidden-information games** — poker, Battleship, fog-of-war
- **Order books that cannot be sandwiched**
- **Fair mints / launches** — no sniping, no gas wars
- **Prediction markets** where the oracle update can't be front-run
- **On-chain RFQ / matching** without the MEV tax
- **Blind voting** with no separate reveal phase

For any of these, the Load-Bearing Test answers itself in one sentence:
**"This cannot exist on a chain where the mempool is readable."**
