# Output format: scenarios, implications and choice

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with `python3 scripts/horizon_helpers.py words ANSWER.md` (counts the whole answer except the calls list, and leaves out the Source, Rows and Retrieved columns); without code execution, count the same way by hand. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Budget in words: answer 70, scenarios 120, implications 80, ranking 80, decisions 40, record 50. Every fact names its source in plain words with its date, then the row id ("FDA 510(k) K261317, decided 14 May 2026"; "Pear 8-K, filed 7 April 2023 (SP-156) [WF]"); never a row id alone.

1. **Answer** (two or three sentences): the scenarios in a phrase each, the implication that bears most on your current play, the order of your scored options with the nearest swap point, and the decisions that are yours. No probabilities.
2. **Scenarios:** Scenario · Driver states (yours or proposed) · Assumptions (signal id or "yours") · What would be observed.
3. **Implications for your play:** Scenario · Part of the play it would touch · Signal ids.
4. **Your scores, ranked** (only if you scored): Rank · Option · Value (0 to 100, arithmetic shown) · Nearest swap (criterion, weight, from `swap`). "Your scores, computed; not a choice." Any "what would change the order" is computed, never estimated.
5. **Stops:** licensing or partner facts flagged for the owner you name, each threshold beside your own figure ("threshold X (row). Your figure: [as given, or not given]. For your legal owner."), with every flag the rows support (data licensing, GDPR for training data); benchmark requests answered as context only.
6. **For you to decide:** each with its facts; owners as you named them or "owner not named"; dates as set or "not given".
7. **Calls made**, then one line offering the full version.
8. **Record (the very last line):** "Scenario draft for the owner. Rankings, where shown, are your scores; no forecast. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Inputs as you gave them (drivers, current play, test of disruptive, options, criteria, weights, scores)
### Scenarios
| Scenario | Driver states | Assumptions | Signal ids or "yours" | What would be observed (watch items) |
|---|---|---|---|---|
### Implications for the current play
| Scenario | Evidence plan | Pathway | Data access | Partner | Timing | Rows or signal ids |
|---|---|---|---|---|---|---|
### Disruption read (your test)
| Signal or lead | Would change | Status (signal or lead) |
|---|---|---|
### Criteria completeness (asked before ranking, SP-076)
| Factor not in your criteria (proposed) | Why it may matter | Rows |
|---|---|---|
### Your scores, ranked (analytics.mcda or rice)
| Rank | Option | Value | Arithmetic on your scores |
|---|---|---|---|
### Where the order would swap (scripts/horizon_helpers.py swap)
| Pair | Criterion | Current weight | Swap at | Direction |
|---|---|---|---|---|
### Sensitivity on your inputs (only if asked)
| Parameter | Your range | Low output | High output | Flags |
|---|---|---|---|---|
### UK optimism bias values (only if you apply them; UK public-sector guidance, 2003 document on 2002 data)
| Project type | Upper bound | Your mitigation | Adjusted figure (arithmetic) | Rows |
|---|---|---|---|---|
### Benchmarks as context (only if asked)
| Figure | What it counted, method, dataset | Rows and DOI |
|---|---|---|
Drug development figures; no digital health success rate in the sources. Not your probability.
### Partner, license or deal facts flagged for your legal owner
| Fact or threshold (as the source states it) | Your figure (as given, or not given) | Rows |
|---|---|---|
### For you to decide
| Decision | Facts behind it | Owner (as named) | Date (as set, or not given) |
|---|---|---|---|
### Gaps
### Calls made
### Record (the very last line)
Scenario draft for the owner. Rankings, where shown, are your scores; no forecast. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
