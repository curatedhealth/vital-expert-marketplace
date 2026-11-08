# Good example: confidence card (offline counts)

Statuses from a manual check (not tool-checked): supported 2, partial 1, unsupported 1, contradicted 0, unverifiable 0, out_of_scope 1.

```text
┌─ Confidence ───────────────────────────────────────
│ Faithfulness:  no figure — not tool-checked (method counts only)
│ Counts:        supported 2 · partial 1 · unsupported 1 · contradicted 0 · unverifiable 0 · out_of_scope 1 · not_checked 0
│ Formula:       would be (2+0.5×1)/(2+1+1+0+0)=62.5% → 63% IF these were tool-returned
│ Source scores: listed on source cards — not averaged here
│ What this is:  passage overlap, not world-truth (RAGAS-style)
│ What to do:    rewrite the unsupported claim; keep out_of_scope out of %
│ Label:         not tool-checked
└────────────────────────────────────────────────────
```

Stamp: `TRUSTED / confidence-scoring: not tool-checked (offline tools) · counts only · no %`
