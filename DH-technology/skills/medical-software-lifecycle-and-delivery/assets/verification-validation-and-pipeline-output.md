# Output format: verification, validation and release pipeline

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/lifecycle_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Budget in words: answer 70, V&V 120, pipeline 120, gaps 40, record 50.

1. **Answer** (two or three sentences): the intended use as written, hazards with and without a planned case, the stages and which one deploys, evidence kept and missing.
2. **V&V structure:** case fields (id, specification line, hazard ids, input, step, expected output, build id, result, date); validation with a user (role, task, named build, misreads); acceptance criteria "set by you [GAP]".
3. **Pipeline:** Stage (your words) · Deploys to production? · Skipped on hotfix? · Rule it serves · Source (row).
4. **Evidence kept:** artifact, where, how long; missing ones as [GAP]; pipeline tools and their CSA record (CSA guidance, 3 February 2026, EN-012).
5. **Calls made**, then one line offering the full version.
6. **Record (the very last line, nothing after it):** "V&V and pipeline draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Intended use and hazards
### Verification case structure (PL21)
### Validation with a user (PL22; human factors routed)
### Pipeline stages
| Stage (your words) | Deploys to production | Hotfix path | Rule it serves | Source (row) |
|---|---|---|---|---|
### Evidence each release keeps
| Artifact | Produced by the pipeline (yes, no, not given) | Where | How long | Source (row) |
|---|---|---|---|---|
### Pipeline tool validation (CSA)
### Separation of environments and production data
### Proposed items (labeled "proposed", not applied until you confirm)
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
V&V and pipeline draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
