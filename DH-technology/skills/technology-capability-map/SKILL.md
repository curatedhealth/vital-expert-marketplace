---
name: technology-capability-map
description: >
  The map of the VITAL Technology pack for CTOs, CDOs, heads of data science,
  engineering, security and interoperability in digital health, medtech and pharma. Use
  it when someone asks "what can the technology pack do", "which skill do I need", or
  names a topic without a skill: model validation, drift, personalization engine,
  responsible AI, fairness, data quality, causal analysis, dashboards, metric
  certification, analytics adoption, IEC 62304, CI/CD, DTx architecture, FHIR, SMART,
  USCDI, EHR integration, threat model, SBOM, vulnerabilities, HIPAA, consent. It routes to one of 14 competency skills and maps every old DH-01.04,
  DH-05.01, DH-05.02, DH-05.03, DH-04.01, DH-04.02, DH-04.03, DH-01.06.1 and DH-01.06.4
  skill. It never does the work, sets a threshold, picks a release or writes exploit
  detail. Not for device pathways (dh-regulatory-and-quality
  regulatory-and-quality-capability-map) or clinical studies (dh-clinical-development
  clinical-development-capability-map).
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Routing only. Needs no connector. The competency skills it routes to run on their
  sourced references and the person's own files, and use the VITAL Digital Health
  Library connector (mcp.vital.expert) mainly for regulatory records, safety events,
  literature and Verify.
metadata:
  name: "technology-capability-map"
  pack: "dh-technology"
  framework_code: "DH-01.04; DH-05.01; DH-05.02; DH-05.03; DH-04.01; DH-04.02; DH-04.03; DH-01.06.1; DH-01.06.4"
  register_code: "CF-12.01.04; CF-12.05.01; CF-12.05.02; CF-12.05.03; CF-12.04.01; CF-12.04.02; CF-12.04.03; CF-12.01.06.1; CF-12.01.06.4"
  framework_path: "DH-01 > DH-01.04 Data Science & AI/ML; DH-05 > DH-05.01 Advanced Analytics & Data Science; DH-05.02 Decision Support & Business Intelligence; DH-05.03 Analytics Product Management & Enablement; DH-04 > DH-04.01 Clinical Integration & Interoperability; DH-04.02 Cybersecurity & Privacy; DH-04.03 Software Engineering Excellence; DH-01 > DH-01.06 Digital Therapeutic Design > DH-01.06.1 Personalization Engine and DH-01.06.4 DTx Architecture"
  worker: "not bound (routing only)"
  version: "0.1.0-draft"
  replaces: "DH-01.04 Data Science & AI/ML and its heading menus DH-01.04.1 to DH-01.04.4; DH-05.01 Advanced Analytics & Data Science and DH-05.01.1 to .3; DH-05.02 Decision Support & Business Intelligence and DH-05.02.1 to .3; DH-05.03 Analytics Product Management & Enablement and DH-05.03.1 to .3; DH-04.01 Clinical Integration & Interoperability and DH-04.01.1 to .4; DH-04.02 Cybersecurity & Privacy and DH-04.02.1 to .4; DH-04.03 Software Engineering Excellence and DH-04.03.1 to .4; DH-01.06 Digital Therapeutic Design menu (DH-01.06.1 and DH-01.06.4 parts) and its heading menus DH-01.06.1 and DH-01.06.4"
---

# Technology: capability map

Framework position: **DH-01.04 Data Science & AI/ML**, the three analytics cores **DH-05.01 Advanced Analytics & Data Science**, **DH-05.02 Decision Support & Business Intelligence** and **DH-05.03 Analytics Product Management & Enablement**, the three engineering cores **DH-04.01 Clinical Integration & Interoperability**, **DH-04.02 Cybersecurity & Privacy** and **DH-04.03 Software Engineering Excellence**, and two headings of **DH-01.06 Digital Therapeutic Design** (DH-01.06.1 Personalization Engine, DH-01.06.4 DTx Architecture), now one pack (`dh-technology`). This skill replaces the eight old core menus and their heading menus. It does one job: show the person what the pack covers and send them to the one competency skill that fits the request.

## What this skill does and does not do

It reads the request, matches it to a competency, names that skill (and the task where it helps), and says in one line why. If two skills fit, it names both and the order. It does not answer the technical question itself, call a connector, or state any rule, standard version, threshold, score or record. Those live in the competency skills, each with its own sourced references.

