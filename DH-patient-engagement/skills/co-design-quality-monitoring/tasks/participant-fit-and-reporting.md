# A2 Participant fit and reporting

Framework task: DH-02.03.1.2, Part A, task A2. Replaces the register task "Participant fit" (CF-12.02.03.1.2.2) and adds a reporting check.

## What this task delivers

Per session, the participant types planned for the research question against those who attended, sessions missing a planned type, staff or clinicians present and how many captures came from them; a note on how far results reach; whether consent was recorded; and, for a report that will be shared, each GRIPP2-SF item (or GRIPP2-LF where involvement is the main focus) marked present, partial or `[GAP]`, with the UK Standards as a framework. It answers "were the right people in the room, and is the involvement reported fully?"

Why it matters: staff standing in for patients is not patient co-design (R-5). A decision built on sessions that missed the planned participant type may not stand (R-19 to R-21). Non-probability samples may not represent the target population (PE-06).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Patient Experience Designer (`patient-experience-designer`) |
| Skill | DH-02.03.1.2 Part A, Participant fit and reporting |
| Workflow | The steps below |
| Knowledge | `references/quality-criteria.md` (sections 2 and 3); rows R-5, R-19 to R-21, PE-06, PE-09, PE-13, PE-56, PE-61, PE-65 to PE-68, PE-89 to PE-92, UX-UK-19 |
| Tools | `scripts/insight_tracker.py` (`check`, `fit`, `tally`); `verify.qualify_source` and `verify.check_claim` (counted, optional) |
| Prompt | This guide |
| Template | `assets/participant-fit-output.md` |
| Input | The request and its context: the research question with its planned participant types, `sessions.csv`, `captures.csv`, the decisions that rest on the sessions, the report to be shared if any, whether consent was recorded per session |
| Governance | `references/governance.md`; records are reviewed, not people |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. |

## Read the request

- **The question and planned types.** From the research plan (sibling skill A1). Without planned types, fit cannot be checked: ask (R-19).
- **Sessions and captures.** Files or a table in the message. Aggregates by type per session are enough; never ask for names.
- **Decisions at stake.** Which decisions rest on which sessions, so the fit note can say whether each still stands (R-21).
- **Report.** If a report will be shared, ask whether involvement is its main focus (GRIPP2-LF) or secondary (GRIPP2-SF).
- **Mode.** Short for a direct question; full for a review.

## Workflow

### Step 1. Check the files

`python3 scripts/insight_tracker.py check FILES`. Stop on any identifier.

### Step 2. Fit per session

Run `python3 scripts/insight_tracker.py fit sessions.csv captures.csv`. Report per session: planned types, attended, planned types missing (R-20), staff or clinicians present, captures by type. Name any insight whose captures come only from staff (R-5) or only from carers (PE-13, carer evidence, not patient evidence).

### Step 3. Does each decision still stand?

For each decision the person names, state which sessions it rests on and whether those sessions included the planned type. Say "rests on sessions that included patients" or "rests on a session without the planned carers"; whether the decision still stands is the owner's call (R-21), and the output says so.

### Step 4. How far results reach

One or two lines: recruitment route, non-probability sampling (PE-06), any saturation claim and its stated basis (PE-09). If the panel is paid by the developer and the product may go to EU joint clinical assessment, note the conflict-of-interest rule for patient experts (PE-56) for the regulatory owner. NICE's two-lay-member rule is context only (PE-61).

### Step 5. Consent recorded

Per session, whether consent was recorded, as the person states it. MHRA's advisory guidance expects informed consent where practicable (UX-UK-19). Do not judge adequacy; missing records go to the person's ethics owner.

### Step 6. Reporting check (if a report will be shared)

Mark each GRIPP2-SF item (aims, methods, results, outcomes, critical perspective; PE-91) present, partial or `[GAP]`, with where it sits in the report. For GRIPP2-LF (PE-90), the full 34-item list is not in the research rows: check against the paper and mark `[GAP]` for items not verified. Optionally map the report to the six UK Standards (PE-65) as a framework. If the report cites GRIPP2 or another method, check the citation with `verify.qualify_source` then `verify.check_claim` on a passage read in the same direction; treat "partial" as unverified (register N3).

## Build the output

Follow `assets/participant-fit-output.md`. Answer first: sessions that missed a planned type or relied on staff, and the decisions that rest on them. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every count is from the person's files or the script.
- Staff and carer evidence is labeled as such.
- No verdict that a decision stands or falls; that is the owner's.
- No grade or score for the report unless the person set a scale.
- No identifier anywhere.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Fit and reporting of co-design only. Who the product reaches or leaves out goes to `health-equity-monitoring`; accessibility conformance goes to the User Experience pack.
- Usability study sample sizes and human factors validation populations belong to the User Experience pack.
- Ethics determinations belong to the person's ethics owner or IRB.
