---
name: "DH-03.02.1.2 Design Control Compliance Assessment & Risk Management Effectiveness Monitoring"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-03.02.1.2 Design Control Compliance Assessment & Risk Management Effectiveness Monitoring. Use when the user asks for Design control check, Trace score, Design control repair. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-03.02.1.2 Design Control Compliance Assessment & Risk Management Effectiveness Monitoring

Heading: DH-03.02.1 Design Controls & Risk Management.
Core: DH-03.02 Quality Management & Compliance.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-03.02.1.2.1 Design control check

Worker: Product Development Lead (`product-development-lead`). 4 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.02.1.2.1 Design control check.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.03.02.1.2. The other skills under this competency do a different job.

### What it does
Define a complete design-control set for this release.

### Method
1. A pass traces user need to input to verification to risk control, for the hazards in this release.
2. A fail is a hazard with no control, or a control with no verification.
3. Name the release.

### Do not
Do not pass because the procedure document exists.

### Output
A trace rule.

A missing fact stays [GAP].

## DH-03.02.1.2.2 Trace score

Worker: Product Development Lead (`product-development-lead`). 4 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.02.1.2.2 Trace score.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.03.02.1.2. The other skills under this competency do a different job.

### What it does
Score the release.

### Method
1. Sample the hazards in the risk file.
2. Mark each traced or broken.
3. Quote the broken link.

### Do not
Do not sample only the hazards that trace.

### Output
A score.

A missing fact stays [GAP].

## DH-03.02.1.2.3 Design control repair

Worker: Product Development Lead (`product-development-lead`). 4 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.02.1.2.3 Design control repair.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.03.02.1.2. The other skills under this competency do a different job.

### What it does
Assign a broken link.

### Method
1. Name the owner.
2. State whether the release waits.
3. Name the review that must accept the repair.

### Do not
Do not ship a release with a hazard that has no control.

### Output
An owner and whether the release waits.

A missing fact stays [GAP].
