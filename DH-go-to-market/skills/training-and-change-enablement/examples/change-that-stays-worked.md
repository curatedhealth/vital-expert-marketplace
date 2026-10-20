# Worked example: B1 change that stays

Run on 19 October 2026. The scenario, scores and weights are illustrative: they were typed for the live measurement and are presented here as the example person's. The ranking is a real library call (`live/mcda_enablement_options.json`); the swap points come from the QMS design skill's helper run on that saved call (`live/mcda_swap_points.md`). The session figures come from `scripts/session_coverage.py` on the illustrative log (`sample-data/run_site_role.txt`).

**Request:** "South site nurses still keep the phone log spreadsheet next to the remote monitoring alert worklist. We are weighing three things: change the worklist screen so the alert note replaces the log, a refresher session at 60 days, or train-the-trainer with ward champions. Our scores are below, weights 0.4 on use-error risk addressed and 0.2 on each of users reached, effort avoided and resistance to decay. The South nurse manager checks the log after 30 days. What first?"

| Option | Use-error risk addressed | Users reached | Effort avoided | Resistance to decay |
|---|---|---|---|---|
| Workflow change in the worklist screen | 4 | 3 | 1 | 4 |
| Refresher training at 60 days | 2 | 3 | 3 | 1 |
| Train-the-trainer with ward champions | 2 | 4 | 2 | 2 |

**Calls and runs**

1. `scripts/session_coverage.py sample-data/illustrative_sessions.csv --as-of 2026-10-19`
2. `analytics.mcda` with the three options and the weights above (counted)

## Answer (short mode)

**The change:** stop the phone log spreadsheet at South. The South nurse manager checks after 30 days (your values). What happens if it is still in use: not stated; please say.

**Your scores rank the workflow change first: 80, then train-the-trainer 60, then the refresher 55.** The largest contribution to the first is use-error risk addressed (40 of 80). The order of the top two would reverse only if users reached, or effort avoided, carried a weight of 0.56 instead of 0.20. Train-the-trainer and the refresher swap if effort avoided reaches 0.33.

**Facts that move the choice**

- Design comes first in FDA's order of risk controls; training is last (UX-US-33). Training depends on memory and can decay (CS77, CS78).
- If the product is a device, the worklist change and any training change may need your regulatory owner first (UX-US-49).
- Train-the-trainer means training designated clinicians to train others (CS45). Your South log shows 2 designated trainers among 12 nurses, 8 of 12 completed the task once, and 2 attended without completion recorded. Both designated trainers completed the task once (SNU01, SNU02).
- No row gives an effect size for any of the three options.

**What to do first:** confirm with the design owner whether the worklist change is possible, and with the regulatory owner whether it or a training change touches validated use. The refresher and champion choices depend on that answer.

**Stops:** the choice (owner not named; please say); the screen change (design owner, and regulatory owner if the product is a device); any payment to ward champions (compliance owner: CP-US-01, CP-US-09).

**Gaps:** what happens if the log is still used after 30 days; device status `[GAP]`.

**Record:** Change plan draft. Scores, weights and the choice are yours; the ranking is not a recommendation. Uncleared. AI-assisted.

The full version adds the facts table per option, the robustness table and the dependency sequence.

## What this example shows

- The person's check window and checker were used; the missing consequence stayed blank.
- The design option sat beside the training options, with its rows.
- The ranking came from the person's scores and was reported with its swap points, never as a recommendation.
- The champion option carried the fraud and abuse stop because the person might pay champions.
