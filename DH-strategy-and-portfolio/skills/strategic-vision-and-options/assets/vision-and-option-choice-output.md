# Output format: vision and option choice

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/options_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Build lines 3 and 4 from `scripts/options_check.py rank` and `tornado` output; do not recount by hand. Budget in words: answer 60, vision 60, ranking 110, sensitivity 70, decision 60, open items 40, record 45.

1. **Answer** (two sentences): the vision as written, the order on your scores with the closest swap point, the input that moves the result most on your ranges, and the decision as stated (or "decision not given"). No winner named by the model.
2. **Vision and objectives:** vision verbatim; each objective with SMART elements present or "not given" (HM Treasury Green Book, 5 February 2026, SP-092; UK public-sector guidance).
3. **Ranking on your scores:** Option · Value · Largest contributions · Not ranked (why, with its tie scores from the script); swap points in one line each; if an unranked option's tie score lies inside 0 to 4, say which empty cell decides the top, never that the order holds; "arithmetic on your scores, not a decision".
4. **Sensitivity on your inputs:** Parameter · Range (yours or default R1) · Output range · Flags.
5. **Decision record:** decision, decider, date, dissent, conditions, as stated.
6. **Open items:** item · owner the person named (or owner not named) · date (or "not given").
7. **Calls made**, then one line offering the full version.
8. **Record (the very last line, nothing after it):** "Vision and option record draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Vision (your words)
### Objectives against the SMART elements (UK public-sector guidance, SP-092)
| Objective | Specific | Measurable | Achievable | Realistic | Time-limited |
|---|---|---|---|---|---|
### Scoring set
| Criterion (your words) | Weight | Weighting method | Who scored, when | ISPOR check (SP-074 to SP-081 [WF]) |
|---|---|---|---|---|
### Ranking (only what you scored)
| Option | Value | Contributions | Not ranked (why) |
|---|---|---|---|
### Tie scores for unranked options (arithmetic on your scores; the missing score stays yours)
| Option | Sum on criteria scored | Missing criterion | Score at which it ties each ranked option |
|---|---|---|---|
### Swap points
### Sensitivity on your inputs
| Parameter | Base | Range (yours or default) | Output low to high | Swing | Flags |
|---|---|---|---|---|---|
### Optimism bias bounds you asked about (UK public-sector guidance; the uplift you apply is yours)
| Project type (yours) | Upper bounds, duration and capital expenditure | Lower bounds | Method and age | Source and rows |
|---|---|---|---|---|
### Input sheet for an NPV or probability you asked for (every cell "not given" until you fill it)
| Option | Costs and timing | License fees or royalties | Uptake | Price | Discount rate | Optimism bias uplift | Probability and counting basis |
|---|---|---|---|---|---|---|---|
### Benchmarks you asked about (context, never your probability)
| Figure | Counting method and population | Source and rows (DOI for [PAPER]) |
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
| Item | Owner | Blocks | Date |
|---|---|---|---|
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Vision and option record draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

