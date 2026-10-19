---
name: "DH-02.01.3.2 Pricing Effectiveness Assessment & Value Message Impact Monitoring"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-02.01.3.2 Pricing Effectiveness Assessment & Value Message Impact Monitoring. Use when the user asks for Price outcome definition, Realized price score, Price miss owner, Audit claims. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-02.01.3.2 Pricing Effectiveness Assessment & Value Message Impact Monitoring

Heading: DH-02.01.3 Pricing & Value Communication.
Core: DH-02.01 Commercial & GTM Strategy.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-02.01.3.2.1 Price outcome definition

Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.01.3.2.1 Price outcome definition.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.01.3.2. The other skills under this competency do a different job.

### What it does
Define which deals count toward a pricing judgment.

### Method
1. Name the period and the deal types (new, renewal, pilot).
2. Define realized price as the contracted unit price, not the list price.
3. Exclude deals whose unit is not the value unit.

### Do not
Do not average list price and realized price together.

### Output
A deal definition and the realized-price rule.

A missing fact stays [GAP].

## DH-02.01.3.2.2 Realized price score

Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.01.3.2.2 Realized price score.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.01.3.2. The other skills under this competency do a different job.

### What it does
Score realized prices against the corridor.

### Method
1. List deals in the period with unit price and currency.
2. Mark each deal inside, below, or above the corridor.
3. Keep the contract id.

### Do not
Do not drop a deal because it was discounted.

### Output
A deal score with contract ids.

A missing fact stays [GAP].

## DH-02.01.3.2.3 Price miss owner

Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.02.01.3.2.3 Price miss owner.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.02.01.3.2. The other skills under this competency do a different job.

### What it does
Assign deals outside the corridor.

### Method
1. Name whether the corridor or the deal is wrong.
2. Name the owner (access, sales, or finance).
3. State the next deal that should use the corrected rule.

### Do not
Do not treat every discount as a failure of the corridor.

### Output
An owner and a next deal per miss.

A missing fact stays [GAP].

## DH-02.01.3.2.4 Audit claims

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
