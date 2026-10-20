# Decision support design: sourced rules

Interpretive reference for task B1. Each sourced rule carries its row; the research files in this folder hold the URL, verbatim quote and read date. Where this file states a step from the old framework tasks (DH-05.02.2.1, DH-05.02.2.3, DH-05.02.3.2, DH-05.01.3.3), it says so.

## 1. Executive dashboards (old task method)

DH-05.02.2.1.1 to .3: name the person or role and the decision, the few metrics that decide it, and the metric kept off ("Do not build an executive dashboard as a catalog of every KPI"); put the decision metric first, show the period and the comparison (last period or target), and show the data timestamp ("Do not hide the timestamp"); review the dashboard with the executive before it becomes the official one: ask them to make the decision from the page, record the metric they asked for that is missing and the one they told you to remove.

Only certified metrics (task A2) appear on an official dashboard; a draft metric shows its status. The comparison is the person's (prior period or their target); the model never supplies a target.

## 2. Commentary and narrative (old task method plus generative AI risks)

DH-05.02.2.3.1 to .3: name the metric move to explain and its comparison, and refuse a sentence the metric does not support; name the breakdown (segment, site, product) that accounts for the move with its numbers, and stop if no breakdown accounts for it ("Do not invent a driver"); write the commentary from that sentence and driver only, with the action as a question unless the decision frame named one, dated and with its author ("Do not add a second claim").

`scripts/metric_check.py driver` computes each segment's share of the total change. A segment "accounts for the move" only under the person's own rule (`--share`); without it, no driver is named.

Where commentary is drafted by a generative model:

| Risk | Source and rows |
|---|---|
| Confabulation: confidently stated but erroneous or false content | NIST AI 600-1, July 2024 (DA-20) |
| Human-AI configuration: automation bias and over-reliance | NIST AI 600-1 (DA-21) |
| Automation bias by professionals and patients is an LMM risk | WHO guidance on large multi-modal models, news release 18 January 2024 (DA-34) |

Rule: every number in generated commentary must match the metric table it sits beside, and every driver must come from the `driver` output. A sentence that cannot be traced to a figure is removed, not softened.

## 3. Embedding analytics in a workflow (old task method)

DH-05.02.3.2.1 to .3: name the host workflow and step, the number or recommendation that appears there and what is removed from that step ("Do not add a link out to a dashboard and call it embedded"); name the action the user can take without leaving the step, the write-back or task it creates, and the action that still needs another system ("Do not claim the workflow changed if the user must export"); name the owner of the metric, the owner of the host workflow, and which one stops the display when the metric is stale ("Do not leave a stale number on a clinical step").

## 4. US: FDA clinical decision support guidance

Current version: FDA "Clinical Decision Support Software", 29 January 2026, superseding the 6 January 2026 issue (UX-US-64). Facts to lay out for a decision support function aimed at health care professionals:

| Fact | Source and rows |
|---|---|
| Criterion 4: the software must enable the HCP to independently review the basis for the recommendations so they rely on their own judgment | FDA CDS guidance, 29 January 2026 (UX-US-65) |
| Software for a critical, time-sensitive task or decision does not meet Criterion 4 | (UX-US-66) |
| Required inputs identified, with plain-language instructions on obtaining them, their relevance and data quality needs | (UX-US-67) |
| Plain-language description of algorithm development and validation | (UX-US-68) |
| Output gives patient-specific information and knowns and unknowns, such as missing or unexpected inputs | (UX-US-69) |
| Basis information prioritizes decision-relevant information and avoids overload | (UX-US-70) |
| Usability testing may be needed to show Criterion 4 is met | (UX-US-71) |
| Automation bias: errors of commission and omission | (UX-US-72) |
| Software that supports or recommends to patients or caregivers, not HCPs, meets the device definition | (UX-US-73) |
| Enforcement discretion where only one option is clinically appropriate and all criteria are otherwise met | (UX-US-74) |

Rule: the model lays these facts beside the person's design (time pressure, audience, inputs shown, basis shown). It never concludes that the function is or is not a device: route to `dh-regulatory-and-quality` regulatory-pathway-and-classification. Usability testing is `dh-patient-and-user-experience` clinical-workflow-ux-design.

## 5. US: ONC decision support interventions (certified health IT)

Applies where the analytic is delivered through a certified Health IT Module (45 CFR 170.315(b)(11), from HTI-1, eCFR read 19 October 2026):

| Requirement | Source and rows |
|---|---|
| Interventions occur while the user is interacting with the technology | (UX-US-54) |
| Users can give feedback on evidence-based interventions; export holds intervention, action, feedback, user, date and location | (UX-US-55) |
| A limited set of identified users can access plain-language source attributes | (UX-US-56) |
| Predictive DSIs disclose intended use, population, users and decision-making role (informs, augments, replaces) | (UX-US-57) |
| Predictive DSIs state tasks, situations or populations where users are cautioned against use | (UX-US-58) |
| Modules indicate when source attributes are not available | (UX-US-59) |
| User-centered design applies to (b)(11), at least 10 test participants per capability | (UX-US-62) |

