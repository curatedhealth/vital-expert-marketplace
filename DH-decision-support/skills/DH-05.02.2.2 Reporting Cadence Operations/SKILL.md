---
name: "DH-05.02.2.2 Reporting Cadence Operations"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-05.02.2.2 Reporting Cadence Operations. Use when the user asks for Cadence, Issue record, Cadence break. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-05.02.2.2 Reporting Cadence Operations

Heading: DH-05.02.2 Executive Dashboards & Reporting.
Core: DH-05.02 Decision Support & Business Intelligence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-05.02.2.2.1 Cadence

Worker: Clinical Content Product Manager (`clinical-content-product-manager`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.02.2.2.1 Cadence.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.02.2.2. The other skills under this competency do a different job.

### What it does
Set the cadence of the report.

### Method
1. Name the report, the audience, and the day it is due.
2. Name the source refresh that must finish first.
3. Name what is sent if the refresh fails.

### Do not
Do not send last period's numbers as this period's.

### Output
A cadence and a failure behavior.

A missing fact stays [GAP].

## DH-05.02.2.2.2 Issue record

Worker: Clinical Content Product Manager (`clinical-content-product-manager`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.02.2.2.2 Issue record.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.02.2.2. The other skills under this competency do a different job.

### What it does
Record each issue of the report.

### Method
1. Name the period, the sender, and the recipients.
2. Attach the data timestamp.
3. Note a metric that was withheld and why.

### Do not
Do not send a report with no timestamp.

### Output
An issue record.

A missing fact stays [GAP].

## DH-05.02.2.2.3 Cadence break

Worker: Clinical Content Product Manager (`clinical-content-product-manager`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.02.2.2.3 Cadence break.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.02.2.2. The other skills under this competency do a different job.

### What it does
Record a missed issue.

### Method
1. Name the missed date and the reason (refresh, owner absent, decision cancelled).
2. Name who was told.
3. Name the next issue date.

### Do not
Do not skip an issue silently.

### Output
A break record.

A missing fact stays [GAP].
