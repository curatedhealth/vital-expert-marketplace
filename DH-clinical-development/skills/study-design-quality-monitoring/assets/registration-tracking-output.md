# Output format: registration and amendment tracking

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** registry id and read date; registered before the reference date or not (CV132, with the reference used); clocks that apply and where they stand, or applicability [GAP]; the most important difference between registry, protocol and paper.
2. **Side by side:** table Element · Registry (verbatim, read date) · Protocol (version, locator) · Paper (locator) · Reading (same, worded differently, not stated) · Rows. Use the rows in references/robustness-signals.md for each element: outcome SP-16, CV113; masking SP-24a; secondary outcomes ES-71.
3. **Clocks:** table Clock · Facts · Days · Applies? · Rows.
4. **Amendments:** one line per change touching outcome, estimand, sample size or analysis, with date and whether a reason is documented.
5. **Calls made:** list.
6. **Record:** "Registration tracking draft for OWNER. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Link between paper and registration
### Side by side
| Element | Registry | Protocol | Paper | Reading | Rows |
|---|---|---|---|---|---|
### Clocks
| Clock | Facts | Days counted | Applies (person, or [GAP]) | Rows |
|---|---|---|---|---|
### Amendment log
| Version | Date | Items affected | Touches primary outcome, estimand, sample size or analysis | After first enrollment | Reason documented |
|---|---|---|---|---|---|
### Stops for the accountable owner
### Gaps
### Calls made
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
