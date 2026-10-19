---
name: "Regulatory Strategy Effectiveness Assessment & Pathway Success Monitoring"
description: "Only while the Digital Health Library connector is connected. Run one task in 03.03.3.2 Regulatory Strategy Effectiveness Assessment & Pathway Success Monitoring. Use when the user asks for Regulatory Pathway Success Monitoring, regulatory pathway pass rule, regulatory pathway miss owner, Watch a register, Search safety events, Read register changes. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# 03.03.3.2 Regulatory Strategy Effectiveness Assessment & Pathway Success Monitoring

Heading: 03.03.3 Regulatory Strategy.
Core: DH-03.03 Regulatory Strategy & Submissions.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## 03.03.3.2.1 Regulatory Pathway Success Monitoring

Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 20 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.03.3.2.1 Regulatory Pathway Success Monitoring.
Prompt: PS-DH.03.03.3.2.1 Regulatory Pathway Success Monitoring.
Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay.
Tool: not bound. Do not invent a class, a pathway, a predicate, a recall, or an authorization.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Prompt

### Task
Watch whether the chosen pathway is still the right one, and list classification risk.

### Inputs
- The in-scope Digital Health question, product, market or regulator if named, and any source the operator already has.

### Output
A bounded draft for Regulatory Pathway Success Monitoring. Mark unresolved facts `[GAP]`.

### Guardrails
No invented evidence, prices, or coverage claims. `[GAP]` when inputs are missing. No off-label instruction. SaMD, DTx, payer, and HTA claims stay evidence-bound.

### Template

### Digital Health overlay

Shared rendering overlay for the Digital Health & Software-Driven Care domain (CF-12). SaMD / DTx / digital-care deliverables render through the D40 shared capability, with domain standards in force: IMDRF SaMD framework, FDA AI/ML SaMD Action Plan (PCCP), EU MDR 2017/745, Germany DVG/DiGA (BfArM), WHO Classification of Digital Health Interventions.

## 03.03.3.2.2 regulatory pathway pass rule

Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 20 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.03.3.2.2 regulatory pathway pass rule.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a class, a pathway, a predicate, a recall, or an authorization.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## 03.03.3.2.3 regulatory pathway miss owner

Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 20 workers are bound to this skill. This run uses this one.
Skill: CF-12.03.03.3.2.3 regulatory pathway miss owner.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a class, a pathway, a predicate, a recall, or an authorization.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

## 03.03.3.2.4 Watch a register

Worker: not bound.
Skill: CF-12.03.03.3.2.4 Watch a register.
Prompt: not bound.
Template: not bound.
Tool: `regulatory-dh.watch_register`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Ask for the product code, the manufacturer, or the EMDN code. One watch per tenant. Call this only when the buyer wants later changes.

## 03.03.3.2.5 Search safety events

Worker: not bound.
Skill: CF-12.03.03.3.2.5 Search safety events.
Prompt: not bound.
Template: not bound.
Tool: `regulatory-dh.search_safety_events`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Ask for the product code, the manufacturer, or the EMDN code. A missing recall or MAUDE row is a gap.

## 03.03.3.2.6 Read register changes

Worker: not bound.
Skill: CF-12.03.03.3.2.6 Read register changes.
Prompt: not bound.
Template: not bound.
Tool: `regulatory-dh.get_register_deltas`. Then close with Verify: verify.extract_claims, verify.check_claim, verify.verify_text, verify.qualify_source, verify.check_currency, verify.build_citation, verify.build_record.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

### Boundary

Ask for the same subject as the watch, and a since date. An empty log means no change recorded. `regulatory-dh.get_deltas` is this same tool. Call one of them, not both.
