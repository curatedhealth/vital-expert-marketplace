# Worked run: A1, A2 and B1 on an illustrative forum sitting

Built 20 October 2026 while the library connector was disconnected. The forum log, rule, benefits plan, people and figures are ILLUSTRATIVE (`examples/sample-data/`), not any company's data or judgment. Every number below comes from `scripts/forum_check.py` on those files (`examples/live/forum_check_runs_output.md`). The recomputation uses the same EVIDEM weighted sum as `analytics.mcda`, checked against a saved live response by the sibling skill.

## The request (illustrative)

"Review the 8 July 2026 sitting of our product portfolio board. The rule we confirmed on 30 June 2026 is attached, with the decision log and the benefits plan for the programs we continued. Read as of 20 October 2026."

## A1 Decision record check (short mode)

**Answer:** Product portfolio board, sitting of 8 July 2026. Pass rule: the old method's default, proposed and confirmed by you. 2 of 4 decisions pass. The fail that matters most: Program C was continued with no rule and no rank, recorded only in a slide.

| Item | Decision | Rule | Rank | Decider | Record | Result | Reason |
|---|---|---|---|---|---|---|---|
| A | continue | Rule 2026-09 | 1 | Dana Okafor | board minutes | pass | all four present |
| B | continue | Rule 2026-09 | 2 | Dana Okafor | board minutes | pass | all four present |
| C | continue | none | none | Dana Okafor | steering deck slide 14 | fail | continue with no rule; no rank; lives only in a slide |
| D | stop | Rule 2026-09 | 4 | not named | none | fail | no decider named; stop with no record |

Record check draft. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## A2 Forum score and benefits read (short mode)

**Answer:** Read against Rule 2026-09 (30 June 2026, before the forum): 3 match, 1 drift. Recorded continue items use 15 of your 14 FTE; Program C is the first past it. One benefit is not measurable.

| Item | Value | Rank | Implied by your rule | Decision | Result |
|---|---|---|---|---|---|
| A | 85.00 | 1 | continue | continue | match |
| B | 72.50 | 2 | continue | continue | match |
| C | 65.00 | 3 | not continue (rule silent on stop or delay) | continue | drift: continue beyond the rule |
| D | 60.00 | 4 | not continue | stop | match |

**Benefits (your plan; register fields from the UK Benefits Measurement Guidance Note, May 2021, SP-104, UK public-sector guidance applied by analogy):** A prescriptions per month 1200 to 1500 against 1800, 50% of planned change. B sites activated 4 of 12, 33%; owner not named. C weekly active clinicians 150 against 400: not measurable, baseline not given, review date not given. No threshold given: numbers, no verdict.

**Changes since the forum:** none supplied for these items. If any item rests on a license signed before 1 May 2026, the transition under Regulation (EU) 2026/877 ends 30 April 2027 (SP-137), and the regulation's 20% combined or 30% per-party market share condition (SP-136) sits beside your shares: not given; conclusion for the owner you name for legal.

Forum score draft. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## B1 Review and repair (short mode, with the person's illustrative choices)

**Answer:** 4 findings (2 record fails, 1 drift with capacity overrun, 1 benefit not measurable). You chose corrections for 3; 1 has no owner.

| Finding | Forum's reason | Correction (yours) | Owner | Forum | Date |
|---|---|---|---|---|---|
| C continued beyond the rule, past 14 FTE, record only in a slide | reason not recorded | Correct the decision: C returns to the next sitting against Rule 2026-09 | Dana Okafor | next portfolio board | date not set |
| D stopped with no record or decider | not applicable | Complete the record | owner not named | forum not named | date not set |
| C benefit baseline missing | not applicable | Complete the plan fields | Sam Patel | next portfolio board | date not set |

**Stop:** reversing C's continue stops for the forum's decider as you name them.

Review draft for the owner. Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

Calls made: none live (connector disconnected 20 October 2026). Computations from `scripts/forum_check.py` on `examples/sample-data/`.
