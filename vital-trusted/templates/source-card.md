# Source card (render this shape)

```text
┌─ Source ───────────────────────────────────────────
│ Title:        <as supplied or returned>
│ Publisher:    <authority / journal / agency>
│ Identifier:   <DOI | PMID | URL | catalogue | document_id | none>
│ Date:         <YYYY or YYYY-MM-DD | unknown>
│ Tier:         gold | silver | bronze | unknown
│ Score:        <0–100 or "not scored">  axes: authority · recency · relevance · provenance · currency
│ Currency:     clear | retracted | corrected | superseded | withdrawn | not checked
│ Fit for job:  yes | with limits | no — <one line why>
│ Label:        tool-checked | not tool-checked
└────────────────────────────────────────────────────
```

## Axes (weights used offline: 25 / 25 / 30 / 10 / 10)

Drop null axes and rescale (same practice as live `qualify_source` scoring). Currency stays **not checked** until `check_currency` or a human notice.

## Citations

- Crossref / Retraction Watch for retraction signals — [CHECK] confirm against live tool when key present.
- CEBM / GRADE inform *clinical* strength language; they do not replace promotional substantiation (IFPMA 4.3 / ABPI 6.2).
