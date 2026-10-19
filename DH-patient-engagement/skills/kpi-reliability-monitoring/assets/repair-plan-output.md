# Output format: KPI repair plan

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** per KPI, what changes (card or dashboard, as the card owner decides), the owner, and the refresh by which the numbers must match.
2. **Plan (compact):** KPI · Finding · Change (card / dashboard / retire, proposed until decided) · Owner · Matching refresh.
3. **Order:** from your scores, or by dependency if you have not scored.
4. **Stops:** repairs touching figures already shared outside, one line each, with the owner.
5. **Record:** "Repair plan draft. Clears: NAME, the owner you named (or 'owner not named'; ask). Uncleared draft: once NAME clears it, the record is built with `verify.build_record`."
6. One line offering the full version.

## Full mode

### Answer

### Checked against your rules
| KPI | Your rule | Evidence (A1 / A2) | Met / missed |
|---|---|---|---|

### Repairs
| KPI | Finding | Options and consequence | Decision (card owner) or "proposed" | Card owner | Job owner | Matching refresh | Old version retired how |
|---|---|---|---|---|---|---|---|

### Order
| Repair | Your numbers | Score | Order |
|---|---|---|---|
Or the dependency sequence, with the reason for each step.

### Hypotheses for unexplained differences (labeled)
| KPI | Hypothesis | What would confirm it |
|---|---|---|

### Stops for the owner

### Gaps

### Record
Repair plan draft. Which formula is right, owners and refreshes are yours. AI-assisted. Clears: NAME, the owner the person named, or "owner not named". Uncleared draft until NAME clears it; the record is then built with `verify.build_record`.
