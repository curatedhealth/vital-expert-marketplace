---
name: "DH-03.01.4.1.8 Retrieve access guidance"
description: "Only while the Digital Health Library connector is connected. Use only after the job DH-03.01.4.1 is chosen, to do Retrieve access guidance. Catalogue job reimbursement-matrix. Tool market-access-dh.retrieve_guidance."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-03.01.4.1.8 Retrieve access guidance

Worker: not bound.
Skill: CF-12.03.01.4.1.8 Retrieve access guidance.
Prompt: not bound.
Template: not bound.
Tool: `market-access-dh.retrieve_guidance`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Use this when the reimbursement rows do not answer the question. A passage the store does not hold is a gap.

Catalogue job: `reimbursement-matrix`.

