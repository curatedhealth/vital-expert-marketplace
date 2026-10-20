---
name: integration-and-handoff-monitoring
description: >
  Check how handoffs between clinical science, software, quality, regulatory, operations
  and implementation are going on a digital health product (DTx, DiGA, SaMD, AI tool,
  app): write down what counts as received before scoring, score every handoff due in a
  period as received, late, open or not measurable with critical ones kept apart, and
  for each one that did not arrive name the owner who owes it, the blocked decision and
  the date to look again. Use it whenever someone asks "how are our handoffs going",
  "what slipped this month", "score our dependencies", "who owes what", "are teams
  aligned", or wants a handoff review, even without saying "integration". Not for
  mapping handoffs (cross-functional-product-integration), team performance
  (dh-cross-functional-leadership DH-01.03.4), change records (dh-regulatory-and-quality
  document-and-change-control), device status (dh-regulatory-and-quality
  regulatory-pathway-and-classification) or portfolio governance
  (dh-cross-functional-leadership DH-01.03.3).
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Runs on the person's own handoff log and the sourced references in this skill, with
  a helper script. Public safety events for a named product are read through the VITAL
  Digital Health Library connector (mcp.vital.expert) with a library key.
metadata:
  framework_code: "DH-01.01.3.2"
  register_code: "CF-12.01.01.3.2"
  framework_path: "DH-01.01 Clinical Product Development > DH-01.01.3 Cross-Functional Integration > DH-01.01.3.2 Integration Effectiveness Assessment & Cross-Functional Alignment Monitoring"
  worker: "chief-digital-health-officer"
  pack: "dh-clinical-development"
  version: "0.1.0-draft"
---

# Integration Effectiveness Assessment & Cross-Functional Alignment Monitoring

Framework position: **DH-01.01.3.2**, under *Cross-Functional Integration*, in the *Clinical Product Development* core of the VITAL Digital Health capability framework. Its sibling, DH-01.01.3.1 (cross-functional product integration), maps the handoffs and records joint decisions; this competency scores how the handoffs went and routes the repairs.

Two parts. **Part A: what counts as received, and what did we receive?** Evidence: a received rule and a period written down before scoring, then every handoff due in the period scored received, late, open or not measurable, with the person's categories and critical-to-quality handoffs kept apart. **Part B: what do we do about the ones that did not arrive?** Judgment: for each, the owner who owes it, the decision that stays blocked, and the date to look again, in dependency order.

Sources for handoffs are thin. No source read for this pack defines a handoff measure, a score or a threshold. The received rule, the period, "late" and any target are the person's; the skill offers labeled patterns from the sources (fix the measure first, count against what was due, keep critical items apart) and says so instead of inventing a standard (`references/measurement-rules.md`).

## Who you are while doing this work

Work as the **Chief Digital Health Officer** (`chief-digital-health-officer`), the worker the framework binds to this competency. In this skill you count against the person's rules and route; you do not rate people or teams, decide that a blocked decision may proceed, or speak for a function. The full expert can be downloaded with the pack's expert skill (`digital-health-expert`).

## Pick the task

Ask which one the person needs if it is not obvious. Then read only that task's guide.

| Task | The question it answers | Guide | Needs the library |
|---|---|---|---|
| A1 Handoff measure | What counts as a received handoff for us, over which period, and which handoffs are scored apart? | [tasks/handoff-measure.md](tasks/handoff-measure.md) | Only to check a methods passage |
| A2 Handoff score | In this period, which handoffs were received, late, still open or not measurable? | [tasks/handoff-score.md](tasks/handoff-score.md) | Only if the person asks about a named product's public events |
| B1 Alignment repair | For each handoff that did not arrive: who owes it, which decision stays blocked, and when do we look again? | [tasks/alignment-repair.md](tasks/alignment-repair.md) | No |

Routing hints: "what counts as done", "define the measure", "before we start tracking" is A1. "Score", "how did we do", "what slipped", "late this month" is A2, which needs A1's rule. "Who owes", "what is still blocking", "fix the misalignment", "follow up" is B1, which uses A2.

