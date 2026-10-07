---
name: gomobile-flutter-backend
description: "Architect and implement Flutter + Go Mobile apps with protobuf platform channels, Go↔native interfaces, async callbacks, and desktop daemon backends. Use when the user mentions gomobile, Go Mobile, Flutter Go backend, Flutter platform channels with Go, protobuf mobile IPC, Digital Carrot-style Go business logic, or shared Go logic across iOS/Android/desktop. Works via npx openskills read gomobile-flutter-backend in any harness."
---

# Flutter + Go Mobile Backend

Battle-tested pattern: **Flutter owns UI**, **Go owns business logic**, bridged
by protobuf over platform channels (mobile) or gRPC/sockets (desktop). Prefer
this when the team is strong in Go, needs shared server/client logic, or wants
Go libraries (Expr, Goja, etc.) that mobile stacks lack.

Source: [One Year of Go Mobile](https://www.davidsobsessions.com/p/one-year-of-gomobile/) (David’s Obsessions / Digital Carrot).

## Architecture

```
Flutter UI
  -- protobuf binary -->  Swift / Kotlin (platform channels)
  -- forward bytes ---->  Go Mobile backend
  <-- protobuf response -

Go --> native APIs via Go interfaces implemented in Swift/Kotlin
      (Screen Time, Health, permissions, etc.)
```

Desktop variant: same Go API as a **background daemon**; UI talks gRPC over
sockets/pipes. Keeps RAM low when UI is not needed (~30–60MB for daemon-only).

## When this stack fits

- Team already lives in Go, or server is Go and you want `go test` sync/client reuse
- Heavy shared business logic + thin native/Flutter UI
- Need Go-only libs (Expr, Goja, networking) on device
- Want to swap UI later (SwiftUI/Kotlin/Compose) without rewriting domain

## When to avoid full Go business logic

- Games / ultra-low-latency UI loops (protobuf round-trips cost ms)
- Tiny apps where binary size (~50MB+ Go backend) dominates
- Team unwilling to maintain Dart + Go + protobuf + native glue

Prefer: put **Go where Go wins**, leave the rest in Dart/Swift/Kotlin.

## Flutter → Go: single protobuf API channel

Do **not** invent a new platform channel per function. Use one call that carries
a large `oneof`:

```protobuf
message AppAPI {
  oneof api {
    Function1API function1 = 10;
    Function2API function2 = 11;
  }
}

message Function1API {
  message Request {}
  message Response {}
  Request request = 1;
  Response response = 2;
}
```

Flow:

1. Flutter fills `request`, wraps in `AppAPI`, sends bytes
2. Native forwards opaque binary to Go
3. Go switches on `api`, fills `response`, returns bytes
4. Flutter decodes typed response

Platform channels only carry primitives (string/bytes/bool) — protobuf is the
marshalling layer. Define messages once; generate Dart + Go stubs.

## Go → Swift/Kotlin: interfaces injected at startup

Undocumented-feeling but required pattern:

1. Define a Go interface with **primitive** args/returns (or `[]byte`):

```go
type IosMethods interface {
    SetShields([]byte) bool
    HasScreentimePermissions() bool
}
```

2. `gomobile bind` generates ObjC/Kotlin protocols
3. Implement in Swift/Kotlin
4. Pass the implementation into Go when constructing the mobile API entrypoint

```swift
self.carrotApi = MobileNewAppleMobileAPI(GoScreentime())
```

Use protobuf/`[]byte` for richer payloads if native→Go call volume grows.

## Async footgun (App Review critical)

Flutter platform channel calls are **not async by default**. A slow Go call
blocks the UI thread (reviewers notice freezes).

**Required pattern:**

- Every non-trivial Go call: hand off to a goroutine
- Return immediately from the channel handler
- Deliver result via callback / completion channel back to Flutter
- Never do network or heavy sync work on the Flutter main isolate via a sync channel invoke

## Go → Flutter notifications

Reliable push from Go→Flutter is awkward. Pragmatic fallback used in production:

- Flutter polls Go for state changes on a short interval (~1s)
- Acceptable for sync/status; not elegant, but cheap and stable

Prefer designing APIs so UI can poll/diff cheaply rather than depending on
fragile event bridges unless you have a proven one.

## Known Go Mobile landmines

| Issue | Fix |
|---|---|
| Local time stuck at GMT | Pass timezone from Swift/Kotlin into Go |
| DNS broken on real iOS devices (works in simulator) | Link `libresolv` in Xcode |
| Large binary | Budget ~50MB+ uncompressed for Go backend; accept or split packages |

## Testing advantages to preserve

- Import client Go packages into server tests — `go test`, no Docker harness
- Business logic tests without spinning Flutter UI
- Replay testing: capture UI→API protobuf calls, replay in Go tests
- Keep UI tests thin; assume domain is covered in Go

## Desktop / multi-protocol benefit

If the API is protobuf/gRPC-shaped:

- Mobile: in-process via gomobile
- Desktop: daemon over sockets/pipes
- Future: point UI (or an AI agent) at the same network API

## Implementation checklist

When scaffolding or reviewing:

- [ ] One protobuf `oneof` API surface (not N platform channels)
- [ ] Generated stubs for Dart + Go checked into/buildable from CI
- [ ] Native interface injection for platform APIs
- [ ] All channel invokes async off main thread
- [ ] iOS: `libresolv` linked; timezone passed in
- [ ] Clear boundary: Flutter = UI/permissions; Go = domain/sync/storage
- [ ] Size/perf tradeoffs documented for stakeholders

## Response style

When advising:

1. Confirm fit (Go-heavy team / shared server logic) vs partial Go extract.
2. Default to single protobuf channel + injected native interfaces.
3. Call out async + DNS + timezone landmines early.
4. Prefer concrete scaffolding steps over theory.
