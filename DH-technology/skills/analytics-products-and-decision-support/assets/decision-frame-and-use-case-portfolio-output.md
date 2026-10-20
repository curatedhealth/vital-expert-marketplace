# Output format: decision frame and use-case portfolio

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/metric_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Build the ranking line from `scripts/metric_check.py rank` output; do not recount by hand. Budget in words: answer 60, frame 90, questions and route 70, bet and value case 90, rank 80, record 45.

1. **Answer** (two sentences): the decision and its two actions as you stated them (or "decision not given"), the first gap that stops later work, whether the current cost is sourced or `[GAP]`, and for a set the order on your rule with the closest tie point. No use case chosen by the model.
2. **Decision frame:** decision maker · choice · action if yes · action if no · analysis not done · (AI only) intended purpose and setting (NIST AI RMF 1.0, January 2023, DA-10) and non-AI alternative (DA-15), each in your words or "not given".
3. **Questions that change the action:** Question · Data that answers it or `[GAP]` · Stops later work (yes or no). Shape and first output in one line; method route by pack and skill.
4. **Bet and value case:** the bet, its metric, comparison and window; discovery evidence (observed or "step not observed"); current cost with your source or `[GAP]`; expected change (your range or `[GAP]`); implementation cost elements "not given" until supplied (Proctor 2011, CS38, DOI 10.1007/s10488-010-0319-7).
5. **Rank on your rule** (sets only): your rule verbatim with its date; Use case · Score · Note; the one placed last; tie points; "arithmetic on your scores, not a decision".
6. **Calls made**, then one line offering the full version.
7. **Record (the very last line, nothing after it):** "Decision frame and portfolio draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Decision frame (your words)
| Element | As you stated it |
|---|---|
| Decision maker | |
| Choice | |
| Action if yes | |
| Action if no | |
| Analysis not done | |
| Intended purpose and setting (AI only, DA-10) | |
| Non-AI alternative considered (AI only, DA-15) | |
| Risks not measured (AI only, DA-12) | |
### Questions that change the action
| Question | Data that answers it | Stops later work | Source and rows |
|---|---|---|---|
### Solution shape and method route
### Bet and discovery evidence
### Value-case sheet (every cell "not given" until you fill it)
| Element | Your figure | Your source | Source and rows |
|---|---|---|---|
| Current cost (time, errors or money) | | | |
| Expected change (range) | | | |
| Implementation cost (CS38) | | | |
| Staffing, training, IT infrastructure (CS63, NHS context) | | | |
### Value arithmetic on your inputs (scenario-modeler; not a forecast)
### Analytics portfolio for your period
| Product | Decision served | Owner | Now, next, later | Holding dependency | People needed |
|---|---|---|---|---|---|
### Rank on your rule (only what you scored)
| Use case | Score | Note | Source and rows |
|---|---|---|---|
### Tie points (arithmetic on your scores)
### Funding record as you stated it
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Decision frame and portfolio draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
