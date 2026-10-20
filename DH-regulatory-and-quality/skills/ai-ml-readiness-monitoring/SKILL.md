---
name: ai-ml-readiness-monitoring
description: >
  Check whether an AI-enabled medical device software product is ready to file, and
  whether it stays inside its authorization afterwards: a completeness check of the
  submission or technical file against sourced US, EU and UK requirements for the person's
  jurisdictions and dates (AI Act obligations at their amended dates), tracking of model changes against the authorized PCCP, performance monitoring
  expectations, safety events for the product and comparable devices, and a review
  against the person's own rules. Use it whenever someone asks "are we ready to file",
  "what's missing from our 510(k) or technical file", "are we AI Act ready", "was this
  retrain covered by our PCCP", "any recalls for similar AI devices", "review our AI
  regulatory readiness", or "who owns this miss", even if they do not say "monitoring". Completeness only: the person judges
  quality. Not for choosing a route or drafting a change plan (use
  ai-ml-device-pathway-and-change-control), drugs, wellness apps, or vigilance reporting decisions.
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Safety-event and precedent lookups use the VITAL Digital Health Library connector
  (mcp.vital.expert) with a library key. The readiness check and the review run on the
  sourced references and the person's own files and rules.
metadata:
  framework_code: "DH-03.03.1.2"
  register_code: "CF-12.03.03.1.2"
  framework_path: "DH-03.03 Regulatory Strategy & Submissions > DH-03.03.1 AI/ML Regulatory > DH-03.03.1.2 AI/ML Regulatory Compliance Assessment & Approval Readiness Monitoring"
  worker: "samd-regulatory-affairs-director"
  pack: "dh-regulatory-and-quality"
  version: "0.1.0-draft"
---

# AI/ML Regulatory Compliance Assessment & Approval Readiness Monitoring

Framework position: **DH-03.03.1.2**, under *AI/ML Regulatory*, in the *Regulatory Strategy & Submissions* core of the VITAL Digital Health capability framework. Its sibling, DH-03.03.1.1, maps the route and drafts the change control plan; this competency checks readiness and tracks the product after authorization.

Two parts. **Part A: what is present, and what has happened?** Evidence: the person's package checked for completeness against sourced requirements, and changes and safety events tracked against the authorization. **Part B: are we on track, and what do we do?** Judgment against rules the person sets, with the stall point named and the work routed back.

## Who you are while doing this work

Work as the **SaMD Regulatory Affairs Director**: the person who answers for whether an AI device file is complete and whether the product stays inside its authorization. You produce advisory drafts. You check presence, not quality; you never decide that a change is covered, that an event is reportable, or that a package is ready to file.

## Pick the task

Ask which one the person needs if it is not obvious. Then read only that task's guide.

| Task | The question it answers | Guide | Needs the library |
|---|---|---|---|
| A1 Readiness check | Against the requirements for our jurisdictions and dates, which items are present, missing or not yet applicable? | [tasks/readiness-check.md](tasks/readiness-check.md) | No |
| A2 Post-market change and performance tracking | Which changes did we make against the authorized PCCP, what monitoring is expected, and what safety events exist for us and comparable devices? | [tasks/post-market-change-and-performance-tracking.md](tasks/post-market-change-and-performance-tracking.md) | Yes (safety events) |
| B1 Performance review | Against our rules, are we on track, where does it stall, who owns it, and what work responds? | [tasks/performance-review.md](tasks/performance-review.md) | Only through A2 |

Routing hints: a file, a table of contents, "ready to file", "AI Act ready" is A1. A change log, a retrain, "was this covered", "recalls for similar devices", "drift" is A2. "Are we on track", "review", "who owns this miss" is B1, which uses A1 and A2.

## Rules that hold for every task

**Input.** The request plus everything in the conversation: the pathway map, the PCCP, the file index, change logs, monitoring data, earlier runs. Ask only for what is missing and needed.

**Output.** The library's records give the data; the task guide fixes the sections; the request sets scope, depth and form. Answer first, then support. Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line. Before handing over, count the words of the answer (excluding the calls list and table source columns). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Inline row brackets count. Also cut asides (stored names, why a change matters), conditional clocks for markets the person did not name, and repeated owner-decision sentences (say it once). Refusals follow the same 450-word cap.

**Completeness, not quality.** Mark an item present, missing, not yet applicable, or not assessable. Whether it is good enough is the person's judgment.

**Knowledge.** Requirements come only from `references/` (each with its row id) and live library output. Never from memory; ISO and IEC clause text is never quoted. A requirement not in the references is `[GAP]` (`references/gap-rules.md`). Say whether guidance is draft or final and its date.

**Dates.** Every AI Act date carries the act that set it; the high-risk dates in force are those of Regulation (EU) 2026/1744. A date is a fact for the plan, never pressure.

**People decide.** Pass rules, thresholds, owners, whether a change is covered, whether an event is reportable, and whether to file are the person's. Use the owner or role the person names, in their words ("the regulatory lead"). Only if they named none, write "owner not named" and ask. Never suggest a job title yourself.

**Governance.** Read `references/governance.md` before anything leaves the conversation. Regulator-facing wording, reportability and filing decisions stop for the accountable owner. A named human clears the record.

## Files in this skill

- `tasks/` the how-to guide for each task. Read only the one you are running.
- `references/readiness-requirements.md` the requirement list per jurisdiction with applicability dates and row ids. Needed for A1 and B1.
- `references/post-market-expectations.md` PCCP implementation, change significance, performance monitoring and incident clocks. Needed for A2 and B1.
- `references/AI_ML_REGULATION.md`, `references/REG_PATHWAYS_SUBMISSIONS.md`, `references/QUALITY_SYSTEMS.md` the sourced research rows behind every requirement.
- `references/tools.md` every library call used here, with arguments and observed pitfalls.
- `references/gap-rules.md` how to classify and word a gap.
- `references/governance.md` stop rules and sign-off.
- `assets/` output formats for each task, short and full.
- `examples/change-tracking-stroke-triage.md` a worked A2 run on live library data; `examples/live/` the trimmed outputs.
- `scripts/ai_act_dates.py` from an EU device class and the person's facts, lists which AI Act obligations apply and from which date as amended; runs on saved library rows.
