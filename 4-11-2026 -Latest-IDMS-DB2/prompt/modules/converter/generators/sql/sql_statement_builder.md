# `converter/generators/sql/sql_statement_builder.py`

Source: [converter/generators/sql/sql_statement_builder.py](../../../../../converter/generators/sql/sql_statement_builder.py) | 594 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `9792e85896b2347deff67caf117f3ad223af506452f9323878015b39fc99d75a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Builds DB2 statement bodies: INSERT / UPDATE / DELETE / SELECT-skip / MOVE.

## Import declarations

```python
from __future__ import annotations
from converter.generators.db2_infrastructure.sql_location_move_builder import SqlLocationMoveBuilder
from converter.services.name_normalizer import NameNormalizer
from rules.sql_location_rules import LEGACY_OPERATION_DELETE, LEGACY_OPERATION_INSERT, LEGACY_OPERATION_UPDATE, LEGACY_RECORD_LOCATION_TEMPLATE
from rules.update_sql_cleanup_rules import UPDATE_QUERYNO
```

## Local dependency notes

- [converter/generators/db2_infrastructure/sql_location_move_builder.py](../db2_infrastructure/sql_location_move_builder.md)
- [converter/services/name_normalizer.py](../../services/name_normalizer.md)
- [rules/sql_location_rules.py](../../../rules/sql_location_rules.md)
- [rules/update_sql_cleanup_rules.py](../../../rules/update_sql_cleanup_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/sql_generator.py](../sql_generator.md)
- [tests/test_sql_insert_sequence_metadata.py](../../../tests/test_sql_insert_sequence_metadata.md)

## Symbol contracts and control points

### `SqlStatementBuilder` - L19-L594

```python
class SqlStatementBuilder()
```

### `SqlStatementBuilder.__init__` - L20-L35

```python
__init__(self, column_resolver, line_builder, date_builder, host_variable_resolver, mapping_repository, update_plan_resolver) -> None
```

### `SqlStatementBuilder._sqlcode_evaluate_block` - L37-L50

```python
_sqlcode_evaluate_block(self, operation: str, table: str) -> list[str]
```

Manual-standard SQLCODE handling shared by INSERT/UPDATE/DELETE.

### `SqlStatementBuilder.select_by_key` - L52-L243

```python
select_by_key(self, record_name: str, *, for_lrf_parent: bool=False, required_columns: list[str] | tuple[str, ...] | set[str] | None=None, status_handling: bool=True, read_kind: str='LRF keyed parent') -> list[str]
```

Render a keyed SELECT when a retrieval needs a mapped record.

Observed calls (lexical order): `NameNormalizer.normalize`, `self.column_resolver.resolved_table_for_record`, `self.line_builder.missing_sql`, `self.column_resolver.key_columns_for_record`, `NameNormalizer.to_cobol`, `getattr`, `callable`, `set`, `rows_for_record`, `type`, `str`, `str(getattr(row, 'cobol_zone', '') or getattr(row, 'reference_field_name_copybook', '') or '').strip`, `seen_columns.add`, `mapped_columns.append`, `available_record_columns.discard`, `required.issubset`.
Another 8 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L76: `if not record or not table`
- L87: `if not key_columns`
- L94: `if not for_lrf_parent`
- L109: `if not callable(rows_for_record)`
- L132: `if required is not None and (not required)`
- L139: `for row in record_rows`
- L149: `if not source_field or not column or column in seen_columns`
- L151: `if required is not None and column not in required`
- Another 4 conditions/loops exist in this source span.

### `SqlStatementBuilder.insert` - L245-L319

```python
insert(self, record_name: str, paragraph: str='') -> list[str]
```

Render a metadata-driven INSERT with sequence and audit defaults.

Observed calls (lexical order): `NameNormalizer.normalize`, `self.column_resolver.resolved_table_for_record`, `self.line_builder.missing_sql`, `self.column_resolver.insert_columns_for_record`, `self.column_resolver.sequence_key_for_record`, `columns.append`, `values.append`, `self.host_variable_resolver.host_reference_for_column`, `NameNormalizer.to_cobol`, `LEGACY_RECORD_LOCATION_TEMPLATE.format`, `str`, `str(paragraph or '').strip`, `SqlLocationMoveBuilder`, `SqlLocationMoveBuilder().sentence`, `lines.append`, `lines.extend`.
Another 4 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L259: `if not record or not table`
- L266: `if not columns`
- L274: `if sequence_key`
- L276: `if not sequence_name or sequence_precision <= 0`
- L284: `if sequence_column not in columns`
- L288: `for column in columns`
- L289: `if sequence_key and column == sequence_column`
- L297: `if not host`
- Another 1 conditions/loops exist in this source span.

### `SqlStatementBuilder._insert_default_moves` - L321-L346

```python
_insert_default_moves(self, table: str, columns: list[str]) -> list[str]
```

Initialize conventional audit/technical columns for a new row.

Observed calls (lexical order): `NameNormalizer.normalize`, `NameNormalizer.normalize(name).startswith`, `next`, `self.host_variable_resolver.host_reference_for_column`, `moves.append`, `self._cobol_move_target`.

Control points:

- L334: `for (prefix, source) in defaults`
- L336: `if not column`
- L339: `if host`
- L342: `if technical_key`
- L344: `if host`

### `SqlStatementBuilder._cobol_move_target` - L349-L356

```python
_cobol_move_target(host_reference: str) -> str
```

Convert a DB2 host reference to a COBOL data-name reference.

Observed calls (lexical order): `str`, `str(host_reference or '').strip`, `str(host_reference or '').strip().lstrip`, `value.split`.

Control points:

- L352: `if '.' in value`
- L354: `if group and field`

### `SqlStatementBuilder.update` - L358-L443

```python
update(self, record_name: str, changed_source_fields: list[str] | None=None, paragraph: str='') -> list[str]
```

The converted MODIFY block, SQL-LOCATION included.

Observed calls (lexical order): `NameNormalizer.normalize`, `self.update_plan_resolver.resolve`, `self.messages.extend`, `self.column_resolver.key_columns_for_record`, `self.line_builder.missing_sql`, `self.line_builder.set_lines`, `self.line_builder.where_lines`, `NameNormalizer.to_cobol`, `str`, `str(paragraph or '').strip`, `LEGACY_RECORD_LOCATION_TEMPLATE.format`, `SqlLocationMoveBuilder`, `SqlLocationMoveBuilder().sentence`, `lines.append`, `lines.extend`, `self._sqlcode_evaluate_block`.

Control points:

- L385: `if plan.table_name`
- L391: `if not plan.is_complete`
- L408: `if not set_lines or not where_lines`
- L418: `if not location`
- L429: `if sql_location`

### `SqlStatementBuilder.delete` - L445-L525

```python
delete(self, record_name: str, paragraph: str='') -> list[str]
```

The converted ERASE block, SQL-LOCATION included.

Observed calls (lexical order): `NameNormalizer.normalize`, `self.column_resolver.resolved_table_for_record`, `self.line_builder.missing_sql`, `self.column_resolver.key_columns_for_record`, `self.line_builder.where_lines`, `NameNormalizer.to_cobol`, `str`, `str(paragraph or '').strip`, `LEGACY_RECORD_LOCATION_TEMPLATE.format`, `SqlLocationMoveBuilder`, `SqlLocationMoveBuilder().sentence`, `lines.append`, `lines.extend`, `self._sqlcode_evaluate_block`.

Control points:

- L476: `if not record or not table`
- L492: `if not where_lines`
- L502: `if not location`
- L513: `if sql_location`

### `SqlStatementBuilder.commit` - L527-L533

```python
commit(self) -> list[str]
```

### `SqlStatementBuilder.rollback` - L535-L541

```python
rollback(self) -> list[str]
```

### `SqlStatementBuilder.changed_field_move` - L543-L583

```python
changed_field_move(self, record_name: str, source_value: str, target_source_field: str) -> list[str]
```

Observed calls (lexical order): `NameNormalizer.normalize`, `self.column_resolver.resolved_table_for_record`, `self.mapping_repository.column_for_source_field`, `self.host_variable_resolver.host_reference_key`, `self.date_builder.is_db2_date_column`, `self.date_builder.date_ymd8_to_db2_external_move`.

Control points:

- L557: `if not table or not column`
- L569: `if not host_key`
- L577: `if self.date_builder.is_db2_date_column(column)`

### `SqlStatementBuilder.missing_mapping` - L585-L594

```python
missing_mapping(self, record_name: str, reason: str) -> list[str]
```

Observed calls (lexical order): `self.line_builder.missing_sql`.

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
