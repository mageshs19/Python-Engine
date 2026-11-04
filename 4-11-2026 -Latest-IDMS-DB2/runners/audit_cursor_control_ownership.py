"""Audit generated COBOL for paragraph entry displays and cursor ownership.

Run against a folder containing one final .cbl per program, e.g.:
    python runners/audit_cursor_control_ownership.py \
        --folder "mainframe/workspace/Validated Output/ROOT_CAUSE_V101"

The audit is read-only. It does not rewrite or approve mainframe compilation.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from converter.composers.cursor_close_guarantee_composer import (
    CursorCloseGuaranteeComposer,
)
from converter.composers.paragraph_entry_display_composer import (
    _is_paragraph,
    _logical,
)


def audit_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    procedure = next(
        (i for i, line in enumerate(lines)
         if re.match(r"^PROCEDURE\s+DIVISION\b", _logical(line), re.I)),
        None,
    )
    if procedure is None:
        return {"file": path.name, "error": "PROCEDURE DIVISION not found"}

    headers = [i for i in range(procedure + 1, len(lines)) if _is_paragraph(lines[i])]
    missing_displays: list[str] = []
    for index in headers:
        name = _logical(lines[index])
        next_index = index + 1
        while next_index < len(lines) and (
            not _logical(lines[next_index]) or _logical(lines[next_index]).startswith(("*", "/"))
        ):
            next_index += 1
        expected = f"DISPLAY '{name}'.".upper()
        if next_index >= len(lines) or _logical(lines[next_index]).upper() != expected:
            missing_displays.append(name)

    cursors = re.findall(r"EXEC\s+SQL\s+DECLARE\s+(\w+)\s+CURSOR", text, re.I)
    cursor_lifecycle: dict[str, dict] = {}
    for cursor in cursors:
        operations: dict[str, dict] = {}
        for operation in ("OPEN", "FETCH", "CLOSE"):
            match = re.search(
                rf"(?m)^\s*\d{{6}}\s+([0-9A-Z-]*{operation}-{cursor})\s*\.",
                text,
                re.I,
            )
            paragraph = match.group(1).upper() if match else None
            references = (
                len(re.findall(rf"\bPERFORM\s+{re.escape(paragraph)}\b", text, re.I))
                if paragraph else 0
            )
            operations[operation] = {
                "paragraph": paragraph,
                "paragraph_found": bool(paragraph),
                "perform_references": references,
            }
        cursor_lifecycle[cursor] = operations

    composer = CursorCloseGuaranteeComposer()
    second_pass = composer.compose(text)
    return {
        "file": path.name,
        "line_count": len(lines),
        "procedure_paragraph_count": len(headers),
        "missing_active_exact_name_displays": missing_displays,
        "declared_cursors": cursors,
        "cursor_lifecycle": cursor_lifecycle,
        "cursor_lifecycle_second_pass_idempotent": second_pass == text,
        "second_pass_diagnostics": composer.messages,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--folder", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    files = sorted(args.folder.glob("*.cbl"))
    if not files:
        parser.error(f"No .cbl files found in {args.folder}")
    results = [audit_file(path) for path in files]
    failures = []
    for result in results:
        if result.get("error"):
            failures.append(result["file"] + ": " + result["error"])
        if result.get("missing_active_exact_name_displays"):
            failures.append(result["file"] + ": missing paragraph DISPLAY")
        if not result.get("cursor_lifecycle_second_pass_idempotent", False):
            failures.append(result["file"] + ": cursor lifecycle pass is not idempotent")
        for cursor, operations in result.get("cursor_lifecycle", {}).items():
            if not all(operations[op]["paragraph_found"] for op in ("OPEN", "FETCH", "CLOSE")):
                failures.append(result["file"] + f": incomplete cursor lifecycle for {cursor}")
    report = {
        "files_audited": len(results),
        "passed": not failures,
        "failures": failures,
        "results": results,
    }
    rendered = json.dumps(report, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
