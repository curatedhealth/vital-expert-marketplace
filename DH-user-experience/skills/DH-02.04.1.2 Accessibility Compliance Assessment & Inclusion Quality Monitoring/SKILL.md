---
name: "DH-02.04.1.2 Accessibility Compliance Assessment & Inclusion Quality Monitoring"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-02.04.1.2 Accessibility Compliance Assessment & Inclusion Quality Monitoring. Use when the user asks for Conformance sample, Open barrier age, Access release decision. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.04.1.2 Accessibility Compliance Assessment & Inclusion Quality Monitoring

Heading: DH-02.04.1 Accessibility & Inclusion.
Core: DH-02.04 User Experience Excellence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-02.04.1.2.1 Conformance sample

Worker: Health Equity & Digital Access Lead (`health-equity-access-lead`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.04.1.2.1 Conformance sample.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.04.1.2. The other skills under this competency do a different job.

### What it does
Sample screens against the named standard.

### Method
1. Use the screen list from the requirement.
2. Check each screen against the requirement you claimed.
3. Record pass, fail, or not tested.

### Do not
Do not test a different standard than the one claimed.

### Output
A sample with a status per screen.

A missing fact stays [GAP].

## DH-02.04.1.2.2 Open barrier age

Worker: Health Equity & Digital Access Lead (`health-equity-access-lead`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.04.1.2.2 Open barrier age.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.04.1.2. The other skills under this competency do a different job.

### What it does
Age the barriers that are still open.

### Method
1. List open breaks from assistive checks.
2. Count days open.
3. Separate a break on a day-one task from a break on a later screen.

### Do not
Do not close a barrier because a scan score improved.

### Output
An age list.

A missing fact stays [GAP].

## DH-02.04.1.2.3 Access release decision

Worker: Health Equity & Digital Access Lead (`health-equity-access-lead`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.04.1.2.3 Access release decision.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.04.1.2. The other skills under this competency do a different job.

### What it does
Decide whether this release meets the requirement.

### Method
1. Block the release if a day-one task has an open break.
2. Allow a later screen only with a named exclusion.
3. Record the decision against the build.

### Do not
Do not ship a day-one task that failed the assistive check.

### Output
A decision: build, block or allow, exclusion if any.

A missing fact stays [GAP].
