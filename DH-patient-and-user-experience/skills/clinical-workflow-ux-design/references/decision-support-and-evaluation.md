# Decision support transparency and the evaluation plan

Used by B1. `UX-` rows are in `ux-usability-research.md`; `CS` rows in `implementation-research.md`.

Boundary first: whether a function is a device, whether it meets the non-device CDS criteria, and what a marketing submission must contain are decided by the person's regulatory owner (dh-regulatory-and-quality). This file lays out what those sources ask the interface to show, so design options can be compared on it.

## 1. What FDA's CDS Criterion 4 asks the interface to show

Current version: FDA "Clinical Decision Support Software", 29 January 2026, superseding the 6 January 2026 issue (UX-US-64).

| Design element | Rule | Row |
|---|---|---|
| Independent review | Non-device CDS must enable the HCP to independently review the basis for recommendations so they rely on their own judgment. | UX-US-65 |
| Time-critical tasks | Software for a critical, time-sensitive task or decision does not meet Criterion 4. | UX-US-66 |
| Inputs | Software or labeling identifies required inputs, with plain-language instructions on obtaining them, their relevance and data quality needs. | UX-US-67 |
| Algorithm basis | Plain-language description of development and validation: approach, data (to judge representativeness), clinical validation results. | UX-US-68 |
| Knowns and unknowns | Output gives patient-specific information and knowns and unknowns, such as missing, corrupted or unexpected inputs. | UX-US-69 |
| Overload | Basis information promotes usability, prioritizes decision-relevant information, makes extra detail available. | UX-US-70 |
| Testing | Developers may need usability testing to show their implementation meets Criterion 4. | UX-US-71 |
| Automation bias | FDA defines automation bias (errors of commission and omission) and weighs automation level and time pressure. | UX-US-72 |
| Patient-facing | Software that supports or recommends to patients or caregivers, not HCPs, meets the device definition. | UX-US-73 |
| One appropriate option | Where only one option is clinically appropriate and all criteria are otherwise met, FDA intends enforcement discretion. | UX-US-74 |

## 2. ONC decision support interventions (certified health IT)

In force on 19 October 2026 per the eCFR text read; the HTI-5 proposed rule of 29 December 2025 would remove several parts. No final rule was found (research "Changes and conflicts" item 9). Treat as in force but at risk.

| Requirement | Row | HTI-5 proposal |
|---|---|---|
| Interventions occur while the user interacts with the technology | UX-US-54 | Not proposed for removal in the rows read |
| User feedback capture and export | UX-US-55 | Not proposed for removal in the rows read |
| Plain-language source attributes for a limited set of identified users | UX-US-56 | Proposed for removal ((b)(11)(iv) and (v)), UX-US-60 |
| Predictive DSI: intended use, population, users, decision-making role (informs, augments, replaces) | UX-US-57 | Source-attribute requirements proposed for removal, UX-US-60 |
| Predictive DSI: tasks, situations or populations where users are cautioned | UX-US-58 | As above |
| Flag when source-attribute information is not available | UX-US-59 | As above |
| Safety-enhanced design: user-centered design applied to listed capabilities; at least 10 test participants per capability | UX-US-62 | Proposed for removal, UX-US-63 |

ONC's stated basis for removal is that developers report most clinical users lack time or background to engage with source attributes; ONC says this is reported, not a measured study (UX-US-61).

## 3. The evaluation plan: formative now, validation later

| Rule | Row |
|---|---|
| Formative evaluation explores design strengths, weaknesses and unanticipated use errors. | UX-US-29 |
| A formative protocol typically states purpose, UI portion, scenarios and tasks, participants, data collection, analysis, and how results will be used. | UX-US-44 |
| Formative sample sizes vary with information need, complexity and user variability. | UX-M-04 |
| Employees may take part in formative work, with caution about bias; not in validation except where all users are employees. | UX-US-45, UX-US-38 |
| Validation: participants represent intended users, all critical tasks performed, final UI, realistic conditions. | UX-US-34 |
| Validation: at least 15 participants per distinct user population. | UX-US-35 |
| Think-aloud is acceptable in formative work, not in validation. | UX-US-40, UX-M-05 |
| Testing should not follow training immediately; training in the test should match real training. | UX-US-41, CS80 |
| If no formative work is done and flaws appear in validation, the validation test effectively becomes formative. | UX-M-06 |
| FDA encourages a Pre-Submission of the draft validation protocol. Whether to file one is the regulatory owner's decision. | UX-US-46 |
| MHRA sets no fixed sample size; the rationale must be documented. | UX-UK-17 |
| Consent and participant risk are considered even in formative work (MHRA). Whether the Common Rule applies depends on federal funding or regulation and on whether the work is "research" (generalizable knowledge); the person's institution decides. | UX-UK-19, UX-M-11, UX-M-12 |

## 4. Handoff inputs for the regulatory owner (not decided here)

The FDA content guidance, final on 29 May 2026 (UX-US-47), sorts submissions into three HF Submission Categories using decision points A to D (UX-US-48). B1 does not pick a category. It hands over the facts the decision points ask about:

- Decision Point B: is there a change to the user interface, intended users, intended uses, use environments, training or labeling (UX-US-49).
- Critical tasks: none, new, or impacted, from A2 (UX-US-50).
- Decision Point D factors: UI history of use, UI complexity, adequacy of existing risk controls (UX-US-51).
- FDA recommends keeping human factors information whether or not it is submitted (UX-US-53).

## 5. Not in the sources

- Alert fatigue rates, override rates or any numeric threshold for interruptive alerts.
- Whether a given product meets Criteria 1 to 3 of the CDS guidance (not read in this pass, and a regulatory decision in any case).
- EU or UK equivalents of the CDS criteria.
