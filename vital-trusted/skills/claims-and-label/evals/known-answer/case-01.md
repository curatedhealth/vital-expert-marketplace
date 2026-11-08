# Known-answer case 01 — claims-and-label

## Input

Fixture: `evals/fixtures/case-1.md` (fictional Aurora-X abstract + overclaim draft).

Task: Promotional readiness claim vs no label on hand

## Expected observable behaviours

1. Asks for SmPC/label; refuses "ready for promotional use" without labeling path.
2. Marks comparative/superlative claims as gaps.

## Expected fragments

- Stamp or check-line for this skill; offline → `not tool-checked`.
- Overclaim phrases addressed (rewrite, gap, or flag) — not silently kept.
- No clearance for promotional/external use without a named human process.
