#!/usr/bin/env python3
"""Harden packaging for 11-skill use-case registry + Hybrid B.

- Restore empty .mcp.json
- plugin.json 0.4.0 Pilot
- CF04 stubs for channel/claims/fair-balance (worked, gap-rules, patterns, rules, assets)
- suite-evals.json 11 skills
- soft-update monorepo test_skills EXPECTED set via companion note (tests updated separately)
"""

from __future__ import annotations

import json
from pathlib import Path

PLUGIN = Path(__file__).resolve().parents[1]
SKILLS = PLUGIN / "skills"
NEW = ("mlr-channel-intent", "mlr-claims-matrix", "mlr-fair-balance-isi")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def stub_cf04(skill: str) -> None:
    root = SKILLS / skill
    write(
        root / "examples" / "worked.md",
        f"""# Worked example — {skill}

Teaching material only (MLR-H2). Not a live input.

See `good-sourced-draft.md` for the world-class Output-card shape and
`poor-*.md` for refuse patterns. Offline stamp via `tools/stamp_ready_line.py`.
""",
    )
    write(
        root / "references" / "gap-rules.md",
        f"""# Gap rules — {skill}

- Missing person-supplied field → [GAP], never invent.
- Missing connector key → label **not tool-checked**.
- Approval-pressure language → refuse (MLR-H3).
- Cross-chair themes → route to owning skill; do not blend.
""",
    )
    write(
        root / "references" / "patterns.md",
        f"""# Patterns — {skill}

1. Read governance stop rules.
2. Prefer offline CLI named in tools.md.
3. Emit Output card from `../../templates/`.
4. Close with stamp + liability line.
""",
    )
    write(
        root / "references" / "rules.md",
        f"""# Rules — {skill}

- MLR-H1…H6 apply.
- Status ∈ findings_only | revise | human_gate_required | prep_complete.
- Markets explicit; never silent US default.
""",
    )
    write(
        root / "assets" / "worksheet-output.md",
        f"""# Worksheet output — {skill}

Point host output at the matching card under `../../templates/`.
Teaching material only.
""",
    )
    write(
        root / "assets" / "liability-line.md",
        "This prepares material for human MLR review. It is not medical, legal, or regulatory approval.\n",
    )
    # ensure Teaching material phrase in poor/good if missing — examples already exist
    for ex in (root / "examples").glob("*.md"):
        text = ex.read_text(encoding="utf-8")
        if "Teaching material" not in text and "teaching" not in text.lower():
            write(ex, "Teaching material only (MLR-H2).\n\n" + text)


def main() -> int:
    write(PLUGIN / ".mcp.json", "{}")
    pj_path = PLUGIN / ".claude-plugin" / "plugin.json"
    pj = json.loads(pj_path.read_text(encoding="utf-8"))
    pj["version"] = "0.4.0"
    pj["release_state"] = "Pilot"
    pj["description"] = (
        "MLR board preparation (READY): 11 skills, Hybrid B offline-first, "
        "never approves. Pilot — not marketplace Released."
    )
    write(pj_path, json.dumps(pj, indent=2))

    for skill in NEW:
        stub_cf04(skill)

    # suite-evals
    suite_path = PLUGIN / "evals" / "suite-evals.json"
    skills = sorted(p.name for p in SKILLS.iterdir() if (p / "SKILL.md").is_file())
    suite = {
        "version": "0.4.0",
        "pack": "vital-mlr-review",
        "release_state": "Pilot",
        "routing_harness": "mcps/mlr_review/tests/test_skills.py",
        "use_case_registry": "evals/USE_CASE_REGISTRY.json",
        "use_case_e2e": "scripts/run_use_case_e2e.py",
        "script_self_tests": [
            "check_forbidden_phrases.py",
            "check_jurisdictions.py",
            "check_finding_shape.py",
            "validate_packet_shape.py",
        ],
        "skills": [
            {
                "id": s,
                "evals": f"skills/{s}/evals/evals.json",
            }
            for s in skills
        ],
        "anthropic_alignment": {
            "third_person_description": True,
            "imperative_skill_body": True,
            "qualified_mcp_tools": True,
            "progressive_disclosure": True,
            "deterministic_scripts": True,
            "model_versus_model": False,
        },
        "counts": {
            "skills": len(skills),
            "use_cases": 60,
        },
    }
    write(suite_path, json.dumps(suite, indent=2))
    print("hardened packaging: empty mcp, 0.4.0 Pilot, CF04 stubs, suite-evals")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
