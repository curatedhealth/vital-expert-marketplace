# Output format: model review and repair

## Short mode (default for direct questions; 250 to 450 words)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

1. **Answer:** two or three sentences: against the person's rules, which pass and which miss, and the one decision needed.
2. **Rules:** Rule (person's words) · Pass, miss or not judgeable · Finding behind it · Owner (person's).
3. **Repairs:** Input or section · Change · Source of new value · Effect on result. Only inputs the person named; others marked "proposed".
4. **Gaps and stop:** at most three gap lines.
5. **Record:** Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode (review pack)

### Answer

### The person's acceptance rules
| Rule | Type | Owner | Confirmed on |
|---|---|---|---|

### Check against each rule
| Rule | Result | Findings (from A1, A2) | Owner |
|---|---|---|---|

### Score (only if the person supplied a scoring rule)
Their rule as written, the arithmetic, the result. Never a CHEERS score.

### Repair list
| Input or section | Named wrong by the person? | Change | New value and source | Before | After | Tool or script |
|---|---|---|---|---|---|---|

### Proposed repairs (not applied)

### Routing
| Miss | Responding work |
|---|---|

### Gaps

### Sources and record
AI-assisted draft. Stops for the owner. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