Proposal, not law: HTI-5 (proposed 29 December 2025, 90 FR 60970) would remove the source-attribute and risk-management requirements of (b)(11)(iv) to (vi) and the safety-enhanced design criterion (UX-US-60, UX-US-63). ONC states its basis as developer reports, not a measured study (UX-US-61). Treat the current text as in force but at risk; no final rule was found on 19 October 2026.

Even where certification does not apply, the predictive DSI attributes (UX-US-57, UX-US-58) are a usable checklist for the "what it is for and where not to use it" panel; say so when used that way. EHR integration build is `interoperability-and-ehr-integration` (this pack).

## 6. US: nondiscrimination in patient care decision support tools

| Fact | Source and rows |
|---|---|
| Covered entities must make reasonable efforts to identify tools using race, color, national origin, sex, age or disability inputs, and to mitigate the risk of discrimination | 45 CFR 92.210, eCFR read 19 October 2026 (PE-113) |
| "Patient care decision support tool" covers any automated or non-automated tool supporting clinical decision-making | (PE-114) |
| Paragraphs (b) and (c) apply within 300 days of 5 July 2024 (the regulation states only the 300 days) | (PE-115) |

Rule: list the inputs of the person's tool that measure a protected characteristic (from their input list), as facts. Whether the entity is covered and whether its efforts are reasonable stops for the owner the person names for legal or compliance matters. Equity monitoring of reach is `dh-patient-and-user-experience` health-equity-monitoring.

## 7. EU: AI Act transparency and human oversight (high-risk systems)

Applies to a decision support system that is high-risk under the AI Act; whether it is high-risk (for example as an MDR device under Annex I) is `responsible-ai-governance` (this pack) and `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control. Dates as amended by Regulation (EU) 2026/1744: Chapter III Sections 1 to 3 apply from 2 December 2027 (Annex III) and 2 August 2028 (Annex I) (DA-67).

| Duty | Source and rows |
|---|---|
| Instructions state accuracy level and metrics, robustness and cybersecurity tested | Regulation (EU) 2024/1689, Article 13(3)(b)(ii) (DA-56) |
| When appropriate, performance for specific persons or groups | Article 13(3)(b)(v) (DA-57) |
| Oversight measures commensurate with risk, autonomy and context | Article 14(3) (DA-59) |
| Overseers remain aware of automation bias | Article 14(4)(b) (DA-60) |
| Overseers can disregard, override or reverse output and stop the system | Article 14(4)(d) and (e) (DA-61) |
| Accuracy levels and metrics declared in the instructions | Article 15(3) (DA-62) |

## 8. Live evaluation and model information

| Fact | Source and rows |
|---|---|
| DECIDE-AI reports early-stage live clinical evaluation of AI decision support: 17 AI-specific items and 10 generic items | Vasey 2022 (DA-80), DOI 10.1136/bmj-2022-070904 |
| Report user agreement with the AI and reasons for variation | DECIDE-AI (DA-82) |
| Report significant errors or malfunctions | DECIDE-AI (DA-83) |
| Report usability evaluation and user learning curves | DECIDE-AI (DA-84) |
| A model card is offered as an example format in a draft (January 2025, not for implementation) | FDA AI-enabled device software functions draft (DA-35, DA-46) |
| In the NHS, local performance of AI can be checked in silent mode before use in care | NICE Evidence Standards Framework, last updated 9 August 2022, standard 15 (CS60) |
| Communication of outputs, features, benefits and limitations (for example a model card) and an end-user training approach | NICE ESF standard 20 (CS65) |

Designing the live evaluation study is `dh-clinical-development` study-protocol-and-endpoint-design. Measuring agreement after go-live is `analytics-adoption-and-impact-monitoring` (this pack).

## 9. Fairness when the product allocates

Fairness concerns apply to polar decisions such as allocating a scarce resource, and fairness criteria are mutually incompatible (Paulus and Kent 2020, DA-116, DOI 10.1038/s41746-020-0304-9). A calibrated model cannot have equal sensitivity and specificity at one threshold for two groups with different outcome rates (DA-119). The three axes are equal outcomes, equal performance and equal allocation (Rajkomar 2018, DA-113, DOI 10.7326/M18-1990). Label bias arises when the outcome is differentially ascertained across groups (DA-115, DA-120).

Rule: when a decision product ranks or allocates, the answer names the criteria in conflict, states DA-119, and asks which criterion fits the decision. The model never reports every criterion as pass or fail and never sets a tolerance. Bias assessment of the model itself is `responsible-ai-governance` (this pack).

## 10. Insight delivery and the recommendation (old task method)

DH-05.01.3.3.1 to .3: state the recommended action and the alternative in the decision maker's choice, the evidence with its source, and the condition that would change it ("Do not write a recommendation that restates the data without an action"); deliver it to the person who decides, with the date, the question they asked that could not be answered and the action they chose if they chose; park a question that blocked the action with the missing data, its owner and whether the action waits ("Do not recommend an action that depends on data marked [GAP]").

In this skill the recommendation is the person's (the analyst's or the decision maker's). The model drafts the statement from the person's analysis, labeled "proposed" if the person has not stated the action, and never adds an action the evidence does not reach.
