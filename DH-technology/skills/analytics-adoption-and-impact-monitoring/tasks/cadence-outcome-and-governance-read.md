# A2 Cadence, outcome and governance read

Framework task: DH-05.02.2.2, DH-05.02.3.3, DH-05.03.1.3, DH-05.03.3.1.3 and DH-05.03.3.2.3, Part A, task A2. Carries the old tasks "Cadence", "Issue record", "Cadence break" (DH-05.02.2.2.1 to .3), "Outcome of the decision" and "Outcome measurement" (DH-05.02.3.3.1 and .2), "Performance question" and "Performance read" (DH-05.03.1.3.1 and .2), "Decertify" (DH-05.03.3.1.3) and "Access review" (DH-05.03.3.2.3), with the in-use read of decision support (user agreement, staleness on a clinical step, ongoing duties).

## What this task delivers

As of the person's read date: the issue cadence read (on time, missed, fresh data or the previous issue's data) with flags C1 to C7; the bet metric against its comparison in the person's window with users and units, and flags O1 to O5; user agreement with the recommendation and the reasons for variation as recorded (DECIDE-AI, DA-82); the timestamps shown on a clinical step against the person's stale rule; certified metrics whose formula changed and dashboards not showing draft status (G1 to G4); publish rights after role changes and reviews (P1 to P3); and the ongoing duties that may apply in the person's market, as facts. It answers "are the numbers going out fresh, did the decision change against our comparison, do users follow the recommendation, and is the certified layer still true?"

Why it matters: "Do not send last period's numbers as this period's", "Do not report a change without the comparison", "Do not treat a missing metric as a zero" and "Do not leave a changed formula certified" are the old tasks' own lines. An outcome read without its comparison, or a certified metric whose formula moved, turns a review into an opinion.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `clinical-content-product-manager` (old DH-05.02.2.2); `data-analytics-lead` (old DH-05.02.3.3); `chief-digital-health-officer` (old DH-05.03.1.3); `ai-ml-governance-director` (old DH-05.03.3). Work as an analytics monitoring analyst who reads the person's logs |
| Skill | Analytics adoption and impact monitoring, Part A, Cadence, outcome and governance read |
| Workflow | The steps below |
| Knowledge | `references/impact-and-governance-checks.md`; rows CS23, CS32, CS104, DA-14, DA-29, DA-35, DA-44, DA-54, DA-55, DA-65 to DA-67, DA-80 to DA-84, DA-91 to DA-93, DA-119, DA-136, DA-139, UX-US-55, UX-US-60, PE-113 to PE-115, EN-101, EN-103, EN-106, EN-107; `references/governance.md` |
| Tools | `literature.get_record` and `verify.check_claim` only for a paper the answer leans on. `scripts/adoption_check.py cadence`, `outcome`, `agreement`, `governance`, `words`; `verify.build_record` when the record leaves |
| Prompt | This guide |
| Template | `assets/cadence-outcome-and-governance-read-output.md` |
| Input | The request and its context: the issue log, the bet (metric, comparison, window) from `analytics-products-and-decision-support` or the person, the outcome file, the case file, the display or issue log with data timestamps and the person's stale rule, the metric register, the publisher list, the review interval, the read date, the market |
| Governance | `references/governance.md`; the person judges |
| Catalogue job | none |

## Read the request

- Which reads: cadence, outcome, agreement, staleness, governance? Run only those steps.
- Is the bet written down (metric, comparison, window)? Without it, the outcome read is "bet not given"; the person's current metric is given as a value only. The product is never reviewed against a goal it was not given (old DH-05.03.1.3.1).
- Is the read date given? Without it, "not given"; ask.
- Which market? Ongoing duties are listed only for the market in the request.

## Workflow

### Step 1. Issue cadence (old DH-05.02.2.2)

Run `python3 scripts/adoption_check.py cadence --log ISSUES.csv`. Give each issue with its period, due date, sent date, data timestamp and status, and the flags: C1 no data timestamp, C2 sent before the source refresh finished, C3 same data timestamp as the previous issue (the old "last period's numbers as this period's"), C4 sent after the due date, C5 missed with no reason, C6 missed with no one told, C7 missed with no next issue date. Withheld metrics and why, as logged. Whether a late or missed issue breaks the cadence is the person's rule.

### Step 2. The bet metric against its comparison (old DH-05.02.3.3 and DH-05.03.1.3)

Write the bet back: metric, comparison, window, as funded. Run:

```
python3 scripts/adoption_check.py outcome --file OUTCOME.csv --bet-metric "<the bet metric>"
```

