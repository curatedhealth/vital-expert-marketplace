---
name: dh-04-03-2-1-verification-validation-execution-for-medical-softw
description: "Only while the Digital Health Library connector is connected. Run one task in DH-04.03.2.1 Verification & Validation Execution for Medical Software. Use when the user asks for Intended use and hazard, Verification case, Validation with a user. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-04.03.2.1 Verification & Validation Execution for Medical Software

Heading: DH-04.03.2 Quality Engineering.
Core: DH-04.03 Software Engineering Excellence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-04.03.2.1.1 Intended use and hazard

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.03.2.1.1 Intended use and hazard.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.03.2.1. The other skills under this competency do a different job.

### What it does
Write the intended use the verification must defend, and the hazard if the software is wrong.

### Method
1. State the intended use in one sentence, including who acts on the output.
2. Name the harm if the output is wrong or late.
3. Separate a wellness display from a function that drives a clinical action.

### Do not
Do not verify a feature that has no intended use.

### Output
An intended-use sentence and a hazard.

A missing fact stays [GAP].

## DH-04.03.2.1.2 Verification case

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.03.2.1.2 Verification case.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.03.2.1. The other skills under this competency do a different job.

### What it does
Write a case that shows the software meets a stated specification.

### Method
1. Point at the specification line.
2. State the input, the step, and the expected output.
3. Record the result against a named build.

### Do not
Do not write a case whose expected output is works correctly.

### Output
A case tied to a specification line and a build.

A missing fact stays [GAP].

## DH-04.03.2.1.3 Validation with a user

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.03.2.1.3 Validation with a user.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.03.2.1. The other skills under this competency do a different job.

### What it does
Check that a person in the intended role can complete the task.

### Method
1. Name the role and the task from the intended use.
2. Observe the person on a named build. Record where they misread the output.
3. File a validation miss separately from a specification miss.

### Do not
Do not use the author of the screen as the only participant.

### Output
A validation note: role, task, build, misreads.

A missing fact stays [GAP].
