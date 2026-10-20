# A1 Study plan

Framework task: DH-02.04.3.1, Part A, task A1. Replaces the earlier "Study question" section (CF-12.02.04.3.1.1).

## What this task delivers

A formative study plan: the decision the study serves, the research question, what the study will not answer, the kind of work (formative, with the boundary to validation stated), user groups and the number per group with the person's rationale, recruitment including people with access needs, methods and tasks, what the protocol must specify, known problems with similar products as proposed scenarios, and an ethics screen of facts for the person's reviewer. It answers "what will this study learn, from whom, and how?"

Why it matters: a study with no named decision produces insights nobody acts on, and a study that mixes formative and validation intent produces evidence neither side can use. FDA's formative results do not carry over to the final design (UXR-03), and validation has its own participant and method rules (UX-US-34 to UX-US-40).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Patient Experience Designer (`patient-experience-designer`) |
| Skill | DH-02.04.3.1 Part A, Study plan |
| Workflow | The steps below |
| Knowledge | `references/formative-and-validation.md`; `references/participants-and-ethics.md`; rows UX-US-29 to UX-US-45, UX-M-01 to UX-M-19, UX-UK-17 to UX-UK-19, UX-UK-25, UXR-01 to UXR-06, PE-04 to PE-09 |
| Tool | `regulatory-dh.search_safety_events` (counted, optional, step 4); `verify.build_record` for sign-off |
| Prompt | This guide |
| Template | `assets/study-plan-output.md` |
| Input | The request and its context: product and design state, the decision, user groups, markets, constraints, the person's sample-size rationale, any critical-task list from their owner |
| Governance | `references/governance.md`; formative only; validation, ethics determinations and critical-task lists are the owner's |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. The post-market-watch job also reads safety events but sets a watch; it is not called. |

## Read the request

- **Decision.** What will change depending on the result (a design choice, a go or no-go on a feature, a content rewrite)? Without it, ask; do not plan.
- **Kind of work.** Words like "summative", "validation", "for the 510(k)", "for the usability file" mean the request crosses the boundary. Say so in the first line of the answer.
- **Design state.** Concept, prototype, beta, released. Formative work fits a design in progress (UX-US-29).
- **User groups.** Patients, caregivers, clinicians (which kind), pediatric or adult. Each is a separate group (UX-US-36).
- **Markets.** The US and Great Britain rows differ (FDA vs MHRA); EU ethics rules are a gap.
- **Constraints the person names.** Budget, recruiting channel, remote or in person.
- **Mode.** Short for a direct question ("how many nurses do we need?"); full for a protocol draft.

## Workflow

### Step 1. Fix the decision and the question

Write back: the decision, the research question in one sentence, the participant (patient, caregiver or clinician) and the task, and what the study will not answer (register method). If the person proposes clinicians for a patient task or the reverse, say so (register "Do not").

### Step 2. Name the kind of work

State "formative user research" and the boundary in one line: results inform design changes and do not demonstrate safe and effective use of the final design (UXR-03). If the request is validation, stop here for the protocol: list the validation design facts as a draft for the owner (UX-US-34 to UX-US-41: representative users, all critical tasks, final UI, realistic conditions, 15 per distinct group, residence, no employees, no think-aloud, training delay) and point to `dh-regulatory-and-quality`.

### Step 3. Participants and numbers

For each user group, record the number the person sets and their rationale. Lay out, as context only: formative sizes vary with the information need (UX-M-04); FDA's restatement of Faulkner (UX-M-01, UX-M-02) with its caveat; FDA's statement that no formula gives a correct size (UX-M-03); MHRA's "document the rationale" (UX-UK-17); saturation has no set criteria (PE-09). If the person quotes 15 per group as a formative target, say it is FDA's validation minimum (UX-US-35) and leave the choice to them.

Recruitment points: people with condition-related limitations (UX-US-37); NHS guidance of 1 in 5 participants with access needs (UX-UK-25, guidance not law); employees allowed with caution in formative work (UX-US-45); sampling choice affects how far results reflect the target population (PE-06).

### Step 4. Known problems with similar products (optional)

If the product has a similar marketed product or category, call `regulatory-dh.search_safety_events` once with one short product term or the manufacturer, `jurisdiction` the person's market, `since` a date the person accepts, `limit` 5 to 10. Example measured call: `{product: "insulin", jurisdiction: "US", since: "2025-01-01", limit: 5}`. For each relevant record, quote its summary and propose a scenario to include, labeled "proposed" (UXR-01). Never call a recall a use error, and never read "no events" as safety. Skip this step if the person declines library calls.

