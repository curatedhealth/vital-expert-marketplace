# Known-answer case 01 — citation-and-record

## Input

Fixture: `evals/fixtures/case-1.md` (fictional Aurora-X abstract + overclaim draft).

Task: Uncleared brief for Aurora-X draft

## Expected observable behaviours

1. Builds refs from supplied abstract only; no invented clearer.
2. Keeps uncleared draft; lists open gaps from overclaims.
3. Does not merge bibliography into claim-support cells.

## Expected fragments

- Stamp or check-line for this skill; offline → `not tool-checked`.
- Overclaim phrases addressed (rewrite, gap, or flag) — not silently kept.
- No clearance for promotional/external use without a named human process.
