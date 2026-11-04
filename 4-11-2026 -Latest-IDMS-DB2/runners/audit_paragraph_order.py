"""Compare original IDMS and converted DB2 COBOL paragraph source order."""
from __future__ import annotations

import argparse
from pathlib import Path

from converter.analyzers.program_flow.paragraph_order_audit import ParagraphOrderAuditor


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--pair", action="append", required=True, metavar="ORIGINAL=CONVERTED",
        help="repeat once per program; paths containing '=' are not supported",
    )
    args = parser.parse_args()
    auditor = ParagraphOrderAuditor()
    failed = False
    for item in args.pair:
        if "=" not in item:
            print(f"ERROR invalid pair {item!r}; expected ORIGINAL=CONVERTED")
            failed = True
            continue
        original_raw, converted_raw = item.split("=", 1)
        original, converted = Path(original_raw), Path(converted_raw)
        if not original.is_file() or not converted.is_file():
            print(f"ERROR missing input: original={original.is_file()} converted={converted.is_file()} ({item})")
            failed = True
            continue
        result = auditor.audit(original, converted)
        status = "ORDER-OK" if result.order_preserved else "ORDER-CHANGED"
        print(
            f"{status} {original.name} -> {converted.name}: "
            f"original_paragraphs={result.original_count} converted_paragraphs={result.converted_count} "
            f"shared={len(result.shared_in_original_order)} missing={len(result.missing_from_converted)}"
        )
        for diagnostic in result.diagnostics:
            print(f"  REVIEW: {diagnostic}")
        failed = failed or not result.order_preserved
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
