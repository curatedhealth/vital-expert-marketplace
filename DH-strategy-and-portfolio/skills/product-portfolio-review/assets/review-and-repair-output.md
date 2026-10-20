# Output format: review and repair

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. Count with `python3 scripts/forum_check.py words ANSWER.md`.

## Short mode (default for a direct question)

1. **Answer:** findings n (record fails, drifts, capacity, benefits) · corrections you chose n · findings with no owner or no forum n · the finding that leaves a rule and a decision in conflict.
2. **Repairs:** Finding · Forum's reason (verbatim, or "reason not recorded") · Correction (yours; or options labeled "proposed") · Owner (as you named, or owner not named) · Forum that shows it (yours, or "forum not named") · Date (yours, or "date not set").
3. **Stops:** reversals, capacity changes, licensing findings for the owner you named for legal (facts by source name and date, then row), external wording.
4. One line offering the full version.
5. **Record:** "Review draft for the owner. Corrections, owners, forums and dates are yours." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

Calls made (after the record line).

## Full mode

### Findings
From the record check and the forum score, each with its evidence.

### Options per finding
| Finding | Correct the decision | Correct the rule | Record the reason (dated override for that decision; rule's weights, scores and capacity unchanged) | What each would mean |
|---|---|---|---|---|
All options labeled "proposed".

### Repairs chosen
| Finding | Correction (yours) | Owner | Forum | Date | Condition |
|---|---|---|---|---|---|

### Stops for the accountable owner

### Record
Review draft for the owner. No person judged. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
