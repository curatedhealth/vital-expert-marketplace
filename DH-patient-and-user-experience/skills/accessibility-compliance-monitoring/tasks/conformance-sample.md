# A1 Conformance sample

Framework task: DH-02.04.1.2, Part A, task A1. Replaces the earlier "Conformance sample" section.

## What this task delivers

For the screens and processes the person sampled, against the version and level their requirement claims: the status of each criterion per screen (pass, fail, not applicable, not tested) from their test records, the method behind each status, the processes left incomplete, and what the sample cannot show. It answers "where does this build stand against the target we set, and what have we not tested?"

Why it matters: conformance holds only for full pages and complete processes (UX-STD-21, UX-STD-22), and automated tests check only part of what needs testing (UX-UK-24). A sample read from a scan alone looks complete and is not.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Health Equity & Digital Access Lead (`health-equity-access-lead`) |
| Skill | DH-02.04.1.2 Part A, Conformance sample |
| Workflow | The steps below |
| Knowledge | `references/conformance-sampling.md`; `references/data/wcag_criteria.csv`; `references/ux-accessibility-research.md` |
| Tools | None from the library. `verify.build_record` only for sign-off |
| Prompt | This guide |
| Template | `assets/conformance-sample-output.md` |
| Input | The request and its context: the claimed target (version, level, or EN 301 549 clause), the screens and processes in the requirement, the build, the person's test records with method and date |
| Governance | `references/governance.md`; statuses come from the person's records; no conformance statement |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. |

## The rule that shapes this task: test what was claimed, report what was tested

Sample against the target in the person's requirement, not another standard (old register rule, kept). Every status rests on a record the person supplied; a criterion with no record is "not tested", never "pass".

## Read the request

- **Target.** Version and level from the requirement. If the person asks about a different one, run it as a second, labeled view; do not replace the claimed target.
- **Scope.** The screens and processes in the requirement, and which were sampled. The person picks the sample; the rows set no sampling rule `[GAP]`.
- **Records.** Results per criterion and screen, with method (automated tool, manual, assistive technology, research session) and date. Ask for the automated tool's list of criteria it checks if results rest on it.
- **Build.** The build or version the records belong to.
- **Mode.** Short for a direct question; full for a sample report.

## Workflow

### Step 1. Fix the frame

Write back: target (version, level, criteria count from `references/data/wcag_criteria.csv`), build, screens sampled, processes they belong to, records and methods. Name any process in the requirement with no sampled page.

### Step 2. Status per criterion, per screen

From the records, mark each in-target criterion: pass, fail (issue id), not applicable (the person's reason; for EN 301 549 a false precondition, UX-STD-33), not tested. Where results come only from an automated tool, mark criteria outside the tool's stated coverage "not tested"; if the coverage list is not given, every criterion without a manual or person-based record is "not tested" (`references/conformance-sampling.md`).

Points to check where they apply:

- Each responsive variation of a screen is part of the page (UX-STD-21).
- A fail on any page of a process means the process does not conform at that level (UX-STD-22).
- Native app screens and web views: EN 301 549 clause 11 (UX-STD-31, UX-STD-32); Section 508 software exceptions (UX-US-03, UX-US-04).
- 4.1.1 Parsing: not in 2.2; report it only if a 2.0 or 2.1 policy applies (UX-STD-08, WX7).

### Step 3. Findings

List findings as facts: "Sign-in process: 3.3.8 fail on the password screen (A11Y-01); the process does not conform at 2.2 AA." "12 of 55 in-target criteria tested only by an automated tool." Each names the screen or process, the criterion and level, the record and the row. No severity unless the person's records carry it.

### Step 4. What the sample cannot show

One short list: processes not sampled, criteria not tested, methods not used (for example no test with assistive technology users, UX-US-78), and that issues not found are not evidence of conformance.

## Build the output

Follow `assets/conformance-sample-output.md`. Answer first: the processes with a fail, the count of in-target criteria not tested, and the method mix. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- The target is the one the requirement claims, and the output says which.
- Every status rests on a record; untested criteria say "not tested".
- Every scan-based result carries the note that automated tests cover only part (UX-UK-24).
- No statement that the build or a screen conforms.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Reads the person's test records; it does not run tests or scan URLs.
- Setting the target and scope is the sibling skill (DH-02.04.1.1, B1). The release decision is B1 here.
- Usability findings that are not accessibility criteria belong to UX 4.x.
