# `converter/resolvers/cursor_column_filter.py`

Source: [converter/resolvers/cursor_column_filter.py](../../../../converter/resolvers/cursor_column_filter.py) | 100 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `043e05f6a2c930a805c7274c00ebb1d30eabbc6d2e9747957c45ba4bf2ffe16a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.resolvers.column_name_resolver import ColumnNameResolver
from converter.resolvers.table_name_resolver import TableNameResolver
from converter.services.name_normalizer import NameNormalizer
from rules.timestamp_audit_rules import AUDIT_COLUMN_PREFIXES
```

## Local dependency notes

- [converter/resolvers/column_name_resolver.py](column_name_resolver.md)
- [converter/resolvers/table_name_resolver.py](table_name_resolver.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)
- [rules/timestamp_audit_rules.py](../../rules/timestamp_audit_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/resolvers/cursor_column_resolver.py](cursor_column_resolver.md)
- [converter/resolvers/cursor_order_by_resolver.py](cursor_order_by_resolver.md)

## Symbol contracts and control points

### `CursorColumnFilter` - L9-L100

```python
class CursorColumnFilter()
```

Filters cursor columns to valid non-audit DB2 columns.

### `CursorColumnFilter.__init__` - L17-L23

```python
__init__(self, table_name_resolver: TableNameResolver, column_name_resolver: ColumnNameResolver) -> None
```

### `CursorColumnFilter.valid_non_audit_columns` - L25-L51

```python
valid_non_audit_columns(self, record_name: str, columns: list[str]) -> list[str]
```

Observed calls (lexical order): `set`, `NameNormalizer.normalize`, `self.is_audit_column`, `self.column_exists_for_record`, `seen.add`, `output.append`.

Control points:

- L33: `for column in columns`
- L36: `if not normalized`
- L39: `if normalized in seen`
- L42: `if self.is_audit_column(normalized)`
- L45: `if not self.column_exists_for_record(record_name, normalized)`

### `CursorColumnFilter.column_exists_for_record` - L53-L66

```python
column_exists_for_record(self, record_name: str, column_name: str) -> bool
```

Observed calls (lexical order): `self.table_name_resolver.table_for_record`, `self.column_name_resolver.has_column`.

Control points:

- L60: `if not table`

### `CursorColumnFilter.is_audit_column` - L68-L77

```python
is_audit_column(self, column_name: str) -> bool
```

Observed calls (lexical order): `NameNormalizer.normalize`, `any`, `column.startswith`.

### `CursorColumnFilter.unique` - L79-L100

```python
unique(self, values: list[str]) -> list[str]
```

Observed calls (lexical order): `set`, `str`, `str(value or '').strip`, `NameNormalizer.normalize`, `seen.add`, `output.append`.

Control points:

- L86: `for value in values`
- L89: `if not normalized`
- L94: `if key in seen`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
