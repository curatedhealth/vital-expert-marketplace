---
name: validate-valuation-assumptions
description: "Use when a buyer (pharma business development or life-sciences investor) has a DCF and an rNPV and needs the ASSUMPTIONS behind them documented and checked: an assumption register in which every input has a source or a labelled team assumption with an owner, is traced to the due diligence register that holds it, and is checked against the success-rate benchmark, the analog range, the exclusivity end, the documentation duty for the discount rate and the risk-counted-twice question. Lists what traces, what is flagged and what is a gap; does not call a valuation validated, choose a rate or adopt a valuation. Not for building the model or for comparables."
metadata:
  level: CF04
  register_code: CF-01.02.02.1.3
  register_id: fcefb2ba-eabb-4cb9-9a5a-21ddc0736440
  version: 0.1.0
  verb: validate
  capability: CF-01.02.02 Financial Modeling & Valuation
  mission: CF-01.02.02.1 DCF & Risk-Adjusted NPV Modeling
  agent: npv_analyst (existing agent row, recommended; not written by the migration)
  atoms: [extract-requirements-from-source, compare-against-criteria, compose-draft]
  feeds: [communicate-valuation-scenarios, design-valuation-scenarios]
  tools: [scripts/assumptions.py, scripts/validate_register.py]
  tier: "Standard (owner ruling of 8 November 2026; the Full tier of ruling V6 was provisional and is retired): this skill is validated with Standard-tier known-answer sets (arithmetic, rules and filing fidelity); not run"
  requires: [build-dcf-model, calculate-risk-adjusted-npv]
  release_state: Draft (build complete; known-answer set built, not run; back-test or review pending)
---

# Validate valuation assumptions

## What competent output looks like
- An assumption register: every input of the DCF and the rNPV with id, range, unit, source or labelled owner, and the pointer of the register row it came from.
- Nine checks stated as ok, flag or gap with the consequence: trace, order, upstream pointer, probability against the benchmark, peak revenue against the analog range, rate documentation, risk counted twice, explicit cash flows beyond the exclusivity end, terminal share.
- No claim that the valuation is validated: the statement says how many checks are ok, flagged or gaps and that a named reviewer decides.
- The adopted valuation shows HUMAN ONLY; no fairness or solvency view.

## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Intake (intake.md) | none | agent asks; human supplies |
| 2 | Collect the assumptions of the DCF and the rNPV with sources or owners (task 01) | extract-requirements-from-source | agent drafts; human reviews |
| 3 | Trace each assumption to the due diligence register that holds it (task 02) | extract-requirements-from-source; compare-against-criteria | agent drafts; human reviews |
| 4 | Run the nine checks (task 03) | scripts/assumptions.py | agent alone (script); human reviews every flag and gap |
| 5 | Screen the failure modes and write the questions (task 04) | compare-against-criteria | agent drafts; human reviews every "triggered" |
| 6 | Validate and write the assumption register (task 05) | scripts/validate_register.py; compose-draft with templates/assumption-register.md | agent alone (script) |
| 7 | Whether any flagged assumption stands; the choice of rate; the adopted valuation | none | human only |

## Rules (general, apply to every case)
1. **Checks bind to names.** C4 applies to the probability assumption named cumulative_pos and C5 to the revenue assumption named peak_net_revenue; an assumption under another name is not compared and the check row is absent, so name them as the register does. **Trace or gap.** An assumption without a source and without a labelled team assumption with an owner is a gap and is not used as a finding.
2. **Benchmarks are the due diligence registers'.** The success-rate stratum, the analog range and the exclusivity end come from those registers; this skill compares and flags, it does not set them.
3. **Flag, do not decide.** An above-benchmark probability or an above-analog peak is flagged with the consequence; whether it stands is a person's call.
4. **Units are not converted.** A unit mismatch is a gap.
5. **No validation claim.** The output says how many checks are ok, flagged or gaps and that a named reviewer decides.
6. **No default thresholds.** The terminal share is reported and no threshold is applied (FV-TERMINAL-SHARE is [CHECK]).

## Method anchoring
The comparison rules reuse registered passages: success-rate benchmarks (VP-B-001, VP-B-004, VP-B-060), published forecast optimism (VP-H-001, VP-H-010), the rate documentation duty and risk placement (VP-V-030, VP-V-031, VP-V-036) and exclusivity statutes (VP-C-001, VP-C-061, VP-C-090). The nine-check set and the ok / flag / gap states are this skill's own rules.

## Connectors
- DCF and rNPV registers; the market, timeline, exclusivity and revenue registers of the due diligence plugin: read-only.
- VITAL Verify (check_claim): check a claim against a quoted passage.

## Quality bar
- Every assumption traced or a stated gap; the nine checks present; statement without a validation claim.
- assumptions.py and validate_register.py exit 0; terminal share [CHECK] listed.
- At least one question; adopted valuation HUMAN ONLY; UNSIGNED until a reviewer signs.
