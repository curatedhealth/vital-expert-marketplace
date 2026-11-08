# Gap rules applied to source assessment

> **Where the marker belongs.** Use the `[GAP: …]` marker only inside a drafted deliverable. In notes, open-item lists and explanations, write the gap as a plain sentence ("Still missing: …, from …"). See `trusted-capability-map/references/gap-rules.md`.

Same format and classes as every TRUSTED skill:
`[GAP: <class> — <what is missing> — <what would close it>]`

| Class | Typical case in this skill |
|---|---|
| `not supplied` | The source itself, the published version behind a press release or preprint, the funding statement, the other studies behind "the evidence shows" |
| `not checkable here` | A field or status only VERIFY can establish (publisher of a link that cannot be opened, retraction status, source score) when VERIFY is not connected |
| `conflicting` | The preprint and the published article give different figures; two versions of a guideline say different things |
| `needs a decision` | Whether data on file or a preprint may be used for this reader, which the company's review process decides |
| `out of date or unclear date` | No date on the source; a guideline or label that may have been replaced; "current" with nothing dated |

## Mapping from VERIFY results

VERIFY's own method uses four words for a miss. Translate them into the TRUSTED classes
above so every skill reads the same way. [CHECK: VERIFY wording as described in the
earlier vital-verify method, 19 October 2026; to be confirmed against the connector.]

| VERIFY result | TRUSTED class | What the person reads |
|---|---|---|
| A provenance field came back empty (no date, no publisher) | `not supplied` | "The source does not show its date." |
| qualify_source returned inadmissible because the fetch failed | `not checkable here` | "VERIFY could not read the link. The details are not filled in." |
| check_currency returned "not checked" (URL only) | `not checkable here` | "Retraction and update status not checked: there is no DOI or PMID." |
| No source was supplied for the claim | `not supplied` | "There is no source for this yet." |

## Wording rules

- Name the exact item: "the funding statement", "the publication date", "the 2024
  version of the guideline", not "more information".
- Never hint at a value inside a gap ("probably peer reviewed", "likely 2023").
- An empty field from a tool is a missing field, not a finding. "No retraction" is a
  finding only when a currency check ran on a literature id and returned clear.
- "Not peer reviewed" is a finding only when the source is a kind that is never peer
  reviewed or says so. Otherwise it is "peer review status not confirmed".
