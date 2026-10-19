# Output format: launch sequence and readiness

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** two or three sentences: where the product stands in each market in scope, with the as-of date, and the prerequisite that blocks the next step.
2. **Sequence:** table Market · Event · Date · Product · Source, retrieved. Product and peers, oldest first; peers labeled comparables; missing peers in one line.
3. **Prerequisites:** table Market · Prerequisite · Row · Your status (shown, stated, not stated). Only the markets asked about.
4. **First in the dependency chain:** one line, with the row.
5. **Gaps:** at most three lines, one per class.
6. **Record:** "Library copy of the registers, retrieved DATE; confirm on the authority's page." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

End with one offer: the full version, or the next task (A2 claim list).

## Full mode (launch plan, board paper)

### Answer

### What the library can see
One line per market from `list_commercial_dh_sources`.

### Launch sequence
| Market | Event (field) | Date | Product (identifier) | Upstream tool | Source, retrieved |
|---|---|---|---|---|---|

### Prerequisites by market
| Market | # | Prerequisite | When | Rows | Your status |
|---|---|---|---|---|---|

### Sequence by dependency
| Do | Before | Because | Row |
|---|---|---|---|
No dates of our own; clocks in the rows are facts.

### Connector readiness count (only if called)
`met_count` N of 7 (g1-commercial-v1), each criterion with status and the pitfall that applies. "A count, not a readiness judgment."

### Gaps
Grouped by class from `references/gap-rules.md`.

### Stops for the accountable owner

### Calls made
Tool, arguments, counted or free.

### Record
Draft. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
