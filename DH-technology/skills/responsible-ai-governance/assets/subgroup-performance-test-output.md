# Output format: subgroup performance test

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/subgroup_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Budget in words: answer 70, test 50, table 150, conflicts 70, limits 50, record 45.

1. **Answer** (two sentences): the largest difference against your reference with counts and interval, the groups unseen, and whether outcome rates differ. No pass, fail, "fair" or "biased".
2. **The test (yours):** model version, dataset version and data cut, subset (internal or external testing), threshold, reference group. Missing: "not given".
3. **By group:** Group · n · Outcome rate · Sensitivity (count, 95% CI) · Specificity · PPV · Mean score vs observed. Every group, "group not recorded", and each [GAP] group as "not tested".
4. **Against your reference:** the differences you asked about, as computed.
5. **Criteria in conflict:** the impossibility result when outcome rates differ (Paulus and Kent 2020, DOI 10.1038/s41746-020-0304-9, DA-119); "which criterion fits the decision is yours" (DA-116).
6. **What the test does not show:** one line each.
7. **Calls made** (script command), then one line offering the full version.
8. **Record (the very last line, nothing after it):** "Subgroup performance test draft. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### The test (yours)
### Results by group
| Group | n | Outcome rate | Mean score | O/E | Sensitivity (95% CI) | Specificity (95% CI) | PPV | NPV | FNR | FPR | Selection rate |
|---|---|---|---|---|---|---|---|---|---|---|---|
### Differences against your reference group
| Group | Metric | Group value | Reference value | Difference | Ratio |
|---|---|---|---|---|---|
### Fairness criteria and the conflict between them
| Criterion | Definition as the source states it | Source and rows |
|---|---|---|
### Possible label bias
### What the test does not show
### Special-category data used to find the groups (EU only)
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Subgroup performance test draft. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
