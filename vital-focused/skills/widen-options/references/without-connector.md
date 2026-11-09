# Local mode (default) - widen-options

No connector key is needed. This is how the skill normally runs.

1. Run the plugin's scripts by full path from the person's working folder: `python3 <plugin root>/tools/<script>.py ...`. The plugin root is two folders above this skill's folder. Never `cd` into the plugin folder.
2. Sessions save to `./focused-sessions/` in the working folder. If a save fails, or scripts cannot run in this host, do the same steps by hand from the person's words only. Do not mention the failure unless the person asked to save.
3. Adding up weights and ratings: run `score_tradeoff_offline.py`. If no script can run, add up openly by hand, show the working in one line per option, and invite the person to check it.
4. Never invent a Decision connector, Navigator or Verify result. Navigator sealed scores and Verify claim checks are only available with their keys; without them, say in plain words that this check is not connected and offer the local path.
5. Do not label coaching replies (no "not tool-checked" or "FOCUSED-local" lines). The stamp goes on a saved record or brief only.

With an optional key (`vdec_`, `vont_`, `vvfy_`) and the person's go-ahead, the connector tools named in SKILL.md replace the local scripts.
