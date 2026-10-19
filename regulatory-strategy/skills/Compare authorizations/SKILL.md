---
name: compare-authorizations
description: "Only while the Digital Health Library connector is connected. Use only after the job Global Regulatory Pathway Strategy & Classification Management is chosen, to do Compare authorizations."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Compare authorizations

## Execution formula
Worker: not bound.
Skill: CF-12.03.03.3.1.9 Compare authorizations.
Prompt: not bound.
Template: not bound.
Tool: `regulatory-dh.compare_authorizations`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Boundary

Ask for two to twelve references. A cell the source does not state is not assessable. UK registration and Swiss devices stay a gap. Do not infer a class, a pathway, or a safety count.
