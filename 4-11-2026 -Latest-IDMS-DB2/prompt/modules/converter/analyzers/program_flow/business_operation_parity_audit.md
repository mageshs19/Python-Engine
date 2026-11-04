# `converter/analyzers/program_flow/business_operation_parity_audit.py`

Source: [converter/analyzers/program_flow/business_operation_parity_audit.py](../../../../../converter/analyzers/program_flow/business_operation_parity_audit.py) | 874 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `c919a68de1fa337d888f2b9b55599305d17f6e946d9082a016093f2c39114878`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Conservative source-to-target audit for IDMS DML operation coverage.

## Module-level bindings

`_SOURCE_COMMANDS` (L57), `_SQL_COMMANDS` (L66), `_SQL_SELECT_FROM` (L74), `_PARAGRAPH` (L75), `_DML_OR_FILE_SIDE_EFFECT` (L209), `_DB2_OR_FILE_SIDE_EFFECT` (L210)

## Import declarations

```python
from __future__ import annotations
import csv
import re
from dataclasses import dataclass
from pathlib import Path
```

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/verification/manual_direct_update_parity.py](../../../mainframe/verification/manual_direct_update_parity.md)
- [mainframe/zowe_semantic_release_gate.py](../../../mainframe/zowe_semantic_release_gate.md)
- [runners/audit_business_operation_parity.py](../../../runners/audit_business_operation_parity.md)
- [tests/test_business_operation_parity_audit.py](../../../tests/test_business_operation_parity_audit.md)
- [tests/test_manual_direct_update_parity.py](../../../tests/test_manual_direct_update_parity.md)

## Symbol contracts and control points

### `SourceOperation` - L16-L21

```python
class SourceOperation()
```

Declared class/data-model fields:

```python
family: str
line: int
paragraph: str | None
statement: str
operand: str | None = None
```

### `OperationParityIssue` - L25-L29

```python
class OperationParityIssue()
```

Declared class/data-model fields:

```python
code: str
family: str
line: int
message: str
```

### `OperationParityReview` - L33-L37

```python
class OperationParityReview()
```

Declared class/data-model fields:

```python
family: str
line: int
operand: str | None
message: str
```

### `BusinessOperationParityReport` - L41-L51

```python
class BusinessOperationParityReport()
```

Declared class/data-model fields:

```python
source_path: str
target_path: str
source_operations: tuple[SourceOperation, ...]
target_sql_families: tuple[str, ...]
issues: tuple[OperationParityIssue, ...]
reviews: tuple[OperationParityReview, ...] = ()
```

### `BusinessOperationParityReport.passed` - L50-L51

```python
passed(self) -> bool
```

### `_body` - L78-L128

```python
_body(line: str) -> tuple[str, bool]
```

Return executable area and whether the record is a comment.

Observed calls (lexical order): `len`, `line[:6].isdigit`, `line.rstrip`, `list`, `''.join`.

Control points:

- L85: `if len(line) >= 7 and line[:6].isdigit()`
- L87: `if indicator in {'*', '/', 'D', 'd'}`
- L95: `while i < len(body)`
- L97: `if quote`
- L98: `if char == quote`
- L99: `if i + 1 < len(body) and body[i + 1] == quote`
- L103: `if char in {"'", '"'}`
- L105: `if body[i:i + 2] == '*>'`
- Another 5 conditions/loops exist in this source span.

### `_resolve_source_operand` - L131-L149

```python
_resolve_source_operand(family: str, operand: str, body: str) -> str
```

Resolve LRF logical-record operands to their named IDMS record when explicit.

Observed calls (lexical order): `operand.upper`, `normalized.startswith`, `re.search`, `match.group`, `match.group(1).upper`, `candidate.split`.

Control points:

- L139: `if not normalized.startswith('VMBTL')`
- L142: `if match`
- L146: `if '-BY-' in candidate`

### `_read_source` - L152-L175

```python
_read_source(source: str | Path) -> tuple[list[tuple[int, str]], list[SourceOperation]]
```

Observed calls (lexical order): `Path`, `Path(source).read_text`, `isinstance`, `str`, `enumerate`, `text.splitlines`, `_body`, `body.strip`, `executable.append`, `_PARAGRAPH.fullmatch`, `header.group`, `header.group(1).upper`, `pattern.finditer`, `SourceOperation`, `operations.append`, `match.group`.
Another 2 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L157: `for (number, raw) in enumerate(text.splitlines(), 1)`
- L159: `if is_comment or not body.strip()`
- L163: `if header`
- L165: `for (family, pattern) in _SOURCE_COMMANDS`
- L166: `for match in pattern.finditer(body)`

