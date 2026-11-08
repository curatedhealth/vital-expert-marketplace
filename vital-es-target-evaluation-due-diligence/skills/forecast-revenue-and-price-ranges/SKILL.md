---
name: forecast-revenue-and-price-ranges
description: "Use when a buyer (pharma business development or life-sciences investor) needs a deal-level estimate of revenue and price for a drug asset, as unrisked and undiscounted RANGES, country by country (US, Germany, France, Italy, Spain, UK), after the market register (patients), the development risk and timeline ranges (launch years, probability of success) and the exclusivity register (end dates) exist: patients x uptake x adherence x list price, with net price kept apart as a deal-team assumption, loss-of-exclusivity erosion from the exclusivity end date when erosion parameters are supplied, a sensitivity table for every driver and the probability of success shown beside the ranges. Never a single forecast, never risk-adjusted or discounted (that belongs to the deal valuation capability), never a recommendation on which forecast to adopt (a human decides). Not for local or regional reimbursement, coverage or access (that is the Market Access pack, shown only as a side-by-side cross-check)."
metadata:
  level: CF04
  register_code: CF-01.02.06.2.2
  register_id: 791f804b-d543-4bbc-8165-ab3e4438e81a
  version: 0.1.0
  verb: forecast
  capability: CF-01.02.06 Target Evaluation & Due Diligence
  mission: CF-01.02.06.2 Commercial & Market Assessment
  agent: bd-due-diligence-lead
  atoms: [extract-requirements-from-source, compare-against-criteria, compose-draft]
  feeds: [determine-commercial-viability, deal valuation capability (future; owns risk adjustment and discounting)]
  tools: [scripts/forecast_range.py, scripts/validate_register.py]
  tier: "Full (owner ruling 7 November 2026): the capability is Full; this skill is validated with a Standard-tier known-answer set (owner ruling R6)"
  requires: [evaluate-market-opportunity-and-competitive-position, estimate-development-risk-and-timeline, assess-ip-portfolio-and-freedom-to-operate]
  release_state: Draft (Q1-Q6 built; Q7 known-answer set designed, not run; Q8 practitioner review pending)
---

# Forecast revenue and price ranges

## What competent output looks like
- A revenue and price register for one asset (company unit: one per pipeline asset, then a side-by-side roll-up):
  1. **Per country, in its own currency** (US, DE, FR, IT, ES, UK; there is no "EU" price; another market is a [GAP]): addressable patients (from the market register), launch year as early, mid and late (from the timeline ranges), the uptake path from analogs with their sources, adherence where supplied, and **list price from a dated public source** where one exists.
  2. **Net price kept separate from list.** Net is an assumption range set by a named deal-team member and labelled so; no default ratio is shipped (rule FC-NET-DEFAULT-RATIO is [CHECK]). List and net revenue are separate fields.
  3. **Revenue as low, mid and high ranges**, unrisked and undiscounted: peak-year revenue, cumulative revenue over the horizon and, when the exclusivity end date is known, cumulative revenue up to that date.
  4. **Loss-of-exclusivity erosion** applied from the exclusivity end year only when erosion parameters with a source reference are supplied; otherwise revenue after the end year is shown unadjusted with a [CHECK] and a GAP (no default curve exists).
  5. **A sensitivity table for every driver** (patients, uptake, adherence, list price, net ratio, launch year, erosion), ranked by effect.
  6. **The probability of success displayed beside the ranges, never applied**, and the statement that no risk adjustment and no discounting are done here.
  7. **Market Access outputs, when available, as side-by-side cross-check columns**, never merged and counted only when the pack is Released.
- Absent evidence is a GAP with the consequence stated. Never "unknown".
- No single forecast, no recommendation, no risk-adjusted or discounted figure. The forecast the deal team adopts is human only.

## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Intake (intake.md): buyer mode, unit, countries, thresholds, who adopts the forecast | none | agent asks; human supplies |
| 2 | Read patients, launch years, probability of success and exclusivity end dates from the upstream registers (task 01) | extract-requirements-from-source | agent drafts; human reviews |
| 3 | Collect list prices per country from dated public sources (task 02) | extract-requirements-from-source; connectors | agent drafts; human reviews every price |
| 4 | Record the deal team's net price assumption ranges (task 03) | extract-requirements-from-source (the team's statement is the source) | agent drafts; deal team sets and confirms |
| 5 | Collect the uptake path from analogs and the erosion parameters (task 04) | extract-requirements-from-source; connectors | agent drafts; human reviews every analog |
| 6 | Compute ranges and the sensitivity table (task 05) | scripts/forecast_range.py | agent alone (script); human confirms the inputs |
| 7 | Screen failure modes and write the questions (task 06) | compare-against-criteria (triggered / not triggered / cannot tell) | agent drafts; human reviews every "triggered" |
| 8 | Validate and write the register (task 07) | scripts/validate_register.py; compose-draft with templates/revenue-register.md | agent alone (script) |
| 9 | Net price assumption ranges; which analogs count; erosion parameters | none | human only (deal team) |
| 10 | Which forecast the deal team adopts | none | human only |

## Rules (general, apply to every case)
1. **Ranges only.** Low, mid and high for every figure; never a single point.
2. **Unrisked and undiscounted.** The calculator rejects discount, risk-adjustment and NPV inputs (E_DISCOUNT, E_RISK_ADJUST). Probability of success is shown beside the ranges and never applied (owner ruling R4).
3. **Country by country, own currency.** No "EU" price. A conversion needs a dated, sourced rate supplied by the team; mixed currencies are rejected for a total; nothing is converted or inflated.
4. **List and net kept apart.** List is a dated public source or a labelled team assumption; net is an assumption set by a named person and never above list.
5. **No default curves.** There is no default uptake curve, no default net ratio and no default erosion curve; each is a [CHECK] rule (references/rules/forecast-rules.json). The team supplies them with sources.
6. **Market Access is a cross-check.** Outputs of the Market Access pack appear in separate columns and are not merged (owner ruling R1).
7. **No forecast error band.** Forecasts of sales are known to run high (VP-H-001, VP-H-010); that is context, and no correction is applied.
8. **Upstream gaps stay gaps.** A missing patient number, launch year or exclusivity date makes that country or that step a GAP; it is never estimated.

## Method anchoring
No published standard exists for deal-level revenue forecasting arithmetic, for net-to-list ratios or for erosion curves; the arithmetic and the checks are engineering rules of this skill (references/method-standards.md, references/grounding-register.md). The eligible-population by treatment-share structure follows the payer-side budget impact method (VP-R-050, VP-R-051), which is a payer method, not a seller forecast standard. Public price sources and their limits are in references/source-register.md and references/markets/. Name the rule id (for example FC-NET-ASSUMPTION) beside every figure.

## Connectors
- Market Access pack (vital-pharma-market-access, read-only; draft 0.1.0): side-by-side cross-check only (references/market-access-interface.md).
- Public price pages (CMS ASP and NADAC files; NHSBSA Drug Tariff; AIFA transparency lists; the Spanish nomenclator; BDPM; GKV-Spitzenverband overview), read by a person or downloaded by the team: each price needs a dated source.
- Literature (literature_search_literature) and company filings read by a person: analog launches and their reported sales or share.
- VITAL Verify (qualify_source, check_claim, build_citation): admit a source and check a claim against a quoted passage.
- Navigator (catalogue_get; methods_scenario, methods_risk_tornado): the competency row; replaying a human-supplied formula and its sensitivity as a cross-check of the script. Never to choose inputs.

## Quality bar
- Every country either computed from sourced inputs or a named GAP with the consequence.
- forecast_range and validate_register exit 0; disabled rules listed as [CHECK]; the sensitivity table covers all seven drivers.
- All six failure modes (FR-01 to FR-06) screened and resolved.
- At least one question for the named reviewer; adopted_forecast shows HUMAN ONLY and recommended_forecast is null; status UNSIGNED until a named reviewer signs.
- Open [CHECK] and [GAP] items, decisions (with decider) and what the Market Access pack and the deal valuation capability own listed at the end.
