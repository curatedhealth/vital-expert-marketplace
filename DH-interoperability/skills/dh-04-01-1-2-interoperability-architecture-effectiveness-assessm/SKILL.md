---
name: dh-04-01-1-2-interoperability-architecture-effectiveness-assessm
description: "Only while the Digital Health Library connector is connected. Run one task in DH-04.01.1.2 Interoperability Architecture Effectiveness Assessment & Standards Compliance Monitoring. Use when the user asks for Conformance check definition, Sample exchange scoring, Nonconformance assignment. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-04.01.1.2 Interoperability Architecture Effectiveness Assessment & Standards Compliance Monitoring

Heading: DH-04.01.1 Interoperability Architecture.
Core: DH-04.01 Clinical Integration & Interoperability.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-04.01.1.2.1 Conformance check definition

Worker: FHIR Integration Specialist (`fhir-integration-specialist`). 5 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.01.1.2.1 Conformance check definition.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.01.1.2. The other skills under this competency do a different job.

### What it does
Write the checks that decide whether an exchange meets the guide.

### Method
1. List must-support elements, cardinality rules, and bound value sets for the profiles in use.
2. Set a pass rule for each check (present and bound, present and unbound, absent and optional).
3. Name who runs the checks and on which environment.

### Do not
Do not score an exchange against a guide version that was not the one selected.

### Output
A check sheet with a pass rule per element.

A missing fact stays [GAP].

## DH-04.01.1.2.2 Sample exchange scoring

Worker: FHIR Integration Specialist (`fhir-integration-specialist`). 5 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.01.1.2.2 Sample exchange scoring.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.01.1.2. The other skills under this competency do a different job.

### What it does
Score a sample of real exchanges against that check sheet.

### Method
1. Pull a stated sample (at least one payload per profile, more when volume allows).
2. Mark each check pass or fail and keep the payload id.
3. Group failures by resource type so a single broken profile is visible.

### Do not
Do not average away a profile that failed every sample.

### Output
A score by profile, with the failing payload ids.

A missing fact stays [GAP].

## DH-04.01.1.2.3 Nonconformance assignment

Worker: FHIR Integration Specialist (`fhir-integration-specialist`). 5 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.01.1.2.3 Nonconformance assignment.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.01.1.2. The other skills under this competency do a different job.

### What it does
Give each failed check an owner and a release.

### Method
1. For each failure class, name the system that must change (sender or receiver).
2. Set the release or patch that will close it, or mark it accepted with a reason.
3. Leave a failure unowned only when the owning team is unknown, and say so.

### Do not
Do not close a failure because a ticket exists.

### Output
An open-item list: failure, owner, release or accepted reason.

A missing fact stays [GAP].
