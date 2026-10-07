# /check-edges

Run the edge-case table against a live prompt. Use when the input is a skip attempt, buyer-only persona, empty pain, bundle, implied solution, or after-report follow-up.

## Inputs

- Original prompt
- Whether a discovery report already exists
- Whether the user named a buyer, market, or demographic

## Steps

1. Match the prompt to an ID in `skill/edge-cases.md`.
2. Do the required behavior. Never do the forbidden one.
3. If a full run is still needed, load `skill/problem-workflow.md` and `skill/sharpen.md`.
4. Emit the six report headings, or the suspect variant.
5. No solution section.

## Output

- Matched edge-case IDs
- Required behavior taken
- Report or suspect report
