---
name: dh-02-02-1-1-customer-implementation-planning-deployment-coordin
description: "Only while the Digital Health Library connector is connected. Run one task in DH-02.02.1.1 Customer Implementation Planning & Deployment Coordination. Use when the user asks for Implementation scope, Deployment sequence, Go-live bar. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.02.1.1 Customer Implementation Planning & Deployment Coordination

Heading: DH-02.02.1 Implementation Delivery.
Core: DH-02.02 Customer Success & Implementation.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-02.02.1.1.1 Implementation scope

Worker: Digital Adoption Lead (`digital-adoption-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.02.1.1.1 Implementation scope.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.02.1.1. The other skills under this competency do a different job.

### What it does
Write what this deployment includes.

### Method
1. Name the site, the modules, and the users in the first release.
2. Name the integrations that are in the first release and those that are later.
3. Name the clinical workflow that must work on day one.

### Do not
Do not include a module the site has not agreed to.

### Output
A scope note: site, modules, day-one workflow.

A missing fact stays [GAP].

## DH-02.02.1.1.2 Deployment sequence

Worker: Digital Adoption Lead (`digital-adoption-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.02.1.1.2 Deployment sequence.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.02.1.1. The other skills under this competency do a different job.

### What it does
Order the work.

### Method
1. List the steps (access, configure, train, go-live) with an owner.
2. Name the step that cannot start until another finishes.
3. Name the date the site expects go-live, or mark it unset.

### Do not
Do not schedule training before the day-one workflow is configured.

### Output
A sequence with dependencies.

A missing fact stays [GAP].

## DH-02.02.1.1.3 Go-live bar

Worker: Digital Adoption Lead (`digital-adoption-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.02.1.1.3 Go-live bar.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.02.1.1. The other skills under this competency do a different job.

### What it does
State what must be true to call the site live.

### Method
1. Name the users who must complete one real task.
2. Name the data that must be present.
3. Name who at the site agrees the bar is met.

### Do not
Do not call a site live because the contract started.

### Output
A go-live bar and the site approver.

A missing fact stays [GAP].
