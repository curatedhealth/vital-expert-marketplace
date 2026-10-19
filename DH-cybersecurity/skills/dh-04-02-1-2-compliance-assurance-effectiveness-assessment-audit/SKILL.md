---
name: dh-04-02-1-2-compliance-assurance-effectiveness-assessment-audit
description: "Only while the Digital Health Library connector is connected. Run one task in DH-04.02.1.2 Compliance Assurance Effectiveness Assessment & Audit Readiness Monitoring. Use when the user asks for Claimed control versus artifact, Gap scoring by citation, Missing artifact owner. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-04.02.1.2 Compliance Assurance Effectiveness Assessment & Audit Readiness Monitoring

Heading: DH-04.02.1 Compliance & Assurance.
Core: DH-04.02 Cybersecurity & Privacy.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-04.02.1.2.1 Claimed control versus artifact

Worker: Privacy Engineering Director (`privacy-engineering-director`). 4 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.02.1.2.1 Claimed control versus artifact.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.02.1.2. The other skills under this competency do a different job.

### What it does
Check that each control named in the matrix has an artifact.

### Method
1. Read the control matrix.
2. Open the policy, configuration, or log that is supposed to prove each row.
3. Mark the row proven, unproven, or contradicted.

### Do not
Do not accept a control whose only evidence is the matrix itself.

### Output
A row-by-row proof status.

A missing fact stays [GAP].

## DH-04.02.1.2.2 Gap scoring by citation

Worker: Privacy Engineering Director (`privacy-engineering-director`). 4 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.02.1.2.2 Gap scoring by citation.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.02.1.2. The other skills under this competency do a different job.

### What it does
Score each unproven control against the citation it claims.

### Method
1. Name the HIPAA, GDPR, or device-security clause the row cites.
2. State what that clause requires and what the artifact shows.
3. Rank the gap as blocking or as a documentation miss.

### Do not
Do not rank every gap as blocking.

### Output
A ranked gap list with the citation.

A missing fact stays [GAP].

## DH-04.02.1.2.3 Missing artifact owner

Worker: Privacy Engineering Director (`privacy-engineering-director`). 4 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.02.1.2.3 Missing artifact owner.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.02.1.2. The other skills under this competency do a different job.

### What it does
Assign an owner to each missing artifact.

### Method
1. Name a person or a role, not a department slogan.
2. Set the date the artifact is due.
3. Record an owner as unknown when you cannot find one.

### Do not
Do not close the assessment because the matrix looks complete.

### Output
An owner and a due date per missing artifact.

A missing fact stays [GAP].
