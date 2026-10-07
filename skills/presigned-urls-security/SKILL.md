---
name: presigned-urls-security
description: "Design, review, and implement S3/Tigris/SigV4 presigned URLs as intentional capability grants with correct expiry, scope, and revocation tradeoffs. Use when the user mentions presigned URLs, signed URLs, X-Amz-Signature, SigV4 object storage auth, temporary download/upload links, hotlink protection, or object-storage access control without sharing long-lived credentials. Works via npx openskills read presigned-urls-security in any harness."
---

# Presigned URLs Security

Presigned URLs are a **replay attack done on purpose**: auth is flattened into
URL query params so any HTTP client can exercise one scoped capability until
the clock says no. Treat them as **capability grants**, not as a general ACL.

Source framing: [Tigris — Presigned URLs are technically a security vuln](https://www.tigrisdata.com/blog/presigned-urls-security-vuln/).

## Mental model

| Normal SigV4 | Presigned URL |
|---|---|
| Secret never leaves client; HMAC over canonical request | Same math, params live in the URL |
| ~15 min clock skew window limits replay | Expiry is chosen (`X-Amz-Expires`, 1s–7d) |
| Headers carry auth | Query string carries auth |
| Hard to share safely | Designed to share (browser, curl, chat) |

**Possession is authorization until expiry.** The signature binds method + path
+ signed headers (+ payload hash when included). A GET grant cannot be mutated
into a DELETE on another object.

## When to use

- Temporary download/upload without giving users access keys
- Browser/mobile clients that cannot hold secrets
- Time-boxed sharing (chat, email, tickets)
- Soft hotlink deterrence (links die; not a hard CDN ACL)

## When not to use (or use carefully)

- Need **per-URL revocation** without rotating the signing key
- Need **single-use** semantics (presigned URLs are replayable until expiry)
- Sensitive objects with long TTL where URL leak risk is high
- High-cost `GetObject` abuse (holders can replay forever until expiry)

## Design checklist

When implementing or reviewing:

1. **Scope tightly**
   - One method, one object key, one bucket
   - Prefer `SignedHeaders=host` only (clients cannot be forced to send exotic headers)
2. **Minimize TTL**
   - Prefer minutes/hours over days
   - Max is typically 7 days; shorter is safer for leak-prone channels
3. **Plan revocation**
   - Individual URLs cannot be revoked
   - Rotating/killing the access key kills **all** URLs signed by that key
   - For critical flows, use short TTL + dedicated signing key (or short-lived STS-style creds) so blast radius is small
4. **Assume leakage**
   - URLs land in logs, browser history, GitHub, chat, Referer headers
   - Design as if every URL will leak within its lifetime
5. **Account for replay cost**
   - No built-in use-count; budget for repeated GETs/PUTs
6. **Prefer HTTPS**
   - TLS protects the signature in transit; if TLS is broken, object storage is the least of your problems

## URL anatomy (SigV4 query form)

```
https://bucket.example/object
  ?X-Amz-Algorithm=AWS4-HMAC-SHA256
  &X-Amz-Credential=<accessKeyId>/<date>/<region>/<service>/aws4_request
  &X-Amz-Date=<YYYYMMDDThhmmssZ>
  &X-Amz-Expires=<seconds>
  &X-Amz-SignedHeaders=host
  &X-Amz-Signature=<hmac-sha256-hex>
```

| Param | Role |
|---|---|
| `X-Amz-Algorithm` | Almost always `AWS4-HMAC-SHA256` |
| `X-Amz-Credential` | Key ID + scope (date/region/service/`aws4_request`) — signing key is derived from these |
| `X-Amz-Date` | Birth time of the URL (UTC) |
| `X-Amz-Expires` | Lifetime in seconds |
| `X-Amz-SignedHeaders` | Headers folded into the signature (usually `host`) |
| `X-Amz-Signature` | HMAC over method, path, query params, signed headers, payload hash |

Changing any signed component invalidates the URL.

## Why clocks beat nonces (context for reviews)

Replay-proof auth usually wants a nonce store — expensive at scale (shared,
consistent “used once” state). SigV4 instead **signs the clock**: both sides
already agree on time (NTP/TLS). Old signatures become paperweights after the
skew/expiry window. Presigned URLs deliberately **lengthen** that replay
window into a product feature.

## Implementation guidance

When writing code:

1. Use the official AWS/S3-compatible SDK `presign` APIs — do not hand-roll SigV4 unless required.
2. Generate URLs server-side with credentials that never ship to clients.
3. Set method explicitly (`GetObject` vs `PutObject`); never reuse a GET URL pattern for uploads.
4. For uploads, constrain content type / content length via signed headers or conditions when the SDK/API supports it.
5. Log issuance metadata (object, TTL, purpose) — not full URLs if logs are broadly readable.
6. Document that expiry is soft protection, not access control theater.

## Review red flags

Flag these in PRs or designs:

- Presigned TTL of days/weeks for private/sensitive objects
- Signing with a long-lived root/admin key shared across many features
- Expecting “revoke this one link” without a key rotation story
- Treating presigned URLs as single-use
- Returning forever-valid “signed” links that are actually public ACL mistakes
- Client-side generation of presigned URLs with embedded secrets

## Response style

When advising:

1. State the capability-grant model in one sentence.
2. Recommend TTL + key isolation + leak assumptions.
3. Call out revocation and replay-cost limits explicitly.
4. Prefer concrete parameter choices over theory.
