# Output format: narrative review and repair (draft for the owner)

## Short mode (default for direct questions; 250 to 450 words)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

1. **Answer:** lines passing and missing on the person's rule, the main cause, the proposed repairs.
2. **Table:** Line · Result (A1, base) · Currency (A2) · Pass or miss (person's rule) · Cause class · Proposed repair · Owner.
3. **Not shown:** lines not assessable, causes not established.
4. **Record:** "Draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Rules applied
The person's rules, in their words.
### Review
| Line | A1 result (measure, base) | A2 status | Pass / miss / not assessable | Cause class and the fact behind it | Owner |
|---|---|---|---|---|---|
### Proposed repairs (draft for the owner)
| Line | Current wording | Proposed wording | Why (row or passage) | Stop |
|---|---|---|---|---|
### Routed elsewhere
Price, coverage, contracts, marketing claims, new claims (to value-narrative-and-dossier A1).
### Decisions for the owner
### Sources and record
"Draft for the owner. The skill does not clear lines. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
