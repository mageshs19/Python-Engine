# `converter/generators/sql/sql_column_resolver.py`

Source: [converter/generators/sql/sql_column_resolver.py](../../../../../converter/generators/sql/sql_column_resolver.py) | 253 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `eb52df6ab8181bad2d158b41c965f41895341b8de9fbe866707f1e222abe3f03`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> SQL column resolution: table, key columns, insert columns, DCLGEN filter.

## Import declarations

```python
from __future__ import annotations
import re
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [converter/services/name_normalizer.py](../../services/name_normalizer.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/sql_generator.py](../sql_generator.md)
- [tests/test_sql_column_resolver_table_alias.py](../../../tests/test_sql_column_resolver_table_alias.md)
- [tests/test_sql_insert_sequence_metadata.py](../../../tests/test_sql_insert_sequence_metadata.md)

## Symbol contracts and control points

### `SqlColumnResolver` - L13-L253

```python
class SqlColumnResolver()
```

### `SqlColumnResolver.__init__` - L14-L22

```python
__init__(self, mapping_repository, dclgen_repository, table_name_resolver) -> None
```

### `SqlColumnResolver.resolved_table_for_record` - L24-L30

```python
resolved_table_for_record(self, record_name: str) -> str
```

Observed calls (lexical order): `self.mapping_repository.db2_table_for_record`, `self.table_name_resolver.resolve_table`.

Control points:

- L28: `if not mapped_table`

### `SqlColumnResolver.key_columns_for_record` - L32-L57

```python
key_columns_for_record(self, record_name: str, table_name: str) -> list[str]
```

Key columns for SQL WHERE. Composite PK / CALC keys required; FK / FOREIGN columns never included; Sheet Mapping order preserved.

Observed calls (lexical order): `hasattr`, `self._key_columns_from_mapping_rows`, `self.mapping_repository.primary_key_columns_for_record`, `self.filter_to_existing_dclgen_columns`.

Control points:

- L43: `if hasattr(self.mapping_repository, 'rows_for_record')`
- L46: `if not columns and hasattr(self.mapping_repository, 'primary_key_columns_for_record')`

### `SqlColumnResolver._key_columns_from_mapping_rows` - L59-L100

```python
_key_columns_from_mapping_rows(self, record_name: str) -> list[str]
```

Observed calls (lexical order): `set`, `self.mapping_repository.rows_for_record`, `NameNormalizer.normalize`, `getattr`, `' '.join`, `seen.add`, `output.append`.

Control points:

- L66: `for row in self.mapping_repository.rows_for_record(record_name)`
- L74: `if not column`
- L80: `if 'FOREIGN' in combined_text`
- L82: `if ' FK ' in padded_text`
- L92: `if not is_key_column`
- L94: `if column in seen`

### `SqlColumnResolver.insert_columns_for_record` - L102-L130

```python
insert_columns_for_record(self, record_name: str, table_name: str) -> list[str]
```

Observed calls (lexical order): `self.mapping_repository.db2_table_for_record`, `self.mapping_repository.db2_columns_for_table`, `self.filter_to_existing_dclgen_columns`, `self._unmapped_technical_idms_key_columns`, `self._unique`.

### `SqlColumnResolver.sequence_key_for_record` - L132-L178

```python
sequence_key_for_record(self, record_name: str, table_name: str) -> tuple[str, str, int] | None
```

Return (column, sequence, precision) for a mapped sequence key.

Observed calls (lexical order): `getattr`, `callable`, `rows_for_record`, `NameNormalizer.normalize`, `' '.join`, `' '.join((str(getattr(row, attr, '') or '') for attr in ('db2_key', 'idms_key', 'remarks', 'hopex_expressio...`, `str`, `self.mapping_repository.db2_table_for_record`, `re.search`, `explicit.group`, `base_table.endswith`, `self._numeric_precision`.

Control points:

- L143: `if not callable(rows_for_record)`
- L146: `for row in rows`
- L151: `if not column`
- L161: `if not sequence_key`
- L171: `if explicit`
- L173: `if base_table.endswith('TB')`
- L175: `if not sequence`

### `SqlColumnResolver._numeric_precision` - L180-L190

```python
_numeric_precision(self, table_name: str, column: str, mapping_row) -> int
```

Observed calls (lexical order): `getattr`, `str`, `getattr(self.dclgen_repository, 'columns_for_table', lambda _t: [])`, `self.table_name_resolver.resolve_table`, `NameNormalizer.normalize`, `re.search`, `int`, `match.group`.

Control points:

- L182: `if not type_text`
- L183: `for dcl_column in getattr(self.dclgen_repository, 'columns_for_table', lambda _t: [])(self.table_name_resolver.resolve_table(table_name)) or []`
- L186: `if NameNormalizer.normalize(getattr(dcl_column, 'column_name', '')) == column`

### `SqlColumnResolver._unmapped_technical_idms_key_columns` - L192-L205

```python
_unmapped_technical_idms_key_columns(self, table_name: str, mapped_columns: list[str]) -> list[str]
```

Observed calls (lexical order): `self.table_name_resolver.resolve_table`, `getattr`, `callable`, `set`, `columns_for_table`, `NameNormalizer.normalize`, `output.append`.

Control points:

- L197: `if not resolved or not callable(columns_for_table)`
- L201: `for column in columns_for_table(resolved) or []`
- L203: `if name and name not in mapped and ('IDMSKEY' in name)`

### `SqlColumnResolver.minimal_select_columns` - L207-L216

```python
minimal_select_columns(self, record_name: str, table_name: str, key_columns: list[str]) -> list[str]
```

Observed calls (lexical order): `self.filter_to_existing_dclgen_columns`.

### `SqlColumnResolver.filter_to_existing_dclgen_columns` - L218-L242

```python
filter_to_existing_dclgen_columns(self, table_name: str, columns: list[str]) -> list[str]
```

Observed calls (lexical order): `self.table_name_resolver.resolve_table`, `set`, `self.dclgen_repository.column_names_for_table`, `NameNormalizer.normalize`, `output.append`, `self._unique`.

Control points:

- L224: `if not resolved_table`
- L230: `if not dclgen_columns`
- L234: `for column in columns`
- L236: `if not normalized`
- L238: `if normalized not in dclgen_columns`

### `SqlColumnResolver._unique` - L244-L253

```python
_unique(self, values: list[str]) -> list[str]
```

Observed calls (lexical order): `set`, `NameNormalizer.normalize`, `seen.add`, `output.append`.

Control points:

- L247: `for value in values`
- L249: `if not normalized or normalized in seen`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
