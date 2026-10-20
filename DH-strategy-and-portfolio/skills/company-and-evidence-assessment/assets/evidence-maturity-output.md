# Output format: evidence maturity read

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with a tool (`python3 scripts/profile_table.py --count ANSWER.md`, which drops the calls list and source columns), not by estimate. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question, the "Full version on request" line. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

Sources and status in every answer: each fact cites its source name and date in plain words, then the row id ("Pear 8-K, 7 April 2023 (SP-156 [WF])"; "BfArM DiGA page, as of 9 September 2026 (DE34)"; "VITAL library screen_market, saved 19 October 2026"); never a row id alone. Company status for a company in `references/named-company-status.md` comes from those rows, with what each form does not mean, and a product's current FDA listing holder is stated apart from the company that was authorized; "Status: [GAP]: not read" only where no row covers the company. Rows the research file marks as an inference carry "(inference)" every time. A date, owner or threshold the person did not give is "not given", with the question to ask.

## Short mode (default for a direct question)

1. **Answer:** the library score with its points ("67, 60 of 90 assessable points"), the component that holds it back, what is excluded, and the proposed framework level with its one main limit. Three sentences.
2. **The library's score (a convention, not a level):** table Component · Points · Inputs · Note, from `scripts/profile_table.py`; then the formula check and the excluded components ("excluded, not zero"). One line: "A stated convention for comparing documented evidence, not a framework level, a rating or a valuation."
3. **Proposed framework level:** Framework · Why it fits · Proposed level or tier · Its own limits · Rows. In the Rows cell, every [PAPER] row carries its DOI beside it ("DL-112, DOI 10.1038/s41746-023-00836-5"; "CV159, DOI 10.1038/s41746-020-0260-4"). Labeled "proposed, for you to confirm".
4. **What would change the read:** at most three items (a graded evidence review, results posted, a register the library does not load), each with its route.
5. **Gaps and stops:** recall flags and safety events from the saved `compare_portfolio` result where safety bears on the question (`none_found`: not proof of none); status line only if the question turns on it ("Status: [GAP]: not read" unless a filing or register was read); "no registered study linked in the loaded sources" where it applies; grading routes to `dh-clinical-development` literature-and-real-world-evidence-review.
6. **Full version:** one line offering it, before the record block.
7. **Calls made** (before the record block; not counted in the word cap): each call with its arguments and retrieval date.
8. **Record (the very last line of the answer; nothing follows it, nothing sits between "Record" and "Clears it"):** "Evidence maturity read draft for OWNER. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### The library's evidence maturity score
| Component | Points | Maximum | Inputs | Rule as returned |
|---|---|---|---|---|
### Formula check and excluded components
### The tool's own limits and risk flags
### Framework chosen and why
### Proposed level
| Framework | Proposed level or components | Basis | Limits | Rows (DOI beside each [PAPER] row) |
|---|---|---|---|---|
### Paper claims checked (Verify, with passage)
### What would change the read
### Gaps
### Calls made (before the record block)
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
