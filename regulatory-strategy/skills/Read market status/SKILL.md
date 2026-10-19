---
name: read-market-status
description: "Only while the Digital Health Library connector is connected. Use only after the job Global Regulatory Pathway Strategy & Classification Management is chosen, to do Read market status."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Read market status

## Execution formula
Worker: not bound.
Skill: CF-12.03.03.3.1.10 Read market status.
Prompt: not bound.
Template: not bound.
Tool: `regulatory-dh.get_market_status`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Boundary

Ask for the product name or one reference. This task is where the product is authorized. Reimbursement fields from this tool stay a gap.
