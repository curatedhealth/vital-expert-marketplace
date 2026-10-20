# Output format: decision support design and delivery

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/metric_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Build the driver line from `scripts/metric_check.py driver` output; do not compute by hand. Budget in words: answer 60, design check 110, driver and commentary 60, facts beside the design 130, open items 40, record 45.

1. **Answer** (two sentences): what your design shows and lacks against the method (timestamp, comparison, stop owner, export), the driver result under your rule, and the decision support fact that bears most on this design. No device or compliance conclusion.
2. **Design check:** Element (decision metric first, comparison, data timestamp, certified metrics only, action without leaving the step, stop owner for stale numbers) · Your design (shown, not shown, not given).
3. **Driver and commentary:** the one sentence; segments that account for the move under your rule, or "no driver named"; the action as a question unless your frame named one.
4. **Facts beside the design:** Fact · Source and date · Row · Your design shows it (yes, no, not given). For the market and audience in the request only.
5. **Open items:** item · owner you named (or owner not named) · date (or "not given"); device status "for the owner you name for regulatory matters", route `dh-regulatory-and-quality` regulatory-pathway-and-classification.
6. **Calls made**, then one line offering the full version.
7. **Record (the very last line, nothing after it):** "Decision support design draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Executive dashboard (your decision, metrics, metric kept off, comparison, timestamp, review record)
### Commentary
| Sentence | Comparison | Driver under your rule | Action (question or from your frame) | Date and author |
|---|---|---|---|---|
### Driver computation (scripts/metric_check.py driver)
### Embedded analytic
| Element | Your design |
|---|---|
| Host workflow and step | |
| What appears | |
| What is removed | |
| Action without leaving the step | |
| Write-back or task created | |
| Action that still needs another system | |
| Metric owner | |
| Workflow owner | |
| Who stops a stale number, and your stale rule | |
### Recommendation and delivery (your action, alternative, evidence, condition that changes it; parked questions)
### Decision support facts beside the design (market and audience in the request)
| Fact | Source and date | Rows | Your design shows it |
|---|---|---|---|
### Fairness criteria in conflict (only if the product ranks or allocates; DA-116 to DA-119, DOI 10.1038/s41746-020-0304-9)
### For the owners you name (device status, compliance)
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Decision support design draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
