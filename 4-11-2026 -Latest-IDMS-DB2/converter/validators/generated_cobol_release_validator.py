"""Static release gate for generated fixed-format COBOL with embedded DB2 SQL.

This is deliberately a structural validator, not a replacement for the DB2
precompiler or Enterprise COBOL compiler. It catches common generator defects
before a file is promoted to a mainframe compile/test environment.
"""
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

from rules.cursor_close_guarantee_rules import NON_PARAGRAPH_SINGLE_WORDS
from converter.services.perform_thru_scope import paragraph_indices, perform_spans
from converter.analyzers.access_error_policy import AccessPattern, classify_access, policy_for


@dataclass(frozen=True)
class ValidationIssue:
    severity: str
    code: str
    line: int
    message: str


_FIXED = re.compile(r"^\d{6}([ */Dd-])")
_EXEC_SQL = re.compile(r"\bEXEC\s+SQL\b", re.I)
_END_EXEC = re.compile(r"\bEND-EXEC\b", re.I)
_SQL_SELECT_INTO = re.compile(r"\bSELECT\s+(.*?)\s+INTO\s+(.*?)\s+FROM\b", re.I | re.S)


def _line_parts(line: str) -> tuple[str, str]:
    if len(line) >= 7 and line[:6].isdigit():
        return line[6:7], line[7:72].rstrip()
    return " ", line.rstrip()


def _is_comment(line: str) -> bool:
    indicator, _ = _line_parts(line)
    return indicator in {"*", "/", "D", "d"}


def _mask_literals_and_inline_comment(body: str) -> str:
    """Blank literals and COBOL inline comments without changing offsets.

    The release gate searches executable COBOL/SQL tokens. Keeping string
    positions stable lets SQL-boundary matches index the original line while
    preventing values such as 'END-EXEC' or 'END-PERFORM' from being parsed as
    syntax. Doubled quote delimiters inside literals are handled.
    """
    chars = list(str(body or ""))
    quote: str | None = None
    i = 0
    while i < len(chars):
        char = chars[i]
        if quote is not None:
            chars[i] = " "
            if char == quote:
                if i + 1 < len(chars) and chars[i + 1] == quote:
                    chars[i + 1] = " "
                    i += 2
                    continue
                quote = None
            i += 1
            continue
        if char in {"'", '"'}:
            quote = char
            chars[i] = " "
            i += 1
            continue
        if char == "*" and i + 1 < len(chars) and chars[i + 1] == ">":
            for j in range(i, len(chars)):
                chars[j] = " "
            break
        i += 1
    return "".join(chars)


def _sql_list_items(text: str) -> list[str]:
    """Split a simple SQL comma list; fail-closed for expressions/aliases."""
    items = [item.strip().lstrip(",").strip() for item in text.replace("\n", " ").split(",")]
    return [item for item in items if item]


