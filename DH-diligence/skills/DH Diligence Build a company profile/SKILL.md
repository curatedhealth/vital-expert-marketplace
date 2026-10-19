---
name: "DH Diligence Build a company profile"
description: "Only while the Digital Health Library connector is connected. Use only after the job DH Diligence Company dossier is chosen, to do Build a company profile. Catalogue job company-dossier. Tool diligence-dh.build_company_profile."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH Diligence Build a company profile

Worker: not bound.
Skill: not a CF-12 row. Library tool `diligence-dh.build_company_profile`.
Prompt: not bound.
Template: not bound.
Tool: `diligence-dh.build_company_profile`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Ask for one company reference: legal name, brand, submission number, LEI, EUDAMED, or SEC filer. Matching is exact. A near spelling is only a labeled proposal. Anything not loaded is [GAP].

Catalogue job: `company-dossier`.

