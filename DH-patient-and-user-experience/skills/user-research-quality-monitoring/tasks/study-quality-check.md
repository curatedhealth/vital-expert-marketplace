# A1 Study quality check

Framework task: DH-02.04.3.2, Part A, task A1. Replaces the earlier "Sample fit" section (CF-12.02.04.3.2.2) and extends it to method fit, protocol completeness and reporting.

## What this task delivers

A finding-by-finding check of one finished study against sourced criteria: whether participants matched the role and task the question named, by user group; whether the method supports the claim the team is making from it; which formative protocol elements are present; whether patient involvement is reported (GRIPP2 short form, where patients were partners); and whether an ethics determination is on file. For each finding it states whether the action drawn from it still stands on the evidence. It answers "can we rely on this study for what we are using it for?"

Why it matters: the commonest misuse of user research is not bad sessions but a claim the sessions cannot carry: clinician findings applied to patients, or formative think-aloud sessions cited as validation. FDA's formative results do not carry to the final design (UXR-03), and validation has its own rules (UX-US-34 to UX-US-40).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Patient Experience Designer (`patient-experience-designer`) |
| Skill | DH-02.04.3.2 Part A, Study quality check |
| Workflow | The steps below |
| Knowledge | `references/study-quality-criteria.md`; `references/formative-and-validation.md`; rows UX-US-29 to UX-US-45, UX-UK-17, UX-UK-25, UX-M-07 to UX-M-19, UXR-02 to UXR-11, PE-06, PE-09, PE-65 to PE-68, PE-89 to PE-91 |
| Tool | `scripts/research_log.py stops` (sample fit from a session log). `verify.qualify_source` then `verify.check_claim` (counted, optional) when the report cites a paper. `verify.build_record` for sign-off |
| Prompt | This guide |
| Template | `assets/study-quality-check-output.md` |
| Input | The request and its context: the study question and plan, the session log or participant summary (pseudonymous), the report or the claims made from it, any protocol and ethics record |
| Governance | `references/governance.md`; criteria and evidence only; adequacy for validation and every verdict are the owner's or the person's |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. |

## Read the request

- **The claim.** What the team is using the study for ("we can ship", "validated", "nurses find it easy", "patients prefer X"). Without a claim, check sample and protocol only.
- **The question and plan.** Role, task, user groups, planned numbers.
- **Who took part.** Session log or a summary: role, group, employee, think-aloud, access needs where recorded.
- **Report and protocol.** What exists; quote it, do not rewrite it.
- **Patient involvement.** Whether patients were partners in the research (GRIPP2 applies) or only participants.
- **Mode.** Short for a direct question; full for a study audit.

## Workflow

### Step 1. Frame

Write back: the study, the claim being checked, and the criteria sets in scope (sample, method, protocol, reporting, ethics record). Confirm before checking.

### Step 2. Sample fit

Run `python3 scripts/research_log.py stops LOG.csv --plan "GROUP=N,..."` if a log exists, or work from the summary and say so. For each finding, check that the participants who produced it hold the role the question named (register method). Note any session with the wrong role, and state whether the action drawn from that finding still stands on the remaining sessions. Report groups apart (UX-US-36); held vs planned; employees (UX-US-45); people with condition-related limits where relevant (UX-US-37); the share with access needs beside NHS guidance of 1 in 5, labeled guidance (UX-UK-25); how participants were found (PE-06); whether a rationale for numbers is recorded (UX-UK-17). If an employee is the only participant in a group who completed a flagged critical task, say so in one line: the group's result on that task rests on a participant validation would exclude (UX-US-38).

### Step 3. Method fit

Match the claim to the method using the table in `references/study-quality-criteria.md` (section 2). If the claim is validation, safety or "easy to use", say which rows the study cannot meet (UXR-03, UX-US-34, UX-US-38, UX-US-40, UX-US-35) and that the claim stops for the regulatory or human factors owner. Saturation claims: ask what the last sessions added (PE-09).

### Step 4. Protocol elements

Mark each of the seven formative elements present, partial or absent (UXR-02). Absent "how results will be used" is reported first.

### Step 5. Reporting and ethics record

Where patients were partners: mark each GRIPP2 short-form item reported or not (UXR-07 to UXR-11); never sum them into a score. Note the UK Standards are a framework, not a rule (PE-65). Ethics: record whether a determination and its maker are on file (UX-M-11, UX-M-12, UXR-06; UX-UK-19 for Great Britain), never whether it was right.

### Step 6. Published claims in the report (optional)

If the report cites a paper (for example a SUS benchmark), call `verify.qualify_source {doi, question}`, then `verify.check_claim` with the claim, the passage you read and the full source object. Accept only if the passage states the claim in the same direction (register N3). For the SUS rows already in this skill, compare the report's wording with UX-M-08 to UX-M-10 directly.

### Step 7. Findings

List findings as facts: "Finding F3 rests on 2 clinician sessions; the question named patients" or "No protocol element states how results will be used". Each with criterion, row and evidence. No grade, score or average.

## Build the output

Follow `assets/study-quality-check-output.md`. Answer first: whether the claim is supported by the method and sample, and the one or two findings that matter most. Short mode: 450 words maximum, counted without the calls list and tables' source column. Every other table cell counts. Before handing over, count the words of the answer above "Calls made" (for example with `wc -w`) and state nothing over 450. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every criterion has a row id; every finding states its evidence.
- Groups are reported apart; wrong-role sessions are named and their effect on each action stated.
- No grade, score or GRIPP2 total; no verdict on adequacy for validation.
- Ethics: presence of a determination only.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Re-planning the study: `patient-and-clinician-user-research` (A1).
- Validation adequacy and submission content: `dh-regulatory-and-quality`.
- Co-design program quality: `co-design-quality-monitoring` (Patient Engagement).
- PRO and COA measurement properties (COSMIN): the clinical or regulatory owner.
