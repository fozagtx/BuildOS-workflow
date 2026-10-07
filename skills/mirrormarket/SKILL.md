---
name: mirrormarket
description: Query the MirrorMarket Prediction Market Intelligence API to compare Polymarket vs Kalshi pricing, find arbitrage opportunities between the two venues, and inspect calibration / longshot-bias stats per platform. Use whenever the user asks about prediction markets, Polymarket, Kalshi, arbitrage between betting venues, market calibration, or "where do these two platforms disagree."
---

# MirrorMarket — Prediction Market Intelligence

Base URL: `https://mirrorcheck.hub.zerve.cloud`

A read-only HTTP API that pulls live snapshots from Polymarket and Kalshi, matches semantically similar markets across both venues, and exposes calibration and arbitrage views. Cache TTL is 300s — repeated calls within 5 minutes return cached data.

## Endpoints

| Path | Returns | Use for |
|---|---|---|
| `GET /` | service status, counts, cache timestamp | health check, "is the API up?" |
| `GET /markets/polymarket` | array of Polymarket markets | listing PM markets, finding a specific question, volume sorting |
| `GET /markets/kalshi` | array of Kalshi markets (~20k) | listing Kalshi markets — large response, filter client-side |
| `GET /arbitrage` | top spread opportunities between matched pairs | "where do PM and Kalshi disagree?", finding mispricings |
| `GET /calibration` | distribution + FLB index per platform | comparing how each venue prices average vs. extreme events |
| `POST /refresh` | force cache rebuild | only when user explicitly wants fresh data |

## Market object fields

**Polymarket:** `market_id, question, yes_prob, volume_24h, liquidity, close_time, platform`
**Kalshi:** `ticker, question, yes_prob, volume_24h, close_time, platform` (no `liquidity` field)

## Arbitrage opportunity fields

```
polymarket_question, kalshi_question, similarity (0-1),
pm_yes_prob, kalshi_yes_prob, spread,
pm_volume_24h, kalshi_volume_24h,
arbitrage_flag, higher_pm
```

## Calibration fields (per platform)

```
n_markets, mean_yes_prob, median_yes_prob, skewness,
flb_index (>1 = longshot bias),
pct_below_10pct, pct_40_60pct, pct_above_90pct,
distribution_bins (10-bucket histogram)
```

## How to use this skill

1. **Pick the right endpoint** — don't pull all 20k Kalshi markets if you only need a stat; use `/calibration` or `/arbitrage` instead.
2. **Use curl via Bash** for raw JSON, or WebFetch when you want a summarized natural-language answer.
3. **Respect the cache** — back-to-back calls within 5 min return identical data; don't loop.
4. **Trust similarity scores cautiously.** The matcher returns pairs as low as 0.55 similarity, and many of those pair semantically unrelated questions (e.g. "Will USA win World Cup" vs "Iran to compete in World Cup"). For a real arbitrage signal, filter to `similarity >= 0.85` AND `kalshi_volume_24h > 0` AND `pm_volume_24h > 0`.
5. **`higher_pm: true`** means Polymarket's YES is priced higher than Kalshi's. Flip the trade direction accordingly.
6. **Results are NOT financial advice.** The API itself returns this disclaimer — propagate it when surfacing arbitrage rows to the user.

## Example calls

```bash
# Health check
curl -s https://mirrorcheck.hub.zerve.cloud/ | jq

# Top 10 highest-spread arbitrage with both sides liquid
curl -s https://mirrorcheck.hub.zerve.cloud/arbitrage \
  | jq '[.opportunities[] | select(.similarity >= 0.85 and .kalshi_volume_24h > 0 and .pm_volume_24h > 0)] | .[0:10]'

# Calibration comparison
curl -s https://mirrorcheck.hub.zerve.cloud/calibration | jq '.platforms[] | {platform, flb_index, median_yes_prob}'

# Top 5 PM markets by 24h volume
curl -s https://mirrorcheck.hub.zerve.cloud/markets/polymarket \
  | jq '[.[] | {question, yes_prob, volume_24h}] | sort_by(-.volume_24h) | .[0:5]'

# Find a specific Kalshi market by keyword
curl -s https://mirrorcheck.hub.zerve.cloud/markets/kalshi \
  | jq '.[] | select(.question | test("Bitcoin"; "i"))'
```

## Common questions this skill can answer

- "Which platform has stronger longshot bias right now?" → `/calibration`, compare `flb_index`
- "Where are the biggest disagreements between PM and Kalshi?" → `/arbitrage`, sort by `spread`
- "Top markets by volume on Polymarket today" → `/markets/polymarket`, sort `volume_24h` desc
- "Is there real tradeable arb between the two?" → `/arbitrage` filtered for similarity ≥ 0.85 and both volumes > 0
- "How many Kalshi markets are priced near 50/50?" → `/calibration`, read `pct_40_60pct`

## Known limitations

- Snapshot-only: no historical time series, no order-book depth, no resolution outcomes.
- Matching is fuzzy: low-similarity pairs are unreliable — always show the similarity score to the user.
- Counts at `/` may differ from endpoint counts by 1 due to cache refresh races (cosmetic).
