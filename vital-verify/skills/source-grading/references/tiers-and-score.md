# Source grading reference

Code: `mcps/verify/tiers.py` (`tier_for`) and `mcps/verify/source_score.py` (`score_source`). The skill states the rules. The code decides the tier.

## Six provenance fields

| Field | Counts as present when |
|---|---|
| authority | `authority` is non-empty. `publisher` can stand in for the bronze rules only. |
| title | non-empty |
| code | a stable identifier (DOI, document number, docket) |
| date | `YYYY-MM` or `YYYY-MM-DD`. A bare year does not count. |
| status | non-empty. `retracted`, `superseded`, and `withdrawn` close the source. |
| official_url | non-empty |

## Tier order

Apply the first match.

1. `inadmissible` when the source type is `model`, the text is model output, the paper is retracted and the claim is not about the retraction, or a doc-to-doc citation points at a primary that cannot be reached.
2. `inadmissible` when no provenance field is present and there is no publisher.
3. `gold` for a catalogue document that is servable, not closed, stable, and missing nothing.
4. `gold` for literature or a URL with all six fields, a stable code, and an open status.
5. `silver` for a peer-reviewed secondary source (a systematic review or a guideline) with all six fields and an open status.
6. `silver` when exactly one field is missing, that field is the code or the date is year-only, and the source is not closed. Reason text: `primary source missing one field: <name>`.
7. `bronze` for an ingested document, or when a publisher or authority and a date are present.
8. `bronze` for a URL that has a title, a publisher or authority, and an official URL, but is missing the date or the code. Reason text: `page title and publisher; the date or the code was not in the metadata`.
9. Otherwise `inadmissible` with reason `no provenance`.

`supported` requires gold or silver. A bronze passage yields at most `partial`, and the rationale is `source tier bronze`.

## Source score

The score is the page, not the claim. Weights: authority 25, recency 25, relevance 30, provenance 10, currency 10. Axes that are null are left out and the remaining weights are rescaled to 100.

| Axis | 25 or 30 | Middle | Low | Dropped |
|---|---|---|---|---|
| authority | 25 for an official publisher, a `.gov` host, or a `.europa.eu` host | 15 when any publisher is named | 0 | never |
| recency | 25 at 18 months or newer | 15 from 18 to 36 months | 5 when older; 0 when there is no date | never |
| relevance | 30 when at least half of the question's content words appear in the title, publisher, or passage | 15 at 20 percent or more | 5 below that | null when no question was passed |
| provenance | gold 10 | silver 7 | bronze 3; anything else 0 | never |
| currency | 10 when the currency check is clear | — | 0 when retracted, superseded, or withdrawn | null when the value is `not_checked` |

Relevance uses words of four or more characters. A short title can score 5 even when the page is the right one. Say that when you print the axes. Do not "correct" the number.

Last reviewed: 20 October 2026. Status of tier thresholds: Confirmed against `mcps/verify/tiers.py` and `source_score.py` as of 19 October 2026; re-confirm after code changes `[CHECK]`.
