# A2 Study execution record

Framework task: DH-01.07.3.1, Part A, task A2. Replaces the earlier "Study execution record" section (CF-12.01.07.3.1.2).

## What this task delivers

A dated execution record for a real-world study, built from the person's own documents, that shows in order: when the study type was declared, when protocol and analysis plan were final, when the study was registered, when anyone first saw outcome data, when analysis started, and every revision and deviation since, with its reason. It answers "can we show the plan was fixed before outcomes were seen, and what changed?"

Why it matters: FDA asks whether protocol and analysis plan were finalized before outcome data were reviewed, and wants to be confident analyses were not chosen to favor a conclusion (CV94, CV75). The record is the only way to show that. It also produces the conformance statement the result must carry (HE-028).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Clinical Trials Director |
| Skill | DH-01.07.3.1 Part A, Study execution record |
| Workflow | The steps below |
| Knowledge | `references/execution-and-reporting.md`; CV and HE rows |
| Tool | `scripts/prespec_check.py` (local); `literature.find_trial {record}` only if a publication exists; the person's registry record otherwise |
| Catalogue job | none |
| Prompt | This guide |
| Template | `assets/study-execution-record-output.md` |
| Input | The request; the person's dated documents (protocol and analysis plan versions, registration record, data-access log, revision and deviation log, data linkage plan) |
| Governance | `references/governance.md`; dates come only from the person's documents |

## Read the request

- **Which study and which framework.** Device (FDA CDRH, CV94), drug or biologic (FDA, CV75), EU medicine non-interventional (CV108), or a HETE publication standard (HE-027). Ask if not clear.
- **What documents exist.** A log, a folder of versions, or only memory. Dates from memory are written as the person's statement and marked "not documented".
- **Purpose.** A submission appendix, an internal audit, or a methods section. Submission use stops for the owner.

## Workflow

### Step 1. Build the log

Turn what the person gives into the JSON shape in `examples/illustrative_study_log.json`: study type and declaration date, document versions with final dates, registration (registry, id, submission date), first outcome access (date and who), analysis start, revisions (document, version, date, reason), deviations (date, description, reason), linkage plan. Never fill a date the person has not given; leave it empty.

### Step 2. Run the check

Run `python3 scripts/prespec_check.py LOG.json --md OUT.md` if code execution is available; otherwise apply the same eight checks by hand (listed in the script header). The script states order and completeness only.

### Step 3. Read the result for the framework

- If first outcome access is not dated: say first that prespecification cannot be shown, and that this blocks a HETE label (HE-026, HE-027).
- If protocol or analysis plan were final after first outcome access: the affected analyses are not prespecified; a device submission must say so (CV94).
- Revisions after first outcome access are deviations; they go in the conformance statement (HE-028), never in the "prespecified" column.
- Registration: confirm from the person's registry record. If a publication exists, `literature.find_trial {record}` searches ClinicalTrials.gov only; "no linked registration found" is not proof of absence. The library cannot search ENCePP, the HMA-EMA Catalogue or PROSPERO (`references/tools.md`).
- Linkage: prespecified with an inconsistency rule, or not (CV24).

### Step 4. Provenance and data handling

Ask, and record the answers as given: where the data first land and whether that store has an audit trail (CV82, CV60 by analogy); whether transformations are documented (CV87); whether data-access agreements allow patient-level submission if a drug application is in view (CV76). Unanswered items are `[GAP]`.

### Step 5. Is it a trial?

If the log shows prospective assignment to the product, it is a clinical trial (CV133) and trial registration and results clocks apply (CV132, CV141, CV145, CV152). State the clocks as facts, not as pressure, and point to dh-clinical-validation `decentralized-trial-operations` (DH-01.02.3.1).

### Step 6. Draft the conformance statement

From the deviations and late revisions, draft the statement of conformance or deviation the result will carry (HE-028), each deviation with its date and reason. Label it "draft for the owner".

## Build the output

Follow `assets/study-execution-record-output.md`. Short mode: the answer (can prespecification be shown, yes, no or not yet, and the one date that decides it), the check table (including the linkage row), at most three open items, the record line. Full mode adds the timeline, the provenance answers, the draft conformance statement and the trial test.

## Before you hand it over

- Every date is the person's, with its document; none is inferred.
- Revisions after first outcome access appear as deviations.
- No statement that the study "complies" with a guidance; the output states order and gaps.
- Submission use, registration changes and regulator wording stop for the owner.
- The record line ends the answer: "Clears it: [the person named, in their words, or owner not named]. The record is built with verify.build_record once that named person clears it; until then, uncleared draft."
- Any [PAPER] row id in the check table (HE-026, HE-027, HE-028) carries the Berger DOI 10.1002/pds.4297, as the script prints it.

## Boundaries

- The model does not register, amend or sign anything.
- Trial operations, monitoring and results posting are dh-clinical-validation `decentralized-trial-operations`.
- Data-protection agreements and consent wording stop for the owner the person names for data protection and consent, or owner not named.
