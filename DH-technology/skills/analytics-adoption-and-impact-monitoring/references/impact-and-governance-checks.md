# Impact, cadence and governance checks

Interpretive reference for tasks A2 and B1. Each sourced rule carries its row; the research files in this folder hold the URL, verbatim quote and read date. Where this file states a step from the old framework tasks (DH-05.02.2.2, DH-05.02.3.3, DH-05.03.1.3, DH-05.03.3.1.3, DH-05.03.3.2.3), it says so.

## 1. Report cadence (old task method)

DH-05.02.2.2.1 to .3: a report has an audience, a due day, the source refresh that must finish first, and what is sent if the refresh fails ("Do not send last period's numbers as this period's"); each issue records period, sender, recipients, the data timestamp and any metric withheld and why ("Do not send a report with no timestamp"); a missed issue records the date, the reason (refresh, owner absent, decision cancelled), who was told and the next issue date ("Do not skip an issue silently").

`cadence` flags C1 to C7. C3 (same data timestamp as the previous issue) is the script's test for "last period's numbers sent as this period's". No source sets a lateness tolerance; the person's cadence rule decides.

## 2. The bet metric and its comparison (old task method with the rows)

DH-05.02.3.3.1 and .2: the outcome is the metric from the bet, in a window after the user acts, against a comparison (before the product, or users who did not get it); count the outcome in the window, keep the comparison, state the number of users. "Do not use page views as the outcome." "Do not report a change without the comparison."

DH-05.03.1.3.1 and .2: review a product against the bet or value case it was funded on, for a named period; report the metric and the comparison from the bet; name a data gap as `[GAP]`; separate product failure from a metric never instrumented. "Do not treat a missing metric as a zero."

| Rule | Source and rows |
|---|---|
| Implementation outcomes are preconditions for service or clinical outcomes; separate a failed deployment from an ineffective product | Proctor 2011 (CS32), DOI 10.1007/s10488-010-0319-7 |
| Effectiveness includes negative effects, quality of life and economic outcomes, not only the primary outcome | RE-AIM, re-aim.org, read 19 October 2026 (CS23) |
| Report unstratified and by each stratum | CMS MMS Hub, read 20 October 2026 (DA-136), CMS quality-measure guidance used as a checklist |
| Descriptive statistics show data are available, not that they are reliable or valid | CMS MMS Hub (DA-139) |

`outcome` flags O1 to O5 and prints the difference as "arithmetic on your file, not evidence that the product caused it". A before-after design cannot separate the product from anything else that changed in the window; a causal design is `data-preparation-and-analytics-methods` (this pack).

## 3. Decision support in use

| Fact | Source and rows |
|---|---|
| Report user agreement with the AI system and reasons for variation from its recommendations | DECIDE-AI, Vasey 2022 (DA-82), DOI 10.1136/bmj-2022-070904 |
| Report significant errors or malfunctions, with rate, causes and impact on care | DECIDE-AI (DA-83) |
| Report usability evaluation and user learning curves | DECIDE-AI (DA-84) |
| Track existing, unanticipated and emergent risks from intended versus actual performance in deployment | NIST AI RMF 1.0, January 2023, MEASURE 3.1 (DA-14) |
| Continuously and transparently assess AI applications during actual use | WHO Ethics and governance of AI for health, 28 June 2021, principle 6 (DA-29) |
| Clinicians should note misalignment between model predictions and their own judgment | Finlayson 2021 (DA-93 [WF]), DOI 10.1056/NEJMc2104626 |

`agreement` prints agreement, variation, unrecorded cases and the reasons as recorded. High agreement is not accuracy and low agreement is not error; neither says whether the recommendation or the user was right.

Ongoing duties that may apply, by market, laid out as facts for the owner the person names:

