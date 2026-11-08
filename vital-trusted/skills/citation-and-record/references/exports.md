# Record method reference

`build_record` refuses when `cleared_by.name` is missing. Prefer `generate_report` to draft exports; `build_record` files clearance. Templates live next to this skill:

| Export | Template | When it exists |
|---|---|---|
| Verify brief | `manifest/templates/verify-brief.md` | Default `generate_report` shape (counts, open items, sources). |
| Gap list | `manifest/templates/gap-list.md` | Open items only. |
| Clearance memo | `manifest/templates/clearance-memo.md` | Always drafted. First line says "Draft" until a human has decided. |
| Source register | `manifest/templates/source-register.md` | One row per source that was graded, including inadmissible rows, with the reason. |
| Evidence table | `manifest/templates/evidence-table.md` | Via `generate_report` or when the user asks for the table alone. |
| Finding card | `manifest/templates/finding-card.md` | One card per finding. |
| Overview / Assessment / Evidence review / Decision memo | `manifest/templates/{overview,assessment,evidence-review,decision-memo}.md` | Brief answer spine (section labels only). Does not commission Brief. Scan, Landscape, Outlook, Plan, Comparison, Diagnosis stay on Brief. |

A record with zero clearances is a draft even if every claim is `supported`. Support is not clearance. `generate_report` never clears.

Citation lines inside the memo are `formatted` from `build_citation`. The key's `citation_style` is `chicago` unless the key or the call says `harvard`. The memo does not add the caption "as returned by Verify."


Restated 22 October 2026 from the Verify method.
