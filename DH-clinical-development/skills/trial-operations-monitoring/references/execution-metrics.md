# Execution metrics: definitions and the rules behind them

Interpretive reference for task A1. CV rows are in `clinical-study-and-rwe-research.md`; CVB rows in `gcp-quality-rows.md`.

## Why these four metrics

ICH E6(R3) asks monitoring to identify missing data, inconsistent data, outliers, unexpected lack of variability and protocol deviations, and to examine trends within and across sites (CVB6). Centralized monitoring evaluates accumulated data to find systemic or site-specific issues (CVB5). FDA recommends centralized monitoring in decentralized trials for missing, inconsistent and outlying data and potential deviations (CV71). The four metrics below are the counts that make those checks possible from the person's own export. The formulas are this skill's working definitions, not definitions any source sets; agree them with the person (step 1 of A1).

| Metric | Formula (in `scripts/trial_ops_metrics.py`) | What it supports | Row |
|---|---|---|---|
| Enrollment | Enrolled count per site; share of the person's target; enrolled per month since site activation | Site-level trend, compared across sites | CVB6 |
| Retention | (active + completed) / enrolled; withdrawn and lost to follow-up listed separately | Missing outcome data; the CONSORT flow diagram documents participant flow | CVB6, CV110 (CONSORT 2025, DOI 10.1136/bmj-2024-081123) |
| Protocol deviations | All deviations and important deviations, per enrolled participant | Deviation trends; important deviations are classed by the sponsor's own trial-specific criteria | CVB1, CVB2, CVB6 |
| Data completeness | Received / expected assessments, per site and per arm | Missing data; same collection method in all arms | CVB6, CV58, CV59 |

## Reading the metrics correctly

- **Important deviations use the person's criteria.** The sponsor sets the trial-specific criteria for "important" (CVB2). If the export has no important-deviation flag, report total deviations only and say the classification is `[GAP]`.
- **Missing data are defined against an estimand.** Whether a missed assessment is "missing" for analysis depends on the estimand and the intercurrent-event strategy (CV41, CV32 to CV39). Completeness here is an operational count, not the analysis definition. Say so when the person moves from operations to analysis.
- **Arm differences matter.** The same collection method is used in all arms (CV58). A completeness gap between arms at one site is a fact to report, even if the trial total looks balanced (an aggregate can hide a site).
- **Withdrawal and loss to follow-up are different.** Keep them apart; CONSORT 2025 adds items on who is included in each analysis and how missing data were handled (CV112, DOI 10.1136/bmj-2024-081123).
- **Visit modality.** If the protocol lets participants choose remote or site visits, completeness by modality is worth asking for: free choice can bias results (CV67), and visit records hold visit type and location (CV69).

## What the sources do not set

No source here sets a retention, completeness, enrollment or deviation threshold. E6(R3) asks the sponsor to pre-specify acceptable ranges where relevant (CVB3); the numbers are the person's. Published retention figures from remote studies were not sourced for this skill `[GAP]`; do not quote one as a benchmark.

## Privacy

The script runs locally on a pseudonymous export. Do not put participant-level rows into a library call or a shared record. Aggregates per site are enough for every output.
