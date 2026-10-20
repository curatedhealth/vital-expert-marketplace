# A2 Increment and gate evidence plan

Framework task: DH-01.01.1.1, Part A, task A2. Replaces the earlier "Development increment" section (DH-01.01.1.1.2).

## What this task delivers

The increment the team will finish in this stage (user, task, build that contains it), what is outside it, who accepts it (as the person names), and, for each upcoming gate, the evidence elements a source names, mapped to the work product that would show each one and whether the person holds it. The result is a plan the gate can later be read against (B1).

Why it matters: an increment that carries a clinical claim not in the evidence plan (the old rule) creates evidence debt at the next gate. The sources name what a design review checks (PL4), what validation means (PL22) and what a clinical evaluation contains (PL63 to PL65), so the plan can be written before the gate rather than argued at it.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Product Manager (`digital-health-product-manager`) |
| Skill | DH-01.01.1.1 Part A, Increment and gate evidence plan |
| Workflow | The steps below |
| Knowledge | `references/gate-evidence-rules.md`; `references/lifecycle-stages.md` section 3; rows PL1 to PL10, PL15 to PL29, PL39 to PL42, PL62 to PL76, PL79 to PL93, PL97 to PL99 [WF], TM11 to TM15, CH9, CH11 (DOI 10.1136/bmj.n2061) |
| Tools | None by default. If a gate rests on published evidence: route to `dh-clinical-development` literature-and-real-world-evidence-review; for a single named source, `verify.qualify_source` then `verify.check_claim` with the read passage |
| Prompt | This guide |
| Template | `assets/gate-evidence-plan-output.md` |
| Input | The request and its context: A1 output or the stage, the intended use, the increment in mind (users, tasks, build), clinical claims in play, markets and routes (US, EU, DiGA, NHS England), the gates ahead and the person's criteria if any, work products held |
| Governance | `references/governance.md`; the person sets the increment scope, the acceptor and the gate criteria |
| Catalogue job | none |

## Read the request

- **Increment.** Which user, which task, which build? Take the person's words. If the increment includes a clinical claim, which one, and is it in their evidence plan?
- **Gates ahead.** Name each gate as the person does (design review, feasibility exit, DiGA application, NHS procurement, Pre-Sub).
- **Routes and markets.** They decide which rows apply (PL79 to PL93 for DiGA; PL97 to PL99 for DTAC [WF]; PL39 to PL42 for a Pre-Sub).
- **Acceptor.** Who accepts the increment, in the person's words, or owner not named.

## Workflow

### Step 1. Write the increment

Three lines from the person's facts: user and task; build that contains it (version); who accepts it. Then the exclusions: what is outside the increment. Flag any clinical claim in the increment that the person's evidence plan does not contain (old rule: do not add a claim not in the evidence plan); the claim's evidence goes to `dh-clinical-development` study-protocol-and-endpoint-design.

### Step 2. Separate functions if the product has more than one

If the product mixes device functions with other functions, note that FDA recommends separating them in design and implementation and that early architecture decisions make this possible (PL26), and that impact assessments are a design validation record (PL25). Whether a function is a device function is a question for `dh-regulatory-and-quality` regulatory-pathway-and-classification.

### Step 3. For each gate, list the named elements

From `references/gate-evidence-rules.md` section 2, list the elements the sources name for that gate type, each with its row. Add the person's own criteria verbatim. Keep the two apart: "named by a source" and "set by you".

### Step 4. Map each element to a work product

For each element: the work product that would show it (from the person's documents, by id and version), present, missing or `[GAP]`, and who the person said supplies it (or owner not named). Elements that depend on another (verification before validation, PL21, PL22; definition statement before clinical evaluation, PL58, PL62) are ordered by dependency.

### Step 5. Attendees and independence

Write the attendees the person named for each gate. State PL1 (functions concerned with the stage) and that independence is a risk-proportionate choice to justify, not a QMSR rule (PL2, QS23, PL66, PL67). Never fill names or titles.

### Step 6. Route what this skill does not hold

Design control and risk file content to `dh-regulatory-and-quality` design-controls-and-risk-management; Pre-Sub wording to `dh-regulatory-and-quality` regulatory-pathway-and-classification and submission content to `dh-regulatory-and-quality` regulatory-submission-and-dossier; study design to `dh-clinical-development` study-protocol-and-endpoint-design; usability evidence to `dh-patient-and-user-experience` patient-and-clinician-user-research; a DiGA listing route to `dh-access-and-value` coverage-pathway-and-access-strategy. Every route names the pack and the skill.

## Build the output

Follow `assets/gate-evidence-plan-output.md`. Answer first: the increment in one line, the next gate, and the element most likely to be missing at it (the first missing item by dependency). Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Increment scope, exclusions and acceptor are the person's words.
- Source-named elements and the person's criteria are in separate columns.
- No element is called met because a status says "done".
- [WF] (DTAC) and draft (PDURS) rows are labeled.
- Each [PAPER] paper cited has its DOI once in prose, and beside its row id in every table.
- The record line is the last line of the answer body (any calls list follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Writing the design inputs, the SRS or the risk file: `dh-regulatory-and-quality` design-controls-and-risk-management.
- Whether a change after release needs a submission (CH9 to CH16): `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control.
- Algorithm and platform architecture: `dh-digital-therapeutic-design` (old pack), headings DH-01.06.1 Personalization Engine and DH-01.06.4 DTx Architecture.
