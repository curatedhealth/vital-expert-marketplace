---
name: check-a-retraction
description: "Use only after the job Digital Endpoint Capture & RWE Platform Management is chosen, to do Check a retraction."
---

# Check a retraction

## Execution formula
Worker: not bound.
Skill: CF-12.01.02.4.1.8 Check a retraction.
Prompt: not bound.
Template: not bound.
Tool: `literature.check_retraction`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Boundary

Flag a retraction. A clear record is still reported as clear.
