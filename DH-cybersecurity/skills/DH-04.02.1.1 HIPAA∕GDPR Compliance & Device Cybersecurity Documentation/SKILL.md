---
name: "DH-04.02.1.1 HIPAA/GDPR Compliance & Device Cybersecurity Documentation"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-04.02.1.1 HIPAA/GDPR Compliance & Device Cybersecurity Documentation. Use when the user asks for Data class and legal basis, Control per data class, Reviewer document set. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-04.02.1.1 HIPAA/GDPR Compliance & Device Cybersecurity Documentation

Heading: DH-04.02.1 Compliance & Assurance.
Core: DH-04.02 Cybersecurity & Privacy.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-04.02.1.1.1 Data class and legal basis

Worker: Privacy Engineering Director (`privacy-engineering-director`). 4 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.02.1.1.1 Data class and legal basis.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.02.1.1. The other skills under this competency do a different job.

### What it does
List the data the product holds and the legal basis for each class.

### Method
1. Separate PHI, device identifiers, logs, and account data.
2. For each class, name the basis (care delivery, consent, legitimate interest, or a gap).
3. Name the region the basis is claimed for.

### Do not
Do not apply one basis to every class.

### Output
A class table: class, region, basis, or gap.

A missing fact stays [GAP].

## DH-04.02.1.1.2 Control per data class

Worker: Privacy Engineering Director (`privacy-engineering-director`). 4 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.02.1.1.2 Control per data class.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.02.1.1. The other skills under this competency do a different job.

### What it does
Name the control that covers each class.

### Method
1. For each class, state access control, retention, and whether it leaves the region.
2. Point at the policy or configuration that implements the control.
3. If the control is only intended, mark it not in force.

### Do not
Do not cite HIPAA or GDPR as the control. Cite the mechanism.

### Output
A control row per class, with the artifact that shows it is in force.

A missing fact stays [GAP].

## DH-04.02.1.1.3 Reviewer document set

Worker: Privacy Engineering Director (`privacy-engineering-director`). 4 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.02.1.1.3 Reviewer document set.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.02.1.1. The other skills under this competency do a different job.

### What it does
Assemble the set a reviewer can open, and mark what is missing.

### Method
1. Include the data-flow, the control matrix, and the retention schedule.
2. Check that each document names the product version it describes.
3. List any missing document as [GAP] rather than drafting it from memory.

### Do not
Do not fill a missing policy with a summary.

### Output
An index of documents plus a gap list.

A missing fact stays [GAP].
