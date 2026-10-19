---
name: search-literature
description: "Only while the Digital Health Library connector is connected. Use only after the job Digital Endpoint Capture & RWE Platform Management is chosen, to do Search literature."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Search literature

## Execution formula
Worker: not bound.
Skill: CF-12.01.02.4.1.4 Search literature.
Prompt: not bound.
Template: not bound.
Tool: `literature.search_literature`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## Boundary

Ask for the claim or the product. Unpublished data stays a gap.
