---
description: Run deterministic refuse / policy preflight on a diligence draft. Use before sharing a pack or claiming Pass.
---

Run the eng refuse preflight:

```bash
python3 "${CLAUDE_PLUGIN_ROOT:-.}/scripts/preflight_refuse_scan.py" path/to/draft.md
```

Also run content refuse smoke when touching rules:

```bash
python3 evals/known-answer/refuse_content_smoke.py
```

Hard fails: FTO clearance language, AI recommend-sign, ASC/FC enable claims, Marketplace Done, self-Pass, independence cleared.
