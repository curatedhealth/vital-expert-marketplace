---
name: "DH-02.01.3.1.4 Map the money flow"
description: "Only while the Digital Health Library connector is connected. Use only after the job DH-02.01.3.1 is chosen, to do Map the money flow. Catalogue job competitor-landscape. Tool commercial-dh.map_money_flow."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.01.3.1.4 Map the money flow

Worker: not bound.
Skill: CF-12.02.01.3.1.4 Map the money flow.
Prompt: not bound.
Template: not bound.
Tool: `commercial-dh.map_money_flow`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Ask for user, buyer, and payer as three roles. An unnamed role is [GAP]. Do not invent a contract term.

Catalogue job: `competitor-landscape`.

