# Confidence card (render this shape)

```text
┌─ Confidence ───────────────────────────────────────
│ Faithfulness:  <N%>   or  "no figure — not tool-checked / all not_checked"
│ Counts:        supported S · partial P · unsupported U · contradicted C · unverifiable V · out_of_scope O · not_checked N
│ Formula:       (S + 0.5×P) / (S+P+U+C+V)   — O and N out of denominator
│ Source scores: listed separately below — never averaged into faithfulness
│ What this is:  overlap with supplied passages (RAGAS-style), not world-truth
│ What to do:    open gaps → rewrite/remove → human MLR / medical review if external
│ Label:         tool-checked | not tool-checked
└────────────────────────────────────────────────────
```

## Grounding

- RAGAS Faithfulness: supported claims / total claims against retrieved context — https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/faithfulness/ (accessed 8 Nov 2026).
- TRUSTED adds **partial** (0.5) and excludes **out_of_scope** / **not_checked** from the denominator (operator overlay on binary NLI).
