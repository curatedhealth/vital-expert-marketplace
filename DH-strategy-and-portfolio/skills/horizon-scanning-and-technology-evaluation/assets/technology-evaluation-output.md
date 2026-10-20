# Output format: technology evaluation and readiness

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with `python3 scripts/horizon_helpers.py words ANSWER.md` (counts the whole answer except the calls list, and leaves out the Source, Rows and Retrieved columns); without code execution, count the same way by hand. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Budget in words: answer 70, fact table 200, limits 60, decisions 40, record 50. Every fact names its source in plain words with its date, then the row id ("FDA 510(k) K261317, decided 14 May 2026"; "Pear 8-K, filed 7 April 2023 (SP-156) [WF]"); never a row id alone.

1. **Answer** (two or three sentences): per technology, its record in one line, the proposed TRL quoted in the EU wording, and the fact that most limits a verdict. The verdict is yours.
2. **Fact table:** Technology · Register record (identifier, date) · Proposed TRL (EU wording, row) · Evidence on record (count, type) · Conditions that apply (rows) · Your score (if given).
3. **Limits:** lookup misses, fields not stored, [WF] or abstract-only rows relied on. For a UK or England use, one line: MHRA AI Airlock is a regulatory sandbox (UK-06), phase 3 announced 6 October 2026 (UK-07); innovator reports are not MHRA guidance (UK-08); eligibility is the regulatory owner's.
4. **Company status** of each named maker: the status already read (`references/company-status.md` section 6) cited by filing or register name and date, or "Status: [GAP]: not read" with the filings to open. The product's current FDA listing holder is stated apart from the company that was authorized.
5. **For you to decide:** fit for purpose, feasibility, the level, with the facts behind each. Any example criteria are labeled "proposed".
6. **Calls made**, then one line offering the full version.
7. **Record (the very last line):** "Technology fact sheet draft. Levels proposed; verdicts and scores yours. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Technology and intended use (as you state it)
### What kind of intervention (WHO classification axes; codes `[GAP]` unless looked up)
### Register record
| Register | Product (as stored) | Maker (as stored) | Identifier | Pathway or class | Decision date | Status | Source | Retrieved |
|---|---|---|---|---|---|---|---|---|
### Current FDA listing holder (if different from the maker above)
| Product | Authorized to | Listed today by | Source |
|---|---|---|---|
### Proposed readiness level
| Proposed TRL | EU wording (verbatim) | Fact behind it | Rows |
|---|---|---|---|
The level is proposed for you to confirm; it is not a regulatory status or a clinical finding. NASA levels 7 to 9 assume space and flight (SP-035).
### Evidence on record (publication and trial signals, not findings)
| Record | Year | Type as stored (library label is a draft) | Trial id | Source |
|---|---|---|---|---|
### Conditions and standards that would apply
| Condition or standard | What it asks | Rows |
|---|---|---|
### Early clinical and regulatory routes that exist
| Route | Facts and status as read | Rows |
|---|---|---|
Eligibility is for the owner you name for regulatory matters.
### Feasibility: facts per your criteria
| Criterion (yours, or "proposed") | Facts that bear on it (ids) | Your score | Question raised |
|---|---|---|---|
### Company status (named makers)
| Company | Status (filing or register, date, row) | What it does not mean |
|---|---|---|
### Gaps
| Fact | Class | Next step |
|---|---|---|
### Calls made
### Record (the very last line)
Technology fact sheet draft. Levels proposed; verdicts and scores yours. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
