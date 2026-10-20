# Dossier elements: what the sources name, and what they do not

Interpretive reference for task A2. The library's `value-dossier` job ("A dossier skeleton, with every claim checked") is design-partner only and lists no tools (`examples/live/jobs_value_dossier.json`), so the skill assembles the dossier itself. It may use only elements a sourced row names. The AMCP Format 6.0 final text was not read (HE-131); its section list, numbering and content are `[GAP]` except the draft rows below. Do not invent a dossier section.

## Elements a sourced row names

| # | Element | What it holds | Rows | Status of source |
|---|---|---|---|---|
| 1 | Dossier type | A unapproved product, B approved product, C unapproved use. Decide from the cleared status the person gives. | HE-133 | AMCP 6.0 draft |
| 2 | Product information | Product description; for digital therapeutics AMCP has a subsection (5.0: under 2.1B; 6.0 draft renumbers it 2.1.1B, no new content). Its content is not sourced: `[GAP]`. | HE-135 | 5.0 final not read; 6.0 draft |
| 3 | Pre-approval product information (type A or C) | AMCP lists components "per FDA Final Guidance, the PIE Act, and AMCP Format recommendation"; the statutory content for devices is 502(gg): description and features, indications investigated, anticipated timeline, pricing, utilization projections, product-related programs, factual results; required statements. | HE-134, PC-US-08 to PC-US-10, PC-US-43 to PC-US-45 | statute; 2018 final guidance |
| 4 | Clinical evidence | The value claims from task A1, each with its passage, check status and the person's certainty rating per outcome. A review, if needed, comes from dh-clinical-validation (literature-and-real-world-evidence-review). | ES-96 to ES-99, PC-US-39 | method rows |
| 5 | Economic evaluation (type B only) | Economic value assessments apply only to approved-product dossiers. Draft 6.0: payer (HCDM) perspective primary, societal supplementary, typically 3 percent discount; QALY or evLY with supplementary measures as additions. Reported to CHEERS 2022. | HE-132, HE-136, HE-137, HE-001 to HE-014 ([PAPER] Husereau et al. 2022, DOI 10.1177/23814683211061097) | AMCP 6.0 draft; CHEERS [PAPER] |
| 6 | Budget impact analysis | Draft 6.0: horizon typically 1 to 3 years, dynamic population, PMPM difference and total impact, no absolute affordability threshold; modifiable electronic model with unlocked inputs. BIA II elements. | HE-138, HE-139, HE-018 to HE-023 ([PAPER] Sullivan et al. 2014, DOI 10.1016/j.jval.2013.08.2291) | AMCP 6.0 draft; BIA II abstract only |
| 7 | Required HCEI context | Study design and methodology, generalizability, limitations, sensitivity analyses, balanced presentation; statement of material differences from labeling where applicable. | PC-US-40, PC-US-04 | 2018 final guidance; statute |
| 8 | Model transparency | A non-technical model description for anyone; technical documentation openly or under IP-protecting agreements. | HE-016 ([PAPER] Eddy et al. 2012, DOI 10.1016/j.jval.2012.04.012) | ISPOR-SMDM, abstract only |
| 9 | Substantiation on request | Substantiation for HCEI is made available to FDA on request. | PC-US-05 | statute |

For an NHS commissioner pack, the ESF standards replace AMCP: standard 13 (impacts against current care), 17 (BIA: population and uptake, technology and implementation costs, comparator costs, UK NHS and PSS costs) and 18 (CUA or CCA for higher financial risk) (HE-086 to HE-091). The ESF is voluntary (HE-079).

## Not sourced (write `[GAP]`, name where it would come from)

- AMCP 6.0 final section list and wording; AMCP 5.0 full text; AMCP's own definition of PIE (HE research "Not sourced").
- Any device-specific or digital-therapeutics dossier content beyond the subsection's existence.
- DiGA dossier content (BfArM application) and HAS device dossier content: dh-market-access owns these.
- A dossier's "executive value summary" or "value story" section: not named by any row; if the person wants one, label it "proposed" and build it in task B1.

## Who fills what

| Element | Filled by |
|---|---|
| Type, product information, cleared indication | The person, or the owner they name for regulatory review |
| Clinical evidence claims | Task A1: checked passages; certainty by a person |
| Economic evaluation, BIA | The person's model (DH-01.07.2) or a review the person supplies; the library's `analytics.budget-impact-model` returned HTTP 422 on 19 October 2026 |
| Required context and statements | Drafted from the rows; stops for the owner the person names for regulatory or legal review, or owner not named |
