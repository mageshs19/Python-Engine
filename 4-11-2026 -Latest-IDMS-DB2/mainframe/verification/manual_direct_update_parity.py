"""Narrow, source-proven manual-parity evidence for paired IDMS CALC/MODIFY.

A handwritten DB2 reference can demonstrate that a generated direct UPDATE
matches the *manual DB2 design*. It does not prove the IDMS runtime's implicit
not-found behavior. Only the two duplicate CALC/UPDATE parity review findings
are eligible for this manual-equivalence classification. No source program or
record name is special-cased.
"""
from __future__ import annotations

import re
from pathlib import Path

from converter.analyzers.program_flow.business_operation_parity_audit import (
    OperationParityReview,
    _body,
    _read_source,
    _target_sql_blocks_with_following_context,
)
from converter.parsers.cobol_parser import CobolParser


_PAIR = re.compile(r"([A-Z][A-Z0-9_]*)\s*=\s*(:[A-Z][A-Z0-9-]*\.[A-Z][A-Z0-9-]*)\s*", re.I)


def _update_assignments(sql: str) -> tuple[str, tuple, tuple] | None:
    normalized = re.sub(r"\s+", " ", sql.upper()).strip().rstrip(".")
    match = re.fullmatch(
        r"UPDATE\s+([A-Z][A-Z0-9_.]*)\s+SET\s+(.+?)\s+WHERE\s+(.+?)"
        r"(?:\s+QUERYNO\s+\d+)?\s*", normalized,
    )
    if not match:
        return None
    table, assignments, predicates = match.groups()

    def parse(section: str, separator: str) -> tuple | None:
        parts = re.split(separator, section, flags=re.I)
        result = []
        for part in parts:
            paired = _PAIR.fullmatch(part.strip())
            if not paired:
                return None  # no OR, expressions, arithmetic, or opaque SQL
            result.append((paired.group(1), paired.group(2)))
        if len(set(item[0] for item in result)) != len(result):
            return None
        return tuple(sorted(result)) if result else None

    set_items = parse(assignments, r"\s*,\s*")
    where_items = parse(predicates, r"\s+AND\s+")
    if not set_items or not where_items:
        return None
    return table.split(".")[-1], set_items, where_items


def _sqlcode_actions(context: str) -> tuple[str, str] | None:
    """Require an operation-local success/error branch with no hidden actions."""
    matched = re.search(r"\bEVALUATE\s+SQLCODE\b(.*?)\bEND-EVALUATE\b", context, re.I | re.S)
    if not matched:
        return None
    branches = list(re.finditer(r"\bWHEN\s+(ZERO|0|100|OTHER)\b", matched.group(1), re.I))
    if len(branches) != 2:
        return None
    kinds = {m.group(1).upper() for m in branches}
    if kinds not in ({"0", "OTHER"}, {"ZERO", "OTHER"}):
        return None
    result = {}
    for index, branch in enumerate(branches):
        start = branch.end()
        end = branches[index + 1].start() if index + 1 < len(branches) else len(matched.group(1))
        code = matched.group(1)[start:end].upper()
        # DISPLAY is diagnostics only, but everything that changes COBOL state
        # or control flow must match and must be understood.
        statements = []
        for line in code.splitlines():
            line = line.strip().rstrip(".")
            if not line or line.startswith("DISPLAY"):
                continue
            action = re.fullmatch(r"ADD\s+\+?1\s+TO\s+([A-Z][A-Z0-9-]*)", line)
            if action:
                statements.append("ADD 1 TO " + action.group(1))
                continue
            action = re.fullmatch(r"PERFORM\s+([A-Z][A-Z0-9-]*)", line)
            if action:
                statements.append("PERFORM " + action.group(1))
                continue
            if line == "CONTINUE":
                continue
            # Wrapped DISPLAY operands, optional SQL-LOCATION or any other
            # statement are ambiguous: do not certify this manual comparison.
            if re.fullmatch(r"'(?:[^']|'')*'", line):
                continue
            return None
        key = "0" if branch.group(1).upper() in {"0", "ZERO"} else branch.group(1).upper()
        result[key] = tuple(statements)
    if not result.get("0") or "PERFORM SQLERROR" not in result.get("OTHER", ()):
        return None
    return result["0"], result["OTHER"]


def _source_has_unconditional_pair(source_text: str, record: str) -> bool:
    executable, operations = _read_source(source_text)
    for pos, op in enumerate(operations[:-1]):
        following = operations[pos + 1]
        if not (
            op.family == "SELECT" and op.statement == f"OBTAIN CALC {record}"
            and following.family == "UPDATE" and following.operand == record
            and op.paragraph == following.paragraph
        ):
            continue
        between = " ".join(code for line, code in executable if op.line <= line < following.line).upper()
        # An explicit error handler or fetched-field dependency is business
        # semantics, not an optimization of the CALC read.
        if re.search(r"\b(?:ON\s+DB-REC-NOT-FOUND|ERROR-STATUS|DB-REC-NOT-FOUND|"
                     r"IF|EVALUATE|WHEN|EXEC|PERFORM|CALL|READ|WRITE|STORE|ERASE|EXIT)\b", between):
            continue
        if re.search(rf"\bMOVE\b[^.]*?\bOF\s+{re.escape(record)}\s+TO\b", between):
            continue
        return True
    return False


def manually_confirmed_direct_updates(
    source_text: str,
    generated_text: str,
    manual_text: str,
    reviews: tuple[OperationParityReview, ...],
    mapped_tables: dict[str, set[str]],
) -> tuple[set[str], tuple[OperationParityReview, ...]]:
    """Return eligible record operands and reviews still requiring resolution.

    Exact manual PROGRAM-ID, single target UPDATE, exact SET/WHERE host pairs,
    and identical operation-local SQLCODE handling are required. Evidence is
    not extrapolated to other SQL or other records in a program.
    """
    generated_id = CobolParser().program_id(generated_text)
    if not generated_id or CobolParser().program_id(manual_text) != generated_id:
        return set(), reviews
    candidates = {getattr(item, "operand", None) for item in reviews if getattr(item, "operand", None)}
    confirmed = set()
    generated_sql = _target_sql_blocks_with_following_context(generated_text)
    manual_sql = _target_sql_blocks_with_following_context(manual_text)
    for record in sorted(candidates):
        if not _source_has_unconditional_pair(source_text, record):
            continue
        tables = mapped_tables.get(record, set())
        if not tables:
            continue
        gen = [(sql, context) for family, table, sql, context in generated_sql
               if family == "UPDATE" and table in tables]
        ref = [(sql, context) for family, table, sql, context in manual_sql
               if family == "UPDATE" and table in tables]
        if len(gen) != 1 or len(ref) != 1:
            continue
        if _update_assignments(gen[0][0]) is None or _update_assignments(gen[0][0]) != _update_assignments(ref[0][0]):
            continue
        gen_handler, ref_handler = _sqlcode_actions(gen[0][1]), _sqlcode_actions(ref[0][1])
        if gen_handler is None or gen_handler != ref_handler:
            continue
        # Manual SELECT or other SQL on the same mapped table can carry
        # pre-update semantics missing from the generated path.
        if any(family in {"SELECT", "DELETE", "INSERT"} and table in tables
               for family, table, _sql, _context in manual_sql):
            continue
        confirmed.add(record)
    resolved_phrases = ("no SELECT on mapped table", "no operation-local affected-row check")
    unresolved = tuple(item for item in reviews if not (
        getattr(item, "operand", None) in confirmed and any(phrase in item.message for phrase in resolved_phrases)
    ))
    return confirmed, unresolved
