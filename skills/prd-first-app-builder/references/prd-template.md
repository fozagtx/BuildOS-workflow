# PRD Template

## Product

What the product does and for whom.

## Non-Negotiables

- PRD before implementation.
- Route permissions before pages.
- No fake demo states.
- Component system defined before UI build.

## Users And Roles

| Role | Description | Can | Cannot |
| --- | --- | --- | --- |
| Visitor | Not authenticated/connected | | |
| Connected User | Authenticated/connected | | |
| Admin/Operator | Operational role, if any | | |

## Route Map And Permissions

| Route | Purpose | Visitor | Connected User | Admin/Operator | Notes |
| --- | --- | --- | --- | --- | --- |
| `/` | Public overview | Allowed | Allowed | Allowed | No protected actions. |

## Page Requirements

For each page:

- purpose
- visible data
- allowed actions
- blocked actions
- empty state
- error state
- loading state

## UI System

- Component library:
- Icons:
- Navigation:
- Forms:
- Tables/lists:
- Toasts/errors:
- Visual restrictions:

## No Fake Demo Rules

Allowed only when labeled:

- mocks
- local fixtures
- simulations

Never allowed:

- fake success
- fake tx hashes/explorer links
- fake balances
- hardcoded production-looking data

## Acceptance Criteria

- Route gates work.
- Unauthorized users cannot access protected actions.
- Fake/simulated data is labeled.
- Build/typecheck pass.
