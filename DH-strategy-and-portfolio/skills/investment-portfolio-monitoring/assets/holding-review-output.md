# Output format: holding review

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with `python3 scripts/portfolio_watch.py words ANSWER.md` (it leaves out the calls list and table source columns), not by estimate. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question, the "Full version on request" line. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

Sources and status in every answer: each fact cites its source name and date in plain words, then the row id ("Pear 8-K, 7 April 2023 (SP-156 [WF])"; "BfArM DiGA page, as of 9 September 2026 (DE34)"; "VITAL library screen_market, saved 19 October 2026"); never a row id alone. Company status for a company in `references/named-company-status.md` comes from those rows, with what each form does not mean, and a product's current FDA listing holder is stated apart from the company that was authorized; "Status: [GAP]: not read" only where no row covers the company. Rows the research file marks as an inference carry "(inference)" every time. A date, owner or threshold the person did not give is "not given", with the question to ask.

## Short mode (default for a direct question)

1. **Answer:** which holdings miss which of the person's rules, who owns each follow-up, and the stop that applies if any. Two sentences.
2. **Rule check:** table Holding · Rule (numbered, verbatim) · Met, not met, triggered (from the person, confidential) or cannot tell · Fact behind it (with date and source) · Owner (person's words or "owner not named") · Reread date (or "not given").
3. **Next reads by dependency:** at most five lines. A holding whose filings in the store end before the asked date: say so ("none after DATE in the store") rather than asking to open them.
3b. **Status:** per company, as the record states (form, item, date, URL, read date, and what it does not mean: a Form 15 or 25 is not dissolution, DL-144, DL-149), or "`[GAP]`: not read" with the filings to open (8-K Items 1.03, 2.01, 3.01, 5.01; Form 25; Form 15; register). Never from press or memory (`references/company-status.md`).
4. **Rules an event touches (if any):** rule facts with rows and dates, routed to the owner the person names for legal or compliance questions (or owner not named); never "clear".
5. **Follow-up order (only if the person scored work):** RICE inputs beside scores; "ranks work, not holdings".
6. **Draft question for the company (only if asked):** labeled "draft for the owner", public record only. Declined LP, board or company wording: the facts-only version labeled "draft for the owner" (what was checked, source and date, what was not checked; no finding). **Owner:** as the person named, in their words, or "Owner not named: who clears this?"
7. **Full version:** one line offering it, before the record block.
8. **Calls made** (before the record block; not counted in the word cap): list.
9. **Record (the very last line of the answer; nothing follows it, nothing sits between "Record" and "Clears it"):** "Holding review draft for OWNER. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Rules (the person's, numbered)
### Rule check per holding
| Holding | Rule | Status | Fact, date, source | Owner | Reread | Rows |
|---|---|---|---|---|---|---|
### Status per holding (references/company-status.md)
### Next reads by dependency
### Transaction and data rule facts (for the owner the person names for legal or compliance questions)
### Follow-up order (person's RICE inputs)
### Drafts for the owner
### Gaps
### Calls made (before the record block)
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
