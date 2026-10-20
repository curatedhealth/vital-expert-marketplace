# Output format: validation record and promotion

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/model_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Build lines 2 to 4 from `scripts/model_check.py evaluate` output; do not recompute by hand. Budget in words: answer 70, criteria 90, values 90, fairness 60, promotion and watch 60, record 45.

1. **Answer** (two sentences): result on each of your criteria (or "criteria not given"), the population that limits the record, the fairness reading on your criterion, who accepts (or "not given").
2. **Your criteria:** criterion · written on · observed · met or not met; "acceptance criteria not given" if none; metrics named after the run flagged.
3. **Values on the locked test set:** Population · n · Events · AUROC · O/E · Calibration slope · Sensitivity and specificity at your threshold; populations not validated.
4. **Fairness on your criterion:** group values; impossibility row where criteria conflict (Paulus and Kent 2020, DOI 10.1038/s41746-020-0304-9, DA-119).
5. **Promotion and drift watch:** stages, required record, who may promote; watch signal, your threshold, who is paged, action; "not given" where missing.
6. **Calls made**, then one line offering the full version.
7. **Record (the very last line, nothing after it):** "Validation record draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### What was named before the run (yours, with dates)
### Values on the locked test set (script output; methods named)
| Population | n | Events | Event rate | AUROC (95% CI) | O/E | Calibration intercept | Calibration slope | Brier | Sensitivity | Specificity | PPV | NPV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
### Against your criteria
| Criterion (yours) | Written on | Observed | Met or not met |
|---|---|---|---|
### Populations not validated
### Fairness on the criterion you chose
### Record
| Field | Value |
|---|---|
| Model version | |
| Dataset version | |
| Run id | |
| Metric and result | |
| Accepted by | |
### Promotion rule (yours)
| Stage | Record required | Who may promote | Who may not |
|---|---|---|---|
### Run record
### Drift watch (yours)
| Signal (logged) | Threshold (yours) | Who is paged | Action allowed | Rows |
|---|---|---|---|---|
### Change control route
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Validation record draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
