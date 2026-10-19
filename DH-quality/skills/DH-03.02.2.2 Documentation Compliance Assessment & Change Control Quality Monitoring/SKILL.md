---
name: "DH-03.02.2.2 Documentation Compliance Assessment & Change Control Quality Monitoring"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-03.02.2.2 Documentation Compliance Assessment & Change Control Quality Monitoring. Use when the user asks for Document check, Document score, Document repair. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-03.02.2.2 Documentation Compliance Assessment & Change Control Quality Monitoring

Heading: DH-03.02.2 Documentation & Change Control.
Core: DH-03.02 Quality Management & Compliance.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-03.02.2.2.1 Document check

Worker: QA Manager, Software (V&V) (`quality-assurance-manager-software`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.02.2.2.1 Document check.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.03.02.2.2. The other skills under this competency do a different job.

### What it does
Define a document system that passes.

### Method
1. A pass is a current version, an approver, and no obsolete copy in the working set.
2. A fail is a submission that cites a version that is not current.
3. Name the set you will score.

### Do not
Do not pass a folder that has two versions labeled final.

### Output
A check.

A missing fact stays [GAP].

## DH-03.02.2.2.2 Document score

Worker: QA Manager, Software (V&V) (`quality-assurance-manager-software`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.02.2.2.2 Document score.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.03.02.2.2. The other skills under this competency do a different job.

### What it does
Score the set.

### Method
1. List each document as current, obsolete-in-use, or missing an approver.
2. Keep the version.
3. Note a submission that cites the wrong version.

### Do not
Do not ignore a wrong citation because the right file also exists.

### Output
A score.

A missing fact stays [GAP].

## DH-03.02.2.2.3 Document repair

Worker: QA Manager, Software (V&V) (`quality-assurance-manager-software`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.02.2.2.3 Document repair.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.03.02.2.2. The other skills under this competency do a different job.

### What it does
Assign an obsolete copy or a wrong citation.

### Method
1. Name the owner.
2. State the copy to remove or the citation to correct.
3. Name the date.

### Do not
Do not file a submission while it cites the wrong version.

### Output
An owner and a date.

A missing fact stays [GAP].
