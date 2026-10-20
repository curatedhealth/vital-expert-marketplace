# Lifecycle rules: what the sources say, row by row

Source: `engineering-interop-security-research.md` (EN rows, read 20 October 2026), `quality-systems-research.md` (QS, EU, ST and CH rows, read 19 October 2026), `product-lifecycle-research.md` (PL rows, read 20 October 2026) and `ai-ml-regulation-research.md` (cited as AI US-nn, read 19 October 2026). Interpretive reference for A1 and A2. Every line carries its row. In answers, cite each fact by source name and date in plain words with the row id after it (`gap-rules.md`, "How to cite"). Rows marked [WF] were read through a summarizing fetch: say so when a fact rests on one. A fact not in a row is `[GAP]`.

## 1. What must be validated, and how effort scales

| Rule | As the source states it | Row |
|---|---|---|
| Scope of validation | Software in a device, software that is a device, and software used in production or the quality system | EN-003 |
| Definition | Confirmation by examination and objective evidence that software specifications conform to user needs and intended uses | EN-004; compare PL22 |
| Effort follows risk | The validation, verification and testing effort varies with the safety risk (hazard) of the automated function | EN-005 |
| Requirements first | Validation cannot be completed without an established software requirements specification | EN-006 |
| Prevent, do not test in | Quality assurance focuses on preventing defects during development | EN-007 |
| Independence | Self-validation is difficult; independent evaluation is better, especially for higher risk; internal staff not involved in the design may serve | EN-010 |
| Software is a component | The QMSR definition of component includes software and firmware | QS6 |
| Design and development scope | ISO 13485 Clause 7.3 applies to class II and III devices and class I devices automated with software | QS9 |
| QMSR terms | "Design controls" and "design validation" are no longer QMSR terms; their elements sit in ISO 13485 Clause 7.3; pre-QMSR guidances carry this note | PL11, PL12 |
| EU software lifecycle | Software is developed to the state of the art, considering development lifecycle, risk management including information security, verification and validation (MDR Annex I 17.2) | EU19 |
| EU reliability | Repeatability, reliability and performance in line with intended use; single fault conditions handled (MDR Annex I 17.1) | EU20 |
| EU mobile platforms | Software for mobile platforms accounts for platform features (screen size, contrast) and external factors (MDR Annex I 17.3) | EN-031 |
| EU minimum IT requirements | The manufacturer sets minimum hardware, IT network and IT security requirements to run the software as intended (MDR Annex I 17.4) | EN-069 |

The GPSV is a final guidance of 11 January 2002 (EN-001). Its Section 6 is superseded by the CSA guidance; every other section remains FDA's current thinking (EN-002). The GPSV predates the QMSR (effective 2 February 2026); its 21 CFR 820 citations refer to the old regulation (EN research file, "Changes and conflicts").

## 2. IEC 62304, IEC 82304-1 and the safety class

