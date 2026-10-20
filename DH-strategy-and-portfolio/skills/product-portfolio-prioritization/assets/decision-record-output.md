# Output format: portfolio decision record

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. Count with `python3 scripts/portfolio_rank.py words ANSWER.md`.

## Short mode (default for a direct question)

1. **Answer:** Forum · date · decider (as you named) · continue n, stop n, delay n · capacity: continue items use X of your Y (unit, period), or "capacity not given" · open item that blocks most.
2. **Decisions:** Item · Rule and rank (or "no rule recorded") · Implied by your rule · Decision (yours) · Reason where they differ (yours, or "reason not given") · Condition.
3. **Dissent and conditions:** in the words you gave.
4. **Open items:** Item · Owner (as you named, or owner not named) · Blocks · Reread date (yours, or "reread date not given"; ask). Facts cited by source name and date, then row.
5. **Stops:** licensing conclusions for the owner you named for legal; external wording.
6. **Record:** "Decision record draft for the owner. Decisions, decider, reasons and owners are yours." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

Calls made (after the record line).

## Full mode

### Forum
Forum, date, decider, attendees as you gave them.

### Rule and rank used
The rule as confirmed in B1, with the rank. If none: "no rule recorded".

### Decisions
| Item | Rank | Implied by your rule | Decision (yours) | Reason (yours) | Condition (yours) | Capacity use (yours) |
|---|---|---|---|---|---|---|

### Capacity
Named capacity (amount, unit, period); total for continue items; first continue item past it. "Do not continue every item" check and your answer, if every item continues.

### Licensing and partnered items
Per item: flags by source name and date, then row; each threshold beside your figure, or "not given"; company status line from the dated filings; owner for legal as you named, or owner not named. No license called exempt.

### Dissent

### Open items
| Open item | Owner | Blocks | Reread date |
|---|---|---|---|

### Record
Decision record draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