### `_dml_paragraph_bodies` - L178-L206

```python
_dml_paragraph_bodies(text: str | Path) -> dict[str, tuple[int, list[str]]]
```

Extract procedure paragraphs for loss-of-business-work checks.

Observed calls (lexical order): `Path`, `Path(text).read_text`, `isinstance`, `str`, `enumerate`, `source.splitlines`, `_body`, `body.strip`, `re.match`, `_PARAGRAPH.fullmatch`, `matched.group`, `matched.group(1).upper`, `result.setdefault`, `result[current][1].append`.

Control points:

- L189: `for (number, raw) in enumerate(source.splitlines(), 1)`
- L191: `if comment or not body.strip()`
- L194: `if re.match('^PROCEDURE\\s+DIVISION\\b', code, re.I)`
- L198: `if not started`
- L201: `if matched and (not re.match('^(?:END-|GOBACK|EXIT|CONTINUE)\\b', matched.group(1), re.I))`
- L204: `if current`

### `_target_sql_statements` - L213-L238

```python
_target_sql_statements(target: str | Path) -> tuple[tuple[str, str | None, str], ...]
```

Observed calls (lexical order): `Path`, `Path(target).read_text`, `isinstance`, `str`, `text.splitlines`, `_body`, `executable_lines.append`, `'\n'.join`, `re.findall`, `re.sub`, `re.sub('\\s+', ' ', block).strip`, `re.search`, `_SQL_SELECT_FROM.search`, `_normalize_table`, `match.group`, `statements.append`.
Another 2 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L216: `for raw in text.splitlines()`
- L218: `if not is_comment`
- L224: `for block in blocks`
- L226: `for (family, pattern) in _SQL_COMMANDS`
- L227: `if family == 'SELECT' and re.search('\\bSELECT\\b', block, re.I)`
- L229: `if match`
- L231: `if family in {'COMMIT', 'ROLLBACK'}`
- L232: `if pattern.search(block)`
- Another 2 conditions/loops exist in this source span.

### `_normalize_table` - L241-L242

```python
_normalize_table(value: str) -> str
```

Observed calls (lexical order): `value.rsplit`, `value.rsplit('.', 1)[-1].strip`, `value.rsplit('.', 1)[-1].strip().upper`.

### `_mapping_reader` - L245-L253

```python
_mapping_reader(handle)
```

Read text exports by content; .csv exports may use tabs or semicolons.

Observed calls (lexical order): `handle.read`, `handle.seek`, `csv.Sniffer`, `csv.Sniffer().sniff`, `sample.partition`, `csv.DictReader`.

### `_mapping_tables` - L256-L286

```python
_mapping_tables(mapping_csv: str | Path | None, dclgen_dir: str | Path | None) -> dict[str, set[str]]
```

Load source-record to DB2 table aliases from the field mapping and DCLGEN inventory.

Observed calls (lexical order): `Path`, `path.is_file`, `Path(dclgen_dir).glob`, `Path(dclgen_dir).is_dir`, `p.is_file`, `p.stem.upper`, `set`, `path.open`, `_mapping_reader`, `(row.get('Cobol Recrd IDMS') or '').strip`, `(row.get('Cobol Recrd IDMS') or '').strip().upper`, `row.get`, `(row.get('New DB2 Record ') or row.get('New DB2 Record') or '').strip`, `(row.get('New DB2 Record ') or row.get('New DB2 Record') or '').strip().upper`, `re.fullmatch`, `_normalize_table`.
Another 5 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L264: `if not mapping_csv`
- L267: `if not path.is_file()`
- L272: `for row in reader`
- L275: `if not record or not table or (not re.fullmatch('[A-Z][A-Z0-9_]*', table))`
- L278: `if table.endswith('B')`
- L280: `if view in dclgen_stems`
- L282: `if table.endswith('V')`
- L284: `if base in {candidate for values in mapping.values() for candidate in values}`

### `_mapping_key_columns` - L289-L302

```python
_mapping_key_columns(mapping_csv: str | Path | None) -> dict[str, set[str]]
```

Return mapped DB2 primary-key columns by original IDMS record name.

