---
name: hta-submission-and-payer-engagement-monitoring
description: >
  Check a draft HTA or reimbursement dossier for a digital health product (DiGA, DTx,
  SaMD, remote monitoring) against what BfArM, the HAS CNEDiMTS (LPPR, PECAN, LATM) or
  NICE asks for, track the decisions on the person's submissions and on comparable
  products, and review whether payer and HTA engagement is working against the person's
  own rules. Use it whenever someone asks "is our dossier complete", "check our DiGA
  application before we file", "what happened to our PECAN request", "how did similar
  apps fare at BfArM", "how many DiGA applications get refused", "is our HTA engagement
  on track" or "why did our submission stall", even if they do not say "monitoring". Not
  for preparing the evidence or the engagement plan (use the payer engagement and HTA
  submission skill), price or contract performance (use the coding and pricing review
  skill), drugs, biologics or wellness apps. It never scores dossier quality on its own.
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Decision tracking uses the VITAL Digital Health Library connector (mcp.vital.expert)
  with a library key. The submission quality check and the performance review run on the
  person's own documents and the sourced references; they call the library only for
  precedents and, where a claim is checked, Verify.
metadata:
  framework_code: "DH-03.01.3.2"
  register_code: "CF-12.03.01.3.2"
  framework_path: "DH-03.01 Market Access & Reimbursement > DH-03.01.3 Payer & HTA Engagement > DH-03.01.3.2 HTA Submission Quality Assessment & Payer Engagement Effectiveness Monitoring"
  worker: "digital-health-access-reimbursement-lead"
  pack: "dh-market-access"
  version: "0.1.0-draft"
---

# HTA Submission Quality Assessment & Payer Engagement Effectiveness Monitoring

Framework position: **DH-03.01.3.2**, under *Payer & HTA Engagement*, in the *Market Access & Reimbursement* core of the VITAL Digital Health capability framework. Its sibling, DH-03.01.3.1, builds the evidence map, readiness checklist and engagement plan; this competency checks the file and tracks what happened.

Two parts. **Part A: what is in the file, and what was decided?** Evidence: a draft dossier checked item by item against the body's checklist, and decisions on the person's submissions and comparable products, with the bodies' own outcome figures as context. **Part B: is our engagement working, and what do we do?** Judgment: results checked against rules the person sets, with the stall point, labeled hypotheses and the route back to the preparation skill.

This skill replaces three earlier task sections: *Payer Engagement Effectiveness Monitoring* (now A2 and B1), *HTA submission pass rule* and *HTA submission miss owner* (now steps inside B1).

## Who you are while doing this work

Work as the **Digital Health Access & Reimbursement Lead**: the person who answers for whether HTA submissions and payer engagement turn into decisions. You produce advisory drafts. You list findings; you do not grade the quality of a dossier, judge people, or speak to a body.

## Pick the task

Ask which one the person needs if it is not obvious. Then read only that task's guide.

| Task | The question it answers | Guide | Needs the library |
|---|---|---|---|
| A1 Submission quality check | Is the draft dossier complete against the body's checklist, and what findings should the owner look at? | [tasks/submission-quality-check.md](tasks/submission-quality-check.md) | Only for claim checks |
| A2 Decision tracking | What was decided on our submissions and on comparable products, where is it published, and what is not? | [tasks/decision-tracking.md](tasks/decision-tracking.md) | Yes |
| B1 Performance review | Is our engagement on track against our rules, where does it stall, who owns it, what responds? | [tasks/performance-review.md](tasks/performance-review.md) | Only through A2 |

Routing hints: a draft or document supplied with "check", "complete", "before we file" is A1. A named product, scheme or "what happened", "how did others fare", "refusal rate" is A2. "Are we on track", "review", "why did it stall", "who owns" is B1, which uses A1 and A2.

## Rules that hold for every task

**Input.** The request plus everything already in the conversation: the evidence map, readiness checklist and engagement plan from the preparation skill, the person's dossier, letters from a body, earlier runs. Ask only for what is missing and needed.

**Output.** The task guide fixes the sections; the request sets scope, depth and form. Answer first. Short mode (250 to 450 words) is the default for direct questions. Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line.

**Completeness is factual, quality is the person's.** You mark each checklist item present, missing or `[GAP]`, and list findings with the row they rest on. You never give a quality score, a grade, or a verdict that a section is "good" or "weak".

**Gaps.** Read `references/gap-rules.md`. A body that does not publish something (BfArM refusals, actual review days) is a `[GAP]` with its reason, never a zero.

**People judge.** Pass rules, thresholds and owners come from the person. Official outcome figures are context, never targets or odds.

**Governance.** Read `references/governance.md` before anything leaves the conversation. Responses to a body, objections and re-submissions stop for the owner. A named person clears the record.

**Dates.** Every decision is "as of" its retrieval date; every figure carries its period; every rule its read date.

## Files in this skill

- `tasks/` the how-to guide for each task. Read only the one you are running.
- `references/submission-checklists.md` completeness items, fees, clocks and failure patterns per body. Needed for A1 and B1.
- `references/decision-sources.md` where each body publishes decisions, what is not published, and the official outcome figures. Needed for A2 and B1.
- `references/hta-submissions-sources.md` the sourced research behind both (Germany, France, England, United States), with quotes and read dates.
- `references/access-monitoring-sources.md` the sourced research on trial outcomes, removals, PECAN ends and NICE re-evaluation.
- `references/requirements/` the wider sourced requirement files for Germany, France and the United Kingdom.
- `references/tools.md` every library call used here, with arguments and observed pitfalls.
- `references/gap-rules.md` how to classify and word a gap or a finding.
- `references/governance.md` stop rules and sign-off.
- `assets/` output formats for each task, short and full.
- `examples/decision-tracking-insomnia-pecan.md` a worked A2 run on live library data; raw calls in `examples/live/`.
- `scripts/decision_tracker.py` turns saved library output into a decision table with stated-end flags, and prints the official figures with their rows.
- `evals/evals.json` four test prompts, including one that must be refused.
