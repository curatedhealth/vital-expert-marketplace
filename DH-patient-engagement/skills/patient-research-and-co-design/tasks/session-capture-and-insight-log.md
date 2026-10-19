# A2 Session capture and insight log

Framework task: DH-02.03.1.1, Part A, task A2. Replaces the register task "Session capture" (CF-12.02.03.1.1.2).

## What this task delivers

A capture of what participants said or did, in their words, each row marked request or observation, linked to an insight; and a tally per insight of how many distinct participants raised it, in how many sessions, with patients and carers counted apart from staff. It answers "what did participants tell us, and which points come up more than once?"

Why it matters: a capture that rewrites participants' words as product requirements loses the evidence the decision rests on (R-9). Counting staff words as patient words turns staff opinion into "what patients said" (R-5). A tally is only as honest as the separation of request from observation (R-7).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Patient Experience Designer (`patient-experience-designer`) |
| Skill | DH-02.03.1.1 Part A, Session capture and insight log |
| Workflow | The steps below |
| Knowledge | `references/insight-log.md`; `references/co-design-method.md` (section 7); rows PE-13, PE-89 to PE-91, PE-102, PE-105 |
| Tools | `scripts/insight_tracker.py` (`check`, `tally`, `fit`); no library call |
| Prompt | This guide |
| Template | `assets/session-capture-output.md` |
| Input | The request and its context: session notes, transcripts or sticky-note photos typed out, the research question from A1, the person's rule for a repeated point if any |
| Governance | `references/governance.md`; no identifiers; the person's data stays in the conversation |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. |

## Read the request

- **Material.** Notes, transcript excerpts or an existing `captures.csv`. If notes are paraphrased by a note-taker, say so per row.
- **Identifiers.** Before anything else, scan for names, contact details, dates of birth, record numbers. With code execution, run `python3 scripts/insight_tracker.py check FILES`. If anything is found, stop and ask the person to remove it.
- **The question.** From A1. Captures that do not bear on the question stay in the log, marked "outside the question".
- **Their rule for "repeated".** Ask. Offer R-10 ("more than one participant") as the starting rule.
- **Mode.** Short for a direct question; full for the session report.

## Workflow

### Step 1. One row per thing said

Split notes into rows: session, date, participant code and type, request or observation, the words. Quote the words exactly where the notes allow (R-6). A request asks for something ("let me see the readings too"); an observation reports what happened or how it felt ("I stopped logging after the first week"). When a row is both, split it. Do not add a product requirement in this step (R-9).

### Step 2. Group into insights

Give rows that make the same point the same `insight_id` and write a one-line summary in neutral words. Keep a row unlinked if it fits nothing yet. Never merge a carer's or staff member's point into a patient insight without saying so.

### Step 3. Tally

With code execution: `python3 scripts/insight_tracker.py tally captures.csv --repeat N` (N only if the person set or adopted a rule). Without code execution, count by hand. Report per insight: distinct patient-side participants, staff captures apart, sessions, requests, observations. With the sessions file, `fit sessions.csv captures.csv` shows planned versus attended participant types and staff present.

### Step 4. Read it carefully

- A point raised by many people in one session may reflect the session, not the population: say how many sessions it came from.
- Recruitment was non-probability (PE-06): counts describe these participants, not patients in general.
- If usage data was discussed, keep dropout attrition and nonusage attrition apart (PE-102) and do not compute engagement measures here.
- No cause, no fix, no priority in this task. Those are B1.

### Step 5. Reporting

If the session report will be published or shared, map it to GRIPP2-SF items (aims, methods, results, outcomes, critical perspective; PE-91) and mark each item present or `[GAP]`.

## Build the output

Follow `assets/session-capture-output.md`. Answer first: the points that repeat under the person's rule (or the counts with no label if no rule), with participant and session counts. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every quote is the participant's words or marked paraphrased.
- Requests and observations are separate.
- Staff and clinician words are counted apart from patients and carers.
- "Repeated" is used only under the person's rule.
- No identifier anywhere; no participant data went into a library call.
- If it leaves the conversation, ask who clears it and call `verify.build_record` (decisions by insight id, no words or codes); otherwise label it an uncleared draft.

## Boundaries

- Capture and counting only. Decisions are B1.
- Usability findings (task failures, use errors) are reported as observations and handed to the User Experience pack; no usability conclusion here.
- Engagement KPIs belong to `engagement-kpi-dashboards`.
