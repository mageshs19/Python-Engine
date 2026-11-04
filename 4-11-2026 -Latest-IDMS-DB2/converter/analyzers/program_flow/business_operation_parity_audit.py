"""Conservative source-to-target audit for IDMS DML operation coverage.

This audit does not claim semantic equivalence from counts. It checks that every
active source operation family has at least one plausible DB2 SQL counterpart in
the converted program and reports operation locations for manual review.
"""
from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class SourceOperation:
    family: str
    line: int
    paragraph: str | None
    statement: str
    operand: str | None = None


@dataclass(frozen=True)
class OperationParityIssue:
    code: str
    family: str
    line: int
    message: str


@dataclass(frozen=True)
class OperationParityReview:
    family: str
    line: int
    operand: str | None
    message: str


@dataclass(frozen=True)
class BusinessOperationParityReport:
    source_path: str
    target_path: str
    source_operations: tuple[SourceOperation, ...]
    target_sql_families: tuple[str, ...]
    issues: tuple[OperationParityIssue, ...]
    reviews: tuple[OperationParityReview, ...] = ()

    @property
    def passed(self) -> bool:
        return not self.issues


# Map the IDMS command family to the expected target SQL family. Coverage is
# intentionally family-level: cursorized reads and repeated update paths mean
# exact command counts are not semantically comparable.
_SOURCE_COMMANDS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("SELECT", re.compile(r"\bOBTAIN\s+(?:CALC|FIRST|NEXT)\s+([A-Z][A-Z0-9-]*)", re.I)),
    ("UPDATE", re.compile(r"\bMODIFY\s+([A-Z][A-Z0-9-]*)", re.I)),
    ("INSERT", re.compile(r"\bSTORE\s+([A-Z][A-Z0-9-]*)", re.I)),
    ("DELETE", re.compile(r"\bERASE\s+([A-Z][A-Z0-9-]*)", re.I)),
    # Transaction boundaries are audited independently of record/table mapping.
    ("COMMIT", re.compile(r"^\s*(COMMIT)\b", re.I)),
    ("ROLLBACK", re.compile(r"^\s*(ROLLBACK)\b", re.I)),
)
_SQL_COMMANDS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("SELECT", re.compile(r"\bSELECT\b", re.I)),
    ("INSERT", re.compile(r"\bINSERT\s+INTO\s+([A-Z][A-Z0-9_.]*)", re.I)),
    ("UPDATE", re.compile(r"\bUPDATE\s+([A-Z][A-Z0-9_.]*)", re.I)),
    ("DELETE", re.compile(r"\bDELETE\s+FROM\s+([A-Z][A-Z0-9_.]*)", re.I)),
    ("COMMIT", re.compile(r"^\s*(COMMIT)\b", re.I)),
    ("ROLLBACK", re.compile(r"^\s*(ROLLBACK)\b", re.I)),
)
_SQL_SELECT_FROM = re.compile(r"\bFROM\s+([A-Z][A-Z0-9_.]*)", re.I)
_PARAGRAPH = re.compile(r"^\s*((?:[A-Z][A-Z0-9-]*|[0-9]+-[A-Z][A-Z0-9-]*))\.\s*$", re.I)


def _body(line: str) -> tuple[str, bool]:
    """Return executable area and whether the record is a comment.

    Accepts fixed-format COBOL (sequence columns 1-6, indicator column 7) and
    free-format test snippets. The returned body excludes sequence/indicator
    and identification columns for fixed-format lines.
    """
    if len(line) >= 7 and line[:6].isdigit():
        indicator = line[6]
        if indicator in {"*", "/", "D", "d"}:
            return "", True
        body = line[7:72]
    else:
        body = line.rstrip()
    # Remove inline comments without truncating quoted literals that contain *>.
    quote: str | None = None
    i = 0
    while i < len(body):
        char = body[i]
        if quote:
            if char == quote:
                if i + 1 < len(body) and body[i + 1] == quote:
                    i += 2
                    continue
                quote = None
        elif char in {"'", '"'}:
            quote = char
        elif body[i:i + 2] == "*>":
            body = body[:i]
            break
        i += 1
    # Mask literals, preserving word spacing, so command-like text in values
    # cannot be interpreted as executable statements.
    chars = list(body)
    quote = None
    i = 0
    while i < len(chars):
        char = chars[i]
        if quote:
            chars[i] = " "
            if char == quote:
                if i + 1 < len(chars) and chars[i + 1] == quote:
                    chars[i + 1] = " "
                    i += 2
                    continue
                quote = None
        elif char in {"'", '"'}:
            quote = char
            chars[i] = " "
        i += 1
    return "".join(chars), False


