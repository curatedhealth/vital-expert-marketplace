---
name: "DH-04.03.1.2 Infrastructure Scalability Assessment & Cloud Performance Monitoring"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-04.03.1.2 Infrastructure Scalability Assessment & Cloud Performance Monitoring. Use when the user asks for Capacity evidence, First-failure review, Region and residency check. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-04.03.1.2 Infrastructure Scalability Assessment & Cloud Performance Monitoring

Heading: DH-04.03.1 Cloud & Infrastructure.
Core: DH-04.03 Software Engineering Excellence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-04.03.1.2.1 Capacity evidence

Worker: Digital Health Product Manager (`digital-health-product-manager`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.03.1.2.1 Capacity evidence.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.03.1.2. The other skills under this competency do a different job.

### What it does
Check the scale claim against a measurement.

### Method
1. Find the latest load result or production peak for the stated unit.
2. Compare it with the number in the design.
3. Record the date and the environment of the measurement.

### Do not
Do not treat a cloud quota as a load test.

### Output
A comparison of claimed limit and measured peak.

A missing fact stays [GAP].

## DH-04.03.1.2.2 First-failure review

Worker: Digital Health Product Manager (`digital-health-product-manager`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.03.1.2.2 First-failure review.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.03.1.2. The other skills under this competency do a different job.

### What it does
See whether the component that was supposed to fail first is the one that struggles.

### Method
1. Look at errors and saturation on that component.
2. If a different component is saturated, say so.
3. State whether the design note should be corrected.

### Do not
Do not hide saturation on a component the design did not mention.

### Output
A note: expected bottleneck, observed bottleneck.

A missing fact stays [GAP].

## DH-04.03.1.2.3 Region and residency check

Worker: Digital Health Product Manager (`digital-health-product-manager`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.03.1.2.3 Region and residency check.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.03.1.2. The other skills under this competency do a different job.

### What it does
Check that the data class is still in the region the design named.

### Method
1. Compare live store region with the placement table.
2. Flag a replica or a backup that leaves the region.
3. Name the owner if a store has moved.

### Do not
Do not assume a backup stays in the primary region.

### Output
A region check per store that holds patient data.

A missing fact stays [GAP].
