---
name: dh-02-04-2-1-scalable-design-system-development-component-manage
description: "Only while the Digital Health Library connector is connected. Run one task in DH-02.04.2.1 Scalable Design System Development & Component Management. Use when the user asks for Component contract, Component change, Adoption of the component. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.04.2.1 Scalable Design System Development & Component Management

Heading: DH-02.04.2 Design Systems.
Core: DH-02.04 User Experience Excellence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-02.04.2.1.1 Component contract

Worker: Service Design Director (`service-design-director`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.04.2.1.1 Component contract.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.04.2.1. The other skills under this competency do a different job.

### What it does
Write the contract for one component.

### Method
1. Name the component and the states it supports.
2. Name the content it must not invent (clinical claims, doses).
3. Name the product surfaces that may use it.

### Do not
Do not let a marketing page and a clinical task share a component that invents clinical content.

### Output
A contract: states, forbidden content, allowed surfaces.

A missing fact stays [GAP].

## DH-02.04.2.1.2 Component change

Worker: Service Design Director (`service-design-director`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.04.2.1.2 Component change.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.04.2.1. The other skills under this competency do a different job.

### What it does
Change the component without breaking the contract.

### Method
1. Name the change and the states it affects.
2. Name the surfaces that must be rechecked.
3. Name the version of the system.

### Do not
Do not change a state that a clinical task depends on without naming that task.

### Output
A change note: version, states, surfaces.

A missing fact stays [GAP].

## DH-02.04.2.1.3 Adoption of the component

Worker: Service Design Director (`service-design-director`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.04.2.1.3 Adoption of the component.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.04.2.1. The other skills under this competency do a different job.

### What it does
Record which surfaces use the current version.

### Method
1. List surfaces on the current version and surfaces on an older one.
2. Name the owner of a surface that is behind.
3. Name the date they will move, or why they will not.

### Do not
Do not assume a published component is the one in the product.

### Output
A version map of surfaces.

A missing fact stays [GAP].
