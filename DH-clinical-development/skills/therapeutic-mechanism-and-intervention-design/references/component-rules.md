# Component rules

Interpretive reference for A2. Every rule cites its row in `therapeutic-mechanism-research.md` (TM). The person decides which components ship, what may vary and the optimization objective; this file lists the elements the sources name.

## 1. Tie each component to one link

| Rule | Rows |
|---|---|
| Deconstruct the intervention into components and agree in advance what variation is permitted and what is prohibited. | TM11 (MRC/NIHR, DOI 10.1136/bmj.n2061) |
| Standardization can apply to function rather than form: the function a component serves is what stays fixed. | TM12 (MRC/NIHR, DOI 10.1136/bmj.n2061) |
| Define core components (ideally tied to the logic pathway) to which fidelity is expected, and aspects sites may adapt. | TM117 (StaRI, DOI 10.1136/bmj.i6795) |
| Content is the intervention's "active ingredients". | TM104 (Carroll, DOI 10.1186/1748-5908-2-40) |
| Detailed, specific interventions are more likely to be implemented with high fidelity than vague ones. | TM106 (Carroll, DOI 10.1186/1748-5908-2-40) |
| Adaptation for a new context keeps key functions; a program theory shows which mechanisms to retain. | TM19, TM20 (MRC/NIHR, DOI 10.1136/bmj.n2061) |

Old task rule kept: a component that cannot be tied to a link in the mechanism is named as left out of this version, with the reason. "Left out" is the person's decision; the model may label a candidate "proposed for removal".

## 2. Describe each component with TIDieR

TIDieR (DOI 10.1136/bmj.g1687) is a 12-item checklist taken here from the official EQUATOR file (TM21). It extends CONSORT 2010 item 5 and SPIRIT 2013 item 11 (TM35); whether the 2025 versions renumber those items was not checked (research file "Already sourced elsewhere").

| Item | Ask of each component | Row |
|---|---|---|
| 1 Brief name | Name or phrase | TM22 |
| 2 Why | Rationale, theory or goal of the essential elements (the link it serves) | TM23 |
| 3 What: materials | Materials given to users or used in delivery or training, and where they are accessed | TM24 |
| 4 What: procedures | Each procedure, activity or process, including enabling or support activities | TM25 |
| 5 Who provided | Each provider category, expertise and training (for a software-only component: none, or the clinician step around it) | TM26 |
| 6 How | Mode of delivery (for example internet), individual or group | TM27 |
| 7 Where | Type of location and needed infrastructure | TM28 |
| 8 When and how much | Number of times, period, sessions, schedule, duration, intensity or dose | TM29 |
| 9 Tailoring | Planned personalization, titration or adaptation: what, why, when, how | TM30 |
| 10 Modifications | Not completed for a protocol or a design | TM31, TM34 |
| 11 How well: planned | How adherence or fidelity will be assessed and maintained | TM32 |
| 12 How well: actual | Not completed for a protocol or a design | TM33, TM34 |

Mark each item filled, N/A (stated by the person) or "?" (not reported) as the checklist instructs (TM36). Never turn "?" into N/A.

## 3. Name the intervention function (BCW) and, if asked, the techniques

| Rule | Rows |
|---|---|
| Nine intervention functions: education, persuasion, incentivization, coercion, training, restriction, environmental restructuring, modelling, enablement (definitions in the rows). One intervention may perform several functions. | TM46 to TM48, TM50 (BCW, DOI 10.1186/1748-5908-6-42) |
| Interventions change behavior; policies (seven categories) enable interventions. A payer or employer rollout is a policy category, not a component. | TM45, TM49 (BCW, DOI 10.1186/1748-5908-6-42) |
| BCT Taxonomy v1 holds 93 techniques in 16 groups and aims to specify active content precisely. Abstract only: the list and group names were not read, so this skill cannot check a technique label. Say so whenever BCTTv1 is applied; accept the person's BCT labels as theirs. | TM51 to TM53 (abstract only, DOI 10.1007/s12160-013-9486-6) |

## 4. Adaptive components: decision rules

Where a component adapts to the user (JITAI, DOI 10.1007/s12160-016-9830-8):

| Element | What to specify | Rows |
|---|---|---|
| Decision points | When an intervention decision is made | TM77, TM78 (JITAI, DOI 10.1007/s12160-016-9830-8) |
| Intervention options | Types, sources, amounts and media of support available at each point | TM79 (JITAI, DOI 10.1007/s12160-016-9830-8) |
| Tailoring variables | Information about the person used to decide when and which option; active (self-report) or passive (sensor) | TM80, TM81 (JITAI, DOI 10.1007/s12160-016-9830-8) |
| Decision rules | Which option, for whom, when; one rule per decision point | TM82 (JITAI, DOI 10.1007/s12160-016-9830-8) |
| Missing data | How each rule behaves when tailoring data are missing, planned in advance | TM89 (JITAI, DOI 10.1007/s12160-016-9830-8) |
| Measurement quality | Unreliable tailoring variables make a rule little better than random; invalid ones may recommend a counterproductive option | TM88 (JITAI, DOI 10.1007/s12160-016-9830-8) |
| Proximal outcomes | Short-term goal of each option, including engagement and fatigue | TM84, TM87 (JITAI, DOI 10.1007/s12160-016-9830-8) |
| Receptivity | Transient ability or willingness to receive and use support | TM86 (JITAI, DOI 10.1007/s12160-016-9830-8) |

Precedent (decision summary, not the person's product): EndeavorRx's adaptive algorithms adjust difficulty per patient in a closed loop, and the regimen is enforced by lock-out and reminders (TM142). Building the engine belongs to `dh-digital-therapeutic-design` (heading DH-01.06.1 Personalization Engine).

## 5. Optimization: which components, at what cost

| Rule | Rows |
|---|---|
| MOST has three phases: preparation, optimization, evaluation. Preparation builds a conceptual model, selects discrete components and pilot tests them. | TM66, TM68 (MOST 2016, DOI 10.1007/s10461-015-1145-4) |
| The optimization criterion (newer term: optimization objective) is set in preparation: an operational definition of the "best" intervention under constraints, for example "Most effective that can be delivered in under one hour". The objective is the person's. | TM69 (MOST 2016, DOI 10.1007/s10461-015-1145-4), TM74, TM75 (MOST 2021, DOI 10.1177/26334895211054363) |
| EASE: effectiveness balanced against affordability, scalability and efficiency; efficiency means only components that actively and positively contribute. | TM74 (MOST 2021, DOI 10.1177/26334895211054363) |
| A component selection experiment (often factorial) estimates each component's effect and interactions; it does not test the package. | TM67, TM71, TM72 (MOST 2016, DOI 10.1007/s10461-015-1145-4), TM76 (MOST 2021, DOI 10.1177/26334895211054363) |
| Scalable means implementable with fidelity without ad hoc cuts of unknown effect. | TM70 (MOST 2016, DOI 10.1007/s10461-015-1145-4) |
| ORBIT Phase Ib: examine candidate components together, identify those essential with independent effects, and study mode, agent, frequency and duration of delivery. | TM59 (ORBIT, DOI 10.1037/hea0000161) |

Where the person has scored candidate components on criteria they chose, `analytics.mcda` or `analytics.rice` may rank those scores; the tools do not score (`references/tools.md`).
