---
name: "DH-05.03.3.1 Metric Certification & Standards"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-05.03.3.1 Metric Certification & Standards. Use when the user asks for Metric certification rule, Certification record, Decertify. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-05.03.3.1 Metric Certification & Standards

Heading: DH-05.03.3 Analytics Governance & Enablement.
Core: DH-05.03 Analytics Product Management & Enablement.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-05.03.3.1.1 Metric certification rule

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.03.3.1.1 Metric certification rule.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.03.3.1. The other skills under this competency do a different job.

### What it does
Write the rule a metric must pass to be certified.

### Method
1. Name the owner, the formula, the grain, and the source.
2. Name the check (recomputation on a sample).
3. Name the status a metric has before it passes (draft).

### Do not
Do not certify a metric with no owner.

### Output
A certification rule.

A missing fact stays [GAP].

## DH-05.03.3.1.2 Certification record

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.03.3.1.2 Certification record.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.03.3.1. The other skills under this competency do a different job.

### What it does
Certify or refuse one metric.

### Method
1. Apply the rule.
2. Record pass or refuse, the date, and the certifier.
3. Point at the semantic-layer definition.

### Do not
Do not certify by adding the metric to a dashboard.

### Output
A record.

A missing fact stays [GAP].

## DH-05.03.3.1.3 Decertify

Worker: AI/ML Governance Director (`ai-ml-governance-director`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.03.3.1.3 Decertify.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.03.3.1. The other skills under this competency do a different job.

### What it does
Remove certification when the formula changes.

### Method
1. Name the metric and the change.
2. Set the status back to draft until the rule is passed again.
3. Name the dashboards that must show the draft status.

### Do not
Do not leave a changed formula certified.

### Output
A decertification.

A missing fact stays [GAP].
