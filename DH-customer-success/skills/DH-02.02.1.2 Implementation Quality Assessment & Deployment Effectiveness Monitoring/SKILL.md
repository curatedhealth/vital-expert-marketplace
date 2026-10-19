---
name: "DH-02.02.1.2 Implementation Quality Assessment & Deployment Effectiveness Monitoring"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-02.02.1.2 Implementation Quality Assessment & Deployment Effectiveness Monitoring. Use when the user asks for Deployment check, Site score, Deployment repair. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.02.1.2 Implementation Quality Assessment & Deployment Effectiveness Monitoring

Heading: DH-02.02.1 Implementation Delivery.
Core: DH-02.02 Customer Success & Implementation.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-02.02.1.2.1 Deployment check

Worker: Digital Adoption Lead (`digital-adoption-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.02.1.2.1 Deployment check.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.02.1.2. The other skills under this competency do a different job.

### What it does
Define a deployment that met the bar.

### Method
1. Use the go-live bar for that site.
2. Set a pass only when each bar item has evidence.
3. Name the evidence (task log, data present, site confirmation).

### Do not
Do not pass a site on the project plan's status field.

### Output
A check list tied to the bar.

A missing fact stays [GAP].

## DH-02.02.1.2.2 Site score

Worker: Digital Adoption Lead (`digital-adoption-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.02.1.2.2 Site score.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.02.1.2. The other skills under this competency do a different job.

### What it does
Score the site.

### Method
1. Check each bar item and keep the evidence id.
2. Mark missing evidence as failed, not as unknown-pass.
3. Note items that slipped past the agreed go-live date.

### Do not
Do not rescore the bar after the site is live to make it pass.

### Output
A site score with evidence ids.

A missing fact stays [GAP].

## DH-02.02.1.2.3 Deployment repair

Worker: Digital Adoption Lead (`digital-adoption-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.02.1.2.3 Deployment repair.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.02.1.2. The other skills under this competency do a different job.

### What it does
Assign what is still open.

### Method
1. Name the open bar item and the owner.
2. State whether the site stays in a limited launch.
3. Name the date the item will be rechecked.

### Do not
Do not close the deployment while a day-one workflow item is open.

### Output
An open item, an owner, and a recheck date.

A missing fact stays [GAP].
