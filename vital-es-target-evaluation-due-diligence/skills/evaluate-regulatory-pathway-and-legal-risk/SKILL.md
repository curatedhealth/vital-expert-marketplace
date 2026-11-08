---
name: evaluate-regulatory-pathway-and-legal-risk
description: "Use when the clinical evidence register is signed off, the probability and timeline ranges exist, and the exclusivity register exists, and the buyer (pharma business development or life-sciences investor) needs the US and EU regulatory routes open to a drug asset (standard, priority or accelerated assessment, accelerated approval or conditional authorisation, exceptional circumstances) with precedent and confirmatory obligations, plus a legal-and-regulatory risk register: gaps between public statements and the regulatory record, manufacturing and inspection history including contract manufacturers, data integrity and compliance exposure, litigation. US and EU only; EU pharma reform is not yet law. Never gives a legal opinion or chooses the route (humans do). Not for revenue or deal value, not for patents (use assess-ip-portfolio-and-freedom-to-operate)."
metadata:
  level: CF04
  register_code: CF-01.02.06.3.3
  register_id: a45deb7a-48d3-4e8f-a942-f25bb8c0c605
  version: 0.1.0
  verb: evaluate
  capability: CF-01.02.06 Target Evaluation & Due Diligence
  mission: CF-01.02.06.3 Financial & Legal Due Diligence
  agent: bd-due-diligence-lead
  atoms: [extract-requirements-from-source, compare-against-criteria, classify-text-labels, rank-by-consequence, compose-draft]
  feeds: [determine-commercial-viability]
  tools: [scripts/validate_pathway.py, references/rules/pathway-rules.json]
  tier: "Full (owner ruling 7 November 2026): the capability is Full; this skill is validated with a Standard-style known-answer set, built in a later lane"
  requires: [review-clinical-data-quality, estimate-development-risk-and-timeline, assess-ip-portfolio-and-freedom-to-operate]
  release_state: Draft (Q1-Q6 built; Q7 back-test pending; Q8 practitioner review pending)
---

# Evaluate regulatory pathway and legal risk

## What competent output looks like
- A pathway map for each market in scope (US, EU): each candidate route (standard; priority review, fast track,
  breakthrough or accelerated approval; accelerated assessment, PRIME, conditional authorisation or
  exceptional circumstances) with every criterion of the route assessed as met, not met or a gap, each "met"
  tied to a row of the clinical evidence register, plus precedent (sourced, or a stated gap) and the confirmatory
  or specific obligations the route carries.
- The route's review clock where the references verify one, with its basis: the US priority-review goal and the
  EU 150 or 210 days excluding clock stops. Elsewhere the clock is a [CHECK].
- A legal-and-regulatory risk register: where public statements and the regulatory record differ, manufacturing
  and inspection history including contract sites, data integrity and compliance exposure, litigation (carried
  from the exclusivity register). Each row has a source or [CHECK].
- Absent evidence is a GAP with the consequence stated. Never "unknown".
- Draft guidances are marked DRAFT wherever used. EU pharma reform is not yet law: current rules are used and
  reform changes are flagged.
- The route choice and the legal opinion are marked HUMAN ONLY. The output states no regulatory outcome as certain.

## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Intake (intake.md): confirm the three upstream outputs; buyer mode, unit, markets, documents | none | agent asks; human supplies |
| 2 | List candidate routes per market with their criteria (task 01) | references/rules/pathway-rules.json; references/markets/ | agent drafts; human reviews |
| 3 | Match register findings to each criterion (task 02) | compare-against-criteria (state set: met / not met / gap) | agent drafts; human reviews every "met" |
| 4 | Precedent and confirmatory obligations per route (task 03) | extract-requirements-from-source; connectors | agent drafts; human reviews |
| 5 | Compare public statements with the regulatory record (task 04) | classify-text-labels (match / no match / contradicts); extract-requirements-from-source | agent drafts; human reviews |
| 6 | Manufacturing, inspection, data integrity and compliance exposure (task 05) | extract-requirements-from-source; connectors | agent drafts; counsel reviews |
| 7 | Litigation and legal risk, questions for counsel; rank by consequence (task 06) | rank-by-consequence | agent drafts; counsel reviews |
| 8 | Validate and write the map and register (task 07) | scripts/validate_pathway.py; compose-draft with templates/pathway-and-risk.md | agent alone (script) |
| 9 | Route choice; bid, price or term decisions; sign-off of the register | none | human only |
| 10 | Legal opinion on any exposure, compliance position or dispute | none | human only (counsel) |

## Rules (general, apply to every case)
1. **Upstream first.** A signed clinical register (skill A), ranges (skill B) and an exclusivity register
   (skill C) must exist. The script rejects a map without them (E_UPSTREAM). The route list refines B's
   timeline assumption; it does not replace B's numbers.
2. **Every criterion assessed.** A route is a candidate only with all its criteria assessed; "met" needs
   evidence from the register. A criterion you cannot assess is a gap, not a guess.
3. **Press release is not the record.** A claim in a press release, deck or abstract is compared with the
   regulatory record (complete response letter, review document, minutes). No record supplied is a GAP that
   names the consequence.
4. **Drafts are marked.** The January 2025 and December 2024 accelerated approval guidances are drafts; a route
   that rests on them sets draft_basis_acknowledged.
5. **Nothing certain.** No "will be approved", no "is compliant". The script rejects such text (engineering rule).
6. **Reform.** Every EU route carries a note that the EU pharma reform is not yet law and current rules are used.
7. **Markets.** US and EU only. Another market is a [GAP].

## Method anchoring
Name the criterion id (for example CM3) and source id (references/method-standards.md) beside every
assessment. Judgements no listed source covers (for example how a regulator will read a given dataset)
are marked [CHECK] and left to the named regulatory reviewer.

## Connectors
- FDA Drugs@FDA, FDA Surrogate Endpoint Table, EMA EPAR and medicine pages: precedent and endpoint history (read-only; the date read is recorded).
- FDA Warning Letters page, FDA Data Dashboard, EMA EudraGMDP database: inspection and certificate history of named sites (leads; read the document before relying on it).
- ClinicalTrials.gov (search_trials, get_trial_details): confirmatory trials registered and their status.
- VITAL Verify (qualify_source, check_claim, build_citation): admit a source and check a claim against a quoted passage.
- Navigator (catalogue_get): the competency row and its siblings.

## Quality bar
- 100% of routes: every criterion assessed; candidates carry a sourced precedent or a gap; confirmatory or obligation block present where the route needs one.
- 100% of risk rows: source or [CHECK]; statement-versus-record rows carry both references.
- All five failure modes (RL-01 to RL-05) screened; script exit 0.
- legal_opinion and route_choice show HUMAN ONLY; status UNSIGNED until a named reviewer signs.
- Open [CHECK] and [GAP] items, decisions (with decider) and the hand-off to the buyer's deal team listed at the end.
