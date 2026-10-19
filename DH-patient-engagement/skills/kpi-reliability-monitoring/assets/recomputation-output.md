# Output format: KPI recomputation

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** match or mismatch, in one sentence, with the three numbers (dashboard, recomputed with the card, recomputed with the dashboard's definition if available).
2. **Comparison (compact):** Source · Value · Numerator · Denominator · As of / refreshed.
3. **What explains the difference:** the evidence (field, rows excluded, refresh), or "unexplained" plus one labeled hypothesis.
4. **Instrument (if any):** COSMIN criteria met or not met by the evidence named, one line each, with rows.
5. **Record:** "Recomputed on your data, as of DATE. Clears: NAME, the owner you named (or 'owner not named'; ask). Uncleared draft: once NAME clears it, the record is built with `verify.build_record`."
6. One line offering the full version.

## Full mode

### Answer

### Run
Card used · dashboard definition used · file · as-of date · period · rows excluded (by reason).

### Three-way comparison
| Source | Value | Numerator | Denominator | As of | Refreshed |
|---|---|---|---|---|---|
| Dashboard | | | | | |
| Recomputed with the card | | | | | |
| Recomputed with the dashboard's definition | | | | | |

### Difference and its evidence
| Difference (units and counts) | Evidence | Explained / unexplained |
|---|---|---|

### Instrument measurement properties (if any)
| Property | COSMIN criterion for sufficient (row) | Evidence named | Met / not met / not seen |
|---|---|---|---|

### Your tolerance
Your rule · the difference · within or outside, or "no rule set".

### Hypotheses (labeled)
| Hypothesis | What would confirm it |
|---|---|

### Gaps

### Record
Recomputed on your data with the card's rules. No number adjusted. AI-assisted. Clears: NAME, the owner the person named, or "owner not named". Uncleared draft until NAME clears it; the record is then built with `verify.build_record`.
