# Lifecycle stages: the vocabularies the sources name, and what each stage owes

Interpretive reference for A1 (and the stage names used in A2 and B1). Every rule carries its row id from the copied research files: PL (`product-lifecycle-research.md`), TM (`mechanism-and-translation-research.md`), QS and CH (`quality-systems-research.md`). Rows marked [PAPER] are published methods; [WF] rows were read through a summarizing fetch tool.

## The rule that shapes this reference

No source read for this skill sets one stage model for a digital health product. The sources name phases, decision points and records, each from its own angle. The person chooses the stage model their organization uses; this skill maps their stages to the sourced elements and says what each stage owes. If the person has no stage model, the skill lays out the vocabularies below as options, labeled "proposed", and the person picks.

## 1. Four vocabularies the sources give

| Vocabulary | Stages as the source names them | What it is for | Rows |
|---|---|---|---|
| MRC/NIHR complex-intervention framework [PAPER] DOI 10.1136/bmj.n2061 | Development or identification of the intervention; feasibility; evaluation; implementation. A program can start at any phase. | Research phases for a complex intervention (a digital therapy is one where it has several components or targets behavior, TM10) (DOI 10.1136/bmj.n2061) | TM1, TM2, TM10 (DOI 10.1136/bmj.n2061) |
| QMSR design and development (21 CFR 820, effective 2 February 2026, incorporating ISO 13485) | No named phases. Design reviews "at major decision points during the design phase"; design validation includes clinical or performance evaluation; the final design output starts the medical device file. | The device quality system's own checkpoints | QS1, QS3, PL5, PL7, PL10 |
| IDEAL-D [PAPER] DOI 10.1097/SLA.0000000000004907 | Stage 0 (preclinical) added before IDEAL stage 1 (first in human); IDEAL = idea, development, exploration, assessment, long-term follow-up. Only stage 0 is sourced in detail. | Device innovation; its stage 0 rules scale with invasiveness and risk | PL110 to PL113; PL121 (2016 original, abstract only [WF]) (DOI 10.1097/SLA.0000000000004907) |
| FDA total product life cycle (TPLC) | Design and development to real-world use, premarket and postmarket in one CDRH team. Not a stage model for the manufacturer; an FDA organization and a database. | Context for why post-market data feed premarket decisions | PL122 to PL124 |

Say which vocabulary a stage name comes from. Do not mix stage names from two vocabularies in one gate without saying so.

## 2. Rules that hold across vocabularies

| Rule | Rows |
|---|---|
| Repeat a phase rather than move on while key uncertainties remain; phases need not be sequential. | TM3 (DOI 10.1136/bmj.n2061) |
| Six core elements are revisited "especially before moving between phases": context, program theory, stakeholders, key uncertainties, refinement, economic considerations. The paper words them as questions a gate can ask (TM5, DOI 10.1136/bmj.n2061). | TM4, TM5 (DOI 10.1136/bmj.n2061) |
| Write the program theory at the start and refine it in later phases. | TM7 (DOI 10.1136/bmj.n2061) |
| Refinement boundaries are agreed at the start of each phase; refinement is rare during efficacy or effectiveness evaluation. | TM13 (DOI 10.1136/bmj.n2061) |
| A feasibility study tests progression criteria that are predefined. | TM14 (DOI 10.1136/bmj.n2061) |
| Before feasibility, consider an evaluability assessment. | TM15 (DOI 10.1136/bmj.n2061) |
| Economic evaluation is part of every phase. | TM18 (DOI 10.1136/bmj.n2061) |
| The more invasive and risky a device, the more proof of safety and effectiveness before first-in-human (stage 1). | PL113 (DOI 10.1097/SLA.0000000000004907) |
| Design reviews at major decision points; attendees include the functions concerned with the stage under review; the manufacturer chooses who attends. | PL5, PL1 |
| The QMSR dropped the old explicit rule that each design review include someone without direct responsibility for the stage. | QS23, PL1, PL2 |

## 3. What a stage owes: sourced work products

Use this table to fill the "owes" column for the person's stage. Only the person decides that a work product is required for their gate; the table says which source names it.

| Work product | Where a source names it | Rows |
|---|---|---|
| Intended use and SaMD definition statement (significance of information, state of the situation, core functionality) | IMDRF N12; a change to the statement triggers recategorization | PL58, PL59 |
| Program theory (components, interactions, mechanisms, context) | MRC/NIHR framework, from the start | TM6, TM7 (DOI 10.1136/bmj.n2061) |
| Key uncertainties and progression criteria | MRC/NIHR feasibility phase | TM4, TM14 (DOI 10.1136/bmj.n2061) |
| Design and development plan and procedures, held in the design and development file | QMSR via ISO 13485 7.3.10 (the former DHF) | PL9, QS24 |
| Design review record covering the elements FDA lists (inputs met for intended use and user needs, verification data against functional, safety, reliability, labeling and regulatory requirements) | QMSR preamble | PL4 |
| Software documentation elements for a premarket submission (ten elements, Basic or Enhanced level) | FDA premarket software guidance (2023) | PL15 to PL20 |
| Risk management file (plan, assessment, report) | FDA premarket software guidance | PL16; the file itself belongs to `dh-regulatory-and-quality` design-controls-and-risk-management |
| Clinical evaluation in three parts: valid clinical association, analytical validation, clinical validation | IMDRF N41; MDCG 2020-1 for the EU | PL62 to PL65, PL68 to PL74 |
| Clinical or performance evaluation inside design validation | QMSR via ISO 13485 7.3.7 | PL7 |
| Final design output that starts the medical device file (design transfer) | QMSR preamble | PL10 |
| Impact assessment of other functions in a multiple function product (negative, positive and no impact, all documented) | FDA multiple function guidance (2020) | PL25, PL27 |
| Stage 0 device-perspective studies (all devices); patient and clinician perspectives (intermediate or high risk); system perspective (high risk) | IDEAL-D stage 0 [PAPER] | PL116, PL117 (DOI 10.1097/SLA.0000000000004907) |
| Clinician learning-curve studies before clinical use, preferably by simulation | IDEAL-D stage 0 [PAPER] | PL119 (DOI 10.1097/SLA.0000000000004907) |
| For a German DiGA application: everything in §§ 3 to 6 DiGAV in place at application (safety, function, quality, data protection and security, interoperability); only the care-effect study may follow under a trial listing | DiGAV and BfArM guide | PL80, PL84 to PL91 |
| For an NHS England route: a DTAC form and evidence per product version [WF] | DTAC | PL98, PL99 |
| Post-market: complaints, PMCF or PMPF, real-world performance and user feedback feed the clinical evaluation update | MDCG 2020-1 | PL76 |

## 4. Boundaries a stage map must state

- Whether the product is a device, its class, and its pathway: not decided here. General wellness (6 January 2026 version), enforcement discretion, multiple function and PDURS (September 2023 draft) rows are context for design (PL45 to PL53, PL30 to PL38); the question goes to `dh-regulatory-and-quality` regulatory-pathway-and-classification.
- IEC 62304 covers software lifecycle processes but not validation and final release of the device (PL105); IEC 82304-1 covers health software products on general platforms (PL103) [abstract page only]. Clause content of either is not read `[GAP]`.
- ISO 13485 7.3 subclause text (planning, transfer, changes) is paywalled and not read; only FDA's restatements are used (research file "Not sourced").
- Stages 1 to 4 of IDEAL-D for devices are not sourced (PL121, abstract only [WF]; research file "Not sourced").
