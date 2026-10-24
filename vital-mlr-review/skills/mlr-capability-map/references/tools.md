# Tool calls

## Companion slot

MLR tools are on MCP server `vital-mlr-review` with a `vmlr_` key.
VERIFY tools are on MCP server `vital-verify` with a `vvfy_` key (same connector as vital-trusted / vital-verify).
Without the needed key, run the method by hand and label the turn **not tool-checked** (MLR-H4).
Never invent a tool field. Always use `ServerName:tool_name`.

## Primary tools

This skill has no primary counted tool. It routes or explains. Do not invent tool payloads.


## Also named

- `vital-mlr-review:mlr_intake`
- `vital-mlr-review:mlr_get_ruleset`
- `vital-verify:qualify_source`
- `vital-verify:check_claim`

These stay on their own connector or skill. This skill does not reimplement them.
`vital-mlr-review:my_usage` is a meter — not a skill tool.
