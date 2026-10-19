---
name: "DH Diligence List diligence sources"
description: "Only while the Digital Health Library connector is connected. Use only after the job DH Diligence List sources is chosen, to do List diligence sources. Catalogue job company-dossier. Tool diligence-dh.list_sources."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH Diligence List diligence sources

Worker: not bound.
Skill: not a CF-12 row. Library tool `diligence-dh.list_sources`.
Prompt: not bound.
Template: not bound.
Tool: `diligence-dh.list_sources`. This call is not counted. Do not close it with Verify.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Every source with credential state, last load, and row counts. A source not loaded states the reason. This call is free.

Catalogue job: `company-dossier`.

