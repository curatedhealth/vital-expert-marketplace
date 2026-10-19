---
name: dh-04-03-1-1-scalable-healthcare-infrastructure-design-cloud-ope
description: "Only while the Digital Health Library connector is connected. Run one task in DH-04.03.1.1 Scalable Healthcare Infrastructure Design & Cloud Operations. Use when the user asks for Workload and data placement, Scale limit, Operate the environment. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-04.03.1.1 Scalable Healthcare Infrastructure Design & Cloud Operations

Heading: DH-04.03.1 Cloud & Infrastructure.
Core: DH-04.03 Software Engineering Excellence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-04.03.1.1.1 Workload and data placement

Worker: Digital Health Product Manager (`digital-health-product-manager`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.03.1.1.1 Workload and data placement.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.03.1.1. The other skills under this competency do a different job.

### What it does
Place each workload and its data store in a named environment.

### Method
1. List the workloads (API, worker, model, device gateway).
2. Name the region and the account or subscription for each.
3. State which data class lives in which store.

### Do not
Do not write multi-region without naming the regions.

### Output
A placement table: workload, region, store, data class.

A missing fact stays [GAP].

## DH-04.03.1.1.2 Scale limit

Worker: Digital Health Product Manager (`digital-health-product-manager`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.03.1.1.2 Scale limit.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.03.1.1. The other skills under this competency do a different job.

### What it does
State the load the design is meant to hold.

### Method
1. Name the unit (launches per minute, messages per device, concurrent clinicians).
2. Set the number the current design is expected to serve.
3. Name the component that fails first when that number is exceeded.

### Do not
Do not claim elastic scale with no first-failure component.

### Output
A limit and the component that fails first.

A missing fact stays [GAP].

## DH-04.03.1.1.3 Operate the environment

Worker: Digital Health Product Manager (`digital-health-product-manager`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.03.1.1.3 Operate the environment.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.03.1.1. The other skills under this competency do a different job.

### What it does
Say how an operator knows the environment is up.

### Method
1. Name the health signal for each workload.
2. Name who is paged and on what condition.
3. Name the runbook, or mark it [GAP].

### Do not
Do not point at a dashboard that nobody is assigned to watch.

### Output
A signal, a person, and a runbook or a gap.

A missing fact stays [GAP].