| Fact | Row |
|---|---|
| IEC 62304 defines lifecycle requirements for medical device software (standalone or embedded) and does not cover validation and final release of the device, even an all-software device | ST6, PL105 |
| Current text: IEC 62304:2006+AMD1:2015, edition 1.1, published 26 June 2015, stability date 2028 | ST7 |
| Edition 2.0 is in preparation, forecast publication 26 October 2028 (read from the page's embedded data) | ST8 |
| FDA recognizes IEC 62304 edition 1.1 in full, number 13-79, entered 14 January 2019 | ST9 |
| EN 62304 is not harmonized under the MDR (measured on the Commission page, decisions to 11 June 2026): it gives no presumption of conformity there | EU30 |
| IEC 82304-1:2016 covers safety and security of health software products on general computing platforms, design to disposal including validation; FDA recognized, number 13-97; edition 1.0, 27 October 2016, stability date 2029 | ST10, ST11, PL103, PL104 |
| For a premarket submission at Basic level, FDA accepts a summary of the lifecycle development plan and of configuration management and maintenance, or a declaration of conformity to IEC 62304 (named subclauses) | PL18 |

**Not sourced.** The IEC 62304 software safety classes (A, B, C), what each class requires, and the process clause detail are paywalled; no regulator text restating them was read (EN research file, "Not sourced"). The skill never states a class definition, never maps a class to required activities from memory, and never assigns a class. The class, the hazard that drove it and the plans it requires are the person's, from their own copy of the standard and their risk file. Write the person's statement verbatim and mark the definitions "IEC 62304 class definitions: not in this skill's sources `[GAP]`; read your licensed copy".

## 3. Off-the-shelf and open-source components (SOUP inventory) and the SBOM

| Rule | As the source states it | Row |
|---|---|---|
| Guidance version | FDA "Off-The-Shelf Software Use in Medical Devices", issued 11 August 2023, superseding 27 September 2019 | EN-023 |
| OTS definition | A generally available component for which the manufacturer cannot claim complete lifecycle control (for example an operating system) | EN-024 |
| Documentation elements | Description, risk assessment, testing within V&V, and assurance of development methods and continued maintenance, scaled to Basic or Enhanced | EN-025 |
| Identity per component | Title, manufacturer, version, release date, patch number and upgrade designation, as appropriate | EN-026 |
| External links | Links to outside software (for example networks) completely defined for each device or module | EN-027 |
| SBOM in a cyber device submission | Commercial, open-source and off-the-shelf components (FD&C Act 524B(b)(3)) | EN-045 |
| SBOM format | Machine-readable, consistent with the NTIA October 2021 minimum elements; justify if not provided | EN-053 |
| SBOM extra fields | Per component: level of support (maintained, no longer maintained, abandoned) and end-of-support date | EN-054 |
| Known vulnerabilities | Identify all known vulnerabilities of the device and its components, including CISA KEV entries, and how they were found | EN-055 |
| EU products outside MDR | The CRA requires a machine-readable SBOM covering at least top-level dependencies; MDR and IVDR devices are excluded from the CRA | EN-092, EN-086 |

The NTIA minimum elements themselves were not read (`[GAP]`); `scripts/lifecycle_check.py items` checks the FDA fields above, not the NTIA list. Vulnerability analysis, the threat model and patch policy route to `cybersecurity-and-privacy-by-design` (this pack).

## 4. Architecture and platform components (old DH-01.06.4.1 tasks)

| Rule | As the source states it | Row |
|---|---|---|
| Premarket element | "System and Software Architecture Diagram" is one of the ten software documentation elements | PL15 |
| Separate the device function | The device function under review should be separated from "other functions" in design and implementation (logical, architectural, code and data partitioning); early architecture decisions make this possible | PL26 |
| Function and other function | A function is a distinct purpose; an other function is non-device, not subject to premarket review, or under enforcement discretion | PL24 |
| Impact assessment | All impact assessments of other functions (negative, positive, no impact) are documented as design validation and are inspectable | PL25, PL27 |
| Changing an other function | Assess impact on the reviewed function; if adverse or a labeled positive impact, the 510(k) or PMA change guidances decide whether a new submission is needed | PL29 |
| Security architecture views | At minimum Global System, Multi-Patient Harm, Updateability/Patchability and Security Use Case views (premarket cybersecurity guidance, 3 February 2026) | EN-056 |
| SDS by level | At Basic level the software design specification stays in the design file; at Enhanced level it is submitted with trace to the SRS | PL17 |

The skill drafts architecture only from components and data flows the person has named (old task rule: "Do not invent an integration"). A component or flow the person has not named is `[GAP]`. Interoperability design (FHIR, SMART, EHR integration) routes to `interoperability-and-ehr-integration` (this pack).

## 5. Cloud placement, scale and operations (old DH-04.03.1.1 tasks)

| Rule | As the source states it | Row |
|---|---|---|
| CSA covers cloud tools | The CSA framework applies to automation, analytics, AI/ML tools and cloud computing used in production or the QMS, including IaaS, PaaS and SaaS | EN-017 |
| Others' validation work | Manufacturers may use validation activities performed by developers, suppliers or cloud service providers | EN-016 |
| HIPAA cloud provider [WF] | A cloud provider storing ePHI is a business associate even without a decryption key, and must meet the applicable Security Rule standards | EN-032, EN-033 |
| Offshore storage [WF] | Storage outside the US is permitted with a BAA; OCR notes location can raise risk that the risk analysis must address | EN-034 |
| Contingency (HIPAA) | Data backup, disaster recovery and emergency mode operation plans are required; testing and criticality analysis are addressable | EN-102 |
| Activity review (HIPAA) | Regular review of audit logs, access reports and incident tracking reports | EN-101 |
| GDPR by design and default | Measures such as pseudonymization at design time; by default only data necessary for each purpose | EN-108, EN-109 |

**Not sourced.** No regulator text sets a scale target, a capacity margin, an uptime figure, a recovery time or a region rule for device software. EU international transfer rules (GDPR Chapter V) are not in this skill's sources. The scale unit, the number the design must hold, the component expected to fail first, the regions and the recovery objectives are the person's; write "not given" when missing. Old task rules kept: name the regions when writing "multi-region"; name the first-failure component when claiming elastic scale; name who is paged and on what condition, or mark the runbook `[GAP]`.

## 6. Secure development and agile practice

| Rule | As the source states it | Row |
|---|---|---|
| NIST SSDF | SP 800-218 version 1.1, February 2022: Prepare the Organization, Protect the Software (source, build pipeline, releases), Produce Well-Secured Software, Respond to Vulnerabilities | EN-036 to EN-040 |
| IEC 81001-5-1 | Secure health software lifecycle aligned to IEC 62443-4-1; FDA recognized in full, number 13-122 (abstract only) | EN-084 |
| Recognized standards are not the whole of 524B | Conformance to TIR57, IEC 81001-5-1 or TIR97 may not satisfy all 524B requirements | EN-083 |
| Agile | AAMI TIR45:2023 on agile practices for medical device software, recognized in full (13-143, 26 May 2025); declarations to the 2012 edition accepted until 2 July 2028 | EN-028 to EN-030 |

TIR45 and IEC 81001-5-1 content beyond the FDA abstracts was not read (`[GAP]`).

## 7. Premarket software documentation (for the regulatory owner)

The ten elements (PL15): documentation level evaluation; software description; risk management file (plan, assessment, report, PL16); SRS; system and software architecture diagram; SDS (PL17); development, configuration management and maintenance practices (PL18); software testing as part of V&V (PL19); software version history; unresolved software anomalies with the impact of each on safety and effectiveness (PL20). The criteria that decide Basic or Enhanced level were not read (`[GAP]`): the level is the regulatory owner's call, routed to `dh-regulatory-and-quality` regulatory-submission-and-dossier. `scripts/lifecycle_check.py docs` checks the person's document register against these elements at the level the person states.

## 8. UK and EU market-entry checklists that touch the lifecycle

NHS DTAC has five sections, including C3 technical security and C4 interoperability; the updated form applies from 24 February 2026 and the old form is not to be used from 6 April 2026 [WF] (PL97, PL99). The form supports DCB0129 compliance; suppliers accessing NHS systems or patient data also complete the Data Security and Protection Toolkit [WF] (PL100). DCB0129 content (clinical safety officer, hazard log, safety case) was not read (PL102): `[GAP]`.