People decide in every skill of this pack: model acceptance criteria, drift and fairness thresholds, data quality limits, release go or no-go, the IEC 62304 software safety class, security risk acceptance, patch priorities, interoperability scope and adoption targets are the person's. No skill supplies a threshold no source sets; drafts and proposed rules are never presented as requirements; no skill writes exploit code or attack steps.

If the named skill is not available in this assistant, say so and name the pack to install (`dh-technology`). Do not do the competency's work from this map.

## The framework tree

Each heading has a skill that does the work (design, specification, computation) and one that checks it over time. The monitoring skill always works from the rules, thresholds and dates the person sets; it never sets its own and never scores a person.

**DH-01.04 and DH-01.06.1: Clinical AI and machine learning**

- `clinical-ml-model-development-and-validation` (DH-01.04.3.1; folds DH-01.04.2.1 and DH-01.06.1.1). Intended use and validation plan with a split check on the team's manifest, personalization rule specification, and the validation record, promotion rule and drift watch against the team's own criteria.
- `model-performance-and-drift-monitoring` (DH-01.04.3.2; folds DH-01.04.2.2 and DH-01.06.1.2). Record completeness against the team's rule, drift, calibration and engine-behavior reads on the team's logs, and review of each miss with owner, action and recheck date.
- `responsible-ai-governance` (DH-01.04.1.1). AI system and harm map, subgroup performance test, release controls and who may accept a difference.
- `responsible-ai-compliance-monitoring` (DH-01.04.1.2). Release evidence checklist and read, governance review with miss owners.

**DH-01.04.4 and DH-05.01: Data and analytics methods**

- `data-preparation-and-analytics-methods` (DH-01.04.4.1; folds DH-05.01.1 and DH-05.01.2). Cohort, features and data handoff; statistical and causal analysis plan; prediction, personalization and forecasting choices.
- `data-quality-monitoring` (DH-01.04.4.2). Data quality rules in Kahn's categories, reads per dataset version, review and feature repair.

**DH-05.02, DH-05.03 and DH-05.01.3: Analytics products and decision support**

- `analytics-products-and-decision-support` (DH-05.02 and DH-05.03 design halves; folds DH-05.01.3). Decision frame and use-case portfolio, metric definition and certification, decision support design and delivery.
- `analytics-adoption-and-impact-monitoring` (DH-05.02 and DH-05.03 monitoring halves). Adoption and literacy read, cadence, outcome and governance read, impact review with miss owners.

**DH-04.03 and DH-01.06.4: Medical software engineering**

- `medical-software-lifecycle-and-delivery` (DH-04.03.4.1; folds DH-04.03.1.1, DH-04.03.2.1, DH-04.03.3.1 and DH-01.06.4.1). Lifecycle plan and architecture, verification, validation and release pipeline, release and change decision.
- `software-quality-and-delivery-monitoring` (DH-04.03.2.2 and DH-04.03.4.2; folds DH-04.03.1.2, DH-04.03.3.2 and DH-01.06.4.2). V&V completeness and compliance read, delivery and platform read, release gate and miss owners.

**DH-04.01: Interoperability**

- `interoperability-and-ehr-integration` (DH-04.01.1.1 to DH-04.01.4.1). Standards and exchange architecture (certification versions kept apart from current publications), EHR launch and terminology mapping, conformance gaps and go-live scope.
- `integration-quality-monitoring` (DH-04.01.1.2 to DH-04.01.4.2). Conformance and launch checks, mapping, workflow and standards read, integration review with miss owners.

**DH-04.02: Security and privacy**

- `cybersecurity-and-privacy-by-design` (DH-04.02.1.1 to DH-04.02.4.1). Privacy and compliance map, threat model and security architecture with the SBOM, vulnerability response and risk acceptance.
- `security-and-privacy-operations-monitoring` (DH-04.02.1.2 to DH-04.02.4.2). Control, threat model and consent assurance, vulnerability and incident read, review with miss owners.

## Which skill do I need

