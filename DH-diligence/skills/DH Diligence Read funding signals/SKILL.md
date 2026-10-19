---
name: "DH Diligence Read funding signals"
description: "Only while the Digital Health Library connector is connected. Use only after the job DH Diligence Company dossier is chosen, to do Read funding signals. Catalogue job company-dossier. Tool diligence-dh.get_funding_signals."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH Diligence Read funding signals

Worker: not bound.
Skill: not a CF-12 row. Library tool `diligence-dh.get_funding_signals`.
Prompt: not bound.
Template: not bound.
Tool: `diligence-dh.get_funding_signals`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Public filings that name the company. An amount the filing does not state stays blank.

Catalogue job: `company-dossier`.

