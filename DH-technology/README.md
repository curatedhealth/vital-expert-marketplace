Install **dh-technology** from `curatedhealth/vital-expert-marketplace`, then paste the Digital Health Library key. The key is not in this pack.

This pack merges eight Digital Health cores. Other Digital Health cores are separate packs.

The connector is `https://mcp.vital.expert/api/mcp/library`. Do not add a second connector.

Choose one heading, then one job. The job holds its tasks as sections. Ask which one task, then follow that section. A missing fact stays a gap.

# dh-technology

This pack replaces eight packs: `dh-data-science` (DH-01.04 Data Science & AI/ML), `dh-advanced-analytics` (DH-05.01 Advanced Analytics & Data Science), `dh-decision-support` (DH-05.02 Decision Support & Business Intelligence), `dh-analytics-product` (DH-05.03 Analytics Product Management & Enablement), `dh-interoperability` (DH-04.01 Clinical Integration & Interoperability), `dh-cybersecurity` (DH-04.02 Cybersecurity & Privacy), `dh-software-engineering` (DH-04.03 Software Engineering Excellence) and two headings of `dh-digital-therapeutic-design` (DH-01.06.1 Personalization Engine and DH-01.06.4 DTx Architecture; DH-01.06.2 and DH-01.06.3 live in `dh-clinical-development`).

People decide in every skill: acceptance criteria, drift, fairness and data quality thresholds, release go or no-go, the IEC 62304 software safety class, security risk acceptance, patch priorities, interoperability scope and adoption targets. No skill supplies a threshold no source sets, presents a draft guidance or proposed rule as a requirement, or writes exploit detail. Start with `technology-capability-map` if unsure.

## Map

- `technology-capability-map`: The map of the VITAL Technology pack for CTOs, CDOs, heads of data science, engineering, security and interoperability in digital health, medtech and pharma.

## DH-01.04 Data Science & AI/ML and DH-01.06.1 Personalization Engine (was dh-data-science and dh-digital-therapeutic-design)

- `clinical-ml-model-development-and-validation`: Develop and validate a clinical ML model or a DTx personalization engine: write the intended use and the decision it may and must not support, check the data split on the team's manifest (leakage, site, time, missing populations) against TRIPOD+AI, PROBAST+AI, EU AI Act Article 10 and the FDA AI draft (labeled draft), specify tailoring rules (decision points, options, missing-data behavior, MRT or MOST tests), compute AUROC, calibration and subgroup results on the locked test set against the team's own criteria, and write the promotion rule and drift watch.
- `model-performance-and-drift-monitoring`: Monitor a released clinical ML model or DTx personalization engine against the team's own rules: check each model's validation and promotion record (intended use, locked test set, metric named before the run, run id, approver, drift watch), read input drift, calibration and performance by period on the team's prediction log (O/E, AUROC, calibration slope, missing share, SMD) and the engine's decision log against its rules, quote recalls as stored, and review each miss with the owner, action and recheck date the team sets.
- `responsible-ai-governance`: Govern a clinical AI or machine learning system in a digital health, medtech or pharma company: map the decision it influences, the harm, the groups it could disadvantage and the rules that may apply (NIST AI RMF, EU AI Act Articles 10 to 15 at their amended dates, 45 CFR 92.210, ONC decision support transparency, FDA CDS Criterion 4, GDPR DPIA, DCB0129); compute subgroup sensitivity, specificity, PPV and calibration on the person's own data; and draft release controls (human oversight, transparency, logging, monitoring, who may accept a gap).
- `responsible-ai-compliance-monitoring`: Check whether a clinical AI or machine learning release holds the responsible-AI evidence it needs, and keep checking after release: build the evidence checklist for the person's markets with each item's standing and date (NIST AI RMF, EU AI Act at its amended dates, GDPR DPIA, 45 CFR 92.210, ONC, FDA CDS, DCB0129), read the person's evidence index for one model version (present, missing, not yet applicable, not assessable; policy in place of a test; evidence on an older model; groups still unseen), add post-release safety events, and review each failed item with the owner, release-waits call and date the person sets.

## DH-01.04.4 Data & Modeling and DH-05.01 Advanced Analytics & Data Science (was dh-data-science and dh-advanced-analytics)

- `data-preparation-and-analytics-methods`: Prepare clinical and real-world data and choose analytics methods: cohort rule, operational definitions, features with leakage refused, data split and versioned handoff (OMOP, FAIR, FDA RWD, EU AI Act Article 10); plan a causal, regression or Bayesian analysis (ICH E9(R1) estimands, FDA covariate and Bayesian guidance); and record the person's choices for a prediction, personalization or forecasting model (label, holdout, threshold, use limit, decision rules).
- `data-quality-monitoring`: Watch the quality of the data behind a digital health model or analysis: write the person's data quality rules in Kahn's categories (conformance, completeness, plausibility; verification and validation) with leak, row-count and version checks; run them on each dataset version and compare versions field by field; and review every failed check with the owner, the repair (feature removed or redefined), the new dataset version and the recheck date the person sets.

