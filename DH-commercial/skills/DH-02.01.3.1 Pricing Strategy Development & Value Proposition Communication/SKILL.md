---
name: "DH-02.01.3.1 Pricing Strategy Development & Value Proposition Communication"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-02.01.3.1 Pricing Strategy Development & Value Proposition Communication. Use when the user asks for Value unit, Price corridor, Value message, Map the money flow, Read the pricing corridor. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.01.3.1 Pricing Strategy Development & Value Proposition Communication

Heading: DH-02.01.3 Pricing & Value Communication.
Core: DH-02.01 Commercial & GTM Strategy.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-02.01.3.1.1 Value unit

Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.01.3.1.1 Value unit.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.01.3.1. The other skills under this competency do a different job.

### What it does
Name the unit the price is attached to.

### Method
1. State the unit (patient-month, site, module, outcome).
2. State what the buyer receives for that unit.
3. State what is excluded from the unit.

### Do not
Do not price a unit you cannot describe.

### Output
One value unit and its exclusions.

A missing fact stays [GAP].

## DH-02.01.3.1.2 Price corridor

Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.01.3.1.2 Price corridor.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.01.3.1. The other skills under this competency do a different job.

### What it does
Set the price corridor and the reason for each end.

### Method
1. Name the floor and the ceiling, with currency.
2. Tie the floor to cost or to the smallest comparators you will name.
3. Tie the ceiling to the outcome or the budget you will cite, or mark it [GAP].

### Do not
Do not publish a single price with no corridor when the buyer set differs.

### Output
A corridor with the reason for each end.

A missing fact stays [GAP].

## DH-02.01.3.1.3 Value message

Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.01.3.1.3 Value message.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.01.3.1. The other skills under this competency do a different job.

### What it does
Write the message that explains the price.

### Method
1. Write the message for the access audience and the message for the economic buyer, if they differ.
2. Use only outcomes you can point to.
3. Mark an outcome you cannot point to as [GAP] rather than a number.

### Do not
Do not put a clinical claim in the price message that is not on the claim list.

### Output
The message, the audience, and the outcomes it uses.

A missing fact stays [GAP].

## DH-02.01.3.1.4 Map the money flow

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

## DH-02.01.3.1.5 Read the pricing corridor

Worker: not bound.
Skill: CF-12.02.01.3.1.5 Read the pricing corridor.
Prompt: not bound.
Template: not bound.
Tool: `commercial-dh.get_pricing_corridor`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Public prices already inside stored reimbursement or listing rows. No row means [GAP]. Do not invent a price.

Catalogue job: `competitor-landscape`.
