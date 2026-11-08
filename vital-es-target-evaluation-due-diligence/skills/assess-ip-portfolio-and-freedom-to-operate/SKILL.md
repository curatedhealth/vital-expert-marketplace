---
name: assess-ip-portfolio-and-freedom-to-operate
description: "Use when a buyer (pharma business development or life-sciences investor) needs the patent and exclusivity picture of a drug asset, or of each pipeline asset of a company, in the US and EU: patent families and claim types, expiry with patent term extension or SPC, regulatory exclusivities, the later of patent or regulatory protection per market, the license and ownership chain with inherited licensor obligations, live disputes, and the questions counsel must answer. Produces an exclusivity register. Never states a freedom-to-operate conclusion (a legal opinion for counsel). Not for the regulatory route (use evaluate-regulatory-pathway-and-legal-risk), not for revenue or deal value, not for markets other than US and EU."
metadata:
  level: CF04
  register_code: CF-01.02.06.3.2
  register_id: ac222c01-a7d7-425e-abd9-66adea5c6c66
  version: 0.1.0
  verb: assess
  capability: CF-01.02.06 Target Evaluation & Due Diligence
  mission: CF-01.02.06.3 Financial & Legal Due Diligence
  agent: bd-due-diligence-lead
  atoms: [extract-requirements-from-source, classify-text-labels, compare-against-criteria, compose-draft]
  feeds: [evaluate-regulatory-pathway-and-legal-risk, determine-commercial-viability]
  tools: [scripts/exclusivity_dates.py, scripts/validate_register.py]
  tier: "Full (owner ruling 7 November 2026): the capability is Full; this skill is validated with a Standard-style known-answer set, built in a later lane"
  requires: []
  release_state: Draft (Q1-Q6 built; Q7 back-test pending; Q8 practitioner review pending)
---

# Assess IP portfolio and freedom to operate

## What competent output looks like
- An exclusivity register per asset (company unit: one per pipeline asset, then a side-by-side roll-up):
  patent families with claim types (composition, method of use, formulation, process), US and EU expiry
  including patent term extension and SPC, regulatory exclusivities, and the effective exclusivity date per
  market as the later of patent or regulatory protection.
- Both effective dates shown: all patents, and composition patents only. A person chooses which counts.
- The license and ownership chain for each family, including obligations that pass to a buyer from an
  upstream licensor (royalty, milestone, change of control, assignment, sublicense, field).
- Live disputes and challenges listed with their source and status.
- The questions for counsel, written so counsel can answer them. The freedom-to-operate opinion stays
  human only; the register never says an asset is free to operate or does not infringe.
- Absent evidence is a GAP with the consequence stated (which period or date cannot be computed). Never "unknown".
- Every period and formula comes from references/rules/exclusivity-rules.json; a rule not verified against
  a primary text is disabled and shows [CHECK].
- EU pharma reform is not yet law: current rules are used and reform changes are flagged.

## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Intake (intake.md): buyer mode, unit, markets, documents, counsel's name | none | agent asks; human supplies |
| 2 | Patent family table from the seller's list and registers (task 01) | extract-requirements-from-source; classify-text-labels for claim types | agent drafts; human reviews |
| 3 | Ownership and license chain, with inherited obligations (task 02) | extract-requirements-from-source | agent drafts; counsel reviews |
| 4 | Disputes and challenges (task 03) | connectors; supplied documents | agent drafts; counsel reviews |
| 5 | Compute exclusivity and term dates (task 04) | scripts/exclusivity_dates.py | agent alone (script); human confirms inputs |
| 6 | Screen failure modes and write the questions for counsel (task 05) | compare-against-criteria (state set: triggered / not triggered / cannot tell) | agent drafts; human reviews every "triggered" |
| 7 | Validate and write the register (task 06) | scripts/validate_register.py; compose-draft with templates/exclusivity-register.md | agent alone (script) |
| 8 | Which patents count toward the effective date; sign-off of the register | none | human only |
| 9 | Freedom-to-operate opinion; validity, enforceability and infringement judgements | none | human only (counsel) |

## Rules (general, apply to every case)
1. **No FTO conclusion.** The script `validate_register.py` rejects text that says an asset is free to operate,
   does not infringe, or has no blocking patents. Write the question for counsel instead.
2. **Dates from inputs.** A date the documents do not give is a GAP. The calculator never estimates one.
3. **Rule status.** Only VERIFIED-REOPENED rules compute. Disabled rules print [CHECK] and are listed in the register.
4. **One patent extended.** Patent term extension (US) applies to one patent for the same regulatory review
   period; the SPC (EU) to the basic patent. Name the patent in the input.
5. **Both effective dates.** Show all-patents and composition-only; do not pick one.
6. **Markets.** US and EU only. Another market is a [GAP], never a guess.
7. **Landscape is not an opinion.** The WIPO guidelines describe a freedom-to-operate report as a request for
   a legal opinion with a very specific, country-specific search of in-force claims; this skill prepares the
   landscape and the questions only (references/method-standards.md, S12).

## Method anchoring
Name the rule id (for example US-PTE-CAP-14Y) beside every date, and the source id from
references/method-standards.md. For judgements no listed standard covers (freedom-to-operate method), say so
and mark [CHECK]; the skill anchors on the sourced failure modes in references/failure-modes.md and on documented practice (S12).

## Connectors
- FDA Orange Book and Purple Book (public databases): patent and exclusivity listings for a US approved product. Listings are the buyer's lead, not proof of validity.
- USPTO PTAB, EPO register, Unified Patent Court: challenge and opposition status. Read-only; the status is as of the date read.
- Literature (literature_search_literature): locate a named publication. Never for finding third-party patents.
- VITAL Verify (qualify_source, check_claim, build_citation): admit a source and check a claim against a quoted passage.
- Navigator (catalogue_get): the competency row and its siblings.

## Quality bar
- 100% of families and ownership rows: source or [CHECK]; absent fields GAP with consequence.
- Script exit 0 for dates and for the register; disabled rules listed.
- All four failure modes (IP-01 to IP-04) screened and resolved.
- At least one question for counsel; fto_opinion shows HUMAN ONLY; status UNSIGNED until a named reviewer signs.
- Open [CHECK] and [GAP] items, decisions (with decider) and the next skill (evaluate-regulatory-pathway-and-legal-risk) listed at the end. The effective exclusivity dates (both views) are a condition in determine-commercial-viability. Cross-check: licensor obligations found by analyze-financial-statements-and-tax are matched against the ownership and license chain.