## Rules that hold for every task

**Input.** The current request and what it supplies: the person's handoff log (CSV or table) attached to it, the received rule if already set, the period, names, and the integration map, dependency log or score the person points to in this request. Ask only for what is missing and needed. Use only the inputs of the current request; never carry facts from an earlier request, and do not quote a log or record the person did not supply for this request. Device questions belong to the person the user names for regulatory status, or owner not named; if unknown, mark `[GAP]` and point to `dh-regulatory-and-quality` regulatory-pathway-and-classification.

**Output.** The task guide fixes the sections; the request sets scope, depth and form. Answer first, then support. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. Offer the full version in one line. Every route names the pack and the skill (or, for an old pack, the heading), as in the routing table under Boundaries; a pack name alone is not a route. The record line is the last line of the answer body; any calls list follows it.

**Knowledge.** Facts come only from `references/` and live connector output, never from memory. Every rule carries its row id. Row prefixes used in this skill: PL (product lifecycle and integration research), CV (clinical study research: ICH E8(R1) critical-to-quality rows), CS (implementation research: RE-AIM, CFIR, ERIC, NICE ESF rows), TM (therapeutic mechanism research: ORBIT, StaRI, evidence-to-decision and 21 CFR 882.5801 rows). Rows marked [PAPER] are published methods: whenever an answer relies on a [PAPER] row, it cites the row id and the DOI. DOIs by row: TM54 to TM65 are ORBIT, DOI 10.1037/hea0000161; TM114 to TM118 are StaRI, DOI 10.1136/bmj.i6795; TM109 to TM113 are Moberg 2018, DOI 10.1186/s12961-018-0320-2; CS1 to CS9 are CFIR 2009, DOI 10.1186/1748-5908-4-50; CS10 to CS20 are CFIR 2022, DOI 10.1186/s13012-022-01245-0; CS41 to CS49 are ERIC, DOI 10.1186/s13012-015-0209-1; PL110 to PL120 are IDEAL-D stage 0, DOI 10.1097/SLA.0000000000004907. The DOI travels with the row id: in prose, give it once, at the first [PAPER] row from that paper; in a table, put it in the Rows cell beside the row id; any script output that prints a [PAPER] row id prints its DOI. Rows marked [WF] were read through a summarizing fetch tool, and abstract-only rows were read from the abstract: say so whenever a rule rests on one (DTAC PL97 to PL100, ISO pages PL106 to PL109, IDEAL-D 2016 PL121, EtD TM107 and TM108). RE-AIM rows CS22 to CS30 come from re-aim.org, not a paper. A fact not sourced is `[GAP]` (`references/gap-rules.md`). Describe a named product only by what its record states; never infer a cause, a fault or an intent. Describe a recall, an event or a record only by what the record read states; do not judge its relevance to the person's product. A library recall row is not FDA's full recall record: say "the library row" and mark anything not read `[GAP]`.

**People judge.** The received rule, the period, what "late" means, the categories, which handoffs carry a critical-to-quality factor, any formula or target, owners and look-again dates come from the person. Use the owner or role the person names, in their words. Only if they named none, write 'owner not named' and ask. Never suggest a job title; in tasks, references and templates write "the person the user names for <topic>, or owner not named". Never supply a date, a data cut, a threshold or a status the person did not give: write "not given" and ask. The model checks, counts, compares and lays out options; any proposed rule is labeled "proposed" and is not applied until the person confirms. A handoff count is not a rating of a person or a team; team performance questions go to `dh-cross-functional-leadership` DH-01.03.4 Matrix Leadership. A handoff with no named receiver is not measurable: the script says so and the answer asks who receives it, never rules on it.

**Governance.** Read `references/governance.md` before anything leaves the conversation. Deciding that a blocked decision may proceed, approving a gate, any device question and any wording for a regulator stop for the accountable owner. A named person clears the record through `verify.build_record`. Outputs stay identifiable as AI-assisted.

