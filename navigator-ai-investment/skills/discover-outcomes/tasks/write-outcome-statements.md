# B Write the outcome statements

Framework task: 2.1 Outcome Discovery, Part B.

## What this task delivers

Each outcome on the longlist rewritten in the standard form, with its party, level, value dimension and the driver it contributes to, checked for solutions and duplicates and accepted by the person.

Why it matters: people can only score what they read the same way. An outcome that names a solution has already chosen the answer; an outcome with no object cannot be measured; an outcome with no party cannot be field-tested with the people it is for (method.md O2, O3, O4).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | AI Investment Decision Lead |
| Skill | 2.1 Outcome Discovery, Part B |
| Workflow | The steps below |
| Knowledge | `references/method.md` (O2 to O4, O6) |
| Tools | `scripts/outcome_statement_check.py statements` |
| Prompt | This guide |
| Template | `assets/outcome-statement-worksheet.md`; "Outcomes" section of the report |
| Input | The longlist from Part A |
| Governance | `references/governance.md` |

## Workflow

### Step 1. Rewrite each outcome in the standard form

| Part | What it holds | Example |
|---|---|---|
| Direction of change | One of: minimize, maximize, increase, reduce, eliminate, maintain | Reduce |
| Object of measurement | What would be counted or timed | the time from a clinician's question to an accurate medical answer |
| Context | Under what conditions | for unsolicited questions on marketed products in Europe |
| Party | For whom it must become true | clinicians |

Rules for the object: two strangers would recognize the same finished state; vague objects ("capability", "performance", "value", "excellence") are qualified until they could be counted. Avoid empty verbs (drive, transform, enable, leverage, optimize, enhance); use one of the six directions.

### Step 2. Check each statement

Run `scripts/outcome_statement_check.py statements` on the list. It flags: a missing part; a direction outside the six; solution words (AI, tool, platform, model, agent, system, automate, deploy, implement, vendor names the person listed); empty verbs; a missing party; a party that is a team doing the work rather than the one the outcome is for (a hint, not a verdict). Read each flag and fix the statement, or keep it and say why. The script never rewrites.

### Step 3. Tag level, dimension and driver

- **Level** (proposed, marked as such until the person accepts): strategic (enterprise, years), category (a family of outcomes for a function or department, months) or mission (one end-to-end piece of work, weeks). Name it in words.
- **Value dimension:** take it from the value driver the outcome contributes to, if the driver has one; otherwise write "not stated" rather than guess (financial, operational, clinical or scientific, risk, capability, strategic). One dimension per outcome; if an outcome seems to need two, it is usually two outcomes.
- **Driver:** "*[outcome]* contributes to *[driver]*".

### Step 4. Merge duplicates, split doubles

Two statements with the same object and party are one outcome. One statement with "and" joining two objects is two. Propose the merge or split; the person decides.

### Step 5. Show and confirm in one turn

Show the rewritten list (statement, party, driver) and ask one question: "Does each say what you mean?" Changes the person makes win. Mark accepted statements "accepted by [name]".

## Boundaries

- The rewrite keeps the person's meaning. If you are not sure what they meant, ask rather than guess.
- A restated solution goes to the options list, visible in the report. It is not dropped.
- Never add an outcome the person did not give or accept.

## When you are unsure

If an outcome cannot be written in the standard form after one attempt with the person, record it as "not yet an outcome" with the words they used. It does not go forward to scoring.