### Step 5. Methods, tasks and protocol elements

Choose methods with the person: contextual inquiry (UXR-04), interviews or focus groups (UXR-05), cognitive walk-through with think-aloud (UX-M-05), task sessions on a prototype. Write the seven formative protocol elements (UXR-02): purpose and priorities; the part of the UI assessed (including labeling and training material where relevant, UX-US-31); scenarios and tasks; participants; data collection; analysis; how results will be used (the decision from Step 1). Mark tasks the person's owner flags as critical; never add the flag yourself (UX-US-28).

**Remote or unmoderated sessions.** If the person plans remote (moderated by video) or unmoderated (self-run by the participant) sessions, record the session mode per method and lay out only what the sources hold:
- The FDA human factors rows in `references/` do not address remote or unmoderated sessions as such `[GAP]`. What they do say: formative evaluation can vary in formality with the information need and the conditions of use (UX-M-04); contextual inquiry observes users in the actual use environment (UXR-04); for EU mobile software, screen size, contrast, light and noise matter (UX-EU-16), so a remote session on the participant's own device and setting can show these, as a design note rather than a rule.
- Consent and recording for remote sessions: MHRA expects informed consent where practicable even in formative work, for Great Britain (UX-UK-19); exemption (d)(3) under the Common Rule covers recorded responses only where the subject agrees in advance and the other conditions hold (UX-M-15). Rules specific to remote consent, screen or video recording, recording storage and cross-border transfer are not in this skill's sources `[GAP]`; they are the person's IRB, ethics committee or privacy owner's.
- Whether a remote or unmoderated session meets the validation condition "sufficiently realistic to represent actual conditions of use" (UX-US-34) is not decided here. Summative validation conditions stay with the regulatory owner (`dh-regulatory-and-quality`).

### Step 6. Ethics screen

Lay out the facts from `references/participants-and-ethics.md` that the person's situation touches: whether the Common Rule applies (UX-M-11), the research definition (UX-M-12), exemption (d)(2) and its three criteria (UX-M-14, UXR-06), (d)(3) for benign tasks with adults (UX-M-15 to UX-M-17), children (UX-M-18), MHRA consent in formative work for Great Britain (UX-UK-19). End with "Determination: your IRB, ethics committee or named reviewer". Never state that the study is exempt. For a US device company, name FDA's IRB rules (21 CFR 50 and 56) as a question for the reviewer, not read in this build `[GAP]`. Payment to participants who may be program beneficiaries: the owner the person names for this `[GAP]`.

### Step 7. Data handling

State that analysis files use pseudonymous codes and that `scripts/research_log.py` refuses identifiable columns. Recordings stay with the person's research operations.

## Build the output

Follow `assets/study-plan-output.md`. Answer first: the decision, the kind of work, groups and numbers (the person's), and the one open point that blocks the plan. Short mode: 450 words maximum, counted without the calls list and tables' source column. Every other table cell counts. Before handing over, count the words of the answer above "Calls made" (for example with `wc -w`) and state nothing over 450. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- The decision is named, and the plan says what it will not answer.
- Formative and validation are not mixed; any validation content is labeled "draft for the owner".
- Every number per group is the person's, with their rationale, and groups are not pooled.
- No critical-task flag, ethics determination or sample-size rule from the model.
- Library events are quoted from their records and labeled "proposed" scenarios.
- No identifiable participant data requested or kept.
- Remote or unmoderated sessions: session mode stated; consent and recording rules not sourced are `[GAP]`; no statement that a remote session suits validation.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Human factors validation, HF Submission Categories and submission content: `dh-regulatory-and-quality`.
- Clinical workflow design and usability monitoring of a released product: UX 4.x (`clinical-workflow-ux-design`, `usability-monitoring`).
- Patients as co-design partners or advisory panels: `patient-research-and-co-design`. Who is reached and left out: Patient Engagement 4.x. Accessibility conformance: UX 1.x.
- Behavioral frameworks for engagement or behavior change: `dh-digital-therapeutic-design`. This task studies how users do tasks; it does not design the behavioral mechanism.
- PRO, COA or preference studies under the PFDD series: the clinical or regulatory owner (PE-01 to PE-27).
