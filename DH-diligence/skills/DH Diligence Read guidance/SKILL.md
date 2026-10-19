---
name: "DH Diligence Read guidance"
description: "Only while the Digital Health Library connector is connected. Run one task in DH Diligence Read guidance. Use when the user asks for Read diligence guidance. Catalogue job company-dossier. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH Diligence Read guidance

Core: DH Diligence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one.

## Read diligence guidance

Worker: not bound.
Skill: not a CF-12 row. Library tool `diligence-dh.retrieve_guidance`.
Prompt: not bound.
Template: not bound.
Tool: `diligence-dh.retrieve_guidance`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Guidance passages from the regulatory store. A passage that is not stored is a gap.

Catalogue job: `company-dossier`.

