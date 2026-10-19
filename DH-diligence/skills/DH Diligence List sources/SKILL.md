---
name: "DH Diligence List sources"
description: "Only while the Digital Health Library connector is connected. Run one task in DH Diligence List sources. Use when the user asks for List diligence sources. Catalogue job company-dossier. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH Diligence List sources

Core: DH Diligence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one.

## List diligence sources

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

