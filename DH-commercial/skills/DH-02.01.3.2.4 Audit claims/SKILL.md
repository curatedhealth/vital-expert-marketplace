---
name: "DH-02.01.3.2.4 Audit claims"
description: "Only while the Digital Health Library connector is connected. Use only after the job DH-02.01.3.2 is chosen, to do Audit claims. Catalogue job competitor-landscape. Tool commercial-dh.audit_claims."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.01.3.2.4 Audit claims

Worker: not bound.
Skill: CF-12.02.01.3.2.4 Audit claims.
Prompt: not bound.
Template: not bound.
Tool: `commercial-dh.audit_claims`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Label up to 20 claims against the stored intended purpose: matches_record, exceeds_record, or no_authorization_on_record. Do not invent a claim or a purpose.

Catalogue job: `competitor-landscape`.

