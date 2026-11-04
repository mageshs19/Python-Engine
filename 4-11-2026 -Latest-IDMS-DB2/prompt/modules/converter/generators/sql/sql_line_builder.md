# `converter/generators/sql/sql_line_builder.py`

Source: [converter/generators/sql/sql_line_builder.py](../../../../../converter/generators/sql/sql_line_builder.py) | 108 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `b795e2ffc79dfe4ab9c777dd1358c1a8be2fc129662f7f8475968bb919da188b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> SQL line builders: SET, WHERE, column list, host list, skipped block.

## Import declarations

```python
from __future__ import annotations
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [converter/services/name_normalizer.py](../../services/name_normalizer.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/sql_generator.py](../sql_generator.md)
- [tests/test_sql_insert_sequence_metadata.py](../../../tests/test_sql_insert_sequence_metadata.md)

## Symbol contracts and control points

### `SqlLineBuilder` - L11-L108

```python
class SqlLineBuilder()
```

### `SqlLineBuilder.__init__` - L12-L13

```python
__init__(self, host_variable_resolver) -> None
```

### `SqlLineBuilder.set_lines` - L15-L41

```python
set_lines(self, table_name: str, columns: list[str], indent: str) -> list[str]
```

Observed calls (lexical order): `NameNormalizer.normalize`, `self.host_variable_resolver.host_reference_for_column`, `assignments.append`, `enumerate`, `len`, `output.append`.

Control points:

- L23: `for column in columns`
- L25: `if not normalized`
- L31: `if not host`
- L36: `for (index, item) in enumerate(assignments)`

### `SqlLineBuilder.where_lines` - L43-L73

```python
where_lines(self, table_name: str, key_columns: list[str], indent: str) -> list[str]
```

Build SQL WHERE lines from composite key columns. The caller passes only PK / CALC key columns; FK exclusion is handled upstream.

Observed calls (lexical order): `NameNormalizer.normalize`, `self.host_variable_resolver.host_reference_for_column`, `conditions.append`, `enumerate`, `output.append`.

Control points:

- L55: `for column in key_columns`
- L57: `if not normalized`
- L63: `if not host`
- L68: `for (index, item) in enumerate(conditions)`

### `SqlLineBuilder.sql_column_list` - L75-L84

```python
sql_column_list(self, columns: list[str], indent: str) -> list[str]
```

Observed calls (lexical order): `enumerate`, `len`, `output.append`.

Control points:

- L81: `for (index, column) in enumerate(columns)`

### `SqlLineBuilder.host_variable_list` - L86-L95

```python
host_variable_list(self, host_variables: list[str], indent: str) -> list[str]
```

Observed calls (lexical order): `enumerate`, `len`, `output.append`.

Control points:

- L92: `for (index, host) in enumerate(host_variables)`

### `SqlLineBuilder.missing_sql` - L97-L108

```python
missing_sql(self, operation: str, record_name: str, reason: str) -> list[str]
```

Observed calls (lexical order): `NameNormalizer.to_cobol`.

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
