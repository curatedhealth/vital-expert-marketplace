# Output format: prediction, personalization and forecasting choices

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/prep_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Build lines 3 and 4 from `scripts/prep_check.py holdout`, `forecast` or `split` output; do not compute by hand. Budget in words: answer 70, application 40, results 130, choices 110, open items 50, record 50.

1. **Answer** (two sentences): the application and the action it drives; the held-out result for all rows and for the group a miss harms; the choices still open.
2. **Application:** type, action, device question routed if it informs diagnosis or treatment.
3. **Held-out result:** Group · n · Events · AUROC · Observed vs mean predicted · at your threshold only: sensitivity, specificity, PPV; flags H1 to H4 (or forecast: MAE forecast vs naive baseline, interval coverage, FC1 to FC3).
4. **Your choices:** label rule, metric, threshold, fairness criterion (with DA-119 if outcome rates differ, Paulus and Kent 2020, DOI 10.1038/s41746-020-0304-9), use limit, reviewer; or policy, log and refusal path; or constraint and who may relax it. Each "yours" or "not given".
5. **Open items:** item · owner (yours, or owner not named) · date (yours, or "not given").
6. **Calls made**, then one line offering the full version.
7. **Record (the very last line, nothing after it):** "Model choices record draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Application, action and device question
### Label rule and exclusions (yours)
### Split facts (from A1)
### Held-out result (script output)
| Group | n | Events | Observed rate | Mean predicted | AUROC | Sensitivity | Specificity | PPV | NPV |
|---|---|---|---|---|---|---|---|---|---|
### Reporting items beside your result
| Item | What you have | Source and rows (DOI for [PAPER]) |
|---|---|---|
### Fairness criterion (your choice) and what cannot hold together
### Score limit and reviewer
### Recommendation unit, policy and log (if personalization)
| Element | Your choice | Source and rows (DOI for [PAPER]) |
|---|---|---|
| Decision points | | |
| Options and one recommendation not made | | |
| Tailoring variables and missing-data behavior | | |
| Decision rule or model version | | |
| Proximal and distal outcomes | | |
| Inputs disclosed to users | | |
| Refusal path | | |
| Log fields and retention | | |
### Forecast or optimization (if forecasting)
| Item | Your choice or script output |
|---|---|
| Quantity, grain, horizon | |
| Decision that uses it | |
| Baseline | |
| Holdout MAE, forecast vs baseline | |
| Interval coverage and nominal level | |
| Constraint and who may relax it | |
### Choices record
| Choice | Yours | Facts behind it | Status |
|---|---|---|---|
### Open items
| Item | Owner | Blocks | Date |
|---|---|---|---|
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Model choices record draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
