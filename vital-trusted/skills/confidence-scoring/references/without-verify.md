# Without VERIFY (offline Prove path)

When no `vvfy_` key is present:

1. Run the skill tasks in order using offline `tools/` under the plugin root.
2. Stamp every output with `tools/stamp_check_line.py --mode offline --skill <name>`.
3. Never invent a Verify status. Use local statuses from `passage_support.py` / method reading only.
4. Do not call live `qualify_source`, `check_claim`, `verify_text`, or other network tools.
5. Tell the person results are **not tool-checked** and still need human review.

When a key is present, prefer live tools for fetch/admission/currency; keep offline tools as fallback.