def _resolve_source_operand(family: str, operand: str, body: str) -> str:
    """Resolve LRF logical-record operands to their named IDMS record when explicit.

    Examples: VMBTL07-R01 WHERE ALL-VMBEVEF-BY-VMBEFF and
    VMBTL03-R01 WHERE SWEEP-VMBFAS. This is lexical resolution only; unknown
    logical-record/set names remain unresolved and are reported for review.
    """
    normalized = operand.upper()
    if not normalized.startswith("VMBTL"):
        return normalized
    match = re.search(r"\bWHERE\s+(?:ALL-|ST-|MO-|SWEEP-)([A-Z][A-Z0-9-]*)", body, re.I)
    if match:
        candidate = match.group(1).upper()
        # ALL-<record>-BY-<set> captures the record before -BY; ST/MO/SWEEP
        # clauses directly name the record.
        if "-BY-" in candidate:
            candidate = candidate.split("-BY-", 1)[0]
        return candidate
    return normalized


def _read_source(source: str | Path) -> tuple[list[tuple[int, str]], list[SourceOperation]]:
    text = Path(source).read_text(encoding="utf-8", errors="replace") if isinstance(source, Path) else str(source)
    executable: list[tuple[int, str]] = []
    operations: list[SourceOperation] = []
    current_paragraph: str | None = None
    for number, raw in enumerate(text.splitlines(), 1):
        body, is_comment = _body(raw)
        if is_comment or not body.strip():
            continue
        executable.append((number, body))
        header = _PARAGRAPH.fullmatch(body)
        if header:
            current_paragraph = header.group(1).upper()
        for family, pattern in _SOURCE_COMMANDS:
            for match in pattern.finditer(body):
                transaction_boundary = family in {"COMMIT", "ROLLBACK"}
                operations.append(SourceOperation(
                    family=family,
                    line=number,
                    paragraph=current_paragraph,
                    statement=match.group(0).upper(),
                    operand=None if transaction_boundary else _resolve_source_operand(family, match.group(1), body),
                ))
    return executable, operations


def _dml_paragraph_bodies(text: str | Path) -> dict[str, tuple[int, list[str]]]:
    """Extract procedure paragraphs for loss-of-business-work checks.

    We compare only shared, unchanged names: renaming/moving a paragraph
    cannot be proven equivalent from names alone, and is audited separately.
    Do not confuse END-IF. / END-EVALUATE. with paragraph declarations.
    """
    source = Path(text).read_text(encoding="utf-8", errors="replace") if isinstance(text, Path) else str(text)
    result: dict[str, tuple[int, list[str]]] = {}
    started = False
    current = ""
    for number, raw in enumerate(source.splitlines(), 1):
        body, comment = _body(raw)
        if comment or not body.strip():
            continue
        code = body.strip()
        if re.match(r"^PROCEDURE\s+DIVISION\b", code, re.I):
            started = True
            current = ""
            continue
        if not started:
            continue
        matched = _PARAGRAPH.fullmatch(code)
        if matched and not re.match(r"^(?:END-|GOBACK|EXIT|CONTINUE)\b", matched.group(1), re.I):
            current = matched.group(1).upper()
            result.setdefault(current, (number, []))
        elif current:
            result[current][1].append(code)
    return result


_DML_OR_FILE_SIDE_EFFECT = re.compile(r"^(?:OBTAIN|MODIFY|STORE|ERASE|WRITE|REWRITE|READ|DELETE|PERFORM)\b", re.I)
_DB2_OR_FILE_SIDE_EFFECT = re.compile(r"^(?:EXEC\s+SQL|PERFORM|WRITE|REWRITE|READ|DELETE|INSERT|UPDATE|CALL|MOVE|IF|EVALUATE|ADD|SUBTRACT|COMPUTE|SET)\b", re.I)


def _target_sql_statements(target: str | Path) -> tuple[tuple[str, str | None, str], ...]:
    text = Path(target).read_text(encoding="utf-8", errors="replace") if isinstance(target, Path) else str(target)
    executable_lines: list[str] = []
    for raw in text.splitlines():
        body, is_comment = _body(raw)
        if not is_comment:
            executable_lines.append(body)
    executable = "\n".join(executable_lines)
    # Restrict parsing to embedded SQL blocks, avoiding COBOL identifiers named SELECT/UPDATE.
    blocks = re.findall(r"\bEXEC\s+SQL\b(.*?)\bEND-EXEC\b", executable, flags=re.I | re.S)
    statements: list[tuple[str, str | None, str]] = []
    for block in blocks:
        block = re.sub(r"\s+", " ", block).strip()
        for family, pattern in _SQL_COMMANDS:
            if family == "SELECT" and re.search(r"\bSELECT\b", block, re.I):
                match = _SQL_SELECT_FROM.search(block)
                if match:
                    statements.append((family, _normalize_table(match.group(1)), block))
            elif family in {"COMMIT", "ROLLBACK"}:
                if pattern.search(block):
                    statements.append((family, None, block))
            elif family != "SELECT":
                match = pattern.search(block)
                if match:
                    statements.append((family, _normalize_table(match.group(1)), block))
    return tuple(statements)


def _normalize_table(value: str) -> str:
    return value.rsplit(".", 1)[-1].strip().upper()


