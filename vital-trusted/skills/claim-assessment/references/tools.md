# Tools and companion slot

Source: VERIFY connector tool schemas and operating instructions as exposed to this
session, read on 20 October 2026. The tools were not called. Anything below that the
schema does not state is marked `[CHECK]` for the owner's cross-check against VERIFY.

## Companion slot

| Task | What VERIFY would do | Tool | Without it |
|---|---|---|---|
| Part A: break into claims | Split the text into claims with exact offsets | `extract_claims` | `scripts/split_claims.py` or a split by hand; "manual, not tool-checked" |
| Part B: decide support | Test each claim against its quoted passage and return a status with the deciding passage | `check_claim`, `verify_text` | Manual comparison with manual result words; "not tool-checked" |

Never simulate a result (TR-H4).

## extract_claims

Schema description: "Split a text of at most 20,000 characters into claims with offsets.
Call it before check_claim. It never decides whether a claim is supported."

| Argument | Type | Required | Schema says |
|---|---|---|---|
| `text` | string | yes | "The text to split. At most 20,000 characters." |
| `granularity` | string, enum `["sentence"]` | no | "sentence (default)." |

Call:

```
extract_claims({ "text": "<the text exactly as submitted>" })
```

Returns: claims with offsets (schema). `[CHECK]` The earlier vital-verify method says each
claim also carries a kind (factual, numeric, causal, comparative, normative,
definitional), a checkable flag, entities and cited markers; the schema does not list
return fields.

Pitfalls:

- Send the text as submitted. Offsets point into that exact text; a cleaned copy breaks
  them and checks a different text (pattern C1).
- Over 20,000 characters: split at paragraph breaks and call once per part.
- Only sentence granularity exists. Two facts in one sentence come back as one claim.

## check_claim

Schema description: "Decide whether a given passage supports a given claim. Call it after
qualify_source has admitted the source. Returns a status and the deciding passage. Never
searches for sources; never judges whether the claim is true."

| Argument | Type | Required | Schema says |
|---|---|---|---|
| `claim` | object | yes | No inner fields listed |
| `passage` | object | no | "text and locator. The passage is quoted, not paraphrased." |
| `source` | object | no | No inner fields listed |

Call:

```
check_claim({
  "claim":   <one claim object as extract_claims returned it>,
  "passage": { "text": "<words quoted exactly from the source>",
               "locator": "<page, section, table or paragraph>" },
  "source":  <the source object qualify_source returned>
})
```

`[CHECK]` Inner field names. The schema names "text and locator" for the passage in its
description but not as typed keys; `claim` and `source` have no listed fields. Passing
the objects returned by `extract_claims` and `qualify_source` unchanged is this skill's
assumption, to be confirmed.

Returns: a status and the deciding passage (schema). Statuses, from the connector
instructions: `supported`, `partial`, `unsupported`, `contradicted`, `unverifiable`,
`out_of_scope`. `[CHECK]` Whether a rationale or the source tier is also returned.

Pitfalls:

- Never put a summary you wrote in `passage.text` (C3).
- Admit the source first (`source-assessment`). The schema says to call after
  `qualify_source` has admitted it.
- `[CHECK]` From the earlier vital-verify method: an empty passage or an inadmissible
  source returns `unverifiable`; a bronze-tier passage returns at most `partial`.
- It does not return the confidence figure. Counts go to `confidence-scoring`.

## verify_text

Schema description: "Extract claims and check them against the sources or ingested
documents the caller names. One counted call. At most 60 findings; longer texts must be
split. It does not clear a record."

| Argument | Type | Required | Schema says |
|---|---|---|---|
| `text` | string | yes | No limit stated `[CHECK]` |
| `sources` | array of objects | no | No inner fields listed |
| `document_ids` | array of strings | no | Ids of documents stored with `ingest_document` |

Call:

```
verify_text({
  "text": "<the text exactly as submitted>",
  "sources": [ <source objects for the sources the person named> ],
  "document_ids": [ "<ingested document id>" ]
})
```

Returns: findings, at most 60 (schema). `[CHECK]` Finding fields; whether each finding
carries the deciding passage as `check_claim` does.

Pitfalls:

- One counted call against the person's key. Use it for a first pass, then
  `check_claim` for rewrites and disputed sentences.
- More than 60 findings: split the text and call again.
- It checks only against what is named. It does not fetch or search for anything else.
- It does not clear a record. Clearance is `citation-and-record` with a named person.

## Not used by this skill

`qualify_source`, `ingest_document`, `check_currency` (`source-assessment`);
`build_citation`, `build_record`, `build_evidence_table` (`citation-and-record`). The
confidence figure and the VERIFY card are `confidence-scoring`.

## Duplicate tool names in this session

`[CHECK]` The Digital Health Library connector in this session also lists tools named
`verify_extract_claims`, `verify_check_claim` and `verify_verify_text`. Whether they are
the same service and contract as the VERIFY connector is not established. This skill
names the VERIFY connector's tools only.

## Script (manual split)

`scripts/split_claims.py` splits a text into sentences with start and end offsets that
slice back to the exact input, and flags priority signals (numbers, comparisons, quotes,
efficacy or safety words, causal words, named titles, recommendation words). It is a
manual aid, labeled "manual split, not tool-checked". It never gives a support result.

```
python scripts/split_claims.py text.txt
python scripts/split_claims.py text.txt --json
```

Pitfalls: abbreviations such as "e.g." and "vs." are not sentence ends; decimals are not
split; flags are signals for ranking, not a judgment.
