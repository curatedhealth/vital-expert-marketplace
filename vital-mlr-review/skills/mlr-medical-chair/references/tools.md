# Tool calls

## Companion slot

MLR tools are on MCP server `vital-mlr-review` with a `vmlr_` key.
VERIFY tools are on MCP server `vital-verify` with a `vvfy_` key (same connector as vital-trusted / vital-verify).
Without the needed key, run the method by hand and label the turn **not tool-checked** (MLR-H4).
Never invent a tool field. Always use `ServerName:tool_name`.

## Primary tools

## `vital-mlr-review:mlr_get_ruleset`

Short name: `mlr_get_ruleset`. Always call the fully qualified name when multiple MCP servers are connected.

Arguments: see MCP descriptors / `mcps/mlr_review/tools.py`.

Pitfall: Treating a successful tool call as MLR approval.

Schema source: `mcps/mlr_review/tools.py`, method pack `0.3.1`.

## `vital-mlr-review:mlr_align_claims`

Short name: `mlr_align_claims`. Always call the fully qualified name when multiple MCP servers are connected.

Arguments: see MCP descriptors / `mcps/mlr_review/tools.py`.

Pitfall: Treating a successful tool call as MLR approval.

Schema source: `mcps/mlr_review/tools.py`, method pack `0.3.1`.


## Also named

- `vital-mlr-review:mlr_handoff_verify`

These stay on their own connector or skill. This skill does not reimplement them.
`vital-mlr-review:my_usage` is a meter — not a skill tool.
