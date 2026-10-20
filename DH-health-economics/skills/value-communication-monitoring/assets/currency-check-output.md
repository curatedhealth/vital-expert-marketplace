# Output format: claim currency check

## Short mode (default for direct questions; 250 to 450 words)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

1. **Answer:** how many lines hold, which need a re-read, which are held, and the main reason.
2. **Table:** Claim · Source · Retraction and currency (source checked) · Passage re-read in the same direction? · Guidance signal · Status.
3. **Candidate new evidence:** up to five records to read, labeled candidates.
4. **Gaps:** one line per class.
5. **Record:** "Draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Source status
| DOI | check_retraction (source) | check_currency | Date checked |
|---|---|---|---|
### Claims re-checked
| Claim | Passage and locator | Verify status (overlap) | Same direction, population, comparator, outcome, time point | Status |
|---|---|---|---|---|
### Candidate new evidence (not read here)
| Record | Year | Design (label; checked?) | Why it may matter |
|---|---|---|---|
### Guidance and methods signals
| Line | Cites | What moved | Row |
|---|---|---|---|
### Lines for B1
### Sources and record
Calls made with dates. "Draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