| If the person asks about | Go to | Why |
|---|---|---|
| Intended use of a model, test set, data split, external validation, TRIPOD+AI, PROBAST+AI, AUROC and calibration on a locked test set, model card, promotion rule | `clinical-ml-model-development-and-validation` | Building and validating the model |
| Adaptive rules, tailoring, JITAI, personalization engine spec, micro-randomized or MOST tests | `clinical-ml-model-development-and-validation` (A2) | The engine's rules are specified with the model |
| "Is our model drifting", calibration over time, production models without a run id, a fired drift watch, the engine's decision log | `model-performance-and-drift-monitoring` | The model after release |
| Bias question, which group could be harmed, subgroup error rates, fairness criterion choice, release controls, 45 CFR 92.210, AI governance | `responsible-ai-governance` | Governing the AI system |
| Responsible-AI release evidence, is the bias test on file, governance misses | `responsible-ai-compliance-monitoring` | Evidence over time |
| Cohort rule, feature definitions, leakage in features, OMOP, data handoff, causal question, regression, Bayesian analysis, forecasting | `data-preparation-and-analytics-methods` | Data and methods |
| Data quality checks, Kahn conformance, completeness, plausibility, dataset version changes, feature repair | `data-quality-monitoring` | Data quality over time |
| Which decision an analysis changes, use-case value and priority, semantic layer, metric certification, dashboards, executive reporting, commentary, embedding analytics in workflow | `analytics-products-and-decision-support` | Analytics product design |
| Are dashboards used, adoption funnel, data literacy, champions, reporting cadence, did the decision change | `analytics-adoption-and-impact-monitoring` | Analytics in use |
| IEC 62304 safety class as set, SOUP, lifecycle plans, FDA software documentation, DTx or SaMD architecture, cloud placement, V&V, CI/CD for device software, release decision | `medical-software-lifecycle-and-delivery` | Building and releasing medical software |
| Trace from hazard to test, build under test, plan completeness, deploy failures, skipped pipeline stages, capacity and residency, platform performance | `software-quality-and-delivery-monitoring` | Software quality over time |
| FHIR, US Core, SMART on FHIR, Bulk Data, USCDI versions, ONC certification, exchange pattern, EHR sandbox launch, terminology mapping, TEFCA, CMS-0057-F, EHDS | `interoperability-and-ehr-integration` | Designing the integration |
| Profile conformance of sample exchanges, launch matrix, map accuracy, workflow fit after go-live, standards that moved | `integration-quality-monitoring` | The integration over time |
| HIPAA, BAA, GDPR legal basis, consent design, threat model, trust boundaries, SBOM, 524B, premarket cybersecurity, vulnerability intake, risk acceptance | `cybersecurity-and-privacy-by-design` | Security and privacy design |
| Control evidence, threat model coverage, consent versus practice, withdrawal test, open vulnerability age, incidents, repeat failures | `security-and-privacy-operations-monitoring` | Security and privacy in operation |

Tie-breakers:

1. Model or data: the model's validation and performance go to the clinical AI pair; the dataset behind it (cohort, features, quality) goes to `data-preparation-and-analytics-methods` and `data-quality-monitoring`.
2. Validation or fairness: computing subgroup results against the team's acceptance criteria is `clinical-ml-model-development-and-validation` B1; the harm map, the bias question and who may accept a difference is `responsible-ai-governance`.
3. Clinical model or analytics product: a model that is or feeds a device function goes to the clinical AI pair; a dashboard, metric or business decision support goes to the analytics pair. A clinical decision support function inside an EHR may need both; start with the clinical AI pair.
4. Personalization: the engine's rules and tests are `clinical-ml-model-development-and-validation` A2; a recommendation or personalization policy for a business analytic (old DH-05.01.2.2) is `data-preparation-and-analytics-methods` B1; the therapeutic content is `dh-clinical-development` therapeutic-mechanism-and-intervention-design.
5. Architecture: DTx and SaMD architecture, cloud and release pipeline go to `medical-software-lifecycle-and-delivery`; integration with EHRs goes to `interoperability-and-ehr-integration`; trust boundaries and threats go to `cybersecurity-and-privacy-by-design`.
6. Design and specification come before monitoring. If nothing has been specified, set or recorded yet, the monitoring skill has nothing to check; send the person to its partner first.
7. If the request is vague ("help with our AI platform"), ask one question: is this about the model, the data, analytics for business users, the software lifecycle, integration, or security and privacy? Then route.

## Old skills and where they went

When a person names an old skill or task (old names quoted as they were, in their original spelling), route as follows. The old folder-by-folder table is in the pack's build notes (pack-structure.md).

### DH-01.04 Data Science & AI/ML (old pack dh-data-science)