Observed calls (lexical order): `Path`, `Path(mapping_csv).is_file`, `Path(mapping_csv).open`, `_mapping_reader`, `(row.get('Cobol Recrd IDMS') or '').strip`, `(row.get('Cobol Recrd IDMS') or '').strip().upper`, `row.get`, `(row.get('DB2 key') or '').strip`, `(row.get('DB2 key') or '').strip().upper`, `(row.get('New DB2_Field name') or '').strip`, `(row.get('New DB2_Field name') or '').strip().upper`, `re.fullmatch`, `result.setdefault`, `result.setdefault(record, set()).add`, `set`.

Control points:

- L292: `if not mapping_csv or not Path(mapping_csv).is_file()`
- L296: `for row in reader`
- L300: `if record and key_kind == 'PRIMARY KEY' and re.fullmatch('[A-Z][A-Z0-9_]*', column)`

### `_mapping_record_fields` - L305-L329

```python
_mapping_record_fields(mapping_csv: str | Path | None) -> dict[str, dict[str, set[str]]]
```

Map original IDMS record fields to DB2 columns using explicit sheet rows.

Observed calls (lexical order): `Path`, `Path(mapping_csv).is_file`, `Path(mapping_csv).open`, `_mapping_reader`, `(row.get('Cobol Recrd IDMS') or '').strip`, `(row.get('Cobol Recrd IDMS') or '').strip().upper`, `row.get`, `(row.get('Cobol Zone') or '').strip`, `(row.get('Cobol Zone') or '').strip().upper`, `(row.get('New DB2_Field name') or '').strip`, `(row.get('New DB2_Field name') or '').strip().upper`, `re.fullmatch`, `re.match`, `match.group`, `result.setdefault`, `result.setdefault(record, {}).setdefault`.
Another 2 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L313: `if not mapping_csv or not Path(mapping_csv).is_file()`
- L316: `for row in _mapping_reader(handle)`
- L320: `if not record or not zone or (not column) or (not re.fullmatch('[A-Z][A-Z0-9_]*', column))`
- L323: `if not match`
- L326: `if field == 'FILLER' or ' REDEFINES ' in zone`

### `_source_modified_fields` - L332-L390

```python
_source_modified_fields(source: str | Path, operation: SourceOperation, mapped_field_names: set[str] | None=None) -> set[str]
```

Find explicit field writes to the modified record before a MODIFY.

Observed calls (lexical order): `set`, `re.search`, `name.upper`, `Path`, `Path(source).read_text`, `isinstance`, `str`, `text.splitlines`, `enumerate`, `_body`, `body.strip`, `_PARAGRAPH.fullmatch`, `header.group`, `header.group(1).upper`, `len`, `min`.
Another 8 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L341: `if operation.family != 'UPDATE' or not operation.operand`
- L345: `if re.search('\\bVMBTL[0-9A-Z-]*\\b', operation.statement, re.I)`
- L354: `for (index, raw) in enumerate(lines[:operation.line - 1])`
- L356: `if comment or not body.strip()`
- L359: `if header and header.group(1).upper() == paragraph`
- L361: `if header and paragraph and (index >= start)`
- L364: `for index in range(start, min(operation.line - 1, len(lines)))`
- L366: `if comment or not body.strip()`
- Another 6 conditions/loops exist in this source span.

### `_update_set_columns` - L393-L398

```python
_update_set_columns(sql: str) -> set[str]
```

Extract left-hand columns from an UPDATE SET clause.

Observed calls (lexical order): `re.search`, `set`, `match.group`, `name.upper`, `re.findall`.

Control points:

- L396: `if not match`

### `_select_projection_columns` - L402-L426

```python
_select_projection_columns(sql: str) -> set[str] | None
```

Return concrete DB2 columns projected by a SELECT, or None for wildcard.

Observed calls (lexical order): `re.search`, `set`, `match.group`, `match.group(1).strip`, `re.sub`, `re.sub('\\bINTO\\b.*$', '', projection, flags=re.I).strip`, `projection.split`, `re.sub('\\s+AS\\s+[A-Z][A-Z0-9_]*\\s*$', '', expression, flags=re.I).strip`, `re.fullmatch`, `columns.add`, `expression.rsplit`, `expression.rsplit('.', 1)[-1].upper`.

Control points:

- L411: `if not match`
- L417: `if re.search('(?:^|,)\\s*(?:[A-Z][A-Z0-9_.]*\\.)?\\*\\s*(?:,|$)', projection, re.I)`
- L420: `for expression in projection.split(',')`
- L424: `if re.fullmatch('[A-Z][A-Z0-9_]*(?:\\.[A-Z][A-Z0-9_]*)?', expression, re.I)`

