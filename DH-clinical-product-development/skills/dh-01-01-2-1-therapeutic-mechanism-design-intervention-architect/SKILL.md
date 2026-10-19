---
name: dh-01-01-2-1-therapeutic-mechanism-design-intervention-architect
description: "Only while the Digital Health Library connector is connected. Run one task in DH-01.01.2.1 Therapeutic Mechanism Design & Intervention Architecture. Use when the user asks for Mechanism statement, Intervention component, Mechanism assumption. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.01.2.1 Therapeutic Mechanism Design & Intervention Architecture

Heading: DH-01.01.2 Therapeutic Design.
Core: DH-01.01 Clinical Product Development.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-01.01.2.1.1 Mechanism statement

Worker: Clinical Validation Director (`clinical-validation-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.01.2.1.1 Mechanism statement.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.01.2.1. The other skills under this competency do a different job.

### What it does
Write how the intervention is supposed to change the outcome.

### Method
1. Name the user action, the body or behavior change, and the outcome.
2. Name the population the mechanism is for.
3. Name a population it is not for.

### Do not
Do not describe the mechanism as the feature list.

### Output
A mechanism: action, change, outcome, population, exclusion.

A missing fact stays [GAP].

## DH-01.01.2.1.2 Intervention component

Worker: Clinical Validation Director (`clinical-validation-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.01.2.1.2 Intervention component.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.01.2.1. The other skills under this competency do a different job.

### What it does
Name the component that delivers that mechanism.

### Method
1. Name the component (content, sensor, clinician step, drug-device combination).
2. Tie it to one link in the mechanism.
3. Name a component that does not serve the mechanism and will not ship in this version.

### Do not
Do not add a component you cannot tie to the mechanism.

### Output
A component tied to one link, and a component left out.

A missing fact stays [GAP].

## DH-01.01.2.1.3 Mechanism assumption

Worker: Clinical Validation Director (`clinical-validation-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.01.01.2.1.3 Mechanism assumption.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.01.01.2.1. The other skills under this competency do a different job.

### What it does
Write the assumption that, if wrong, stops the intervention.

### Method
1. Name the assumption.
2. Name the study or the signal that would show it is wrong.
3. Name who stops the version if that signal appears.

### Do not
Do not leave the stopping rule unnamed.

### Output
An assumption, a signal, and a stopper.

A missing fact stays [GAP].
