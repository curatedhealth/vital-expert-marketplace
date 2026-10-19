---
name: dh-04-03-3-2-devops-effectiveness-assessment-deployment-quality
description: "Only while the Digital Health Library connector is connected. Run one task in DH-04.03.3.2 DevOps Effectiveness Assessment & Deployment Quality Monitoring. Use when the user asks for Deploy frequency and failure, Skipped stage check, Pipeline change owner. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-04.03.3.2 DevOps Effectiveness Assessment & Deployment Quality Monitoring

Heading: DH-04.03.3 DevOps & Deployment.
Core: DH-04.03 Software Engineering Excellence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-04.03.3.2.1 Deploy frequency and failure

Worker: Digital Health Product Manager (`digital-health-product-manager`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.03.3.2.1 Deploy frequency and failure.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.03.3.2. The other skills under this competency do a different job.

### What it does
Measure how often a deploy fails or is rolled back.

### Method
1. Count deploys and rollbacks over a stated period.
2. Separate a failed health check from a reverted clinical defect.
3. Name the stage that caught the failure, or say it was caught in production.

### Do not
Do not report a green dashboard as zero failures.

### Output
A count for the period, split by where the failure was caught.

A missing fact stays [GAP].

## DH-04.03.3.2.2 Skipped stage check

Worker: Digital Health Product Manager (`digital-health-product-manager`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.03.3.2.2 Skipped stage check.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.03.3.2. The other skills under this competency do a different job.

### What it does
Find releases that skipped a stage the policy requires.

### Method
1. Compare release records with the stage list.
2. List releases that used the hotfix exception.
3. State whether the exception was recorded at the time.

### Do not
Do not treat an unrecorded skip as a hotfix.

### Output
A list of skips, recorded or not.

A missing fact stays [GAP].

## DH-04.03.3.2.3 Pipeline change owner

Worker: Digital Health Product Manager (`digital-health-product-manager`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.03.3.2.3 Pipeline change owner.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.03.3.2. The other skills under this competency do a different job.

### What it does
Assign the stage that is failing or being skipped.

### Method
1. Name the owner of that stage.
2. State the change (restore a test, stop an unrecorded skip).
3. Name the next release that should show the change.

### Do not
Do not assign the whole platform team.

### Output
One stage, one owner, one release.

A missing fact stays [GAP].
