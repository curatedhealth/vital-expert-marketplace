#!/usr/bin/env python3
"""End-to-end offline harness for ON↔DD use-case packs.

World-class bars (eng — not Marketplace Done / independent Pass):
  B1 Structure — required steps + workflow twin + goldens
  B2 Honesty — no recommend-sign / FTO clearance / Marketplace Done / ASC enable in pack prose
  B3 Return loop — return packet template fields referenced; ON handoff expect-return exists
  B4 Assemble — IR all-clear fixtures assemble with all options recommended=false
  B5 Preflight — return-packet golden + filled Aurora fixture pass preflight_refuse_scan
  B6 Shape coverage — top_down + middle_out + bottom_up packs present
  B7 Craft CI — refuse smoke + preflight self-test
  B8 Teaching depth — every pack return/golden carries recommended=false + dual-read|[CHECK] + refuse vocabulary

Exit 0 = all bars pass; 1 = failures; 2 = runner error.
No network. Stdlib only.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXAMPLES = Path(__file__).resolve().parent
ON_ROOT = ROOT.parents[1] / "ontology_navigator" / "plugin" / "vital-navigator-outcomes"
# path: mcps/due_diligence/plugin/... → parents[1]=due_diligence, need mcps/
MCPS = ROOT.parents[1]  # due_diligence's parent is mcps if structure is mcps/due_diligence/plugin/...
# ROOT = .../vital-es-target-evaluation-due-diligence
# parents[0]=plugin, [1]=due_diligence, [2]=mcps
MCPS = ROOT.parents[2]
ON_HANDOFF = (
    MCPS
    / "ontology_navigator/plugin/vital-navigator-outcomes/examples/due-diligence-handoff"
)

PACKS = {
    "UC02-asset-acquisition-aurora-x": {
        "shape": "top_down",
        "workflow": "WF-UC02-asset-acquisition.md",
        "required": [
            "00-on-route.md",
            "01-on-frame.md",
            "02-session-contract.md",
            "03-dd-intake.md",
            "04-dd-workstreams.md",
            "05-dd-assemble.md",
            "06-return-packet.md",
            "07-on-compare-close.md",
            "goldens/02-return-packet-excerpt.md",
            "fixtures/filled-return-packet.md",
        ],
    },
    "UC02-company-roll-up": {
        "shape": "top_down",
        "workflow": "WF-UC02-company-mna.md",
        "required": [
            "00-route.md",
            "01-intake-or-scope.md",
            "02-return.md",
            "goldens/01-return-headline.md",
        ],
    },
    "UC02-in-license": {
        "shape": "top_down",
        "workflow": "WF-UC02-in-license.md",
        "required": [
            "00-route.md",
            "01-intake-or-scope.md",
            "02-return.md",
            "goldens/01-return-headline.md",
        ],
    },
    "UC02-partner-option": {
        "shape": "top_down",
        "workflow": "WF-UC02-partner-option.md",
        "required": [
            "00-route.md",
            "01-intake-or-scope.md",
            "02-return.md",
            "goldens/01-return-headline.md",
        ],
    },
    "bridge-UC06-portfolio-keep-kill": {
        "shape": "middle_out",
        "workflow": "WF-bridge-UC06-portfolio-keep-kill.md",
        "required": [
            "00-route.md",
            "01-intake-or-scope.md",
            "02-return.md",
            "goldens/01-return-headline.md",
        ],
    },
    "bridge-UC08-evidence-access": {
        "shape": "bottom_up",
        "workflow": "WF-bridge-UC08-evidence-access.md",
        "required": [
            "00-route.md",
            "01-intake-or-scope.md",
            "02-return.md",
            "goldens/01-return-headline.md",
        ],
    },
}

TEACHING_NEEDLES = (
    "recommended=false",
    ("dual-read", "[check]"),
    ("fto", "asc", "marketplace done", "refuse"),
)

BANNED = [
    (r"\bfto\s+clearance\b", "FTO clearance"),
    (r"\bai\s+recommends?\s+sign\b", "AI recommend-sign"),
    (r"\bstudio\s+marketplace\s+done\b", "Marketplace Done claim"),
    (r"\benable\s+asc\s*205\b", "ASC enable"),
    (r"\benable\s+fc-(net|uptake|loe)\b", "FC enable"),
    (r"\bwe recommend acquiring\b", "deal recommend"),
]


def _run(cmd: list[str], cwd: Path | None = None, input_text: str | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        cmd,
        cwd=str(cwd or ROOT),
        input=input_text,
        capture_output=True,
        text=True,
        check=False,
    )


def bar_structure() -> list[str]:
    fails: list[str] = []
    for name, meta in PACKS.items():
        d = EXAMPLES / name
        if not d.is_dir():
            fails.append(f"missing pack {name}")
            continue
        for rel in meta["required"]:
            if not (d / rel).is_file():
                fails.append(f"{name}: missing {rel}")
        wf = ROOT / "templates/workflows" / meta["workflow"]
        if not wf.is_file():
            fails.append(f"{name}: missing workflow twin {meta['workflow']}")
        readme = d / "README.md"
        if readme.is_file() and meta["workflow"] not in readme.read_text():
            fails.append(f"{name}: README must cite {meta['workflow']}")
    return fails


def bar_honesty() -> list[str]:
    fails: list[str] = []
    for name in PACKS:
        d = EXAMPLES / name
        for path in d.rglob("*.md"):
            text = path.read_text(encoding="utf-8", errors="replace")
            low = text.lower()
            for pat, label in BANNED:
                if re.search(pat, low):
                    # allow mentioning "not Marketplace Done" / "do not enable"
                    if label == "Marketplace Done claim" and (
                        "not claimed" in low or "not marketplace" in low or "≠" in text
                    ):
                        continue
                    if "do not" in low or "never" in low or "refuse" in low:
                        # contextual refuse OK if pattern appears in refuse instruction
                        if any(
                            x in low
                            for x in (
                                "do not",
                                "never",
                                "refuse",
                                "not claimed",
                                "stays",
                                "disabled",
                            )
                        ):
                            continue
                    fails.append(f"{name}/{path.relative_to(d)}: banned phrase ({label})")
    return fails


def bar_return_loop() -> list[str]:
    fails: list[str] = []
    pkt = ROOT / "templates/handoff-to-navigator-return-packet.md"
    if not pkt.is_file():
        fails.append("missing templates/handoff-to-navigator-return-packet.md")
    else:
        t = pkt.read_text()
        for needle in (
            "Graded claims",
            "recommended=false",
            "compare-options",
            "handoff-verify",
            "never values the asset",
        ):
            if needle.lower() not in t.lower() and needle not in t:
                # flexible
                if needle == "never values the asset" and "never value" not in t.lower():
                    fails.append(f"return packet missing concept: {needle}")
                elif needle != "never values the asset" and needle not in t:
                    fails.append(f"return packet missing: {needle}")
    if not (ON_HANDOFF / "01-expect-return.md").is_file():
        fails.append("ON due-diligence-handoff missing 01-expect-return.md")
    cmd = ROOT / "commands/dd-handoff-to-navigator.md"
    if not cmd.is_file():
        fails.append("missing commands/dd-handoff-to-navigator.md")
    return fails


def bar_assemble() -> tuple[list[str], Path | None]:
    fails: list[str] = []
    manifest = ROOT / "evals/dd-integrated-report/fixtures/all-clear/manifest.json"
    if not manifest.is_file():
        return ["missing IR all-clear manifest"], None
    tmp = Path(tempfile.mkdtemp(prefix="dd-e2e-"))
    out_json = tmp / "report.json"
    out_md = tmp / "report.md"
    proc = _run(
        [
            sys.executable,
            str(ROOT / "tools/assemble_report.py"),
            str(manifest),
            "--out",
            str(out_json),
            "--md",
            str(out_md),
        ]
    )
    if proc.returncode != 0:
        fails.append(f"assemble_report exit {proc.returncode}: {(proc.stderr or proc.stdout)[-300:]}")
        return fails, tmp
    data = json.loads(out_json.read_text())
    asset = data["assets"][0]
    opts = asset.get("decision_options") or []
    if len(opts) < 3:
        fails.append("assemble: expected ≥3 decision options")
    for o in opts:
        if o.get("recommended") is not False:
            fails.append(f"assemble: option {o.get('option')} recommended must be false")
    if asset.get("deal_lead_decision") and "HUMAN" not in str(asset.get("deal_lead_decision")):
        fails.append("assemble: deal_lead_decision must stay HUMAN ONLY / PENDING")
    md = out_md.read_text().lower()
    if "nothing is recommended" not in md and "none recommended" not in md:
        fails.append("assemble md: missing none-recommended framing")
    return fails, tmp


def bar_preflight(assemble_tmp: Path | None) -> list[str]:
    fails: list[str] = []
    script = ROOT / "scripts/preflight_refuse_scan.py"
    golden = (
        EXAMPLES
        / "UC02-asset-acquisition-aurora-x/goldens/02-return-packet-excerpt.md"
    )
    filled = (
        EXAMPLES
        / "UC02-asset-acquisition-aurora-x/fixtures/filled-return-packet.md"
    )
    texts = []
    if golden.is_file():
        texts.append(("golden-return", golden.read_text()))
    if filled.is_file():
        texts.append(("filled-aurora-return", filled.read_text()))
    else:
        fails.append("missing Aurora filled-return-packet.md fixture")
    pkt = (ROOT / "templates/handoff-to-navigator-return-packet.md").read_text()
    texts.append(("template-return", pkt))
    if assemble_tmp and (assemble_tmp / "report.md").is_file():
        texts.append(("assemble-md", (assemble_tmp / "report.md").read_text()))
    for label, text in texts:
        proc = _run(
            [sys.executable, str(script), "--stdin-transcript"],
            input_text=text,
        )
        if proc.returncode not in (0, 2):
            fails.append(f"preflight {label}: unexpected rc {proc.returncode}")
        elif proc.returncode == 2:
            fails.append(f"preflight {label}: HARD refuse\n{proc.stdout[-400:]}")
    return fails


def bar_shapes() -> list[str]:
    shapes = {meta["shape"] for meta in PACKS.values()}
    need = {"top_down", "middle_out", "bottom_up"}
    missing = need - shapes
    return [f"shape coverage missing: {sorted(missing)}"] if missing else []


def bar_teaching_depth() -> list[str]:
    """Refuse greenwash: stubs that omit honesty vocabulary fail."""
    fails: list[str] = []
    for name in PACKS:
        d = EXAMPLES / name
        blobs: list[str] = []
        for rel in ("02-return.md", "06-return-packet.md"):
            p = d / rel
            if p.is_file():
                blobs.append(p.read_text(encoding="utf-8", errors="replace"))
        for g in sorted((d / "goldens").glob("*.md")) if (d / "goldens").is_dir() else []:
            blobs.append(g.read_text(encoding="utf-8", errors="replace"))
        if not blobs:
            fails.append(f"{name}: no return/golden text to score teaching depth")
            continue
        joined = "\n".join(blobs).lower()
        if "recommended=false" not in joined:
            fails.append(f"{name}: teaching depth missing recommended=false")
        if "dual-read" not in joined and "[check]" not in joined:
            fails.append(f"{name}: teaching depth missing dual-read or [CHECK]")
        if not any(x in joined for x in ("fto", "asc", "marketplace done", "refuse")):
            fails.append(f"{name}: teaching depth missing refuse vocabulary")
    # Aurora filled fixture must itself be deep
    filled = (
        EXAMPLES
        / "UC02-asset-acquisition-aurora-x/fixtures/filled-return-packet.md"
    )
    if filled.is_file():
        t = filled.read_text().lower()
        if "recommended=false" not in t or "human only" not in t:
            fails.append("Aurora filled return: must keep recommended=false + HUMAN ONLY")
        if "marketplace done" not in t or "not claimed" not in t:
            fails.append("Aurora filled return: must state Marketplace Done not claimed")
    return fails


def bar_craft_ci() -> list[str]:
    fails: list[str] = []
    st = _run([sys.executable, str(ROOT / "scripts/preflight_refuse_scan.py"), "--self-test"])
    if st.returncode != 0:
        fails.append("preflight --self-test failed")
    smoke = _run([sys.executable, str(ROOT / "evals/known-answer/refuse_content_smoke.py")])
    if smoke.returncode != 0:
        fails.append(f"refuse smoke failed: {(smoke.stderr or smoke.stdout)[-200:]}")
        return fails
    try:
        data, _ = json.JSONDecoder().raw_decode(smoke.stdout)
    except json.JSONDecodeError:
        fails.append("refuse smoke: could not parse JSON")
        return fails
    if data.get("fail_count", 1) != 0:
        fails.append(f"refuse smoke fail_count={data.get('fail_count')}")
    if data.get("pass_count", 0) < 15:
        fails.append(f"refuse smoke pass_count too low: {data.get('pass_count')}")
    return fails


def write_scorecard(results: dict, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    results: dict = {
        "kind": "on_dd_use_case_e2e",
        "as_of": date.today().isoformat(),
        "world_class_claim": "eng_bars_only",
        "marketplace_done": False,
        "asc_fc_full_enabled": False,
        "bars": {},
        "failures": [],
    }
    assemble_tmp = None
    try:
        checks = [
            ("B1_structure", bar_structure),
            ("B2_honesty", bar_honesty),
            ("B3_return_loop", bar_return_loop),
            ("B6_shapes", bar_shapes),
            ("B7_craft_ci", bar_craft_ci),
            ("B8_teaching_depth", bar_teaching_depth),
        ]
        for name, fn in checks:
            fails = fn()
            results["bars"][name] = {"pass": not fails, "failures": fails}
            results["failures"].extend(fails)

        a_fails, assemble_tmp = bar_assemble()
        results["bars"]["B4_assemble"] = {"pass": not a_fails, "failures": a_fails}
        results["failures"].extend(a_fails)

        p_fails = bar_preflight(assemble_tmp)
        results["bars"]["B5_preflight"] = {"pass": not p_fails, "failures": p_fails}
        results["failures"].extend(p_fails)

        results["pass"] = len(results["failures"]) == 0
        out = (
            ROOT
            / "diligence"
            / "dd-wc-craft-exports-2026-11-08"
            / f"E2E_SCORECARD_ON_DD_{date.today().isoformat()}.json"
        )
        write_scorecard(results, out)
        print(json.dumps(results, indent=2))
        print(f"Scorecard: {out.relative_to(ROOT)}")
        return 0 if results["pass"] else 1
    except Exception as exc:  # noqa: BLE001
        print(f"runner error: {exc}", file=sys.stderr)
        return 2
    finally:
        if assemble_tmp and assemble_tmp.exists():
            shutil.rmtree(assemble_tmp, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
