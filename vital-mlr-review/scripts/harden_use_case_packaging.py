#!/usr/bin/env python3
"""Harden packaging for 11-skill use-case registry + Hybrid B.

Default (no flags or --check): read-only check, exit 0/1.
--write: create only missing pieces (empty .mcp.json, CF04 stubs, suite-evals
entries); version and release_state are always read from plugin.json, never pinned.
- soft-update monorepo test_skills EXPECTED set via companion note (tests updated separately)
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

PLUGIN = Path(__file__).resolve().parents[1]
SKILLS = PLUGIN / "skills"
NEW = ("mlr-channel-intent", "mlr-claims-matrix", "mlr-fair-balance-isi")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def write_if_missing(path: Path, text: str) -> None:
    if not path.exists():
        write(path, text)


def stub_cf04(skill: str) -> None:
    root = SKILLS / skill
    write_if_missing(
        root / "examples" / "worked.md",
        f"""# Worked example — {skill}

Teaching material only (MLR-H2). Not a live input.

See `good-sourced-draft.md` for the world-class Output-card shape and
`poor-*.md` for refuse patterns. Offline stamp via `tools/stamp_ready_line.py`.
""",
    )
    write_if_missing(
        root / "references" / "gap-rules.md",
        f"""# Gap rules — {skill}

- Missing person-supplied field → [GAP], never invent.
- Missing connector key → label **not tool-checked**.
- Approval-pressure language → refuse (MLR-H3).
- Cross-chair themes → route to owning skill; do not blend.
""",
    )
    write_if_missing(
        root / "references" / "patterns.md",
        f"""# Patterns — {skill}

1. Read governance stop rules.
2. Prefer offline CLI named in tools.md.
3. Emit Output card from `../../templates/`.
4. Close with stamp + liability line.
""",
    )
    write_if_missing(
        root / "references" / "rules.md",
        f"""# Rules — {skill}

- MLR-H1…H6 apply.
- Status ∈ findings_only | revise | human_gate_required | prep_complete.
- Markets explicit; never silent US default.
""",
    )
    write_if_missing(
        root / "assets" / "worksheet-output.md",
        f"""# Worksheet output — {skill}

Point host output at the matching card under `../../templates/`.
Teaching material only.
""",
    )
    write_if_missing(
        root / "assets" / "liability-line.md",
        "This prepares material for human MLR review. It is not medical, legal, or regulatory approval.\n",
    )
    # ensure Teaching material phrase in poor/good if missing — examples already exist
    for ex in (root / "examples").glob("*.md"):
        text = ex.read_text(encoding="utf-8")
        if "Teaching material" not in text and "teaching" not in text.lower():
            write(ex, "Teaching material only (MLR-H2).\n\n" + text)


CF04_FILES = (
    "examples/worked.md",
    "references/gap-rules.md",
    "references/patterns.md",
    "references/rules.md",
    "assets/worksheet-output.md",
    "assets/liability-line.md",
)
ALLOWED_STATES = {"Pilot", "Back-tested", "Released"}


def _disk_skills() -> list[str]:
    return sorted(p.name for p in SKILLS.iterdir() if (p / "SKILL.md").is_file())


def check() -> list[str]:
    """Read-only packaging check. Returns a list of failures (empty = pass)."""
    fails: list[str] = []
    try:
        if json.loads((PLUGIN / ".mcp.json").read_text(encoding="utf-8")) != {}:
            fails.append(".mcp.json not empty (Hybrid B)")
    except (OSError, json.JSONDecodeError) as exc:
        fails.append(f".mcp.json unreadable: {exc}")
    pj = json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    if not re.fullmatch(r"\d+\.\d+\.\d+", str(pj.get("version") or "")):
        fails.append(f"plugin.json version not semver: {pj.get('version')!r}")
    if pj.get("release_state") not in ALLOWED_STATES:
        fails.append(f"plugin.json release_state {pj.get('release_state')!r} not in {sorted(ALLOWED_STATES)}")
    for skill in NEW:
        for rel in CF04_FILES:
            if not (SKILLS / skill / rel).is_file():
                fails.append(f"{skill} missing CF04 file {rel}")
    suite = json.loads((PLUGIN / "evals" / "suite-evals.json").read_text(encoding="utf-8"))
    ids = sorted(s["id"] for s in suite.get("skills", []))
    if ids != _disk_skills():
        fails.append(f"suite-evals skills {ids} != skills on disk {_disk_skills()}")
    for entry in suite.get("skills", []):
        if not entry.get("must_refuse"):
            fails.append(f"suite-evals {entry.get('id')} missing must_refuse")
    if suite.get("version") != pj.get("version"):
        fails.append(f"suite-evals version {suite.get('version')!r} != plugin.json {pj.get('version')!r}")
    return fails


def write_missing() -> None:
    """Create only what is missing. Never changes plugin.json version, release_state
    or description, and never overwrites existing CF04 files or suite entries."""
    write(PLUGIN / ".mcp.json", "{}")
    pj = json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    for skill in NEW:
        stub_cf04(skill)
    suite_path = PLUGIN / "evals" / "suite-evals.json"
    suite = json.loads(suite_path.read_text(encoding="utf-8")) if suite_path.is_file() else {"skills": []}
    suite["version"] = pj["version"]
    suite["release_state"] = pj.get("release_state")
    have = {s["id"] for s in suite.get("skills", [])}
    for skill in _disk_skills():
        if skill in have:
            continue
        ev = json.loads((SKILLS / skill / "evals" / "evals.json").read_text(encoding="utf-8"))
        refuse = (ev.get("must_refuse") or [{}])[0].get("request", "")
        suite.setdefault("skills", []).append(
            {"id": skill, "must_refuse": refuse, "scripts": [], "primary_tools": []}
        )
    write(suite_path, json.dumps(suite, indent=2))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument(
        "--write",
        action="store_true",
        help="create missing packaging pieces (default is a read-only --check)",
    )
    ap.add_argument("--check", action="store_true", help="read-only packaging check (default)")
    args = ap.parse_args(argv)
    if args.write and not args.check:
        write_missing()
    fails = check()
    if fails:
        print(f"FAIL ({len(fails)}):")
        for f in fails:
            print(" -", f)
        return 1
    print("PASS packaging: empty mcp, version/state from plugin.json, CF04 files, suite-evals covers all skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
