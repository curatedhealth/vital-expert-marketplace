# Output format: partner scorecard (A2)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question; 250 to 450 words)

1. **Answer:** which partners missed which of your rules, which hit a hold rule, and any open claim breach. One or two sentences.
2. **Scores:** one line per partner: each measure "count (record) vs your threshold: met or missed".
3. **Not counted:** partner-reported numbers not tied to a buyer, with what the partner claimed.
4. **Claim breaches:** quoted with date and source; the rule it touches (row); "goes to OWNER".
5. **Duty checks:** "evidence given" or "not shown", one line each.
6. **Record:** "Scorecard draft on your data and rules. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
7. One line offering the full version.

## Full mode

### Answer

### Scorecard
| Partner | Type | Measure | Count (record) | Rule (yours) | Met / Missed / Not measurable |
|---|---|---|---|---|---|

### Not counted
| Partner | Date | What the partner reported | Why not counted |
|---|---|---|---|

### Claim breaches
| Partner | Date | Wording as used (quoted) | On approved list? | Rule touched | Row | Goes to |
|---|---|---|---|---|---|---|

### Duty checks
| Partner | Duty | Evidence given / Not shown | Row |
|---|---|---|---|

### Gaps

### Calls made

### Record
Scorecard draft. Counts are from your record; rules are yours. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
