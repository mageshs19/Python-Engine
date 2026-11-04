# `converter/repositories/mapping_row_query.py`

Source: [converter/repositories/mapping_row_query.py](../../../../converter/repositories/mapping_row_query.py) | 193 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `f03b955524d0b303b7e99f6cc61c4c13b592782b0270df579c041cc25645baf2`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Sheet Mapping row query helpers.

## Import declarations

```python
from __future__ import annotations
from converter.domain.models import SheetMappingRow
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [converter/domain/models.py](../domain/models.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/repositories/mapping_column_resolver.py](mapping_column_resolver.md)
- [converter/repositories/mapping_key_resolver.py](mapping_key_resolver.md)
- [converter/repositories/mapping_repository.py](mapping_repository.md)

## Symbol contracts and control points

### `MappingRowQuery` - L16-L193

```python
class MappingRowQuery()
```

### `MappingRowQuery.__init__` - L17-L21

```python
__init__(self, rows: list[SheetMappingRow]) -> None
```

### `MappingRowQuery.all` - L23-L24

```python
all(self) -> list[SheetMappingRow]
```

Observed calls (lexical order): `list`.

### `MappingRowQuery.count` - L26-L27

```python
count(self) -> int
```

Observed calls (lexical order): `len`.

### `MappingRowQuery.records` - L29-L35

```python
records(self) -> list[str]
```

Observed calls (lexical order): `NameNormalizer.normalize`, `sorted`.

### `MappingRowQuery.tables` - L37-L47

```python
tables(self) -> list[str]
```

Observed calls (lexical order): `NameNormalizer.normalize`, `sorted`.

### `MappingRowQuery.rows_for_record` - L49-L62

```python
rows_for_record(self, record_name: str) -> list[SheetMappingRow]
```

Observed calls (lexical order): `NameNormalizer.normalize`.

Control points:

- L55: `if not target`

### `MappingRowQuery.rows_for_table` - L64-L79

```python
rows_for_table(self, table_name: str) -> list[SheetMappingRow]
```

Observed calls (lexical order): `NameNormalizer.normalize`.

Control points:

- L70: `if not target`

### `MappingRowQuery.db2_columns_for_table` - L81-L97

```python
db2_columns_for_table(self, table_name: str) -> list[str]
```

Observed calls (lexical order): `set`, `self.rows_for_table`, `NameNormalizer.normalize`, `seen.add`, `output.append`.

Control points:

- L88: `for row in self.rows_for_table(table_name)`
- L92: `if not column or column in seen`

### `MappingRowQuery.db2_table_for_record` - L99-L115

```python
db2_table_for_record(self, record_name: str) -> str
```

Observed calls (lexical order): `self.rows_for_record`, `NameNormalizer.normalize`.

Control points:

- L105: `for row in rows`
- L107: `if table`
- L110: `for row in rows`
- L112: `if table`

### `MappingRowQuery.cobol_field_for_column` - L123-L171

```python
cobol_field_for_column(self, table_name: str, column_name: str) -> str
```

The COBOL Zone this DB2 column was mapped FROM.

Observed calls (lexical order): `NameNormalizer.normalize`, `self.rows_for_table`, `self._cobol_zone_field`.

Control points:

- L146: `if not target`
- L150: `if not rows`
- L155: `for row in rows`
- L160: `if column != target`
- L163: `for candidate in (row.cobol_zone, row.reference_field_name_copybook)`
- L168: `if field`

### `MappingRowQuery._cobol_zone_field` - L174-L193

```python
_cobol_zone_field(value) -> str
```

The data-name inside a COBOL Zone cell.

Observed calls (lexical order): `str`, `str(value or '').strip`, `text.split`, `len`, `parts[0].isdigit`, `' '.join`, `NameNormalizer.to_cobol`, `text.strip`.

Control points:

- L186: `if not text`
- L190: `if len(parts) > 1 and parts[0].isdigit()`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
