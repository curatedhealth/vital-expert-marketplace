# A1 Clinical task and workflow fit

Framework task: DH-02.04.4.1, Part A, task A1. Replaces the earlier "Clinical task fit" and "Workflow placement" sections.

## What this task delivers

A task fit for one screen or feature: the task, the role, the setting and the moment in the workflow; the data the screen must show for that task and the data it withholds; the step it replaces (paper, another system, a phone call) and any step it adds, including training; where decision support and its feedback sit; and the deployment facts the site will check. When the person asks for the whole service rather than one screen, it adds a service blueprint (step 7). It answers "where does this screen sit in clinical work, and what does the clinician stop doing?"

Why it matters: fit with workflows is a construct of its own in implementation science (CS14), and FDA counts labeling, training and logic of operation as part of the user interface (UX-US-31). A screen designed from a generic dashboard has no task to be checked against, so its misreads (A2) and its test (usability-monitoring) have nothing to anchor on.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Service Design Director (`service-design-director`) |
| Skill | DH-02.04.4.1 Part A, Clinical task and workflow fit |
| Workflow | The steps below |
| Knowledge | `references/workflow-fit.md`; `references/implementation-research.md`; `references/ux-usability-research.md` |
| Tools | None from the library. `verify.build_record` only for sign-off |
| Prompt | This guide |
| Template | `assets/task-fit-output.md` |
| Input | The request and its context: the product and feature, intended users and settings, the person's description of current practice, screens or descriptions |
| Governance | `references/governance.md`; fit is described, never claimed as a time or outcome gain |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. |

## The rule that shapes this task: one real task, named

Every fit starts from a named task done by a named role at a named moment. Never design from a generic dashboard (old register rule). Never claim the screen saves time without naming the old step; even then, the saving is the person's measurement, not the model's estimate.

## Read the request

