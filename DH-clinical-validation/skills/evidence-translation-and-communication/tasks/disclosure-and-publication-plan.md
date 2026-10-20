# A2 Disclosure and publication plan

Framework task: DH-01.02.2.1, Part A, task A2. Replaces the old "Clinical Publication Development" section.

## What this task delivers

For each study the person names: which disclosure regimes the person says apply, the registration test (ICMJE and, where applicable, US law), each results clock with its due date computed from the person's dates, the reporting checklist that fits the design with the items most often missed, the authorship test, the AI-use rule and the data sharing statement content. Every rule carries its row; every date shows its arithmetic.

Why it matters: registration timing decides whether an ICMJE journal will consider the paper (CV132), results clocks are legal duties for applicable trials (CV145, CV152), and a paper written without its checklist is sent back. These are fixed facts that can be planned in order, not judgment calls.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`) |
| Skill | DH-01.02.2.1 Part A, Disclosure and publication plan |
| Workflow | The steps below |
| Knowledge | `references/disclosure-rules.md`; `references/clinical-study-and-rwe-research.md` (CV rows) |
| Tools | `literature.find_trial` (registration link for a paper, or an NCT id), optional; `literature.build_citation` for a published paper; `verify.build_record` |
| Prompt | This guide |
| Template | `assets/disclosure-plan-output.md` |
| Input | The request and its context: per study, the registry and id, design, the person's dates (first consent, first enrollment, registration submitted, primary completion, end of trial in all EU Member States, any delay certification, approval or clearance), and the person's answers on which regimes apply |
| Governance | `references/governance.md`; registry actions and author lists are the person's |
| Catalogue job | none. The catalogue has no disclosure job. |

## Read the request

- **Which study, which design?** Trial, protocol, observational study, prediction model, sensor-derived measure. The design picks the checklist.
- **Which regimes?** Ask the person whether the trial is a US applicable clinical trial, whether it runs under the EU CTR, whether the funder signed the WHO joint statement, and whether results go to an ICMJE journal. Lay out the tests from `references/disclosure-rules.md` (CV133, CV142, CV143) if they are unsure, but the answer is theirs, or the owner's they name for registration (owner not named if none). Unanswered: compute nothing for that regime, `[GAP]`.
- **Dates.** Take dates from the person or from the registry record they give. Registry "start date" is a different field from first consent and first enrollment; ask which the person means.
- **Short or full?** "When are results due" is short. "Publication plan", "disclosure plan for the program" is full.

## Workflow

### Step 1. Confirm identity and registration link

If the person gives a paper, call `literature.find_trial` with the record; if an NCT id, with `nct_id`. It reaches ClinicalTrials.gov only and returns status, phase and sponsor without dates (`references/tools.md`). A trial registered elsewhere (for example DRKS) returns nothing: take the id from the paper. Never conclude a trial is unregistered from an empty result.

### Step 2. Registration test

- ICMJE: registration submitted at or before first patient consent (CV132), in an accepted registry (CV134). Compare the two dates the person gives; say "at or before" or "after by N days".
- US applicable clinical trial: due 21 calendar days after the first participant is enrolled (CV141). Show the date.
- Data sharing plan in the registration for trials enrolling from 1 January 2019 (CV135).

### Step 3. Results clocks

For each regime the person confirmed, compute and show:
- US: primary completion date plus 1 year (CV145). With a delay certification: 30 days after approval or clearance for a studied use, or after a 210-day withdrawal, and no later than 2 years after the certification (CV146). Extensions for good cause are requested before the deadline (CV147). Content: mortality table, adverse events above 5 percent in any arm, protocol and SAP (CV148).
- EU CTR: end of trial in all Member States plus 1 year, with the lay summary (CV152); end-of-trial notices within 15 days (CV151); halts and interim analyses (CV154); clinical study report within 30 days after a marketing authorization decision (CV153).
- WHO pledge (signatories only): 12 months from primary completion for summary results; 24 months from study completion for publication, indicative (CV140).
Write each date in full with its arithmetic ("31 January 2025 plus 1 year = 31 January 2026"). The counting convention for "1 year" is not in the rows `[GAP]`; say that one calendar year was added. State the status as of today: due on DATE, or past DATE and not reported by the person. A missing date is `[GAP]`, never estimated.

### Step 4. Reporting checklist

Name the checklist for the design with its [PAPER] row and DOI (`references/disclosure-rules.md`): CONSORT 2025 for a randomized trial, with CONSORT-AI where the intervention is AI (noting it extends CONSORT 2010); SPIRIT 2025 for a protocol; STROBE for observational studies; TRIPOD+AI for a prediction model; V3 terms for a sensor-derived measure. If the person shares a draft, list the checklist items the draft does not yet address, by item number, from the rows only (for CONSORT 2025: items 2 to 5, 8, 10, 14, 15, 21b, 21c, 24a are quoted in the rows; other items are not quoted `[GAP]`).

### Step 5. Authorship, AI and data sharing

State the four ICMJE criteria (CV130); the author list is the authors'. AI is not an author and its use is disclosed (CV131). The data sharing statement must say whether IPD will be shared ("undecided" is not acceptable), what, related documents, when and how long, and access criteria (CV136). Registry results posted as a brief structured abstract or tables are not prior publication (CV137), so posting results does not block the paper.

### Step 6. Order by dependency

List the actions in the order one unlocks the next (registration before consent; SAP before outcome data are seen, CV94 where the study is a device RWE study; results summary, then lay summary, then paper), each with its owner as the person named them, or "owner not named". Clocks are facts; no urgency language.

## Build the output

Follow `assets/disclosure-plan-output.md`. Answer first: the next due date and the rule behind it, or the regime decision that blocks the computation.

## Before you hand it over

- Every clock shows its rule, the input date and the arithmetic; no regime applied that the person did not confirm.
- No statement that a trial is or is not an applicable clinical trial or under the EU CTR.
- Every checklist cites its [PAPER] row and DOI.
- Count the words in short mode.
- If the plan leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- The skill does not register a trial, post results, request extensions or certify delays.
- Study design and protocol content belong to DH-01.02.1 (clinical study design) in this pack; trial operations to DH-01.02.3.
- Monitoring of whether the duties were met over time belongs to the sibling skill, evidence-communication-monitoring (task A1).
- Drugs and biologics are out of scope for this pack, even though some rows cover drug trials.
