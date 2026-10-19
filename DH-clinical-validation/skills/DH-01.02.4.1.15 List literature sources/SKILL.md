---
name: "DH-01.02.4.1.15 List literature sources"
description: "Only while the Digital Health Library connector is connected. Use only after the job DH-01.02.4.1 is chosen, to do List literature sources. Catalogue job evidence-table. Tool literature.list_sources."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-01.02.4.1.15 List literature sources

Worker: not bound.
Skill: CF-12.01.02.4.1.15 List literature sources.
Prompt: not bound.
Template: not bound.
Tool: `literature.list_sources`. This call is not counted. Do not close it with Verify.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

List the indexes this server queries. An index that is off stays off. Do not treat the list as a search.

Catalogue job: `evidence-table`.

