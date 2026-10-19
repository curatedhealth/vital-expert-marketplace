# A2 Barrier fix and assistive check

Framework task: DH-02.04.1.1, Part A, task A2. Replaces the earlier "Barrier fix" and "Assistive check" sections.

## What this task delivers

For one barrier on one listed screen: the WCAG criterion it meets and the criterion's level in the person's target version, the requirement as sourced, the change (the person's, or a proposal labeled "proposed"), the path a person using the named method takes to complete the task after the change, and the record of the assistive check (method, task, where it breaks). It answers "what does this barrier fail, what changes, and how do we know a person can now complete the task?"

Why it matters: a fix that only moves a scan score has not changed what a person can do. Automated tests check only part of what needs testing (UX-UK-24), and accessible components do not make a service accessible (UX-UK-28, UX-US-78).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Health Equity & Digital Access Lead (`health-equity-access-lead`) |
| Skill | DH-02.04.1.1 Part A, Barrier fix and assistive check |
| Workflow | The steps below |
| Knowledge | `references/barrier-criteria.md`; `references/data/wcag_criteria.csv`; `references/ux-accessibility-research.md` |
| Tools | None from the library. `scripts/criteria_lookup.py find` for the criterion and level. `verify.build_record` only for sign-off |
| Prompt | This guide |
| Template | `assets/barrier-fix-output.md` |
| Input | The request and its context: the barrier as observed, the screen and task, the target version and level, the assistive method the requirement names, any check results the person has |
| Governance | `references/governance.md`; the change and "fixed" are the person's; no conformance statement |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. |

## The rule that shapes this task: one barrier, one screen, one path

Each run handles one barrier on one listed screen. A barrier is recorded as fixed only when the person states the path someone using the named method takes to complete the task, and who checked it with which method (`references/barrier-criteria.md`). An automated scan does not substitute for a method the requirement names (old register rule, kept).

## Read the request

- **Barrier.** What was observed, in the person's words, and how (automated, manual, assistive technology, research session).
- **Screen and task.** Which listed screen, which task the person was doing. If the screen is not in the release's list, say so; scope is B1's.
- **Target.** Version and level (from B1 or the person). Without one, give the level in each version and ask.
- **Method.** The assistive method the requirement names (keyboard, screen reader, magnification, voice). If none is named, ask; do not pick.
- **Mode.** Short for one barrier; full for a fix record.

## Workflow

### Step 1. Name the criterion

Match the barrier to a criterion using `references/barrier-criteria.md`, or by number with `scripts/criteria_lookup.py find <number or words>`. Give the number, name, level in the target version, and the row. If the criterion's text is not quoted in a UX-STD row, write "criterion text not quoted here `[GAP]`". If the barrier fits more than one criterion, list each; if none fits, write "criterion not identified" and ask the person or their tester.

### Step 2. Check it against the target

State whether the criterion is in the target (version and level). Outside the target (a 2.2-only criterion against a 2.1 target, an AAA criterion against AA, 4.1.1 against 2.2): say so and keep the barrier; whether to fix it is the person's call. Where another obligation from A1 names the criterion (for example NHS requires the six new 2.2 A and AA criteria, UX-UK-23), say that in one line.

### Step 3. Describe the change

Use the change the person's team proposes. If asked for one, write it as "proposed", tied to the sourced requirement (for example "proposed: raise the dose button's target to at least 24 by 24 CSS pixels, UX-STD-11"). Do not quote code or platform guidance from memory. A proposal may still state what the change must achieve in each candidate criterion's own terms, labeled "proposed": for a drag-only slider, a way to set the value with a single pointer without dragging (UX-STD-10) and a control whose value the named assistive technology can read and set (4.1.2, Level A, text [GAP]).

### Step 4. The path

Write the task as the person using the named method would complete it after the change, step by step, for that screen only. If the path cannot be written from what the person supplied, the barrier stays open and the output says what is missing.

### Step 5. The assistive check record

Record: method (as named), task, screen, build or version, date, who ran it, result per step, where it breaks. Breaks stay open; do not mark a break minor or call the barrier fixed. If the check was automated only and the requirement names a person, write "assistive check not yet run".

## Build the output

Follow `assets/barrier-fix-output.md`. Answer first: the criterion and level, whether it is in the target, and the barrier's state (open, change proposed, change made and checked with the named method). Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- The criterion has its number, level from the table and a row; unquoted text is `[GAP]`.
- The change is the person's or labeled "proposed".
- "Fixed" appears only with a path and a check by the named method.
- No statement that the screen or release conforms.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- One barrier at a time. Logging, ageing and summarizing many issues is the monitoring skill (DH-02.04.1.2, A2).
- Usability problems that are not accessibility criteria (task flow, workflow fit, use error) belong to UX 4.x.
- Which assistive technologies to support is the person's decision; the sources do not list them `[GAP]`.
