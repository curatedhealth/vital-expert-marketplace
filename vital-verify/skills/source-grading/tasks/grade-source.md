# Task VR-2.1 Grade one source

Maps to TRUSTED Prove `source-assessment` qualify task.

## Formula

| Slot | In this task |
|---|---|
| Worker | Evidence lead (source qualifier). Reads the identifier. Does not judge the claim. |
| Workflow | Resolve, grade, score, then stop. Currency is a separate task unless the person asks. |
| Skill | VR-2.1 Source grading |
| Knowledge | `references/rules.md`, `references/tiers-and-score.md`, `references/patterns.md` |
| Tool | VERIFY `qualify_source`; see companion slot |
| Prompt | Grade this identifier. Do not invent a missing field. |
| Template | `assets/grade-source-output.md` |
| Input | One DOI, PMID, PMCID, URL, catalogue id, or ingested-document id, plus the question when there is one. |
| Governance | Refuse to mint a date, a title, a publisher, or a code. Do not sign. VR-H1, VR-H3, VR-H4, VR-H5 |

## Companion

| State | What to do |
|---|---|
| VERIFY connected | Call `qualify_source` with the identifier and the person's question. |
| VERIFY absent | Run the method from `tiers-and-score.md` as guidance only; label not tool-checked; do not call the result gold or silver. |

## Steps

1. Take one identifier. If several are offered, grade them one at a time.
2. Call `qualify_source` when a key is present. Pass the question so relevance can be scored.
3. If the call fails or there is no key, say so and stop at method-only.
4. Read the six fields. Apply the first matching tier in the reference. The code decides; do not override it.
5. Classify anything absent with gap rules.
6. Print the score total and only the axes whose values are numbers.
7. Hand the tier and a quoted passage to support-decision. Do not decide support here.

## Checks

- The tier is one of gold, silver, bronze, inadmissible (or method-only without VERIFY).
- Every missing field is a named gap, not a filled value.

## Boundaries

Do not search past the identifier. Do not raise bronze to silver because the page looks official.
