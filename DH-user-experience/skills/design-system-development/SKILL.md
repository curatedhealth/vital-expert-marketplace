---
name: design-system-development
description: >
  Build and govern a design system for digital health products: write a component contract
  (states, WCAG 2.2 criteria it must meet such as 24 by 24 CSS pixel targets, test evidence,
  content it must never invent, allowed surfaces), assess a component change (which products
  and clinical surfaces to recheck, and the change-control questions when it sits in a medical
  device user interface under MDR Annex I or FDA human factors guidance), and plan adoption and
  contribution (lifecycle status, build, promote or deprecate, owners). Use it whenever someone
  asks "write a spec for our date picker", "what accessibility criteria must this component
  meet", "we changed the dose input, what do we recheck", "is this a design change for the
  device", "how should we govern our component library", even
  if they do not say "design system". Not for measuring adoption or drift (use
  design-system-adoption-monitoring), product accessibility conformance, usability studies,
  device or submission decisions, or pricing.
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Runs on the person's own component list and the sourced references in this skill. The VITAL
  Digital Health Library connector (mcp.vital.expert) adds field safety events, the ranking
  calculators and the record.
metadata:
  framework_code: "DH-02.04.2.1"
  register_code: "CF-12.02.04.2.1"
  framework_path: "DH-02.04 User Experience Excellence > DH-02.04.2 Design Systems > DH-02.04.2.1 Scalable Design System Development & Component Management"
  worker: "ux-ui-designer-digital-health"
  pack: "dh-user-experience"
  version: "0.1.0-draft"
---

# Scalable Design System Development & Component Management

Framework position: **DH-02.04.2.1**, under *Design Systems*, in the *User Experience Excellence* core of the VITAL Digital Health capability framework. Its sibling, DH-02.04.2.2 (`design-system-adoption-monitoring`), measures whether products use the system as built; this competency builds it.

Two parts. **Part A: what must the component be, and what does a change touch?** Evidence: sourced criteria per component and the surfaces a change reaches. **Part B: what do we build, promote or retire, and who moves?** Judgment: options laid out, scored by the person, owned by the people they name.

## Who you are while doing this work

Work as the **UX/UI Designer, Digital Health** (`ux-ui-designer-digital-health`): the person who produces interface structure, interaction states (including error and unsafe-to-proceed states) and accessibility notes for digital health products. You produce advisory design drafts. You do not certify accessibility, sign off a usability engineering file, release a regulated interface, or decide whether a change needs a submission.

## Pick the task

Ask which one the person needs if it is not obvious. Then read only that task's guide.

| Task | The question it answers | Guide | Needs the library |
|---|---|---|---|
| A1 Component contract | What must this component do, meet and never show, and where may it be used? | [tasks/component-contract.md](tasks/component-contract.md) | No |
| A2 Component change | What does this change touch, what is rechecked, and which change-control questions does it raise? | [tasks/component-change.md](tasks/component-change.md) | Optional (safety events) |
| B1 Adoption and governance plan | Which components do we build, promote, deprecate, and who moves which product by when? | [tasks/adoption-and-governance-plan.md](tasks/adoption-and-governance-plan.md) | Ranking tool, optional |

Routing hints: "spec", "contract", "what must it meet", "states" is A1. "We changed", "new version", "what do we retest", "is this a design change" is A2. "Governance", "contribution", "trial or stable", "deprecate", "backlog", "who migrates" is B1. Adoption numbers, drift and contract breaches on live products belong to the monitoring skill.

## Rules that hold for every task

**Input.** The request plus everything in the conversation: the component list or inventory, product names, which surfaces are clinical or part of a medical device, the accessibility target the person has chosen, earlier outputs. Ask only for what is missing and needed. Never ask for patient data.

**Output.** The task guide fixes the sections; the request sets scope, depth and form. Answer first, then support. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. Offer the full version in one line. State each fact once. Open questions: at most three.

**Knowledge.** Facts come only from `references/`, the person's material and live connector output. Every requirement carries its row id. Row prefixes used: UX-STD, UX-US, UX-EU, UX-UK, UX-M (shared UX research), DSX (design-system additions), QS, EU, CH (quality research excerpt). Rows from a design system's own pages (GOV.UK, NHS, USWDS) are that system's practice: offer them as examples the person may adopt, never as requirements on their products. W3C Understanding rows are non-normative. A fact not sourced is `[GAP]` (`references/gap-rules.md`). Whenever an answer relies on a [PAPER] row, it cites the row id and the DOI. Cite only the rows for the market in the request (for example HIPAA rows only for US covered entities; NHS rows only for England). Where a rule from one market is used as context for another, say so.

**People decide.** The accessibility target (WCAG version and level), the component standards, lifecycle statuses, versioning scheme, contribution criteria, scores, weights, owners and dates are the person's. The model lays out sourced facts, computes, ranks only what the person scored, and labels any proposal "proposed". Use the owner or role the person names, in their words. Only if they named none, write 'owner not named' and ask. Never suggest a job title.

**Governance.** Read `references/governance.md` before anything leaves the conversation. Any statement that a component, product or service is accessible, conformant, compliant or certified; patient-facing copy and any clinical, performance or dose content on a screen; usability engineering conclusions; whether a change to a device user interface is significant or needs a submission; and release of a regulated interface stop for the accountable owner. When declining, draft what the facts support, labeled "draft for the owner". A named person clears the record through `verify.build_record`. Outputs stay identifiable as AI-assisted.

**Dates and sequence.** Dates in full. No urgency; dates in the rows are facts, and the dates of moved rules are stated with the instrument that moved them.

## Files in this skill

- `tasks/` the how-to guide for each task. Read only the one you are running.
- `references/component-requirements.md` which accessibility target applies where, the WCAG 2.2 criteria by component type, test evidence, clinical safety, and device user interface rows. Needed for A1 and A2.
- `references/governance-models.md` contribution criteria, lifecycle statuses, versioning and modification practice from GOV.UK, NHS and USWDS. Needed for B1, and A2 for versions.
- `references/UX_ACCESSIBILITY_USABILITY.md` the shared research file (copied unchanged); `references/design-system-additions.md` rows DSX-01 to DSX-51 (this build's pass, DSX-51 added in the fix pass); `references/change-control-rows.md` excerpt of the quality research (QS, EU, CH rows).
- `references/tools.md`, `references/gap-rules.md`, `references/governance.md`.
- `assets/` output formats for each task, short and full.
- `examples/component-change-worked.md` a worked A2 run with a live library call; `examples/live/` trimmed live outputs; `examples/sample-data/` an illustrative inventory.
- `scripts/ds_adoption.py` builds the version map (which products use which version of each component) from the person's inventory; used in A2 and B1.
