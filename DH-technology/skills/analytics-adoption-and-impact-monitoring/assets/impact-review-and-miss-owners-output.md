# Output format: impact review and miss owners

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/adoption_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Budget in words: answer 60, rules 60, misses 150, limits 60, decisions 60, record 45.

1. **Answer** (two sentences): counts of units met, missed and not measurable against your rules; the misses by name; how many have an owner and a recheck date; the flag that most limits the review. No verdict.
2. **Your rules:** one line per rule, verbatim with its date; units without a rule listed.
3. **Misses:** Unit · Fact behind it · Owner (yours, or owner not named) · Recheck date (yours, "not given", or "stopped").
4. **Limits:** not measurable or not comparable, one line each (no denominator, no comparison, not instrumented, rule written after the result).
5. **For you to decide:** each with its facts; keep, change the insertion or stop is yours.
6. **Calls made**, then one line offering the full version.
7. **Record (the very last line, nothing after it):** "Impact review draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Your pass rules (verbatim, numbered, with dates)
### Results against your rules
| Unit | Your rule | Result | Met, missed, not measurable | Flags |
|---|---|---|---|---|
### Misses, owners and recheck dates
| Unit | Fact behind it | Owner | Recheck date or stopped | Follow-up (your words) |
|---|---|---|---|---|
### Not measurable or not comparable
### Follow-up options ranked on your scores (only if you scored them; arithmetic, not a decision)
### For you to decide
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Impact review draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