| Duty | Source and rows |
|---|---|
| US certified health IT: users can give feedback on evidence-based interventions; export holds intervention, action, feedback, user, date and location | 45 CFR 170.315(b)(11), eCFR read 19 October 2026 (UX-US-55). HTI-5 (proposed 29 December 2025) would remove the source-attribute and risk-management requirements of (b)(11)(iv) to (vi); proposed only (UX-US-60) |
| US covered entities: an ongoing duty to make reasonable efforts to identify tools using race, color, national origin, sex, age or disability inputs, and to mitigate the risk of discrimination | 45 CFR 92.210, eCFR read 19 October 2026 (PE-113 to PE-115) |
| EU high-risk AI systems: automatic event logs over the lifetime; logs support post-market monitoring | Regulation (EU) 2024/1689, Articles 12(1) and 12(2) (DA-54, DA-55) |
| EU high-risk AI systems: post-market monitoring collects and analyzes performance data over the lifetime; Commission template guidance by 2 September 2027 | Articles 72(2) and 72(3) as amended by Regulation (EU) 2026/1744 (DA-65, DA-66) |
| EU dates as amended: Articles 10 to 15 apply from 2 December 2027 (Annex III) and 2 August 2028 (Annex I) | (DA-67) |
| FDA draft: a postmarket performance monitoring plan for AI-enabled devices | FDA AI-enabled device software functions draft, January 2025, not for implementation (DA-35, DA-44); a draft, never a requirement |

Whether a duty applies stops for the owner the person names for regulatory, legal or compliance matters. AI Act compliance monitoring is `responsible-ai-compliance-monitoring` (this pack).

Calibration drift of a predictive score behind the product (Davis 2017, DA-91, DA-92, DOI 10.1093/jamia/ocx030) is read by `model-performance-and-drift-monitoring` (this pack). This skill reports usage, agreement and outcome; a change in agreement is a reason to ask that skill, not a drift finding.

## 4. Stale numbers on a clinical step (old task method)

DH-05.02.3.2.3: name the metric owner, the workflow owner and which one stops the display when the metric is stale. "Do not leave a stale number on a clinical step." A2 reads the person's display log or issue log for the data timestamp shown on the step against their stale rule; without a stale rule, the timestamps are reported and nothing is called stale.

## 5. Decertification (old task method)

DH-05.03.3.1.3: when a formula changes, the metric goes back to draft until the certification rule is passed again, and the dashboards that use it show the draft status. "Do not leave a changed formula certified." `governance` flags G2 (formula changed after certification and still certified) and G3 (dashboards use a draft or changed metric without showing its status). Decertifying is the certifier's decision.

Curriculum units that teach a changed metric are flagged (old DH-05.03.2.1.3; `adoption-measurement.md` section 8).

## 6. Access review (old task method with the rows)

DH-05.03.3.2.3: list current publishers, remove a publisher who has changed role, record the review date. "Do not leave publish rights on a departed role."

| Fact | Source and rows |
|---|---|
| Regular review of records of information system activity (audit logs, access reports, security incident tracking) is required | HIPAA Security Rule, eCFR read 20 October 2026 (EN-101) |
| Unique user identification is required | HIPAA Security Rule (EN-103) |
| The January 2025 Security Rule NPRM is a proposal, a long-term action with final action shown as July 2027; the current rule remains in force | Federal Register, 6 January 2025 (EN-106); 2026 Unified Agenda (EN-107) |
| Role-based access: identify which workforce classes need which PHI | 45 CFR 164.514 (CS104) |

`governance` flags P1 (role changed since the grant and rights kept), P2 (never reviewed) and P3 (last review older than the person's interval, only if the person gives one). The review interval is the person's; the CMS three-year measure reevaluation (DA-140) is not an access review interval. Removing a right is the platform owner's decision. Access log monitoring as a security operation is `security-and-privacy-operations-monitoring` (this pack).

## 7. What is not sourced

- Any cadence tolerance, agreement or override limit, outcome-change target or review interval `[GAP]`.
- A source that sets how long a number may stay on a clinical step before it is stale `[GAP]`; the person's stale rule.
