# Output format: evidence outcome review (review draft)

## Short mode (default; 250 to 450 words)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

1. **Verdict by body:** Body · On track / At risk / Missed · Stall point in the evidence chain · Owner you named.
2. **The decision needed:** one or two sentences.
3. **Score (only with your formula):** the arithmetic in one line, labeled your score.
4. **Hypotheses to test first:** at most three, each labeled, with the decision quote it rests on and what would confirm it.
5. **Where the response sits:** one line per miss.
6. **Record:** "Review draft. Outcomes, formula and owners are yours." Clears it: [the person named, in their words, or owner not named: ask "Who clears this record?"]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Summary

### Outcomes (yours)
| Body | Outcome in your words | Shown by | Owner | Confirmed on |
|---|---|---|---|---|

### Results
| Body | Outcome | Quote or fact behind it | Met / Missed / Not measurable | Source (A1 or A2, date) |
|---|---|---|---|---|

### Score (your formula)
| Body | Formula | Inputs | Result |
|---|---|---|---|

### Stall points
| Body | First failed point in the chain | What it means |
|---|---|---|

### Hypotheses
| Body | Hypothesis | Decision quote it rests on | What would confirm it |
|---|---|---|---|
Labeled as hypotheses; none is a finding.

### Response routing
| Body | Stall point | Responding work | Owner you named |
|---|---|---|---|

### Record
Review draft. Responses to a body stop for the accountable owner. AI-assisted. Clears it: [the person named, in their words, or owner not named: ask "Who clears this record?"]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