Give each group's rate with units and users, the difference as "arithmetic on your file, not evidence that the product caused it", the comparison type, and the flags: O1 no comparison, O2 windows differ between concurrent groups, O3 users not given, O4 page views or clicks as the outcome, O5 metric differs from the bet. Read the adoption figures from A1 beside it: a product used by few cannot be judged on the outcome (Proctor 2011, CS32, DOI 10.1007/s10488-010-0319-7). Ask for negative effects the person tracks (RE-AIM effectiveness includes them, re-aim.org, read 19 October 2026, CS23). Give results by stratum where the person's file has strata (CMS MMS Hub, DA-136, used as a checklist). A metric never instrumented is "not instrumented `[GAP]`", never zero, and never a product failure. A design that separates the product's effect from other changes is `data-preparation-and-analytics-methods` (this pack).

### Step 3. User agreement with the recommendation

Run `python3 scripts/adoption_check.py agreement --file CASES.csv`. Give agreement, variation and unrecorded cases with denominators, the share of variations with a reason recorded, and the reasons as recorded (DECIDE-AI, Vasey 2022, DA-82, DOI 10.1136/bmj-2022-070904). State that high agreement is not accuracy and low agreement is not error. If the person wants agreement compared across patient or user groups and calls it fairness, state that fairness criteria conflict (Paulus and Kent 2020, DA-119, DOI 10.1038/s41746-020-0304-9) and ask which criterion fits. A change in agreement over time is a reason to ask `model-performance-and-drift-monitoring` (this pack) about calibration (Davis 2017, DA-91, DOI 10.1093/jamia/ocx030), not a drift finding here.

### Step 4. Stale numbers on a clinical step (old DH-05.02.3.2.3)

From the person's display log or issue log, give the data timestamp shown on the step against the person's stale rule, with the metric owner, the workflow owner and who stops the display. Without a stale rule, give the timestamps and write "stale rule not given"; nothing is called stale.

### Step 5. Certification and access (old DH-05.03.3.1.3 and DH-05.03.3.2.3)

Run:

```
python3 scripts/adoption_check.py governance --metrics REGISTER.csv --publishers PUBLISHERS.csv --as-of <read date> [--review-every-days <the person's interval>]
```

Give G1 certified with no owner, G2 formula changed after certification and still certified, G3 dashboards using a draft or changed metric without showing status, G4 certified with no certifier or date; P1 role changed since grant with rights kept, P2 never reviewed, P3 review older than the person's interval (only if given). Beside the access flags, where PHI is involved (US): regular activity review and unique user identification are required (HIPAA Security Rule, eCFR read 20 October 2026, EN-101, EN-103); role-based access by workforce class (45 CFR 164.514, CS104); the January 2025 NPRM is a proposal (EN-106, EN-107). Decertifying and removing rights are the owners' decisions.

### Step 6. Ongoing duties, as facts

For the person's market, list the duties that may apply, each with source and date and "for the owner you name": ONC user feedback capture in certified health IT (UX-US-55) with the HTI-5 proposal stated as proposed only (UX-US-60); the ongoing duty under 45 CFR 92.210 (PE-113 to PE-115); AI Act logging and post-market monitoring for high-risk systems (DA-54, DA-55, DA-65, DA-66) with dates as amended (DA-67); tracking intended versus actual performance (NIST AI RMF 1.0, MEASURE 3.1, DA-14) and continuous assessment in use (WHO, 28 June 2021, DA-29). The FDA postmarket monitoring plan (DA-44) is in a January 2025 draft, not for implementation (DA-35).

## Build the output

Follow `assets/cadence-outcome-and-governance-read-output.md`. Answer first: the cadence flags that matter for the person's question, the bet metric difference with its comparison type and flags, agreement and the share of variations with a reason, and the governance flags. No verdict. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/adoption_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every figure carries its window and read date; every rate its numerator and denominator.
- No causal claim from a before-after difference; no verdict on the product.
- No target, tolerance, interval or stale rule came from the model.
- Drafts and proposals are labeled; AI Act dates are stated as amended.
- Every fact names its source and date in plain words with the row id after it; [PAPER] rows carry their DOI.
- `python3 scripts/adoption_check.py words ANSWER.md` prints "within the short-mode cap".
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Calibration and drift of the model: `model-performance-and-drift-monitoring` (this pack).
- Causal design for impact: `data-preparation-and-analytics-methods` (this pack).
- Security operations on access logs: `security-and-privacy-operations-monitoring` (this pack).
- AI Act compliance monitoring: `responsible-ai-compliance-monitoring` (this pack).
- Device post-market duties: `dh-regulatory-and-quality` ai-ml-readiness-monitoring.
