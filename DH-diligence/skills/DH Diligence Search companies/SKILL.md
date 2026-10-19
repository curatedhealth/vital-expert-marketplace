---
name: "DH Diligence Search companies"
description: "Only while the Digital Health Library connector is connected. Use only after the job DH Diligence Screen a market is chosen, to do Search companies. Catalogue job market-screen. Tool diligence-dh.search_companies."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH Diligence Search companies

Worker: not bound.
Skill: not a CF-12 row. Library tool `diligence-dh.search_companies`.
Prompt: not bound.
Template: not bound.
Tool: `diligence-dh.search_companies`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Search by name, product, identifier, or segment slug dtx, samd-diagnostic, cdss, rpm. Matching is exact, not semantic.

Catalogue job: `market-screen`.

