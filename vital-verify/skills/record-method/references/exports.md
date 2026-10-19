# Record method reference

`build_record` refuses when `cleared_by.name` is missing. The templates live next to this skill:

| Export | Template | When it exists |
|---|---|---|
| Clearance memo | `manifest/templates/clearance-memo.md` | Always drafted. First line says "Draft" until a human has decided. |
| Source register | `manifest/templates/source-register.md` | One row per source that was graded, including inadmissible rows, with the reason. |
| Evidence table | `manifest/templates/evidence-table.md` | Only when the user asks. Columns are claim, status, source, tier, locator, and currency. |
| Finding card | `manifest/templates/finding-card.md` | One card per finding. It does not replace the short Verify card in the answer. |

A record with zero clearances is a draft even if every claim is `supported`. Support is not clearance.

Citation lines inside the memo are `formatted` from `build_citation`. The key's `citation_style` is `chicago` unless the key or the call says `harvard`. The memo does not add the caption "as returned by Verify."


Restated 19 October 2026 from the Verify method.
