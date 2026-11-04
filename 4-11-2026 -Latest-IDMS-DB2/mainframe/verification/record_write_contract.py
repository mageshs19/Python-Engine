"""Static fixed-record size integrity checks driven by WRITE statements.

A proof is attempted only when the FD declares an exact LRECL and the source
buffer has a fully supported PIC layout. Unknown COPY/OCCURS/REDEFINES cases
are not silently assigned invented lengths. The audit does not replace runtime
binary output comparisons.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from .cobol_storage_layout import group_byte_length

_FD = re.compile(r'^FD\s+([\w-]+)\b', re.I)
_REC = re.compile(r'^01\s+([\w-]+)\b', re.I)
_EXPLICIT = re.compile(r'\bRECORD\s+CONTAINS\s+(\d+)(?=\s|$)', re.I)
_WRITE = re.compile(r'\bWRITE\s+([\w-]+)(?:\s+FROM\s+([\w-]+))?\b', re.I)


@dataclass(frozen=True)
class RecordWriteFinding:
    level: str  # FAIL or UNVERIFIED
    record: str
    buffer: str
    reason: str


def _code(line: str) -> str:
    if len(line) >= 7 and line[:6].isdigit():
        return '' if line[6] in ('*', '/', 'D', 'd') else line[7:72].strip()
    return '' if line.lstrip().startswith('*') else line.strip()


def _mask_quoted_literals(text: str) -> str:
    """Ignore COBOL DISPLAY/error text; only executable WRITE verbs count."""
    result = list(text)
    quote = None
    pos = 0
    while pos < len(result):
        char = result[pos]
        if quote:
            result[pos] = ' '
            if char == quote:
                if pos + 1 < len(result) and result[pos + 1] == quote:
                    result[pos + 1] = ' '
                    pos += 2
                    continue
                quote = None
        elif char in ("'", '"'):
            quote = char
            result[pos] = ' '
        pos += 1
    return ''.join(result)


def audit_fixed_record_writes(text: str) -> tuple[RecordWriteFinding, ...]:
    lines = [_code(ln) for ln in text.splitlines()]
    fd_record_size: dict[str, int] = {}
    declared_rec_size: dict[str, int] = {}
    in_fd = False
    fd = ''
    first_rec = ''
    for code in lines:
        if re.match(r'^WORKING-STORAGE\s+SECTION\b', code, re.I):
            break
        match = _FD.match(code)
        if match:
            fd, in_fd, first_rec = match.group(1).upper(), True, ''
            continue
        if not in_fd:
            continue
        declared = _EXPLICIT.search(code)
        if declared:
            fd_record_size[fd] = int(declared.group(1))
        first = _REC.match(code)
        if first and not first_rec:
            first_rec = first.group(1).upper()
            if fd in fd_record_size:
                declared_rec_size[first_rec] = fd_record_size[fd]
            else:
                try:
                    declared_rec_size[first_rec] = group_byte_length(text, first_rec)
                except ValueError:
                    pass

    findings: list[RecordWriteFinding] = []
    in_sql = False
    in_procedure = False
    for code in lines:
        if re.match(r'^PROCEDURE\s+DIVISION\b', code, re.I):
            in_procedure = True
        if not in_procedure:
            continue
        if re.search(r'\bEXEC\s+SQL\b', code, re.I):
            in_sql = True
        if in_sql:
            if re.search(r'\bEND-EXEC\b', code, re.I):
                in_sql = False
            continue
        for match in _WRITE.finditer(_mask_quoted_literals(code)):
            record, buffer = match.group(1).upper(), (match.group(2) or match.group(1)).upper()
            if record not in declared_rec_size:
                findings.append(RecordWriteFinding('UNVERIFIED', record, buffer,
                                                    'FD record size cannot be proven from the available source'))
                continue
            expected = declared_rec_size[record]
            try:
                actual = group_byte_length(text, buffer)
            except ValueError as exc:
                findings.append(RecordWriteFinding('UNVERIFIED', record, buffer,
                                                    f'output source buffer not statically evaluable: {exc}'))
                continue
            if actual != expected:
                findings.append(RecordWriteFinding('FAIL', record, buffer,
                                                    f'buffer {actual} bytes versus FD record {expected} bytes'))
    return tuple(findings)
