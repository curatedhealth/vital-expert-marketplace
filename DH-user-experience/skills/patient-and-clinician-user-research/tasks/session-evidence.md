# A2 Session evidence

Framework task: DH-02.04.3.1, Part A, task A2. Replaces the earlier "Session evidence" section (CF-12.02.04.3.1.2).

## What this task delivers

A session record built from the person's own logs: participants per user group against the plan, outcomes per task, each stop with the number of distinct participants who hit it by group and their own words, stops on tasks the owner flagged critical, method flags (employees, think-aloud), and SUS scores per respondent and per group or round with published means as labeled context. It answers "what happened in the sessions, and how many people hit each stop?"

Why it matters: findings written before or apart from the session record drift toward what the team expected. Counting distinct participants by group, in their words, is what lets B1 decide on evidence and lets the monitoring sibling check later that an action traced to a real stop.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Patient Experience Designer (`patient-experience-designer`) |
| Skill | DH-02.04.3.1 Part A, Session evidence |
| Workflow | The steps below |
| Knowledge | `references/session-evidence-and-sus.md`; `references/formative-and-validation.md`; rows UX-US-27, UX-US-28, UX-US-31, UX-US-36, UX-US-40, UX-US-41, UX-US-45, UX-UK-15, UX-M-07 to UX-M-10, PE-09 |
| Tool | `scripts/research_log.py stops` and `sus` (local, no connector). `verify.qualify_source` and `verify.check_claim` only if the person brings a published SUS claim. `verify.build_record` for sign-off |
| Prompt | This guide |
| Template | `assets/session-evidence-output.md` |
| Input | The request and its context: the study plan (A1), a session log and a SUS file with pseudonymous codes, the person's critical-task flags and their rule for "repeated" if any |
| Governance | `references/governance.md`; counts and words only; use error, severity and acceptability are the owner's |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. |

## Read the request

- **Files.** A session log (one row per participant per task) and, if used, a SUS file. Columns are listed in the script header. If the person pastes a summary instead, work from it and say "from your summary, not a log".
- **Identifiers.** If a file holds names, contact details or record numbers, stop and ask for a pseudonymized version. The script refuses such files.
- **Plan.** Planned numbers per group from A1, if any.
- **Critical-task flags.** From the person or their owner. None given: "critical tasks not flagged `[GAP]`".
- **Rule for "repeated".** The person's minimum, if any.
- **Mode.** Short for "what did the sessions show"; full for a session report.

## Workflow

### Step 1. Run the counts

`python3 scripts/research_log.py stops LOG.csv --plan "GROUP=N,..." [--min-participants N]`. Without a log, build the same table by hand from the summary. Report participants per group against the plan; a group short of its plan is a fact, not a verdict.

### Step 2. Stops, in their words

For each stop: distinct participants, split by user group (UX-US-36), the tasks it occurred on, and one or two verbatim quotes. Do not merge stops the person coded separately; if two look alike, ask. Treat the instructions, labels and training material as part of the UI (UX-US-31).

### Step 3. Critical-task stops

List every stop on a task the owner flagged critical, whatever its count, and say it goes to the human factors or regulatory owner as recorded. Do not label it a use error (UX-US-27, UX-UK-15) or rate severity. Note when training was given if the log records it (UX-US-41).

### Step 4. Method flags

Report employees and think-aloud sessions. Both are acceptable in formative work (UX-US-45, UX-US-40). If anyone plans to reuse these sessions as validation evidence, say they cannot serve that purpose (UX-US-38, UX-US-40, UXR-03). If an employee is the only participant in a group who completed a flagged critical task, say so in one line. It is a fact from the log, not a verdict.

### Step 5. SUS (if a file is given)

`python3 scripts/research_log.py sus SUS.csv --by user_group` (or `round`). Report per group: n, mean, median, SD, range; list excluded responses with the reason (no imputation, `[GAP]`). Beside the person's figures, give context with its basis: 68 (SD 12.5), the general benchmark as cited by Hyzy et al. from Sauro and Lewis (UX-M-08, [PAPER], DOI 10.2196/37290); 76.64 (SD 15.12) across 114 digital health apps, 68.05 without physical-activity apps (UX-M-09, [PAPER], DOI 10.2196/37290). Never call a score good, bad, passing or failing; no adjective bands (`[GAP]`). If the person's own rule exists, apply it and say it is theirs.

### Step 6. Saturation note

Say whether the last sessions in the log added stops not seen before. Do not declare saturation; FDA sets no criteria for it (PE-09).

## Build the output

Follow `assets/session-evidence-output.md`. Answer first: the stops hit by the most participants, by group; any stop on a flagged critical task; the SUS figures with n. Short mode: 450 words maximum, counted without the calls list and tables' source column. Every other table cell counts. Before handing over, count the words of the answer above "Calls made" (for example with `wc -w`) and state nothing over 450. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every count is distinct participants, by group, from the log or the person's summary (say which).
- Quotes are verbatim; no finding is written that the record does not show.
- Critical-task stops are listed for the owner without a use-error or severity label.
- SUS: n beside every mean, exclusions listed, published means labeled as context.
- No "usable", "easy to use" or "validated" wording.
- If the person asks for board, investor or regulator wording, decline the claim and give a "draft for the owner" stating only the measured figures with n and round, for example "Round 1 mean SUS 68.1 (n 9); round 2 80.7 (n 7), different respondents; stops on both flagged critical tasks."
- No identifiable data in the answer or the files used.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Whether stops lead to actions is B1; whether research was acted on over time is `user-research-quality-monitoring`.
- Validation results, residual risk and the usability engineering file: the regulatory or human factors owner (`dh-regulatory-strategy`).
- Usability metrics on a released product over time: `usability-monitoring`.
