# `converter/services/update_cobol_reference_cleanup.py`

Source: [converter/services/update_cobol_reference_cleanup.py](../../../../converter/services/update_cobol_reference_cleanup.py) | 223 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `f8652cc24bea02fd650e70b94b607e3cc0fc85d594a4cf1c9752e29a3500e15e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from collections import Counter
from converter.services.fixed_format_line_service import FixedFormatLineService
from converter.services.update_cobol_final_cleanup_utils import UpdateCobolFinalCleanupUtils
from patterns.update_final_feedback_patterns import DCLGEN_OF_REFERENCE_PATTERN, EXEC_SQL_END_PATTERN, EXEC_SQL_START_PATTERN, INITIALIZE_DCL_PATTERN, MOVE_TO_BARE_RECORD_PATTERN, NON_SQL_DCL_DOT_REFERENCE_PATTERN, SQL_LOCATION_DB_OPERATION_PATTERN
from rules.update_cobol_final_cleanup_rules import UPDATE_FINAL_LOOKAHEAD_LIMIT, UPDATE_FINAL_LOOKBACK_DUPLICATE_LIMIT
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

### `UpdateCobolReferenceCleanup` - L26-L223

```python
class UpdateCobolReferenceCleanup()
```

Handles non-SQL DCLGEN reference cleanup and safe bare-record initialization.

### `UpdateCobolReferenceCleanup.__init__` - L36-L43

```python
__init__(self, *, fixed_format: FixedFormatLineService, utils: UpdateCobolFinalCleanupUtils) -> None
```

### `UpdateCobolReferenceCleanup.normalize_non_sql_dcl_dot_references` - L45-L88

```python
normalize_non_sql_dcl_dot_references(self, text: str) -> str
```

Observed calls (lexical order): `text.splitlines`, `self.fixed_format.logical`, `EXEC_SQL_START_PATTERN.match`, `output.append`, `EXEC_SQL_END_PATTERN.match`, `NON_SQL_DCL_DOT_REFERENCE_PATTERN.sub`, `self.fixed_format.replace_body`, `self.utils.body_with_existing_indent`, `'\n'.join`, `'\n'.join(output).rstrip`.

Control points:

- L53: `for line in lines`
- L56: `if EXEC_SQL_START_PATTERN.match(logical)`
- L61: `if in_exec_sql`
- L64: `if EXEC_SQL_END_PATTERN.match(logical)`
- L74: `if updated_logical == logical`

### `UpdateCobolReferenceCleanup.replace_bare_record_initialization` - L90-L153

```python
replace_bare_record_initialization(self, text: str) -> str
```

Observed calls (lexical order): `text.splitlines`, `enumerate`, `self.fixed_format.logical`, `EXEC_SQL_START_PATTERN.match`, `output.append`, `EXEC_SQL_END_PATTERN.match`, `self.fixed_format.is_comment_or_control_line`, `MOVE_TO_BARE_RECORD_PATTERN.match`, `match.group`, `str`, `str(match.group('target') or '').upper`, `self.utils.is_protected_bare_target`, `self.nearest_dcl_group_after`, `self.recent_output_has_initialize`, `self.fixed_format.replace_body`, `self.utils.body_with_existing_indent`.
Another 2 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L98: `for (index, line) in enumerate(lines)`
- L101: `if EXEC_SQL_START_PATTERN.match(logical)`
- L106: `if in_exec_sql`
- L109: `if EXEC_SQL_END_PATTERN.match(logical)`
- L114: `if self.fixed_format.is_comment_or_control_line(line)`
- L120: `if not match`
- L126: `if self.utils.is_protected_bare_target(target)`
- L135: `if not group`
- Another 1 conditions/loops exist in this source span.

### `UpdateCobolReferenceCleanup.nearest_dcl_group_after` - L155-L197

```python
nearest_dcl_group_after(self, *, lines: list[str], start_index: int) -> str
```

Observed calls (lexical order): `range`, `len`, `min`, `self.fixed_format.logical`, `EXEC_SQL_START_PATTERN.match`, `EXEC_SQL_END_PATTERN.match`, `DCLGEN_OF_REFERENCE_PATTERN.finditer`, `match.group`, `str`, `str(match.group('group') or '').upper`, `groups.append`, `NON_SQL_DCL_DOT_REFERENCE_PATTERN.finditer`, `SQL_LOCATION_DB_OPERATION_PATTERN.match`, `Counter`, `Counter(groups).most_common`.

Control points:

- L164: `for index in range(start_index, min(len(lines), start_index + UPDATE_FINAL_LOOKAHEAD_LIMIT))`
- L170: `if EXEC_SQL_START_PATTERN.match(logical)`
- L174: `if in_exec_sql`
- L175: `if EXEC_SQL_END_PATTERN.match(logical)`
- L179: `for match in DCLGEN_OF_REFERENCE_PATTERN.finditer(logical)`
- L182: `if group`
- L185: `for match in NON_SQL_DCL_DOT_REFERENCE_PATTERN.finditer(logical)`
- L188: `if group`
- Another 2 conditions/loops exist in this source span.

### `UpdateCobolReferenceCleanup.recent_output_has_initialize` - L199-L214

```python
recent_output_has_initialize(self, output: list[str], group: str) -> bool
```

Observed calls (lexical order): `str`, `str(group or '').upper`, `len`, `max`, `range`, `self.fixed_format.logical`, `INITIALIZE_DCL_PATTERN.match`, `match.group`, `str(match.group('group') or '').upper`.

Control points:

- L207: `for index in range(len(output) - 1, start - 1, -1)`
- L211: `if match and str(match.group('group') or '').upper() == target`

### `UpdateCobolReferenceCleanup._replace_dcl_dot_with_of` - L216-L223

```python
_replace_dcl_dot_with_of(self, match) -> str
```

Observed calls (lexical order): `match.group`, `str`, `str(match.group('group') or '').upper`, `str(match.group('host') or '').upper`.

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
