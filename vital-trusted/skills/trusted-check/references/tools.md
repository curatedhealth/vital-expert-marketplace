# Tools

See plugin [`connectors.md`](../../../connectors.md).

Most Build skills are method-only. Optional Verify may be used when a Prove handoff needs passage checks. Offline scripts under this skill's `scripts/` remain valid; shared Prove helpers live in plugin `tools/`.

## Prior notes

# Tools and companion slot

## Companion slot per task

| Task | What a companion would do | Tool | Without it |
|---|---|---|---|
| Run the active letters | Each letter skill's own slot (label source, MLR preparation, safety routing, AI policy) would let that letter check instead of ask | No companion yet for any Build letter | Each letter runs as method; checks that need a missing companion read "not checked" in the summary |
| Write the summary | None needed | `scripts/scan_verdicts.py` where code can run | Read the summary once for the words in `references/patterns.md` P1 |
| Hand off to Prove | Check factual claims against supplied sources, qualify sources and their currency, compute confidence, build citations and a record | VERIFY, through the four Prove skills | Name what VERIFY would check; never simulate (TR-H4) |

## "Could not be checked" lines for empty slots

Use these plain lines when the letter is active and the check needed the companion:

| Empty slot | Plain line |
|---|---|
| Label source (Rule-compliant, Safe) | "Whether statements about the product match the approved label: no label tool yet, and no label was supplied." (Drop the first half if the person supplied the label and the letter compared it.) |
| MLR preparation | Not listed; promotional review is named as the next process instead |
| Safety routing | Not listed; the safety reporting procedure is named in open items |
| AI policy | "Whether the tool and data use fit your AI policy: checked only against what you told me about it." |
| VERIFY not connected | See `tasks/prove-handoff.md`, steps when VERIFY is not connected |

## VERIFY chain (through the Prove skills)

`trusted-check` calls no VERIFY tool. It hands the packet to the Prove skills, which own
the arguments and the interpretation. The order and contracts below are read from the
VERIFY tool schemas on 20 October 2026, so authors of the Prove skills and the owner's
cross-check start from the same list. Anything beyond the schema is `[CHECK]`.

| Order | Prove skill | VERIFY tool | Takes (from the schema) | Gives back (from the schema) | Notes |
|---|---|---|---|---|---|
| 1 | `source-assessment` | `qualify_source` | One of `doi`, `pmid`, `pmcid`, `url`, `catalogue_id`, `document_id`; `question` for relevance | A source with a tier and a `source_score` | Never searches for a source the caller did not name. An http(s) URL is fetched for title, publisher and date |
| 1a | `source-assessment` | `ingest_document` | `pdf_base64` (≤10 MB) or `text` or `url`; `uploader_attestation`; optional `metadata`, `retention_days` (default 90) | Stored passages and locators for this tenant | Requires `verify:write` and the person's attestation that they may process the document. Ask first |
| 1b | `source-assessment` | `check_currency` | One of `doi`, `pmid`, `pmcid`, `catalogue_id`, `url`, or a `record` | Whether retracted, corrected, superseded or withdrawn | A URL alone returns "not checked" |
| 2 | `claim-assessment` | `extract_claims` | `text` (≤20,000 characters), `granularity` = sentence | Claims with offsets | Never decides support. Longer drafts are split |
| 2 | `claim-assessment` | `check_claim` | `claim` (object, required), `passage` (quoted text and locator), `source` | A status and the deciding passage | Call after the source is admitted. Shape of the `claim`, `passage` and `source` objects: `[CHECK]` |
| 2 alt | `claim-assessment` | `verify_text` | `text` (required), `sources` or `document_ids` | Findings, at most 60 | One counted call; does not clear a record. When to prefer it over `check_claim`: `claim-assessment` decides |
| 3 | `confidence-scoring` | none | Results of steps 1 and 2 | Confidence line and the VERIFY card | Formula in `references/rules.md` V3 `[CHECK]` |
| 4 | `citation-and-record` | `build_citation` | `source`, `record` (for a paper), `passage`; `style` chicago or harvard, or omit for the key preference | One formatted citation line | Free. Does not check the claim. Paste
