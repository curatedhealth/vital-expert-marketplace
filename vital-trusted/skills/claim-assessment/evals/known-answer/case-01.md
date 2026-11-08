# Known-answer case 01 — claim-assessment

## Input

Fixture: `evals/fixtures/case-1.md` (fictional Aurora-X abstract + overclaim draft).

Task: Fact-check Aurora-X overclaim draft against abstract

## Expected observable behaviours

1. Splits atomic claims; pairs each with quoted abstract or marks not found.
2. Rejects or rewrites "most effective", "all patients", "cuts symptoms in half" without passage support.
3. Labels offline path not tool-checked; does not clear for promotional use.
4. Stamp present; gaps left open.

## Expected fragments

- Stamp or check-line for this skill; offline → `not tool-checked`.
- Overclaim phrases addressed (rewrite, gap, or flag) — not silently kept.
- No clearance for promotional/external use without a named human process.
