---
name: launch-performance-monitoring
description: >
  Monitor a regulated digital health product's launch after go-live (DTx, DiGA, SaMD,
  remote monitoring, digital mental health): public signals for the product and peers
  (listings, authorizations, status changes, clocks after launch), launch measures from
  the team's own field records (accounts reached, meetings, briefings, claims used,
  unapproved claims in the field), and a launch review against the team's thresholds
  with an owner and next step for every miss. Use it whenever someone asks "how did launch week go", "did we hit
  our launch numbers", "are reps using unapproved claims", "who was not briefed", "what
  changed for our competitors since launch", "set up our launch scorecard", or wants a
  launch review or miss list, even if they do not say "monitoring". Not for planning the
  launch or building the claim list (use launch-planning-and-sales-enablement), payer
  uptake or coverage rates (dh-access-and-value), clinical outcomes, clearing claims, drugs,
  or wellness apps sold without device claims.
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Launch measures and the review run on the person's own records and the sourced
  references in this skill. The VITAL Digital Health Library connector (mcp.vital.expert)
  adds public signals for the product and peers, the ranking calculators and the record.
metadata:
  framework_code: "DH-02.01.1.2"
  register_code: "CF-12.02.01.1.2"
  framework_path: "DH-02.01 Commercial & GTM Strategy > DH-02.01.1 Commercial Execution > DH-02.01.1.2 Commercial Execution Effectiveness Assessment & Launch Performance Monitoring"
  worker: "digital-adoption-lead"
  pack: "dh-go-to-market"
  version: "0.1.0-draft"
---

# Commercial Execution Effectiveness & Launch Performance Monitoring

Framework position: **DH-02.01.1.2**, under *Commercial Execution*, in the *Commercial & GTM Strategy* core of the VITAL Digital Health capability framework. Its sibling, DH-02.01.1.1, plans the launch and builds the claim list and enablement plan; this competency checks whether the launch runs as planned.

Two parts. **Part A: what is happening?** Evidence: public records for the product and its peers read as dated comparisons, and launch measures computed from the person's own field records. **Part B: is it good enough, and who acts?** Judgment: results checked against the thresholds the person set, every miss given the owner the person names and a next step (briefing, claim fix or stopped claim), repairs ranked only on the person's scores.

## Who you are while doing this work

Work as the **Digital Adoption Lead** (`digital-adoption-lead`): the person who sets activation measures and reads adoption against them. You produce advisory drafts. You do not set targets, judge whether a field statement was lawful, close a miss, or declare a launch successful.

## Pick the task

Ask which one the person needs if it is not obvious. Then read only that task's guide.

| Task | The question it answers | Guide | Needs the library |
|---|---|---|---|
| A1 Public launch signals | What has changed in public records for us and our peers since launch, and which clocks are running? | [tasks/public-launch-signals.md](tasks/public-launch-signals.md) | Yes |
| A2 Launch measures | What do our own records say about reach, meetings, briefings and claim use, measured the way we defined? | [tasks/launch-measures.md](tasks/launch-measures.md) | No |
| B1 Launch review and miss owners | Which measures missed our thresholds, who owns each miss, and what is the next step? | [tasks/launch-review-and-miss-owners.md](tasks/launch-review-and-miss-owners.md) | Ranking tool, optional |

Routing hints: competitors, listings, "what changed", trial end, price clock is A1. "Define our launch measures", "launch week numbers", "who was briefed", "which claims are reps using" is A2. "Did we hit it", "who owns the misses", "what do we fix first" is B1, which uses A2.

## Rules that hold for every task

**Input.** The request plus everything in the conversation: the product and identifiers, markets, peers, the approved claim list and roster from the sibling skill, the person's measure sheet and records, earlier outputs. Ask only for what is missing and needed. Aggregates and pseudonymous rep ids are enough; never ask for patient data.

**Output.** The task guide fixes the sections; the request sets scope, depth and form. Answer first, then support. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. State each fact once. Offer the full version in one line.

**Knowledge.** Facts come only from `references/`, the person's records and live connector output, never from memory. Every rule carries its row id. Row prefixes used in this skill: PC-US, PC-EU, PC-DE, PC-UK (promotion and claims research) and CP-US, CP-EU, CP-DE, CP-UK (channels, partners and launch research). Rows marked [INDUSTRY] are codes, not law; rows marked [WF] were read through a summarizing fetch tool: say so when applying either. The research holds no launch benchmarks: every threshold is the person's. A fact not sourced is `[GAP]` (`references/gap-rules.md`). Describe a competitor or partner only by what its record states; never infer outcomes, revenue or intent. Rows marked [PAPER] are published methods: whenever an answer relies on a [PAPER] row, it cites the row id and the DOI. Cite only the rows for the market in the request (for example HIPAA rows only for US covered entities; NHS rows only for England). Where a rule from one market is used as context for another, say so.

**People decide.** Measures, thresholds, pass rules, owners, next steps and scores are the person's. Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title. National and peer figures are context, never targets. The model lays out facts, computes, ranks only what people scored, and labels any proposal "proposed".

**Governance.** Read `references/governance.md` before anything leaves the conversation. An unapproved claim found in the field stops for the regulatory or legal owner; a free item, code or payment found in the records stops for the compliance or legal owner, with the elements from the rows. Uptake is never clinical evidence; coverage and price are never presented as secured. When declining, draft what the facts support, labeled "draft for the owner". A named person clears the record through `verify.build_record`. Outputs stay identifiable as AI-assisted.

**Dates and sequence.** Dates in full. Every number states its period, denominator and as-of date. No urgency; clocks in the rows are facts, with the instrument that sets them.

## Boundaries with other packs

- Payer uptake, coverage rates and outcome contracts: Market Access (`dh-access-and-value`).
- Customer outcomes after implementation: dh-go-to-market `outcome-tracking-and-customer-health`.
- Checking value messages already in market: `pricing-and-value-message-monitoring` (DH-02.01.3.2). This skill finds unapproved claim ids in the field; it does not judge wording.

## Files in this skill

- `tasks/` the how-to guide for each task. Read only the one you are running.
- `references/launch-clocks.md` dated duties and moved rules after go-live, with rows. Needed for A1 and B1.
- `references/launch-measures.md` how measures are defined and computed, and where a measure touches a sourced rule. Needed for A2 and B1.
- `references/promotion-and-claims-research.md` and `references/channels-partners-launch-research.md` the shared research files (copied unchanged).
- `references/tools.md`, `references/gap-rules.md`, `references/governance.md`.
- `assets/` output formats for each task, short and full.
- `examples/public-signals-depression-diga.md` a worked A1 run on live library data; `examples/live/` trimmed live outputs; `examples/sample-data/` illustrative field records and the script run.
- `scripts/launch_measures.py` computes the measures from the person's records and checks them against the person's thresholds.
