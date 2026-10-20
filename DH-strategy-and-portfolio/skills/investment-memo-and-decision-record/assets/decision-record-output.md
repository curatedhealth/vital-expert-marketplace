# Output format: memo and decision record

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/memo_facts.py words ANSWER.md` (counts the body above the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap.

Sources and status in every answer: each fact cites its source name and date in plain words, then the row id ("Pear 8-K, 7 April 2023 (SP-156 [WF])"; "BfArM DiGA page, as of 9 September 2026 (DE34)"; "VITAL library screen_market, saved 19 October 2026"); never a row id alone. Company status for a company in `references/named-company-status.md` comes from those rows, with what each form does not mean, and a product's current FDA listing holder is stated apart from the company that was authorized; "Status: [GAP]: not read" only where no row covers the company. Rows the research file marks as an inference carry "(inference)" every time. A date, owner or threshold the person did not give is "not given", with the question to ask.

## Short mode (default for a direct question)

Budget in words: answer 60, thesis against record 90, scores 60, non-public 40, decision record 60, open items 80, record 50.

1. **Answer** (two sentences): the decision as the person stated it, the decider and date, counts of the person's criteria met, unmet and not measurable, and the open item that blocks most. No recommendation.
2. **Thesis against the record:** each thesis claim that names a public fact, with the fact and source beside it or `[GAP]`; the company status line from A1 where the thesis assumes the company operates. The person's headings (or "proposed" headings) are used as section labels only in full mode.
3. **Scores and ranking** (only if several options were scored): the person's weights and scores and the `analytics.mcda` value; "arithmetic on your scores, not a decision".
4. **From you (non-public):** labeled, kept apart.
5. **Decision record:** decision, decider, date, attendees, dissent, conditions, all as stated.
6. **Open items:** item · owner the person named for it (or owner not named) · what it blocks · reread date (or "not given").
7. **Full version:** one line offering it, before the record block.
8. **Calls made** (before the record block; not counted in the word cap): each call with its arguments.
9. **Record (the very last line of the answer; nothing follows it, nothing sits between "Record" and "Clears it"):** "Decision record draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Memo under your headings
(each heading: facts with source, retrieval date or row; [PAPER] rows with their DOI)
### Thesis against the record
| Thesis claim (your words) | Public fact | Source and date | Status (fact present, `[GAP]`) |
|---|---|---|---|
### Criteria and scores
| Criterion (your words) | Weight | Option | Your score | Fact behind it, if any |
|---|---|---|---|---|
### Ranking (only what you scored)
| Option | Value | Contributions | Not ranked (why) |
|---|---|---|---|
### Transaction and data flags (from A2; conclusions for your owner)
### From you (non-public)
| Fact | Where you gave it | Used for |
|---|---|---|
### Decision record
| Field | As you stated it |
|---|---|
| Decision | |
| Decider | |
| Date | |
| Attendees | |
| Dissent | |
| Conditions | |
### Open items
| Item | Owner | Blocks | Reread date |
|---|---|---|---|
### Gaps
### Calls made (before the record block)
### Record
Decision record draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
