# Output format: release gate and miss owners

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/delivery_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Budget in words: answer 60, rules 60, failed elements 150, limits 50, decisions 50, record 50.

1. **Answer** (two sentences): counts of units passed, failed and not readable against your rules; blocking failures by name; how many failures have an owner and a recheck date; the flag that most limits the review. No go or no-go.
2. **Your rules:** one line per rule, verbatim; units without a rule listed.
3. **Failed elements:** Unit · Element · Blocks release (yours) · Owner (yours, or owner not named) · Recheck date (yours, "not given", or "stopped").
4. **Limits:** units without a rule, cases not on the candidate build, closed without evidence, build id missing; one line each.
5. **For you to decide:** go or no-go; accept or fix each non-blocking miss and who accepts it; rules to reset (with the date written); units to stop.
6. **Calls made**, then one line offering the full version.
7. **Record (the very last line, nothing after it):** "Release gate review draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Your pass rules (verbatim, numbered)
### Results against your rules
| Unit | Element | Your rule | Result | Blocks release | Flags |
|---|---|---|---|---|---|
### Failed elements, owners and recheck dates
| Unit | Element | Fact behind it | Owner | Recheck date or stopped | Follow-up (your words) |
|---|---|---|---|---|---|
### Gate record (build id, blocking elements, named acceptor, decision: yours)
### For you to decide
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Release gate review draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
