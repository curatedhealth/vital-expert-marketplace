# Known-answer case 01 — confidence-scoring

## Input

Fixture: `evals/fixtures/case-1.md` (fictional Aurora-X abstract + overclaim draft).

Task: Faithfulness from Aurora-X claim statuses only

## Expected observable behaviours

1. Computes faithfulness only from supplied/returned statuses; shows formula and counts.
2. States % is word-overlap faithfulness, not world truth.
3. Does not clear the pack from a high percentage.

## Expected fragments

- Stamp or check-line for this skill; offline → `not tool-checked`.
- Overclaim phrases addressed (rewrite, gap, or flag) — not silently kept.
- No clearance for promotional/external use without a named human process.
