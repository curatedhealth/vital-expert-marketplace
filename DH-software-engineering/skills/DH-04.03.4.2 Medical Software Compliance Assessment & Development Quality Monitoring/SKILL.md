---
name: "DH-04.03.4.2 Medical Software Compliance Assessment & Development Quality Monitoring"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-04.03.4.2 Medical Software Compliance Assessment & Development Quality Monitoring. Use when the user asks for Class versus hazard check, Plan completeness, Release gate for the class. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-04.03.4.2 Medical Software Compliance Assessment & Development Quality Monitoring

Heading: DH-04.03.4 Medical Software Development.
Core: DH-04.03 Software Engineering Excellence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-04.03.4.2.1 Class versus hazard check

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.03.4.2.1 Class versus hazard check.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.03.4.2. The other skills under this competency do a different job.

### What it does
Check that the safety class still matches the hazard.

### Method
1. Read the current hazard and the class statement.
2. Flag a class A item that can influence a clinical action.
3. Flag a class that was never tied to a hazard.

### Do not
Do not confirm the class from the document title alone.

### Output
A class check against the hazard.

A missing fact stays [GAP].

## DH-04.03.4.2.2 Plan completeness

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.03.4.2.2 Plan completeness.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.03.4.2. The other skills under this competency do a different job.

### What it does
Score the plans the class requires.

### Method
1. Use the checklist from the process skill.
2. Open each plan marked present and confirm it names this product.
3. Count plans that are missing or that describe a different product.

### Do not
Do not score a template that has not been filled for this product.

### Output
A count of present, empty, and missing plans.

A missing fact stays [GAP].

## DH-04.03.4.2.3 Release gate for the class

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.03.4.2.3 Release gate for the class.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.03.4.2. The other skills under this competency do a different job.

### What it does
Decide whether this class can ship.

### Method
1. Block the release when a required plan is missing or a hazardous problem is open.
2. Allow the release only with a named acceptor when a gap is documentation rather than an open hazard.
3. Record the decision against the build id.

### Do not
Do not ship class C on an informal chat approval.

### Output
A gate decision: build id, block or accept, acceptor if any.

A missing fact stays [GAP].
