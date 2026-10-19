---
name: cf-12-01-02-4-1
description: "Start the job Digital Endpoint Capture and RWE Platform Management (CF-12.01.02.4.1) in Clinical Validation and Evidence. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

# Digital Endpoint Capture and RWE Platform Management

Code: CF-12.01.02.4.1. Mission: CF-12.01.02.4.

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- Digital Endpoint Instrumentation. Skill `cf-12-01-02-4-1-1`. Worker: Clinical Informatics Lead (`clinical-informatics-lead`). 30 workers are bound to this skill. This run uses this one. Prompt: PS-DH.01.02.4.1.1 Digital Endpoint Instrumentation. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- RWE Data Pipeline Management. Skill `cf-12-01-02-4-1-2`. Worker: AI/ML Governance Director (`ai-ml-governance-director`). 32 workers are bound to this skill. This run uses this one. Prompt: PS-DH.01.02.4.1.2 RWE Data Pipeline Management. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Signal Detection Analysis. Skill `cf-12-01-02-4-1-3`. Worker: AI/ML Governance Director (`ai-ml-governance-director`). 30 workers are bound to this skill. This run uses this one. Prompt: PS-DH.01.02.4.1.3 Signal Detection Analysis. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Search literature. Skill `cf-12-01-02-4-1-4`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `literature.search_literature`.
- Open a literature record. Skill `cf-12-01-02-4-1-5`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `literature.get_record`.
- Link a trial. Skill `cf-12-01-02-4-1-6`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `literature.find_trial`.
- Grade evidence. Skill `cf-12-01-02-4-1-7`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `literature.grade_evidence`.
- Check a retraction. Skill `cf-12-01-02-4-1-8`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `literature.check_retraction`.
- Build an evidence table. Skill `cf-12-01-02-4-1-9`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `literature.build_evidence_table`.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