def validate_generated_cobol(text: str, *, path: str = "<memory>") -> list[ValidationIssue]:
    lines = str(text or "").splitlines()
    issues: list[ValidationIssue] = []

    # Fixed-format record width and sequence area.
    for number, line in enumerate(lines, 1):
        if _FIXED.match(line) and len(line) > 80:
            issues.append(ValidationIssue("ERROR", "FIXED_WIDTH", number,
                                          f"fixed-format record is {len(line)} columns (maximum 80)"))

    # Protect PERFORM THRU physical execution ranges from synthetic helper
    # paragraphs invoked explicitly elsewhere. A helper inside such a range
    # is executed again by fall-through, even if its PERFORM call is guarded.
    labels = paragraph_indices(lines)
    scopes = perform_spans(lines)
    executed = "\n".join(
        _mask_literals_and_inline_comment(_line_parts(line)[1]).upper()
        for line in lines if not _is_comment(line)
    )
    for name, index in labels.items():
        if not name.startswith("WRITE-"):
            continue
        if not re.search(rf"\bPERFORM\s+{re.escape(name)}\b", executed):
            continue
        for span in scopes:
            if span.start_index <= index <= span.end_index:
                issues.append(ValidationIssue(
                    "ERROR", "WRITE_HELPER_INSIDE_PERFORM_THRU", index + 1,
                    f"{name} is inside PERFORM {span.start} THRU {span.end}: possible unguarded duplicate WRITE",
                ))
                break

    # Embedded SQL blocks must be paired. This is lexical only; precompiler
    # validation is still required for SQL grammar and host-variable typing.
    sql_depth = 0
    sql_start = 0
    sql_blocks: list[tuple[int, int, str]] = []
    active: list[str] = []
    for number, line in enumerate(lines, 1):
        if _is_comment(line):
            continue
        body = _line_parts(line)[1]
        syntax = _mask_literals_and_inline_comment(body)
        cursor = 0
        while cursor < len(body):
            if not sql_depth:
                start_match = re.search(r"\bEXEC\s+SQL\b", syntax[cursor:], re.I)
                if not start_match:
                    break
                sql_depth = 1
                sql_start = number
                active = []
                cursor += start_match.end()
            end_match = re.search(r"\bEND-EXEC\b", syntax[cursor:], re.I)
            next_start = re.search(r"\bEXEC\s+SQL\b", syntax[cursor:], re.I)
            if next_start and (not end_match or next_start.start() < end_match.start()):
                issues.append(ValidationIssue("ERROR", "NESTED_SQL", number,
                                              "EXEC SQL starts before previous END-EXEC"))
                active.append(body[cursor:cursor + next_start.start()])
                cursor += next_start.end()
                sql_start = number
                active = []
                continue
            if end_match:
                active.append(body[cursor:cursor + end_match.start()])
                sql_blocks.append((sql_start, number, "\n".join(active)))
                sql_depth = 0
                active = []
                cursor += end_match.end()
            else:
                active.append(body[cursor:])
                cursor = len(body)
    if sql_depth:
        issues.append(ValidationIssue("ERROR", "MISSING_END_EXEC", sql_start,
                                      "EXEC SQL has no matching END-EXEC"))

    for start, _end, sql in sql_blocks:
        # Only singleton SELECT INTO statements have an explicit host list.
        # Cursor declarations use SELECT without INTO and are checked elsewhere.
        for match in _SQL_SELECT_INTO.finditer(sql):
            columns = _sql_list_items(match.group(1))
            hosts = re.findall(r":\s*[A-Z][A-Z0-9-]*(?:\.[A-Z][A-Z0-9-]*)?", match.group(2), re.I)
            if not columns or not hosts:
                issues.append(ValidationIssue("ERROR", "SQL_PROJECTION_UNREADABLE", start,
                                              "could not parse SELECT projection or INTO host list"))
            elif len(columns) != len(hosts):
                issues.append(ValidationIssue("ERROR", "SQL_PROJECTION_MISMATCH", start,
                                              f"SELECT has {len(columns)} columns but INTO has {len(hosts)} host variables"))

    # Residual IDMS executable statements are release blockers. Ignore comments
    # and inspect only the COBOL source area, not sequence/identification fields.
    residual_patterns = (
        ("RESIDUAL_OBTAIN", re.compile(r"\bOBTAIN\s+(?:CALC|FIRST|NEXT)\b", re.I)),
        # Cover the complete core IDMS DML/access family. These checks apply
        # only to executable source areas; comments and quoted literals are
        # masked above. A generated DB2 candidate must not silently retain an
        # IDMS mutation/access command merely because the earlier gate focused
        # on OBTAIN and ERROR-STATUS.
        ("RESIDUAL_MODIFY", re.compile(r"\bMODIFY\s+[A-Z][A-Z0-9-]*\b", re.I)),
        ("RESIDUAL_STORE", re.compile(r"\bSTORE\s+[A-Z][A-Z0-9-]*\b", re.I)),
        ("RESIDUAL_ERASE", re.compile(r"\bERASE\s+[A-Z][A-Z0-9-]*\b", re.I)),
        ("RESIDUAL_BIND", re.compile(r"\bBIND\s+(?:RUN-UNIT|[A-Z][A-Z0-9-]*)\b", re.I)),
        ("RESIDUAL_READY", re.compile(r"\bREADY\s+[A-Z][A-Z0-9-]*\s+USAGE-MODE\b", re.I)),
        ("RESIDUAL_FINISH", re.compile(r"\bFINISH\s*\.", re.I)),
        ("RESIDUAL_IDMS_ERROR", re.compile(r"\bON\s+ANY-ERROR-STATUS\b", re.I)),
        ("RESIDUAL_IDMS_STATUS", re.compile(r"\bPERFORM\s+IDMS-STATUS\b", re.I)),
        ("RESIDUAL_IDMS_COPY", re.compile(r"\bCOPY\s+IDMS\s+IDMS-STATUS\b", re.I)),
        ("RESIDUAL_ERROR_STATUS", re.compile(r"\bERROR-STATUS\b", re.I)),
    )
    for number, line in enumerate(lines, 1):
        if _is_comment(line):
            continue
        body = _mask_literals_and_inline_comment(_line_parts(line)[1])
        for code, pattern in residual_patterns:
            if pattern.search(body):
                issues.append(ValidationIssue("ERROR", code, number,
                                              f"residual executable IDMS statement: {pattern.pattern}"))

    # Reserved COBOL verbs are not data receivers. A period-free MOVE that
    # accidentally absorbs the following WRITE/READ statement may compile into
    # multiple bogus MOVE receivers and silently remove a file output. Fail
    # the candidate even if the upstream parser regresses again.
    invalid_move_target = re.compile(
        r"\bMOVE\s+[^.\n]*?\bTO\s+(?:WRITE|REWRITE|READ|FROM|CLOSE|OPEN|PERFORM|END-IF|END-PERFORM)\b",
        re.I,
    )
    for number, line in enumerate(lines, 1):
        if _is_comment(line):
            continue
        syntax = _mask_literals_and_inline_comment(_line_parts(line)[1])
        if invalid_move_target.search(syntax):
            issues.append(ValidationIssue(
                "ERROR", "INVALID_MOVE_RECEIVER", number,
                "MOVE has a COBOL verb or clause keyword as a receiving data item; possible swallowed statement",
            ))

    # A bounded LRF FIRST/NEXT search with an inline business predicate must
    # not silently pass release validation while its generated cursor walk is
    # still present. The post-layout singleton rewriter is expected to remove
    # this exact safe shape; catching stale pre-rewrite artifacts here prevents
    # an old output file from being mistaken for the current conversion.
    executable = "\n".join(
        _mask_literals_and_inline_comment(_line_parts(line)[1])
        for line in lines if not _is_comment(line)
    )
    executable_upper = executable.upper()
    has_expanded_lrf_first = "EXPANDED LRF FIRST" in str(text or "").upper()
    bounded_cursor = re.search(
        r"\bDECLARE\s+(?P<cursor>[A-Z0-9-]+)\s+CURSOR\s+WITH\s+HOLD\b",
        executable_upper,
        re.I,
    )
    if has_expanded_lrf_first and bounded_cursor:
        cursor_name = bounded_cursor.group("cursor")
        if (
            re.search(rf"\bPERFORM\s+UNTIL\s+{re.escape(cursor_name)}-EOC\b", executable_upper, re.I)
            and re.search(rf"\bPERFORM\s+[0-9]+-FETCH-{re.escape(cursor_name)}\b", executable_upper, re.I)
            and re.search(r"\b[A-Z][A-Z0-9-]*\s+(?:OF\s+[A-Z][A-Z0-9-]*)?\s*=\s*['\"]?[^\s.]+", executable_upper, re.I)
        ):
            issues.append(ValidationIssue(
                "ERROR", "LRF_BOUNDED_CURSOR_REMAINS", 0,
                f"bounded LRF cursor {cursor_name} remains in generated output; run the singleton rewrite or retain it as an explicit unresolved release blocker",
            ))

    # Generated numeric paragraph references must resolve. This is a
    # structural control-flow check: it catches stale PERFORM targets after
    # paragraph renumbering without trying to reinterpret business logic.
    paragraph_header = re.compile(
        r"^\s*(?P<name>(?:\d{1,6}-)?[A-Z][A-Z0-9-]*)\.\s*$",
        re.I,
    )
    paragraph_names: set[str] = set()
    paragraph_positions: dict[str, list[int]] = {}
    duplicate_cursor_headers: set[str] = set()
    for number, line in enumerate(lines, 1):
        if _is_comment(line):
            continue
        body = _line_parts(line)[1]
        match = paragraph_header.fullmatch(body)
        if not match:
            continue
        name = match.group("name").upper()
        # COBOL verbs such as END-IF and END-EXEC are period-terminated but
        # are not paragraph headers. Excluding them is essential before
        # building PERFORM/THRU ranges.
        if name in NON_PARAGRAPH_SINGLE_WORDS:
            continue
        if name in paragraph_names and re.match(r"^\d{3,6}-(?:OPEN|FETCH|CLOSE)-", name):
            duplicate_cursor_headers.add(name)
        paragraph_names.add(name)
        paragraph_positions.setdefault(name, []).append(number)
    for name in sorted(duplicate_cursor_headers):
        issues.append(ValidationIssue(
            "ERROR", "DUPLICATE_CURSOR_PARAGRAPH", 0,
            f"generated cursor paragraph {name} is defined more than once",
        ))

    # Numbered PERFORM and PERFORM THRU endpoints are the highest-risk
    # references when the paragraph allocator changes. Validate all numeric
    # targets, not only generated cursor calls, while leaving named external
    # or copybook-provided paragraphs alone.
    numeric_perform = re.compile(
        r"\bPERFORM\s+(?P<target>\d{1,6}-[A-Z][A-Z0-9-]*)"
        r"(?:\s+(?:THRU|THROUGH)\s+(?P<through>\d{1,6}-[A-Z][A-Z0-9-]*))?",
        re.I,
    )
    for number, line in enumerate(lines, 1):
        if _is_comment(line):
            continue
        body = _mask_literals_and_inline_comment(_line_parts(line)[1])
        for match in numeric_perform.finditer(body):
            target = match.group("target").upper()
            through = (match.group("through") or "").upper()
            if target not in paragraph_names:
                issues.append(ValidationIssue(
                    "ERROR", "PERFORM_TARGET_MISSING", number,
                    f"PERFORM references numbered paragraph {target}, but no matching paragraph exists",
                ))
            if through and through not in paragraph_names:
                issues.append(ValidationIssue(
                    "ERROR", "PERFORM_THRU_TARGET_MISSING", number,
                    f"PERFORM THRU references numbered end paragraph {through}, but no matching paragraph exists",
                ))

    # PERFORM A THRU B executes a physical paragraph range. Both labels
    # resolving is insufficient if B appears before A: that can execute a
    # much larger/different range than the author intended. Also refuse a
    # range that accidentally encloses generated cursor paragraphs; cursor
    # operations are independently controlled and must not be swept into a
    # business paragraph range by a numbering/layout change.
    perform_thru = re.compile(
        r"\bPERFORM\s+(?P<target>(?:\d{1,6}-)?[A-Z][A-Z0-9-]*)"
        r"\s+(?:THRU|THROUGH)\s+(?P<through>(?:\d{1,6}-)?[A-Z][A-Z0-9-]*)",
        re.I,
    )
    cursor_header_lines = {
        line_number
        for name, positions in paragraph_positions.items()
        if re.match(r"^\d{3,6}-(?:OPEN|FETCH|CLOSE)-", name)
        for line_number in positions
    }
    perform_flow_source = "\n".join(
        "" if _is_comment(line)
        else _mask_literals_and_inline_comment(_line_parts(line)[1])
        for line in lines
    )
    for match in perform_thru.finditer(perform_flow_source):
        number = perform_flow_source.count("\n", 0, match.start()) + 1
        target = match.group("target").upper()
        through = match.group("through").upper()
        starts = paragraph_positions.get(target, [])
        ends = paragraph_positions.get(through, [])
        if not starts or not ends:
            continue  # Missing numeric endpoints are reported above.
        start_line = starts[0]
        end_line = ends[0]
        if end_line < start_line:
            issues.append(ValidationIssue(
                "ERROR", "PERFORM_THRU_REVERSED", number,
                f"PERFORM THRU range {target} -> {through} is reversed in source order",
            ))
            continue
        enclosed = sorted(
            cursor_line for cursor_line in cursor_header_lines
            if start_line < cursor_line < end_line
        )
        if enclosed:
            issues.append(ValidationIssue(
                "ERROR", "PERFORM_THRU_CROSSES_CURSOR_PARAGRAPH", number,
                f"PERFORM THRU range {target} -> {through} encloses generated cursor paragraph(s); verify business-flow boundaries",
            ))

    # Duplicate non-cursor paragraph labels are also unsafe: PERFORM resolution
    # becomes compiler- or dialect-dependent. Cursor duplicates have their own
    # more specific diagnostic above.
    for name, positions in paragraph_positions.items():
        if len(positions) > 1 and name not in duplicate_cursor_headers:
            issues.append(ValidationIssue(
                "ERROR", "DUPLICATE_PARAGRAPH_LABEL", positions[1],
                f"paragraph label {name} is defined more than once (lines {positions[0]} and {positions[1]})",
            ))

    # IDMS-STOP is a program-defined termination path, not a generic status
    # hook. A retained PERFORM must resolve to its paragraph, and the common
    # SQLCODE guard must not end with a period immediately before that PERFORM:
    # COBOL would then execute the stop call unconditionally.
    executable_lines = [
        (number, _mask_literals_and_inline_comment(_line_parts(line)[1]).strip())
        for number, line in enumerate(lines, 1)
        if not _is_comment(line)
    ]
    has_stop_call = any(
        re.search(r"\bPERFORM\s+IDMS-STOP\b", body, re.I)
        for _, body in executable_lines
    )
    if has_stop_call and "IDMS-STOP" not in paragraph_names:
        call_line = next(
            number for number, body in executable_lines
            if re.search(r"\bPERFORM\s+IDMS-STOP\b", body, re.I)
        )
        issues.append(ValidationIssue(
            "ERROR", "IDMS_STOP_TARGET_MISSING", call_line,
            "PERFORM IDMS-STOP is present but no local IDMS-STOP paragraph resolves it",
        ))
    for index, (number, body) in enumerate(executable_lines):
        if not re.fullmatch(r"IF\s+SQLCODE\s+NOT\s*=\s*0\s*\.", body, re.I):
            continue
        next_item = next(
            ((next_number, next_body) for next_number, next_body in executable_lines[index + 1:]
             if next_body),
            None,
        )
        if next_item and re.match(r"PERFORM\s+IDMS-STOP\b", next_item[1], re.I):
            issues.append(ValidationIssue(
                "ERROR", "IDMS_STOP_IF_SCOPE_BROKEN", number,
                f"period ends IF before {next_item[1]}; IDMS-STOP would execute unconditionally",
            ))

    cursor_targets = re.compile(
        r"\bPERFORM\s+(?P<target>\d{3,6}-(?:OPEN|FETCH|CLOSE)-[A-Z0-9-]+)\b",
        re.I,
    )
    for number, line in enumerate(lines, 1):
        if _is_comment(line):
            continue
        body = _mask_literals_and_inline_comment(_line_parts(line)[1])
        for match in cursor_targets.finditer(body):
            target = match.group("target").upper()
            if target not in paragraph_names:
                issues.append(ValidationIssue(
                    "ERROR", "PERFORM_CURSOR_TARGET_MISSING", number,
                    f"PERFORM references generated cursor paragraph {target}, but no matching paragraph exists",
                ))

    # Cursor numbering is a contract, not a label-only style choice. For
    # each complete generated cursor, OPEN/FETCH/CLOSE must follow either the
    # legacy 710/720/730 convention or the current four-digit 2100/2200/2300
    # convention, and SQL-LOCATION inside each operation must match its label.
    cursor_ops: dict[str, dict[str, tuple[int, str]]] = {}
    cursor_first_position: dict[str, int] = {}
    cursor_header = re.compile(
        r"^\s*(?P<number>\d{3,6})-(?P<operation>OPEN|FETCH|CLOSE)-(?P<cursor>[A-Z0-9-]+)\.\s*$",
        re.I,
    )
    for index, line in enumerate(lines):
        if _is_comment(line):
            continue
        body = _line_parts(line)[1]
        match = cursor_header.fullmatch(body)
        if match:
            cursor_name = match.group("cursor").upper()
            cursor_first_position.setdefault(cursor_name, index)
            cursor_ops.setdefault(cursor_name, {})[
                match.group("operation").lower()
            ] = (int(match.group("number")), match.group("operation").upper())
    # Prefer cursor DECLARE order as the identity authority; generated paragraph
    # order is a fallback for snippets/legacy files that omit declarations.
    # This prevents a paragraph-layout change from silently redefining C1/C2.
    declared_cursor_order: dict[str, int] = {}
    declare_pattern = re.compile(r"\bDECLARE\s+([A-Z][A-Z0-9-]*)\s+CURSOR\b", re.I)
    for sql_start_line, _sql_end_line, sql in sorted(sql_blocks, key=lambda block: block[0]):
        declaration = declare_pattern.search(sql)
        if declaration:
            declared_cursor_order.setdefault(declaration.group(1).upper(), sql_start_line)
    # Enforce the global contract as well as each cursor's internal offsets:
    # C1=2100/2200/2300, C2=2400/2500/2600, C3=2700/2800/2900, etc.
    ordered_cursors = sorted(
        cursor_ops,
        key=lambda name: (
            0 if name in declared_cursor_order else 1,
            declared_cursor_order.get(name, cursor_first_position[name]),
            cursor_first_position[name],
        ),
    )
    for cursor_order, cursor in enumerate(ordered_cursors, start=1):
        operations = cursor_ops[cursor]
        # Inspect each operation paragraph until the next paragraph header;
        # the SQL location literal must stay synchronized with the label.
        ordered_headers = []
        for idx, line in enumerate(lines):
            if _is_comment(line):
                continue
            header_match = cursor_header.fullmatch(_line_parts(line)[1])
            if header_match and header_match.group("cursor").upper() == cursor:
                ordered_headers.append((idx, int(header_match.group("number"))))
        for header_idx, label_number in ordered_headers:
            end_idx = len(lines)
            for next_idx in range(header_idx + 1, len(lines)):
                if _is_comment(lines[next_idx]):
                    continue
                if paragraph_header.fullmatch(_line_parts(lines[next_idx])[1]):
                    end_idx = next_idx
                    break
            for stmt_idx in range(header_idx + 1, end_idx):
                if _is_comment(lines[stmt_idx]):
                    continue
                stmt = _mask_literals_and_inline_comment(_line_parts(lines[stmt_idx])[1])
                loc_match = re.search(r"\bMOVE\s+(\d+)\s+TO\s+SQL-LOCATION\b", stmt, re.I)
                if loc_match and int(loc_match.group(1)) != label_number:
                    issues.append(ValidationIssue(
                        "ERROR", "CURSOR_SQL_LOCATION_MISMATCH", stmt_idx + 1,
                        f"cursor paragraph numbered {label_number} sets SQL-LOCATION to {loc_match.group(1)}",
                    ))
        if set(operations) != {"open", "fetch", "close"}:
            issues.append(ValidationIssue(
                "ERROR", "INCOMPLETE_CURSOR_PARAGRAPHS", 0,
                f"cursor {cursor} has operations {sorted(operations)}; expected OPEN, FETCH, and CLOSE together",
            ))
            continue
        open_number = operations["open"][0]
        expected_open_number = 2100 + ((cursor_order - 1) * 1000)
        expected = {
            "open": expected_open_number,
            "fetch": expected_open_number + 100,
            "close": expected_open_number + 200,
        }
        if open_number >= 1000 and open_number != expected_open_number:
            issues.append(ValidationIssue(
                "ERROR", "CURSOR_IDENTITY_NUMBERING_MISMATCH", 0,
                f"cursor {cursor} is cursor #{cursor_order} in generated paragraph order but OPEN is numbered {open_number}; expected {expected_open_number} (FETCH/CLOSE +100/+200)",
            ))
        for operation, expected_number in expected.items():
            actual_number = operations[operation][0]
            if actual_number != expected_number:
                issues.append(ValidationIssue(
                    "ERROR", "CURSOR_NUMBERING_MISMATCH", 0,
                    f"cursor {cursor} {operation.upper()} is numbered {actual_number}; expected {expected_number}",
                ))

    # SQL error routing is operation-specific, not cursor-level-specific:
    # every generated OPEN/FETCH/CLOSE must send unexpected SQLCODE values
    # through the shared SQLERROR routine. SQLCODE +100 is an end-of-cursor
    # signal only for FETCH; for OPEN/CLOSE it is an unexpected result and
    # must remain in WHEN OTHER. Parent/child status affects FETCH diagnostics
    # only and must never suppress the shared error call.
    for cursor, operations in cursor_ops.items():
        for operation, (label_number, _operation_name) in operations.items():
            access_pattern = classify_access(cursor_operation=operation)
            access_policy = policy_for(access_pattern)
            header_idx = next((idx for idx, line in enumerate(lines)
                               if not _is_comment(line)
                               and (m := cursor_header.fullmatch(_line_parts(line)[1]))
                               and m.group("cursor").upper() == cursor
                               and m.group("operation").lower() == operation
                               and int(m.group("number")) == label_number), None)
            if header_idx is None:
                continue
            end_idx = len(lines)
            for next_idx in range(header_idx + 1, len(lines)):
                if _is_comment(lines[next_idx]):
                    continue
                boundary_match = paragraph_header.fullmatch(_line_parts(lines[next_idx])[1])
                if boundary_match and boundary_match.group("name").upper() not in NON_PARAGRAPH_SINGLE_WORDS:
                    end_idx = next_idx
                    break
            paragraph_lines = lines[header_idx + 1:end_idx]
            paragraph_code = "\n".join(
                _mask_literals_and_inline_comment(_line_parts(item)[1])
                for item in paragraph_lines if not _is_comment(item)
            )
            # Only validate executable cursor paragraphs; short synthetic
            # label-only snippets used by numbering checks remain supported.
            if not re.search(r"\bEXEC\s+SQL\b", paragraph_code, re.I):
                continue
            eval_match = re.search(r"\bEVALUATE\s+SQLCODE\b", paragraph_code, re.I)
            if not eval_match:
                issues.append(ValidationIssue(
                    "ERROR", "CURSOR_SQLCODE_EVALUATE_MISSING", header_idx + 1,
                    f"{label_number}-{operation.upper()}-{cursor} executes SQL but has no EVALUATE SQLCODE",
                ))
                continue
            end_eval_match = re.search(r"\bEND-EVALUATE\b", paragraph_code[eval_match.end():], re.I)
            if not end_eval_match:
                issues.append(ValidationIssue(
                    "ERROR", "CURSOR_SQLCODE_EVALUATE_UNCLOSED", header_idx + 1,
                    f"{label_number}-{operation.upper()}-{cursor} has an unclosed EVALUATE SQLCODE",
                ))
                continue
            evaluate_body = paragraph_code[eval_match.end():eval_match.end() + end_eval_match.start()]
            other_match = re.search(r"\bWHEN\s+OTHER\b", evaluate_body, re.I)
            if not other_match:
                issues.append(ValidationIssue(
                    "ERROR", "CURSOR_SQLCODE_WHEN_OTHER_MISSING", header_idx + 1,
                    f"{label_number}-{operation.upper()}-{cursor} has no WHEN OTHER SQL error branch",
                ))
                continue
            error_branch = evaluate_body[other_match.end():]
            if not re.search(r"\bPERFORM\s+SQLERROR\b", error_branch, re.I):
                issues.append(ValidationIssue(
                    "ERROR", "CURSOR_SQLERROR_PERFORM_MISSING", header_idx + 1,
                    f"{label_number}-{operation.upper()}-{cursor} WHEN OTHER does not PERFORM SQLERROR",
                ))
            if operation == "fetch" and access_policy.sqlcode_100 == "set_this_cursor_eoc_only":
                if not re.search(r"\bWHEN\s+(?:100|ZERO)\b", evaluate_body, re.I) or not re.search(r"\bWHEN\s+100\b", evaluate_body, re.I):
                    issues.append(ValidationIssue(
                        "ERROR", "CURSOR_FETCH_EOC_BRANCH_MISSING", header_idx + 1,
                        f"{label_number}-FETCH-{cursor} must handle SQLCODE 100 as end-of-cursor separately from WHEN OTHER",
                    ))
            elif re.search(r"\bWHEN\s+100\b", evaluate_body, re.I):
                issues.append(ValidationIssue(
                    "ERROR", "CURSOR_NON_FETCH_100_BRANCH", header_idx + 1,
                    f"{label_number}-{operation.upper()}-{cursor} treats SQLCODE 100 as end-of-cursor outside FETCH",
                ))

    # Inline PERFORM scopes must balance. Count the inline forms that require
    # END-PERFORM (PERFORM UNTIL, PERFORM VARYING, and PERFORM ... TIMES).
    # A paragraph call such as `PERFORM 200-READ UNTIL EOF` is not inline and
    # must not be counted; it has no END-PERFORM in COBOL. TIMES loops were
    # previously omitted, causing valid generated programs to fail this gate.
    # Reuse the masked executable stream so literals and *> comments do not
    # affect structural token counts.
    inline_until = len(re.findall(r"\bPERFORM\s+UNTIL\b", executable, re.I))
    inline_varying = len(re.findall(r"\bPERFORM\s+VARYING\b", executable, re.I))
    inline_times = len(re.findall(
        r"\bPERFORM\b(?:(?!\bPERFORM\b|\.).){0,240}?\bTIMES\b",
        executable,
        re.I | re.S,
    ))
    inline_performs = inline_until + inline_varying + inline_times
    end_performs = len(re.findall(r"\bEND-PERFORM\b", executable, re.I))
    if inline_performs != end_performs:
        issues.append(ValidationIssue("ERROR", "PERFORM_SCOPE_MISMATCH", 0,
                                      f"inline PERFORM scope count {inline_performs} != END-PERFORM count {end_performs}"))

    return issues


def validate_file(path: Path) -> list[ValidationIssue]:
    return validate_generated_cobol(path.read_text(encoding="utf-8", errors="replace"), path=str(path))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", help="generated COBOL files to validate")
    args = parser.parse_args()
    all_issues: list[tuple[str, ValidationIssue]] = []
    for raw_path in args.paths:
        path = Path(raw_path)
        if not path.is_file():
            print(f"ERROR {path}: file not found")
            return 2
        issues = validate_file(path)
        all_issues.extend((str(path), issue) for issue in issues)
        if not issues:
            print(f"PASS {path}: structural checks passed")
    for path, issue in all_issues:
        line = f":{issue.line}" if issue.line else ""
        print(f"{issue.severity} {path}{line} [{issue.code}] {issue.message}")
    return 1 if any(issue.severity == "ERROR" for _, issue in all_issues) else 0


if __name__ == "__main__":
    raise SystemExit(main())
