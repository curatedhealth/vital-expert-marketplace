# Currency check reference

`check_currency` does not change a support status by itself. Source grading reads the result.

| Input | What the tool may say | Effect on the tier |
|---|---|---|
| DOI, PMID, or PMCID | retracted, corrected, superseded, withdrawn, or clear | Retracted and the claim is not about the retraction: `inadmissible`. |
| Catalogue document | `doc_status` | Superseded or withdrawn: not gold. |
| URL and no literature id | notices `["not checked"]` | Tier is unchanged. Source-score currency is null. |

`checked_at` is the time of this call, in ISO 8601. Copy it onto the finding. Do not copy a page's "current as of" date into `checked_at`. That date belongs in provenance.


Restated 19 October 2026 from the Verify method.

Last reviewed: 20 October 2026.