def _mapping_reader(handle):
    """Read text exports by content; .csv exports may use tabs or semicolons."""
    sample = handle.read(8192)
    handle.seek(0)
    try:
        delimiter = csv.Sniffer().sniff(sample, delimiters=",\t;|").delimiter
    except csv.Error:
        delimiter = "\t" if "\t" in sample.partition("\n")[0] else ","
    return csv.DictReader(handle, delimiter=delimiter)


def _mapping_tables(mapping_csv: str | Path | None, dclgen_dir: str | Path | None) -> dict[str, set[str]]:
    """Load source-record to DB2 table aliases from the field mapping and DCLGEN inventory.

    A mapped DB2 base table can have a corresponding DCLGEN view with the same stem
    and a B/V final character. That alias is accepted only when the DCLGEN member
    actually exists, so this does not invent a naming convention for absent members.
    """
    mapping: dict[str, set[str]] = {}
    if not mapping_csv:
        return mapping
    path = Path(mapping_csv)
    if not path.is_file():
        return mapping
    dclgen_stems = {p.stem.upper() for p in Path(dclgen_dir).glob("*") if p.is_file()} if dclgen_dir and Path(dclgen_dir).is_dir() else set()
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = _mapping_reader(handle)
        for row in reader:
            record = (row.get("Cobol Recrd IDMS") or "").strip().upper()
            table = (row.get("New DB2 Record ") or row.get("New DB2 Record") or "").strip().upper()
            if not record or not table or not re.fullmatch(r"[A-Z][A-Z0-9_]*", table):
                continue
            mapping.setdefault(record, set()).add(_normalize_table(table))
            if table.endswith("B"):
                view = table[:-1] + "V"
                if view in dclgen_stems:
                    mapping[record].add(view)
            elif table.endswith("V"):
                base = table[:-1] + "B"
                if base in {candidate for values in mapping.values() for candidate in values}:
                    mapping[record].add(base)
    return mapping


def _mapping_key_columns(mapping_csv: str | Path | None) -> dict[str, set[str]]:
    """Return mapped DB2 primary-key columns by original IDMS record name."""
    result: dict[str, set[str]] = {}
    if not mapping_csv or not Path(mapping_csv).is_file():
        return result
    with Path(mapping_csv).open(encoding="utf-8-sig", newline="") as handle:
        reader = _mapping_reader(handle)
        for row in reader:
            record = (row.get("Cobol Recrd IDMS") or "").strip().upper()
            key_kind = (row.get("DB2 key") or "").strip().upper()
            column = (row.get("New DB2_Field name") or "").strip().upper()
            if record and key_kind == "PRIMARY KEY" and re.fullmatch(r"[A-Z][A-Z0-9_]*", column):
                result.setdefault(record, set()).add(column)
    return result


def _mapping_record_fields(mapping_csv: str | Path | None) -> dict[str, dict[str, set[str]]]:
    """Map original IDMS record fields to DB2 columns using explicit sheet rows.

    Only rows with both an IDMS record, a concrete COBOL field name, and a DB2
    field are included. Group rows are allowed when the mapping sheet explicitly
    supplies a DB2 column; filler/redefines rows are ignored.
    """
    result: dict[str, dict[str, set[str]]] = {}
    if not mapping_csv or not Path(mapping_csv).is_file():
        return result
    with Path(mapping_csv).open(encoding="utf-8-sig", newline="") as handle:
        for row in _mapping_reader(handle):
            record = (row.get("Cobol Recrd IDMS") or "").strip().upper()
            zone = (row.get("Cobol Zone") or "").strip().upper()
            column = (row.get("New DB2_Field name") or "").strip().upper()
            if not record or not zone or not column or not re.fullmatch(r"[A-Z][A-Z0-9_]*", column):
                continue
            match = re.match(r"\s*\d{1,2}\s+([A-Z][A-Z0-9-]*)", zone)
            if not match:
                continue
            field = match.group(1)
            if field == "FILLER" or " REDEFINES " in zone:
                continue
            result.setdefault(record, {}).setdefault(field, set()).add(column)
    return result


