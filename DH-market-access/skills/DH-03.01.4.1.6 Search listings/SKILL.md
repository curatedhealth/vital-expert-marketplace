---
name: "DH-03.01.4.1.6 Search listings"
description: "Only while the Digital Health Library connector is connected. Use only after the job DH-03.01.4.1 is chosen, to do Search listings. Catalogue job reimbursement-matrix. Tool market-access-dh.search_listings."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-03.01.4.1.6 Search listings

Worker: not bound.
Skill: CF-12.03.01.4.1.6 Search listings.
Prompt: not bound.
Template: not bound.
Tool: `market-access-dh.search_listings`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Search stored listings by product, manufacturer, scheme, or decision reference. A missing row is a gap.

Catalogue job: `reimbursement-matrix`.

