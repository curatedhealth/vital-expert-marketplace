Install **dh-clinical-development** from `curatedhealth/vital-expert-marketplace`, then paste the Digital Health Library key. The key is not in this pack.

This pack merges two Digital Health cores. Other Digital Health cores are separate packs.

The connector is `https://mcp.vital.expert/api/mcp/library`. Do not add a second connector.

Choose one heading, then one job. The job holds its tasks as sections. Ask which one task, then follow that section. A missing fact stays a gap.

# Clinical Development (DH)

Replaces two packs: dh-clinical-product-development (DH-01.01) and dh-clinical-validation (DH-01.02); also routes the folded DH-01.06.2 Safety & Efficacy and DH-01.06.3 Engagement Mechanics headings.

## Pack map

- `clinical-development-capability-map` (DH-01.01; DH-01.02): The map of the VITAL Clinical Development pack for digital health products: clinical product development and clinical validation.

## DH-01.01.1 Product Development

- `clinical-product-lifecycle-and-stage-gates` (DH-01.01.1.1): Run the lifecycle of a clinical digital health product (DTx, DiGA, SaMD): name the stage and what it owes, define the next increment and what each gate needs, and write the stage gate record against the team's criteria.
- `lifecycle-quality-monitoring` (DH-01.01.1.2): Watch the health of a clinical digital health product's lifecycle (DTx, DiGA, SaMD) against measures the team sets: define a healthy stage move, read the gate log per stage (owed items present or missing, days open, accepted with no evidence, next stage started while blocked), list post-market register events as the records state them, and review each miss with its owner, block and reread date.

## DH-01.01.2 Therapeutic Design

- `mechanism-validation-monitoring` (DH-01.01.2.2): Check whether a digital therapeutic or DiGA works as designed and stays within its safety and efficacy limits: plan the evidence for each mechanism link, check a study or cohort link by link against thresholds set in advance, read usage and dropout against the person's definitions (DiGAV § 23c for a DiGA), read complaints, events, use errors and efficacy drift against thresholds set before launch, and handle each miss with the team's named owner.
- `therapeutic-mechanism-and-intervention-design` (DH-01.01.2.1): Design how a digital therapeutic, DiGA or software therapy works and stays safe: mechanism of action, components tied to each link (TIDieR, COM-B, decision rules), engagement mechanics (behavioral mechanics, loops and adherence features tied to a link; effective engagement, not usage; dark-pattern and incentive limits), safety by design (risks to health, mitigations, labeling) and the assumptions that would stop it.

## DH-01.01.3 Cross-Functional Integration

- `cross-functional-product-integration` (DH-01.01.3.1): Map the handoffs between clinical science, software, quality, regulatory, operations and implementation on a digital health product (DTx, DiGA, SaMD, app): what moves from whom to whom, which decision waits on it, who attends the design review, which dependencies are open with a late path, and a record of decisions that needed more than one function.
- `integration-and-handoff-monitoring` (DH-01.01.3.2): Check how handoffs between clinical science, software, quality, regulatory, operations and implementation are going on a digital health product (DTx, DiGA, SaMD, AI tool, app): write down what counts as received before scoring, score every handoff due in a period as received, late, open or not measurable with critical ones kept apart, and for each one that did not arrive name the owner who owes it, the blocked decision and the date to look again.

## DH-01.01.4 Clinical Science Translation

- `evidence-to-intervention-translation` (DH-01.01.4.1): Turn clinical evidence into what a digital health product (DTx, DiGA, SaMD) does and says: map each product claim to the passage that supports it or mark it [GAP], write the intervention as a buildable specification (program theory, TIDieR items, behavior change functions, decision rules, dose), and write the translation limits: populations, doses and outcomes the evidence does not cover and the features that stay off.
- `translation-fidelity-monitoring` (DH-01.01.4.2): Check that a digital health product (DTx, DiGA, SaMD, app-based therapy) still says and does what its evidence supports, release after release: write the fidelity rules (core components, permitted variation, fails such as a wider population, a stronger verb or a dropped caveat), sample the claims and decision rules shipped in a version and quote every word that differs from the source, measure delivered dose against the regimen from usage logs, and route each failure to the owner the person names with the version that must not ship it.

