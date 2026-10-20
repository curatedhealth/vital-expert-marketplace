# Output format: screen criteria and short list

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words (`scripts/screen_helpers.py wordcount <answer.md>`, or by hand). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

Sources and status in every answer: each fact cites its source name and date in plain words, then the row id ("Pear 8-K, 7 April 2023 (SP-156 [WF])"; "BfArM DiGA page, as of 9 September 2026 (DE34)"; "VITAL library screen_market, saved 19 October 2026"); never a row id alone. Company status for a company in `references/named-company-status.md` comes from those rows, with what each form does not mean, and a product's current FDA listing holder is stated apart from the company that was authorized; "Status: [GAP]: not read" only where no row covers the company. Rows the research file marks as an inference carry "(inference)" every time. A date, owner or threshold the person did not give is "not given", with the question to ask.

## Short mode (default for a direct question)

1. **Answer:** how many candidates pass the person's rules, the order as scored, and the close call. Two sentences. No recommendation.
2. **Pass rules:** Candidate · Status (primary record, or `[GAP]`: not read) · Rule 1 · Rule 2 · ... (pass, fail, not measurable `[GAP]`, each with its fact and source).
3. **Ranking as scored:** Candidate · Value · Largest contributor · Swap point with the next candidate. "Your scores and weights."
4. **Not ranked:** candidates with a missing score or a `[GAP]` that blocks the rule, one reason each.
5. **Flags for the owner you name for legal questions:** Rule (row, instrument and date) · Trigger in the facts (source) · Question for the owner. "Not assessed here."
6. **Decision for the person:** the short list, in their words.
7. **Full version:** one line offering it, before the record block.
8. **Calls made** (before the record block; not counted in the word cap): tool and arguments, one line each.
9. **Record (the very last line of the answer; nothing follows it, nothing sits between "Record" and "Clears it"):** "Short-list draft on your criteria and scores. Not investment advice." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Criteria and pass rules (yours)
| No. | Criterion or rule, in your words | Checkable from the record? | Fact used |
|---|---|---|---|
### Company status
| Candidate | Status as the record states it (form or item, date) | Source and read date | Does not mean (row) |
|---|---|---|---|
### Pass rule results
| Candidate | Rule | Result | Fact | Source and retrieved |
|---|---|---|---|---|
### Scores and weights (yours)
| Candidate | Criterion | Score (0 to 4) | Weight |
|---|---|---|---|
### Ranking as scored
| Candidate | Value | Contributions | Swap point |
|---|---|---|---|
### Not ranked
### Flags for the owner you name for legal questions
| Rule | Rows | Instrument and date | Trigger in the facts | Facts not given |
|---|---|---|---|---|
### Short list (your decision)
| Candidate | In or out | Reason (yours) |
|---|---|---|
### Gaps
### Calls made (before the record block)
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
