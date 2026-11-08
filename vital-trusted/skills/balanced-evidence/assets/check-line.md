# Output format: check line for trusted-check

Returned to `trusted-check` only, never shown at the end of a direct reply. One line per
task that ran, in plain words. Counts only; no verdict words (TR-H3, TR-H13). The shape
matches the proposal in `trusted-check/references/letter-lines.md`.

```
Unbiased · balance: <n> benefit statements, <n> risk or limitation statements, <n> benefits with no risk or limitation nearby (not tool-checked)
Unbiased · selective reporting: <n> studies, endpoints or time points in the material left out of the draft (not tool-checked)
```

Each line may carry up to three short plain notes after it, for the summary. Use them for
what the counts do not show:

```
  - <e.g. "side effects only in the footnote on slide 2">
  - <e.g. "'well tolerated' used without the figures">
  - <e.g. "discontinuations (9% vs 4%) not in the value story">
  - <e.g. "the second trial, which missed its primary endpoint, is not mentioned">
  - <e.g. "week 8 result shown; the planned week 24 result is not">
  - <e.g. "primary result appears after the secondary results">
```

If the task could not run:

```
Unbiased · balance: not checkable — no side-effect, discontinuation or limitation data supplied (<n> benefit statements affected)
Unbiased · selective reporting: not checkable — only the draft was supplied, not the material it draws on (<n> results affected)
```

Counting rules:

- A benefit statement is any sentence or bullet stating a benefit of the product or
  intervention (efficacy, outcome, convenience, value). A risk or limitation statement
  states a side effect, discontinuation, warning or limitation.
- "Nearby" means in the same slide, paragraph or section, in the body, not only in a
  footnote or another piece.
- Left-out items are counted from the evidence inventory, after deciding which are out
  of a stated scope. Items outside a stated scope are not counted.
