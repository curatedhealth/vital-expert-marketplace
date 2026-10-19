---
name: "DH-04.02.4.1 Privacy Engineering & Consent Management Implementation"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-04.02.4.1 Privacy Engineering & Consent Management Implementation. Use when the user asks for Consent purpose list, Consent capture check, Privacy engineering change. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-04.02.4.1 Privacy Engineering & Consent Management Implementation

Heading: DH-04.02.4 Privacy & Consent.
Core: DH-04.02 Cybersecurity & Privacy.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-04.02.4.1.1 Consent purpose list

Worker: Privacy Engineering Director (`privacy-engineering-director`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.02.4.1.1 Consent purpose list.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.02.4.1. The other skills under this competency do a different job.

### What it does
List the purposes the product asks a person to agree to.

### Method
1. Write each purpose in the words the product uses.
2. Tie each purpose to a data class.
3. Mark a purpose that has no screen or form yet.

### Do not
Do not collapse research, care, and marketing into one purpose.

### Output
A purpose list mapped to data classes.

A missing fact stays [GAP].

## DH-04.02.4.1.2 Consent capture check

Worker: Privacy Engineering Director (`privacy-engineering-director`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.02.4.1.2 Consent capture check.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.02.4.1. The other skills under this competency do a different job.

### What it does
Check that a yes is stored with enough context to honor a later no.

### Method
1. Record what is stored (who, when, which purpose, which version of the text).
2. State how a withdrawal is stored and which processing it stops.
3. Name a purpose that cannot be withdrawn and the reason.

### Do not
Do not treat a checkbox defaulted to on as a captured consent.

### Output
A capture note: fields stored, and what withdrawal stops.

A missing fact stays [GAP].

## DH-04.02.4.1.3 Privacy engineering change

Worker: Privacy Engineering Director (`privacy-engineering-director`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.02.4.1.3 Privacy engineering change.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.02.4.1. The other skills under this competency do a different job.

### What it does
Change the design when a purpose collects more than it uses.

### Method
1. Find a field that is collected and not read by the stated purpose.
2. Remove it, or name the purpose that actually needs it.
3. Record the product version that carries the change.

### Do not
Do not keep a field because it might be useful later.

### Output
One field decision and the version that carries it.

A missing fact stays [GAP].
