# Rigor checks: interpretive reference

What to look at, per result, when judging how much weight an outcomes study can bear. Every rule names its row; the quotes are in the three `*-sources.md` files (read 19 October 2026). This file interprets; where it and a row disagree, the row wins. The judgments themselves are the reviewers'.

## 1. Pick the tool by design and by audience

| Design of the result | Tool | Row | Note |
|---|---|---|---|
| Comparative non-randomized study (cohort, case-control, EHR or claims comparison) | ROBINS-I (2016, [PAPER] Sterne et al. BMJ 2016, DOI 10.1136/bmj.i4919) | ES-75, ES-164 | EU JCA validity guidance asks for ROBINS-I at outcome level (ES-164). NICE asks for a validated tool for non-randomized studies (ES-131). |
| Randomized trial, Cochrane-style review | RoB 2 (current version 22 August 2019) | ES-69, ES-70 | |
| Randomized trial, EU JCA dossier | RoB 1 | ES-163 | Conflict with Cochrane's RoB 2: be ready to present RoB 1 for JCA (ES "Changes and conflicts"). |
| Uncontrolled before-after | ROBINS-I; usually serious or critical | ES-78 | |
| ROBINS-I V2 | Draft, cohort studies only, subject to change | ES-80, ES-81, ES-82 | Do not use as the published tool; HTACG cites the 2016 version. |

Assessments are per result, not per study (ES-70 for RoB 2; ES-164 per outcome for JCA). A study with three outcomes can carry three different levels.

## 2. ROBINS-I 2016: domains, levels, and what the sources fix

Seven domains (ES-75): confounding and selection of participants (before intervention); classification of interventions (at intervention); deviations from intended interventions, missing data, measurement of outcomes, selection of the reported result (after).

Levels per domain: Low (comparable to a well-performed randomized trial), Moderate, Serious, Critical (too problematic to provide useful evidence), No information (ES-76).

Fixed by the sources: critical in at least one domain means critical overall, and the result should not be included in any synthesis (ES-77). Low risk of bias due to confounding is exceptional (ES-79). The overall level when no domain is critical is not in the sourced rows `[GAP]`: it is the person's rule (A2), with "least favorable domain" available as a proposal.

V2 (draft) adds algorithms, a triage section mapping straight to critical, and immortal-time questions in classification and selection (ES-81, ES-82). Immortal time is worth asking about in any app study where "users" are defined by later use; cite it as a V2 draft question.

## 3. RoB 2: domains, levels, overall

Five domains (ES-71): randomization process, deviations from intended interventions, missing outcome data, measurement of the outcome, selection of the reported result. Signalling answers: Yes, Probably yes, Probably no, No, No information (ES-72). Domain levels: Low, Some concerns, High, proposed by an algorithm that reviewers may override with justification (ES-73). Overall: the least favorable domain; several "some concerns" can add up to high (ES-74).

## 4. Facts to lay out per domain (no judgment)

For each domain, A1 lists what the paper says and where, so reviewers can judge. Typical facts for a real-world app study:

| Domain | Facts to find in the paper |
|---|---|
| Confounding | Adjustment method (weighting, matching, regression), covariates named, whether time-varying confounding is discussed; comparator group and period (concurrent or historical) |
| Selection of participants | Who entered the cohort and when follow-up started relative to app start; exclusions after start |
| Classification of interventions | How "user" is defined (prescribed, activated, used for N weeks) and whether it depends on later events |
| Deviations | Discontinuation, switching, co-interventions, and how they were handled |
| Missing data | Complete-case or other handling; counts analyzed against counts eligible |
| Measurement of outcomes | Source (claims code, EHR field, self-report), whether the definition was validated (CV80, CV81), whether assessors knew exposure |
| Selection of the reported result | Prespecified plan available, registration, changes after outcome access (section 6) |

## 5. Is the data fit for purpose?

Name one framework and apply it (CV "Changes and conflicts"): ICH E6(R3) Annex 2, reliability = accuracy, completeness, provenance, traceability, relevance = key data elements for the question (CV23); FDA drugs, reliability = accuracy, completeness, traceability, relevance = key variables and enough representative patients (CV79); FDA devices, reliability = accrual, quality, integrity, relevance = availability, timeliness, generalizability (CV91, CV92). Operational definitions validated against a reference (CV81). Claims continuity of coverage (CV83). Traceability establishes provenance (CV82).

## 6. Was the plan fixed before outcomes were seen?

- FDA devices: protocol and analysis plan finalized before reviewing outcome data, and the submission states whether (CV94). FDA drugs: finalized before prespecified analyses; revisions date-stamped with reasons (CV75).
- HETE studies: declared a priori, registered publicly before analysis, results with a conformance or deviation statement (HE-026, HE-027, HE-028) ([PAPER] Berger et al. 2017, DOI 10.1002/pds.4297).
- Subgroup conclusions are reliable only if pre-specified (ES-87).
- The library searches only ClinicalTrials.gov for registrations (`references/tools.md`); a missing link is not proof of no registration.

## 7. Reporting completeness is not quality

STROBE (22 items) is a reporting guide, not a quality appraisal tool (CV123, [PAPER] DOI 10.1371/journal.pmed.0040296); item wording is not sourced `[GAP]`. CHEERS 2022 has no validated scoring system and using it as a score is strongly discouraged (HE-005). Report missing items; never turn a checklist count into a quality score.

## 8. Currency, retraction, trustworthiness

- Examine retraction notices and errata for included studies, and again at update (ES-119, ES-120). Retracted status is not displayed consistently (ES-123). Comments may warn of future retraction (ES-122).
- IQWiG: untrustworthy studies may be flagged and tested by a sensitivity analysis without them; data the submitter will not allow to be published cannot be used (ES-144).
- NICE HealthTech: unpublished company evidence needs enough detail to judge it against published evidence (ES-134).

## 9. From risk of bias to certainty (context, not a rating)

GRADE has four levels (ES-89); non-randomized evidence starts low (ES-90); sound non-randomized studies are generally graded low even with ROBINS-I (ES-100; the chapter's own figure suggests otherwise, see ES "Changes and conflicts"); rating down for risk of bias is one of five domains (ES-91); certainty is per outcome (ES-96); GRADE is judgment, not a score (ES-94); any rating other than high is explained (ES-99). The library's GRADE output is a draft scaffold with empty factors (`references/tools.md`). The rating is the person's or the HTA body's.

## 10. Conflicts of interest and funding

Note who funded the study and the funder's role, as the paper states it (CHEERS item 27 and 28 for economic evaluations, HE-014). Reviews should be done by a team free of potential conflicts (ES-42). State the facts; do not infer intent.
