# Intervention specification rules

Interpretive reference for task A2. Every rule cites its row in `therapeutic-mechanism-and-translation-research.md` (TM rows, read 20 October 2026). DOIs travel with the rows as listed in SKILL.md. Where a fact is not in a row, it is `[GAP]`.

## 1. Development frameworks (the person chooses; none is required)

| Framework | What it names | Rows |
|---|---|---|
| MRC/NIHR 2021 (DOI 10.1136/bmj.n2061) | Four phases: develop or identify, feasibility, evaluation, implementation; a program can start at any phase; repeat a phase rather than move on while key uncertainties remain. Six core elements at every phase: context, program theory, stakeholders, key uncertainties, refinement, economic considerations. | TM2 to TM5 |
| MRC/NIHR feasibility | A feasibility study tests predefined progression criteria about the evaluation design and the intervention (content, delivery, acceptability, adherence, likely cost-effectiveness, provider capacity). | TM14 |
| ORBIT (DOI 10.1037/hea0000161) | Phase Ia define, Ib refine, IIa proof of concept, IIb pilots, then efficacy; milestones set in advance on clinical, not statistical, significance; return to earlier phases allowed; not prescriptive. | TM54 to TM65 |
| MOST (DOI 10.1007/s10461-015-1145-4; DOI 10.1177/26334895211054363) | Preparation, optimization, evaluation; an optimization objective set in preparation (older papers say "criterion"); EASE: effectiveness balanced against affordability, scalability, efficiency; optimization trials test components, not the package. | TM66 to TM76 |

The research file notes the "criterion" and "objective" terms are the same concept; prefer the newer term (Changes and conflicts item 2).

## 2. Program theory

| Rule | Rows |
|---|---|
| Program theory states key components and how they interact, mechanisms, contextual features that influence mechanisms, and how mechanisms might influence context. | TM6 |
| Develop it at the start with diverse stakeholders from evidence and theory; refine it through later phases. | TM7 |
| Context is any feature of the circumstances in which the intervention is conceived, developed, evaluated and implemented. | TM9 |
| Refinements follow the program theory within boundaries agreed at the start of each phase, with the rationale reported; refinement is rare during efficacy or effectiveness evaluation. | TM13 |
| When adapting an existing intervention, a developed program theory shows what to adapt and which key mechanisms to retain. | TM20 |

## 3. Describing the intervention: TIDieR (DOI 10.1136/bmj.g1687)

Items 1 brief name, 2 why, 3 materials, 4 procedures, 5 who provided, 6 how, 7 where, 8 when and how much, 9 tailoring, 10 modifications, 11 how well (planned), 12 how well (actual) (TM22 to TM33). Items 10 and 12 cannot be completed for a protocol (TM34); the same holds for a specification written before delivery. N/A for items that do not apply; "?" when a reviewer finds an item unreported (TM36). TIDieR extends CONSORT 2010 item 5 and SPIRIT 2013 item 11 (TM35); whether the 2025 versions renumber those items was not checked (research file "Already sourced elsewhere"). TIDieR-PHP (TM37, TM38) is for population health and policy programs only.

## 4. Behavior change functions (DOI 10.1186/1748-5908-6-42)

| Rule | Rows |
|---|---|
| COM-B: capability, opportunity and motivation interact to produce behavior; six subcomponents (physical and psychological capability, physical and social opportunity, reflective and automatic motivation). | TM40 to TM44 |
| Nine intervention functions: education, persuasion, incentivisation, coercion, training, restriction, environmental restructuring (example: on-screen prompts), modelling, enablement. One intervention may perform several. | TM46 to TM48, TM50 |
| Seven policy categories sit outside the functions; they matter for health-system programs, not app features. | TM49 |
| BCT Taxonomy v1: 93 techniques in 16 groups. Abstract only: the list and group names were not read. Any technique name comes from the person and is labeled. | TM51 to TM53 |

## 5. Decision rules for adaptive features (DOI 10.1007/s12160-016-9830-8)

| Rule | Rows |
|---|---|
| Four components: decision points, intervention options, tailoring variables, decision rules; one decision rule per decision point. | TM77 to TM80, TM82 |
| Tailoring variables come from active (self-report) or passive (sensor) assessment. | TM81 |
| Distal outcome is the ultimate goal, usually the primary clinical outcome; proximal outcomes are the short-term goals of each option, often mediators. | TM83, TM84 |
| Include proximal outcomes for engagement and fatigue. | TM87 |
| Unreliable tailoring variables make a rule little better than random; invalid ones may recommend counterproductive options. | TM88 |
| Plan in advance how each rule behaves when tailoring data are missing. | TM89 |
| A micro-randomized trial randomizes options at many decision points to estimate effects on proximal outcomes (design option only; protocols belong to dh-clinical-development). | TM90 |

## 6. Dose and regimen

| Rule | Rows |
|---|---|
| TIDieR item 8 asks for number of sessions, schedule, duration, intensity or dose. | TM29 |
| A DiGA application states the minimum duration of use the manufacturer considers necessary. | TM150 |
| 882.5804 (fibromyalgia, 26 June 2026) labeling states recommended treatment regimens including frequency and duration of use; 886.5500 (amblyopia, 22 April 2026) labeling states treatment and retreatment length supported by clinical testing. | TM126, TM130 |
| Precedents: reSET recommends 4 lessons per week of 10 to 20 minutes, core lessons unlock in sequence (TM134); EndeavorRx enforces about 25 minutes per day, 5 days per week by lock-out and reminders (TM142). | TM134, TM142 |

## 7. Core and adaptable

| Rule | Rows |
|---|---|
| Deconstruct the intervention into components and agree permissible and prohibited variation in advance. | TM11 |
| Standardization can apply to function rather than form. | TM12 |
| Adaptation in implementation is acceptable if key functions are maintained and adaptations understood. | TM19 |
| Define core components (tied to the logic pathway) where fidelity is expected and aspects sites may adapt. | TM117 |
| A treatment manual fixed in Phase II is the basis for training and fidelity monitoring. | TM61 |

## 8. Regulatory texts that name a model of therapy (context only)

882.5801 requires describing a validated model of behavioral therapy and validating it as implemented, and software documentation showing the device implements it (TM120, TM121). 876.5960, 880.5735 and 890.5800 use similar wording (TM127 to TM129). 882.5803, 882.5705 and 886.5500 do not use "model of therapy" wording (Changes and conflicts item 7). Whether any regulation applies to the person's product is the question for `dh-regulatory-and-quality` regulatory-pathway-and-classification.
