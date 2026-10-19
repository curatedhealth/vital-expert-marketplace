---
name: "Evidence and Reimbursement"
description: "Only while the Digital Health Library connector is connected. List the Evidence and Reimbursement pack. Use when the user asks what this pack can do, or mentions evidence, reimbursement, a payer, a model, or a digital health expert, and has not chosen a core or the expert download."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Evidence and Reimbursement

One pack. One connector: the Digital Health Library. Show this list when the buyer has not chosen a core.

## DH-01.02 Clinical Validation & Evidence
Skill `clinical-validation-and-evidence`. Studies, evidence communication, trial operations, and the evidence table.

## DH-01.07 Health Economics & Value Demonstration
Skill `health-economics-and-value-demonstration`. Access support, economic models, the budget impact model, the launch price anchor, outcomes research, and value communication.

## DH-03.01 Market Access & Reimbursement
Skill `DH-03.01 Market Access & Reimbursement`. Value-based contracts, coding and pricing, payer and HTA engagement, and coverage.

## Experts
- Download a digital health expert. Skill `download-a-digital-health-expert`.

Choosing Clinical Validation or Health Economics loads that core's jobs, then one task skill. Choosing Market Access loads a heading, then one job. That job runs one task section. Choosing the expert job finds one expert and downloads that file. A task calls a library tool only when that task names one.
