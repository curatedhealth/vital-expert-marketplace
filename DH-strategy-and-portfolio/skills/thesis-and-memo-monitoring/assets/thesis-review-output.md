# Output format: thesis review

Short mode: 450 words maximum, counted without the calls list and the Source, Source of now and Rows columns. Before handing over, count the words with `python3 scripts/thesis_check.py --words ANSWER.md` (counts the body above the calls list and leaves out Source, Source of now and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap.

Sources and status in every answer: each fact cites its source name and date in plain words, then the row id ("Pear 8-K, 7 April 2023 (SP-156 [WF])"; "BfArM DiGA page, as of 9 September 2026 (DE34)"; "VITAL library screen_market, saved 19 October 2026"); never a row id alone. Company status for a company in `references/named-company-status.md` comes from those rows, with what each form does not mean, and a product's current FDA listing holder is stated apart from the company that was authorized; "Status: [GAP]: not read" only where no row covers the company. Rows the research file marks as an inference carry "(inference)" every time. A date, owner or threshold the person did not give is "not given", with the question to ask.

## Short mode (default for a direct question)

Build lines 1 and 2 from `scripts/thesis_check.py` output; do not recount by hand. Budget in words: answer 60, table 180, met triggers 50, limits 60, decisions 40, record 50.

1. **Answer** (two sentences): as of the read date, counts of rules met, not met, and not measurable or not comparable; the met triggers by name; the flag that most limits the read. No overall verdict.
2. **Assumption table:** Id · Assumption · At memo · Now · Rule met · Owner · Reread · Flags. Trigger wording and sources go to the full version.
3. **Met triggers:** what your rule says follows, with the owner you named, or "follow-up not given; your call".
4. **Limits:** T5, T4, T3 and a signal broader than its assumption, one line each; the company status line from A2.
5. **For you to decide:** each with its facts.
6. **Full version:** one line offering it, before the record block.
7. **Calls made** (before the record block; not counted in the word cap): each call with its arguments.
8. **Record (the very last line of the answer; nothing follows it, nothing sits between "Record" and "Clears it"):** "Thesis review draft for the owner. Not investment advice. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Assumption table (script output)
### Met triggers and follow-ups (your rules)
| Id | Trigger | Fact behind it | Follow-up (your words) | Owner | Reread date |
|---|---|---|---|---|---|
### Not met, with caveats
### Not measurable or not comparable
### Owners and reread dates
### For you to decide
### Gaps
### Calls made (before the record block)
### Record
Thesis review draft for the owner. Not investment advice. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
