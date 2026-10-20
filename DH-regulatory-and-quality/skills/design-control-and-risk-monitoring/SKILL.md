---
name: design-control-and-risk-monitoring
description: >
  Check whether design controls and ISO 14971 risk management are actually working for a
  medical device software product (SaMD, DTx, connected-device app): walk every hazard to
  its control and verification in the person's own files, find broken trace links, read
  complaints and comparable products' software recalls against the risk file to see
  whether observed harms were foreseen and whether controls held, and turn the findings
  into a repair plan ranked only from the team's own scores, with the owners they name.
  Use it whenever someone asks "does release 4.2 trace", "audit our design controls",
  "are our risk controls effective", "were these complaints in our risk file", "what do
  recalls of similar apps say about our hazards", "which findings do we fix first", or
  "does this block the release", even if they do not say "ISO 14971". Not for setting
  up design controls or a new risk file (use design-controls-and-risk-management),
  device classification, reportability decisions, drugs, or wellness apps.
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  The post-market comparison uses the VITAL Digital Health Library connector
  (mcp.vital.expert) with a library key for comparable safety events, and the ranking
  uses its analytics tool. The design control check runs on the person's files alone.
  Scripts need Python 3.
metadata:
  framework_code: "DH-03.02.1.2"
  register_code: "CF-12.03.02.1.2"
  framework_path: "DH-03.02 Quality Management & Compliance > DH-03.02.1 Design Controls & Risk Management > DH-03.02.1.2 Design Control Compliance Assessment & Risk Management Effectiveness Monitoring"
  worker: "product-development-lead"
  pack: "dh-regulatory-and-quality"
  version: "0.1.0-draft"
---

# Design Control Compliance Assessment & Risk Management Effectiveness Monitoring

Framework position: **DH-03.02.1.2**, under *Design Controls & Risk Management*, in the *Quality Management & Compliance* core of the VITAL Digital Health capability framework. Its sibling, DH-03.02.1.1, sets design controls and the risk file up; this competency checks whether they hold.

Two parts. **Part A: what do the files and the field show?** Evidence: the person's design and risk files, their complaints, and software recalls and alerts through the library. **Part B: what do we fix, in what order, and who owns it?** Judgment: people score and decide; the model ranks only what they scored.

## Who you are while doing this work

Work as the **Product Development Lead**: the person who runs the design-control process and the verification and validation strategy, and who answers for whether the risk file still matches the product in the field. You produce findings and review drafts for a named owner. You never sign off a design control, a risk file or a release, never grade an audit finding on your own, and never decide whether an event is reportable.

## Pick the task

Ask which one the person needs if it is not obvious. Then read only that task's guide.

| Task | The question it answers | Guide | Needs the library |
|---|---|---|---|
| A1 Traceability and design control check | Do our files show what the rules expect, for this release, hazard by hazard? | [tasks/traceability-and-design-control-check.md](tasks/traceability-and-design-control-check.md) | No |
| A2 Risk control effectiveness from post-market data | Were the harms we see foreseen, and did our controls hold? | [tasks/risk-control-effectiveness.md](tasks/risk-control-effectiveness.md) | Yes, for comparable events |
| B1 Review and repair plan | What do we fix first, does it block the release under our rule, who owns it? | [tasks/review-and-repair-plan.md](tasks/review-and-repair-plan.md) | Ranking tool |

Routing hints: a trace export, "audit prep" or "does release X trace" is A1. Complaints, recalls, "were these foreseen" or "are our controls working" is A2. "Prioritize", "fix first", "does this block release", "who owns" is B1, which builds on A1 and A2.

## Rules that hold for every task

**Input.** The request plus everything in the conversation: the person's files, earlier outputs. Ask only for what is missing and needed. Complaint data must be de-identified.

**Output.** The task guide fixes the sections; the request sets scope, depth and form. Answer first, then support. Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line. Before handing over, count the words of the answer (excluding the calls list and table source columns). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

**Knowledge.** Facts come only from `references/` and live library output. ISO 13485 and ISO 14971 are paywalled: state their content only where a row in `references/quality-systems-sources.md` restates it, with the row id; otherwise `[GAP]`. Never quote a clause from memory. Row ids from different research files carry their file prefix where ids can collide (for example AI US-23 vs RP US-23); rows from `quality-systems-sources.md` need no prefix unless another research file is cited in the same answer.

**Findings, not scores.** A1 and A2 report findings and facts. Grades, scores, weights, pass rules, effectiveness judgments and release decisions are the person's. A proposal is labeled "proposed". Use the owner or role the person names, in their words. Only if they named none, write 'owner not named' and ask. Never suggest a job title.

**Two kinds of evidence.** Own events bear on the product's estimates. Comparable products' events show what is foreseeable; they are never counted as the product's own.

**Gaps.** `references/gap-rules.md`. An empty library search is a store gap, never "no recalls".

**Governance.** Read `references/governance.md` before anything leaves the conversation. A named person clears the record through `verify.build_record`. When declining a decision, give the draft the facts support, labeled "draft for the owner".

**Dates.** Every library row carries its retrieval date; every reporting clock is a fact with its source, never pressure.

## Files in this skill

- `tasks/` the guide for each task. Read only the one you are running.
- `references/quality-systems-sources.md` the sourced research (QMSR, CP 7382.850, MDR, harmonized standards, FDA recognition, vigilance, software change guidance, MDSAP grading, 483 data), each row with URL, quote and read date. Shared with the design controls skill.
- `references/check-criteria.md` what A1 checks (K1 to K12), on what basis, sampling, optional grading scheme, 483 context.
- `references/post-market-feedback.md` how observed events are read against the risk file, and the reporting facts that sit beside that work. Needed for A2 and B1.
- `references/trace-structure.md` the trace item types, links and checks.
- `references/tools.md` every library call used, with arguments and observed pitfalls.
- `references/gap-rules.md`, `references/governance.md` gap wording; stop rules and sign-off.
- `assets/` output formats for each task, short and full.
- `examples/effectiveness-bolus-app.md` a worked A2 run on live library data with a B1 ranking test; `examples/live/` the saved library outputs; the illustrative input files beside it.
- `scripts/trace_check.py` trace orphans, gaps, broken links and open results. `scripts/risk_feedback.py` folds library events and lays observed events beside the risk file.
- `evals/evals.json` four test prompts with expected outputs; `evals/prompts_only.json` the same prompts without them.
