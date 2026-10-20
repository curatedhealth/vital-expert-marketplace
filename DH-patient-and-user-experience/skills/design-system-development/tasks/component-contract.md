# A1 Component contract

Framework task: DH-02.04.2.1, Part A, task A1. Replaces the register task "Component contract" (CF-12.02.04.2.1.1).

## What this task delivers

The contract for one component: what it is for, the states it supports, the accessibility criteria it must meet with their sources, the evidence that shows it meets them, the content it must never invent, the product surfaces allowed to use it, and, if it sits in a medical device user interface, the device rows that apply. It answers "what must this component do, meet and never show, and where may it be used?"

Why it matters: a component is reused across products, so a defect or an omission repeats everywhere it is used. Accessible components do not make a product accessible (UX-UK-28, UX-US-78), but a component without stated criteria and evidence passes its gaps to every product that uses it.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | UX/UI Designer, Digital Health (`ux-ui-designer-digital-health`) |
| Skill | DH-02.04.2.1 Part A, Component contract |
| Workflow | The steps below |
| Knowledge | `references/component-requirements.md`; `references/design-system-additions.md`; `references/UX_ACCESSIBILITY_USABILITY.md` |
| Tools | None from the library. `verify.build_record` only for sign-off |
| Prompt | This guide |
| Template | `assets/component-contract-output.md` |
| Input | The request and its context: the component and its purpose, the states the person's screens show, the products and surfaces that use or will use it, the accessibility target the person has chosen, whether any surface is clinical or part of a medical device, test evidence they hold |
| Governance | `references/governance.md`; contract and criteria lists may proceed as drafts; clinical content and any conformance statement stop |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. |

## Read the request

- **Component.** Its name and purpose in the person's words, and its type (button, form input, slider, status message, and so on), which decides the criteria in `component-requirements.md` section 2.
- **States.** The states their screens show. Ask for error, disabled, loading, empty and any unsafe-to-proceed state if the person has not said whether they exist; never assume one exists.
- **Surfaces.** Which products and screens use it, and which are clinical tasks, patient-facing, marketing, or part of a medical device per their regulatory owner.
- **Target.** The WCAG version and level they have chosen. If none, lay out section 1 of `component-requirements.md` and ask. If they give a reason for the target (Section 504, Section 508, NHS, a buyer), state in one line what that instrument cites and from when, with its rows from section 1, and the instrument that moved any date (for Section 504: WCAG 2.1 A and AA from 11 May 2027, or 10 May 2028 under 15 employees, dates moved by an HHS interim final rule effective 7 May 2026, UX-US-16 to UX-US-18).
- **Evidence.** Test results they hold (automated, manual, with people), with dates.
- **Mode.** Short for a direct question; full for a contract document.

## Workflow

### Step 1. Fix the frame

Write back: component, type, purpose, surfaces (with clinical and device flags as the person gave them), target ("your target: WCAG 2.2 AA" or "target not chosen"). Confirm before writing the contract.

### Step 2. States

List the states the person named. For each, record what the component shows and what it must do. Where a state is needed by a criterion (for example an error state for Error Identification, UX-STD-19, or a visible focus state, DSX-04), say so and ask whether it exists.

### Step 3. Accessibility criteria

From `component-requirements.md` section 2, list the criteria that apply to the component type, each with level and row. Filter by the person's target: under WCAG 2.1, the six new 2.2 A and AA criteria (UX-STD-07) are listed as "beyond your target, required by NHS and GOV.UK (UX-UK-08, UX-UK-23)". Criteria the type needs but the rows do not quote are `[GAP]`. Do not add criteria from memory.

Write each criterion as a testable line in the person's terms, for example "Every tappable area at least 24 by 24 CSS pixels, or one of the five exceptions documented (UX-STD-11)". Never write the result of a test the person has not shown.

### Step 4. Evidence required

For each criterion, name the evidence that would show it is met, using section 3 of `component-requirements.md`: automated scan, manual test (keyboard, screen reader, zoom, touch, browsers; DSX-37), testing with people including disabled people (UX-UK-30). Record the person's evidence as seen (what, date), described, or none. Say once that component tests are evidence toward page conformance, not a conformance claim (UX-STD-21, UX-STD-22).

### Step 5. Content the component must never invent

Apply the register rule: name the content the component must not generate or alter, for example clinical claims, doses, results, risk scores. If the component displays clinical content, record where that content comes from and who owns it. A marketing surface and a clinical task do not share a component that generates clinical content. If the person wants NHS's "clinically safe" criterion (DSX-18), record the clinician involvement they describe; do not assess clinical safety.

### Step 6. Allowed surfaces

List the surfaces allowed to use the component and any excluded, in the person's words. Flag surfaces marked clinical or device.

### Step 7. Device user interface (only if the person's regulatory owner says a surface is a device)

Add the rows from `component-requirements.md` section 5 that bear on this component type: display scales (UX-EU-15), mobile screen size and contrast (UX-EU-16), lay-use error and invalid-result warning (UX-EU-18, UX-EU-19), user interface including labeling and training (UX-US-31). Ask whether any critical task (UX-US-28) uses the component; the answer comes from the person's use-related risk analysis, not from the model. Record that changes to this component follow the person's change control (A2).

### Step 8. Lifecycle status

If the person has a lifecycle scheme, record the status they assign. If not, show GOV.UK's and USWDS's schemes as options (`governance-models.md` section 3) and leave the status blank.

## Build the output

Follow `assets/component-contract-output.md`. Answer first: the component, its target, the criteria with no evidence yet, and the content it must never invent. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every criterion has a row id or is marked `[GAP]`; criterion numbers match DSX-50 or UX-STD-07.
- Every evidence line says seen, described or none.
- No statement that the component, or any product using it, is accessible, conformant or compliant.
- No clinical, dose or patient-facing wording written by the model; any such content is marked "stops for the owner".
- Owners are the person's words or "owner not named".
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- A contract draft, not a conformance assessment of a product (dh-patient-and-user-experience Accessibility & Inclusion) and not a usability study.
- Whether a surface is a medical device belongs to dh-regulatory-and-quality.
- Who is reached and who is left out (equity) belongs to dh-patient-and-user-experience Health Equity, which points here for component conformance criteria.
- Changes to the component are A2; adoption and governance are B1; measuring use on live products is the monitoring skill.
