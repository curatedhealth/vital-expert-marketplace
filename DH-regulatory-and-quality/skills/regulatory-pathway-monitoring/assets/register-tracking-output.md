# Output format: authorization and register tracking

Short mode is 450 words maximum, counted without tables' source column and the calls list. Before handing over, count the words of the answer (excluding the calls list and table source columns). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question, full-mode sections. Never cut a gap, a stop or the record line. Offer the full version in one line. A refusal or stop answer follows the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** one or two sentences: what changed since the baseline, and which clock or obligation decides the next move.
2. **Status by jurisdiction:** Product or comparable · Jurisdiction · Status per record · Changed since baseline? · Source (retrieved DATE).
3. **Open reviews:** Submission · Calendar days · FDA days (if hold days given) · Labeled reference figure.
4. **Register duties:** one line per jurisdiction: the rule and the person's status as given.
5. **Gaps:** one line (change log not started; UK and CH not loaded; EU decision dates not stored).
6. **Record:** "Tracking snapshot as of DATE. Uncleared." or the clearer's name.

## Full mode

### What the library can see

Per jurisdiction: loaded or not, count, last load date.

### Changes since the baseline

| Item | Field | Baseline (date) | Now (date) | Source |
|---|---|---|---|---|

Change-log result per scope, worded as a fact about the log.

### Review clocks

| Submission | Route | Submitted | Calendar days | FDA days | Regulation clock | MDUFA goal (FDA days) | FDA observed average total days |
|---|---|---|---|---|---|---|---|

### Register obligations

| Jurisdiction | Rule (row) | Your status as given | What it bears on |
|---|---|---|---|

### What it means for the pathway

Conditional consequences, each with its source; routing to the pathway and classification skill where a strategy fact moved.

### Gaps

Classified per `references/gap-rules.md`.

### Record

Tracking draft. No compliance verdict. Pathway changes and regulator wording stop for the regulatory owner. AI-assisted. Cleared by NAME, or uncleared.
