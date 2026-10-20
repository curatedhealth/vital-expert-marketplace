# Tool calls

## Companion slot

`qualify_source` needs a VERIFY key. Without it, method-only and not tool-checked (VR-H4).

# Tool calls

Call these only when a Verify key is present. The method still runs without one.

## qualify_source

Arguments: the identifier (DOI, PMID, PMCID, URL, catalogue id, or ingested id) and the person's question when they asked one.

Returns: provenance fields, tier, reasons, and source_score. Currency on that score is not_checked until a currency call.

Pitfall: a fast failure means the fetch failed. The reason names the failure. Do not replace it with a title you remember.

## check_currency

Not this task, unless the person also asks whether the source is retracted. That task is currency-check.

Schema source: the Verify connector tool list as deployed on mcp.vital.expert, read with the product instructions on 19 October 2026.
