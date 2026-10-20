# Task VR-2.2 Check whether a source is still in force

## Formula

| Slot | In this task |
|---|---|
| Worker | Evidence lead (source qualifier). Does not decide support and does not sign. |
| Workflow | Identify the kind of id, call the currency check, record the time, then stop. |
| Skill | VR-2.2 Currency check |
| Knowledge | `references/rules.md`, `references/notices.md`, `references/patterns.md` |
| Tool | VERIFY `check_currency`; see companion slot |
| Prompt | Report the notice. Do not describe an unchecked URL as current. |
| Template | `assets/check-currency-output.md` |
| Input | One already identified source. |
| Governance | A failed lookup is not proof the paper is in force. VR-H1, VR-H4, VR-H5 |

## Companion

| State | What to do |
|---|---|
| VERIFY connected | Call `check_currency` for DOI/PMID/PMCID or catalogue id. |
| VERIFY absent | Say currency was not checked. Do not guess from the year. |

## Steps

1. If the id is a DOI, PMID, or PMCID, call `check_currency` when a key is present.
2. If it is a catalogue document, read doc_status from that call.
3. If it is a URL alone, the notices are ["not checked"]. Leave the currency axis empty.
4. Record checked_at as the time of this call.
5. A retraction makes the source inadmissible unless the claim is that the paper was retracted.
6. Superseded or withdrawn: currency axis 0; not gold.

## Checks

- Notice is one of clear, retracted, corrected, superseded, withdrawn, or not checked.
- An unchecked URL is not described as current.

## Boundaries

Do not assign supported or partial here.
