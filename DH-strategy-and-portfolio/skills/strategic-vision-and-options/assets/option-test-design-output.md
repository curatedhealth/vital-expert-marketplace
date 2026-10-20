# Output format: option test design

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/options_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Budget in words: answer 60, test 60, plan elements 110, routes 90, what it will not show 50, record 45.

1. **Answer** (two sentences): what the test asks, whether a rule exists written before the start, the route the sources describe for the market, and the element that most limits what the test can show.
2. **The test (your words):** option, question, prototype or concept, population, market.
3. **Plan elements:** Element · Yours (or "not given") · Status (present, not given, written after start) · Source and rows. Purpose, endpoint, success criterion, decision rule, date written, sample.
4. **Routes for your market:** Route · What the source states · Source and rows (source name and date in plain words, row id after). Only the market in the request; "whether it applies: dh-regulatory-and-quality regulatory-pathway-and-classification".
5. **What a result will and will not show:** one line each.
6. **Readout** (only for a finished test): result against your rule, in your words: met, not met, or not readable, and why.
7. **Calls made**, then one line offering the full version.
8. **Record (the very last line, nothing after it):** "Option test plan draft. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### The test (your words)
### Plan elements
| Element | Yours | Status | Borrowed wording, if any | Source and rows (DOI for [PAPER]) |
|---|---|---|---|---|
### Routes the sources describe for your market
| Route | What the source states | Date or count with its date | Source and rows |
|---|---|---|---|
### What a result will and will not show
### Readout against your rule (finished tests only)
| Rule (your words, date written) | Result (your data) | Met, not met, not readable | Why |
|---|---|---|---|
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Option test plan draft. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

