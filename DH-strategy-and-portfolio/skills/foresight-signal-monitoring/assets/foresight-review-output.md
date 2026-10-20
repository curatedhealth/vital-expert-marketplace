# Output format: foresight review

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with `python3 scripts/foresight_check.py --words ANSWER.md` (counts the whole answer except the calls list, and leaves out the Source, Rows, Retrieved and Evidence columns); without code execution, count the same way by hand. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Budget in words: answer 70, rules table 120, misses 120, feedback 60, record 50. Every fact names its source in plain words with its date, then the row id ("FDA 510(k) K261317, decided 14 May 2026"; "Pear 8-K, filed 7 April 2023 (SP-156) [WF]"); never a row id alone.

1. **Answer** (two or three sentences): per pass rule, met or not met with its counts and denominator, and what would change if the proposed outcomes were confirmed (script `--if-confirmed`, computed); the misses and their owners as you named them; the decision that is yours. No benchmark, no rating of people.
2. **Pass rules:** Rule (your words) · Counts behind it · Met or not met.
3. **Misses:** Id · Miss · Owner (as named, or owner not named) · Reread (as set, or not given) · Follow-up (your rule, or "not given; your call"). Add one line listing every row flagged O1 (owner not named in the log), misses or not, and ask who owns it. Where the log names a different owner than the one you named for that kind of row (O4), show both names and ask which applies. A follow-up rule relative to the review stays in your words; no calendar date unless you gave the review date.
4. **Proposed feedback** into the next scan, labeled proposed.
5. **For you to decide:** each with its facts.
6. **Calls made**, then one line offering the full version.
7. **Record (the very last line):** "Foresight review draft for the owner. Rules, outcomes and owners yours. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Rules as you gave them
### Pass rules applied (scripts/foresight_check.py --pass-rule)
| Rule | Metric values | Denominator | Met |
|---|---|---|---|
### Misses and failed checks
| Id | What missed | Evidence | Owner (as named; both names if the log differs) | Reread date (as set, or not given) | Follow-up (your rule, in your words) |
|---|---|---|---|---|---|
### Rows with owner not named in the log (O1), misses or not
### Proposed outcomes not yet confirmed (not counted; result if confirmed, from `--if-confirmed`)
### Proposed feedback into the next scan
### For you to decide
### Gaps
### Calls made
### Record (the very last line)
Foresight review draft for the owner. Rules, outcomes and owners yours. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
