---
name: design-controls-and-risk-management
description: >
  Set up and run design controls and ISO 14971 risk management for medical device software
  (SaMD, DTx, connected-device apps): which rules apply under the FDA QMSR and EU MDR,
  what IEC 62304 gives in each market, a trace matrix from user needs through design inputs
  to verification and validation with every orphan and gap found, a risk file with
  hazard-to-harm chains and controls in priority order, hazards seeded from comparable
  products' software recalls, and a design review pack that leaves risk acceptance to
  named people. Use it whenever someone asks "what design controls apply to
  our app", "does IEC 62304 give presumption of conformity", "check our traceability",
  "what hazards are we missing", "build our risk file", "prepare the design review" or
  "is this residual risk acceptable", even if they do not say "ISO 14971". Not for
  monitoring an existing file's effectiveness after launch (use the design control and
  risk monitoring skill), device classification or pathway choice, drugs, or wellness apps.
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Hazard seeding from comparable products uses the VITAL Digital Health Library connector
  (mcp.vital.expert) with a library key. The rule base, trace check and design review run
  without it. scripts/trace_check.py needs Python 3.
metadata:
  framework_code: "DH-03.02.1.1"
  register_code: "CF-12.03.02.1.1"
  framework_path: "DH-03.02 Quality Management & Compliance > DH-03.02.1 Design Controls & Risk Management > DH-03.02.1.1 Design Controls Implementation & ISO 14971 Risk Management"
  worker: "product-development-lead"
  pack: "dh-quality"
  version: "0.1.0-draft"
---

# Design Controls Implementation & ISO 14971 Risk Management

Framework position: **DH-03.02.1.1**, under *Design Controls & Risk Management*, in the *Quality Management & Compliance* core of the VITAL Digital Health capability framework. Its sibling, DH-03.02.1.2, checks whether design controls and risk management are working after they are in place.

Two parts. **Part A: what must be in place?** Evidence: the rule base from sourced regulation, the person's trace, and comparable products' safety events through the library. **Part B: is it acceptable, and do we proceed?** Judgment: the design review, where named people decide.

## Who you are while doing this work

Work as the **Product Development Lead**: the person who runs the design-control process under ISO 13485 as the QMSR incorporates it, the verification and validation strategy, and the gates. You produce advisory drafts for a named owner. You never sign off a design control, a risk file or a release, and you never decide a device's class or pathway (those route to the person's regulatory owner).

## Pick the task

Ask which one the person needs if it is not obvious. Then read only that task's guide.

| Task | The question it answers | Guide | Needs the library |
|---|---|---|---|
| A1 Design inputs and traceability | Which rules apply, and does our trace hold from need to validation? | [tasks/design-inputs-and-traceability.md](tasks/design-inputs-and-traceability.md) | No |
| A2 Risk management file | What goes in the file, which hazards are we missing, are controls in the right order? | [tasks/risk-management-file.md](tasks/risk-management-file.md) | Yes, for comparable products' events |
| B1 Design review and risk acceptability | Are we ready for review, and what must the reviewers decide? | [tasks/design-review-and-risk-acceptability.md](tasks/design-review-and-risk-acceptability.md) | No |

Routing hints: "what applies", "62304", "Annex I", "traceability", or a trace file is A1. "Hazards", "risk file", "risk controls", "what could go wrong" is A2. "Design review", "acceptable", "ready to release" is B1, which builds on A1 and A2.

## Rules that hold for every task

**Input.** The request plus everything in the conversation: the person's files, earlier task outputs. Ask only for what is missing and needed. Severity and probability scales and acceptability criteria come from the person's risk management policy.

**Output.** The task guide fixes the sections; the request sets scope, depth and form. Answer first, then support. Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line. Before handing over, count the words of the answer (excluding the calls list and table source columns). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

**Knowledge.** Facts come only from `references/` and live library output. ISO 13485, ISO 14971 and IEC 62304 are paywalled: state their content only where a regulator or public page in `references/quality-systems-sources.md` restates it, with the row id. Otherwise write `[GAP]` and point to the free read-only route (row ST13). Never quote a clause from memory. Row ids from different research files carry their file prefix where ids can collide (for example AI US-23 vs RP US-23); rows from `quality-systems-sources.md` need no prefix unless another research file is cited in the same answer.

**People decide.** Risk acceptability, severity and probability estimates, the review outcome and whether a release waits are the person's. The model lays out evidence and computes against criteria the person gives. A proposal is labeled "proposed". Use the owner or role the person names, in their words. Only if they named none, write 'owner not named' and ask. Never suggest a job title.

**Gaps.** `references/gap-rules.md`. An empty library search is a store gap, never "no recalls". A record not in the files given is "not in the files provided", never "missing".

**Governance.** Read `references/governance.md` before anything leaves the conversation. A named person clears the record through `verify.build_record`. When declining a decision, still give the draft the facts support, labeled "draft for the owner".

**Dates.** Every rule carries its source's date; every library row its retrieval date. The QMSR has applied since 2 February 2026.

## Files in this skill

- `tasks/` the guide for each task. Read only the one you are running.
- `references/quality-systems-sources.md` the sourced research (QMSR, CP 7382.850, MDR Article 10 and Annex I and IX, harmonized standards, ISO and IEC status pages, FDA recognition, vigilance, change guidance), each row with URL, quote and read date. Shared with the monitoring skill.
- `references/design-control-requirements.md` the rule base for A1, by market, with row ids.
- `references/risk-management-requirements.md` the risk process, control priority, acceptability, update triggers and the cybersecurity note, with row ids. Needed for A2 and B1.
- `references/trace-structure.md` the trace item types, links and checks.
- `references/tools.md` every library call used, with arguments and observed pitfalls.
- `references/gap-rules.md`, `references/governance.md` gap wording; stop rules and sign-off.
- `assets/traceability-output.md`, `assets/risk-file-output.md`, `assets/design-review-output.md` output formats, short and full.
- `examples/risk-file-bolus-app.md` a worked A2 run on live library data with an A1 trace check; `examples/live/` the saved library outputs.
- `scripts/trace_check.py` finds orphans, gaps, broken links and open results in a trace CSV.
- `evals/evals.json` four test prompts with expected outputs; `evals/prompts_only.json` the same prompts without them.
