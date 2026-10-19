# A2 Control and field-signal check

Framework task: DH-02.04.4.2, Part A, task A2. Replaces the earlier "Control check" section.

## What this task delivers

Two checks. First, for each risk control in the use-error analysis (identity, units, timestamp and the rest), whether it is present in the build version the person names, of which type as designed and as shipped, and on what evidence. Second, what field signals show after release: decision support feedback exports, usage against the expected profile, pilot-site statements, the deploying site's SAFER self-assessment, and comparable recalls and MHRA alerts from the library, described by their records. It answers "is the control really in the build, and what is the field telling us?"

Why it matters: the old register rule holds: a screen does not pass because the mock-up had the control. FDA does not accept labeling or training as the fix for critical-task errors without data (UX-US-42), so a control that slid from design to a training note between mock-up and build is a change worth seeing.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Service Design Director (`service-design-director`) |
| Skill | DH-02.04.4.2 Part A, Control and field-signal check |
| Workflow | The steps below |
| Knowledge | `references/controls-and-field-signals.md`; `references/tools.md`; `references/implementation-research.md` |
| Tools | `regulatory-dh.list_jurisdictions` (free); `regulatory-dh.search_safety_events` (counted); `verify.build_record` for sign-off |
| Prompt | This guide |
| Template | `assets/control-and-field-output.md` |
| Input | The request and its context: the control list (design skill A2 or the person's), the build version and evidence, field data the person has, the product type and comparables they name |
| Governance | `references/governance.md`; field events are prompts, never findings about other products |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. The post-market-watch job also reads safety events but sets a watch; it is not called. |

## The rule that shapes this task: check the build; describe events only by their records

A control is "present" only on evidence from the named build (screenshot, build note, test record), seen or described by the person. Field events from other products are described by what their records state and used as prompts. Absence of events is not evidence of safety.

## Read the request

- **Controls.** From the design skill's A2 or the person's list, with the use error each answers and its designed type.
- **Build.** The version shipped or about to ship. Without it: "build not named `[GAP]`"; nothing is marked present.
- **Evidence per control.** What the person can show or describe.
- **Field data.** DSI feedback export (if certified health IT), usage against the profile agreed at commissioning, pilot-site statements, complaints the person chooses to summarize (aggregates only).
- **Comparables.** Product type words, comparable product or manufacturer names, markets, the period ("since" date) the person chooses.
- **Mode.** Short or full.

## Workflow

### Step 1. Fix the frame

Write back: build version, controls in scope, markets, period for field signals. Confirm.

### Step 2. Control-by-control check

For each control: the use error it answers; type as designed and as shipped (design, protective measure, information for safety; UX-US-33); status: present (seen), present (described, not seen), missing, changed type; evidence and its date. A control missing from the build is a miss, whatever the mock-up showed. A design control replaced by a label or training is "changed type" and, on a critical task, "needs data" (UX-US-42, CS79). Controls outside the screen count: labeling, training materials, alarms (UX-US-31). For lay-use screens that show a result, check the valid-result warning (UX-EU-19). If the training customers receive differs from the training used in validation, note it (CS80).

### Step 3. Field signals the person holds

Summarize, with dates and denominators as the person gives them:
- DSI feedback (intervention, action, feedback, user, date, location) where the product is certified health IT (UX-US-55);
- usage against the expected usage profile agreed at commissioning, and any agreed performance-change reporting (NICE ESF Standard 16, CS61, CS62);
- pilot-site statements on use as expected (CS59);
- the deploying site's SAFER Guide self-assessment, as the site's own (CS72 to CS74).
No threshold is applied unless the person sets one.

### Step 4. Comparable field events from the library

Call `regulatory-dh.list_jurisdictions` once (free). On 19 October 2026 the library held US 892, UK 10, EU 0 and CH 0 safety events; say so for EU or Swiss products. Then, for the comparables the person accepts:

- `regulatory-dh.search_safety_events {product: "<type word>", jurisdiction: "US", since: "<person's date>", limit: 10}`
- `regulatory-dh.search_safety_events {manufacturer: "<named comparable>", limit: 10}`
- `regulatory-dh.search_safety_events {product: "software", jurisdiction: "UK", limit: 10}` for MHRA alerts

Record what the filter could and could not do for this query (`references/tools.md`): no use-error filter (a "use error" query returned nothing), product words match text not cause, US rows cite the API not the recall, event date basis unstated, one recall may return as several rows, MAUDE blocks attached without a reason are reports, not confirmed events. Read every summary; keep those describing the interface or user interaction, and say the sorting is yours. For each kept event: product as stated, event date, class or alert type, the summary's own words, and the prompt for this product ("check comma decimal entry on all dose fields", after the Omnipod 5 iOS App recall of 23 May 2025). Never state that another product had a use error or a design flaw.

### Step 5. Findings

Facts only: "Units label on the dose field: in the mock-up, missing in the named build (screenshot dated by the person)" (illustrative wording). "Patient banner: changed type from design to a training note; critical task T1; needs data". Field findings with counts and dates.

## Build the output

Follow `assets/control-and-field-output.md`. Answer first: controls missing or changed type on critical tasks, then the one field signal that matters most. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every "present" has evidence from the named build; seen and described are kept apart.
- Every changed-type or missing control on a critical task is listed.
- Library calls are listed with arguments; events are described by their records; the sorting is labeled; no inference about other products.
- No threshold applied that the person did not set.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Vigilance reporting, complaint handling and CAPA belong to the Quality pack (audit-capa-and-complaints) and the person's quality owner.
- Whether a field signal is reportable to a regulator is the regulatory owner's.
- Software release verification belongs to the Software Engineering pack (DH-04.03).