### `_source_fields_read_after_obtain` - L429-L461

```python
_source_fields_read_after_obtain(source: str | Path, operation: SourceOperation) -> set[str]
```

Find record fields read after OBTAIN and before the next DML/paragraph.

Observed calls (lexical order): `set`, `Path`, `Path(source).read_text`, `isinstance`, `str`, `text.splitlines`, `operation.operand.upper`, `re.escape`, `re.compile`, `_body`, `body.strip`, `_PARAGRAPH.fullmatch`, `re.search`, `field_ref.finditer`, `match.start`, `match.group`.
Another 2 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L439: `if operation.family != 'SELECT' or not operation.operand`
- L446: `for raw in lines[operation.line:]`
- L448: `if comment or not body.strip()`
- L450: `if _PARAGRAPH.fullmatch(body)`
- L452: `if re.search('\\b(?:OBTAIN|MODIFY|STORE|ERASE)\\b', body, re.I)`
- L454: `for match in field_ref.finditer(body)`
- L458: `if re.search('\\b(?:MOVE|ADD|SUBTRACT|COMPUTE|MULTIPLY|DIVIDE|INITIALIZE|SET)\\b.*\\b(?:TO|GIVING)\\s*$', prefix, re.I)`

### `_target_sql_blocks_with_following_context` - L463-L509

```python
_target_sql_blocks_with_following_context(target: str | Path) -> tuple[tuple[str, str | None, str, str], ...]
```

Return SQL blocks with nearby executable COBOL context after END-EXEC.

Observed calls (lexical order): `Path`, `Path(target).read_text`, `isinstance`, `str`, `text.splitlines`, `_body`, `lines.append`, `'\n'.join`, `list`, `re.finditer`, `enumerate`, `match.group`, `re.sub`, `re.sub('\\s+', ' ', match.group(1)).strip`, `re.search`, `_SQL_SELECT_FROM.search`.
Another 10 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L474: `for raw in text.splitlines()`
- L476: `if not is_comment`
- L481: `for (index, match) in enumerate(blocks)`
- L485: `for (candidate, pattern) in _SQL_COMMANDS`
- L486: `if candidate == 'SELECT' and re.search('\\bSELECT\\b', block, re.I)`
- L488: `if table_match`
- L491: `if candidate in {'COMMIT', 'ROLLBACK'} and pattern.search(block)`
- L494: `if candidate not in {'SELECT', 'COMMIT', 'ROLLBACK'}`
- Another 3 conditions/loops exist in this source span.

### `_target_sql_families` - L512-L514

```python
_target_sql_families(target: str | Path) -> tuple[str, ...]
```

Observed calls (lexical order): `_target_sql_statements`, `tuple`.

### `BusinessOperationParityAuditor` - L517-L873

```python
class BusinessOperationParityAuditor()
```

Audit source DML family coverage and per-operation DB2 table linkage.

### `BusinessOperationParityAuditor.__init__` - L520-L523

```python
__init__(self, mapping_csv: str | Path | None=None, dclgen_dir: str | Path | None=None)
```

Observed calls (lexical order): `_mapping_tables`, `_mapping_key_columns`, `_mapping_record_fields`.

### `BusinessOperationParityAuditor.audit` - L525-L873

```python
audit(self, source: str | Path, target: str | Path) -> BusinessOperationParityReport
```

Observed calls (lexical order): `_read_source`, `_target_sql_statements`, `tuple`, `any`, `set`, `match.group`, `match.group(1).upper`, `re.match`, `Path`, `Path(target).read_text`, `isinstance`, `str`, `target_text.splitlines`, `(body := _body(raw)[0]).strip`, `_body`, `OperationParityIssue`.
Another 39 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L550: `for (number, record_name) in source_writes`
- L551: `if record_name not in target_write_records`
- L562: `for (name, (number, source_body)) in original_paragraphs.items()`
- L563: `if name not in generated_paragraphs`
- L565: `if not any((_DML_OR_FILE_SIDE_EFFECT.match(line) for line in source_body))`
- L568: `if any((_DB2_OR_FILE_SIDE_EFFECT.match(line) for line in generated_body))`
- L580: `for family in sorted(source_families - target_set)`
- L601: `if direct_update_review_only`
- Another 38 conditions/loops exist in this source span.

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
