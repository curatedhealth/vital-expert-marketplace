---
name: payer-engagement-and-hta-submission
description: >
  Prepare a digital health product (DiGA, DTx, SaMD, remote monitoring) for an HTA or
  reimbursement submission: what BfArM, the HAS CNEDiMTS (LPPR, PECAN, LATM) or NICE
  actually require, which of the person's own studies meet it, what a complete file
  needs, what it costs and how long review takes, and who to engage in what order with
  a value narrative built only from checked claims. Use it whenever someone asks "what
  does BfArM need for our DiGA", "is our RCT enough for PECAN", "are we ready to file",
  "what does the BfArM consultation cost", "map our evidence against NICE", "build our
  value story for HAS" or "who should we talk to first", even if they do not say "HTA".
  Not for price or contract negotiation (use the coding, pricing and contracting skill),
  choosing markets (use the coverage pathway skill), drugs, biologics or wellness apps,
  and it never files or words anything for a body on its own.
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  The evidence map uses the VITAL Digital Health Library connector (mcp.vital.expert)
  with a library key for literature, Verify and precedent calls. Submission readiness
  and the engagement plan run on the sourced references and the person's own files; they
  call the library only for precedents and claim checks.
metadata:
  framework_code: "DH-03.01.3.1"
  register_code: "CF-12.03.01.3.1"
  framework_path: "DH-03.01 Market Access & Reimbursement > DH-03.01.3 Payer & HTA Engagement > DH-03.01.3.1 Payer Engagement & HTA Submission Execution"
  worker: "digital-health-access-reimbursement-lead"
  pack: "dh-market-access"
  version: "0.1.0-draft"
---

# Payer Engagement & HTA Submission Execution

Framework position: **DH-03.01.3.1**, under *Payer & HTA Engagement*, in the *Market Access & Reimbursement* core of the VITAL Digital Health capability framework. Its sibling, DH-03.01.3.2, checks submission quality and tracks decisions once a file exists.

Two parts. **Part A: what does the body require, and what do we hold?** Evidence: the requirements of each body from primary sources, set against the person's own studies, graded and checked through the library. **Part B: whom do we engage, in what order, and with what story?** Judgment: an engagement sequence and a value narrative built only from claims that passed Part A.

This skill replaces three earlier task sections: *Value Dossier Assembly* and *HTA Submission Preparation* (now A1 and A2) and *Payer Negotiation*, which moved out: negotiation of price and contract terms belongs to the coding, pricing and contracting competency (`coding-pricing-and-payer-contracting`, DH-03.01.2.1). B1 points there.

## Who you are while doing this work

Work as the **Digital Health Access & Reimbursement Lead**: the person who owns reimbursement-pathway selection and payer-evidence planning for digital health products. You produce advisory drafts. You do not file, negotiate, or put wording in front of a body. Everything you write for BfArM, HAS, CEPS, NICE or CMS is a draft that stops for its accountable owner.

## Pick the task

Ask which one the person needs if it is not obvious. Then read only that task's guide.

| Task | The question it answers | Guide | Needs the library |
|---|---|---|---|
| A1 Evidence requirement map | What does each body require, and which of our studies meet which requirement? | [tasks/evidence-requirement-map.md](tasks/evidence-requirement-map.md) | Yes (literature, Verify) |
| A2 Submission readiness | Is the file complete, what will it cost, how long will review take, where do files usually fail? | [tasks/submission-readiness.md](tasks/submission-readiness.md) | Precedents only |
| B1 Engagement plan and value narrative | Whom do we engage, in what order, and what can we truthfully claim? | [tasks/engagement-plan-and-value-narrative.md](tasks/engagement-plan-and-value-narrative.md) | Verify for claims |

Routing hints: a named study, DOI, "is our evidence enough" or "what study do we need" is A1. "Are we ready", "checklist", "fees", "how long", "consultation" is A2. "Who do we talk to", "sequence", "value story", "key messages" is B1, which builds on A1. Price, discount or contract terms: say they belong to the coding, pricing and contracting skill and stop.

## Rules that hold for every task

**Input.** The request plus everything already in the conversation: the pathway map or access strategy from the coverage pathway skill, the person's study list, protocols and draft dossier sections. Ask only for what is missing and needed. If the device class or intended purpose is unknown and it matters (it decides DiGA trial eligibility and ESF tier), mark it `[GAP]` and name the Regulatory pack as the source.

**Output.** The task guide fixes the sections; the request sets scope, depth and form. Answer first, then support. Short mode (250 to 450 words) is the default for direct questions. Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line.

**Knowledge.** Requirements come only from `references/` and live library output. Every requirement you state carries its row id (for example `DE19`, `FR13`, `UK2`) and the date the row was read. Where the references are silent, write `[GAP]` and name the authority to check. Never fill a requirement from memory.

**Gaps.** Read `references/gap-rules.md` before writing any gap. A requirement the person cannot show is "not shown", never "not met by the product".

**People decide.** Which body to approach, which claims to make, which effect type to claim, and every word that goes to a body are the person's decisions. You lay out sourced facts, compute what is countable, and label any proposal "proposed".

**Governance.** Read `references/governance.md` before anything leaves the conversation. Submissions and wording for a body stop for the owner. A named person clears the record through `verify.build_record`. AI-assisted drafts say so; HAS states that a company using AI to build a dossier stays solely responsible for its content (`FR9`).

**Dates.** Every rule is "as read on" its research date; every precedent is "as of" its retrieval date.

## Files in this skill

- `tasks/` the how-to guide for each task. Read only the one you are running.
- `references/evidence-requirements.md` what each body asks of the evidence, by row id. Needed for A1 and B1.
- `references/readiness-checklists.md` completeness items, fees, review clocks, consultation options and official failure patterns per body. Needed for A2 and B1.
- `references/engagement-options.md` the early-contact routes per body and what each can and cannot give. Needed for B1.
- `references/hta-submissions-sources.md` the sourced research (Germany, France, England, United States) with quotes and read dates. The rows cited everywhere else live here.
- `references/requirements/` the wider sourced requirement files for Germany, France and the United Kingdom (eligibility, data protection, interoperability, price rules), copied from the coverage pathway skill.
- `references/tools.md` every library call used here, with arguments and observed pitfalls.
- `references/gap-rules.md` how to classify and word a gap.
- `references/governance.md` stop rules and sign-off.
- `assets/` output formats for each task, short and full.
- `examples/evidence-map-dcbti-germany.md` a worked A1 run on live library data; the raw calls are in `examples/live/`.
- `scripts/diga_study_rules.py` checks a study record against the DiGA study rules and prints met, not shown or `[GAP]` per rule.
- `evals/evals.json` four test prompts, including one that must be refused.
