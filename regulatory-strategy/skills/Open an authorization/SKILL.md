---
name: open-an-authorization
description: "Only while the Digital Health Library connector is connected. Use only after the job Global Regulatory Pathway Strategy & Classification Management is chosen, to do Open an authorization."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Open an authorization

## Execution formula
Worker: not bound.
Skill: CF-12.03.03.3.1.8 Open an authorization.
Prompt: not bound.
Template: not bound.
Tool: `regulatory-dh.get_authorization`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Boundary

Ask for one reference: a 510(k), De Novo, or PMA number, a Basic UDI-DI, or an SRN with the trade name. Return the stored fields with their source. A missing record is a gap.
