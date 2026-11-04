# `converter/resolvers/cursor_column_resolver.py`

Source: [converter/resolvers/cursor_column_resolver.py](../../../../converter/resolvers/cursor_column_resolver.py) | 339 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `f4155c1afdf1055f442fea5a71f5c7446e3fdd2234d4f805c58cddcbe40c705e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.analyzers.field_usage_analyzer import FieldUsageAnalysis
from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.column_name_resolver import ColumnNameResolver
from converter.resolvers.cursor_column_filter import CursorColumnFilter
from converter.resolvers.cursor_field_usage_column_selector import CursorFieldUsageColumnSelector
from converter.resolvers.cursor_order_by_resolver import CursorOrderByResolver
from converter.resolvers.relationship_resolver import RelationshipResolver
from converter.resolvers.table_name_resolver import TableNameResolver
from converter.services.name_normalizer import NameNormalizer
from rules.cursor_column_rules import CURSOR_COLUMN_MESSAGES, ENFORCE_FULL_RECORD_SELECT
from rules.timestamp_audit_rules import AUDIT_COLUMN_PREFIXES
```

## Local dependency notes

- [converter/analyzers/field_usage_analyzer.py](../analyzers/field_usage_analyzer.md)
- [converter/repositories/mapping_repository.py](../repositories/mapping_repository.md)
- [converter/resolvers/column_name_resolver.py](column_name_resolver.md)
- [converter/resolvers/cursor_column_filter.py](cursor_column_filter.md)
- [converter/resolvers/cursor_field_usage_column_selector.py](cursor_field_usage_column_selector.md)
- [converter/resolvers/cursor_order_by_resolver.py](cursor_order_by_resolver.md)
- [converter/resolvers/relationship_resolver.py](relationship_resolver.md)
- [converter/resolvers/table_name_resolver.py](table_name_resolver.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)
- [rules/cursor_column_rules.py](../../rules/cursor_column_rules.md)
- [rules/timestamp_audit_rules.py](../../rules/timestamp_audit_rules.md)

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure_generator.py](../generators/db2_infrastructure_generator.md)
- [tests/generated_fields/test_db2_code_fixes.py](../../tests/generated_fields/test_db2_code_fixes.md)
- [tests/test_cursor_materialised_projection.py](../../tests/test_cursor_materialised_projection.md)
- [tests/test_cursor_select_column_parity.py](../../tests/test_cursor_select_column_parity.md)
- [tests/test_db2_code_fixes.py](../../tests/test_db2_code_fixes.md)

## Symbol contracts and control points

### `CursorColumnResolver` - L21-L339

```python
class CursorColumnResolver()
```

Resolves minimal cursor SELECT and ORDER BY columns generically.

### `CursorColumnResolver.__init__` - L41-L65

```python
__init__(self, mapping_repository: MappingRepository, table_name_resolver: TableNameResolver, column_name_resolver: ColumnNameResolver, relationship_resolver: RelationshipResolver) -> None
```

Observed calls (lexical order): `CursorColumnFilter`, `CursorFieldUsageColumnSelector`, `CursorOrderByResolver`.

### `CursorColumnResolver.select_columns_for_record` - L73-L144

```python
select_columns_for_record(self, record_name: str, field_usage_analysis=None, force_full_record: bool=False) -> list[str]
```

Cursor SELECT columns for one IDMS record.

Observed calls (lexical order): `NameNormalizer.normalize`, `self._usage_columns`, `self._materialised_record_columns`, `self._unique`, `list`, `self._without_audit_columns`, `self._without_unnecessary_columns`, `self._log`, `len`.

Control points:

- L104: `if not record`
- L113: `if force_full_record`
- L115: `if full_columns`
- L134: `if resolved`

### `CursorColumnResolver._usage_columns` - L149-L186

```python
_usage_columns(self, record_name: str, field_usage_analysis=None) -> list[str]
```

Columns proven used by the original COBOL. Never fabricated.

Observed calls (lexical order): `getattr`, `self._log`, `selector.columns_from_field_usage`, `str`, `self._unique`.

Control points:

- L165: `if field_usage_analysis is None`
- L169: `if selector is None`

### `CursorColumnResolver._materialised_record_columns` - L188-L237

```python
_materialised_record_columns(self, record_name: str) -> list[str]
```

Return columns represented by the COBOL record layout.

Observed calls (lexical order): `self._unique`, `self.column_name_resolver.columns_for_record`, `getattr`, `callable`, `rows_for_record`, `set`, `str`, `str(getattr(row, 'cobol_zone', '') or getattr(row, 'reference_field_name_copybook', '') or '').strip`, `NameNormalizer.normalize`, `field_backed.add`.

Control points:

- L208: `if not columns or not callable(rows_for_record)`
- L217: `for row in rows`
- L227: `if source_field and target_column`
- L231: `if not field_backed`

### `CursorColumnResolver._without_audit_columns` - L243-L263

```python
_without_audit_columns(columns: list[str]) -> list[str]
```

Drop audit columns from a cursor SELECT list.

Observed calls (lexical order): `tuple`, `str`, `str(prefix or '').strip`, `str(prefix or '').strip().upper`, `list`, `str(column).upper`, `str(column).upper().startswith`.

Control points:

- L256: `if not prefixes`

### `CursorColumnResolver._without_unnecessary_columns` - L266-L293

```python
_without_unnecessary_columns(columns: list[str]) -> list[str]
```

Remove columns that are not typically needed in application logic.

Observed calls (lexical order): `str`, `str(column).upper`, `any`, `filtered.append`.

Control points:

- L286: `for column in columns or []`
- L289: `if any((pattern in col_upper for pattern in unnecessary_patterns))`

### `CursorColumnResolver._unique` - L299-L314

```python
_unique(values: list[str]) -> list[str]
```

Normalised, order-preserving de-duplication.

Observed calls (lexical order): `set`, `NameNormalizer.normalize`, `seen.add`, `output.append`.

Control points:

- L308: `for value in values or []`
- L310: `if not normalized or normalized in seen`

### `CursorColumnResolver._log` - L316-L322

```python
_log(self, key: str, **values) -> None
```

Observed calls (lexical order): `CURSOR_COLUMN_MESSAGES.get`, `hasattr`, `self.diagnostics.append`, `template.format`.

Control points:

- L318: `if not template`
- L320: `if not hasattr(self, 'diagnostics')`

### `CursorColumnResolver._usage_selector` - L324-L333

```python
_usage_selector(self)
```

The CursorFieldUsageColumnSelector held by this resolver.

Observed calls (lexical order): `vars`, `vars(self).values`, `hasattr`.

Control points:

- L330: `for value in vars(self).values()`
- L331: `if hasattr(value, 'select_columns_for_record')`

### `CursorColumnResolver.order_by_columns_for_record` - L335-L339

```python
order_by_columns_for_record(self, record_name: str) -> list[str]
```

Observed calls (lexical order): `self.order_by_resolver.order_by_columns_for_record`.

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
