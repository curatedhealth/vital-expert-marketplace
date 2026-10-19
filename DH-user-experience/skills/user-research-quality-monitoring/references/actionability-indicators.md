# Insight actionability indicators

Interpretive reference for A2 and B1. It defines indicators the person's own logs can produce, and what each can and cannot show. No indicator carries a target: thresholds come from the person. The indicators make the register's three old checks measurable: trace a shipped change to a session record; mark a change with no stop as not from this study; give every repeated stop an owner and a date for its action or refusal.

## Indicators from the person's logs

| Indicator | Computed from | What it can show | What it cannot show | Basis |
|---|---|---|---|---|
| Decision status | Insight log `decision` (action, refusal, open) | How many insights have an action, a refusal, or nothing written | Whether the decision was right | Register method (B1 of the sibling) |
| Open insight age | `raised_on` to the as-of date, for open insights | How long stops sit without a decision | Why | Register "Do not leave the stop only in a recording" |
| Time to decision | `raised_on` to `decided_on` for actions and refusals | How long decisions take (median, longest) | Quality of the decision | Register method |
| Refusals without a reason | Refusal rows with no `decision_ref` | Refusals nobody can audit | Whether the refusal was justified | Register method ("refuse it with a reason") |
| No owner | Rows with no `owner` | Insights nobody holds | Who should hold them | Owner rule |
| Actions not shipped | Actions with no change shipped by the as-of date | Decisions that have not reached users | Whether the change worked | Register method ("name the release") |
| Changes not traced | Shipped changes with no `insight_id` | Work credited to research that the record does not support, or simply not research-driven | Whether the change was good | Register "Do not attribute a roadmap item to research after the fact" |
| Broken links | Changes citing an insight id missing from the log | Gaps in the log | | Register method |
| SUS across rounds | SUS file with `round` | Difference of means per round, with n | Significance (no test in the sources); safe use of critical tasks | UX-M-07; see "SUS" below |

`scripts/research_log.py trace INSIGHTS.csv --as-of DATE --changes CHANGES.csv` computes the first eight; `sus FILE --by round` the last. "Overdue" means past the person's own rule, never a model default.

## Critical-task stops

Stops on tasks the owner flagged critical are counted apart. FDA gives severity of harm more weight than probability (UX-US-32), so one such stop open is reported whatever the overall numbers. Whether it is a use error, and whether a fix is acceptable, is the owner's (UX-US-27, UX-US-42).

## SUS

Scoring as restated by Hyzy et al. 2022 ([PAPER], DOI 10.2196/37290; cite the row id and the DOI whenever an answer uses these rows): odd items minus 1, 5 minus even items, sum times 2.5 (UX-M-07). Context figures: 68 (SD 12.5) as cited by Hyzy et al. (UX-M-08); 76.64 (SD 15.12) across 117 scores for 114 digital health apps, 2011 to 2021, and 68.05 (SD 14.05) without physical-activity apps (UX-M-09); the authors find the 68 benchmark suitable for digital health apps, one meta-analysis with its own limits (UX-M-10). Context only, never a target. No adjective bands (not read, `[GAP]`). When rounds have different respondents, say so.

## Rules for reading the numbers

1. Report each number with its denominator and its as-of date.
2. An insight counts once, under its latest decision.
3. A change traced to an insight shows the link exists, not that the change came from the stop; check the stop id and the participants' words when the person asks for an action trace.
4. Never average studies or teams into one score.
5. Fewer open insights is not better research: a study that raised few insights may have asked a narrow question. Say what the numbers cannot show.

## Gaps

- No sourced benchmark for time to decision, open insight age or share of insights actioned `[GAP]`. These are the person's rules.
- No sourced method for testing a SUS change between rounds `[GAP]`.