| Old skill or task | Go to | Task there |
|---|---|---|
| "DH-01.04 Data Science & AI/ML" (core menu); heading menus "DH-01.04.1 Responsible AI", "DH-01.04.2 MLOps & Monitoring", "DH-01.04.3 Model Development & Validation", "DH-01.04.4 Data & Modeling" | this map | none |
| DH-01.04.1.1.1 "Bias question" | `responsible-ai-governance` | A1 AI system and harm map |
| DH-01.04.1.1.2 "Bias test" | `responsible-ai-governance` | A2 Subgroup performance test |
| DH-01.04.1.1.3 "Governance control" | `responsible-ai-governance` | B1 Release controls and acceptance |
| DH-01.04.1.2.1 "Governance evidence" | `responsible-ai-compliance-monitoring` | A1 Release evidence checklist |
| DH-01.04.1.2.2 "Release score" | `responsible-ai-compliance-monitoring` | A2 Release evidence read (pass or fail in B1) |
| DH-01.04.1.2.3 "Governance miss" | `responsible-ai-compliance-monitoring` | B1 Governance review and miss owners |
| DH-01.04.2.1.1 "Model promotion rule", .2 "Pipeline run", .3 "Drift watch" | `clinical-ml-model-development-and-validation` | B1 Validation record and promotion (steps 6 and 7) |
| DH-01.04.2.2.1 "MLOps check", .2 "Promotion score" | `model-performance-and-drift-monitoring` | A1 Record completeness check (whether a watch fired is also read in A2) |
| DH-01.04.2.2.3 "Drift response" | `model-performance-and-drift-monitoring` | B1 Performance review and miss owners |
| DH-01.04.3.1.1 "Clinical model intended use", .2 "Validation dataset" | `clinical-ml-model-development-and-validation` | A1 Intended use and validation plan |
| DH-01.04.3.1.3 "Validation record" | `clinical-ml-model-development-and-validation` | B1 Validation record and promotion |
| DH-01.04.3.2.1 "Validation completeness", .2 "Validation score" | `model-performance-and-drift-monitoring` | A1 Record completeness check |
| DH-01.04.3.2.3 "Validation miss" | `model-performance-and-drift-monitoring` | B1 Performance review and miss owners |
| DH-01.04.4.1.1 "Cohort rule", .2 "Feature definition", .3 "Data handoff" | `data-preparation-and-analytics-methods` | A1 Cohort, features and data handoff |
| DH-01.04.4.2.1 "Data quality rule" | `data-quality-monitoring` | A1 Data quality rules |
| DH-01.04.4.2.2 "Data quality score" | `data-quality-monitoring` | A2 Data quality read |
| DH-01.04.4.2.3 "Feature repair" | `data-quality-monitoring` | B1 Data quality review and feature repair |
| "DH-01.04 Data Science & AI/ML Download a digital health expert", "Download one digital health expert", "Find digital health experts" | `digital-health-expert` (shared skill) | none |

### DH-01.06 Digital Therapeutic Design, Personalization Engine and DTx Architecture (old pack dh-digital-therapeutic-design)

| Old skill or task | Go to | Task there |
|---|---|---|
| "DH-01.06 Digital Therapeutic Design" (core menu); heading menus "DH-01.06.1 Personalization Engine", "DH-01.06.4 DTx Architecture" | this map | none |
| DH-01.06.1.1.1 "Adaptive Logic Design", .2 "Personalisation Model Development", .3 "Tailoring Rule Validation" | `clinical-ml-model-development-and-validation` | A2 Personalization rule specification |
| DH-01.06.1.2.1 "Personalisation Adaptation Monitoring" | `model-performance-and-drift-monitoring` | A2 Drift, calibration and adaptation read |
| DH-01.06.1.2.2 "personalisation pass rule", .3 "personalisation miss owner" | `model-performance-and-drift-monitoring` | B1 Performance review and miss owners (steps 1 and 4) |
| DH-01.06.4.1.1 "SaMD Architecture Design", .2 "Platform Component Development", .3 "Data-Flow & Integration Design" | `medical-software-lifecycle-and-delivery` | A1 Lifecycle plan and architecture |
| DH-01.06.4.2.1 "Platform Performance Monitoring" | `software-quality-and-delivery-monitoring` | A2 Delivery and platform read |
| DH-01.06.4.2.2 "DTx architecture pass rule", .3 "DTx architecture miss owner" | `software-quality-and-delivery-monitoring` | B1 Release gate and miss owners |
| DH-01.06.2 Safety & Efficacy and DH-01.06.3 Engagement Mechanics | `dh-clinical-development` therapeutic-mechanism-and-intervention-design and mechanism-validation-monitoring | outside this pack (folded there earlier) |
| "DH-01.06 Digital Therapeutic Design Find digital health experts", "Download a digital health expert", "Download one digital health expert" | `digital-health-expert` (shared skill) | none |

