---
name: "DH-04.01.3.1 Clinical Data Mapping & Terminology Governance Execution"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-04.01.3.1 Clinical Data Mapping & Terminology Governance Execution. Use when the user asks for Code system selection, Equivalence mapping, Unmatched code hold. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-04.01.3.1 Clinical Data Mapping & Terminology Governance Execution

Heading: DH-04.01.3 Data Exchange & Terminology.
Core: DH-04.01 Clinical Integration & Interoperability.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-04.01.3.1.1 Code system selection

Worker: Data Engineering Manager (Health) (`data-engineering-manager-health`). 5 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.01.3.1.1 Code system selection.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.01.3.1. The other skills under this competency do a different job.

### What it does
Choose the source code system and the target code system for each data element.

### Method
1. List the data elements that carry a code (condition, observation, medication, procedure).
2. Name the source system as it arrives and the target (SNOMED CT, LOINC, RxNorm, ICD) the product will store.
3. If an element has no code on arrival, say so and do not invent a default code.

### Do not
Do not map free text into a code without a stated method.

### Output
An element list: source system, target system, or uncoded.

A missing fact stays [GAP].

## DH-04.01.3.1.2 Equivalence mapping

Worker: Data Engineering Manager (Health) (`data-engineering-manager-health`). 5 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.01.3.1.2 Equivalence mapping.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.01.3.1. The other skills under this competency do a different job.

### What it does
Map each source code and state how close the target code is.

### Method
1. For each source code in scope, choose a target code.
2. Label the map equal, wider, narrower, or unmatched.
3. Keep the map version and the terminology version on the row.

### Do not
Do not label a narrower map as equal.

### Output
A map table with equivalence and both versions.

A missing fact stays [GAP].

## DH-04.01.3.1.3 Unmatched code hold

Worker: Data Engineering Manager (Health) (`data-engineering-manager-health`). 5 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.01.3.1.3 Unmatched code hold.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.01.3.1. The other skills under this competency do a different job.

### What it does
Keep unmatched codes out of the production map and name the person who may add them.

### Method
1. Separate unmatched codes from the map that production reads.
2. Count them and show the source system.
3. Name the steward who can promote a code into the map, and the rule they use.

### Do not
Do not drop unmatched codes from the source feed.

### Output
A hold list and the steward's rule for promotion.

A missing fact stays [GAP].
