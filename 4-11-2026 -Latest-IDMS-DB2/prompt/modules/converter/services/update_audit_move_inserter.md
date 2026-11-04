# `converter/services/update_audit_move_inserter.py`

Source: [converter/services/update_audit_move_inserter.py](../../../../converter/services/update_audit_move_inserter.py) | 420 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `29677189fa5deb8498ba93fb13c0aa618566dedb833abacb7ff1f94b1cd59c9a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`ASSIGNMENT_SEPARATOR` (L26), `SENTENCE_TERMINATOR` (L27), `WHERE_INFIX` (L28), `__all__` (L420)

## Import declarations

```python
from __future__ import annotations
from converter.services.fixed_format_line_service import FixedFormatLineService
from converter.services.update_cobol_final_cleanup_utils import UpdateCobolFinalCleanupUtils
from patterns.update_final_feedback_patterns import EXEC_SQL_END_PATTERN, EXEC_SQL_START_PATTERN, MOVE_TO_DCL_OF_REFERENCE_PATTERN, SET_KEYWORD_PATTERN, SQL_SET_ASSIGNMENT_PATTERN, UPDATE_STATEMENT_PATTERN, WHERE_KEYWORD_PATTERN
from rules.timestamp_audit_rules import UPDATE_AUDIT_COLUMN_PREFIXES
from rules.update_cobol_final_cleanup_rules import AUDIT_SOURCE_BY_KIND, TIMESTAMP_AUDIT_PREFIXES, UPDATE_FINAL_LOOKBACK_DUPLICATE_LIMIT, USER_AUDIT_PREFIXES
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](fixed_format_line_service.md)
- [converter/services/update_cobol_final_cleanup_utils.py](update_cobol_final_cleanup_utils.md)
- [patterns/update_final_feedback_patterns.py](../../patterns/update_final_feedback_patterns.md)
- [rules/timestamp_audit_rules.py](../../rules/timestamp_audit_rules.md)
- [rules/update_cobol_final_cleanup_rules.py](../../rules/update_cobol_final_cleanup_rules.md)

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/services/update_cobol_final_cleanup_service.py](update_cobol_final_cleanup_service.md)
- [converter/ui/conversion_actions.py](../ui/conversion_actions.md)
- [runners/batch/update_postprocess_pipeline.py](../../runners/batch/update_postprocess_pipeline.md)
- [runners/update/update_postprocess_pipeline.py](../../runners/update/update_postprocess_pipeline.md)

## Symbol contracts and control points

### `UpdateAuditMoveInserter` - L31-L417

```python
class UpdateAuditMoveInserter()
```

Inserts audit MOVE statements before a generated UPDATE SQL block.

### `UpdateAuditMoveInserter.__init__` - L80-L88

```python
__init__(self, *, fixed_format: FixedFormatLineService, utils: UpdateCobolFinalCleanupUtils) -> None
```

### `UpdateAuditMoveInserter.insert_update_audit_moves` - L93-L173

```python
insert_update_audit_moves(self, text: str) -> str
```

Observed calls (lexical order): `text.splitlines`, `self.find_update_exec_sql_blocks`, `self.messages.append`, `text.rstrip`, `list`, `sorted`, `self.audit_targets_from_update_block`, `self.has_recent_move_to_host`, `self.source_for_audit_kind`, `insert_lines.append`, `self.fixed_format.replace_body`, `self.utils.body_with_existing_indent`, `len`, `'\n'.join`, `'\n'.join(output).rstrip`.

Control points:

- L102: `if not update_blocks`
- L112: `for (start, end) in sorted(update_blocks, reverse=True)`
- L116: `if not audit_targets`
- L126: `for (group, host, audit_kind) in audit_targets`
- L127: `if self.has_recent_move_to_host(lines=output, insert_index=start, group=group, host=host)`
- L141: `if not source`
- L161: `if not insert_lines`
- L167: `if inserted`

### `UpdateAuditMoveInserter.find_update_exec_sql_blocks` - L178-L216

```python
find_update_exec_sql_blocks(self, lines: list[str]) -> list[tuple[int, int]]
```

Observed calls (lexical order): `enumerate`, `self.fixed_format.logical`, `logical.upper`, `EXEC_SQL_START_PATTERN.match`, `UPDATE_STATEMENT_PATTERN.match`, `EXEC_SQL_END_PATTERN.match`, `blocks.append`.

Control points:

- L187: `for (index, line) in enumerate(lines)`
- L191: `if EXEC_SQL_START_PATTERN.match(logical)`
- L196: `if 'END-EXEC' in upper`
- L206: `if in_exec_sql and UPDATE_STATEMENT_PATTERN.match(logical)`
- L209: `if in_exec_sql and EXEC_SQL_END_PATTERN.match(logical)`
- L210: `if has_update`

