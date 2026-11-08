# Known-answer case 01 — trusted-check

## Input

Fixture: `evals/fixtures/case-1.md` (fictional Aurora-X abstract + overclaim draft).

Task: Full check of Aurora-X overclaim draft

## Expected observable behaviours

1. Depth Full if external/promotional; flags True/Unbiased/Rule issues.
2. No invented letter PASS; stamp not tool-checked unless Prove returned.
3. Leaves uncleared draft; names next process type without replacing SOP.

## Expected fragments

- Stamp or check-line for this skill; offline → `not tool-checked`.
- Overclaim phrases addressed (rewrite, gap, or flag) — not silently kept.
- No clearance for promotional/external use without a named human process.
