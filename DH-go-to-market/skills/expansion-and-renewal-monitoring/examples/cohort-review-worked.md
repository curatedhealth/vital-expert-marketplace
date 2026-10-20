# Worked example: A2 cohort figures, then B1 expansion review

Run on 19 October 2026. The account file and the definitions are illustrative, written for this example and labeled so (`sample-data/accounts_illustrative.csv`, `sample-data/definitions_illustrative.json`). The script runs are saved beside them (`sample-data/cohort_run_2026-10-19.txt`, `sample-data/expansion_run_2026-10-19.txt`). No library call is needed for the computation; the live outputs in `live/` come from the sibling build and show the ranking call and the record refusal used at B1 Steps 6 and sign-off.

**Request:** "Our definitions are in the attached file (Dana Ortiz owns them). For 1 January to 30 September 2026, what are our renewal rate, gross and net retention, and did the upsell offers we made from 1 November 2025 to 30 September 2026 convert? We report net retention as value retained with expansion. No targets set yet."

**Runs**

1. `scripts/renewal_metrics.py cohort sample-data/accounts_illustrative.csv sample-data/definitions_illustrative.json`
2. `scripts/renewal_metrics.py expansion sample-data/accounts_illustrative.csv sample-data/definitions_illustrative.json`

## Answer (short mode)

These are your definitions (owner-stated, owner Dana Ortiz); no source defines renewal or retention measures, so nothing here is compared with a benchmark.

**1 January to 30 September 2026: 6 of 9 counted accounts renewed (66.7 percent). Net retention on your definition is 74.9 percent; gross is 67.3 percent.** One open account is in the denominator.

| Figure (your name) | Formula | Value |
|---|---|---|
| Renewal rate | renewed / (renewed + lost + open) = 6 / 9 | 66.7 percent |
| Gross retention | (765,000 - 130,000 lost - 10,000 contraction - 110,000 open) / 765,000 | 67.3 percent |
| Net retention | (as gross + 58,000 expansion) / 765,000 | 74.9 percent |

No rules set, so no verdicts. What rule do you hold for each?

**Outside the figures:** ACC-04 (CT-1004) excluded as a pilot, by your rule. ACC-08 (CT-1008) is open past its 31 August 2026 renewal date and holds 110,000 USD of the base: check the record.

**Losses by recorded reason, kept apart:** ACC-03 (CT-1003) price, routes to your pricing owner; ACC-06 (CT-1006) implementation open, routes to the implementation skills. An implementation that never completed cannot show whether value would have followed (CS32).

**Offers made 1 November 2025 to 30 September 2026:** 6 offers made, 3 signed, 1 refused, 1 open; acceptance 3 / 5 = 60.0 percent. ACC-09's outcome is "meeting held": not a signature on your definition, so it is listed apart and outside the denominator. The one refusal, ACC-02, records "result not yet seen by the account": it routes to the Customer Health skills, with an owner you name (owner not named).

**What it means for you:** of the 250,000 USD not counted as retained before expansion (130,000 lost + 10,000 contraction + 110,000 open), 110,000 USD is one open account (ACC-08); if it signs at its current value, gross retention on your definition would be 625,000 / 765,000 = 81.7 percent. The two losses had different recorded reasons; neither repeats.

**Record:** Figures on your data and your definitions. Uncleared. AI-assisted.

The full version adds the value bridge, the full account tables and the definitions card.

## What this example shows

- The figures are computed only on stated definitions, with each formula printed.
- Open and excluded accounts and a non-signature outcome stay visible instead of improving the rate.
- Reasons are reported as recorded and routed; no cause is inferred.
