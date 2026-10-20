# A2 Verification, validation and release pipeline

Framework task: DH-04.03.2.1 with DH-04.03.3.1, Part A, task A2. Carries the old tasks "DH-04.03.2.1.1 Intended use and hazard", "DH-04.03.2.1.2 Verification case", "DH-04.03.2.1.3 Validation with a user", "DH-04.03.3.1.1 Pipeline stages for device software", "DH-04.03.3.1.2 Evidence the pipeline keeps" and "DH-04.03.3.1.3 Separation of environments" as steps.

## What this task delivers

A verification and validation plan tied to the intended use and the hazards the person lists, with a case structure that points every case at a specification line and a named build, and a release pipeline description: the stages the repository runs, which stage deploys to production, the hotfix path, the evidence each release leaves behind, the validation of the pipeline tools themselves, and how production data is kept out of earlier stages. It answers "how do we prove each release does what it should, and what record does the pipeline leave?"

Why it matters: any change, even a small one, re-opens validation (EN-008), and the tools that automate production or the quality system must themselves be validated for their intended use (EN-011). No regulator text addresses CI/CD directly (EN research file, "Not sourced"), so a pipeline is defensible only when each stage maps to a sourced rule and leaves a record.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `clinical-algorithm-validator` (old DH-04.03.2.1.x); `digital-health-product-manager` (old DH-04.03.3.1.x). Work as a quality engineer who maps the person's stages and cases to sourced rules |
| Skill | DH-04.03.2.1 Part A, Verification, validation and release pipeline |
| Workflow | The steps below |
| Knowledge | `references/delivery-and-change-rules.md` sections 1 and 2; `references/lifecycle-rules.md` sections 1, 3 and 6; the research files |
| Tools | None required. `verify.build_record` on sign-off |
| Prompt | This guide |
| Template | `assets/verification-validation-and-pipeline-output.md` |
| Input | The request and its context: intended use in one sentence, who acts on the output, the hazards from the person's risk file, specification ids, the stages the repository runs, the deploy rights, the hotfix path, the artifacts kept and where, how test data is made, any job that copies production data, the tools in the pipeline and their validation records |
| Governance | `references/governance.md`; acceptance criteria, coverage and release rules are the person's |
| Catalogue job | none known (needs a live check) |

## Read the request

- **Intended use and hazards.** Needed for step 1. If the person gives none, ask once; draft with "intended use: not given" and "hazards: not given".
- **Pipeline facts.** Ask for the stages as the repository runs them today. Old rule: never describe a pipeline the repository does not run. If the person wants a proposed pipeline, label every stage "proposed".
- **AI models.** If a model is retrained or updated through the pipeline, add the PCCP rows (AI US-12, AI US-31) and route the plan itself to `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control; model validation routes to `clinical-ml-model-development-and-validation` (this pack).
- **Short or full.** "What should our CI/CD keep for a SaMD?" is short mode. "Write our V&V plan and pipeline design" is full mode.

## Workflow

### Step 1. Intended use and hazard (old 2.1.1)

Write the intended use in one sentence, including who acts on the output. List the harm if the output is wrong or late, from the person's risk file. Separate a wellness display from a function that drives a clinical action; whether a function is a device function is decided with `dh-regulatory-and-quality` regulatory-pathway-and-classification (PL45 to PL49 are context). Old rule: do not verify a feature that has no intended use.

### Step 2. Verification cases (old 2.1.2)

Case structure: case id, specification line, hazard ids, input, step, expected output, build id, result, date. Verification is phase output against phase input (PL21); validation is specifications against user needs and intended uses (PL22, EN-004). Old rule: no expected output of "works correctly". Testing evidence expected in a US submission scales with the level the person states (PL19). Acceptance criteria and coverage are the person's ("acceptance criterion: set by the person `[GAP]`").

### Step 3. Validation with a user (old 2.1.3)

Name the role and task from the intended use; observe the person on a named build; record where they misread the output; file a validation miss apart from a specification miss. Old rule: the screen's author is never the only participant. Clinical or performance evaluation sits inside design validation (PL7); human factors validation routes to `dh-patient-and-user-experience` usability-monitoring.

### Step 4. Pipeline stages (old 3.1.1)

Write the stages as the repository runs them (build, automated test, review, release, or the person's names), which stage may deploy to production, and which stage the hotfix path skips. Map each stage to the rule it serves: regression after change analysis (EN-009), independent review where risk is higher (EN-010), protection of source, build and releases from tampering (SSDF PS, EN-038), security tests named in the premarket cybersecurity guidance (EN-058, test design routed to `cybersecurity-and-privacy-by-design`, this pack). A stage with no rule mapped is shown as the person's choice, not a gap.

### Step 5. Evidence the pipeline keeps (old 3.1.2)

List the artifacts kept per release (test report, review record, build id, SBOM if produced, signature if produced), where they are stored and for how long. The CSA record elements (EN-020) and digital records such as system logs and audit trails (EN-022) are the sourced reference; the tested-version history belongs in a US submission (PL20); HIPAA Security Rule documentation is kept six years (EN-105). Old rule: never claim an SBOM or a signed build the pipeline does not produce; a missing artifact is `[GAP]`.

### Step 6. Pipeline tool validation

The tools that automate production or the quality system (build server, test runner, deployment tool, issue tracker used as the problem log) are validated for their intended use (EN-011) under the CSA guidance reissued 3 February 2026 (EN-012), which allows risk-based and unscripted testing, continuous monitoring and work done by vendors or cloud providers (EN-016, EN-017), with proportionate records (EN-021). CSA covers production and QMS software, not the device software itself (EN-015). Say that FDA's TIR45 recognition entry still lists CSA as a 2022 draft; the current version is the 3 February 2026 reissue.

### Step 7. Separation of environments (old 3.1.3)

State which stages can reach production, how test data is produced for earlier stages, and every job that copies production data with the control on that copy. Old rule: production patient data is never the default fixture; by default only data necessary for each purpose are processed (GDPR Article 25(2), EN-109). Privacy design routes to `cybersecurity-and-privacy-by-design` (this pack).

## Build the output

Follow `assets/verification-validation-and-pipeline-output.md`. Answer first: the intended use as written, the number of hazards with and without a planned case, the stages and which one deploys, the evidence kept and missing. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/lifecycle_check.py words ANSWER.md`; without code execution, count the same way by hand. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- No acceptance criterion, coverage figure, pass rate or release rule with a value the model chose.
- No stage, artifact, SBOM or signature described that the person did not say exists; proposals labeled "proposed".
- CSA stated as the 3 February 2026 final; GPSV Section 6 only superseded.
- No attack steps or exploit detail; security tests named at the level of EN-058.
- `python3 scripts/lifecycle_check.py words ANSWER.md` prints "within the short-mode cap".
- The record line is the very last line: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Human factors validation: `dh-patient-and-user-experience` usability-monitoring.
- Clinical validation studies: `dh-clinical-development` study-protocol-and-endpoint-design.
- Security test design, penetration testing, SBOM vulnerability handling: `cybersecurity-and-privacy-by-design` (this pack).
- Reading how releases and V&V performed: `software-quality-and-delivery-monitoring` (this pack).
