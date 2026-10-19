# A1 Result definitions

Framework task: DH-02.03.2.2, Part A, task A1. Replaces the earlier "Engagement result definition" section (CF-12.02.03.2.2.1).

## What this task delivers

One result definition per activity: the action named in the program's purpose, the period, the record that proves it, the denominator, and, where a questionnaire or scale is used, the measurement properties the sources ask for. It also names what the definition cannot show. It answers "what counts as this activity working, and how will we know?"

Why it matters: engagement has a behavioral and an experiential side (PE-105), "effective engagement" means enough to achieve the intended outcome rather than more (PE-104), and attrition comes in two kinds that must be reported apart (PE-102). Counting attendance or followers when the purpose was an action measures the wrong thing.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Marketing Manager (`digital-marketing-manager`) |
| Skill | DH-02.03.2.2 Part A, Result definitions |
| Workflow | The steps below |
| Knowledge | `references/result-definitions.md` |
| Tools | None from the library. `verify.build_record` only for sign-off |
| Prompt | This guide |
| Template | `assets/result-definitions-output.md` |
| Input | The request and its context: the program purpose (audience, action asked), the activities, the records the person holds, any questionnaire they use, the period |
| Governance | `references/governance.md`; definitions and targets are the person's |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. |

## Read the request

- **Purpose.** The action asked, from the design skill (DH-02.03.2.1 A1) or the person. Without it, ask; a result cannot be defined without the action.
- **Activities.** The list.
- **Records.** Which systems or logs hold evidence of the action (booking export, completion log, survey).
- **Denominator.** Ask who the denominator is: everyone reached, or only those for whom the action was due when they joined (for example, due for screening), and whether a baseline is recorded at joining.
- **Questionnaire.** If the result is a score (activation, a PROM), its name and what the person knows of its properties.
- **Mode.** Short for a direct question; full for a measurement plan.

## Workflow

### Step 1. One action per activity

For each activity write the action from the purpose that the activity is meant to produce. Apply the kept rule: the action, not attendance or follower counts. If the person proposes a reach or follower measure, keep it as "reach (context)" and write the action beside it.

### Step 2. Period, record, denominator

For each definition: the period (the person's), the record that proves the action, and the denominator (reached, enrolled, eligible) stated plainly. If no record exists, write "no record: the activity will be unscored" and ask whether one can be created.

### Step 3. Usage and attrition, if the program is digital

Write the usage measure in the person's terms (for example "opened a session") and say that dropout and nonusage attrition will be reported separately, with a curve and a usage half-life (PE-102, PE-103). The as-of date is the person's.

### Step 4. Questionnaire properties, if a score is used

From section 3 of the reference, list the properties to check: content validity first (PE-93), reliability and internal consistency at 0.70 (PE-95), structural validity and measurement error criteria (PE-96). State that these are the source's criteria for the instrument, not targets for the program. PAM level cut points are `[GAP]`.

### Step 5. What the definition cannot show

One line each, from the rows: participants are rarely a probability sample (PE-06); engagement is not clinical benefit (governance); who was not reached is Patient Engagement 4.x. If the program reports patient involvement, point to GRIPP2 short or long form (PE-90, PE-91).

### Step 6. Targets

Ask for a target per definition. If the person gives one, record it as theirs. If not, write "no target set". Never propose a number.

## Build the output

Follow `assets/result-definitions-output.md`. Answer first: the definitions in one table and the activities that cannot be scored for lack of a record. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every definition names an action, a period, a record and a denominator, or says which is missing.
- No target, benchmark or threshold appears that the person did not give; questionnaire thresholds are labeled as instrument criteria.
- No definition is described as evidence of clinical benefit.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Definitions for program and partnership results. Product KPI frameworks across the pack are Patient Engagement 3.x.
- Clinical outcome measurement for evidence is dh-clinical-validation.
