---
name: "DH Diligence Generate a company report"
description: "Only while the Digital Health Library connector is connected. Use only after the job DH Diligence Company dossier is chosen, to do Generate a company report. Catalogue job company-dossier. Tool diligence-dh.generate_report."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH Diligence Generate a company report

Worker: not bound.
Skill: not a CF-12 row. Library tool `diligence-dh.generate_report`.
Prompt: not bound.
Template: not bound.
Tool: `diligence-dh.generate_report`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Cite-bound dossier from stored rows. template is memo, identity, regulatory, or evidence. Do not invent a filing.

Catalogue job: `company-dossier`.

