---
name: dh-02-04-2-2-design-system-effectiveness-assessment-adoption-qua
description: "Only while the Digital Health Library connector is connected. Run one task in DH-02.04.2.2 Design System Effectiveness Assessment & Adoption Quality Monitoring. Use when the user asks for Contract check, Behind-version count, System follow-up. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.04.2.2 Design System Effectiveness Assessment & Adoption Quality Monitoring

Heading: DH-02.04.2 Design Systems.
Core: DH-02.04 User Experience Excellence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-02.04.2.2.1 Contract check

Worker: Service Design Director (`service-design-director`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.04.2.2.1 Contract check.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.04.2.2. The other skills under this competency do a different job.

### What it does
Check a surface against the component contract.

### Method
1. Pick a surface that uses the component.
2. Compare states and forbidden content with the contract.
3. Mark a breach.

### Do not
Do not pass a surface because it looks similar.

### Output
A check: surface, version, breaches.

A missing fact stays [GAP].

## DH-02.04.2.2.2 Behind-version count

Worker: Service Design Director (`service-design-director`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.04.2.2.2 Behind-version count.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.04.2.2. The other skills under this competency do a different job.

### What it does
Count surfaces not on the current version.

### Method
1. Use the version map.
2. Count surfaces behind, by owner.
3. Separate a clinical task from a marketing surface.

### Do not
Do not hide a clinical task on an old component.

### Output
A count by owner.

A missing fact stays [GAP].

## DH-02.04.2.2.3 System follow-up

Worker: Service Design Director (`service-design-director`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.04.2.2.3 System follow-up.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.04.2.2. The other skills under this competency do a different job.

### What it does
Assign the breach or the old surface.

### Method
1. Name the owner.
2. State whether the contract or the surface changes.
3. Name the version that should contain the fix.

### Do not
Do not update the contract silently to match a breach.

### Output
An owner and a version.

A missing fact stays [GAP].