## DH-05.02 Decision Support & Business Intelligence, DH-05.03 Analytics Product Management & Enablement and DH-05.01.3 Advanced Analytics Consulting (was dh-decision-support, dh-analytics-product and dh-advanced-analytics)

- `analytics-products-and-decision-support`: Design analytics products and decision support for a digital health, medtech or pharma organization: frame the decision before the data, write the bet and value case, rank analytics use cases on the person's own rule, define and certify metrics (CMS measure specification structure, Kahn data quality, HIPAA minimum necessary), and design executive dashboards, commentary and analytics embedded in clinical workflows with FDA CDS Criterion 4, ONC DSI, 45 CFR 92.210 and EU AI Act oversight facts laid out.
- `analytics-adoption-and-impact-monitoring`: Track whether analytics products and decision support are used and change the decision in a digital health, medtech or pharma organization: an adoption funnel from the person's roster and usage log with valid denominators (RE-AIM, Proctor penetration), practice proof rather than attendance, champion load, issue cadence and stale data, the bet metric against its comparison, user agreement and override reasons (DECIDE-AI), certified metrics whose formula changed, publish rights after role changes, and each miss with the owner and recheck date the person sets.

## DH-04.03 Software Engineering Excellence and DH-01.06.4 DTx Architecture (was dh-software-engineering and dh-digital-therapeutic-design)

- `medical-software-lifecycle-and-delivery`: Plan and run the lifecycle of medical device software, SaMD, DTx and connected health apps: record the safety class and items the team set, check the SOUP inventory, lifecycle plans and FDA software documents, lay out architecture, data flows and cloud placement, design V&V and the CI/CD release pipeline with the evidence it keeps, and prepare release and change decisions for the owner.
- `software-quality-and-delivery-monitoring`: Watch the quality and delivery of medical device software, SaMD and DTx platforms against the team's own rules: trace hazards to V&V cases, find cases run on an older build, check required plans, count deploys, rollbacks and skipped pipeline stages, read capacity and data residency, flag SBOM components past end of support or in a KEV list, read recalls of comparable software, and review each failed element with the owner and recheck date the person sets.

## DH-04.01 Clinical Integration & Interoperability (was dh-interoperability)

- `interoperability-and-ehr-integration`: Design how a digital health, medtech or pharma product exchanges data with EHRs, payers and networks: which FHIR, US Core, SMART, Bulk Data and USCDI versions apply (required for ONC certification kept apart from current HL7 publications), guide and exchange pattern, SMART scopes and sandbox launch, screen-to-FHIR maps, SNOMED CT, LOINC and ICD mapping, CMS-0057-F payer APIs, TEFCA, information blocking, EHDS, DiGA ePA and DTAC; then a conformance gap record and go-live scope for the owner.
- `integration-quality-monitoring`: Check whether a built EHR or FHIR integration of a digital health, medtech or pharma product holds up against the person's rules: score sample exchanges by profile against their check sheet, run the SMART launch matrix by role, patient and encounter state, read terminology map accuracy with blinded clinical review, compare designed and observed clinical steps, read which standards and CMS, ONC or EHDS dates the integration relies on have moved, then review each failure with the owner, release or named acceptance the person sets.

## DH-04.02 Cybersecurity & Privacy (was dh-cybersecurity)

- `cybersecurity-and-privacy-by-design`: Design security and privacy into a digital health product (SaMD, connected device, DTx, remote monitoring, health app): map which regimes the facts point to (HIPAA and BAAs, FTC health breach rule, Washington MHMDA, 42 CFR Part 2, GDPR, FD&C 524B cyber devices, FDA premarket cybersecurity guidance of 3 February 2026, MDR Annex I, Cyber Resilience Act, NIS2, DTAC, DiGA BSI), build data-class, control, consent and reviewer document tables, threat-model each hop, check an SBOM for end of support and KEV entries, and lay out vulnerability response options and clocks.
- `security-and-privacy-operations-monitoring`: Check whether security and privacy work in operation for a digital health product (SaMD, connected device, DTx, remote monitoring, health app or platform): claimed controls against their artifacts, threat-model coverage and currency, consent text against what the system does and whether a withdrawal stops it, open vulnerability age against the team's own windows, closure evidence (deployed version, unexpired named acceptance), repeat failure classes, incidents with the clocks that may apply, and each miss with the owner and recheck date the person sets.

## Shared

- `digital-health-expert`: Find and download a VITAL Digital Health expert (a ready-made role such as the SaMD Regulatory Affairs Director, the Quality & Software Lifecycle Director or the Regulatory Submission Manager) to run on the person's own assistant.

16 skills: 1 capability map, 14 competency skills and the shared `digital-health-expert` skill. Version 0.1.0, 20 October 2026.