- **Task and role.** Which task, by whom (in the person's role names), where (ward, clinic, home, pharmacy), at which point (admission, round, order entry, discharge, between visits).
- **Users.** Professionals, lay users or both; adults, children or both. FDA treats each as distinct populations (UX-US-36); one fit per population if they differ.
- **Current practice.** The old step. If the person does not know it, it stays `[GAP]` and the before and after cannot be written.
- **Certified health IT?** If the product is or plugs into ONC-certified health IT with decision support, the DSI rows apply (UX-US-54, UX-US-55).
- **Market.** US, EU, UK. Rows differ by market.
- **Mode.** Short for a direct question; full for a design document.

## Workflow

### Step 1. Fix the frame

Write back in one table: task, role, setting, moment, users and population split, market, whether certified health IT is involved. Confirm before going on. Make the CFIR domains concrete if the person wants them: inner setting is the unit where the task happens, outer setting the system around it (CS11, CS12).

### Step 2. Data shown and data withheld

List the data the screen must show for the task, in the order the task needs it, and the data it withholds because it distracts or is not for this role. For decision support, use the CDS overload principle as the test: decision-relevant information first, more detail available on request (UX-US-70). Mark each item "shown", "on request" or "withheld", with the reason in the person's words. Ask which elements are core and which may vary by site (CS4).

### Step 3. Before and after

Write the old step, the screen that replaces it, and any step it adds. Include steps outside the screen that FDA counts as interface: labeling, training, alarms, logic of operation (UX-US-31). Training the step needs is part of the pathway description NICE asks for (CS58). If the old step is not named: "old step not named `[GAP]`", and no saving is stated.

### Step 4. Decision support placement and feedback

If the screen carries decision support: say where in the task the intervention appears. For certified health IT it must appear while the user interacts with the technology (UX-US-54), and users must be able to give feedback that is exported with intervention, action, feedback, user, date and location (UX-US-55); name where in the task that feedback would be given. If the task is time critical, note that FDA does not consider software for a critical, time-sensitive task to meet CDS Criterion 4 (UX-US-66) and route the device question to the regulatory owner; do not decide it.

### Step 5. Environment

Note what the setting does to the screen: mobile screen size, contrast, light and noise (MDR Annex I 17.3, UX-EU-16); display scales for the users and setting (UX-EU-15); lay skills and instructions for lay use (UX-EU-17). Facts only for the markets in scope.

### Step 6. What the deploying site will check

Name the deployment facts tied to the task, as facts about the site's own process, not as the manufacturer's duty:
- the SAFER Guide whose practices the task touches (for example Patient Identification, CPOE with Decision Support, Test Results Reporting and Follow-Up, Clinician Communication) (CS72, CS73; the CMS measure wording differs, CS74);
- silent-mode checking where the product adapts to local data (NICE ESF Standard 15, CS60);
- communication of outputs, features, benefits and limitations and the end-user training approach (NICE ESF Standard 20, CS65);
- in NHS England, DCB0160 for the deploying organization (CS70, CS71, both [WF]; clause content `[GAP]`).

### Step 7. Service blueprint (only when the person asks for the whole service)

Use this when the question is the care service around the product (for example "map the service from referral to follow-up", "who does what behind the screen"), not one screen. The layout is method, not a sourced rule: no source in `references/` prescribes a blueprint format, lane names or a number of steps. Never attach a number, threshold or legal statement to the layout itself.

Lanes, one row per step in the order the service runs, all in the person's words:
- **Patient steps:** what the patient does and where (home, clinic, app).
- **Clinician steps:** what each named role does, at which moment (from steps 1 and 3).
- **Back-stage steps:** what happens out of sight of patient and clinician (triage queue, data processing, review by another role, manufacturer support).
- **Handoffs:** each point where work passes between roles, systems or organizations, with who sends and who receives. Mark a handoff with no named receiver as `[GAP]`.
- **Data:** what data moves at each step and in which system. Where the person's product is assessed under NICE ESF (England), the company provides a deployment data flow map and data dictionary (Standard 19, CS64); use the person's map if they have one.
- **Support:** training and help each role needs at that step. Training needs belong in the pathway description (NICE ESF Standard 12, CS58) and the end-user training approach is described by the company (Standard 20, CS65). Any support level, response time or staffing figure is the person's; none is sourced.

Sourced facts to attach to steps, by market (name the jurisdiction when used elsewhere):
- US hospitals: mark the steps that touch a SAFER Guide practice area, for example Clinician Communication or Test Results Reporting and Follow-Up for handoffs, Contingency Planning for what happens when the system is down (CS72, CS73). Practice text is not extracted `[GAP]`.
- England: silent-mode checking as a step before use in care for products affected by local factors (CS60); DCB0160 for the deploying organization (CS70, CS71, [WF]).
- The NHS service manual rows in `references/` cover accessibility and the NHS design system only (UX-UK-08, UX-UK-21); no sourced service design rule from it `[GAP]`.

Fit (CS14) is recorded per step; whether the service will be adopted is never predicted from it (CS3). The blueprint feeds A2 (each handoff is a place to ask what a user could miss, as method) and the service pilot option in B1.

## Build the output

Follow `assets/task-fit-output.md`. Answer first: the task, role and moment in one line, the data shown first, and the step the screen replaces and adds. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- One named task, role, setting and moment per fit; one fit per distinct population.
- Every data item is shown, on request or withheld, with a reason.
- A blueprint, if built, is labeled "method, not a sourced rule"; every handoff has a named receiver or `[GAP]`; support figures are the person's.
- The old step is named or marked `[GAP]`; no time or outcome claim.
- Every rule carries a row id; [WF] rows say so.
- A row from a non-US or non-EU instrument (NICE, DTAC, DCB0160) names its jurisdiction when used for another market, or is replaced by UX-US-31 alone.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Task and workflow grain. Screen layouts and interaction specs stay with the person's UX designer.
- Use errors and controls are A2; option choice and the evaluation plan are B1; test results are usability-monitoring.
- A service blueprint here stays at design grain. Customer deployment plans, deployment pilots and training delivery belong to the Customer Success pack (DH-02.02, `customer-implementation-planning`); EHR integration build to the Interoperability pack (DH-04.01).
- Whether a function is a device stays with dh-regulatory-and-quality.
