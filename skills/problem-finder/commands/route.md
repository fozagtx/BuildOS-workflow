# /route

Classify the live prompt and load only the files that path needs.

## Inputs

- Original prompt
- Whether a discovery report already exists
- Whether the user asked about the skill itself or asked to apply it

## Steps

1. Read `skill/router.md`.
2. Match one ID (R0–R7). If two match, take the earlier ID.
3. Read only the files that ID names.
4. On apply paths (R5, R7): classify obvious vs non-obvious before any solution.
5. Do not emit a product, stack, or feature list until a report exists.

## Output

- Matched route ID
- Files read
- Obvious / non-obvious / suspect / no-run
- Next module, or the report
