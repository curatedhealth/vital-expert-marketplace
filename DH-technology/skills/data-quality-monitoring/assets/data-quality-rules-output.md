# Output format: data quality rules

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/dq_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Build line 3 from `scripts/dq_check.py rules` output. Budget in words: answer 60, dataset 40, checks 150, missing 70, record 50, close 40.

1. **Answer** (two sentences): checks by Kahn category, how many have a limit, whether a leak check and a version exist, what is missing most.
2. **Dataset:** name, version (or "not given"), unit of row, intended use, written by and on (yours).
3. **Checks:** Check · Kahn category (Kahn et al. 2016, DA-94 to DA-98, DOI 10.13063/2327-9214.1244) · Field · Context · Your limit (or "not given"); proposed checks labeled "proposed", with no limit.
4. **Still missing:** flags Q1 to Q6 in one line each; the categories not covered.
5. **Calls made**, then one line offering the full version.
6. **Record (the very last line, nothing after it):** "Data quality rules draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Dataset, version, unit of row and intended use (yours)
### Checks
| Check | Kahn category | Field(s) and parameters | Context (verification or validation) | Your limit | Flags |
|---|---|---|---|---|---|
### Categories not covered (proposed checks, no limits)
### Requirements laid beside the rules (market and status stated)
| Requirement | Source and date | Rows |
|---|---|---|
### Written by and on
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Data quality rules draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
