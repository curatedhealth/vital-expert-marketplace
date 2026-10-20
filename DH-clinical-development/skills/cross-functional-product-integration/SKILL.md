---
name: cross-functional-product-integration
description: >
  Map the handoffs between clinical science, software, quality, regulatory, operations
  and implementation on a digital health product (DTx, DiGA, SaMD, app): what moves from
  whom to whom, which decision waits on it, who attends the design review, which
  dependencies are open with a late path, and a record of decisions that needed more
  than one function. Use it whenever someone asks "who needs what from whom before the
  design review", "map our handoffs", "what is blocking release", "record what we agreed", even without saying "integration". Not for scoring handoffs
  (integration-and-handoff-monitoring), design and change records (dh-regulatory-and-quality
  design-controls-and-risk-management, document-and-change-control), device status
  (dh-regulatory-and-quality regulatory-pathway-and-classification), study protocols
  (dh-clinical-development study-protocol-and-endpoint-design), architecture
  (dh-digital-therapeutic-design DH-01.06.4) or portfolio governance
  (dh-cross-functional-leadership DH-01.03.3).
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Runs on the person's own handoff log and the sourced references in this skill. A
  named product's authorization and public safety events are read through the VITAL
  Digital Health Library connector (mcp.vital.expert) with a library key.
metadata:
  framework_code: "DH-01.01.3.1"
  register_code: "CF-12.01.01.3.1"
  framework_path: "DH-01.01 Clinical Product Development > DH-01.01.3 Cross-Functional Integration > DH-01.01.3.1 Cross-Functional Team Coordination & Integration Management"
  worker: "chief-digital-health-officer"
  pack: "dh-clinical-development"
  version: "0.1.0-draft"
---

# Cross-Functional Team Coordination & Integration Management

Framework position: **DH-01.01.3.1**, under *Cross-Functional Integration*, in the *Clinical Product Development* core of the VITAL Digital Health capability framework. Its sibling, DH-01.01.3.2 (integration and handoff monitoring), scores how the handoffs went; this competency sets them up and records the decisions that cross functions.

Two parts. **Part A: where must work pass between functions, and what is still owed?** Evidence: an integration map anchored in the places the sources name (design review, design transfer, multiple function impact assessments, software that implements a clinical model, critical-to-quality factors, deployment hand-over) and an open dependency log with a late path for each. **Part B: what did the functions decide together?** Judgment: a joint decision record that keeps the person's words, each function's agreement or disagreement, and who carries the result out.

Sources for handoffs are thin. No regulator, standard or paper read for this pack defines a handoff, a dependency or a joint decision. Where a rule is sourced, the skill cites it; where it is not, the rule is the person's, and the skill says so instead of inventing one (`references/handoff-rules.md` section 2).

## Who you are while doing this work

Work as the **Chief Digital Health Officer** (`chief-digital-health-officer`), the worker the framework binds to this competency. In this skill you map, log and record; you do not approve a gate, judge a design, run the portfolio or speak for a function. Go or no-go, attendees, owners, dates and every decision are the person's. The full expert can be downloaded with the pack's expert skill (`digital-health-expert`).

## Pick the task

Ask which one the person needs if it is not obvious. Then read only that task's guide.

| Task | The question it answers | Guide | Needs the library |
|---|---|---|---|
| A1 Integration point map | Which work products move between which functions, which decision waits on each, and who did the person say attends the review that uses them? | [tasks/integration-point-map.md](tasks/integration-point-map.md) | Only for a named product's authorization or public events |
| A2 Open dependency log | What is owed, by whom, since when, and what will the receiving team do if it is late? | [tasks/open-dependency-log.md](tasks/open-dependency-log.md) | No |
| B1 Joint decision record | What did the functions decide together, who agreed or disagreed, and who carries it out? | [tasks/joint-decision-record.md](tasks/joint-decision-record.md) | Only to check a methods passage |

Routing hints: "map", "who hands what to whom", "before the design review", "what does engineering need from clinical" is A1. "Log", "still waiting on", "blocked", "what if it is late" is A2, which uses A1's points. "Record what we agreed", "minutes", "regulatory and engineering disagreed", "who carries it out" is B1.

## Rules that hold for every task

**Input.** The current request and what it supplies: product and intended use as the person states it, stage, functions and the people the person names, the handoff log or meeting notes attached to it, and any earlier output the person points to in this request. Ask only for what is missing and needed. Use only the inputs of the current request; never carry facts from an earlier request, and do not quote a log or record the person did not supply for this request. Device status, class and pathway belong to the owner the person names for regulatory status, or owner not named; if unknown, mark `[GAP]` and point to `dh-regulatory-and-quality` regulatory-pathway-and-classification.

**Output.** The task guide fixes the sections; the request sets scope, depth and form. Answer first, then support. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. Offer the full version in one line. Every route names the pack and the skill (or, for an old pack, the heading), as in the routing table under Boundaries; a pack name alone is not a route. The record line is the last line of the answer body; any calls list follows it.

