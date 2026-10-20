# Worked example: A2 implementation outcomes

Run on 19 October 2026. The site and milestone files are illustrative, written for this example (`sample-data/sites.csv`, `sample-data/milestones.csv`): a remote monitoring product deployed across six clinics of one customer, two of them pilots. The figures below are the script's output on those files (`outcomes_run_2026-10-19.md`). The Verify calls are real (`live/verify_proctor.json`).

**Request:** "How is the rollout going? Attached: our site file and the milestone tracker. We agreed 5 readings per active patient per week at commissioning. Our target is 50 percent of eligible patients active at every live clinic."

**Calls and runs**

1. `python3 scripts/implementation_outcomes.py sample-data/sites.csv --milestones sample-data/milestones.csv --as-of 2026-10-19`
2. Not needed for the answer; run once to show the definition check: `verify.qualify_source {doi: "10.1007/s10488-010-0319-7"}` (gold) then `verify.check_claim` with the CS39 passage ("supported"; passage read and states the same formula).

## Answer (short mode)

**Against your target of 50 percent of eligible patients active at every live clinic: met at Clinic A only (66.9 percent); missed at Clinic B (40.0), Clinic C (42.0) and Clinic D (20.0).** As of 19 October 2026.

| Site | Patient penetration (CS39) | Provider penetration (CS39) | Usage vs agreed 5 per week (CS61) | Go-live slippage |
|---|---|---|---|---|
| Clinic A (pilot) | 281/420 = 66.9% | 11/12 = 91.7% | 92% | 0 days |
| Clinic B (pilot) | 152/380 = 40.0% | 6/10 = 60.0% | 62% | 28 days |
| Clinic C | 214/510 = 42.0% | 9/14 = 64.3% | 84% | 14 days |
| Clinic D | 58/290 = 20.0% | 3/8 = 37.5% | 40% | 63 days |
| Clinic E | not live | not live | not live | 42 days past agreed date, not live |

Pooled patient penetration 705/1600 = 44.1 percent (site range 20.0 to 66.9); shown beside the sites, not as a score. Setting adoption: 5 of 6 clinics approached agreed or went live (CS28).

**Fidelity to plan (milestones done by their baseline date, CS9):** Clinic A 5 of 5; Clinic B 1 of 6, with 5 re-baselined; Clinic C 1 of 5; Clinic D 0 of 6, every core milestone late (median 52.5 days); Clinic E 2 of 5, with day-one workflow configuration open 70 days past its baseline. Clinic B's results interface to the EHR is open 196 days past baseline (not a core item).

**What it means for you:**
- Penetration is an implementation outcome and comes before any clinical result (CS32): outcome data from Clinic D would describe a fifth of its eligible patients.
- At Clinic E, training and go-live follow configuration in the plan, so their baseline dates have passed too.

**Data checks:** none flagged. Clinic F has only been approached: no data `[GAP]`.

**Record:** Outcome read on your data. Uncleared. AI-assisted.

The full version adds the definitions table, the late-milestone list and months since go-live (Clinic A 7, Clinic B 6, Clinic C 4, Clinic D 2).

## What this example shows

- One target from the person produced verdicts for that measure only; everything else is reported without a verdict.
- Every figure names its definition; pooled figures sit beside per-site figures.
- No cause is given for Clinic D; hypotheses belong to B1.
