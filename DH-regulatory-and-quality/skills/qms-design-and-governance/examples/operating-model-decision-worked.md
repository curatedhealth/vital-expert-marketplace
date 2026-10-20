# Worked example: B1 operating model decision

Live connector call on 19 October 2026. The person, their markets and their scores are written for this example; the ranking and the facts are real (connector response and research rows).

**Request:** "We are a 40-person SaMD company. Our product is class II in the US per our regulatory lead, and we plan the EU and Canada next. Should we run one global QMS with MDSAP, one without, or separate US and EU systems? Here are our scores (0 to 4, higher is better) and weights." The person gave four criteria: markets served (0.35), audit burden avoided (0.25), build effort avoided (0.20), speed to first market (0.20), and named their CEO as the accountable owner.

**Calls made**

1. `analytics.mcda` with the three options, the person's scores and weights (saved as `live/mcda_operating_model.json`). Response: method "EVIDEM Multi-Criteria Decision Analysis (weighted-sum, 0-4 scale)"; values 80, 73.75 and 52.5.
2. `scripts/mcda_swap.py live/mcda_operating_model.json`: values match the connector; swap points below.

No other library call: the facts come from `references/operating-model-options.md`.

## Answer (short mode)

**Your scores put "single global QMS with MDSAP" first (80), "single global QMS without MDSAP" second (73.75) and "regional QMS" third (52.5).** The top two are close. The order of the top two reverses if build effort avoided is weighted 0.36 instead of 0.20, if speed to first market is weighted 0.29 instead of 0.20, if audit burden avoided falls to 0.14 from 0.25, or if markets served falls to 0.13 from 0.35. The regional option stays third under any single weight change.

**Facts that move the choice, for your markets**

| Fact | Row |
|---|---|
| The MDSAP site states MDSAP certification is required for Canadian Class II, III and IV licenses; the regulation requires a QMS certificate from a recognized registrar. | MR-05, MR-03 |
| FDA uses MDSAP reports in place of routine surveillance inspections only; non-surveillance inspections still happen. | QS40, MR-39 |
| No row says an MDSAP audit replaces a notified body audit under the MDR; Annex IX audits run at least every 12 months. `[GAP]` on substitution. | QS38, EU25 |
| MDSAP runs on a three-year cycle with surveillance audits in years two and three. | QS42 |
| The QMSR incorporates ISO 13485:2016, and EN ISO 13485 is harmonized under the MDR, so one ISO 13485-based system can carry both, with the US and EU additions. | QS3, EU28 |

What it means for you: your MDSAP score rests mostly on Canada. If Canada leaves the plan, rescore "markets served" and "audit burden avoided" before relying on this order.

**What to decide first:** confirm the market list and the class per market with your regulatory lead (A1). The MDSAP value depends on it (MR-35 to MR-39), and the EU conformity route sets the notified body audit cadence (EU25).

**Stops:** the operating model decision is your CEO's, as you named. Any later substantial change to a certified EU QMS goes to the notified body before it takes effect (EU24).

**Record:** Decision paper draft. Scores, weights and the decision are yours. Uncleared. AI-assisted.

The full version adds the facts-per-option table and the dependency sequence.

## What this example shows

- The model did not score. It ranked the person's scores and showed four weight changes that flip the top two.
- `mcda_swap.py` confirmed the connector's values (it found no difference) and added the robustness view the connector does not return (register item C17).
- The Canada fact carries the MDSAP case; the answer says so instead of calling MDSAP "recommended".
