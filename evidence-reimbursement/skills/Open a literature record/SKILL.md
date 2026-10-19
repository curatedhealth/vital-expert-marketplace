---
name: open-a-literature-record
description: "Use only after the job Digital Endpoint Capture & RWE Platform Management is chosen, to do Open a literature record."
---

# Open a literature record

## Execution formula
Worker: not bound.
Skill: CF-12.01.02.4.1.5 Open a literature record.
Prompt: not bound.
Template: not bound.
Tool: `literature.get_record`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Boundary

Open one hit the search already returned.
