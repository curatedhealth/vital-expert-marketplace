---
name: "DH-04.01.2.2 EHR Integration Quality Assessment & Deployment Reliability Monitoring"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-04.01.2.2 EHR Integration Quality Assessment & Deployment Reliability Monitoring. Use when the user asks for Launch matrix definition, Launch matrix run, Failed cell report. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-04.01.2.2 EHR Integration Quality Assessment & Deployment Reliability Monitoring

Heading: DH-04.01.2 EHR Integration Delivery.
Core: DH-04.01 Clinical Integration & Interoperability.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-04.01.2.2.1 Launch matrix definition

Worker: FHIR Integration Specialist (`fhir-integration-specialist`). 5 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.01.2.2.1 Launch matrix definition.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.01.2.2. The other skills under this competency do a different job.

### What it does
Define the launches that must work before the integration is called ready.

### Method
1. List the user roles, patient states, and encounter states the product claims to support.
2. Set a pass for launch (token contains the context the screen needs) and a pass for write-back (the chart shows the written resource).
3. Set a latency ceiling for the token response and for the first clinical read.

### Do not
Do not declare ready from a single happy-path launch.

### Output
A matrix of role, patient state, and encounter state, with the two pass rules and the latency ceiling.

A missing fact stays [GAP].

## DH-04.01.2.2.2 Launch matrix run

Worker: FHIR Integration Specialist (`fhir-integration-specialist`). 5 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.01.2.2.2 Launch matrix run.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.01.2.2. The other skills under this competency do a different job.

### What it does
Execute the matrix and keep the HTTP result of each cell.

### Method
1. Run each cell in the named sandbox.
2. Record status code, whether context was present, and whether write-back was visible in the chart.
3. Stop and record the cell when the EHR returns an error, rather than retrying until it passes.

### Do not
Do not substitute a mocked token for an EHR launch.

### Output
A filled matrix with one outcome per cell.

A missing fact stays [GAP].

## DH-04.01.2.2.3 Failed cell report

Worker: FHIR Integration Specialist (`fhir-integration-specialist`). 5 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.01.2.2.3 Failed cell report.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.01.2.2. The other skills under this competency do a different job.

### What it does
Turn each failed cell into a defect the EHR owner or the app owner can act on.

### Method
1. State the cell, the scope requested, and the HTTP status or OperationOutcome.
2. Assign the defect to the app or to the EHR configuration.
3. Leave the cell failed until a later run passes it.

### Do not
Do not reclassify a failed cell as a known limitation without naming who accepted it.

### Output
A defect list keyed to matrix cells.

A missing fact stays [GAP].
