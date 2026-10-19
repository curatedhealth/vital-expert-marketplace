# Worked example: B1 site review and repair

Run on 19 October 2026, continuing the A2 example (illustrative site data). The ranking is a real library call (`live/rice_repairs.json`); the numbers were typed for the measurement and are presented as the example person's.

**Request:** "Use those results. Our rules: 50 percent patient penetration at every live clinic, and no core milestone more than 30 days late. Clinic D is Sam's; nobody owns Clinic B's interface yet. Rank these repairs with our RICE numbers: Clinic D workflow re-configuration with super-users (reach 290, impact 2, confidence 50 percent, effort 3); Clinic B finish the results interface (380, 1, 80 percent, 4); refresher training at all live clinics (1600, 0.5, 50 percent, 2)."

**Calls**

1. `analytics.rice {initiatives: [... confidence: 0.5 ...]}`: returned confidence 0.005 and scores of 2, 0.9667 and 0.76. The tool reads confidence as a percent.
2. `analytics.rice {initiatives: [... confidence: 50 ...]}`: refresher training 200, Clinic D re-configuration 96.67, Clinic B interface 76.

## Answer (short mode)

**Three of four live clinics miss your penetration rule (B 40.0, C 42.0, D 20.0 percent; only A meets it). Your lateness rule is missed at Clinic D (every core milestone, 34 to 65 days late) and Clinic E (three open core milestones, 42 to 70 days); not at B (11 to 28 days) or C (4 to 14 days).** Clinic E is not live and its day-one workflow configuration is open: that deployment is not closed.

| Site | Open item | Owner | Limited launch | Recheck |
|---|---|---|---|---|
| Clinic D | Penetration 20.0% vs 50% | Sam (yours) | yours to decide | blank |
| Clinic B | Results interface to EHR, open 196 days | owner not named | yours to decide | blank |
| Clinic C | Penetration 42.0% vs 50% | owner not named | yours to decide | blank |
| Clinic E | Day-one workflow configuration open | owner not named | not live | blank |

**Hypotheses (not causes, CS3):**
- Clinic D: low provider penetration (37.5 percent) with usage at 40 percent of the agreed profile. Hypothesis: providers lack time or training to deliver. Confirm with training records by role and the deliverers' capability and opportunity as the site describes them (CS19).
- Clinic B and C: provider penetration 60 to 64 percent. Hypothesis: eligible patients are not offered the product in the workflow. Confirm with the offer rate (CS14).

**Ranking of your RICE numbers:** refresher training 200, Clinic D re-configuration 96.67, Clinic B interface 76. Refresher training leads on reach (1600). If its confidence were 24 percent instead of 50, Clinic D would lead. Note: refresher training alone is the weakest control for a workflow fault, and training decays (CS77, CS78).

**Proposed repairs (ERIC):** audit and feedback to Clinic D's clinicians (CS44); identify and prepare champions (CS46).

**Stops:** telling the customer any clinic is live or performing; closing Clinic E's deployment while its day-one item is open.

**Record:** Site review draft. Uncleared. AI-assisted.

## Check of the ranking

Score = reach x impact x confidence / effort: 1600 x 0.5 x 0.5 / 2 = 200; 290 x 2 x 0.5 / 3 = 96.67; 380 x 1 x 0.8 / 4 = 76. Swap point for the top two: 1600 x 0.5 x c / 2 = 96.67 gives c = 0.242, so a confidence of about 24 percent.