### DH-05.01 Advanced Analytics & Data Science (old pack dh-advanced-analytics)

| Old skill or task | Go to | Task there |
|---|---|---|
| "DH-05.01 Advanced Analytics & Data Science" (core menu); heading menus "DH-05.01.1 Statistical Modeling & Inference", "DH-05.01.2 Machine Learning Applications", "DH-05.01.3 Advanced Analytics Consulting" | this map | none |
| DH-05.01.1.1 "Causal question", "Design choice", "Estimate record"; DH-05.01.1.2 "Model target", "Fit and check", "Model limit"; DH-05.01.1.3 "Uncertainty question", "Posterior or interval", "Sensitivity of the prior" | `data-preparation-and-analytics-methods` | A2 Statistical and causal analysis plan |
| DH-05.01.2.1 "Prediction target", "Train and holdout", "Score limit"; DH-05.01.2.2 "Recommendation unit", "Policy", "Recommendation log"; DH-05.01.2.3 "Forecast target", "Forecast and interval", "Optimization constraint" | `data-preparation-and-analytics-methods` | B1 Prediction, personalization and forecasting choices |
| DH-05.01.3.1 "Decision frame", "Question list", "Frame review"; DH-05.01.3.2 "Solution shape", "Method match", "Analysis boundary" | `analytics-products-and-decision-support` | A1 Decision frame and use-case portfolio |
| DH-05.01.3.3 "Recommendation statement", "Delivery to the owner", "Unresolved question" | `analytics-products-and-decision-support` | B1 Decision support design and delivery |
| "DH-05.01 Advanced Analytics & Data Science Download a digital health expert", "Download one digital health expert", "Find digital health experts" | `digital-health-expert` (shared skill) | none |

### DH-05.02 Decision Support & Business Intelligence (old pack dh-decision-support)

| Old skill or task | Go to | Task there |
|---|---|---|
| "DH-05.02 Decision Support & Business Intelligence" (core menu); heading menus "DH-05.02.1 Self-Service BI Enablement", "DH-05.02.2 Executive Dashboards & Reporting", "DH-05.02.3 Decision Intelligence Products" | this map | none |
| DH-05.02.1.1 "Metric on the semantic layer", "Entity the metric hangs on", "Layer change"; DH-05.02.1.2 "Template purpose", "Template contents", "Template retirement" | `analytics-products-and-decision-support` | A2 Metric definition and certification |
| DH-05.02.1.3 "Enablement task", "Practice record" | `analytics-adoption-and-impact-monitoring` | A1 Adoption and literacy read |
| DH-05.02.1.3 "Support after the session" | `analytics-adoption-and-impact-monitoring` | B1 Impact review and miss owners |
| DH-05.02.2.1 "Executive question", "Dashboard layout", "Executive review"; DH-05.02.2.3 "Commentary claim", "Driver", "Commentary text" | `analytics-products-and-decision-support` | B1 Decision support design and delivery |
| DH-05.02.2.2 "Cadence", "Issue record", "Cadence break" | `analytics-adoption-and-impact-monitoring` | A2 Cadence, outcome and governance read (the follow-up of "Cadence break" in B1) |
| DH-05.02.3.1 "Decision product user", "Product bet", "Discovery evidence" | `analytics-products-and-decision-support` | A1 Decision frame and use-case portfolio |
| DH-05.02.3.2 "Workflow insertion point", "Action from the number", "Embed owner" | `analytics-products-and-decision-support` | B1 Decision support design and delivery |
| DH-05.02.3.3 "Outcome of the decision", "Outcome measurement" | `analytics-adoption-and-impact-monitoring` | A2 Cadence, outcome and governance read |
| DH-05.02.3.3 "Bet review" | `analytics-adoption-and-impact-monitoring` | B1 Impact review and miss owners |
| "DH-05.02 Decision Support & Business Intelligence Download a digital health expert", "Download one digital health expert", "Find digital health experts" | `digital-health-expert` (shared skill) | none |

### DH-05.03 Analytics Product Management & Enablement (old pack dh-analytics-product)

