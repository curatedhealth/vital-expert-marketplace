# Output format: forum score and benefits read

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. Count with `python3 scripts/forum_check.py words ANSWER.md`.

## Short mode (default for a direct question)

1. **Answer:** Forum and sitting · rule read against (ref and date, confirmed before the forum) · match n, drift n, not measurable n · capacity: recorded continue items use X of your Y · benefits: items below your rule or not measurable · the change since the forum that touches most.
2. **Decisions against your rule:** Item · Recomputed value and rank · Recorded rank · Implied by your rule · Recorded decision · Match or drift.
3. **Benefits (your plan):** Benefit · Item · Owner · Baseline · Target · Actual (date) · Share of planned change · Your rule (or "no rule given") · Flags. "UK public-sector guidance, applied by analogy" where SP-099 to SP-105 are used.
4. **Changes since the forum:** change · instrument and date · rows · items it touches. For a licensed item: the market share condition beside your figure, or "not given" (Regulation (EU) 2026/877, SP-136). Company status line for any named counterparty, from its dated filings (for example "Akili 8-K, 2 July 2024 (SP-151)"), listed from the most recent backward, with what each form does not mean.
5. One line offering the full version.
6. **Record:** "Forum score draft. Match and drift are readings against your rule, not verdicts." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

Calls made (after the record line).

## Full mode

### Rule and inputs
Rule as confirmed before the forum (weights, decision rule, capacity, date); scores as recorded; read date.

### Decisions
| Item | Value | Rank (recomputed) | Rank (recorded) | Implied | Decision | Result | Forum's reason (if recorded) |
|---|---|---|---|---|---|---|---|

### Capacity
Named capacity; total for recorded continue items; first continue item past it.

### Benefits
| Benefit | Item | Objective | Owner | Baseline | Target | Actual (date) | Share | Your rule | Flags |
|---|---|---|---|---|---|---|---|---|---|

### Changes since the forum
| Change | Instrument and date | Rows | Items | Note |
|---|---|---|---|---|
Counterparty status lines; library change log limits (began 12 October 2026).

### Record
Forum score draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
