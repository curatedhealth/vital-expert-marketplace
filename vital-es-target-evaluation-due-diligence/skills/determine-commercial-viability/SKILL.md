---
name: determine-commercial-viability
description: "Use when a buyer (pharma business development or life-sciences investor) needs the commercial picture of a drug asset set out as options before a human decides, in the US and EU, after the market register exists: a peak-sales RANGE built from analog launches that the person supplies or that are sourced with dates (never a single point), and an option set GO, CONDITIONAL GO and NO-GO, each with the conditions that would have to hold, the evidence for and against, and what would change the call. Reads the market register, the clinical evidence register, the development risk ranges, the mechanism register, the exclusivity register and the pathway map. Price, coverage and access assumptions come from the Market Access pack and are a gap until it is Released. Never makes the commercial decision (human only). Not for valuation or deal value, not for revenue and price ranges (use forecast-revenue-and-price-ranges), not for markets other than US and EU."
metadata:
  level: CF04
  register_code: CF-01.02.06.2.3
  register_id: ceb0232d-3472-475b-93d7-4b43fefda66f
  version: 0.1.0
  verb: determine
  capability: CF-01.02.06 Target Evaluation & Due Diligence
  mission: CF-01.02.06.2 Commercial & Market Assessment
  agent: bd-due-diligence-lead
  atoms: [extract-requirements-from-source, compare-against-criteria, rank-by-consequence, compose-draft]
  feeds: [decision-owner (human only)]
  tools: [scripts/analog_range.py, scripts/option_set.py, scripts/validate_register.py]
  tier: "Full (owner ruling 7 November 2026): the capability is Full; this skill is validated with a Standard-style known-answer set, built in a later lane"
  requires: [evaluate-market-opportunity-and-competitive-position, forecast-revenue-and-price-ranges]
  release_state: Draft (Q1-Q6 built; Q7 back-test pending; Q8 practitioner review pending)
---

# Determine commercial viability

## What competent output looks like
- A commercial viability register for one asset (company unit: one per pipeline asset, then a side-by-side roll-up):
  1. **Peak sales as a range**: the lowest, the median and the highest peak annual sales of the included analog launches, with n, currency, geography and the range recomputed leaving each analog out. Each analog states why it is comparable and carries a dated source. The method says so on the page: it is a range from analogs, not a forecast, not a point estimate, not a deal value, and it is not adjusted for price, coverage or access.
  2. **An option set** with three options, always all three: GO, CONDITIONAL GO, NO-GO. Each lists the conditions that would have to hold, the evidence for and against, and what would change the call. No option is ranked or recommended.
  3. **The conditions** and the state of each (met, not met, straddles a threshold, gap), with its owner skill. They are drawn from the signed registers of skills A, F, G, from the ranges of B, from the exclusivity register of C and the pathway map of D. Thresholds (a peak-sales hurdle, the exclusivity wanted after launch, the minimum number of supported differentiation claims) are the buyer's; the skill never sets one.
  4. **The price and revenue input** (owner ruling R7, 7 November 2026): price and revenue ranges are read from the signed register of skill forecast-revenue-and-price-ranges (condition C-RV, unrisked and undiscounted ranges, country by country). Until that register is signed they are a GAP. **The Market Access hand-off** now covers coverage and access, and the pack's price figures are only a side-by-side cross-check (references/market-access-interface.md); until that pack is Released they are a GAP and the register says the range is not adjusted for them and may be overstated.
- No single peak-sales figure and no statement that the asset is or is not viable. The commercial decision is human only.
- Absent evidence is a GAP with the consequence stated. Never "unknown".

## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Intake (intake.md): buyer mode, unit, thresholds, analogs, the owner of the decision | none | agent asks; human supplies |
| 2 | Collect or source analog launches with dated sources and a stated basis for comparability (task 01) | extract-requirements-from-source; connectors | agent drafts; human reviews every analog |
| 3 | Compute the analog range and its leave-one-out sensitivity (task 02) | scripts/analog_range.py | agent alone (script); human confirms the analog set |
| 4 | Read the upstream registers and exclusivity and pathway dates into conditions (task 03) | compare-against-criteria (met / not met / straddles / gap); scripts/option_set.py | agent drafts; human reviews |
| 5 | Read price and revenue from the signed revenue register (C-RV) and coverage and access from the Market Access pack, or record the GAP (task 04) | scripts/option_set.py | agent alone; human confirms the pack state |
| 6 | Build the option set (task 05) | scripts/option_set.py; rank-by-consequence orders the open items by what each puts at risk | agent drafts; human reviews |
| 7 | Screen failure modes and write the questions (task 06) | compare-against-criteria (triggered / not triggered / cannot tell) | agent drafts; human reviews every "triggered" |
| 8 | Validate and write the register (task 07) | scripts/validate_register.py; compose-draft with templates/viability-register.md | agent alone (script) |
| 9 | Which analogs count; which patents count toward exclusivity; the buyer's thresholds | none | human only |
| 10 | The commercial decision: GO, CONDITIONAL GO or NO-GO | none | human only |

## Rules (general, apply to every case)
1. **Range, never a point.** The analog calculator returns low, median and high with n; fewer than three included analogs returns a GAP and no range.
2. **Analogs are the person's or sourced with dates.** Each has a stated basis, a source with a date on or before the reference date, one currency and one geography. Nothing is converted or inflated.
3. **No error band without a verified source.** The forecast-error study this skill cites was behind a paywall; its results were not read, so no band is applied and the script prints [CHECK] (references/rules/viability-rules.json).
4. **Thresholds are the buyer's.** A condition against a threshold is "gap" when the buyer supplied none.
5. **Upstream gaps stay gaps.** An unsigned or missing register is a "gap", never "not met": it is missing evidence, not evidence against.
6. **Price, revenue, coverage and access are not built here.** Price and revenue come from the signed register of forecast-revenue-and-price-ranges (C-RV); coverage and access come from the Market Access pack and count only when it is Released and carries records.
7. **No recommendation.** The validator rejects text that recommends an option or says the asset is or is not viable.
8. **Markets.** US and EU only; another market is a [GAP].

## Method anchoring
No published standard exists for analog-based peak-sales ranges or for a commercial go/no-go test; the method and the conditions are engineering rules of this skill, documented here. Name the source id from references/method-standards.md beside every statement that rests on a source: the forecasting study for the context on overestimation (H1), the AMNOG withdrawal study for the access failure mode (H2), the FDA statement for cross-trial comparison (H3), the Directive text for EU protection (H4).

## Connectors
- Market Access pack (vital-pharma-market-access, read-only; draft 0.1.0): access-assumption-register, launch-price-corridor-assembly, market-pathway-mapping, access-environment-and-barrier-assessment, access-scenario-inputs. See references/market-access-interface.md.
- Literature (literature_search_literature) and company filings read by a person: locate analog launches and their reported peak sales; each analog needs a dated source.
- VITAL Verify (qualify_source, check_claim, build_citation): admit a source and check a claim against a quoted passage.
- Navigator (catalogue_get; methods_scenario, methods_risk_tornado): the competency row; replaying a human-supplied formula and its sensitivity as a cross-check of the script. Never to choose analogs or thresholds.

## Quality bar
- Analog range from three or more included analogs with dated sources, or a named GAP and no range.
- option_set, analog_range and validate_register exit 0; disabled rules listed; all three options present.
- All four failure modes (MH-01 to MH-04) screened and resolved.
- At least one question for the decision owner; commercial_decision shows HUMAN ONLY and recommended_option is null; status UNSIGNED until a named reviewer signs.
- Open [CHECK] and [GAP] items, decisions (with decider) and what the Market Access pack and the valuation capability own listed at the end.
