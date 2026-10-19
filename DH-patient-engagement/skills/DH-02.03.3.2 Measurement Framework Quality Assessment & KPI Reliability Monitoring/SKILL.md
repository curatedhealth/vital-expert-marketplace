---
name: "DH-02.03.3.2 Measurement Framework Quality Assessment & KPI Reliability Monitoring"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-02.03.3.2 Measurement Framework Quality Assessment & KPI Reliability Monitoring. Use when the user asks for KPI recomputation, Formula drift, KPI repair. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.03.3.2 Measurement Framework Quality Assessment & KPI Reliability Monitoring

Heading: DH-02.03.3 Measurement & KPIs.
Core: DH-02.03 Patient Engagement & Advocacy.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-02.03.3.2.1 KPI recomputation

Worker: Data & Analytics Lead (`data-analytics-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.03.3.2.1 KPI recomputation.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.03.3.2. The other skills under this competency do a different job.

### What it does
Recompute one KPI from the source.

### Method
1. Pick a KPI and a period.
2. Recompute the formula from the source table.
3. Compare it with the number on the dashboard.

### Do not
Do not trust the dashboard number without a recomputation.

### Output
A comparison: source, dashboard, difference.

A missing fact stays [GAP].

## DH-02.03.3.2.2 Formula drift

Worker: Data & Analytics Lead (`data-analytics-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.03.3.2.2 Formula drift.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.03.3.2. The other skills under this competency do a different job.

### What it does
Find a KPI whose dashboard formula is not the card.

### Method
1. Read the KPI card and the dashboard definition.
2. Mark match or drift.
3. Name the grain if it differs.

### Do not
Do not treat a renamed KPI as the same formula.

### Output
A drift note.

A missing fact stays [GAP].

## DH-02.03.3.2.3 KPI repair

Worker: Data & Analytics Lead (`data-analytics-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.03.3.2.3 KPI repair.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.03.3.2. The other skills under this competency do a different job.

### What it does
Assign a drifted or unrecomputable KPI.

### Method
1. Name the owner of the card or the job.
2. State whether the card or the dashboard changes.
3. Name the refresh after which the numbers must match.

### Do not
Do not leave both versions live.

### Output
An owner and the refresh that must match.

A missing fact stays [GAP].
