---
name: "DH-04.03.4.1 FDA-Compliant Software Development & IEC 62304 Execution"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-04.03.4.1 FDA-Compliant Software Development & IEC 62304 Execution. Use when the user asks for Safety class and software items, Required process for the class, Problem resolution record. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-04.03.4.1 FDA-Compliant Software Development & IEC 62304 Execution

Heading: DH-04.03.4 Medical Software Development.
Core: DH-04.03 Software Engineering Excellence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-04.03.4.1.1 Safety class and software items

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.03.4.1.1 Safety class and software items.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.03.4.1. The other skills under this competency do a different job.

### What it does
Set the software safety class and list the software items it covers.

### Method
1. State the class (A, B, or C) and the harm that drove it.
2. List the software items in that class.
3. Separate items that are unknown off-the-shelf from items the team writes.

### Do not
Do not assign class A because the team prefers a lighter process.

### Output
A class statement and an item list.

A missing fact stays [GAP].

## DH-04.03.4.1.2 Required process for the class

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.03.4.1.2 Required process for the class.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.03.4.1. The other skills under this competency do a different job.

### What it does
Name the plans the class requires and whether each plan exists.

### Method
1. For the chosen class, list the plans (development, risk, configuration, problem resolution, maintenance).
2. Mark each plan present, draft, or missing.
3. Tie the plan to the product version.

### Do not
Do not cite IEC 62304 as a plan. Cite the document.

### Output
A plan checklist against the class.

A missing fact stays [GAP].

## DH-04.03.4.1.3 Problem resolution record

Worker: Clinical Algorithm Validator (`clinical-algorithm-validator`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.03.4.1.3 Problem resolution record.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.03.4.1. The other skills under this competency do a different job.

### What it does
Record a software problem so it can be traced to a change.

### Method
1. Give the problem an id, a software item, and the version found.
2. State the effect on the hazardous function.
3. Point at the change that fixed it, or leave it open.

### Do not
Do not close a problem that affects a class B or C function without a change or an accepted rationale.

### Output
A problem record: id, item, version, effect, change or open.

A missing fact stays [GAP].
