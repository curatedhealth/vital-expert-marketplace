---
name: "DH-02.03.3.1 KPI Dashboard Development & Automated Performance Tracking"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-02.03.3.1 KPI Dashboard Development & Automated Performance Tracking. Use when the user asks for KPI definition, Dashboard slice, Tracking job. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.03.3.1 KPI Dashboard Development & Automated Performance Tracking

Heading: DH-02.03.3 Measurement & KPIs.
Core: DH-02.03 Patient Engagement & Advocacy.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-02.03.3.1.1 KPI definition

Worker: Data & Analytics Lead (`data-analytics-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.03.3.1.1 KPI definition.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.03.3.1. The other skills under this competency do a different job.

### What it does
Define each KPI the dashboard will show.

### Method
1. Name the decision the KPI serves.
2. Write the formula, the grain (account, site, week), and the source table.
3. Name a KPI you will not show, and why.

### Do not
Do not add a KPI with no source table.

### Output
A KPI card: decision, formula, grain, source.

A missing fact stays [GAP].

## DH-02.03.3.1.2 Dashboard slice

Worker: Data & Analytics Lead (`data-analytics-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.03.3.1.2 Dashboard slice.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.03.3.1. The other skills under this competency do a different job.

### What it does
Place the KPIs on one dashboard for one audience.

### Method
1. Name the audience.
2. Place only the KPIs that audience decides on.
3. Name the refresh cadence.

### Do not
Do not build one dashboard for every audience.

### Output
One dashboard: audience, KPIs, cadence.

A missing fact stays [GAP].

## DH-02.03.3.1.3 Tracking job

Worker: Data & Analytics Lead (`data-analytics-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.03.3.1.3 Tracking job.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.03.3.1. The other skills under this competency do a different job.

### What it does
Name the job that refreshes the dashboard.

### Method
1. Name the job and the owner who is paged when it fails.
2. State how a failed refresh is visible to the audience.
3. State the last successful run you will show.

### Do not
Do not hide a stale dashboard behind the last good numbers without a timestamp.

### Output
A job, an owner, and a visible timestamp.

A missing fact stays [GAP].
