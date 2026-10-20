# A1 Conformance and launch checks

Framework tasks: DH-04.01.1.2 and DH-04.01.2.2, Part A, task A1. Carries the old tasks "DH-04.01.1.2.1 Conformance check definition", "DH-04.01.1.2.2 Sample exchange scoring", "DH-04.01.2.2.1 Launch matrix definition" and "DH-04.01.2.2.2 Launch matrix run".

## What this task delivers

The person's check sheet written back with a pass rule per element; a score by profile across a stated sample of exchanges, with the failing payload ids; the launch matrix (role, patient state, encounter state) with the person's two pass rules and latency ceilings; and the matrix run, one outcome per cell. It answers "against our checks, which profiles and which launches fail, in which samples and cells?"

Why it matters: the old tasks were explicit that a profile failing every sample must not be averaged away, that one happy-path launch is not readiness, and that a mocked token is not an EHR launch.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `fhir-integration-specialist` (old DH-04.01.1.2.1, .2; DH-04.01.2.2.1, .2). Work as an integration quality analyst who reads the person's data against the person's checks |
| Skill | DH-04.01.1.2 with DH-04.01.2.2, Part A, Conformance and launch checks |
| Workflow | The steps below |
| Knowledge | `references/monitoring-rules.md` sections 1 and 2 |
| Tools | `scripts/integration_check.py score` and `launch` on the person's files; `verify.build_record` when the output leaves |
| Prompt | This guide |
| Template | `assets/conformance-and-launch-checks-output.md` |
| Input | The request and its context: the check sheet and guide version, the sample exchanges and how they were drawn, the launch matrix with results, the person's pass rules and ceilings, the sandbox, the read date |
| Governance | `references/governance.md`; checks, rules and ceilings are the person's |
| Catalogue job | none |

## Read the request

- **Read date.** The date the sample and the matrix were run, from the person; "not given" otherwise. Never use today's date.
- **Which part.** Conformance scoring, launch matrix, or both. "Which profiles fail?" is short mode on scoring.
- **Sandbox or production.** Synthetic or de-identified data only. If the person pastes what looks like real patient data, stop and ask for sandbox data.

## Workflow

### Step 1. Check definition (old "Conformance check definition")

Write back the person's sheet: per profile, the elements, cardinality, bound systems and the pass rule for each check, plus who runs the checks and on which environment ("not given" otherwise). State the guide version and whether it is the version ONC certification requires or a current HL7 publication (`monitoring-rules.md` section 1). If the sheet's version differs from the version selected for the integration, stop scoring and say so. No sheet: "check sheet not given `[GAP]`".

### Step 2. Sample scoring (old "Sample exchange scoring")

State the sample (count per profile, how drawn, dates) as the person gives it. Run `python3 scripts/integration_check.py score --sheet SHEET.json PAYLOADS...`. Quote the table by profile: samples, samples with a miss, the failing payload and resource ids with the element, and the flags S1 (failed in every sample), S2 (one sample only) and S3 (no sheet entry, not checked). Never average a profile into an overall score.

### Step 3. Launch matrix definition (old "Launch matrix definition")

The roles, patient states and encounter states the product claims to support (from the person); the launch pass (the token carries the context the screen needs, EN-140) and the write-back pass (the chart shows the written resource); the token and first-read latency ceilings. Each is the person's; any missing one is "not given". A matrix with one cell is flagged L7.

### Step 4. Launch matrix run (old "Launch matrix run")

Run `python3 scripts/integration_check.py launch MATRIX.csv --token-ms N --read-ms N` with the person's ceilings (omit a ceiling the person did not give; latency is then reported, not judged). Quote one row per cell with flags L1 (HTTP status not 2xx), L2 (context missing), L3 (write-back not visible), L4 (over the person's ceiling), L5 (mocked token), L6 (not run). A cell stopped on an EHR error is recorded as run, not retried until it passes.

### Step 5. What the certified EHR owes (only when a cell fails on an EHR duty)

Where a failure touches a certified API duty (group requests, refresh token life, patient-directed revocation, public documentation: EN-142 to EN-145), state the duty with its source and the observed fact side by side, for the owner the person names. Never call it non-compliance.

## Build the output

Follow `assets/conformance-and-launch-checks-output.md`. Answer first: profiles checked and those with misses (with S1 profiles named), cells run and cells flagged, the flag that most limits the read. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/integration_check.py words ANSWER.md`; without code execution, count the same way by hand. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every check, rule, ceiling and sample definition is the person's, or "not given".
- No overall conformance or reliability score; no profile averaged away; S1 profiles named.
- Mocked-token and not-run cells are visible.
- Every fact names its source and date in plain words with the row id after it.
- The record line is the very last line; the calls list and the offer of the full version come before it.

## Boundaries

- Choosing the guide, version or scopes: `dh-technology` interoperability-and-ehr-integration.
- Authorization errors that may be security issues: report the cell result only; analysis routes to `dh-technology` security-and-privacy-operations-monitoring.
