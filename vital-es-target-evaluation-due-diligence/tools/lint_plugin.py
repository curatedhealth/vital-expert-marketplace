#!/usr/bin/env python3
"""Lint this plugin against VITAL skill authoring standard v0.1 (sections 2, 2b, 3, 4).

Usage: lint_plugin.py [plugin folder] [--leakage-file FILE]
  --leakage-file  a text file (kept OUTSIDE the plugin) with one forbidden name per line; matches are errors.
Exit 0 = pass, 1 = findings, 2 = setup error. Needs PyYAML.
"""
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML is required", file=sys.stderr)
    sys.exit(2)

FM = re.compile(r"\A---\n(.*?)\n---\n", re.S)
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
FULL_META = ["level", "register_code", "verb", "capability", "mission", "agent", "atoms", "requires", "release_state"]
FULL_FILES = ["SKILL.md", "intake.md", "governance.md", "references/method-standards.md", "references/failure-modes.md", "evals/evals.json"]
FULL_DIRS = ["tasks", "scripts", "templates", "examples", "evals/fixtures"]
STUBS = []
FULL = ["review-clinical-data-quality", "estimate-development-risk-and-timeline",
        "assess-ip-portfolio-and-freedom-to-operate", "evaluate-regulatory-pathway-and-legal-risk",
        "analyze-financial-statements-and-tax", "assess-scientific-validity-and-moa",
        "evaluate-market-opportunity-and-competitive-position", "forecast-revenue-and-price-ranges", "determine-commercial-viability"]
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
# Full-tier chain F -> A -> B: anatomy v1.1 section 7 checks (upgrade lane, 7 November 2026)
CHAIN = ["assess-scientific-validity-and-moa", "review-clinical-data-quality", "estimate-development-risk-and-timeline",
         "assess-ip-portfolio-and-freedom-to-operate", "evaluate-regulatory-pathway-and-legal-risk", "analyze-financial-statements-and-tax",
         "evaluate-market-opportunity-and-competitive-position", "forecast-revenue-and-price-ranges", "determine-commercial-viability"]
CARD_FIELDS = ["Input", "Atom", "Tool", "Template", "Output", "Check", "Human"]
VP = re.compile(r"VP-[A-Z]-\d{3}")
REG_KEYS = ["id", "source_id", "section", "page", "text", "url", "access_date", "cue"]
NORM = (("VERIFIED (re-opened)", "VERIFIED-REOPENED"), ("PARTIAL (summary only)", "SUMMARY-ONLY"))


def norm(s):
    for a, b in NORM:
        s = s.replace(a, b)
    return s


STATUSES = ("VERIFIED-REOPENED", "SUMMARY-ONLY", "[CHECK]", "ENGINEERING RULE")


def table_rows(path):
    """Yield the cells of every data row of every markdown table in a file."""
    for line in path.read_text().splitlines():
        if line.startswith("|") and not line.startswith("|---"):
            yield [c.strip() for c in line.strip().strip("|").split("|")]


def all_chain_ids(root):
    out = set()
    for name in CHAIN:
        f = root / "skills" / name / "references/verbatim-passages.json"
        if f.is_file():
            try:
                out |= {p["id"] for p in json.loads(f.read_text())["passages"]}
            except Exception:
                pass
    return out


