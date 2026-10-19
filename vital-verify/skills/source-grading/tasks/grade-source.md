# Grade one source

## Formula

| Slot | In this task |
|---|---|
| Worker | Source qualifier. Reads the identifier. Does not judge the claim. |
| Workflow | Resolve, grade, score, then stop. Currency is a separate task unless the person asks. |
| Skill | Source grading. Register code is [GAP]: no CF04 binding was confirmed. |
| Knowledge | Six provenance fields and the score axes in [references/tiers-and-score.md](../references/tiers-and-score.md), taken from `mcps/verify/tiers.py` and `mcps/verify/source_score.py` as of 19 October 2026. |
| Tool | `qualify_source` with the identifier and the person's question. See [references/tools.md](../references/tools.md). |
| Prompt | Grade this identifier. Do not invent a missing field. |
| Template | [assets/grade-source-output.md](../assets/grade-source-output.md) |
| Input | One DOI, PMID, PMCID, URL, catalogue id, or ingested-document id, plus the question when there is one. |
| Governance | Refuse to mint a date, a title, a publisher, or a code. Do not sign. |

## Steps

1. Take one identifier. If several are offered, grade them one at a time.
2. If a Verify key is present, call `qualify_source`. Pass the question so relevance can be scored.
3. If the call fails or there is no key, say so and stop at method-only. Do not guess the publisher from the URL's look.
4. Read the six fields. Apply the first matching tier in the reference. The code decides; do not override it.
5. Classify anything absent with [references/gap-rules.md](../references/gap-rules.md).
6. Print the score total and only the axes whose values are numbers. Say when relevance is low because the title is short.
7. Hand the tier and a quoted passage to support decision. Do not decide support here.

## Checks

- The tier is one of gold, silver, bronze, inadmissible.
- Every missing field is a named gap, not a filled value.
- The score axes match the connector object.

## Boundaries

Do not edit catalogue tier scripts. Do not search past the identifier. Do not raise bronze to silver because the page looks official.
