---
name: "DH-05.03.3.2 Analytics Platform Governance"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-05.03.3.2 Analytics Platform Governance. Use when the user asks for Platform access rule, Publish record, Access review. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-05.03.3.2 Analytics Platform Governance

Heading: DH-05.03.3 Analytics Governance & Enablement.
Core: DH-05.03 Analytics Product Management & Enablement.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-05.03.3.2.1 Platform access rule

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.03.3.2.1 Platform access rule.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.03.3.2. The other skills under this competency do a different job.

### What it does
Write who may publish a metric or a dashboard.

### Method
1. Name the roles that may publish to the certified layer.
2. Name the roles that may explore without publishing.
3. Name the data they may not export.

### Do not
Do not give publish rights to everyone who can log in.

### Output
An access rule.

A missing fact stays [GAP].

## DH-05.03.3.2.2 Publish record

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.03.3.2.2 Publish record.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.03.3.2. The other skills under this competency do a different job.

### What it does
Record a publish.

### Method
1. Name the object, the publisher, and the date.
2. Name whether it uses only certified metrics.
3. Refuse a publish that recomputes a certified metric locally.

### Do not
Do not publish a local recomputation of a certified metric.

### Output
A publish record or a refusal.

A missing fact stays [GAP].

## DH-05.03.3.2.3 Access review

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.03.3.2.3 Access review.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.03.3.2. The other skills under this competency do a different job.

### What it does
Review publish rights.

### Method
1. List current publishers.
2. Remove a publisher who has changed role.
3. Record the review date.

### Do not
Do not leave publish rights on a departed role.

### Output
A review.

A missing fact stays [GAP].
