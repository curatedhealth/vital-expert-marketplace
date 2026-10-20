# A2 Mapping, workflow and standards read

Framework tasks: DH-04.01.3.2 and DH-04.01.4.2, Part A, task A2, with a dated standards currency read. Carries the old tasks "DH-04.01.3.2.1 Map sample definition", "DH-04.01.3.2.2 Blinded clinical review", "DH-04.01.4.2.1 Designed versus observed step" and "DH-04.01.4.2.2 Time and workaround count".

## What this task delivers

Three dated reads against the person's own definitions: the map sample (exact-match rate, unmatched rate, reviewer disagreements, error classes by map version); the clinical step after release (each designed action done, skipped or replaced, workarounds quoted, time range with the number of observations); and a standards currency read (which versions and dates the integration relies on have expired, moved or remain proposals, as read on 19 and 20 October 2026). It answers "how accurate is our map by our definition, what are clinicians actually doing at the step, and has any standard or rule we rely on moved?"

Why it matters: a map checked only by its author, a workflow read from analytics that cannot see the paper workaround, or a roadmap still built to US Core 3.1.1 after its adoption expired each says more than the data does.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `data-engineering-manager-health` (old DH-04.01.3.2.1, .2); `clinical-informatics-lead` (old DH-04.01.4.2.1, .2). Work as an integration quality analyst who reads the person's samples and observations against the person's definitions |
| Skill | DH-04.01.3.2 with DH-04.01.4.2, Part A, Mapping, workflow and standards read |
| Workflow | The steps below |
| Knowledge | `references/monitoring-rules.md` sections 3, 4 and 5 |
| Tools | `scripts/integration_check.py mapsample` and `workflow`; `verify.build_record` when the output leaves |
| Prompt | This guide |
| Template | `assets/mapping-workflow-and-standards-read-output.md` |
| Input | The request and its context: the map review sample (CSV), the person's rate definitions and thresholds if set, the workflow observations (CSV), the versions and rules the integration relies on, the read date |
| Governance | `references/governance.md`; definitions and thresholds are the person's |
| Catalogue job | none |

## Read the request

- **Read date.** From the person; "not given" otherwise.
- **Which reads.** Map, workflow, standards, or a combination. "Is our map good enough?" is short mode on the map, and "good enough" is the person's threshold: ask for it.
- **Thresholds.** If the person asks the model for a threshold, decline that part (no source sets one, `monitoring-rules.md`) and offer what the facts support: the computed rates, the Kahn categories and the decisions the person faces.

## Workflow

### Step 1. Map sample definition (old "Map sample definition")

Write back the person's sample size, draw method, the two rates as they define them, and their threshold for production use ("not given" if none). Flag a sample drawn from rows already hand-checked (R4).

### Step 2. Blinded clinical review (old "Blinded clinical review")

Run `python3 scripts/integration_check.py mapsample SAMPLE.csv --exact-labels "LABELS" [--min-exact R] [--max-unmatched R]` with the person's labels and thresholds (omit a threshold not given). Quote: rows sampled and reviewed, the exact-match and unmatched rates with numerator and denominator, the person's threshold met or not met (or "not given"), disagreement rows, and flags R1 (reviewer is the mapper), R2 (reviewer not blinded), R4. Frame the categories with Kahn et al. 2016 (DOI 10.13063/2327-9214.1244, DA-94 to DA-97): the target code against allowed values is value conformance; the reviewer's acceptance for the stated use is validation. Error classes are counted by map version.

### Step 3. Designed versus observed step (old "Designed versus observed step")

Run `python3 scripts/integration_check.py workflow OBS.csv`. Quote per designed action the done, skipped and replaced counts and each workaround verbatim with its observation id and site. Where the EHR is certified and the intervention is inside it, note that user feedback export exists as a data source (UX-US-55); HTI-5 proposes removing parts of (b)(11), proposed only (UX-US-60).

### Step 4. Time and workaround count (old "Time and workaround count")

From the same run: the time range with the number of observations per step; flag W1 where one observation exists (no mean, no range). Separate a slow screen from a step the design got wrong only where the person's observations say which; otherwise "not distinguishable from the observations".

### Step 5. Standards currency read

List the versions, compliance dates and proposals the person's integration relies on, and quote each from `monitoring-rules.md` section 5 with its source and date: expired adoptions (US Core 3.1.1, SMART 1.0.0, USCDI v1), dates passed (USCDI v3 update, CMS-0057-F process duties, Part 2 compliance, DTAC transition), dates ahead (CMS-0057-F APIs in 2027, EHDS 2027, 2029 and 2031), and proposals (HTI-5, HIPAA NPRM, CMS drug prior authorization, FHIR R6). State that the rows were read on 19 and 20 October 2026 and anything later is `[GAP]` until a research pass. Dates are facts, never pressure.

## Build the output

Follow `assets/mapping-workflow-and-standards-read-output.md`. Answer first: the two map rates with denominators and the person's threshold result, disagreements and reviewer flags; workarounds per step; the standards item that most affects the integration. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/integration_check.py words ANSWER.md`; without code execution, count the same way by hand. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every rate shows numerator, denominator and the person's definition.
- No threshold was supplied by the model; a missing one says "not given".
- Workarounds are quoted, not paraphrased; no mean from one observation.
- Every standards fact carries its source, its date and "as read on" date; proposals say "proposed".
- Every fact names its source and date in plain words with the row id after it; the Kahn rows carry the DOI at first use.
- The record line is the very last line; the calls list and the offer of the full version come before it.

## Boundaries

- Redesigning the step: `dh-patient-and-user-experience` clinical-workflow-ux-design.
- Organization-wide adoption: `dh-go-to-market` adoption-monitoring.
- Analytic dataset quality: `dh-technology` data-quality-monitoring.