### `UpdateAuditMoveInserter.audit_targets_from_update_block` - L221-L250

```python
audit_targets_from_update_block(self, block: list[str]) -> list[tuple[str, str, str]]
```

Observed calls (lexical order): `self.set_clause_text`, `region.split`, `segment.strip`, `SQL_SET_ASSIGNMENT_PATTERN.match`, `match.group`, `str`, `str(match.group('column') or '').upper`, `str(match.group('group') or '').upper`, `str(match.group('host') or '').upper`, `self.audit_kind_for_column`, `targets.append`, `self.unique_targets`.

Control points:

- L228: `for segment in region.split(ASSIGNMENT_SEPARATOR)`
- L231: `if not candidate`
- L236: `if not match`
- L245: `if not audit_kind`

### `UpdateAuditMoveInserter.set_clause_text` - L252-L300

```python
set_clause_text(self, block: list[str]) -> str
```

Everything between SET and WHERE, as ONE logical string.

Observed calls (lexical order): `self.fixed_format.logical`, `logical.strip`, `SET_KEYWORD_PATTERN.match`, `logical[opener.end():].strip`, `opener.end`, `parts.append`, `WHERE_KEYWORD_PATTERN.match`, `logical.upper`, `logical.upper().find`, `logical[:marker].strip`, `' '.join`.

Control points:

- L265: `for line in block`
- L268: `if not logical.strip()`
- L271: `if not in_set`
- L274: `if not opener`
- L280: `if remainder`
- L285: `if WHERE_KEYWORD_PATTERN.match(logical)`
- L290: `if marker >= 0`
- L293: `if head`

### `UpdateAuditMoveInserter.audit_kind_for_column` - L305-L320

```python
audit_kind_for_column(self, column: str) -> str
```

Observed calls (lexical order): `str`, `str(column or '').upper`, `self.has_update_audit_prefix`, `normalized.startswith`.

Control points:

- L311: `if not self.has_update_audit_prefix(normalized)`
- L314: `if normalized.startswith(TIMESTAMP_AUDIT_PREFIXES)`
- L317: `if normalized.startswith(USER_AUDIT_PREFIXES)`

### `UpdateAuditMoveInserter.has_update_audit_prefix` - L322-L331

```python
has_update_audit_prefix(self, column: str) -> bool
```

Observed calls (lexical order): `str`, `str(column or '').upper`, `any`, `normalized.startswith`, `str(prefix or '').upper`.

### `UpdateAuditMoveInserter.source_for_audit_kind` - L333-L337

```python
source_for_audit_kind(self, audit_kind: str) -> str
```

Observed calls (lexical order): `AUDIT_SOURCE_BY_KIND.get`, `str`, `str(audit_kind or '').lower`.

### `UpdateAuditMoveInserter.has_recent_move_to_host` - L342-L375

```python
has_recent_move_to_host(self, *, lines: list[str], insert_index: int, group: str, host: str) -> bool
```

Observed calls (lexical order): `str`, `str(group or '').upper`, `str(host or '').upper`, `max`, `range`, `self.fixed_format.logical`, `logical.strip`, `self.is_sentence_boundary`, `MOVE_TO_DCL_OF_REFERENCE_PATTERN.match`, `match.group`, `str(match.group('group') or '').upper`, `str(match.group('host') or '').upper`.

Control points:

- L355: `for index in range(insert_index - 1, floor - 1, -1)`
- L358: `if not logical.strip()`
- L361: `if self.is_sentence_boundary(logical)`
- L366: `if not match`
- L372: `if found_group == target_group and found_host == target_host`

### `UpdateAuditMoveInserter.is_sentence_boundary` - L378-L389

```python
is_sentence_boundary(logical: str) -> bool
```

A single word closed by a period: header or scope terminator.

Observed calls (lexical order): `str`, `str(logical or '').strip`, `text.endswith`, `len`, `text[:-len(SENTENCE_TERMINATOR)].strip`, `bool`.

Control points:

- L384: `if not text.endswith(SENTENCE_TERMINATOR)`

### `UpdateAuditMoveInserter.unique_targets` - L394-L417

```python
unique_targets(self, values: list[tuple[str, str, str]]) -> list[tuple[str, str, str]]
```

Observed calls (lexical order): `set`, `str`, `str(group or '').upper`, `str(host or '').upper`, `str(audit_kind or '').lower`, `seen.add`, `output.append`.

Control points:

- L401: `for (group, host, audit_kind) in values`
- L408: `if not key[0] or not key[1] or (not key[2])`
- L411: `if key in seen`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
