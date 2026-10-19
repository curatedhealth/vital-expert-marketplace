---
name: "DH-02.01.1.1.5 Read launch readiness"
description: "Only while the Digital Health Library connector is connected. Use only after the job DH-02.01.1.1 is chosen, to do Read launch readiness. Catalogue job competitor-landscape. Tool commercial-dh.get_launch_readiness."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.01.1.1.5 Read launch readiness

Worker: not bound.
Skill: CF-12.02.01.1.1.5 Read launch readiness.
Prompt: not bound.
Template: not bound.
Tool: `commercial-dh.get_launch_readiness`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Seven criteria, each met, attested, or [GAP]. This is a count, not a score. Do not invent a met criterion.

Catalogue job: `competitor-landscape`.

