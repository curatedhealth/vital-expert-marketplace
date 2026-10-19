---
name: "DH Diligence Watch companies"
description: "Only while the Digital Health Library connector is connected. Run one task in DH Diligence Watch companies. Use when the user asks for Watch companies, Read company changes. Catalogue job market-screen. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH Diligence Watch companies

Core: DH Diligence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one.

## Watch companies

Worker: not bound.
Skill: not a CF-12 row. Library tool `diligence-dh.watch_companies`.
Prompt: not bound.
Template: not bound.
Tool: `diligence-dh.watch_companies`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Register a watch on 1 to 12 companies and return the snapshot hash. since is ignored on the write. One watch per tenant.

Catalogue job: `market-screen`.

## Read company changes

Worker: not bound.
Skill: not a CF-12 row. Library tool `diligence-dh.get_deltas`.
Prompt: not bound.
Template: not bound.
Tool: `diligence-dh.get_deltas`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

What the store recorded for the watch since a date. State when the watch has no later sweep. Do not invent an event.

Catalogue job: `market-screen`.