| Old skill or task | Go to | Task there |
|---|---|---|
| "DH-05.03 Analytics Product Management & Enablement" (core menu); heading menus "DH-05.03.1 Analytics Product Strategy", "DH-05.03.2 Data Literacy & Adoption", "DH-05.03.3 Analytics Governance & Enablement" | this map | none |
| DH-05.03.1.1 "Analytics portfolio list", "Roadmap slice", "Portfolio change"; DH-05.03.1.2 "Use case value", "Priority rule", "Priority decision" | `analytics-products-and-decision-support` | A1 Decision frame and use-case portfolio |
| DH-05.03.1.3 "Performance question", "Performance read" | `analytics-adoption-and-impact-monitoring` | A2 Cadence, outcome and governance read |
| DH-05.03.1.3 "Review outcome" | `analytics-adoption-and-impact-monitoring` | B1 Impact review and miss owners |
| DH-05.03.2.1 "Literacy objective", "Curriculum unit", "Curriculum owner"; DH-05.03.2.2 "Campaign audience", "Campaign activity", "Campaign result"; DH-05.03.2.3 "Champion role", "Champion roster", "Champion load" | `analytics-adoption-and-impact-monitoring` | A1 Adoption and literacy read (follow-up of "Campaign result" and "Champion load" in B1) |
| DH-05.03.3.1 "Metric certification rule", "Certification record"; DH-05.03.3.2 "Platform access rule", "Publish record"; DH-05.03.3.3 "CoE charter", "CoE decision log", "CoE dispute" | `analytics-products-and-decision-support` | A2 Metric definition and certification |
| DH-05.03.3.1 "Decertify"; DH-05.03.3.2 "Access review" | `analytics-adoption-and-impact-monitoring` | A2 Cadence, outcome and governance read |
| "DH-05.03 Analytics Product Management & Enablement Download a digital health expert", "Download one digital health expert", "Find digital health experts" | `digital-health-expert` (shared skill) | none |

### DH-04.01 Clinical Integration & Interoperability (old pack dh-interoperability)

| Old skill or task | Go to | Task there |
|---|---|---|
| "DH-04.01 Clinical Integration & Interoperability" (core menu); heading menus "DH-04.01.1 Interoperability Architecture", "DH-04.01.2 EHR Integration Delivery", "DH-04.01.3 Data Exchange & Terminology", "DH-04.01.4 Clinical Workflow Enablement" | this map | none |
| DH-04.01.1.1.1 "Implementation guide selection", .2 "Exchange pattern design" | `interoperability-and-ehr-integration` | A1 Standards and exchange architecture |
| DH-04.01.2.1.1 "SMART app registration", .2 "Screen to FHIR interaction map", .3 "Sandbox launch proof"; DH-04.01.3.1.1 "Code system selection", .2 "Equivalence mapping"; DH-04.01.4.1.1 "Current step observation", .2 "New exchange placement" | `interoperability-and-ehr-integration` | A2 EHR launch and terminology mapping |
| DH-04.01.1.1.3 "Conformance gap record"; DH-04.01.3.1.3 "Unmatched code hold"; DH-04.01.4.1.3 "Adoption measure" | `interoperability-and-ehr-integration` | B1 Conformance gaps and go-live scope |
| DH-04.01.1.2.1 "Conformance check definition", .2 "Sample exchange scoring"; DH-04.01.2.2.1 "Launch matrix definition", .2 "Launch matrix run" | `integration-quality-monitoring` | A1 Conformance and launch checks |
| DH-04.01.3.2.1 "Map sample definition", .2 "Blinded clinical review"; DH-04.01.4.2.1 "Designed versus observed step", .2 "Time and workaround count" | `integration-quality-monitoring` | A2 Mapping, workflow and standards read |
| DH-04.01.1.2.3 "Nonconformance assignment"; DH-04.01.2.2.3 "Failed cell report"; DH-04.01.3.2.3 "Map error classes"; DH-04.01.4.2.3 "Step change for the next release" | `integration-quality-monitoring` | B1 Integration review and miss owners |
| "DH-04.01 Clinical Integration & Interoperability Download a digital health expert", "Download one digital health expert", "Find digital health experts" | `digital-health-expert` (shared skill) | none |

### DH-04.02 Cybersecurity & Privacy (old pack dh-cybersecurity)

