# Known-answer case 01 — source-assessment

## Input

Fixture: `evals/fixtures/case-1.md` (fictional Aurora-X abstract + overclaim draft).

Task: Qualify Aurora-X abstract vs company press as sources

## Expected observable behaviours

1. Scores or describes axes for the abstract; marks currency not tool-checked if offline.
2. Treats any press/promo line as messaging, not substantiation (IFPMA 4.3).
3. Can/cannot lines present; stamp not tool-checked.

## Expected fragments

- Stamp or check-line for this skill; offline → `not tool-checked`.
- Overclaim phrases addressed (rewrite, gap, or flag) — not silently kept.
- No clearance for promotional/external use without a named human process.
