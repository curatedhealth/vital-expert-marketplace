# Reception measures: what is sourced and what is the person's

Interpretive reference for tasks A1 and B1. Rows from `health-economics-research.md` (HE), `promotion-and-claims-research.md` (PC) and `evidence-synthesis-research.md` (ES), read 19 October 2026.

## Not sourced: the measure itself

No research row defines a reception measure, a reception score, a benchmark for payer acceptance, or a threshold for "failed". The old skill's rules stand: use the measure the person named; score only with the result the person supplied; name the line the person said failed. The measure, the codes and the flag rule are the person's.

## The log

One row per stakeholder response to one line of the narrative or dossier. Columns: `date`, `audience` (person's words), `organization`, `use` (dossier, payer meeting, ESF pack ...), `line_id`, `claim_id` (from the sibling's claim register), `response_code` (the person's codes), `note` (verbatim, short). Keep no patient-level data and no confidential deal terms in the log.

Example codes the person may choose (not sourced, illustrative only): accepted, questioned, rejected, no response.

## Sourced facts that explain what a stakeholder asked for

These help classify an objection in B1. They do not make the objection right or wrong.

| Stakeholder asked for | What the sources say | Rows |
|---|---|---|
| Budget impact on their own population | BIA inputs should reflect the decision maker's population; scenarios chosen from the decision maker's perspective. | HE-021, HE-022 ([PAPER] Sullivan et al. 2014, DOI 10.1016/j.jval.2013.08.2291, abstract only) |
| PMPM rather than a total | AMCP 6.0 draft: report PMPM difference and total budget impact; no absolute affordability threshold. | HE-138 (AMCP 6.0 draft) |
| A model they can change | AMCP 6.0 draft: modifiable electronic model with unlocked inputs. | HE-139 (AMCP 6.0 draft) |
| Savings in year one (US DHT) | ICER-PHTI: BIA over one year, 2-to-5-year scenarios where offsets accrue later. | HE-122 |
| UK costs | ESF standard 17: costs relevant to the UK, NHS and PSS resources. | HE-089 |
| Cost-effectiveness for a higher-risk purchase | ESF standard 18 applies to higher financial risk DHTs; CUA or CCA. | HE-090, HE-091 |
| Whether a result applies outside the trial population | HCEI must relate to the labeled population; communications to clinicians must stay consistent with labeling. | PC-US-37, PC-US-27 |
| Limitations, sensitivity analyses | Required context in HCEI. | PC-US-40 |
| Certainty of the effect | Certainty is per outcome and explained when below high. | ES-96, ES-99 |

HE-018 to HE-023 all come from [PAPER] Sullivan et al. 2014, DOI 10.1016/j.jval.2013.08.2291 (abstract only), although only HE-018 carries the mark in the research file. Whenever any of HE-018 to HE-023 is cited, cite the DOI with it.

## Facts that bear on keeping a dossier current

| Fact | Rows |
|---|---|
| The AMCP dossier is a living document from pre-approval through post-approval. | HE-132 |
| Information given to payors about an uncleared use should be followed up if it becomes materially outdated. | PC-US-46 |
| Out-of-date reviews risk misleading decision makers. | ES-101 |
