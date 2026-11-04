"""Byte-exact, order-sensitive verification of fixed-length batch output files.

Run after the original/manual and converted programs execute against an
identical snapshot with identical job parameters. This comparator does not
pretend that matching COBOL source proves output equivalence.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class FileEvidence:
    path: str
    bytes: int
    records: int | None
    sha256: str
    aligned: bool


@dataclass(frozen=True)
class Comparison:
    passed: bool
    record_size: int
    manual: FileEvidence
    generated: FileEvidence
    first_mismatched_record: int | None
    first_mismatched_byte: int | None
    reason: str


def _evidence(path: Path, record_size: int, chunk_bytes: int = 1024 * 1024) -> FileEvidence:
    digest = hashlib.sha256()
    size = 0
    with path.open('rb') as stream:
        while data := stream.read(chunk_bytes):
            digest.update(data)
            size += len(data)
    aligned = (size % record_size) == 0
    return FileEvidence(str(path), size, size // record_size if aligned else None, digest.hexdigest(), aligned)


def compare(manual: str | Path, generated: str | Path, record_size: int) -> Comparison:
    """Compare records exactly, including padding and original file order.

    Neither EBCDIC nor ASCII decoding is attempted. The files must both be raw
    fixed-record bytes in the same encoding; VB/RDW and text line endings are
    deliberately not accepted. Data bytes are never included in the report.
    """
    if not isinstance(record_size, int) or isinstance(record_size, bool) or record_size <= 0:
        raise ValueError('record_size must be a positive integer')
    m, g = Path(manual), Path(generated)
    if m.resolve() == g.resolve():
        raise ValueError('manual and generated files must be different physical paths')
    me, ge = _evidence(m, record_size), _evidence(g, record_size)
    if not me.aligned or not ge.aligned:
        return Comparison(False, record_size, me, ge, None, None,
                          'input size is not a multiple of the declared fixed-record length')
    if me.bytes == ge.bytes and me.sha256 == ge.sha256:
        return Comparison(True, record_size, me, ge, None, None, 'byte-exact match')
    with m.open('rb') as ms, g.open('rb') as gs:
        index = 0
        while True:
            left, right = ms.read(record_size), gs.read(record_size)
            if not left and not right:
                break
            index += 1
            if left != right:
                if len(left) != len(right):
                    return Comparison(False, record_size, me, ge, index, None,
                                      'different record counts')
                offset = next((i + 1 for i, (a, b) in enumerate(zip(left, right)) if a != b), None)
                return Comparison(False, record_size, me, ge, index, offset,
                                  'record bytes differ at the indicated 1-based position')
    return Comparison(False, record_size, me, ge, None, None,
                      'hash mismatch without detected byte difference (unexpected I/O change)')


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description='Compare manual and generated fixed-record outputs (exact bytes/order).')
    parser.add_argument('--manual', type=Path, required=True)
    parser.add_argument('--generated', type=Path, required=True)
    parser.add_argument('--record-size', type=int, required=True,
                        help='fixed LRECL in bytes, from FD/JCL. No line delimiters or RDWs.')
    parser.add_argument('--report', type=Path, help='write machine-readable result without exposing data bytes')
    args = parser.parse_args(argv)
    try:
        result = compare(args.manual, args.generated, args.record_size)
    except (ValueError, OSError) as exc:
        parser.exit(2, f'FAIL: {exc}\n')
    report = json.dumps(asdict(result), indent=2) + '\n'
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(report, encoding='utf-8')
    print(report, end='')
    return 0 if result.passed else 2


if __name__ == '__main__':
    raise SystemExit(main())
