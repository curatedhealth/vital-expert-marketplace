---
name: analyze-financial-statements-and-tax
description: "Use when a buyer (pharma business development or life-sciences investor) needs the financial position of a drug-development company, or of the counterparty behind an asset, read from filed documents in the US and EU: cash and runway with the filed going-concern language, financing history and dilution, upstream licensor milestone and royalty obligations that a buyer would inherit, contingent and off-balance-sheet commitments, tax attributes flagged for a specialist, and the seller's financial claims cross-checked against filings. Produces a financial register and the questions for the accountant and tax specialist. Never gives a quality-of-earnings, net debt, accounting or tax opinion (human only). Not for valuation or deal value, not for the legal opinion on a license, not for markets other than US and EU."
metadata:
  level: CF04
  register_code: CF-01.02.06.3.1
  register_id: 24ffff27-feef-4f80-b9b6-627992a10ab8
  version: 0.1.0
  verb: analyze
  capability: CF-01.02.06 Target Evaluation & Due Diligence
  mission: CF-01.02.06.3 Financial & Legal Due Diligence
  agent: bd-due-diligence-lead
  atoms: [extract-requirements-from-source, compare-against-criteria, classify-text-labels, compose-draft]
  feeds: [determine-commercial-viability]
  tools: [scripts/runway.py, scripts/validate_register.py]
  tier: "Full (owner ruling 7 November 2026): the capability is Full; this skill is validated with a Standard-style known-answer set, built in a later lane"
  requires: []
  release_state: Draft (Q1-Q6 built; Q7 back-test pending; Q8 practitioner review pending)
---

# Analyze financial statements and tax

## What competent output looks like
- A financial register: cash and runway (from the filed liquidity disclosures, with any going-concern
  language quoted), financing history and dilution, upstream licensor milestone and royalty obligations
  taken from the filed license agreements and notes, contingent and off-balance-sheet commitments, and tax
  attributes flagged for specialist review (for example loss carryforwards and the limits on their use).
- Three modes, set at intake:
  - **company**: the full workstream above.
  - **asset**: the counterparty's ability to perform and the license obligations the buyer would inherit.
    Dilution and tax attributes are out of scope.
  - **investor**: weighted toward runway, dilution and the financing path; at least three runway scenarios.
- Runway with a stated burn basis (one of trailing operating cash flow, company guidance, management budget,
  analyst assumption), its source, and scenarios. The runway is arithmetic on supplied inputs, never a forecast.
- Seller claims (for example "runway into 2028") cross-checked against the filings, each result recorded as
  consistent, inconsistent or not found in filings, with a question for every inconsistency.
- Absent evidence is a GAP with the consequence stated (which figure cannot be computed). Never "unknown".
- Quality of earnings, the net debt definition, accounting opinions and tax opinions stay human only. The
  register shows each as HUMAN ONLY and never certifies a figure, a statement or a tax position.

## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Intake (intake.md): buyer mode, unit and mode, documents, specialists' names | none | agent asks; human supplies |
| 2 | Cash, liquidity discussion and going-concern language from the filings (task 01) | extract-requirements-from-source | agent drafts; human reviews |
| 3 | Runway with burn basis and scenarios (task 02) | scripts/runway.py | agent alone (script); human confirms the burn basis |
| 4 | Financing history and dilution (task 03) | extract-requirements-from-source; scripts/runway.py | agent drafts; human reviews |
| 5 | Upstream licensor obligations that pass to a buyer (task 04) | extract-requirements-from-source; classify-text-labels for obligation types | agent drafts; counsel reviews |
| 6 | Contingent and off-balance-sheet commitments; tax attributes flagged (task 05) | extract-requirements-from-source; scripts/runway.py tax flag | agent drafts; accountant and tax specialist review |
| 7 | Seller claims cross-checked against filings; data-room completeness (task 06) | compare-against-criteria (consistent / inconsistent / not found) | agent drafts; human reviews every "inconsistent" |
| 8 | Screen failure modes and write the questions (task 07) | compare-against-criteria (triggered / not triggered / cannot tell) | agent drafts; human reviews every "triggered" |
| 9 | Validate and write the register | scripts/validate_register.py; compose-draft with templates/financial-register.md | agent alone (script) |
| 10 | Quality of earnings; net debt definition; accounting opinion; tax opinion | none | human only |
| 11 | Materiality of an obligation or a tax limit in a deal term; sign-off of the register | none | human only |

## Rules (general, apply to every case)
1. **No certification.** `validate_register.py` rejects text that states a quality-of-earnings, net debt,
   going-concern, fair-presentation or tax conclusion. Write the question for the specialist instead.
2. **Filed language is quoted, not summarized into comfort.** If a filing carries going-concern language, the
   register quotes it. "No going-concern issue" is never written by the agent.
3. **Burn needs a basis.** No basis, no source, no runway: the calculator records a GAP and stops.
4. **Rule status.** Only VERIFIED-REOPENED rules compute. The one-year-after-issuance look-ahead of ASC 205-40
   is SUMMARY-ONLY and disabled; the script prints [CHECK] (references/rules/finance-rules.json).
5. **Tax is a flag.** The Section 382 ownership-change test is shown as a flag with the inputs; the
   limitation amount is not computed; a tax specialist decides.
6. **Dates and sources.** A figure carries its filing, period and page or note. A date the documents do not
   give is a GAP, never an estimate.
7. **Markets.** US and EU only. Another market is a [GAP].
8. **No standard for runway.** No published standard exists for burn or runway calculation; the burn-basis
   rule is an engineering rule of this skill, and the horizons come from Item 303(b)(1) and AS 2415.

## Method anchoring
Name the rule id (for example FIN-HORIZON-12M, TAX-382-OWNERSHIP-50PT) beside every flag, and the source id
from references/method-standards.md. For judgements no listed standard covers (runway method, quality of
earnings, net debt), say so and mark [CHECK]; the skill anchors on the sourced failure modes in
references/failure-modes.md and on the filings themselves.

## Connectors
- SEC EDGAR full-text and filing pages, read by a person or a read-only page reader: 10-K, 10-Q, S-1, 8-K and exhibits. No scripted bulk access.
- Company filings outside the US (EU registers and annual reports), supplied by the buyer or read by a person.
- Literature (literature_search_literature): locate a named publication. Never for company financial data.
- VITAL Verify (qualify_source, check_claim, build_citation): admit a source and check a claim against a quoted passage.
- Navigator (catalogue_get): the competency row and its siblings.

## Quality bar
- 100% of financing events, obligations, commitments, tax attributes and cross-checks: source or [CHECK]; absent fields GAP with consequence.
- Script exit 0 for runway and for the register; disabled rules listed.
- All four failure modes (FE-01 to FE-04) screened and resolved.
- At least one question for a named specialist; the four human-only fields show HUMAN ONLY; status UNSIGNED until a named reviewer signs.
- Open [CHECK] and [GAP] items, decisions (with decider) and the hand-off (this skill is standalone in company mode; its licensor obligations are the cross-check for the ownership and license chain in assess-ip-portfolio-and-freedom-to-operate) listed at the end.
