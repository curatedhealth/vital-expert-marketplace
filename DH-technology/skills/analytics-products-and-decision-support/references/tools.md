# Library tools used by this competency

Connector: VITAL Digital Health Library (`mcp.vital.expert`). Names below are the library's; your assistant may prefix them (for example `analytics_rice`). Counted calls draw on the library key's monthly allowance; a call that returns an error says "Nothing was counted".

**How this file was built.** The connector was not connected during this build (checked 20 October 2026: no `Vital_Digital_Health` tools were available), so no call was made. Every behavior below comes from live outputs saved on 19 October 2026 by earlier builds, copied into `examples/live/` (file named on each entry, read 20 October 2026). Where a tool has no saved output for this skill's use, the step is marked **needs a live check**. Most of this skill runs on the sourced references and the person's own files; the library is used only for arithmetic on the person's scores and inputs, for reading a published paper, and for the record.

## analytics.rice (counted; A1, only on the person's scores)

- Arguments: `initiatives`, each `id`, `reach`, `impact` (0.25, 0.5, 1, 2 or 3), `confidence`, `effort`.
- Saved: `rice_percent_confidence.json` (19 October 2026, illustrative inputs): with confidence 80, 100 and 50 the tool returned scores 2.1333, 6 and 0.375 and printed confidence as 0.8, 1 and 0.5. `scripts/metric_check.py rank --input examples/live/rice_percent_confidence.json` reproduces all three.
- Pitfalls: confidence must be a whole percent (80, not 0.8); given 0.8, a sibling build saw scores 100 times too small (register N5 notes the analytics schema issues). The method cites a vendor article (McClure, Intercom 2016): a calculator the person chooses, not a sourced rule.
- Never call it with proposed scores. The rank is arithmetic on the person's scores, never the funding decision.

## analytics.mcda (counted; A1, only if the person scores on weighted criteria)

- Arguments: `alternatives` (each `id` and `scores`, criterion to a number on 0 to 4) and `criteria_weights` (the person's weights, summing to 1).
- Saved: `mcda_enablement_options.json` (19 October 2026, illustrative inputs): method "EVIDEM Multi-Criteria Decision Analysis (weighted-sum, 0-4 scale)"; values 80, 60 and 55 with contributions. `scripts/metric_check.py rank` reproduces all three and prints tie points.
- Pitfalls (register C17): every criterion is read as higher-is-better; name criteria so higher is better ("effort avoided", not "effort"). No robustness view: the script prints tie points. A missing score returned HTTP 400 in a sibling build, nothing counted: drop an unscored option and list it as not ranked.

## analytics.scenario-modeler (counted; A1, value-case arithmetic on the person's inputs)

- Saved: `analytics_calls_2026-10-19.json` (illustrative inputs). Arguments `parameters` (name to number, or a list with one value per period), `formula`, `periods`, `aggregate` (`sum`, `cumulative` or `none`). `population * uptake * (device_cost - offset)` with 10000, [0.05, 0.1, 0.15], 250, 120 returned 65,000, 130,000 and 195,000 (cumulative 390,000).
- Pitfalls: `^` is rejected with HTTP 400 (use `**`); `t` starts at 0, so period 0 is undiscounted; `aggregate: "none"` still returns cumulative values. Every output is "arithmetic on your inputs, not a forecast".
- `analytics.risk-tornado` (same file) applies plus or minus 20 percent to any parameter without a range and skips list parameters; if used for a value case, pass the person's range for every parameter and say when the default applied.

## literature.get_record and verify.qualify_source, verify.check_claim (counted; A1 and B1, only for a [PAPER] row the answer leans on)

- Saved: `literature_get_record_proctor.json` (`{doi: "10.1007/s10488-010-0319-7"}`, 19 October 2026): the library gives year 2010 (online first) while the research row labels the paper Proctor 2011; cite by DOI. `verify_proctor.json` (19 October 2026): `qualify_source` rated the paper "gold"; `check_claim` returned "supported" for the penetration formula and also "supported" (38 percent overlap) for a distorted claim about licenses sold (register N3: accept a claim only with a passage read in the same direction); the citation block came back with title null (register C18).
- The same file shows the NICE ESF page rated "inadmissible", "no provenance" (register C1). Research rows already carry URL, verbatim quote and read date: cite them directly.
- For DECIDE-AI, Kahn, FAIR, Rajkomar and Paulus and Kent: **needs a live check** (no saved output for these DOIs).

## verify.build_record (counted)

- Saved: `verify_build_record_refusal.json` (19 October 2026): `{cleared_by: {name: "Claude"}}` returned "build_record refuses a record without a human cleared_by.name". Call it only when the output leaves the conversation and the person names who clears it.

## Catalogue jobs

- `list_jobs_2026-10-19.json` (19 October 2026) lists no job for analytics products, metric certification or decision support design. `partner-prioritization` runs `analytics.mcda` and `analytics.rice` but is scoped to partners and indications; call the calculators directly. Every task's formula row says "Catalogue job: none".

## Not used here

- `regulatory-dh.*`: device status of decision support software is `dh-regulatory-and-quality` regulatory-pathway-and-classification.
- Every `watch_*` tool: never called.
- `analytics.budget-impact-model` and `analytics.vba-price-anchor`: payer economics, `dh-access-and-value` economic-model-development (the saved file shows budget-impact-model returning HTTP 422 on three argument shapes).
