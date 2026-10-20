# Output format: reception tracking

## Short mode (default for direct questions; 250 to 450 words)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

1. **Answer:** which lines land and which do not, on the person's measure, with the base and the log period.
2. **Table:** Line · n · counts by code · share on the person's measure · flag (only under the person's rule).
3. **What stakeholders asked for:** up to three notes, verbatim, each with the row that speaks to it where one exists.
4. **Gaps:** measure, codes or flag rule not set; groups below the person's minimum base.
5. **Record:** "Draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Log checked
Rows read, rows dropped and why, period, grouping.
### Results
| Group | n | Counts by code | Share (person's measure) | Flag (person's rule) |
|---|---|---|---|---|
### Notes and the sources they touch
| Group | Note (verbatim) | Row that speaks to it | Reading (explains the request; does not decide it) |
|---|---|---|---|
### Decisions for the person
### Sources and record
Log file and date; script call if used. "Draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
