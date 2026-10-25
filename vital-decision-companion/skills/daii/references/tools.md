# Tool calls

## Companion slot

`decision_daii_plan` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_daii_plan

Arguments: session_id, roles: {decide, advise, inform, implement}.

- **Send:** `decide` is one display-name string. `advise` / `inform` / `implement` are arrays of display-name strings (the person's words). Do not invent `{name, status}` objects on input.
- **Read back:** each of advise / inform / implement may return either a **string** or an object `{name, status}` (live 0.3.1+). When `status` is `unverified_person`, print `"<name> (unverified, role not person)"` and list it under Gaps. Treat a bare string as a verified person name.

Returns: roles and gaps. Empty decide is a gap. Gap `role_only_name` may name an index (for example advise[0]).

Pitfall: Filling Decide with "the model" or "Decision Companion" fails the human-author rule.

A call the skill must refuse returns `gaps` whose text starts with `refused:`. The rejected field is not stored.

Schema source: `mcps/decision_companion/tools.py`, content pack `2026-10-26.1`. See also `docs/decision-companion/CONTRACT_CHANGES.md` (role entry dual shape).

## Also named

- `decision_run_stage`

These tools stay on their own connector. This skill does not reimplement them.

## Connector version

| Condition | What to do |
|---|---|
| Gap `role_only_name` on Decide | Ask who the person is. Do not store a role title as decide. |
| Gap `role_only_name` on Advise / Inform / Implement | Ask for a named person. If the person insists on the role title, keep it; read back `{name, status: "unverified_person"}` as unverified. |
| Role entry is a string | Print the name as given. |
| Role entry is `{name, status: "unverified_person"}` | Print `"<name> (unverified, role not person)"`; Gaps. |

