---
name: "DH-02.01.1.1.6 Commercial brief"
description: "Only while the Digital Health Library connector is connected. Use only after the job DH-02.01.1.1 is chosen, to do Commercial brief. Catalogue job competitor-landscape. Tool commercial-dh.generate_commercial_brief."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.01.1.1.6 Commercial brief

Worker: not bound.
Skill: CF-12.02.01.1.1.6 Commercial brief.
Prompt: not bound.
Template: not bound.
Tool: `commercial-dh.generate_commercial_brief`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Same arguments as the commercial report, template memo. The first line states it is not a regulatory opinion.

Catalogue job: `competitor-landscape`.

