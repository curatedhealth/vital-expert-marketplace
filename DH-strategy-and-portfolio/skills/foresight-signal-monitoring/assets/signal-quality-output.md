# Output format: signal quality check

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with `python3 scripts/foresight_check.py --words ANSWER.md` (counts the whole answer except the calls list, and leaves out the Source, Rows, Retrieved and Evidence columns); without code execution, count the same way by hand. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Build counts from `scripts/foresight_check.py` output; do not recount by hand. Budget in words: answer 70, table 180, rereads 70, leads 40, record 50. Every fact names its source in plain words with its date, then the row id ("FDA 510(k) K261317, decided 14 May 2026"; "Pear 8-K, filed 7 April 2023 (SP-156) [WF]"); never a row id alone.

1. **Answer** (two or three sentences): how many signals pass the checks (yours, or proposed checks), how many are leads, what the reread changed, and the check that fails most often.
2. **Check table:** Id · Signal · Checks failed (Q1 to Q8) · Reread result · Source. Only rows tied to the question.
3. **Rereads:** "On DATE the log read X; on reread the record reads Y (retrieved DATE)."
4. **Leads, not signals:** each with the record that would confirm it.
5. **Company status** (signals about a named company): the status already read (`references/company-status.md` section 6) cited by filing or register name and date, or "Status: [GAP]: not read" with the newest stored filings named as the first to open. A product's current FDA listing holder is stated apart from the company that was authorized.
6. **Calls made**, then one line offering the full version.
7. **Record (the very last line):** "Signal quality draft for the owner. Checks yours or proposed. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Checks applied (yours, or proposed Q1 to Q8)
### Perimeter now versus at the scan
| Source | At the scan | Now | Effect |
|---|---|---|---|
### Check results (script output plus Q4 to Q8)
| Id | Signal | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Source |
|---|---|---|---|---|---|---|---|---|---|---|
### Rereads
| Id | Log reading (date) | Record now (identifier) | Retrieved | Changed |
|---|---|---|---|---|
### Leads, duplicates, drafts logged as final
### False positives (your definition, or proposed with the failed check)
### Company status (named companies)
### Gaps
### Calls made
### Record (the very last line)
Signal quality draft for the owner. Checks yours or proposed. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
