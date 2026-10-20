# Delivery and change rules: what the sources say, row by row

Source: as in `lifecycle-rules.md`. Interpretive reference for A2 and B1. Every line carries its row; cite by source name and date in plain words with the row id after it. A fact not in a row is `[GAP]`.

## 1. Verification and validation design (old DH-04.03.2.1 tasks)

| Rule | As the source states it | Row |
|---|---|---|
| Verification | Confirmation by objective evidence that a phase's output meets that phase's input; includes testing, code and document inspections, design reviews, technical evaluations and traceability analyses | PL21 |
| Validation | Establishing by objective evidence that software specifications conform to user needs and intended uses | PL22, EN-004 |
| Requirements baseline | No validation without an established SRS | EN-006 |
| Testing evidence by level | Basic: summary of unit, integration and system testing plus system-level protocol and report. Enhanced adds unit and integration protocols and reports | PL19 |
| Clinical evaluation inside design validation | ISO 13485 Clause 7.3.7 requires clinical or performance evaluation as part of design validation | PL7 |
| Final release | IEC 62304 does not cover validation and final release; for standalone health software IEC 82304-1 covers product validation | ST6, PL105, PL103 |
| Security testing set | Fuzzing, attack surface analysis, vulnerability chaining, known-vulnerability scanning, binary composition analysis, static and dynamic analysis, penetration testing; the report states tester independence, scope, duration and methods | EN-058, EN-059 |

