# Output format: intended use and validation plan

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/model_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Build line 3 from `scripts/model_check.py split` output; do not recount by hand. Budget in words: answer 60, intended use 70, data plan 120, split check 80, subgroups and metrics 60, needed from you 30, record 45.

1. **Answer** (two sentences): the intended use in one line or what it lacks, the split flags that matter most, populations not validated, and what is still needed from you.
2. **Intended use:** user · input · output · decision supported · decision excluded · population, each yours or "not given".
3. **Split check (your manifest):** Split · Records · Patients · Sites · Dates; flags S0 to S5 verbatim with their rows.
4. **Data plan against the rows:** Element · Yours · Rule · Rows (draft or final, with date).
5. **Subgroups and metrics:** subgroups and counts; fairness criterion (yours or "not given"); metrics named before the run and the date named; values "not given" unless yours.
6. **Needed from you:** item · why.
7. **Calls made**, then one line offering the full version.
8. **Record (the very last line, nothing after it):** "Validation plan draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Intended use (your words)
| Element | Yours | Rows |
|---|---|---|
| User | | DA-10, CV125 |
| Input | | DA-36 (draft) |
| Output | | CV127 |
| Decision supported | | old DH-01.04.3.1.1 |
| Decision excluded | | old DH-01.04.3.1.1, DA-11 |
| Population | | CV125 |
### Data subsets named (training, tuning, internal test, external test by site or time)
### Data plan against the rows
| Element | Yours | Rule (status and date) | Rows (DOI for [PAPER]) |
|---|---|---|---|
### Split check on your manifest (script output)
### Populations not validated
### Subgroups and fairness criterion (yours; impossibility row where criteria conflict, DA-119, DOI 10.1038/s41746-020-0304-9)
### Metrics named before the run (yours, with date)
### Checklists that fit (PROBAST+AI, DECIDE-AI, CLAIM 2024, TRIPOD+AI)
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Validation plan draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
