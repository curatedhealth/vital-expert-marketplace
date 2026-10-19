---
name: "DH-05.02.2.1 Executive Dashboard Design"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-05.02.2.1 Executive Dashboard Design. Use when the user asks for Executive question, Dashboard layout, Executive review. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-05.02.2.1 Executive Dashboard Design

Heading: DH-05.02.2 Executive Dashboards & Reporting.
Core: DH-05.02 Decision Support & Business Intelligence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-05.02.2.1.1 Executive question

Worker: Clinical Content Product Manager (`clinical-content-product-manager`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.02.2.1.1 Executive question.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.02.2.1. The other skills under this competency do a different job.

### What it does
Name the question this dashboard answers for a named executive.

### Method
1. Name the person or the role and the decision.
2. Name the few metrics that decide it.
3. Name the metric you will keep off this dashboard.

### Do not
Do not build an executive dashboard as a catalog of every KPI.

### Output
A question and a short metric list.

A missing fact stays [GAP].

## DH-05.02.2.1.2 Dashboard layout

Worker: Clinical Content Product Manager (`clinical-content-product-manager`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.02.2.1.2 Dashboard layout.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.02.2.1. The other skills under this competency do a different job.

### What it does
Place those metrics so the decision is visible.

### Method
1. Put the decision metric first.
2. Show the period and the comparison (last period or target).
3. Show the timestamp of the data.

### Do not
Do not hide the timestamp.

### Output
A layout: first metric, comparison, timestamp.

A missing fact stays [GAP].

## DH-05.02.2.1.3 Executive review

Worker: Clinical Content Product Manager (`clinical-content-product-manager`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.05.02.2.1.3 Executive review.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.05.02.2.1. The other skills under this competency do a different job.

### What it does
Review the dashboard with the executive before it is the official one.

### Method
1. Ask them to make the decision from the page.
2. Record the metric they asked for that is missing.
3. Record a metric they told you to remove.

### Do not
Do not declare the dashboard official without that review.

### Output
A review note.

A missing fact stays [GAP].
