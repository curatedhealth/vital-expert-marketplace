# Check whether a source is still in force

## Formula

| Slot | In this task |
|---|---|
| Worker | Source qualifier. Does not decide support and does not sign. |
| Workflow | Identify the kind of id, call the currency check, record the time, then stop. |
| Skill | Currency check. Register code is [GAP]. |
| Knowledge | Notice table in [references/notices.md](../references/notices.md), from check_currency behavior as of 19 October 2026. |
| Tool | `check_currency` on a DOI, PMID, PMCID, catalogue document, or URL. |
| Prompt | Report the notice. Do not describe an unchecked URL as current. |
| Template | [assets/check-currency-output.md](../assets/check-currency-output.md) |
| Input | One already identified source. |
| Governance | A failed lookup is not proof the paper is in force. |

## Steps

1. If the id is a DOI, PMID, or PMCID, call `check_currency` when a key is present.
2. If it is a catalogue document, read doc_status from that call.
3. If it is a URL alone, the notices are ["not checked"]. Leave the currency axis of the score empty.
4. Record checked_at as the time of this call. Do not copy the page's "current as of" date into that field.
5. A retraction makes the source inadmissible unless the claim is that the paper was retracted.
6. Superseded or withdrawn is not gold. The currency axis is 0 when the notice is one of those.

## Checks

- The notice is one of clear, retracted, corrected, superseded, withdrawn, or not checked.
- An unchecked URL is not described as current.

## Boundaries

Do not assign supported or partial here.