def chain_checks(sk, fm, e):
    n = sk.name
    union = all_chain_ids(sk.parent.parent)
    meta = fm.get("metadata") or {}
    for k in ("tier", "feeds", "tools"):
        if not meta.get(k):
            e(f"{n}: metadata.{k} missing (anatomy 1.1, 3.1)")
    # seven task-card fields
    for card in sorted((sk / "tasks").glob("0*.md")):
        txt = card.read_text()
        for f in CARD_FIELDS:
            if not re.search(rf"^{f}:\s*\S", txt, re.M):
                e(f"{n}/tasks/{card.name}: field '{f}' missing or empty")
    # verbatim register
    reg = sk / "references/verbatim-passages.json"
    ids = set()
    if not reg.is_file():
        e(f"{n}: references/verbatim-passages.json missing")
    else:
        try:
            passages = json.loads(reg.read_text())["passages"]
        except Exception as ex:
            passages = []
            e(f"{n}: verbatim register does not parse: {ex}")
        for p in passages:
            for k in REG_KEYS:
                # a web page has no page number: page may be null, but the key and a section must exist
                if k == "page":
                    if "page" not in p:
                        e(f"{n}: passage {p.get('id')} lacks the page key")
                elif not p.get(k):
                    e(f"{n}: passage {p.get('id')} lacks {k}")
            if p.get("id") in ids:
                e(f"{n}: duplicate passage id {p.get('id')}")
            ids.add(p.get("id"))
    # every VP pointer anywhere in the skill resolves in this skill's or another chain skill's register
    for f in sk.rglob("*"):
        if f.is_file() and f.suffix in {".md", ".json", ".py"} and f.name != "verbatim-passages.json" and "__pycache__" not in f.parts:
            for pid in sorted(set(VP.findall(f.read_text(errors="ignore")))):
                if pid not in union:
                    e(f"{n}/{f.relative_to(sk)}: pointer {pid} not in any chain register")
    # governance: every gate names a role
    gov = sk / "governance.md"
    in_gates = False
    for line in gov.read_text().splitlines():
        if line.startswith("## Human gates"):
            in_gates = True
        elif line.startswith("## "):
            in_gates = False
        elif in_gates and line.startswith("|") and not line.startswith("|---") and not line.startswith("| Gate"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 3 or not cells[-1]:
                e(f"{n}/governance.md: gate without a deciding role: {line[:60]}")
    # grounding register: statuses, no UNGROUNDED, pointers resolve
    gr = sk / "references/grounding-register.md"
    if not gr.is_file():
        e(f"{n}: references/grounding-register.md missing")
    else:
        rows = [r for r in table_rows(gr) if r and r[0] != "Item type"]
        if not rows:
            e(f"{n}: grounding register is empty")
        types = {r[0] for r in rows}
        for need in ("step", "task card", "template", "constant or list", "detection question", "example", "eval fixture"):
            if need not in types:
                e(f"{n}: grounding register has no '{need}' row")
        for r in rows:
            if len(r) < 4:
                e(f"{n}: grounding row malformed: {r[:2]}")
                continue
            if r[2] == "UNGROUNDED" or r[2] not in STATUSES:
                e(f"{n}: grounding row '{r[1]}' has status '{r[2]}'")
            if r[2] == "VERIFIED-REOPENED" and not (set(VP.findall(r[3])) and set(VP.findall(r[3])) <= union):
                e(f"{n}: grounding row '{r[1]}' is VERIFIED-REOPENED without a resolving passage id")
            if r[2] == "ENGINEERING RULE" and len(r[3]) < 15:
                e(f"{n}: grounding row '{r[1]}' is ENGINEERING RULE without a reason")
    # reference rows: VERIFIED-REOPENED rows carry a resolving passage id
    for refname in ("method-standards.md", "failure-modes.md"):
        for r in table_rows(sk / "references" / refname):
            r = [norm(c) for c in r]
            line = " | ".join(r)
            if "VERIFIED-REOPENED" in r[-1] or ("VERIFIED-REOPENED" in line and "SUMMARY-ONLY" not in line and "[CHECK]" not in line):
                found = set(VP.findall(line))
                if not found or not found <= union:
                    e(f"{n}/references/{refname}: VERIFIED-REOPENED row without a resolving passage id: {line[:60]}")



def frontmatter(path):
    m = FM.match(path.read_text())
    if not m:
        return None
    return yaml.safe_load(m.group(1))



def integrated_report_checks(root, e):
    """Plugin-level integrated diligence report: command, template, schema, tool, tests, evals, wiring."""
    import hashlib
    cmd = root / "commands" / "dd-integrated-report.md"
    if not cmd.is_file():
        e("integrated report: commands/dd-integrated-report.md missing")
    else:
        t = cmd.read_text()
        for need in ("command:", "args:", "REQUIRES", "deal lead", "human only"):
            if need not in t:
                e(f"integrated report: command lacks '{need}'")
    tpl = root / "templates" / "integrated-diligence-report.md"
    sch = root / "templates" / "integrated-diligence-report.schema.json"
    if not tpl.is_file() or not sch.is_file():
        e("integrated report: template or schema missing")
    else:
        heads = [l for l in tpl.read_text().splitlines() if l.startswith("## ")]
        if len([h for h in heads if h[3:4].isdigit()]) != 8:
            e("integrated report: template must carry the eight numbered sections")
        try:
            sj = json.loads(sch.read_text())
            if sj.get("properties", {}).get("recommended_option", {}).get("type") != "null":
                e("integrated report: schema must fix recommended_option to null")
        except Exception as ex:
            e(f"integrated report: schema does not parse ({ex})")
    tool, test = root / "tools" / "assemble_report.py", root / "tools" / "test_assemble_report.py"
    if not tool.is_file() or not test.is_file():
        e("integrated report: tools/assemble_report.py or its tests missing")
    else:
        src = tool.read_text()
        for need in ("Deterministic", "R-STATUS", "ENGINEERING RULE", "team-set defaults", "R-CONF-5"):
            if need not in src:
                e(f"integrated report: tool docstring lacks '{need}'")
        for bad in ("import socket", "urllib", "import requests", "http.client"):
            if bad in src:
                e(f"integrated report: tool uses the network ({bad})")
    ev = root / "evals" / "dd-integrated-report"
    try:
        evs = json.loads((ev / "evals.json").read_text())["evals"]
        if len(evs) < 5:
            e("integrated report: fewer than five evals")
        for x in evs:
            for k in ("id", "prompt", "files", "expect", "must_not"):
                if k not in x:
                    e(f"integrated report eval {x.get('id')}: lacks {k}")
            for f in x.get("files", []):
                if not (ev / f).is_file():
                    e(f"integrated report eval {x.get('id')}: fixture missing {f}")
    except Exception as ex:
        e(f"integrated report: evals.json ({ex})")
    cs = ev / "CHECKSUMS.sha256"
    if not cs.is_file() or not (ev / "FREEZE.md").is_file():
        e("integrated report: CHECKSUMS.sha256 or FREEZE.md missing")
    else:
        for line in cs.read_text().splitlines():
            if not line.strip():
                continue
            h, _, name = line.partition("  ")
            fp = ev / name.strip()
            if not fp.is_file() or hashlib.sha256(fp.read_bytes()).hexdigest() != h:
                e(f"integrated report: checksum mismatch for {name.strip()}")
    for rel, word in (("README.md", "dd-integrated-report"), ("agents/bd-due-diligence-lead.md", "dd-integrated-report"),
                      ("skills/target-evaluation-due-diligence-capability-map/SKILL.md", "dd-integrated-report")):
        f = root / rel
        if f.is_file() and word not in f.read_text():
            e(f"integrated report: {rel} does not mention {word}")


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    leak = []
    if "--leakage-file" in argv:
        lf = argv[argv.index("--leakage-file") + 1]
        args = [a for a in args if a != lf]
        leak = [l.strip().lower() for l in Path(lf).read_text().splitlines() if l.strip()]
    root = Path(args[0]) if args else Path(__file__).resolve().parent.parent
    errs = []
    e = errs.append
    # plugin level
    try:
        pj = json.loads((root / ".claude-plugin/plugin.json").read_text())
        if not pj.get("version"):
            e("plugin.json: version missing")
    except Exception as ex:
        pj = {}
        e(f"plugin.json: {ex}")
    for f in ["README.md", "connectors.md"]:
        if not (root / f).is_file():
            e(f"missing {f}")
    if not list((root / "agents").glob("*.md")):
        e("agents/: no agent file")
    if not list((root / "commands").glob("*.md")):
        e("commands/: none")
    if not (root / "skills/target-evaluation-due-diligence-capability-map/SKILL.md").is_file():
        e("capability map missing")
    readme = (root / "README.md").read_text() if (root / "README.md").is_file() else ""
    for s in ("Status", "Depends on", "Not covered", "Tier", "Back-test", "[CHECK] means"):
        if s not in readme:
            e(f"README lacks '{s}'")
    # skills
    for sk in sorted((root / "skills").iterdir()):
        if not sk.is_dir():
            continue
        md = sk / "SKILL.md"
        if not md.is_file():
            e(f"{sk.name}: SKILL.md missing")
            continue
        fm = frontmatter(md)
        if not isinstance(fm, dict):
            e(f"{sk.name}: frontmatter does not parse")
            continue
        if fm.get("name") != sk.name or not NAME_RE.match(fm.get("name", "")) or len(fm.get("name", "")) > 64:
            e(f"{sk.name}: name must equal folder, lowercase-hyphen, <=64")
        d = " ".join(str(fm.get("description", "")).split())
        if not d or len(d) > 1024:
            e(f"{sk.name}: description missing or over 1024 characters ({len(d)})")
        meta = fm.get("metadata") or {}
        if str(meta.get("version")) != str(pj.get("version")):
            e(f"{sk.name}: metadata.version != plugin.json version")
        text = md.read_text()
        if len(text.splitlines()) > 500:
            e(f"{sk.name}: SKILL.md over 500 lines")
        if sk.name in FULL:
            for k in FULL_META:
                if k not in meta:
                    e(f"{sk.name}: metadata.{k} missing")
            for f in FULL_FILES:
                if not (sk / f).is_file():
                    e(f"{sk.name}: {f} missing")
            for dd in FULL_DIRS:
                if not (sk / dd).is_dir() or not any((sk / dd).iterdir()):
                    e(f"{sk.name}: {dd}/ missing or empty")
            if not list((sk / "scripts").glob("test_*.py")):
                e(f"{sk.name}: scripts have no tests")
            ex = [p.name for p in (sk / "examples").glob("*")]
            if not any(n.startswith("good") for n in ex) or not any(n.startswith("poor") for n in ex):
                e(f"{sk.name}: examples need one good* and one poor*")
            if not list((sk / "tasks").glob("0*.md")):
                e(f"{sk.name}: tasks/ has no task cards")
            for need in ("agent alone", "human only"):
                if need not in text:
                    e(f"{sk.name}: steps table lacks autonomy value '{need}'")
            if "Method anchoring" not in text or "Quality bar" not in text or "Connectors" not in text:
                e(f"{sk.name}: SKILL.md lacks Method anchoring / Connectors / Quality bar")
            for refname in ("method-standards.md", "failure-modes.md"):
                for line in norm((sk / "references" / refname).read_text()).splitlines():
                    if line.startswith("| ") and not line.startswith("| Id") and not line.startswith("|---"):
                        if "summary-level" in line.lower() and "VERIFIED-REOPENED" in line and "SUMMARY-ONLY" not in line:
                            e(f"{sk.name}/references/{refname}: summary-level reading marked VERIFIED-REOPENED: {line[:60]}")
                        if not any(t in line for t in ("VERIFIED-REOPENED", "SUMMARY-ONLY", "[CHECK]")):
                            e(f"{sk.name}/references/{refname}: row not tagged VERIFIED-REOPENED, SUMMARY-ONLY or [CHECK]: {line[:60]}")
            if sk.name in CHAIN:
                chain_checks(sk, fm, e)
        elif sk.name in STUBS:
            if "DRAFT STUB" not in text or "Not for use" not in text.replace("not for use", "Not for use"):
                e(f"{sk.name}: DRAFT banner missing")
            extra = [p.name for p in sk.iterdir() if p.name != "SKILL.md"]
            if extra:
                e(f"{sk.name}: stub holds extra files {extra}")
        # links
        for link in LINK.findall(text):
            if link.startswith(("http", "#", "mailto")):
                continue
            if not (sk / link).exists():
                e(f"{sk.name}: broken link {link}")
    for n in FULL + STUBS:
        if not (root / "skills" / n).is_dir():
            e(f"expected skill folder missing: {n}")
    integrated_report_checks(root, e)
    # hygiene + leakage
    for p in root.rglob("*"):
        if "__pycache__" in p.parts or p.suffix == ".pyc":
            e(f"stray cache: {p.relative_to(root)}")
        if leak and p.is_file() and p.suffix in {".md", ".json", ".py", ".txt", ".yaml", ".yml"}:
            t = p.read_text(errors="ignore").lower()
            for name in leak:
                if name in t:
                    e(f"leakage: '{name}' in {p.relative_to(root)}")
    for x in errs:
        print("FAIL", x)
    print(f"{len(errs)} finding(s)")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
