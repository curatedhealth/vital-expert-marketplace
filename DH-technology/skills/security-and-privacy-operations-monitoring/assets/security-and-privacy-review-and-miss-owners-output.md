# Output format: security and privacy review and miss owners

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/secops_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Budget in words: answer 60, rules 60, misses 160, decisions 70, record 50.

1. **Answer** (two sentences): counts of units met, missed and not measurable against your rules; the misses by name; how many have an owner and a recheck date; the flag that most limits the review. No overall verdict.
2. **Your rules:** one line per rule type, verbatim; units without a rule listed.
3. **Misses:** Unit · What missed · Fact behind it · Owner (yours, or owner not named) · Recheck date or fix version (yours, or "not given").
4. **Consent misses with two owners:** text owner · job owner · which changes · who moves first (yours, or "not given").
5. **For you to decide:** each with its facts.
6. **Calls made**, then one line offering the full version.
7. **Record (the very last line, nothing after it):** "Security and privacy review draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Your pass rules (verbatim, numbered)
### Results against your rules
| Unit | Your rule | Result | Met, missed, not measurable | Flags |
|---|---|---|---|---|
### Misses, owners and recheck dates
| Unit | What missed | Fact behind it | Owner | Recheck date or fix version | Follow-up (your words) |
|---|---|---|---|---|---|
### Consent misses with two owners
### Not measurable or not comparable
### For you and your owners to decide
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Security and privacy review draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
