# Output format: segment choice and GTM motion (decision draft)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Ranking as scored by you:** Segment · Value (0 to 100) · Biggest contributing criterion. If no scores were given, say that criteria, weights and 0 to 4 scores from the person will be run through `analytics.mcda`, and show the fact table instead.
2. **Close call:** the weight at which the top two would swap; the same for second and third.
3. **In scope and out of scope:** your choice, one reason each; or "not chosen yet".
4. **Motion per chosen segment:** Segment · Channel · Offer · Proof before a meeting (row) · Binding rules (rows) · Owner you named.
5. **Stops:** what goes to compliance, pricing or the regulatory owner.
6. **Record:** "Decision draft. Scores, weights, choice and owners are yours." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
7. One line offering the full version.

## Full mode

### What this ranks
Segments considered, segments left out and why; scores and weights are the person's.

### Criteria, anchors and weights
| Criterion | 0 means | 2 means | 4 means | Weight |
|---|---|---|---|---|

### Facts behind the scores
| Segment | Criterion 1 | Criterion 2 | ... |
|---|---|---|---|
Each cell: fact with row or source, then the person's score in brackets. A `[GAP]` cell says so.

### Ranking
| Rank | Segment | Value | Contributions |
|---|---|---|---|
Method: as returned by the tool (EVIDEM weighted sum; ISPOR MCDA good practice).

### How robust
| Pair | Criterion | Current weight | Swap at |
|---|---|---|---|

### Scope
| Segment | In or out | Order | Reason (yours) |
|---|---|---|---|

### Motions
| Segment | Channel | Offer | Proof before a meeting | Channel rules (rows) | Owner |
|---|---|---|---|---|---|

### Stops for the accountable owner
Each with the elements laid out (met, missed, `[GAP]`) and "draft for the owner".

### Record
Decision draft. No price, no forecast, no arrangement called protected. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
