---
name: dh-04-02-2-1-security-by-design-threat-modelling-for-digital-hea
description: "Only while the Digital Health Library connector is connected. Run one task in DH-04.02.2.1 Security-by-Design & Threat Modelling for Digital Health Platforms. Use when the user asks for Trust boundary drawing, Threat enumeration, Mitigation or accepted risk. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-04.02.2.1 Security-by-Design & Threat Modelling for Digital Health Platforms

Heading: DH-04.02.2 Security Architecture.
Core: DH-04.02 Cybersecurity & Privacy.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-04.02.2.1.1 Trust boundary drawing

Worker: Security Engineer, Digital Health (`security-engineer-digital-health`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.02.2.1.1 Trust boundary drawing.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.02.2.1. The other skills under this competency do a different job.

### What it does
Draw the boundaries where trust changes.

### Method
1. Name the components (app, EHR, device, identity provider, data store).
2. Mark each hop that crosses a network, a tenant, or a privilege level.
3. Label what is inside the product boundary and what is a third party.

### Do not
Do not draw a single box labeled cloud.

### Output
A boundary sketch with the hops that leave the product.

A missing fact stays [GAP].

## DH-04.02.2.1.2 Threat enumeration

Worker: Security Engineer, Digital Health (`security-engineer-digital-health`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.02.2.1.2 Threat enumeration.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.02.2.1. The other skills under this competency do a different job.

### What it does
List threats on each boundary.

### Method
1. For each hop, ask what can be spoofed, tampered with, disclosed, or denied.
2. Write the threat as actor, hop, and asset.
3. Drop a threat that has no asset.

### Do not
Do not paste a generic STRIDE list that is not tied to a hop.

### Output
A threat list keyed to hops.

A missing fact stays [GAP].

## DH-04.02.2.1.3 Mitigation or accepted risk

Worker: Security Engineer, Digital Health (`security-engineer-digital-health`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.02.2.1.3 Mitigation or accepted risk.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.02.2.1. The other skills under this competency do a different job.

### What it does
Choose a mitigation or an explicit acceptance for each threat.

### Method
1. Name the control that addresses the threat, or state that the risk is accepted.
2. Name the person who accepts a risk, and the condition that would reopen it.
3. Leave no threat in the list without one of those two outcomes.

### Do not
Do not accept a risk anonymously.

### Output
A threat register: mitigation, or acceptor plus reopen condition.

A missing fact stays [GAP].
