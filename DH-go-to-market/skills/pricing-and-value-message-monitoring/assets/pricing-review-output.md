# Output format: pricing and message review (review draft)

## Short mode (default for direct questions; 250 to 450 words)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

1. **Verdict by rule:** Rule (your words) · Pass / Miss / Not measurable · Number behind it · Owner you named.
2. **Corridor or deal:** for the main pricing miss, both readings with the facts for each; the person decides.
3. **Message misses:** live Stop or unsupported claims, where they run, pattern or one-off.
4. **Where the response sits:** one line per miss.
5. **The decision needed:** one or two sentences.
6. **Record:** "Review draft. Rules and owners are yours." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Summary

### Pass rules
| Rule type | Rule in your words | Threshold | Owner | Measured by |
|---|---|---|---|---|

### Results
| Rule | Number behind it | Date | Pass / Miss / Not measurable | Source (A1, A2, your data) |
|---|---|---|---|---|

### Corridor or deal
| Miss | Facts pointing to the corridor | Facts pointing to the deal | Next deal the corrected rule applies to |
|---|---|---|---|

### Message misses
| Claim | Level | Where it runs | Pattern or one-off | Rows |
|---|---|---|---|---|

### Hypotheses
| Miss | Hypothesis | What would confirm it |
|---|---|---|
Labeled as hypotheses; none is a finding.

### Response routing
| Miss | Responding work | Owner you named |
|---|---|---|

### Gaps and record
Rules not measurable and why. Corridor changes, discount policy, claim wording and payer matters stop for their owners. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
