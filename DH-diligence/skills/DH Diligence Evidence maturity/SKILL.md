---
name: "DH Diligence Evidence maturity"
description: "Only while the Digital Health Library connector is connected. Run one task in DH Diligence Evidence maturity. Use when the user asks for Read evidence maturity. Catalogue job evidence-maturity. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH Diligence Evidence maturity

Core: DH Diligence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one.

## Read evidence maturity

Worker: not bound.
Skill: not a CF-12 row. Library tool `diligence-dh.get_evidence_maturity`.
Prompt: not bound.
Template: not bound.
Tool: `diligence-dh.get_evidence_maturity`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

One company. Report the formula, every input, the assessable points, and the dimensions excluded because their source is missing. Do not invent a score.

Catalogue job: `evidence-maturity`.

