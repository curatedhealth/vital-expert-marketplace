---
name: dh-04-03-3-1-ci-cd-pipeline-management-for-medical-device-softwa
description: "Only while the Digital Health Library connector is connected. Run one task in DH-04.03.3.1 CI/CD Pipeline Management for Medical Device Software. Use when the user asks for Pipeline stages for device software, Evidence the pipeline keeps, Separation of environments. Ask which one task, then follow that section."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# DH-04.03.3.1 CI/CD Pipeline Management for Medical Device Software

Heading: DH-04.03.3 DevOps & Deployment.
Core: DH-04.03 Software Engineering Excellence.

Ask which one task to run. Follow that section only. A missing fact stays [GAP]. Call a library tool only when the section names one. Close a tool task with the Verify calls named in that section.

## DH-04.03.3.1.1 Pipeline stages for device software

Worker: Digital Health Product Manager (`digital-health-product-manager`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.03.3.1.1 Pipeline stages for device software.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.03.3.1. The other skills under this competency do a different job.

### What it does
Name the stages a medical-software change must pass.

### Method
1. List build, automated test, review, and release as they exist today.
2. State which stage is allowed to deploy to production.
3. Mark a stage that is skipped for hotfixes.

### Do not
Do not describe a pipeline the repository does not run.

### Output
A stage list, including the hotfix exception.

A missing fact stays [GAP].

## DH-04.03.3.1.2 Evidence the pipeline keeps

Worker: Digital Health Product Manager (`digital-health-product-manager`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.03.3.1.2 Evidence the pipeline keeps.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.03.3.1. The other skills under this competency do a different job.

### What it does
Say what record remains after a release.

### Method
1. Name the artifacts kept (test report, review, build id, SBOM if one is produced).
2. State where they are stored and for how long.
3. Mark a missing artifact as [GAP].

### Do not
Do not claim an SBOM or a signed build if the pipeline does not produce it.

### Output
A retention list of release evidence.

A missing fact stays [GAP].

## DH-04.03.3.1.3 Separation of environments

Worker: Digital Health Product Manager (`digital-health-product-manager`). 2 workers are bound to this skill. This run uses this one.
Skill: CF-12.04.03.3.1.3 Separation of environments.
Prompt: not bound.
Template: not bound.
Tool: not bound. Do not invent a fact the source does not state.
Input: use the inputs named in the prompt. A missing input stays blank.

Follow the prompt when one is bound, and put the answer in the template when one is bound. Call the tool only when this formula names one.

One skill under CF-12.04.03.3.1. The other skills under this competency do a different job.

### What it does
Keep production data out of the stages that do not need it.

### Method
1. State which stages can reach production.
2. State how test data is produced for the earlier stages.
3. Name any job that copies production data, and the control on that copy.

### Do not
Do not use production patient data as the default fixture.

### Output
An environment note: who can deploy, and where test data comes from.

A missing fact stays [GAP].
