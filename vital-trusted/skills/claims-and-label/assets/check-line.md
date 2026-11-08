# Output format: check line for trusted-check

Returned to `trusted-check` only, never shown at the end of a direct reply. One line per
task that ran, in plain words. Counts only; no verdict words (TR-H3, TR-H13). Shapes
match `trusted-check/references/letter-lines.md`.

```
Rule-compliant · label and intended use: <n> statements beyond the label or intended use, label supplied (not tool-checked)
Rule-compliant · promotion: <n> promotional statements in material meant as scientific exchange (not tool-checked)
Rule-compliant · promotion: <n> statements that need promotional review (not tool-checked)
Rule-compliant · comparisons: <n> comparative or superiority claims, <n> without a head-to-head source (not tool-checked)
```

Which promotion line to use: the first when the person states the piece is scientific
exchange, a reply to a question or disease information; the second when the piece is
promotional or its use was not stated. Never both.

Each line may carry up to three short plain notes, for the summary:

```
  - <where and what, e.g. "key message 3 reaches teenagers; your label covers adults only">
  - <e.g. "subject line calls the treatment 'game-changing' in a reply to a doctor">
  - <e.g. "'patients deserve better than Kelandro' talks down a competitor">
```

If the label or intended purpose was not supplied (following the not-checkable form in
the contract):

```
Rule-compliant · label and intended use: not checkable — label not supplied (<n> product statements affected)
```

If the comparisons rest on studies not supplied:

```
Rule-compliant · comparisons: not checkable — studies behind the comparisons not supplied (<n> comparative claims affected)
```

"Not tool-checked" stays on every line until a companion for this skill exists. A
comparison checked against its passage by `claim-assessment` reports that result in its
own True line, not here.
