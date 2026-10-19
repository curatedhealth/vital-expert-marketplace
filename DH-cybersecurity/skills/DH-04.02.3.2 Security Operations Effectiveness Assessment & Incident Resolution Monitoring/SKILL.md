---
name: "DH-04.02.3.2 Security Operations Effectiveness Assessment & Incident Resolution Monitoring"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-04.02.3.2 Security Operations Effectiveness Assessment & Incident Resolution Monitoring. Use when the user asks for Open vulnerability age, Resolution evidence, Repeat failure class. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-04.02.3.2 Security Operations Effectiveness Assessment & Incident Resolution Monitoring

Heading: DH-04.02.3 Security Operations.
Core: DH-04.02 Cybersecurity & Privacy.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-04.02.3.2.1 Open vulnerability age

Worker: Security Engineer, Digital Health (`security-engineer-digital-health`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.02.3.2.1 Open vulnerability age.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.02.3.2. The other skills under this competency do a different job.

### What it does
Measure how long reachable vulnerabilities have stayed open.

### Method
1. List reachable items that are not patched and not accepted.
2. Compute age from intake date.
3. Separate items past the team's stated window from items still inside it.

### Do not
Do not include unreachable CVEs in the age count.

### Output
An aging list of reachable open items.

A missing fact stays [GAP].

## DH-04.02.3.2.2 Resolution evidence

Worker: Security Engineer, Digital Health (`security-engineer-digital-health`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.02.3.2.2 Resolution evidence.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.02.3.2. The other skills under this competency do a different job.

### What it does
Check that a closed item has evidence.

### Method
1. For a patched item, confirm the deployed version.
2. For an accepted item, confirm the acceptance is unexpired.
3. Reopen an item whose evidence is a ticket with no deployment.

### Do not
Do not treat a merged pull request as deployment.

### Output
A closed-item check: deployed version or unexpired acceptance.

A missing fact stays [GAP].

## DH-04.02.3.2.3 Repeat failure class

Worker: Security Engineer, Digital Health (`security-engineer-digital-health`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.02.3.2.3 Repeat failure class.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.02.3.2. The other skills under this competency do a different job.

### What it does
Name the class of vulnerability that keeps returning.

### Method
1. Group open and recently closed items (dependency, auth, exposed admin, device protocol).
2. Name the class with the most reachable items.
3. State the engineering change that would shrink that class, as distinct from patching one CVE.

### Do not
Do not recommend a new scanner as the change.

### Output
One repeat class and one engineering change.

A missing fact stays [GAP].