def _source_modified_fields(
    source: str | Path, operation: SourceOperation, mapped_field_names: set[str] | None = None
) -> set[str]:
    """Find explicit field writes to the modified record before a MODIFY.

    Conservative scope: same paragraph, since the previous IDMS DML operation,
    and only explicit MOVE ... TO field OF record statements. This avoids
    guessing about group moves, COPY-expanded fields, and writes in other paths.
    """
    if operation.family != "UPDATE" or not operation.operand:
        return set()
    # LRF logical-record operations may prepare helper fields rather than direct
    # fields on the physical record; their mutation semantics need LRF metadata.
    if re.search(r"\bVMBTL[0-9A-Z-]*\b", operation.statement, re.I):
        return set()
    mapped_field_names = {name.upper() for name in (mapped_field_names or set())}
    text = Path(source).read_text(encoding="utf-8", errors="replace") if isinstance(source, Path) else str(source)
    lines = text.splitlines()
    start = 0
    # Locate the current operation and restrict the scan to its paragraph and
    # statements following the prior DML statement in that paragraph.
    paragraph = operation.paragraph
    for index, raw in enumerate(lines[:operation.line - 1]):
        body, comment = _body(raw)
        if comment or not body.strip():
            continue
        header = _PARAGRAPH.fullmatch(body)
        if header and header.group(1).upper() == paragraph:
            start = index + 1
        elif header and paragraph and index >= start:
            start = index + 1
    # Narrow to after the last DML operation in the same paragraph.
    for index in range(start, min(operation.line - 1, len(lines))):
        body, comment = _body(lines[index])
        if comment or not body.strip():
            continue
        if re.search(r"\b(?:OBTAIN|MODIFY|STORE|ERASE)\b", body, re.I):
            start = index + 1
    fields: set[str] = set()
    record = re.escape(operation.operand.upper())
    move_re = re.compile(
        rf"\bMOVE\b.*?\bTO\s+([A-Z][A-Z0-9-]*)(?:\s+OF\s+({record}))?\b", re.I
    )
    for raw in lines[start:operation.line - 1]:
        body, comment = _body(raw)
        if comment or not body.strip():
            continue
        if _PARAGRAPH.fullmatch(body):
            continue
        match = move_re.search(body)
        if match:
            field = match.group(1).upper()
            explicit_record = match.group(2)
            # A qualified field is attributable to this record even when its
            # mapping is absent (it can be reported for review). An unqualified
            # field is only attributable when the mapping sheet confirms it.
            if explicit_record or field in mapped_field_names:
                fields.add(field)
    return fields


def _update_set_columns(sql: str) -> set[str]:
    """Extract left-hand columns from an UPDATE SET clause."""
    match = re.search(r"\bSET\b(.*?)(?:\bWHERE\b|$)", sql, re.I | re.S)
    if not match:
        return set()
    return {name.upper() for name in re.findall(r"(?:^|,)\s*([A-Z][A-Z0-9_]*)\s*=", match.group(1), re.I)}



def _select_projection_columns(sql: str) -> set[str] | None:
    """Return concrete DB2 columns projected by a SELECT, or None for wildcard.

    This is deliberately a small lexical parser for generated SQL: it handles
    comma-separated identifiers and qualified identifiers, and treats wildcard
    projections as covering all mapped fields. Expressions that cannot be mapped
    to a concrete column are not guessed.
    """
    match = re.search(r"\bSELECT\s+(.*?)\s+FROM\b", sql, re.I | re.S)
    if not match:
        return set()
    projection = match.group(1).strip()
    # Embedded DB2 SELECT INTO places host variables before FROM; they are not
    # projection expressions and must be removed before splitting columns.
    projection = re.sub(r"\bINTO\b.*$", "", projection, flags=re.I).strip()
    if re.search(r"(?:^|,)\s*(?:[A-Z][A-Z0-9_.]*\.)?\*\s*(?:,|$)", projection, re.I):
        return None
    columns: set[str] = set()
    for expression in projection.split(","):
        expression = re.sub(r"\s+AS\s+[A-Z][A-Z0-9_]*\s*$", "", expression, flags=re.I).strip()
        # A bare/qualified identifier is provable. Avoid treating functions or
        # arithmetic expressions as source-column projections.
        if re.fullmatch(r"[A-Z][A-Z0-9_]*(?:\.[A-Z][A-Z0-9_]*)?", expression, re.I):
            columns.add(expression.rsplit(".", 1)[-1].upper())
    return columns


def _source_fields_read_after_obtain(
    source: str | Path, operation: SourceOperation
) -> set[str]:
    """Find record fields read after OBTAIN and before the next DML/paragraph.

    Only explicit ``FIELD OF RECORD`` references are considered. Destination
    references in common COBOL writes (MOVE/ADD/SUBTRACT/COMPUTE) are excluded,
    so a field merely being populated before MODIFY is not mistaken for a fetched
    value consumed from the OBTAIN. Ambiguous syntax is left to broader review.
    """
    if operation.family != "SELECT" or not operation.operand:
        return set()
    text = Path(source).read_text(encoding="utf-8", errors="replace") if isinstance(source, Path) else str(source)
    lines = text.splitlines()
    record = re.escape(operation.operand.upper())
    field_ref = re.compile(rf"\b([A-Z][A-Z0-9-]*)\s+(?:OF|IN)\s+{record}\b", re.I)
    result: set[str] = set()
    for raw in lines[operation.line:]:
        body, comment = _body(raw)
        if comment or not body.strip():
            continue
        if _PARAGRAPH.fullmatch(body):
            break
        if re.search(r"\b(?:OBTAIN|MODIFY|STORE|ERASE)\b", body, re.I):
            break
        for match in field_ref.finditer(body):
            prefix = body[:match.start()]
            # The matched field is a destination when it follows TO/GIVING in a
            # write statement; do not require it to be fetched by SELECT.
            if re.search(r"\b(?:MOVE|ADD|SUBTRACT|COMPUTE|MULTIPLY|DIVIDE|INITIALIZE|SET)\b.*\b(?:TO|GIVING)\s*$", prefix, re.I):
                continue
            result.add(match.group(1).upper())
    return result

