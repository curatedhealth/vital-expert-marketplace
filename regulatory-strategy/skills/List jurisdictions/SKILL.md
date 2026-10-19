---
name: list-jurisdictions
description: "Only while the Digital Health Library connector is connected. Use only after the job Multi-Region Regulatory Alignment & Harmonisation Execution is chosen, to do List jurisdictions."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# List jurisdictions

## Execution formula
Worker: not bound.
Skill: CF-12.03.03.2.1.4 List jurisdictions.
Prompt: not bound.
Template: not bound.
Tool: `regulatory-dh.list_jurisdictions`. This call is not counted. Do not close it with Verify.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Boundary

Call this when the buyer asks which registers are loaded. This call is not counted. It returns stored authorization and safety-event counts, the last load date, and the sources.
