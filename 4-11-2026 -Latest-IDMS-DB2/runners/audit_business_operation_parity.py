"""Audit source IDMS DML family coverage in converted DB2 COBOL candidates."""
from __future__ import annotations

import argparse
from pathlib import Path

from converter.analyzers.program_flow.business_operation_parity_audit import BusinessOperationParityAuditor

DEFAULT_ROOT = Path(__file__).resolve().parents[1] / "mainframe" / "workspace"
DEFAULT_PAIRS = (
    ("VM1BD526.cbl", "VMDZ1526"),
    ("VM1BD567.cbl", "VMDZ1567"),
    ("VM4BD302.cbl", "VMDZ4302"),
    ("VM4BD310.cbl", "VMDZ4310"),
    ("VM4BD420.cbl", "VMDZ4420"),
    ("VM7BD200.cbl", "VMDZ7200"),
)


def latest_candidate(output_dir: Path, target_prefix: str) -> Path | None:
    """Return newest generated output regardless of timestamp/stable filename style."""
    candidates = [path for path in output_dir.glob(f"{target_prefix}_*.cbl") if path.is_file()]
    return max(candidates, key=lambda path: (path.stat().st_mtime_ns, path.name), default=None)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--output", type=Path, help="specific generated COBOL candidate for a single program")
    parser.add_argument("--source", type=Path, help="specific original IDMS COBOL source")
    parser.add_argument("--mapping", type=Path, help="explicit mapping export; required if workspace has multiple exports")
    args = parser.parse_args()
    mapping_files = sorted((args.workspace / "Mapping Sheet").glob("*.csv"))
    if args.mapping:
        mapping_csv = args.mapping
    elif len(mapping_files) == 1:
        mapping_csv = mapping_files[0]
    else:
        parser.error("provide --mapping: workspace must contain exactly one mapping CSV")
    if not mapping_csv.is_file():
        parser.error(f"mapping export does not exist: {mapping_csv}")
    dclgen_dir = args.workspace / "DCLGen"
    auditor = BusinessOperationParityAuditor(mapping_csv=mapping_csv, dclgen_dir=dclgen_dir)
    failed = False
    pairs = [(args.source, args.output)] if args.source and args.output else DEFAULT_PAIRS
    if bool(args.source) != bool(args.output):
        parser.error("--source and --output must be supplied together")
    output_dir = args.output_dir or (args.workspace / "Output")
    for source_name, target_prefix in pairs:
        source_path = source_name if isinstance(source_name, Path) else args.workspace / "Program" / source_name
        if args.source and args.output:
            target_path = args.output
        else:
            # Include stable names as well as timestamped candidates. Timestamp-only
            # filtering could silently audit an older output after regeneration.
            target_path = latest_candidate(output_dir, target_prefix)
            if target_path is None:
                print(f"ERROR {target_prefix}: no generated candidate found in {output_dir}")
                failed = True
                continue
        if not source_path.is_file() or not target_path.is_file():
            print(f"ERROR missing pair: {source_path} -> {target_path}")
            failed = True
            continue
        report = auditor.audit(source_path, target_path)
        status = "FAIL" if report.issues else ("REVIEW" if report.reviews else "PASS")
        print(
            f"{status} {source_path.name} -> {target_path.name}: "
            f"source_ops={len(report.source_operations)} target_sql_families={','.join(report.target_sql_families) or '<none>'} "
            f"issues={len(report.issues)} reviews={len(report.reviews)}"
        )
        for issue in report.issues:
            print(f"  ERROR {issue.code} line {issue.line} [{issue.family}]: {issue.message}")
        for review in report.reviews:
            print(f"  REVIEW line {review.line} [{review.family}] {review.operand or '<unknown>'}: {review.message}")
        failed = failed or bool(report.issues)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