def _target_sql_blocks_with_following_context(
    target: str | Path,
) -> tuple[tuple[str, str | None, str, str], ...]:
    """Return SQL blocks with nearby executable COBOL context after END-EXEC.

    Context stops at the next embedded SQL block or paragraph header. This lets
    condition audits correlate SQLCODE handling with the operation it follows,
    instead of accepting an unrelated WHEN 100 elsewhere in the program.
    """
    text = Path(target).read_text(encoding="utf-8", errors="replace") if isinstance(target, Path) else str(target)
    lines: list[str] = []
    for raw in text.splitlines():
        body, is_comment = _body(raw)
        if not is_comment:
            lines.append(body)
    executable = "\n".join(lines)
    blocks = list(re.finditer(r"\bEXEC\s+SQL\b(.*?)\bEND-EXEC\b", executable, flags=re.I | re.S))
    result: list[tuple[str, str | None, str, str]] = []
    for index, match in enumerate(blocks):
        block = re.sub(r"\s+", " ", match.group(1)).strip()
        family = None
        table = None
        for candidate, pattern in _SQL_COMMANDS:
            if candidate == "SELECT" and re.search(r"\bSELECT\b", block, re.I):
                table_match = _SQL_SELECT_FROM.search(block)
                if table_match:
                    family, table = candidate, _normalize_table(table_match.group(1))
                    break
            elif candidate in {"COMMIT", "ROLLBACK"} and pattern.search(block):
                family = candidate
                break
            elif candidate not in {"SELECT", "COMMIT", "ROLLBACK"}:
                table_match = pattern.search(block)
                if table_match:
                    family, table = candidate, _normalize_table(table_match.group(1))
                    break
        context_end = blocks[index + 1].start() if index + 1 < len(blocks) else len(executable)
        context = executable[match.end():context_end]
        # Do not let a later paragraph's branch satisfy this SQL operation.
        context_lines = context.splitlines()
        for line_index, context_line in enumerate(context_lines):
            if _PARAGRAPH.fullmatch(context_line):
                context_lines = context_lines[:line_index]
                break
        context = "\n".join(context_lines)
        result.append((family or "", table, block, context))
    return tuple(result)


def _target_sql_families(target: str | Path) -> tuple[str, ...]:
    families = {family for family, _table, _sql in _target_sql_statements(target)}
    return tuple(family for family in ("SELECT", "INSERT", "UPDATE", "DELETE", "COMMIT", "ROLLBACK") if family in families)


