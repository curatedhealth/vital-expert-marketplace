---
name: "DH Diligence Screen a market"
description: "Only while the Digital Health Library connector is connected. Run one task in DH Diligence Screen a market. Use when the user asks for Screen a market, Search companies. Catalogue job market-screen. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH Diligence Screen a market

Core: DH Diligence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one.

## Screen a market

Worker: not bound.
Skill: not a CF-12 row. Library tool `diligence-dh.screen_market`.
Prompt: not bound.
Template: not bound.
Tool: `diligence-dh.screen_market`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Segment, jurisdiction (US, EU, UK, CH), and a minimum evidence maturity the buyer supplies. Rank only by those criteria.

Catalogue job: `market-screen`.

## Search companies

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

