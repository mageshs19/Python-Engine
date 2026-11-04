# `converter/services/update_diagnostic_label_normalizer.py`

Source: [converter/services/update_diagnostic_label_normalizer.py](../../../../converter/services/update_diagnostic_label_normalizer.py) | 234 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `5eff07ec7ac0bd79d7bd59885f348aea4f28a2ba16608704127f750c51390d84`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.services.fixed_format_line_service import FixedFormatLineService
from converter.services.update_cobol_final_cleanup_utils import UpdateCobolFinalCleanupUtils
from patterns.update_final_feedback_patterns import CONVERTED_DB2_OPERATION_COMMENT_PATTERN, EXEC_SQL_END_PATTERN, EXEC_SQL_START_PATTERN, FROM_STATEMENT_PATTERN, SQL_LOCATION_DB_OPERATION_PATTERN, UPDATE_STATEMENT_PATTERN
from rules.update_cobol_final_cleanup_rules import UPDATE_FINAL_LOOKAHEAD_LIMIT
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](fixed_format_line_service.md)
- [converter/services/update_cobol_final_cleanup_utils.py](update_cobol_final_cleanup_utils.md)
- [patterns/update_final_feedback_patterns.py](../../patterns/update_final_feedback_patterns.md)
- [rules/update_cobol_final_cleanup_rules.py](../../rules/update_cobol_final_cleanup_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/services/update_cobol_final_cleanup_service.py](update_cobol_final_cleanup_service.md)

## Symbol contracts and control points

### `UpdateDiagnosticLabelNormalizer` - L20-L234

```python
class UpdateDiagnosticLabelNormalizer()
```

Rewrites generated DB2 diagnostic labels from IDMS record naming to nearby resolved DB2 table naming when SQL context is available.

### `UpdateDiagnosticLabelNormalizer.__init__` - L26-L33

```python
__init__(self, *, fixed_format: FixedFormatLineService, utils: UpdateCobolFinalCleanupUtils) -> None
```

### `UpdateDiagnosticLabelNormalizer.normalize_db2_diagnostic_labels` - L35-L77

```python
normalize_db2_diagnostic_labels(self, text: str) -> str
```

Observed calls (lexical order): `text.splitlines`, `enumerate`, `self.fixed_format.logical`, `SQL_LOCATION_DB_OPERATION_PATTERN.match`, `self._replacement_sql_location`, `sql_location_match.group`, `str`, `output.append`, `CONVERTED_DB2_OPERATION_COMMENT_PATTERN.match`, `self._replacement_comment`, `comment_match.group`, `'\n'.join`, `'\n'.join(output).rstrip`.

Control points:

- L42: `for (index, line) in enumerate(lines)`
- L47: `if sql_location_match`
- L55: `if replacement`
- L61: `if comment_match`
- L71: `if replacement`

### `UpdateDiagnosticLabelNormalizer._replacement_sql_location` - L79-L104

```python
_replacement_sql_location(self, *, line: str, lines: list[str], start_index: int, operation: str) -> str
```

Observed calls (lexical order): `self.nearby_table_for_operation`, `str`, `str(operation or '').upper`, `self.fixed_format.replace_body`, `self.utils.body_with_existing_indent`.

Control points:

- L93: `if not table`

### `UpdateDiagnosticLabelNormalizer._replacement_comment` - L106-L133

```python
_replacement_comment(self, *, line: str, lines: list[str], start_index: int, operation_text: str, prefix: str, suffix: str) -> str
```

Observed calls (lexical order): `self.nearby_table_for_comment_operation`, `self.fixed_format.replace_body`, `self.utils.comment_body_for_line`.

Control points:

- L122: `if not table`

### `UpdateDiagnosticLabelNormalizer.nearby_table_for_comment_operation` - L135-L172

```python
nearby_table_for_comment_operation(self, *, lines: list[str], start_index: int, operation_text: str) -> str
```

Observed calls (lexical order): `str`, `str(operation_text or '').upper`, `self.nearby_table_for_operation`.

Control points:

- L144: `if 'MODIFY' in normalized`
- L151: `if 'OBTAIN' in normalized or 'FIND' in normalized`
- L158: `if 'STORE' in normalized`
- L165: `if 'ERASE' in normalized`

### `UpdateDiagnosticLabelNormalizer.nearby_table_for_operation` - L174-L216

```python
nearby_table_for_operation(self, *, lines: list[str], start_index: int, operation: str) -> str
```

Observed calls (lexical order): `str`, `str(operation or '').upper`, `range`, `len`, `min`, `self.fixed_format.logical`, `EXEC_SQL_START_PATTERN.match`, `EXEC_SQL_END_PATTERN.match`, `UPDATE_STATEMENT_PATTERN.match`, `str(update_match.group('table') or '').upper`, `update_match.group`, `FROM_STATEMENT_PATTERN.match`, `from_match.group`, `str(from_match.group('table') or '').upper`, `self.table_for_insert_or_delete`.

Control points:

- L184: `for index in range(start_index, min(len(lines), start_index + UPDATE_FINAL_LOOKAHEAD_LIMIT))`
- L190: `if EXEC_SQL_START_PATTERN.match(logical)`
- L194: `if in_exec_sql and EXEC_SQL_END_PATTERN.match(logical)`
- L198: `if wanted_operation == 'UPDATE'`
- L201: `if update_match`
- L204: `if wanted_operation == 'SELECT'`
- L207: `if from_match`
- L210: `if wanted_operation in {'INSERT', 'DELETE'}`
- Another 1 conditions/loops exist in this source span.

### `UpdateDiagnosticLabelNormalizer.table_for_insert_or_delete` - L218-L234

```python
table_for_insert_or_delete(self, logical: str) -> str
```

Observed calls (lexical order): `str`, `str(logical or '').strip`, `str(logical or '').strip().upper`, `text.split`, `len`.

Control points:

- L225: `if len(parts) < 3`
- L228: `if parts[0] == 'INSERT' and parts[1] == 'INTO'`
- L231: `if parts[0] == 'DELETE' and parts[1] == 'FROM'`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
