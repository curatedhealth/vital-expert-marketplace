# A1 Co-design trace

Framework task: DH-02.03.1.2, Part A, task A1. Replaces the register task "Co-design trace" (CF-12.02.03.1.2.1).

## What this task delivers

For a release or a period, the trace from each design change credited to co-design back to the insight and the participants' captured words: traced, credited with no capture link, planned before the first capture, linked to an unknown insight; plus accepted insights with no shipped change. It answers "can each change we credit to patients be traced to what they said?"

Why it matters: a change credited to co-design with no capture behind it is not from this research (R-18), and a change the team had already planned should not be credited to co-design (R-14). A team that says "designed with patients" without a trace makes a claim it cannot support; the UK Standards ask that the difference involvement makes be identified and shared (PE-68).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Patient Experience Designer (`patient-experience-designer`) |
| Skill | DH-02.03.1.2 Part A, Co-design trace |
| Workflow | The steps below |
| Knowledge | `references/quality-criteria.md` (section 1); `references/insight-log.md`; rows R-12, R-14, R-16 to R-18, R-23, PE-68, PE-91 |
| Tools | `scripts/insight_tracker.py` (`check`, `trace`, `status`); no library call |
| Prompt | This guide |
| Template | `assets/co-design-trace-output.md` |
| Input | The request and its context: `changes.csv` (or the release notes with a "credited to co-design" mark), `insights.csv`, `captures.csv`, backlog dates where the person has them, the as-of date, any rule for trace coverage |
| Governance | `references/governance.md`; a trace shows provenance, not effect; "co-designed" claims stop for the owner |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. |

## Read the request

- **Scope.** Which release, product version or period.
- **Files.** The four files in `references/insight-log.md`, or the same facts in the message. If changes are not marked as credited to co-design, ask which ones the team credits (R-16).
- **Backlog dates.** Ask whether the team can give, per credited change, the date it first entered the backlog. Without it, the "planned before capture" check cannot run: `[GAP]`.
- **Their rule.** Ask whether they have a rule (for example every credited change traced). Without one, report numbers and no verdict.
- **Mode.** Short for a direct question; full for a review pack.

## Workflow

### Step 1. Check the files

With code execution: `python3 scripts/insight_tracker.py check FILES`. Stop on any identifier. Check that every insight id on a change exists in the log.

### Step 2. Trace

Run `python3 scripts/insight_tracker.py trace changes.csv insights.csv captures.csv`. Without code execution, do the same by hand. Report:

- traced: credited change → insight → at least one capture (R-17);
- credited with no capture link: "not from this research" (R-18);
- planned before capture: backlog date earlier than the first capture of every linked insight; do not credit co-design for the idea, though the capture may still support it (R-14);
- unknown insight ids;
- accepted insights with no change in the file, accepted insights with no version (R-12), and accepted insights with no owner (R-23; `status`).

### Step 3. Evidence behind each traced change

For each traced change, give the insight's distinct patient-side participants and sessions (`tally`) and one quote. Flag a traced change whose only captures are staff words (R-5): traced to a capture, but not to patient co-design.

### Step 4. Check against their rule, if any

Trace coverage is traced credited changes over all credited changes. Pass or miss only against the person's rule; otherwise "no rule set".

### Step 5. What it means for the person

Two or three consequences, conditional and from the rows only. For example: "If release notes say 'designed with patients' for CH-13, the trace does not support it (R-18); that wording stops for your owner." "A change planned before the sessions can still cite the sessions as support, not as its origin (R-14)."

## Build the output

Follow `assets/co-design-trace-output.md`. Answer first: traced out of credited, and which changes are not supported. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every count comes from the person's files or the script output.
- "Traced" is never written as "worked", "validated" or "patient-centered".
- No verdict without the person's rule.
- Staff-only traces are flagged.
- No identifier anywhere; nothing from the files went into a library call.
- If it leaves the conversation, ask who clears it and call `verify.build_record` with change and insight ids only; otherwise label it an uncleared draft.

## Boundaries

- Provenance only. Whether participants fit the question is A2; what to do about open points is B1.
- Whether a change improved use, adherence or outcomes belongs to engagement measurement and clinical evidence skills.
- Promotional "co-designed" wording goes to the person's regulatory or legal owner (Commercial claims rules).