| Old skill or task | Go to | Task there |
|---|---|---|
| "DH-04.02 Cybersecurity & Privacy" (core menu); heading menus "DH-04.02.1 Compliance & Assurance", "DH-04.02.2 Security Architecture", "DH-04.02.3 Security Operations", "DH-04.02.4 Privacy & Consent" | this map | none |
| DH-04.02.1.1.1 "Data class and legal basis", .2 "Control per data class", .3 "Reviewer document set"; DH-04.02.4.1.1 "Consent purpose list", .2 "Consent capture check", .3 "Privacy engineering change" | `cybersecurity-and-privacy-by-design` | A1 Privacy and compliance map |
| DH-04.02.2.1.1 "Trust boundary drawing", .2 "Threat enumeration", .3 "Mitigation or accepted risk" | `cybersecurity-and-privacy-by-design` | A2 Threat model and security architecture (acceptance in B1) |
| DH-04.02.3.1.1 "Vulnerability intake", .2 "Response action", .3 "Incident record" | `cybersecurity-and-privacy-by-design` | B1 Vulnerability response and risk acceptance |
| DH-04.02.1.2.1 "Claimed control versus artifact", .2 "Gap scoring by citation"; DH-04.02.2.2.1 "Threat coverage check", .3 "Model update trigger"; DH-04.02.4.2.1 "Consent text versus practice", .2 "Withdrawal test" | `security-and-privacy-operations-monitoring` | A1 Control, threat model and consent assurance |
| DH-04.02.3.2.1 "Open vulnerability age", .2 "Resolution evidence", .3 "Repeat failure class"; DH-04.02.2.2.2 "Residual risk score" | `security-and-privacy-operations-monitoring` | A2 Vulnerability and incident read |
| DH-04.02.1.2.3 "Missing artifact owner"; DH-04.02.4.2.3 "Consent compliance owner" | `security-and-privacy-operations-monitoring` | B1 Security and privacy review and miss owners |
| "DH-04.02 Cybersecurity & Privacy Find digital health experts", "Download a digital health expert", "Download one digital health expert" | `digital-health-expert` (shared skill) | none |

### DH-04.03 Software Engineering Excellence (old pack dh-software-engineering)

| Old skill or task | Go to | Task there |
|---|---|---|
| "DH-04.03 Software Engineering Excellence" (core menu); heading menus "DH-04.03.1 Cloud & Infrastructure", "DH-04.03.2 Quality Engineering", "DH-04.03.3 DevOps & Deployment", "DH-04.03.4 Medical Software Development" | this map | none |
| DH-04.03.4.1.1 "Safety class and software items", .2 "Required process for the class"; DH-04.03.1.1.1 "Workload and data placement", .2 "Scale limit", .3 "Operate the environment" | `medical-software-lifecycle-and-delivery` | A1 Lifecycle plan and architecture |
| DH-04.03.2.1.1 "Intended use and hazard", .2 "Verification case", .3 "Validation with a user"; DH-04.03.3.1.1 "Pipeline stages for device software", .2 "Evidence the pipeline keeps", .3 "Separation of environments" | `medical-software-lifecycle-and-delivery` | A2 Verification, validation and release pipeline |
| DH-04.03.4.1.3 "Problem resolution record" | `medical-software-lifecycle-and-delivery` | B1 Release and change decision |
| DH-04.03.2.2.1 "Trace from hazard to case", .2 "Build under test"; DH-04.03.4.2.1 "Class versus hazard check", .2 "Plan completeness" | `software-quality-and-delivery-monitoring` | A1 V&V completeness and compliance read |
| DH-04.03.1.2.1 "Capacity evidence", .2 "First-failure review", .3 "Region and residency check"; DH-04.03.3.2.1 "Deploy frequency and failure", .2 "Skipped stage check" | `software-quality-and-delivery-monitoring` | A2 Delivery and platform read |
| DH-04.03.4.2.3 "Release gate for the class"; DH-04.03.2.2.3 "Open validation miss"; DH-04.03.3.2.3 "Pipeline change owner" | `software-quality-and-delivery-monitoring` | B1 Release gate and miss owners |
| "DH-04.03 Software Engineering Excellence Download a digital health expert", "Download one digital health expert", "Find digital health experts" | `digital-health-expert` (shared skill) | none |

## Catalogue jobs

The old files of these eight packs bind no library tool or job ("Tool: not bound"). A saved `list_jobs` of 19 October 2026 shows no technology job (no model validation, data quality, analytics, software, interoperability or security job); each competency skill names any job in its own formula table and marks the check "needs a live check". This map never starts a job.

## Out of scope for this pack

Say so in one line and route where a home exists, naming the pack and the skill, never the pack alone. Do not do the work from this map.