Old task rules kept as steps: state the intended use in one sentence including who acts on the output; separate a wellness display from a function that drives a clinical action (FDA's wellness and device software policies, PL45 to PL49, decide which it is: route to `dh-regulatory-and-quality` regulatory-pathway-and-classification); every case points to a specification line, states input, step and expected output, and is recorded against a named build; never write an expected output of "works correctly"; validation with a user names the role and task from the intended use, uses a named build and does not rely on the screen's author as the only participant; a validation miss is filed apart from a specification miss.

Human factors validation, summative usability testing and use-error analysis route to `dh-patient-and-user-experience` usability-monitoring and clinical-workflow-ux-design. Security test design routes to `cybersecurity-and-privacy-by-design` (this pack); this skill lists where the security tests sit in the pipeline, never how to attack the product.

## 2. The release pipeline (old DH-04.03.3.1 tasks)

**No CI/CD-specific regulator text was found** (EN research file, "Not sourced"): no FDA or EU source addresses pipelines, infrastructure as code or continuous deployment of device software directly. The pipeline is therefore built from the general rules below, each cited, and the stage list, gates and tools are the person's.

| Rule that applies to a pipeline | As the source states it | Row |
|---|---|---|
| Any change re-opens validation | When any change (even a small change) is made, the validation status needs to be re-established, with system-wide impact analysis | EN-008 |
| Regression testing | After change analysis, regression testing shows that unchanged but vulnerable portions were not adversely affected | EN-009 |
| Pipeline and QMS tools are validated | Software that automates any part of production or the quality system must be validated for its intended use | EN-011 |
| CSA for those tools | Risk-based approach (CSA guidance, reissued 3 February 2026, supersedes the 24 September 2025 final, replaces only GPSV Section 6) | EN-012 to EN-014 |
| CSA scope | Production and QMS software; its intended use is not the device's intended use (device software is out of its scope) | EN-015 |
| CSA methods | Risk-based and unscripted testing, continuous performance and data monitoring, validation by developers, suppliers or cloud providers | EN-016 |
| High process risk | Failure may cause a quality problem that foreseeably compromises safety | EN-018 |
| CSA record | Intended use, risk analysis result, assurance activities with issues found, conclusion of acceptability, who tested and when, approval where appropriate | EN-020 |
| Proportionate records | No more evidence than needed for the risk identified | EN-021 |
| Digital records | System logs, audit trails and software-generated data are recommended as assurance evidence | EN-022 |
| Protect the build | SSDF PS: protect all software components from tampering and unauthorized access | EN-038 |
| Version history | The submission includes a history of tested versions with dates and change descriptions | PL20 |
| Change control area | FDA's inspection Change Control area confirms changes are evaluated for risk and impact before implementation; elements include software changes (ISO 13485 4.1.6, 7.5.6, 7.6) | QS34 |
| Inspection element | Design and development software validation is a minimum element in inspection model 2 (CP 7382.850, 2 February 2026) | QS33 |
| AI model updates under a PCCP | A change specified in the authorized PCCP and done per its Modification Protocol needs no new submission but is documented in the quality system; the plan includes detect-and-revert mechanisms | AI US-12, AI US-31 |
| HIPAA documentation | Security Rule documentation retained six years from creation or last effective date | EN-105 |

**Version trap.** FDA's recognition entry for AAMI TIR45 still lists CSA as a "Draft ... September 2022"; the GPSV cover note names the September 2025 title. The current CSA is the 3 February 2026 reissue, titled for "Quality Management System Software" (EN-012; EN research file, "Changes and conflicts"). Never treat CSA as a draft.

Old task rules kept as steps: describe only stages the repository actually runs; say which stage may deploy to production; mark a stage skipped for hotfixes; never claim an SBOM or a signed build the pipeline does not produce; state which stages can reach production, how test data is made, and every job that copies production data with its control; never use production patient data as the default fixture (by default only the data necessary for each purpose are processed: GDPR Article 25(2), EN-109).

## 3. Deciding what a change re-opens (B1)

| Question | As the source states it | Row |
|---|---|---|
| FDA: any software modification is a design change | "Deciding When to Submit a 510(k) for a Software Change to an Existing Device", 25 October 2017; it predates the QMSR and FDA says to check against the current QMSR | CH9, CH10 |
| Start with risk | A risk-based assessment of whether the change could significantly affect safety or effectiveness comes first | CH11 |
| Cybersecurity-only change | In many cases not likely to require a new 510(k) | CH12 |
| Restore to specification | Restoring the most recently cleared specification likely needs no new 510(k), but impact is still evaluated | CH13 |
| New or modified risk | A new 510(k) is likely if the change creates or modifies a hazard, the harm is serious or worse pre-mitigation, and it is not already effectively mitigated | CH14 |
| Risk controls | New or changed controls needed to prevent significant harm likely trigger a new 510(k) | CH15 |
| Clinical performance | Could the change significantly affect clinical functionality or performance specifications tied to intended use? | CH16 |
| 524B and modifications | New authentication or encryption algorithms, new connectivity or a changed update mechanism may bring 524B documentation | EN-060 |
| EU legacy devices | MDCG 2020-3 Rev.1 (May 2023): software changes assessed with chart C; bug fixes, latency improvements and security updates are examples of non-significant changes only if the benefit-risk ratio is not negatively affected; new architecture, algorithm changes that may alter diagnosis or therapy and new interoperability channels are significant examples | CH3 to CH8 |
| Other functions | A change to an other function is assessed for impact on the device function; the result is documented in the quality system | PL29 |
| Risk files kept current | Risk documentation reviewed and updated when unforeseen risks or new information emerge | QS22 |

The skill lays these questions beside the person's change description and risk file, and writes what each answer depends on. Whether a new submission is needed, and the answer to each question, are the regulatory owner's: route to `dh-regulatory-and-quality` document-and-change-control (change records) and ai-ml-device-pathway-and-change-control (AI changes and PCCPs). The EU significant-change test applies to legacy devices under MDR Article 120 (CH1 to CH4); for MDR-certified devices the notified body's change rules apply and were not read here (`[GAP]`).

## 4. Problem resolution and open anomalies (old DH-04.03.4.1.3)

| Rule | As the source states it | Row |
|---|---|---|
| Open anomalies in the submission | A list of unresolved anomalies with an evaluation of each one's impact on safety and effectiveness | PL20 |
| Patch cadence for cyber devices | Known unacceptable vulnerabilities on a justified regular cycle; critical ones that could cause uncontrolled risks out of cycle as soon as possible (524B(b)(2)) | EN-044 |
| Uncontrolled risk clocks | 30 days to communicate and 60 days to fix under FDA's 806 enforcement policy: an enforcement policy, not a statutory deadline | EN-066, EN-067 |

Old task rules kept: each problem record carries an id, a software item, the version found, the effect on the hazardous function, and the change that fixed it or "open"; a problem that affects a function the person's own risk file ties to serious harm is not closed without a change or an accepted rationale signed by the person they name. Corrections and removals, complaints and CAPA route to `dh-regulatory-and-quality` audit-capa-and-complaints.

## 5. Release

IEC 62304 stops before final release (ST6). No source sets a release criterion, an acceptable number of open anomalies, a regression coverage figure or a test pass rate. Go or no-go is the person's. The skill assembles the facts the person needs (open problems, cases run on a build other than the candidate, pipeline evidence present or missing, change questions open) and labels the record "release decision draft for the owner".
