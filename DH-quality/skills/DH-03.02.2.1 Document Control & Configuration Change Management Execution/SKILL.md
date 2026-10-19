---
name: "DH-03.02.2.1 Document Control & Configuration Change Management Execution"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-03.02.2.1 Document Control & Configuration Change Management Execution. Use when the user asks for Controlled document, Change record, Obsolete copy. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-03.02.2.1 Document Control & Configuration Change Management Execution

Heading: DH-03.02.2 Documentation & Change Control.
Core: DH-03.02 Quality Management & Compliance.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-03.02.2.1.1 Controlled document

Worker: QA Manager, Software (V&V) (`quality-assurance-manager-software`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.02.2.1.1 Controlled document.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.03.02.2.1. The other skills under this competency do a different job.

### What it does
Put one document under control.

### Method
1. Name the document, the version, and the owner.
2. Name who may approve a change.
3. Name the previous version that this one replaces.

### Do not
Do not circulate an uncontrolled copy as the current procedure.

### Output
A controlled document: version, owner, approver, predecessor.

A missing fact stays [GAP].

## DH-03.02.2.1.2 Change record

Worker: QA Manager, Software (V&V) (`quality-assurance-manager-software`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.02.2.1.2 Change record.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.03.02.2.1. The other skills under this competency do a different job.

### What it does
Record a change to a controlled document or a configuration item.

### Method
1. Name the item, the change, and the reason.
2. Name the products or submissions the change affects.
3. Name the approver and the date.

### Do not
Do not change a released configuration without this record.

### Output
A change record.

A missing fact stays [GAP].

## DH-03.02.2.1.3 Obsolete copy

Worker: QA Manager, Software (V&V) (`quality-assurance-manager-software`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.02.2.1.3 Obsolete copy.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.03.02.2.1. The other skills under this competency do a different job.

### What it does
Remove the obsolete version from use.

### Method
1. Name where the current version lives.
2. Name the obsolete copy you found, or say you found none.
3. Name who checks the next time.

### Do not
Do not leave the obsolete version in the working folder.

### Output
A location for the current version, and any obsolete copy.

A missing fact stays [GAP].