class BusinessOperationParityAuditor:
    """Audit source DML family coverage and per-operation DB2 table linkage."""

    def __init__(self, mapping_csv: str | Path | None = None, dclgen_dir: str | Path | None = None):
        self.mapping_tables = _mapping_tables(mapping_csv, dclgen_dir)
        self.mapping_key_columns = _mapping_key_columns(mapping_csv)
        self.mapping_record_fields = _mapping_record_fields(mapping_csv)

    def audit(self, source: str | Path, target: str | Path) -> BusinessOperationParityReport:
        _source_lines, operations = _read_source(source)
        target_statements = _target_sql_statements(target)
        target_families = tuple(family for family in ("SELECT", "INSERT", "UPDATE", "DELETE", "COMMIT", "ROLLBACK")
                                if any(sql_family == family for sql_family, _table, _sql in target_statements))
        target_set = set(target_families)
        source_families = {operation.family for operation in operations}
        issues: list[OperationParityIssue] = []
        reviews: list[OperationParityReview] = []
        # Physical COBOL file writes are non-SQL business side effects.
        # SQL-family coverage alone missed a real erased WRITE ... FROM when
        # the preceding period-free MOVE swallowed that statement. Do not
        # equate SQL SELECT parity with preservation of an output file.
        source_writes = [
            (number, match.group(1).upper())
            for number, body in _source_lines
            if (match := re.match(r"^\s*WRITE\s+([A-Z][A-Z0-9-]*)\b", body, re.I))
        ]
        target_text = Path(target).read_text(encoding="utf-8", errors="replace") if isinstance(target, Path) else str(target)
        target_write_records = {
            match.group(1).upper()
            for raw in target_text.splitlines()
            if (body := _body(raw)[0]).strip()
            if (match := re.match(r"^\s*WRITE\s+([A-Z][A-Z0-9-]*)\b", body, re.I))
        }
        for number, record_name in source_writes:
            if record_name not in target_write_records:
                issues.append(OperationParityIssue(
                    code="SOURCE_FILE_WRITE_MISSING",
                    family="COBOL_WRITE",
                    line=number,
                    message=(f"source WRITE {record_name} has no corresponding physical file WRITE "
                             "in converted output; output-file business side effect may have been lost"),
                ))

        original_paragraphs = _dml_paragraph_bodies(source)
        generated_paragraphs = _dml_paragraph_bodies(target)
        for name, (number, source_body) in original_paragraphs.items():
            if name not in generated_paragraphs:
                continue  # A renamed paragraph needs call-graph verification.
            if not any(_DML_OR_FILE_SIDE_EFFECT.match(line) for line in source_body):
                continue
            _target_line, generated_body = generated_paragraphs[name]
            if any(_DB2_OR_FILE_SIDE_EFFECT.match(line) for line in generated_body):
                continue
            issues.append(OperationParityIssue(
                code="SOURCE_BUSINESS_PARAGRAPH_EMPTIED",
                family="CONTROL_FLOW",
                line=number,
                message=(f"original paragraph {name} performed database/file I/O or "
                         "called business work; generated same-name paragraph has no "
                         "executable business work beyond diagnostics. Verify relocation or restore the "
                         "semantic transformation upstream."),
            ))

        for family in sorted(source_families - target_set):
            family_operations = [operation for operation in operations if operation.family == family]
            # An OBTAIN CALC immediately paired with a same-record MODIFY may be
            # represented as a direct keyed UPDATE. That is not automatic PASS: the
            # per-operation audit below emits REVIEW for not-found/fetched-value parity.
            # Avoid adding a contradictory family-level FAIL when every missing SELECT
            # has this explicit, reviewable replacement pattern.
            direct_update_review_only = (
                family == "SELECT"
                and bool(family_operations)
                and all(
                    operation.statement.startswith("OBTAIN CALC")
                    and bool(operation.operand)
                    and any(other.family == "UPDATE" and other.operand == operation.operand
                            for other in operations)
                    and bool(self.mapping_tables.get(operation.operand, set()))
                    and any(sql_family == "UPDATE" and table in self.mapping_tables[operation.operand]
                            for sql_family, table, _sql in target_statements)
                    for operation in family_operations
                )
            )
            if direct_update_review_only:
                continue
            first = family_operations[0]
            issues.append(OperationParityIssue(
                code="SOURCE_OPERATION_WITHOUT_TARGET_SQL",
                family=family,
                line=first.line,
                message=(f"source contains {family} operation(s), but converted output has no "
                         f"corresponding DB2 {family} statement; first occurrence: "
                         f"{first.statement} in paragraph {first.paragraph or '<unknown>'}"),
            ))

        # Check every source operation where the source operand maps unambiguously
        # to a DB2 table. Set-name/LRF operations remain explicit review items until
        # relationship metadata resolves the accessed record.
        for operation in operations:
            if operation.operand is None:
                continue
            expected_tables = self.mapping_tables.get(operation.operand, set())
            if not expected_tables:
                reviews.append(OperationParityReview(
                    family=operation.family, line=operation.line, operand=operation.operand,
                    message=(f"No unambiguous IDMS-record to DB2-table mapping for operand "
                             f"{operation.operand}; resolve via schema/set/LRF metadata."),
                ))
                continue
            matched = [(table, sql) for family, table, sql in target_statements
                       if family == operation.family and table in expected_tables]
            if not matched and operation.family == "SELECT" and operation.statement.startswith("OBTAIN CALC"):
                # Some safe keyed read/update patterns are converted to a direct
                # UPDATE by key. Do not claim semantic equivalence; surface it for review.
                update_match = [(table, sql) for family, table, sql in target_statements
                                if family == "UPDATE" and table in expected_tables]
                if update_match and any(op.family == "UPDATE" and op.operand == operation.operand for op in operations):
                    reviews.append(OperationParityReview(
                        family=operation.family, line=operation.line, operand=operation.operand,
                        message=(f"OBTAIN CALC {operation.operand} has no SELECT on mapped table, "
                                 f"but a same-record MODIFY maps to direct UPDATE; verify no fetched "
                                 f"record values and not-found behavior are lost. A DB2 UPDATE that "
                                 f"matches zero rows can still return SQLCODE 0; inspect SQLERRD(3) "
                                 f"or GET DIAGNOSTICS if the source requires missing-record detection."),
                    ))
                    continue
            if not matched:
                issues.append(OperationParityIssue(
                    code="SOURCE_OPERATION_TABLE_NOT_FOUND_IN_TARGET_SQL",
                    family=operation.family,
                    line=operation.line,
                    message=(f"{operation.statement} in paragraph {operation.paragraph or '<unknown>'} "
                             f"maps to DB2 table(s) {', '.join(sorted(expected_tables))}, but no "
                             f"target {operation.family} statement references those tables."),
                ))
                continue
            if operation.family in {"UPDATE", "DELETE"}:
                expected_keys = self.mapping_key_columns.get(operation.operand or "", set())
                if expected_keys:
                    # Every mapped key must participate in the WHERE clause. Check
                    # identifiers, not substrings, to avoid suffix/prefix collisions.
                    for table, sql in matched:
                        where = re.split(r"\bWHERE\b", sql, maxsplit=1, flags=re.I)
                        where_text = where[1] if len(where) == 2 else ""
                        where_columns = {token.upper() for token in re.findall(r"\b[A-Z][A-Z0-9_]*\b", where_text)}
                        missing_keys = sorted(expected_keys - where_columns)
                        if missing_keys:
                            issues.append(OperationParityIssue(
                                code="TARGET_KEY_PREDICATE_MISSING_MAPPED_KEY",
                                family=operation.family,
                                line=operation.line,
                                message=(f"{operation.statement} maps to {table}, but target {operation.family} "
                                         f"WHERE clause does not reference mapped primary-key column(s): "
                                         f"{', '.join(missing_keys)}."),
                            ))
        # A source OBTAIN CALC followed by MODIFY can be emitted as a direct
        # keyed UPDATE. DB2 reports SQLCODE 0 when the statement executes
        # successfully even if zero rows matched, so require an operation-local
        # affected-row check before treating this as equivalent. This audit only
        # flags missing evidence; it does not invent source not-found behavior.
        for index, operation in enumerate(operations[:-1]):
            if operation.family != "SELECT" or not operation.statement.startswith("OBTAIN CALC"):
                continue
            following = operations[index + 1]
            if following.family != "UPDATE" or following.operand != operation.operand:
                continue
            if operation.paragraph != following.paragraph:
                continue
            expected_tables = self.mapping_tables.get(operation.operand or "", set())
            direct_updates = [
                (table, sql, context)
                for family, table, sql, context in _target_sql_blocks_with_following_context(target)
                if family == "UPDATE" and table in expected_tables
            ]
            if not direct_updates:
                continue
            # A row-count mention is not a guard: ADD SQLERRD(3) TO a
            # counter does not detect a successful UPDATE that matched zero
            # rows. Require an actual zero/positive comparison in executable
            # control flow. Keep GET DIAGNOSTICS support, but likewise require
            # its ROW_COUNT value to be tested rather than merely assigned.
            row_count_guard = re.compile(
                r"(?:\bSQLERRD\s*\(\s*3\s*\)\s*"
                r"(?:=|EQUAL\s+TO|<|LESS\s+THAN)\s*0\b|"
                r"\bSQLERRD\s*\(\s*3\s*\)\s*"
                r"(?:NOT\s+GREATER\s+THAN|<=)\s*0\b|"
                r"\b(?:IF|WHEN|UNTIL)\b[^.]{0,180}"
                r"\bROW_COUNT\b\s*(?:=|<|<=)\s*0\b|"
                r"\b(?:IF|WHEN|UNTIL)\b[^.]{0,180}"
                r"\bROW_COUNT\b\s*(?:NOT\s+GREATER\s+THAN)\s*0\b)",
                re.I,
            )
            if not any(row_count_guard.search(context) for _table, _sql, context in direct_updates):
                reviews.append(OperationParityReview(
                    family="UPDATE", line=following.line, operand=following.operand,
                    message=(f"OBTAIN CALC {operation.operand} followed by MODIFY is represented by "
                             "a direct keyed DB2 UPDATE, but no operation-local affected-row check "
                             "(SQLERRD(3) or GET DIAGNOSTICS ROW_COUNT) was detected. SQLCODE 0 "
                             "does not prove that a row matched. Confirm the original IDMS not-found "
                             "semantics before adding a zero-row branch."),
                ))

        # Conditional not-found parity: IDMS ON DB-REC-NOT-FOUND branches must
        # have a plausible SQLCODE +100 path in the target. This is deliberately
        # a review, not a PASS/FAIL proof, because the branch must be correlated
        # to the corresponding SQL statement and its paragraph manually.
        source_text = (Path(source).read_text(encoding="utf-8", errors="replace")
                       if isinstance(source, Path) else str(source))
        target_text = (Path(target).read_text(encoding="utf-8", errors="replace")
                       if isinstance(target, Path) else str(target))
        target_sql_contexts = _target_sql_blocks_with_following_context(target)
        source_selects = [operation for operation in operations if operation.family == "SELECT"]
        for line_number, raw in enumerate(source_text.splitlines(), 1):
            body, is_comment = _body(raw)
            if is_comment or not re.search(r"\bON\s+DB-REC-NOT-FOUND\b", body, re.I):
                continue
            # Associate the handler with the nearest preceding OBTAIN in the
            # current paragraph. If no mapping is available, do not accept a
            # program-wide SQLCODE 100 as proof of equivalence.
            source_operation = next(
                (operation for operation in reversed(source_selects)
                 if operation.line <= line_number
                 and (line_number - operation.line) <= 8),
                None,
            )
            expected_tables = self.mapping_tables.get(source_operation.operand or "", set()) if source_operation else set()
            correlated = [
                (family, table, sql, context)
                for family, table, sql, context in target_sql_contexts
                if family == "SELECT" and table in expected_tables
            ]
            local_not_found_branch = any(re.search(
                r"\b(?:WHEN\s+\+?100\b|SQLCODE\s*(?:=|IS)\s*\+?100\b)",
                context, re.I
            ) for _family, _table, _sql, context in correlated)
            if not local_not_found_branch:
                source_operand = source_operation.operand if source_operation else None
                reason = (
                    f"no mapped SELECT-local SQLCODE +100/WHEN 100 branch was detected for "
                    f"{source_operand}"
                    if expected_tables else
                    "the source operation could not be correlated to a mapped target SELECT"
                )
                reviews.append(OperationParityReview(
                    family="SELECT", line=line_number, operand=source_operand,
                    message=(f"Source contains ON DB-REC-NOT-FOUND, but {reason}. "
                             "A not-found branch elsewhere in the program does not establish "
                             "equivalence; verify the branch following the corresponding SQL."),
                ))

        # Field-level UPDATE parity: every explicitly moved field on the IDMS
        # record immediately before MODIFY must be represented in SET when the
        # mapping sheet supplies a concrete DB2 column. Extra audit fields such
        # as update timestamp/user are allowed.
        for operation in operations:
            if operation.family != "UPDATE" or not operation.operand:
                continue
            record_map = self.mapping_record_fields.get(operation.operand, {})
            changed_fields = _source_modified_fields(source, operation, set(record_map))
            if not changed_fields:
                continue
            expected_columns: set[str] = set()
            unmapped_fields: set[str] = set()
            for field in changed_fields:
                mapped = record_map.get(field, set())
                if mapped:
                    expected_columns.update(mapped)
                else:
                    unmapped_fields.add(field)
            if unmapped_fields:
                reviews.append(OperationParityReview(
                    family="UPDATE", line=operation.line, operand=operation.operand,
                    message=("Explicitly changed source field(s) lack a concrete DB2 field mapping: "
                             + ", ".join(sorted(unmapped_fields)) + "."),
                ))
            mapped_tables = self.mapping_tables.get(operation.operand, set())
            update_sqls = [sql for family, table, sql in target_statements
                           if family == "UPDATE" and table in mapped_tables]
            if not expected_columns or not update_sqls:
                continue
            represented = set().union(*(_update_set_columns(sql) for sql in update_sqls))
            missing_columns = sorted(expected_columns - represented)
            if missing_columns:
                issues.append(OperationParityIssue(
                    code="TARGET_UPDATE_SET_MISSING_SOURCE_FIELD",
                    family="UPDATE", line=operation.line,
                    message=(f"MODIFY {operation.operand} explicitly changes mapped field(s), "
                             "but the DB2 UPDATE SET clause does not include: "
                             + ", ".join(missing_columns) + "."),
                ))

        # SELECT projection parity: when source code consumes fields from a record
        # after OBTAIN, the target SELECT on that mapped table must project those
        # fields. A direct keyed UPDATE can be valid when no fetched values are
        # consumed; it is not valid as a substitute for a read whose values drive
        # later business logic.
        for operation in operations:
            if operation.family != "SELECT" or not operation.operand:
                continue
            record_map = self.mapping_record_fields.get(operation.operand, {})
            read_fields = _source_fields_read_after_obtain(source, operation)
            if not read_fields:
                continue
            expected_columns: set[str] = set()
            unmapped_fields: set[str] = set()
            for field in read_fields:
                mapped = record_map.get(field, set())
                if mapped:
                    expected_columns.update(mapped)
                else:
                    unmapped_fields.add(field)
            if unmapped_fields:
                reviews.append(OperationParityReview(
                    family="SELECT", line=operation.line, operand=operation.operand,
                    message=("Source reads record field(s) after OBTAIN that have no concrete DB2 mapping: "
                             + ", ".join(sorted(unmapped_fields)) + "."),
                ))
            expected_tables = self.mapping_tables.get(operation.operand, set())
            select_matches = [(table, sql) for family, table, sql in target_statements
                              if family == "SELECT" and table in expected_tables]
            if not expected_columns:
                continue
            if not select_matches:
                issues.append(OperationParityIssue(
                    code="TARGET_SELECT_MISSING_DOWNSTREAM_FIELD_READ",
                    family="SELECT", line=operation.line,
                    message=(f"OBTAIN {operation.operand} is followed by reads of mapped field(s) "
                             f"{', '.join(sorted(expected_columns))}, but no DB2 SELECT projects them "
                             "from the mapped table; a direct UPDATE is not sufficient."),
                ))
                continue
            missing_by_sql: list[set[str]] = []
            for _table, sql in select_matches:
                projection = _select_projection_columns(sql)
                if projection is None:
                    missing_by_sql.append(set())
                else:
                    missing_by_sql.append(expected_columns - projection)
            missing_columns = set.intersection(*missing_by_sql) if missing_by_sql else expected_columns
            if missing_columns:
                issues.append(OperationParityIssue(
                    code="TARGET_SELECT_PROJECTION_MISSING_SOURCE_FIELD",
                    family="SELECT", line=operation.line,
                    message=(f"OBTAIN {operation.operand} is followed by reads requiring DB2 column(s) "
                             f"{', '.join(sorted(expected_columns))}, but mapped SELECT projections omit: "
                             + ", ".join(sorted(missing_columns)) + "."),
                ))

        return BusinessOperationParityReport(
            source_path=str(source) if isinstance(source, Path) else "<source-text>",
            target_path=str(target) if isinstance(target, Path) else "<target-text>",
            source_operations=tuple(operations),
            target_sql_families=target_families,
            issues=tuple(issues),
            reviews=tuple(reviews),
        )

