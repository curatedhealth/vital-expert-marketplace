---
name: "DH-03.01.4.2 Coverage Strategy Effectiveness Assessment & Access Rate Monitoring"
description: "Only while the Digital Health Library connector is connected. Run one task in DH-03.01.4.2 Coverage Strategy Effectiveness Assessment & Access Rate Monitoring. Use when the user asks for Access Rate Monitoring, coverage strategy pass rule, coverage strategy miss owner, Find scheme precedents, Watch a scheme, List schemes, Compare schemes. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-03.01.4.2 Coverage Strategy Effectiveness Assessment & Access Rate Monitoring

Heading: DH-03.01.4 Coverage & Access Strategy.
Core: DH-03.01 Market Access & Reimbursement.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-03.01.4.2.1 Access Rate Monitoring

Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 13 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.01.4.2.1 Access Rate Monitoring.
Prompt: PS-DH.03.01.4.2.1 Access Rate Monitoring.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Watch whether coverage strategy is converting into access, and list stalled markets.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Access Rate Monitoring. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound. Not the Market Access roof (`PS-04.02`).

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

### Boundary

Use a status history already retrieved. Do not invent a rate.

## DH-03.01.4.2.2 coverage strategy pass rule

Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 13 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.01.4.2.2 coverage strategy pass rule.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Write the pass rule in the buyer's words.

## DH-03.01.4.2.3 coverage strategy miss owner

Worker: Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`). 13 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.01.4.2.3 coverage strategy miss owner.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a study, a rate, a price, a contract term, or a coverage decision.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Name the owner the buyer named.

## DH-03.01.4.2.4 Find scheme precedents

Worker: not bound.
Skill: CF-12.03.01.4.2.4 Find scheme precedents.
Prompt: not bound.
Template: not bound.
Tool: `market-access-dh.find_scheme_precedents`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Ask for the scheme and the indication. An empty scheme is a gap.

## DH-03.01.4.2.5 Watch a scheme

Worker: not bound.
Skill: CF-12.03.01.4.2.5 Watch a scheme.
Prompt: not bound.
Template: not bound.
Tool: `market-access-dh.watch_scheme`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Call this only when the buyer asks for later changes. One watch per tenant.

## DH-03.01.4.2.6 List schemes

Worker: not bound.
Skill: CF-12.03.01.4.2.6 List schemes.
Prompt: not bound.
Template: not bound.
Tool: `market-access-dh.list_schemes`. This call is not counted. Do not close it with Verify.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

List schemes the connector serves. This call is free. An empty scheme stays empty.

Catalogue job: `scheme-precedents`.

## DH-03.01.4.2.7 Compare schemes

Worker: not bound.
Skill: CF-12.03.01.4.2.7 Compare schemes.
Prompt: not bound.
Template: not bound.
Tool: `market-access-dh.compare_schemes`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Compare one product across registered schemes. A scheme the connector did not check is not assessable.

Catalogue job: `scheme-precedents`.
