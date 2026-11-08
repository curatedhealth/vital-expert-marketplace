# Tools and companion slot

## Companion slot

| Task | What the companion does | Tool | Without it |
|---|---|---|---|
| Qualify the source | Resolves an identifier into a source record with provenance fields, a tier and a source score scored against the person's question | VERIFY `qualify_source`; `ingest_document` first for a supplied PDF or text | Method runs by hand; card says "not tool-checked"; tool-only fields are `[GAP: not checkable here]` |
| Evidence strength and currency | Reports whether a paper or catalogue document is retracted, corrected, superseded or withdrawn | VERIFY `check_currency` | Method runs; ask for the date; currency "not checked" |

Never simulate a result (TR-H4). Never call a tool the person has not connected.

## Schema source

Arguments below are copied from the VERIFY connector's tool schemas as exposed in this
session on 20 October 2026 (tool list read, no tool called). Anything about returns
beyond the schema descriptions is marked `[CHECK]` and must be confirmed against a live
run before release.

## qualify_source

Schema description: "Turn a DOI, PMID, PMCID, URL, catalogue document id, or ingested
document id into a source with a tier and a source_score. Pass question so relevance is
scored. An http(s) URL is fetched for title, publisher, and date. It never searches for
a source the caller did not name."

Arguments (all optional strings in the schema; pass one identifier plus `question`):

| Argument | Put here |
|---|---|
| `doi` | A DOI, for example `10.xxxx/yyyy` (no `https://doi.org/` prefix needed) [CHECK: whether a prefixed DOI is accepted] |
| `pmid` | A PubMed id, digits only |
| `pmcid` | A PubMed Central id, `PMC` plus digits |
| `url` | An http(s) link the person supplied |
| `catalogue_id` | A VITAL catalogue document id. Schema: "servable applies only here." |
| `document_id` | An id returned by `ingest_document` for this tenant |
| `question` | The person's question, in their words. "Used only to score relevance." |

Example calls:

```
qualify_source({ "doi": "<DOI as supplied>", "question": "<the person's question>" })
qualify_source({ "url": "<link as supplied>", "question": "<the person's question>" })
qualify_source({ "document_id": "<id from ingest_document>", "question": "<the person's question>" })
```

Returns (per schema): a source with a tier and a source_score. [CHECK: field names.
The earlier vital-verify method describes provenance fields (authority, title, code,
date, status, official_url), a tier of gold, silver, bronze or inadmissible, reasons,
and a source_score with axes authority, recency, relevance, provenance and currency,
where an axis may be null. Not confirmed against a live return in this build.]

Pitfalls:

- Leaving out `question` leaves relevance without a value [CHECK: per the earlier
  method, relevance is null when no question is passed].
- A short title can score low on relevance even when it is the right page [CHECK].
  Say so; do not change the number.
- An inadmissible result: say so with the tool's reason. VERIFY's instruction: "If
  qualify_source returns inadmissible, say the fetch failed and do not invent the
  missing fields." Where the reason given is something other than a fetch (for example
  a retraction or no identifying details), report that reason instead [CHECK: whether
  inadmissible is ever returned for reasons other than a failed fetch, as the earlier
  method describes].
- Never pass a title, publisher or date you supplied yourself; the tool reads its own.

## ingest_document

Schema description: "Store passages and locators from a PDF or a URL the caller
supplies, for this tenant only. Requires verify:write and an uploader attestation. It
does not store the whole document and it does not write a shared index. Retention
defaults to 90 days."

| Argument | Put here |
|---|---|
| `pdf_base64` | A PDF of at most 10 MB, base64 |
| `text` | Pasted text, when there is no PDF [CHECK: whether text alone is accepted without a URL or PDF] |
| `url` | A link to the document |
| `metadata` | Object; what the person states about the document (title, issuing body, date) [CHECK: accepted keys] |
| `uploader_attestation` | `true` only when the person has said they may process this document. Schema: "The uploader attests they may process the document." |
| `retention_days` | Integer; defaults to 90 |

Example call:

```
ingest_document({ "pdf_base64": "<file>", "uploader_attestation": true, "metadata": { "title": "<as the person states>" } })
```

Then `qualify_source({ "document_id": "<returned id>", "question": "…" })`.

Pitfalls:

- Needs the `verify:write` scope on the key. If the call is refused, say so; do not
  qualify the document as if it had been stored.
- Ask before uploading. Confidential, unpublished or patient-containing documents go
  through the person's AI use policy first.
- Metadata the person supplies is their statement, not a fact the tool established.
  Report it as "as stated by you".
- Returns: a document id [CHECK: field name].

## check_currency

Schema description: "Report whether a named DOI, PMID, PMCID, or catalogue id is
retracted, corrected, superseded, or withdrawn. A URL alone returns notices ["not
checked"]. It does not grade the claim."

| Argument | Put here |
|---|---|
| `doi`, `pmid`, `pmcid` | The literature identifier |
| `catalogue_id` | A catalogue document id |
| `url` | A link; alone it returns "not checked" |
| `record` | Object; a source record [CHECK: whether the qualify_source result can be passed here] |

Example call:

```
check_currency({ "doi": "<DOI as supplied>" })
```

Returns (per schema): notices. [CHECK: the earlier method also records a `checked_at`
time; field names to be confirmed.]

Pitfalls:

- "Not checked" is not "clear". Never write "current" or "not retracted" from it.
- The schema names retracted, corrected, superseded and withdrawn. It does not name
  "expression of concern" [CHECK: whether expressions of concern are reported]. Until
  confirmed, say: "VERIFY does not say whether an expression of concern exists."
- A clear result for a paper is not a statement that a guideline or label citing it is
  current.
- Copy the time of the check, not the page's own "last updated" date, as the check time.

## Not used by this skill

- `check_claim`, `extract_claims`, `verify_text`: deciding support belongs to
  `claim-assessment`. VERIFY's instruction pairs qualify_source with a check_claim on a
  quoted passage from the same source; this skill hands the qualified source and the
  passage over for that step.
- `build_citation`, `build_record`, `build_evidence_table`: `citation-and-record`.

## Scripts

Run where code can execute; otherwise do the step by eye.

### `scripts/identify_source_id.py`

Reads a string and says which identifier it holds and which VERIFY argument it belongs
in. It does not resolve or check the identifier.

```
python scripts/identify_source_id.py "https://doi.org/10.1000/xyz123"
python scripts/identify_source_id.py "PMID: 12345678" --json
```

### `scripts/print_source_score.py`

Reads the JSON a qualify_source call returned and prints the total and each axis that
has a number, leaving out null axes, as VERIFY instructs. It does not compute or change
a score. Because the return shape is `[CHECK]`, it accepts a `source_score` object with
a `total` and either an `axes` object or axis keys at the same level, and stops with a
plain message if it finds neither.

```
python scripts/print_source_score.py qualify_result.json
```

## Future companion (candidate, not a commitment)

The Digital Health Library connector in this session lists tools named
`literature_check_retraction` (none, retracted, expression_of_concern or corrected),
`literature_classify_study` (rct, cohort, case_control, systematic_review,
meta_analysis, preprint, other) and `literature_grade_evidence` (CEBM 2011 or GRADE,
GRADE always draft). They could fill the evidence-strength slot. Not used by this
skill; fit to be confirmed by a lane. [CHECK]
