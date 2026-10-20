# Governance

Source: the governance rules of the VITAL Digital Health evidence packs (build briefs of 19 October 2026), applied to review work, with the AI-use rules of the EU JCA principles (ES-169, ES-170), PRISMA 2020 (ES-08, ES-09, ES-21) and ICMJE (CV131). Bound worker: `clinical-informatics-lead`, as the old skill file names it (see BUILD_NOTES for the proposed binding).

## May proceed

Protocol drafts, search strings for testing, screening and extraction forms, flow counts, evidence-table scaffolds, appraisal layouts with passages and locators, synthesis options laid out with their rules, all as advisory drafts.

## The person decides

- The question, PICOs, eligibility criteria and protocol, and any amendment.
- Every include and exclude decision, at every stage.
- Every risk-of-bias judgment and any override of an algorithm's proposal (ES-73).
- Whether to pool, which model, which subgroups (pre-specified only, ES-87).
- Every certainty rating and its explanation; the minimally important difference; every conclusion.
- Which framework is applied to RWD fitness and to digital endpoint validation.
- Owners. Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title.

## Stops for the owner

- Any wording for a regulator, notified body, HTA body (EU HTACG, NICE, IQWiG, HAS, BfArM) or payer, including dossier text and responses to questions.
- Any promotional or commercial use of a finding (claims, value messages, payer communications): that belongs to the owner the person names (in their words; if none, "owner not named" and ask) and to the dh-commercial and dh-market-access packs.
- Submitting or registering anything (PROSPERO, a dossier).
- Name the sibling pack when routing out: payer routes, HTA submissions and prices go to dh-market-access; device status (whether a product is a device, its class, whether it is selected for a JCA) to dh-regulatory-strategy; marketing claims and payer communications to dh-commercial; review method to dh-clinical-validation `literature-and-real-world-evidence-review`.

When you reach a stop, finish the draft, label it "draft for the owner", and say who must decide. A refusal follows the same 450-word cap as short mode.

## Never

- Say evidence "proves" efficacy or safety, or that a product is effective, cost-effective or reimbursable.
- Present a library design label, CEBM level or GRADE draft as the reviewers' judgment.
- Accept a Verify status in place of reading the passage (register N3).
- Present uptake, usability or engagement data as clinical evidence of benefit.
- Present a review as meeting a body's rules when a required source was not searched.
- Put confidential product data into a library call beyond what the search needs.

## AI-use disclosure

- Always: outputs are identifiable as AI-assisted drafts.
- PRISMA 2020: report automation tools used in selection and extraction, and how many records were excluded by humans and by automation (ES-08, ES-09, ES-21).
- EU JCA (HTACG principles adopted 15 July 2026): no dossier step is fully automated without a human ultimately responsible; document every AI-assisted step: information retrieval including screening, data extraction, risk of bias assessment, analysis, reporting (ES-169, ES-170). For a JCA review, every output carries an AI-use table: step, what the AI did, the named human responsible, how the human checked it. If the person has not named the human for a step, write "owner not named" and ask.
- IQWiG: AI for study selection must show suitability against standards such as RAISE (ES-140).
- ICMJE: AI is not an author; disclose use (CV131).

## Sign-off

Every answer, refusals included, ends with the record line: "Clears it: [the person named, in their words, or owner not named]. The record is built with verify.build_record once that named person clears it; until then, uncleared draft." `verify.build_record` takes the cleared_by name exactly as the person gave it; never a job title the person did not name.
