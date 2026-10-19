---
name: "DH Diligence Compare a portfolio"
description: "Only while the Digital Health Library connector is connected. Run one task in DH Diligence Compare a portfolio. Use when the user asks for Compare a portfolio. Catalogue job portfolio-comparison. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH Diligence Compare a portfolio

Core: DH Diligence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one.

## Compare a portfolio

Worker: not bound.
Skill: not a CF-12 row. Library tool `diligence-dh.compare_portfolio`.
Prompt: not bound.
Template: not bound.
Tool: `diligence-dh.compare_portfolio`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Compare 2 to 12 companies the buyer names. A company the store does not hold is a gap.

Catalogue job: `portfolio-comparison`.

