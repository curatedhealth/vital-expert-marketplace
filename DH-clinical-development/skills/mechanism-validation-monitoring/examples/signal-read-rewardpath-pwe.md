# Worked example: A4 signal read and B1 hand-off, with the live PWE records

ILLUSTRATIVE product and data: "RewardPath", an invented contingency-management app, version 3.1, with invented events, exposure and thresholds (`evals/files/signal_*_illustrative.*`). The public records are real: the live `regulatory-dh.search_safety_events {product_code: "PWE"}` and `get_authorization {reference: "DEN160018"}` outputs of 20 October 2026 saved in `examples/live/connector_calls_2026-10-20.json`. The connector was not available when this example was written; the records were reused, not re-called, and need a live recheck when it returns.

## The request (invented)

"Here are our Q2 and Q3 complaint and event logs for RewardPath 3.1 against the thresholds we set on 16 March 2026 before launch. Six people in Q3 say the app gave them a reward spin after a positive drug screen. Is that reportable, and does the reSET recall mean we have the same bug?"

## Script run

`python3 scripts/signal_read.py --thresholds evals/files/signal_thresholds_illustrative.json --events evals/files/signal_events_illustrative.csv --exposure evals/files/signal_exposure_illustrative.csv --version 3.1`

```
Version: 3.1 | Thresholds set on: 2026-03-16 | Set before launch: True
Events of other versions excluded: 1 | Events outside every period: ['E15']

Period 2026-Q2 (2026-04-01 to 2026-06-30), active users 1840:
  S1 reward logic complaint (event_rate_per_1000): 0.54 [1 events / 1840 active users x 1000] alert when > 2.0: not crossed
  S2 use error (event_count): 2 [count] alert when > 5: not crossed
  S3 adverse event (event_count): 0 [count] alert when > 0: not crossed
  S4 negative_screen_share_weeks_9_12 (measure): 0.41 [per the person's measure definition] alert when < 0.35: not crossed
  Categories without a threshold (counted, no verdict): {'app store review': 1}
  Seriousness as assigned: {'app store review / not assessed': 1, 'reward logic complaint / not assessed': 1, 'use error / not assessed': 2}

Period 2026-Q3 (2026-07-01 to 2026-09-30), active users 2210:
  S1 reward logic complaint (event_rate_per_1000): 2.71 [6 events / 2210 active users x 1000] alert when > 2.0: crossed the person's threshold
  S2 use error (event_count): 1 [count] alert when > 5: not crossed
  S3 adverse event (event_count): 1 [count] alert when > 0: crossed the person's threshold
  S4 negative_screen_share_weeks_9_12 (measure): 0.33 [per the person's measure definition] alert when < 0.35: crossed the person's threshold
  Categories without a threshold (counted, no verdict): {'app store review': 1}
  Seriousness as assigned: {'adverse event / not assessed': 1, 'app store review / not assessed': 1, 'reward logic complaint / not assessed': 6, 'use error / not assessed': 1}

Note: Categories and seriousness are as the person assigned them; none is reclassified here.
Note: Whether any event is reportable under 21 CFR 803 or 806 or MDR Articles 87 to 89, and by when, is the call of the owner the person names for vigilance reporting (route: dh-regulatory-and-quality audit-capa-and-complaints).
Note: A crossed threshold is a signal for the miss review (B1), not a finding that the product is unsafe or ineffective; a threshold not crossed is not a finding that it is safe or effective.
```

## The answer (short mode)

**Answer.** RewardPath 3.1, thresholds set 16 March 2026 before launch. In 2026-Q3 three of your four signals crossed your thresholds: reward logic complaints at 2.71 per 1,000 active users (6 of 2,210; your threshold above 2.0), one event you categorized as an adverse event (your threshold above 0), and the negative-screen share in weeks 9 to 12 at 0.33 (your threshold below 0.35). Use errors did not cross. In 2026-Q2 nothing crossed. One use error dated 3 October 2026 falls outside both periods and is listed, not dropped. Whether any of this is reportable is the call of the owner you name for vigilance reporting; you have not named one (owner not named).

**Rule text that touches these categories (not a finding).** "Caused or contributed" includes failure, malfunction, design, labeling and user error (SE39). A malfunction is a failure to meet performance specifications, which "include all claims made in the labeling" (SE40). A reportable event is information that reasonably suggests a death or serious injury, or a malfunction likely to cause one if it recurred (SE38). Reportability and clocks from the awareness date: `dh-regulatory-and-quality` audit-capa-and-complaints.

**Public record, as stated.** Product code PWE (reSET, DEN160018, granted 14 September 2017): two Class II recalls dated 7 June 2021, one for reSET and one for reSET-O, each stating: "Due to a software issue, patients with a urine drug screen (UDS) received access to a contingency management wheel spin for potential rewards regardless of the UDS results." MAUDE: 2 reports for PWE; counts are reports, not confirmed events. Whether that record bears on RewardPath is not judged here.

**Handed to B1.** S1 reward logic complaints (delivery link: the reward component), S3 adverse event (safety signal; reportability first), S4 negative-screen share (efficacy signal; read beside your claims). Risk file: `dh-regulatory-and-quality` design-controls-and-risk-management. Owners and the date to look again are yours.

Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

Calls made: none live (connector unavailable); saved records reused: `regulatory-dh.search_safety_events {product_code: "PWE", limit: 10}` and `regulatory-dh.get_authorization {reference: "DEN160018"}`, both of 20 October 2026.
