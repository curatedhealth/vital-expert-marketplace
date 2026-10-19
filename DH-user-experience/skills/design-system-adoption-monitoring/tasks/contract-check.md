# A2 Contract check

Framework task: DH-02.04.2.2, Part A, task A2. Replaces the register task "Contract check" (CF-12.02.04.2.2.1).

## What this task delivers

A check of one live surface (a screen or flow in a product) against the contract of a component it uses: the version on the surface, each state and criterion in the contract, the evidence for each (seen, described, none), and the breaches found, stated as facts. It answers "does this surface still match the component contract?"

Why it matters: a component can be on the current version and still breach its contract on a surface: a state overridden, a token changed, clinical content placed where the contract forbids it. The register rule: do not pass a surface because it looks similar. USWDS expects teams to test components in context (DSX-38), and the presence of the system's code does not show the implementation is usable or accessible (DSX-41).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | UX/UI Designer, Digital Health (`ux-ui-designer-digital-health`) |
| Skill | DH-02.04.2.2 Part A, Contract check |
| Workflow | The steps below |
| Knowledge | The component contract (from the development skill or the person's own); `references/component-requirements.md`; `references/design-system-additions.md` |
| Tools | None from the library. `verify.build_record` only for sign-off |
| Prompt | This guide |
| Template | `assets/contract-check-output.md` |
| Input | The request and its context: the contract, the surface (screenshot, recording, markup, test results or a description), the version in use, whether the surface is clinical or a device user interface |
| Governance | `references/governance.md`; breaches are facts; no conformance statement; clinical content and device conclusions stop |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. |

## Read the request

- **Contract.** The contract for the component: states, criteria, never-invent content, allowed surfaces. If none exists, say so and offer to draft one with the development skill; without a contract, check only against the criteria for the component type in `component-requirements.md` section 2 and say which.
- **Surface.** What the person can show: screenshots, a recording, markup, test output. If you cannot view images or run the product, ask for a paste or a description, and mark every item checked that way "described, not seen".
- **Version.** The component version on the surface, from the inventory or the person.
- **Surface type.** Clinical task, patient-facing, marketing, device user interface (per the person's regulatory owner).
- **Mode.** Short for a direct question; full for a check record.

## Workflow

### Step 1. Fix the frame

Write back: component, contract version or "no contract: type criteria only", surface, component version on it, surface type. Confirm.

### Step 2. Allowed surface

Is the surface among those the contract allows? A clinical task using a component the contract limits to marketing, or a marketing page using a component that generates clinical content, is a breach (register rule).

### Step 3. States

For each state in the contract: present on the surface, altered (how), missing, or not checkable from what was supplied.

### Step 4. Criteria

For each criterion in the contract: what was observed, the evidence (seen with date, described, none), and the result as a fact ("stepper buttons measure below 24 by 24 CSS pixels in the supplied markup, with no exception documented; the contract requires 24 by 24 or a documented exception (UX-STD-11)"). Never measure from memory or estimate a pixel size or contrast ratio from a description; without a measurement the item is "not checked". A result from an automated tool is one of three kinds of evidence (UX-UK-24) and is labeled with the tool the person named.

### Step 5. Never-invent content

Check whether the surface shows content the contract forbids the component to generate (doses, clinical claims, results). Report what is shown and where it comes from, as the person describes it. Do not judge whether clinical content is correct; it stops for its owner.

### Step 6. Breaches and concerns

List breaches as facts, each with the contract item, the row and the evidence. For a contract item with no reference row, the row column reads "your contract", never a VITAL or method label. If the person classifies accessibility concerns as GOV.UK does, record theoretical or evidenced (DSX-44) with the evidence type (DSX-46); otherwise skip. No severity unless the person's scheme sets it (GOV.UK's three-factor test, DSX-45, is an option).

### Step 7. Device user interface

If the person says the surface is part of a device user interface, list as questions for their regulatory and quality owners, without answering them: is the fix recorded as a design change (CH9), assessed for risk and impact before implementation (QS34), is it a change to the user interface under Decision Point B (UX-US-49), and does it touch a critical task (UX-US-28)? Release of the fixed version stops for them (dh-regulatory-strategy, dh-quality).

## Build the output

Follow `assets/contract-check-output.md`. Answer first: breach or no breach found on what was checked, the one or two breaches that matter most (clinical and device first), and what was not checkable. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every contract item has a status: met on evidence seen, breach, described not seen, or not checked.
- "No breach found" is limited to what was checked and says so; it is never "passes" or "conformant".
- No measurement invented; no pass on similarity.
- No conclusion on clinical content or on use error.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- One surface against one contract; not an accessibility audit of a product (DH-02.04.1.x) and not a usability evaluation (DH-02.04.4.x).
- Whether the contract or the surface changes, and who fixes it, is B1.