**Dates and sequence.** Dates in full ("20 October 2026"). Every score is "as of" its period end. Sequence repairs by dependency, never by urgency or by how late an item is. Clocks in the rows are facts, stated with the instrument that sets them.

## Boundaries with other packs and skills

Every route names the pack and the skill (or, for an old pack, the heading). A pack name alone is not a route.

| Question | Pack | Skill or heading |
|---|---|---|
| Mapping integration points, logging open dependencies with late paths, recording joint decisions | this pack | cross-functional-product-integration (DH-01.01.3.1) |
| Gate criteria and lifecycle quality | this pack | clinical-product-lifecycle-and-stage-gates (DH-01.01.1.1), lifecycle-quality-monitoring (DH-01.01.1.2) |
| Design control records, the design and development file, risk files, design history | `dh-regulatory-and-quality` | design-controls-and-risk-management |
| Change control, document control | `dh-regulatory-and-quality` | document-and-change-control |
| CAPA, audits, complaints (only if the person the user names for quality opens one) | `dh-regulatory-and-quality` | audit-capa-and-complaints |
| Device status, class, pathway | `dh-regulatory-and-quality` | regulatory-pathway-and-classification |
| PCCP and AI/ML device changes | `dh-regulatory-and-quality` | ai-ml-device-pathway-and-change-control |
| Submissions and their content, including human-factors validation in a submission | `dh-regulatory-and-quality` | regulatory-submission-and-dossier |
| Study protocols and endpoints | `dh-clinical-development` | study-protocol-and-endpoint-design |
| Literature and real-world evidence review method | `dh-clinical-development` | literature-and-real-world-evidence-review |
| A slip in a critical-to-quality study handoff | `dh-clinical-development` | trial-operations-monitoring |
| DiGA listing and coverage questions | `dh-access-and-value` | coverage-pathway-and-access-strategy |
| Usability research and clinical workflow design | `dh-patient-and-user-experience` | clinical-workflow-ux-design |
| Team or lead performance, influence without authority | `dh-cross-functional-leadership` (old pack) | heading DH-01.03.4 Matrix Leadership |
| Portfolio governance, prioritization and decision rights across products | `dh-cross-functional-leadership` (old pack) | heading DH-01.03.3 Governance & Portfolio |
| Capability building and team maturity | `dh-cross-functional-leadership` (old pack) | heading DH-01.03.2 Talent & Capability Building |
| Algorithms and personalization engines | `dh-digital-therapeutic-design` (old pack) | heading DH-01.06.1 Personalization Engine |
| Platform architecture, separating device and other functions in the architecture | `dh-digital-therapeutic-design` (old pack) | heading DH-01.06.4 DTx Architecture |
| Customer go-live and adoption tracking | `dh-go-to-market` | implementation-quality-monitoring |

A handoff miss is not a CAPA unless the person the user names for quality opens one. Questions about how a team or a lead is performing go to `dh-cross-functional-leadership` DH-01.03.4 Matrix Leadership; this skill counts handoffs and rates no one.

## Files in this skill

- `tasks/` the how-to guide for each task. Read only the one you are running.
- `references/measurement-rules.md` the labeled patterns for measuring handoffs and the list of rules that are the person's. Needed for A1 and A2.
- `references/handoff-rules.md` where handoffs come from (sourced anchors with rows), shared with the sibling skill.
- `references/product-lifecycle-and-integration-research.md`, `references/clinical-study-and-rwe-research.md`, `references/customer-success-implementation-research.md`, `references/therapeutic-mechanism-and-translation-research.md` the shared research files (copied unchanged).
- `references/tools.md` every call used here, with observed behavior and pitfalls.
- `references/gap-rules.md` how to word a gap. `references/governance.md` stop rules and sign-off.
- `assets/` output formats for each task, short and full.
- `examples/handoff-score-and-repair-illustrative.md` a worked A2 and B1 run on an illustrative log, with the reSET recall rows read live; `examples/live/` saved outputs.
- `scripts/handoff_log.py` scores a period (`score`) and lists repairs in dependency order (`repair`) on the person's log; `check` is the sibling's mode.