## DH-01.02.1 Clinical Study Design

- `study-design-quality-monitoring` (DH-01.02.1.2): Check whether a digital health study protocol (DTx, DiGA, SaMD, AI tool, wearable or app-captured endpoint) will hold up, and keep it holding up: every SPIRIT 2025 item addressed, the estimand and digital-measure duties present, the registry record matching the protocol and the paper, registration and results clocks, amendments tracked, and a robustness review against the pass rules the team sets, with an owner for every miss.
- `study-protocol-and-endpoint-design` (DH-01.02.1.1): Design the clinical study for a digital health product (DTx, DiGA, SaMD, AI tool, remote monitoring, wearable or app-captured endpoint): pick endpoints and clinical outcome assessments from what comparable registered trials used, check whether a digital measure is fit for purpose (verification and validation), draft a protocol that covers every SPIRIT 2025 item, write the estimand, and lay out the statistical analysis plan decisions for the statistician.

## DH-01.02.2 Evidence Communication

- `evidence-communication-monitoring` (DH-01.02.2.2): Check whether the evidence a regulated digital health product (DTx, SaMD, DiGA) communicates stayed true and was disclosed on time: registration, results posting and publication per trial against 42 CFR Part 11, EU CTR Article 37, ICMJE and the WHO pledge; a fidelity audit of abstracts, lay summaries, payer narratives, slides and reviews against their passages and certainty ratings; and a review against the person's own pass rules, with owners and responses.
- `evidence-translation-and-communication` (DH-01.02.2.1): Turn the clinical evidence for a regulated digital health product (DTx, SaMD, DiGA, remote monitoring, digital mental health) into statements people can rely on: a per-outcome evidence statement with passages checked and certainty worded as the person or HTA body rated it, a registration, results-posting and publication plan (42 CFR Part 11, EU CTR Article 37, ICMJE, CONSORT 2025, CONSORT-AI, TRIPOD+AI), and evidence narratives per audience (payer, clinician, lay) inside the sourced communication rules.

## DH-01.02.3 Clinical Operations

- `decentralized-trial-operations` (DH-01.02.3.1): Set up and run the operations of a clinical trial with decentralized elements for a digital health product or a trial that uses digital health technologies (DHTs): which visits are remote, at site or the participant's choice, remote consent, local health care providers, wearables and apps as data acquisition tools, source data, data flow, verification, validation and usability evidence, same method across arms, audit trails and system validation.
- `trial-operations-monitoring` (DH-01.02.3.2): Check how a running clinical trial of a digital health product, or a trial with decentralized elements, is executing: enrollment, retention, protocol deviations and data completeness by site and by arm, computed from the person's own export; registration, update and results-reporting clocks under 42 CFR Part 11, EU CTR Article 37, ICMJE and the WHO joint statement; and a review of which sites miss the person's rules, where execution stalls, who owns it and what responds.

## DH-01.02.4 Digital Evidence Generation

- `evidence-quality-and-signal-monitoring` (DH-01.02.4.2): Check whether a literature review or evidence base for a digital health product (DTx, SaMD, DiGA, app or sensor data) is still current and how far it can be trusted, then frame the update decision.
- `literature-and-real-world-evidence-review` (DH-01.02.4.1): Run a literature and real-world evidence review for a digital health product (DTx, SaMD, DiGA, app or sensor endpoints) the way Cochrane, NICE, IQWiG and the EU JCA expect: PICO, protocol, search strings, PRESS, PRISMA-S and registration; screening, deduplication, extraction and risk of bias (RoB 2, RoB 1 for a JCA, ROBINS-I) with library design labels checked against the paper; GRADE, Summary of Findings, PRISMA 2020 flow and evidence table.

## Shared

- `digital-health-expert` (shared): Find and download a VITAL Digital Health expert (a ready-made role such as the SaMD Regulatory Affairs Director, the Quality & Software Lifecycle Director or the Regulatory Submission Manager) to run on the person's own assistant.
