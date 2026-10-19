---
name: "DH Diligence Company dossier"
description: "Only while the Digital Health Library connector is connected. Run one task in DH Diligence Company dossier. Use when the user asks for Build a company profile, Read funding signals, Generate a company report. Catalogue job company-dossier. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH Diligence Company dossier

Core: DH Diligence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one.

## Build a company profile

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

## Read funding signals

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

## Generate a company report

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