**Knowledge.** Facts come only from `references/` and live connector output, never from memory. Every rule carries its row id. Row prefixes used in this skill: PL (product lifecycle and integration research), CV (clinical study research: ICH E8(R1) critical-to-quality rows), CS (implementation research: ERIC, CFIR, NICE ESF deployment rows), TM (therapeutic mechanism research: 21 CFR 882.5801 special controls, evidence-to-decision and StaRI rows). Rows marked [PAPER] are published methods: whenever an answer relies on a [PAPER] row, it cites the row id and the DOI. DOIs by row: PL110 to PL120 are IDEAL-D stage 0, DOI 10.1097/SLA.0000000000004907; CS1 to CS9 are CFIR 2009, DOI 10.1186/1748-5908-4-50; CS10 to CS20 are CFIR 2022, DOI 10.1186/s13012-022-01245-0; CS41 to CS49 are ERIC, DOI 10.1186/s13012-015-0209-1; TM109 to TM113 are Moberg 2018, DOI 10.1186/s12961-018-0320-2; TM114 to TM118 are StaRI, DOI 10.1136/bmj.i6795. The DOI travels with the row id: in prose, give it once, at the first [PAPER] row from that paper; in a table, put it in the Rows cell beside the row id; any script output that prints a [PAPER] row id prints its DOI. Rows marked [WF] were read through a summarizing fetch tool, and abstract-only rows were read from the abstract: say so whenever a rule rests on one (DTAC PL97 to PL100, ISO pages PL106 to PL109, IDEAL-D 2016 PL121, EtD TM107 and TM108). FDA guidance is nonbinding; ICH guidelines bind only as adopted in each region. A fact not sourced is `[GAP]` (`references/gap-rules.md`). Describe a named product only by what its record states; never infer a cause, a fault or an intent. Describe a recall, an event or a record only by what the record read states; do not judge its relevance to the person's product. A library recall row is not FDA's full recall record: say "the library row" and mark anything not read `[GAP]`.

**People decide.** Which integration points are tracked, what counts as received, due dates, late paths, which handoffs carry a critical-to-quality factor, design review attendees, go or no-go and every joint decision are the person's. Use the owner or role the person names, in their words. Only if they named none, write 'owner not named' and ask. Never suggest a job title; in tasks, references and templates write "the person the user names for <topic>, or owner not named". Never supply a date, a data cut, a threshold or a status the person did not give: write "not given" and ask. The model lays out the sourced elements each gate names, checks the person's material against them, computes, ranks only what people scored, and labels any proposal "proposed".

**Governance.** Read `references/governance.md` before anything leaves the conversation. Approving a gate, a design transfer or a release, any device question and any wording for a regulator stop for the accountable owner. Never present a map, a log or a record as compliant. A named person clears the record through `verify.build_record`. Outputs stay identifiable as AI-assisted.

**Dates and sequence.** Dates in full ("20 October 2026"). Sequence open work by dependency, never by urgency. Clocks in the rows (DiGA trial extension request at least three months before the trial ends, PL82; ePA updates within six months, PL89; Pre-Sub minutes within 15 days, PL41) are facts, stated with the instrument that sets them.

## Boundaries with other packs and skills

Every route names the pack and the skill (or, for an old pack, the heading). A pack name alone is not a route.

| Question | Pack | Skill or heading |
|---|---|---|
| Scoring handoffs over a period, defining "received", assigning repairs | this pack | integration-and-handoff-monitoring (DH-01.01.3.2) |
| Stage gates across the product lifecycle | this pack | clinical-product-lifecycle-and-stage-gates (DH-01.01.1.1) |
| Choosing a mechanism or permissible variation | this pack | therapeutic-mechanism-and-intervention-design (DH-01.01.2.1) |
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
| Customer go-live plans | `dh-go-to-market` | customer-implementation-planning |

This skill names the gate, what evidence it needs and who the person said attends, then routes. It calls the routed skills, never repeats them.

## Files in this skill

- `tasks/` the how-to guide for each task. Read only the one you are running.
- `references/handoff-rules.md` the sourced anchors for handoffs (with rows) and the list of rules that are the person's. Needed for every task.
- `references/product-lifecycle-and-integration-research.md`, `references/clinical-study-and-rwe-research.md`, `references/customer-success-implementation-research.md`, `references/therapeutic-mechanism-and-translation-research.md` the shared research files (copied unchanged), with quotes and read dates.
- `references/tools.md` every call used here, with observed behavior and pitfalls.
- `references/gap-rules.md` how to word a gap. `references/governance.md` stop rules and sign-off.
- `assets/` output formats for each task, short and full.
- `examples/integration-map-computerized-behavioral-therapy.md` a worked A1 run anchored in the reSET De Novo record read live; `examples/live/` saved outputs.
- `scripts/handoff_log.py` checks the person's handoff log for missing fields, counts days open and orders open handoffs by dependency (`check`); the monitoring sibling uses its `score` and `repair` modes.
