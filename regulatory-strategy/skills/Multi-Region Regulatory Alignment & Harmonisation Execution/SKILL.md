---
name: multi-region-regulatory-alignment-and-harmonisation-execution
description: "Only while the Digital Health Library connector is connected. Start the job Multi-Region Regulatory Alignment & Harmonisation Execution in Regulatory Strategy & Submissions. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Multi-Region Regulatory Alignment & Harmonisation Execution

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- Cross-Jurisdiction Requirement Mapping. Skill `cross-jurisdiction-requirement-mapping`. Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 15 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.03.2.1.1 Cross-Jurisdiction Requirement Mapping. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Harmonised Evidence Planning. Skill `harmonised-evidence-planning`. Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 29 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.03.2.1.2 Harmonised Evidence Planning. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Regional Submission Adaptation. Skill `regional-submission-adaptation`. Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 15 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.03.2.1.3 Regional Submission Adaptation. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.

- List jurisdictions. Skill `list-jurisdictions`. Worker: not bound. Prompt: not bound. Template: not bound. Tool: `regulatory-dh.list_jurisdictions`.
Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
