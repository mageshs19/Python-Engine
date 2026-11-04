"""Compare the AI-standardized V6 COBOL examples with current Python output and manual references.

This is a review aid, not a compiler or semantic-equivalence proof. It deliberately does
not rewrite COBOL or automatically remove helper variables.
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any

PROGRAMS = {
    "VMDZ1526": "txt",
    "VMDZ1567": "cbl",
    "VMDZ4302": "txt",
    "VMDZ4310": "txt",
    "VMDZ4420": "cbl",
    "VMDZ7200": "cbl",
}
TIMESTAMP_RE = re.compile(r"_(\d{2}-\d{2}-\d{4})_(\d{6})\.cbl$", re.I)


def latest_python_output(output_dir: Path, program: str) -> Path | None:
    candidates = list(output_dir.glob(f"{program}_*.cbl"))
    if not candidates:
        return None

    timestamped: list[tuple[datetime, Path]] = []
    for path in candidates:
        match = TIMESTAMP_RE.search(path.name)
        if not match:
            continue
        try:
            timestamped.append((datetime.strptime("_".join(match.groups()), "%d-%m-%Y_%H%M%S"), path))
        except ValueError:
            continue
    # Ignore unversioned review artifacts whenever timestamped generated outputs exist.
    if timestamped:
        return max(timestamped, key=lambda item: (item[0], item[1].name))[1]
    return max(candidates, key=lambda path: (path.stat().st_mtime, path.name))


def read_lines(path: Path | None) -> list[str]:
    if path is None or not path.is_file():
        return []
    return path.read_text(encoding="utf-8", errors="replace").splitlines()


def body_text(lines: list[str]) -> str:
    # Drop sequence areas, keep indicator and source area; sequence numbers are not semantics.
    return "\n".join((line[6:72] if len(line) >= 7 else line).upper() for line in lines)


def count(pattern: str, text: str) -> int:
    return len(re.findall(pattern, text, re.I | re.M))


def inspect_program(path: Path | None, project_root: Path | None = None) -> dict[str, Any]:
    lines = read_lines(path)
    text = "\n".join(lines)
    semantic = body_text(lines)
    exec_sql_lines = [i for i, line in enumerate(lines) if re.search(r"\bEXEC\s+SQL\b", line, re.I)]
    sql_location_before = 0
    for index in exec_sql_lines:
        prior = "\n".join(lines[max(0, index - 6):index])
        if re.search(r"\bMOVE\b[^\n]*\bTO\s+SQL-LOCATION\b", prior, re.I):
            sql_location_before += 1
    cursor_names = sorted(set(re.findall(r"\bDECLARE\s+([A-Z0-9-]+)\s+CURSOR\b", semantic, re.I)))
    cursor_audit: dict[str, Any] = {}
    for name in cursor_names:
        cursor_audit[name] = {
            "open": count(rf"\bOPEN\s+{re.escape(name)}\b", semantic),
            "fetch": count(rf"\bFETCH\s+{re.escape(name)}\b", semantic),
            "close": count(rf"\bCLOSE\s+{re.escape(name)}\b", semantic),
        }
    labels = re.findall(r"(?im)^\s*[0-9]{4,6}-[A-Z0-9][A-Z0-9-]*\s*\.", semantic)
    duplicates = sorted({label.strip().rstrip(".") for label in labels if labels.count(label) > 1})
    try:
        display_path = str(path.relative_to(project_root)) if path and project_root else (path.name if path else None)
    except ValueError:
        display_path = str(path) if path else None
    return {
        "file": display_path,
        "exists": bool(lines),
        "line_count": len(lines),
        "fixed_80_columns": bool(lines) and all(len(line) == 80 for line in lines),
        "max_line_length": max((len(line) for line in lines), default=0),
        "duplicate_numbered_labels": duplicates,
        "lifecycle": {
            "main": count(r"^\s*0000-MAIN-PROCEDURE\s*\.", semantic),
            "initialize": count(r"^\s*1000-INITIALIZE-PROGRAM\s*\.", semantic),
            "process": count(r"^\s*2000-PROCESS-PROGRAM\s*\.", semantic),
            "finalize": count(r"^\s*3000-FINALIZE-PROGRAM\s*\.", semantic),
            "treat_program": count(r"^\s*2000-TREAT-PROGRAM\s*\.", semantic),
        },
        "conventions": {
            "cs_program_references": count(r"\bCS-PROGRAM\b", semantic),
            "timestamp_paragraph": count(r"^\s*\d{3,6}-GET-TIMESTAMP\s*\.", semantic),
            "sqlerrws_include": count(r"\bINCLUDE\s+SQLERRWS\b", semantic),
            "sqlerror_include_or_call": count(r"\bINCLUDE\s+SQLERROR\b", semantic) + count(r"\bPERFORM\s+SQLERROR\b", semantic),
            "sql_location_moves": count(r"\bMOVE\b[^\n]*\bTO\s+SQL-LOCATION\b", semantic),
            "exec_sql_blocks": len(exec_sql_lines),
            "exec_sql_with_recent_sql_location": sql_location_before,
        },
        "cursors": cursor_audit,
        "text": text,
    }


def normalized_diff_counts(left: list[str], right: list[str]) -> dict[str, int]:
    # Compare body text after removing sequence columns and blank lines. This is a change-size
    # indicator only; it does not establish business equivalence.
    a = [re.sub(r"\s+", " ", line[6:72]).strip().upper() for line in left]
    b = [re.sub(r"\s+", " ", line[6:72]).strip().upper() for line in right]
    a = [x for x in a if x]
    b = [x for x in b if x]
    import difflib
    matcher = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    added = removed = 0
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag in ("insert", "replace"):
            added += j2 - j1
        if tag in ("delete", "replace"):
            removed += i2 - i1
    return {"reference_nonblank_lines": len(a), "candidate_nonblank_lines": len(b), "changed_lines_added": added, "changed_lines_removed": removed}


def build_report(project_root: Path, reference_dir: Path | None = None) -> dict[str, Any]:
    reference_dir = reference_dir or project_root / "references" / "AI_STANDARDIZED_V6"
    output_dir = project_root / "mainframe" / "workspace" / "Output"
    manual_dir = project_root / "mainframe" / "workspace" / "Manual Output"
    result: dict[str, Any] = {
        "report_type": "AI standardized COBOL reference comparison",
        "reference_version": "IDMS_DB2_STANDARDIZED_V6",
        "principle": "Advisory benchmark only; do not assume V6 is 100% correct and do not remove helpers without representation, initialization, and path proof.",
        "programs": {},
        "policy_conflicts": [
            {
                "topic": "Cursor numbering",
                "V6_reference": "C1 2100/2200/2300; C2 2400/2500/2600; C3 2700/2800/2900",
                "previous_defect": "C1 2100/2200/2300; C2 3100/3200/3300; later cursors continued by +1000",
                "current_project_contract": "C1 2100/2200/2300; C2 2400/2500/2600; C3 2700/2800/2900; each subsequent cursor advances by +300",
                "decision": "The centralized numbering rule and release validator enforce the agreed cursor identity convention and validate generated PERFORM targets and SQL-LOCATION values.",
            },
            {
                "topic": "Lifecycle paragraph restructuring",
                "V6_reference": "Uses 0000/1000/2000/3000 lifecycle wrappers and removes detail-forwarding paragraphs.",
                "current_project_contract": "ProcedureDivisionOrganizer is conservative because moving paragraph bodies can alter fall-through, PERFORM THRU ranges, and business execution order.",
                "decision": "Use as a target style, but require CFG/reference/order parity before automatic restructuring.",
            },
            {
                "topic": "Helper-variable removal",
                "V6_reference": "Removes several staging helpers and uses direct fields/normalized dates.",
                "current_project_contract": "Helper removal can alter data representation, truncation, numeric/alphanumeric comparison, or initialization behavior.",
                "decision": "Treat each removal as a candidate; require PIC/REDEFINES compatibility, all-path assignment, and read/write-use checks before adoption.",
            },
        ],
        "helper_removal_audit_from_v6": {},
        "limitations": [
            "Static source comparison only; no COBOL compiler or DB2 precompiler/runtime equivalence proof.",
            "SQL-LOCATION proximity and SQLCODE branch counts are heuristics, not control-flow proofs.",
            "Line-difference counts are diagnostic and must not be interpreted as semantic error counts.",
        ],
    }
    helper_audit_path = reference_dir / "HELPER_VARIABLE_AUDIT.json"
    if helper_audit_path.exists():
        result["helper_removal_audit_from_v6"] = json.loads(helper_audit_path.read_text(encoding="utf-8"))
    for program, manual_ext in PROGRAMS.items():
        py_path = latest_python_output(output_dir, program)
        ref_path = reference_dir / f"{program}.cbl"
        manual_path = manual_dir / f"{program}.{manual_ext}"
        py_info = inspect_program(py_path, project_root)
        ref_info = inspect_program(ref_path, project_root)
        manual_info = inspect_program(manual_path, project_root)
        result["programs"][program] = {
            "python_output": {k: v for k, v in py_info.items() if k != "text"},
            "ai_standardized_v6": {k: v for k, v in ref_info.items() if k != "text"},
            "manual_output": {k: v for k, v in manual_info.items() if k != "text"},
            "python_vs_v6_diff": normalized_diff_counts(read_lines(ref_path), read_lines(py_path)),
            "v6_vs_manual_diff": normalized_diff_counts(read_lines(manual_path), read_lines(ref_path)),
        }
    return result


def markdown_report(report: dict[str, Any]) -> str:
    out = [
        "# AI Standardized V6 Reference Comparison",
        "",
        "> V6 is an advisory example, not an unquestioned source of truth. Static checks do not prove COBOL/DB2 semantic equivalence.",
        "",
        "## Decisions before applying V6 patterns",
        "",
    ]
    for item in report["policy_conflicts"]:
        out += [f"### {item['topic']}", f"- **V6 reference:** {item['V6_reference']}", f"- **Current project:** {item['current_project_contract']}", f"- **Decision:** {item['decision']}", ""]
    out += ["## Per-program comparison", "", "| Program | Latest Python output | Python lines | V6 lines | Manual lines | Python↔V6 changed lines (+/−) | V6↔manual changed lines (+/−) |", "|---|---|---:|---:|---:|---:|---:|"]
    for program, item in report["programs"].items():
        py = item["python_output"]
        ref = item["ai_standardized_v6"]
        man = item["manual_output"]
        d1 = item["python_vs_v6_diff"]
        d2 = item["v6_vs_manual_diff"]
        out.append(f"| {program} | `{Path(py['file']).name if py['file'] else 'MISSING'}` | {py['line_count']} | {ref['line_count']} | {man['line_count']} | +{d1['changed_lines_added']}/−{d1['changed_lines_removed']} | +{d2['changed_lines_added']}/−{d2['changed_lines_removed']} |")
    out += ["", "## Infrastructure checks", ""]
    for program, item in report["programs"].items():
        out.append(f"### {program}")
        for source_key, title in [("python_output", "Latest Python output"), ("ai_standardized_v6", "V6 reference"), ("manual_output", "Manual output")]:
            info = item[source_key]
            conv = info["conventions"]
            life = info["lifecycle"]
            out.append(
                f"- **{title}:** fixed-80={info['fixed_80_columns']}; CS-PROGRAM refs={conv['cs_program_references']}; "
                f"timestamp paragraph={conv['timestamp_paragraph']}; SQLERRWS={conv['sqlerrws_include']}; "
                f"SQLERROR include/calls={conv['sqlerror_include_or_call']}; SQL-LOCATION moves={conv['sql_location_moves']}; "
                f"EXEC SQL blocks={conv['exec_sql_blocks']}; nearby SQL-LOCATION={conv['exec_sql_with_recent_sql_location']}; "
                f"lifecycle labels={life['main']}/{life['initialize']}/{life['process']}/{life['finalize']}; "
                f"cursors={list(info['cursors'])}"
            )
        out.append("")
    out += ["## Helper-variable rule", "", "Never delete a helper merely because the V6 file deleted it. Before adopting each removal, verify:", "1. Source and target `PIC`/`USAGE` and `REDEFINES` layouts preserve the same bytes and numeric/alphanumeric interpretation.", "2. The helper is assigned on every path before it is read; initialization and default values are equivalent.", "3. Direct moves do not change truncation, sign, leading-zero, date-format, or comparison behavior.", "4. No hidden copybook, `REPLACING`, or paragraph reference depends on the helper.", "5. Manual output and test cases agree; otherwise retain the helper and flag the case for review.", "", "## Limitations", ""]
    out.extend(f"- {item}" for item in report["limitations"])
    out.append("")
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--reference-dir", type=Path, default=None)
    parser.add_argument("--json-out", type=Path, default=None)
    parser.add_argument("--markdown-out", type=Path, default=None)
    args = parser.parse_args()
    report = build_report(args.project_root, args.reference_dir)
    json_out = args.json_out or args.project_root / "AI_STANDARDIZED_V6_COMPARISON.json"
    md_out = args.markdown_out or args.project_root / "AI_STANDARDIZED_V6_COMPARISON.md"
    json_out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    md_out.write_text(markdown_report(report), encoding="utf-8")
    print(f"Wrote {json_out}")
    print(f"Wrote {md_out}")
    for program, item in report["programs"].items():
        py = item["python_output"]
        conv = py["conventions"]
        print(f"{program}: output={Path(py['file']).name if py['file'] else 'MISSING'} lines={py['line_count']} SQLERRWS={conv['sqlerrws_include']} SQLERROR={conv['sqlerror_include_or_call']} SQLLOC={conv['sql_location_moves']} cursors={len(py['cursors'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
