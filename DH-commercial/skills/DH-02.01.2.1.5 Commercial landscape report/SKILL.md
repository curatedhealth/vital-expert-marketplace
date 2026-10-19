---
name: "DH-02.01.2.1.5 Commercial landscape report"
description: "Only while the Digital Health Library connector is connected. Use only after the job DH-02.01.2.1 is chosen, to do Commercial landscape report. Catalogue job competitor-landscape. Tool commercial-dh.generate_report."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.01.2.1.5 Commercial landscape report

Worker: not bound.
Skill: CF-12.02.01.2.1.5 Commercial landscape report.
Prompt: not bound.
Template: not bound.
Tool: `commercial-dh.generate_report`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Render the public report from sections already held. Templates are memo, identity, regulatory, reimbursement, or commercial. Do not treat it as a regulatory opinion.

Catalogue job: `competitor-landscape`.

