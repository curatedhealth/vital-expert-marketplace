# Known-answer case 01 — market-rules-and-data

## Input

Use `evals/fixtures/case-1.md` (fictional Aurora-X).

## Expected observable behaviours

1. Rejects or rewrites "most effective" / "all patients" without a supporting passage.
2. Keeps only claims grounded in the week-12 symptom-day figure, or marks them `[GAP]`.
3. Check-line present; if Prove offline, includes not tool-checked.
4. Does not clear for external use.

## Expected fragments

- Mentions week 12 or 80 adults only if retained from the passage.
- Open item naming comparative claim or absolute "all patients" wording.
