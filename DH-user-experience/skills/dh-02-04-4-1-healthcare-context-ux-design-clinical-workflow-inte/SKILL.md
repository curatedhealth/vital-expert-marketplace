---
name: dh-02-04-4-1-healthcare-context-ux-design-clinical-workflow-inte
description: "Only while the Digital Health Library connector is connected. Run one task in DH-02.04.4.1 Healthcare Context UX Design & Clinical Workflow Integration. Use when the user asks for Clinical task fit, Workflow placement, Safety of the screen. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.04.4.1 Healthcare Context UX Design & Clinical Workflow Integration

Heading: DH-02.04.4 Healthcare UX Design.
Core: DH-02.04 User Experience Excellence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-02.04.4.1.1 Clinical task fit

Worker: Service Design Director (`service-design-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.04.4.1.1 Clinical task fit.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.04.4.1. The other skills under this competency do a different job.

### What it does
Place the interface on a real clinical task.

### Method
1. Name the task, the role, and the point in the workflow.
2. Name the data the screen must show for that task.
3. Name the data it must not show, because it distracts or it is not for this role.

### Do not
Do not design the screen from a generic dashboard.

### Output
A task fit: role, data shown, data withheld.

A missing fact stays [GAP].

## DH-02.04.4.1.2 Workflow placement

Worker: Service Design Director (`service-design-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.04.4.1.2 Workflow placement.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.04.4.1. The other skills under this competency do a different job.

### What it does
Say what the clinician stops doing.

### Method
1. Name the old step (paper, another system, a phone call).
2. Name the screen that replaces it.
3. Name the step this screen adds, if it adds one.

### Do not
Do not claim the screen saves time without naming the old step.

### Output
A before and after of one task.

A missing fact stays [GAP].

## DH-02.04.4.1.3 Safety of the screen

Worker: Service Design Director (`service-design-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.04.4.1.3 Safety of the screen.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.04.4.1. The other skills under this competency do a different job.

### What it does
Name the clinical mistake the screen could cause.

### Method
1. Name the misread (wrong patient, wrong dose, stale result).
2. Name the control on the screen (identity, units, timestamp).
3. Mark a misread you have no control for as [GAP].

### Do not
Do not ship a task screen with an open misread gap.

### Output
A misread and a control, or a gap.

A missing fact stays [GAP].
