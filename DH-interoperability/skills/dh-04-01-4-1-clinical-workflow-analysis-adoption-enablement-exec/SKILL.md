---
name: dh-04-01-4-1-clinical-workflow-analysis-adoption-enablement-exec
description: "Only while the Digital Health Library connector is connected. Run one task in DH-04.01.4.1 Clinical Workflow Analysis & Adoption Enablement Execution. Use when the user asks for Current step observation, New exchange placement, Adoption measure. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-04.01.4.1 Clinical Workflow Analysis & Adoption Enablement Execution

Heading: DH-04.01.4 Clinical Workflow Enablement.
Core: DH-04.01 Clinical Integration & Interoperability.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-04.01.4.1.1 Current step observation

Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.01.4.1.1 Current step observation.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.01.4.1. The other skills under this competency do a different job.

### What it does
Watch the clinical step as it is done today, before designing the integration.

### Method
1. Name the step (order, result review, documentation, discharge).
2. Record the system the person uses and the data they retype.
3. Note who performs the step and how often.

### Do not
Do not describe the future workflow as if it were the current one.

### Output
A short observation: step, actor, system, data retyped.

A missing fact stays [GAP].

## DH-04.01.4.1.2 New exchange placement

Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.01.4.1.2 New exchange placement.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.01.4.1. The other skills under this competency do a different job.

### What it does
Place the FHIR exchange on that step and say what the person stops doing.

### Method
1. Name the screen or message that replaces the retyped data.
2. State the click or the reading that goes away.
3. If the exchange adds a step, say so.

### Do not
Do not claim time saved without naming the step that was removed.

### Output
A before-and-after of one step.

A missing fact stays [GAP].

## DH-04.01.4.1.3 Adoption measure

Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.01.4.1.3 Adoption measure.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.01.4.1. The other skills under this competency do a different job.

### What it does
Define what adoption means for that step.

### Method
1. Name the people who count as adopters (role, site).
2. Name the action that counts (the new screen used, the old retype stopped).
3. Set the period over which the action will be counted.

### Do not
Do not use a login as the adoption event.

### Output
One adoption definition: who, which action, over what period.

A missing fact stays [GAP].
