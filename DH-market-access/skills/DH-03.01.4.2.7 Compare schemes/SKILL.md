---
name: "DH-03.01.4.2.7 Compare schemes"
description: "Only while the Digital Health Library connector is connected. Use only after the job DH-03.01.4.2 is chosen, to do Compare schemes. Catalogue job scheme-precedents. Tool market-access-dh.compare_schemes."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-03.01.4.2.7 Compare schemes

Worker: not bound.
Skill: CF-12.03.01.4.2.7 Compare schemes.
Prompt: not bound.
Template: not bound.
Tool: `market-access-dh.compare_schemes`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Compare one product across registered schemes. A scheme the connector did not check is not assessable.

Catalogue job: `scheme-precedents`.

