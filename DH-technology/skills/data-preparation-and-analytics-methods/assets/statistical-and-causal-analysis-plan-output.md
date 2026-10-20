# Output format: statistical and causal analysis plan

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/prep_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Build line 4 from `scripts/prep_check.py bayes` output; do not compute by hand. Budget in words: answer 70, question 90, design 90, uncertainty 90, record 60, close 50.

1. **Answer** (two sentences): what this design supports (effect or association); the estimate and interval as computed; whether your decision holds under every prior you named.
2. **The question:** treatment and comparator, population, variable, intercurrent-event strategy, summary (ICH E9(R1), adopted 20 November 2019, CV33, CV34; a trial addendum used as a checklist); a confounder held and one not held.
3. **Design:** the assignment fact; what can be claimed; if a causal claim is refused, what is estimated instead; covariates and their source (yours; FDA covariate guidance, May 2023, drugs, DA-122 to DA-125, context where not a drug).
4. **Uncertainty:** Prior (yours, with source) · Posterior mean · Interval (level stated) · Probability past your threshold · Meets your rule; which prior reverses the decision, if any; which FDA Bayesian document applies (device final 2010, DA-127; drug draft January 2026, DA-130, draft).
5. **Estimate record:** estimate, interval, sample, breaking assumption, data and code version.
6. **Calls made**, then one line offering the full version.
7. **Record (the very last line, nothing after it):** "Analysis plan draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### The decision and who makes it (yours)
### Question and estimand
| Attribute | Your choice | Source and rows |
|---|---|---|
| Treatment and comparator | | |
| Population | | |
| Variable | | |
| Intercurrent events and strategy | | |
| Population-level summary | | |
### Design the data can support
### Covariates and adjustment
### Regression target, fit, check and limit
| Item | Your choice |
|---|---|
| Outcome and unit of row | |
| Predictors used and left out (why) | |
| Use (description or prediction) | |
| Fitting sample and holdout | |
| Assumption checked | |
| Metric chosen before results | |
| Where it must not be used | |
| Who may promote it | |
### Uncertainty under your priors (script output)
| Prior | Beta(a, b) | Posterior mean | Interval | Probability past your threshold | Meets your rule |
|---|---|---|---|---|---|
### Estimate record
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Analysis plan draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
