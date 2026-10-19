# A2 Use-error and critical-task analysis

Framework task: DH-02.04.4.1, Part A, task A2. Replaces the earlier "Safety of the screen" section.

## What this task delivers

For each task in the A1 fit: the use errors that could happen (misreads such as wrong patient, wrong dose, wrong unit, stale result, and wrong actions), the harm each could lead to, the severity the person assigns, whether the task is critical under the definition the person adopts, the control on the screen or around it, and the control's type in FDA's order of preference. Controls that rest only on labeling or training are marked "needs data". A misread with no control stays open as `[GAP]`. Optionally, comparable field events from the library prompt misreads the team has not listed. It answers "what could a user get wrong here, and what stops it?"

Why it matters: FDA defines a critical task by the serious harm an error could cause, including compromised care (UX-US-28), and ranks design above protective measures above labeling and training (UX-US-33). A team that lists controls without their type tends to lean on training, which FDA does not accept alone after critical-task errors (UX-US-42, CS79).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Service Design Director (`service-design-director`) |
| Skill | DH-02.04.4.1 Part A, Use-error and critical-task analysis |
| Workflow | The steps below |
| Knowledge | `references/use-error-and-critical-tasks.md`; `references/ux-usability-research.md`; `references/implementation-research.md` |
| Tools | `regulatory-dh.list_jurisdictions` (free) and `regulatory-dh.search_safety_events` (counted), optional; `verify.build_record` for sign-off |
| Prompt | This guide |
| Template | `assets/use-error-output.md` |
| Input | The request and its context: the A1 fit (or the person's task list), their known misreads and controls, their severity scale and any risk file entries |
| Governance | `references/governance.md`; severity, criticality and risk acceptance are the person's |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. The post-market-watch job also reads safety events but sets a watch; it is not called. |

## The rule that shapes this task: the person assigns severity; the model never closes a gap

The model lays out each use error with the sourced definitions. The person assigns severity on their own scale and decides which tasks are critical. A misread without a control is never closed by the model, and a screen with an open critical-task gap is never called ready (old register rule): it stops for the risk owner.

## Read the request

- **Tasks.** From A1 if present; otherwise the person's task list. One analysis per distinct population (UX-US-36).
- **Severity scale.** Ask for theirs. Without it, severity stays "not assigned `[GAP]`".
- **Definition.** FDA's (UX-US-28) for US, MHRA's (UX-UK-18) for GB, or both. For the EU the duty is MDR Annex I section 5 (UX-EU-14); no separate EU definition of critical task is in the sources `[GAP]`.
- **Known controls.** What exists in the design, and whether it exists in the build (a mock-up is not the build).
- **Product and comparables.** For the optional field-event step: the product type, and any comparable products or manufacturers the person names.
- **Mode.** Short or full.

## Workflow

### Step 1. Fix the frame

Write back: tasks, populations, market, definition used, the person's severity scale (or none). Confirm.

### Step 2. List use errors per task

For each task, list misreads and wrong actions, using the person's known issues first. Prompt for the classes the old register named (wrong patient, wrong dose, stale result) and for the user's medical and physical conditions and environment (UX-EU-14) and, where the condition limits function, the range of those limits (UX-US-37). Check each against the definition: a wrong result caused solely by a device fault is not a use error (UX-US-27, UX-UK-15); move it to the person's risk file as a device failure.

### Step 3. Optional: comparable field events

Only if the person wants comparables. Call `regulatory-dh.list_jurisdictions` once (free) to know which markets hold events (on 19 October 2026: US 892, UK 10, EU 0, CH 0). Then call `regulatory-dh.search_safety_events` with the product type or a named comparable:

- `{product: "<product type word, for example insulin>", jurisdiction: "US", since: "<YYYY-MM-DD the person chooses>", limit: 10}`
- `{manufacturer: "<comparable the person names>", limit: 10}`

The tool has no use-error filter (`references/tools.md`). Read each summary and keep only those that describe the interface or user interaction, and say the sorting is yours. Report each as its record states, with title, event date and severity class, cited as "openFDA enforcement report, record not linked" for US rows or the gov.uk URL for UK alerts. Turn each into a prompt ("check how the dose field handles a comma decimal separator", after the Omnipod 5 recall of 23 May 2025), never into a finding about that product.

### Step 4. Severity and criticality

Ask the person to assign severity to each use error on their scale, then to mark which tasks are critical under the definition they chose. Write both back in their words. FDA treats severity as more meaningful than probability for deciding what to design out (UX-US-32); do not estimate probability.

### Step 5. Controls and their type

For each use error, record the control the person names and its type: design (inherent safety), protective measure, or information for safety (labeling, training) (UX-US-33). Mark:
- "needs data" for a critical-task control that is labeling or training only (UX-US-42, CS79);
- "designed, not in build" where the control exists only in a mock-up;
- "no control `[GAP]`" where none is named.

For lay-use screens that show a result, check whether the user can tell the device works and is warned when no valid result was produced (UX-EU-19).

### Step 6. Open items and stops

List every "no control" and "needs data" item on a critical task. Each stops for the risk owner the person names ("owner not named" if none). Propose design controls only as "proposed", in FDA's order of preference, with the row.

## Build the output

Follow `assets/use-error-output.md`. Answer first: the critical tasks as the person marked them, any with no control or a training-only control, and the one decision needed. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every severity and every "critical" mark is the person's, and the output says so.
- Every control has a type; training-only and labeling-only controls on critical tasks say "needs data".
- Open gaps are listed, not closed.
- Field events are described only by their records, with the sorting labeled as yours; no inference about another product.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Use-related risk at the interface. The full risk management file (ISO 14971) belongs to the Quality pack (design-controls-and-risk-management).
- Whether a control was effective with users is usability-monitoring.
- No device classification, no HF Submission Category: dh-regulatory-strategy.
