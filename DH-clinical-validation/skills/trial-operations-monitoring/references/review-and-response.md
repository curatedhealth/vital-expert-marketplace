# Review and response: stall points, hypotheses and routing

Interpretive reference for task B1. CV rows are in `clinical-study-and-rwe-research.md`; CVB rows in `gcp-quality-rows.md`.

## What the sources ask of a review

- Pre-specified acceptable ranges for critical-to-quality factors, where relevant; when one is exceeded, an evaluation checks for a systemic issue and whether action is needed. CVB3
- Important quality issues, including exceeded ranges, and the remedial actions taken are documented in the clinical trial report. CVB4
- The investigator documents all deviations and, for important ones, explains them and acts to prevent recurrence. CVB1
- Risk control proportionate to the importance of the risk. CV7

So the review has three outputs the sources expect: which ranges were exceeded, whether the cause looks systemic or site-specific, and what remedial action is recorded. The ranges, the judgment and the action are the person's.

## Stall points (first metric that misses a rule, in this order)

| Stall point | What it usually means for the next step |
|---|---|
| Enrollment | The trial may not reach its sample; registration status updates follow a recruitment change (CV149). |
| Retention | Outcome data will be missing for withdrawn or lost participants; the estimand decides how (CV41). |
| Protocol deviations | Data reliability or participant safety may be affected if deviations are important (CVB2). |
| Data completeness | Endpoint data missing for participants still enrolled; check whether it differs by arm (CV58) or by visit modality (CV67). |
| Disclosure clock | A registration, update or results date has passed without a recorded submission (A2). |

## Hypotheses to test (never stated as causes)

Each is drawn from a sourced mechanic. Offer the ones that fit the data, each with what would confirm it.

| Pattern in the data | Hypothesis | What would confirm it | Row |
|---|---|---|---|
| Completeness lower in one arm at one site | Collection method differs between arms in practice (device version, app build, visit modality) | Device and app version by arm; visit type by arm | CV58, CV69 |
| Completeness lower for remote visits | Participant choice of remote visits selects sicker or less engaged participants | Completeness and retention by visit type | CV67 |
| Low completeness from a DHT stream | The trial population struggles to use the DHT as intended | Usability evidence for this population; support tickets by site | CV51, CV48 |
| Gaps in DHT data with no participant pattern | Transfer to the first durable repository fails | Transfer logs; data flow overview | CV60, CV102 |
| Important deviations clustered at one site | A site-specific process issue rather than a systemic one | Deviation categories by site; monitoring report | CVB5, CVB6 |
| Same deviation type at every site | A systemic design or protocol issue | Deviation categories across sites | CVB3 |
| Local-provider tasks behind deviations | Protocol-specific tasks given to non-trial personnel | Task list against the routine-practice test | CV70 |
| Unexpected lack of variability in a site's data | A data-quality problem the guideline names | Distribution of values by site | CVB6 |

## Routing the response (the person chooses)

| Stall point or hypothesis | Responding work |
|---|---|
| Setup, consent route, local providers, DHT fitness, data flow | The decentralized trial operations skill (DH-01.02.3.1): A1, A2 or B1 |
| Endpoint, estimand or analysis definition | The study design skill (DH-01.02.1) |
| Device status, human factors | dh-regulatory-strategy |
| Participant engagement and retention programs | dh-patient-engagement |
| Registration, update or results submission | The owner the person names for registration, or owner not named, with the registry |

## Never

- State a cause the data do not show.
- Name an owner the person did not name.
- Present a retention or completeness figure as clinical evidence, or read operational metrics as the trial's result.