- Device status, classification, pathway, PCCP and submissions: `dh-regulatory-and-quality` regulatory-pathway-and-classification, ai-ml-device-pathway-and-change-control, regulatory-submission-and-dossier.
- Design controls and the risk file: `dh-regulatory-and-quality` design-controls-and-risk-management. Complaints, events and reportability: `dh-regulatory-and-quality` audit-capa-and-complaints.
- Clinical validation studies, protocols and endpoints: `dh-clinical-development` study-protocol-and-endpoint-design.
- Therapeutic mechanism, engagement mechanics, safety and efficacy of a DTx (old DH-01.06.2 and DH-01.06.3): `dh-clinical-development` therapeutic-mechanism-and-intervention-design and mechanism-validation-monitoring.
- Usability and human factors: `dh-patient-and-user-experience` usability-monitoring; clinical workflow UX design: `dh-patient-and-user-experience` clinical-workflow-ux-design.
- Strategy, build or buy, and product portfolio choices: `dh-strategy-and-portfolio` strategic-vision-and-options.
- A threshold no source sets (drift, fairness, data quality, adoption), a release decision, a security risk acceptance or an IEC 62304 class assigned by the model: given by no skill; the skills lay out sourced requirements and compute on the person's own rules.
- Exploit code, attack steps or detail beyond public vulnerability identifiers: written by no skill.

## Routing examples

- "Is the external test set for our sepsis model really external, and what do we still need before we run it?" Route to `clinical-ml-model-development-and-validation` A1.
- "Our triage model's calibration looks off since the new lab analyzer went in." Route to `model-performance-and-drift-monitoring` A2; the input data checks themselves to `data-quality-monitoring`.
- "Which subgroups could our readmission model disadvantage, and who signs off a difference?" Route to `responsible-ai-governance` (A1, then B1).
- "Run the old 'Feature repair' task on our claims dataset." Route to `data-quality-monitoring` B1.
- "Define and certify our 30-day readmission metric for the executive dashboard." Route to `analytics-products-and-decision-support` A2.
- "What IEC 62304 class is our app, and what does our pipeline need to keep?" Route to `medical-software-lifecycle-and-delivery` (A1, A2); the class is the team's, recorded as they set it.
- "Which US Core version do we need for certification, and is our SMART launch working at all three hospitals?" Route to `interoperability-and-ehr-integration` A1, then `integration-quality-monitoring` A1.
- "Threat model our remote monitoring platform and tell us what the 524B SBOM needs." Route to `cybersecurity-and-privacy-by-design` A2.
- "Give us the drift threshold FDA requires." No source sets one and the FDA AI-enabled device software functions guidance is a draft. Route to `model-performance-and-drift-monitoring`, which computes against the team's own thresholds. Say this in one line.

## Related packs

- **Regulatory and quality** (`dh-regulatory-and-quality`): `ai-ml-device-pathway-and-change-control`, `ai-ml-readiness-monitoring`, `design-controls-and-risk-management`. Start with `regulatory-and-quality-capability-map`.
- **Clinical development** (`dh-clinical-development`): `study-protocol-and-endpoint-design`, `therapeutic-mechanism-and-intervention-design`, `mechanism-validation-monitoring`. Start with `clinical-development-capability-map`.
- **Patient and user experience** (`dh-patient-and-user-experience`): `usability-monitoring`, `clinical-workflow-ux-design`. Start with `patient-and-user-experience-capability-map`.
- **Strategy and portfolio** (`dh-strategy-and-portfolio`): `strategic-vision-and-options`. Start with `strategy-and-portfolio-capability-map`.

## Downloading a technology expert

If the person wants an expert role on their own assistant, route to the shared skill `digital-health-expert`. It replaces the expert shims of the eight old packs (DH-01.04, DH-01.06, DH-05.01, DH-05.02, DH-05.03, DH-04.01, DH-04.02, DH-04.03).

## Rules that hold here

- Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line. A routing answer is at most 150 words: the skill name, one line on why, and the next question the skill will ask. Cut optional extra routes before cutting the next question. Count the words before handing over (a routing answer has no tables or calls list; every word counts).
- Answer first: name the skill in the first sentence.
- Every route names the pack and the skill, never the pack alone.
- People decide. This map never proposes a threshold, an acceptance criterion, a class, a release decision, a risk acceptance, a scope, a target or an owner, even as an example.
- Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title.
- American English, dates in full, no urgency framing.

## Files in this skill

- `evals/evals.json` six routing tests: one clinical AI request, one old task name, one request across two halves of the pack, one engineering request, one out-of-pack request, and one request this map must decline to answer itself.
- `evals/prompts_only.json` the same prompts without expected output, for blind baseline tests.
