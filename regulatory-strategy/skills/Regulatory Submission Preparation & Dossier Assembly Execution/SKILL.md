---
name: regulatory-submission-preparation-and-dossier-assembly-execution
description: "Only while the Digital Health Library connector is connected. Start the job Regulatory Submission Preparation & Dossier Assembly Execution in Regulatory Strategy & Submissions. Use when the user asks for this job. It lists the tasks and loads one task skill."
---

If the Digital Health Library connector is not connected, stop. Do not use this skill and do not answer from this pack.

# Regulatory Submission Preparation & Dossier Assembly Execution

Ask which one task to run, then load that task skill. Do not run every task.

The task skill carries the worker, the prompt, the template, and the tool. Follow that prompt and render that template.

- Clinical Evaluation Report Assembly. Skill `clinical-evaluation-report-assembly`. Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 24 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.03.4.1.1 Clinical Evaluation Report Assembly. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Submission Dossier Compilation. Skill `submission-dossier-compilation`. Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 20 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.03.4.1.2 Submission Dossier Compilation. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.
- Agency Interaction Management. Skill `agency-interaction-management`. Worker: SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`). 20 workers are bound to this skill. This run uses this one. Prompt: PS-DH.03.03.4.1.3 Agency Interaction Management. Template: ST05-PHARMA-DH-OVERLAY Digital Health overlay. Tool: not bound.

Call a connector tool only when the chosen task names one. Stay inside this pack's tools.
