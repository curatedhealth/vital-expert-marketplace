---
name: "DH-02.01.2.1.4 Screen commercial peers"
description: "Only while the Digital Health Library connector is connected. Use only after the job DH-02.01.2.1 is chosen, to do Screen commercial peers. Catalogue job competitor-landscape. Tool commercial-dh.screen_commercial_peers."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.01.2.1.4 Screen commercial peers

Worker: not bound.
Skill: CF-12.02.01.2.1.4 Screen commercial peers.
Prompt: not bound.
Template: not bound.
Tool: `commercial-dh.screen_commercial_peers`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Ask for a segment. Limit is 1 to 25. Coverage names which of the three feeds answered. A peer a feed did not return is a gap.

Catalogue job: `competitor-landscape`.

