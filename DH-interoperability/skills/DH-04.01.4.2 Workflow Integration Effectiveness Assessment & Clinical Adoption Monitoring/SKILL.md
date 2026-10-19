---
name: "DH-04.01.4.2 Workflow Integration Effectiveness Assessment & Clinical Adoption Monitoring"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-04.01.4.2 Workflow Integration Effectiveness Assessment & Clinical Adoption Monitoring. Use when the user asks for Designed versus observed step, Time and workaround count, Step change for the next release. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-04.01.4.2 Workflow Integration Effectiveness Assessment & Clinical Adoption Monitoring

Heading: DH-04.01.4 Clinical Workflow Enablement.
Core: DH-04.01 Clinical Integration & Interoperability.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-04.01.4.2.1 Designed versus observed step

Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.01.4.2.1 Designed versus observed step.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.01.4.2. The other skills under this competency do a different job.

### What it does
Compare the step people actually perform with the step that was designed.

### Method
1. Observe the same step after release.
2. Mark each designed action as done, skipped, or replaced.
3. Quote the workaround when a person leaves the product to finish the step.

### Do not
Do not score adoption from analytics that do not see the workaround.

### Output
A step comparison with workarounds written out.

A missing fact stays [GAP].

## DH-04.01.4.2.2 Time and workaround count

Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.01.4.2.2 Time and workaround count.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.01.4.2. The other skills under this competency do a different job.

### What it does
Count the extra time and the workarounds.

### Method
1. Time the step for a small stated number of observations.
2. Count how often the workaround appears.
3. Separate a slow screen from a step the design got wrong.

### Do not
Do not report a mean time from a single observation.

### Output
A count of workarounds and the range of times, with the number of observations.

A missing fact stays [GAP].

## DH-04.01.4.2.3 Step change for the next release

Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 3 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.01.4.2.3 Step change for the next release.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.01.4.2. The other skills under this competency do a different job.

### What it does
Name the one step that must change before the next release.

### Method
1. Pick the step with the workaround that blocks the clinical purpose.
2. State the change (remove a field, prefill a code, move the exchange).
3. Name the owner of that change.

### Do not
Do not list every polish item as the blocking step.

### Output
One blocking step, the change, and the owner.

A missing fact stays [GAP].
