# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them. Counted calls draw on the key's monthly allowance; an error says "Nothing was counted".

Behavior observed in live calls on 19 October 2026 with illustrative numbers; saved outputs in `examples/live/` (shared with the sibling skill economic-model-development, which measured the same calls). Every analytics tool computes only on numbers the person supplies.

## verify.qualify_source and verify.check_claim (published inputs and the rules a model cites)

- Sequence: `qualify_source` with the DOI (or PMID or URL), then `check_claim` with the claim, the verbatim passage (`text`, `locator`) and the full returned source object (register C18).
- Live: the CHEERS 2022 DOI 10.1177/23814683211061097 rated "gold" (PMID 35036563, retraction status none).
- Pitfall (method rules): the item 10 rule in the passage's own words came back "partial", rationale "the passage does not state the figure". The tool expects a number; a method rule is not a figure. For a rule, read the passage yourself and cite the HE row; do not count "partial" as a failure of the model.
- Pitfall (direction, register N3): a claim stating the opposite of its passage ("CHEERS 2022 provides a validated quality score") came back "unsupported" (11 percent overlap), not "contradicted". Accept an input only when you have read the passage and it states the figure in the same direction.
- Pitfall (register C1): the NICE PMG48 methods page URL was rated "inadmissible, no provenance". Do not send NICE rules to Verify; cite their HE rows.
- Pitfall (register C18): `check_claim` citations return `doi: null` and `year: null`; cite from the `qualify_source` result.

## verify.check_currency

Use on a DOI behind a model input before treating it as current (retraction, correction, supersession). Not measured in this build; `check_claim` returned a `currency` block (retracted, corrected, superseded, withdrawn all false for CHEERS 2022), which is the same information for an already qualified source.

## verify.build_record

Needs a named human in `cleared_by`; refuses a model or tool name. Use only when a review leaves the conversation.

## analytics.scenario-modeler (recomputation and monitoring runs)

- Exposed and working on 19 October 2026. `parameters`, `formula` over the names and `t` (from 0), `periods`, `aggregate`. Powers need `**`; `^` returns HTTP 400. `aggregate: "none"` still returns cumulative values.
- Use it to verify a reported number independently (HE-017 verification, DOI 10.1016/j.jval.2012.04.012; HE-023, DOI 10.1016/j.jval.2013.08.2291): rebuild the reported arithmetic as one formula and compare. Live: `population * uptake * (device_cost - offset)` returned 65,000, 130,000, 195,000, matching `scripts/he_model.py`.

## analytics.risk-tornado

- Exposed and working. Skips list parameters; applies plus or minus 20 percent where no range is given; ranked a sign-flipped ICER (-2,016) as the smallest swing with no flag. When reviewing a model's tornado, check whether it was run on a ratio and whether the ranges were the modeler's or a default.

## analytics.budget-impact-model

- HTTP 422 on three payload shapes on 19 October 2026 (register N5). For recomputing a BIA use the scenario modeler or `scripts/he_model.py`.

## Catalogue jobs

No catalogue job covers model validation or monitoring (`find_job {query: "economic model cost-effectiveness"}` returned none). Formula rows say "none".

## Scripts

- `scripts/cheers_check.py` CHEERS 2022 sourced-item completeness and reference-case check on the person's model description; no score.
- `scripts/he_model.py` and `scripts/sensitivity_summary.py` (copied from the sibling skill): recompute the person's model from its inputs, and run the person's observed values as scenarios against the base case.

## Not used here

`watch_*` tools; literature searching (dh-clinical-development literature-and-real-world-evidence-review owns the review method).
