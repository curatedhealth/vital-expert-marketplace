# Output format: the Verify card

Follows the confidence line. Plain words for each status (TR-H13); VERIFY's status names
appear only if the person asks. Size it to the stakes (TR-H12).

| VERIFY status | Words on the card |
|---|---|
| supported | backed by the passage |
| partial | partly backed |
| unsupported | not backed by the passages checked |
| contradicted | contradicted by a passage |
| unverifiable | could not be checked |
| out_of_scope | not a factual statement (not counted) |

## Full card (leadership or leaving the company)

```
Verify card (draft, for human review)

Checked with VERIFY: <total> statements
  <n> backed by the passage
  <n> partly backed
  <n> not backed by the passages checked
  <n> contradicted by a passage
  <n> could not be checked
  <n> not a factual statement (not counted)

Open for a human (<m>)
1. "<short quote of statement>" (contradicted). The passage says: "<quoted words>".
2. "<short quote>" (not backed). The passages checked do not state this.
3. "<short quote>" (could not be checked). <No source supplied | the source could not be read>.
4. "<short quote>" (partly backed). The passage gives <part>; it does not give <part>.

Recommendation: <one sentence on what to do to the text or the sources>.

The check matches words in each statement with words in its passage; a reworded or
weaker sentence can still come back backed, so a human read still matters.
<If the work leaves the company:> Next step: <kind of internal process, e.g. your
promotional review process> before it is used.
This card is not a clearance. A named reviewer clears the record.

This check flags issues. It is not medical, legal, regulatory or ethics review.
```

## Short card (internal)

```
Checked with VERIFY: <total> statements. <n> backed, <n> partly backed, <n> not backed,
<n> contradicted, <n> could not be checked, <n> not factual.
Recommendation: <one sentence>.
```

## Without VERIFY (no card)

```
Read, not tool-checked: <total> statements
  <n> found in your material · <n> not found in it · <n> not factual
No confidence figure. Connect VERIFY to check each statement against its passage.
```
