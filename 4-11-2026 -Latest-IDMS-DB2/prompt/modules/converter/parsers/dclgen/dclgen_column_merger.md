# `converter/parsers/dclgen/dclgen_column_merger.py`

Source: [converter/parsers/dclgen/dclgen_column_merger.py](../../../../../converter/parsers/dclgen/dclgen_column_merger.py) | 136 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `56a5db5580d8e1d354d349831080b833b722a14dd6c4b1c08008048c06913d1e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Merges parsed SQL columns with COBOL host fields into DclgenColumn objects.

## Import declarations

```python
from __future__ import annotations
from catalogs.dclgen_schema import DCLGEN_HOST_FIELD_SUFFIXES_TO_IGNORE
from converter.domain.models import DclgenColumn
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [catalogs/dclgen_schema.py](../../../catalogs/dclgen_schema.md)
- [converter/domain/models.py](../../domain/models.md)
- [converter/services/name_normalizer.py](../../services/name_normalizer.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/parsers/dclgen_parser.py](../dclgen_parser.md)

## Symbol contracts and control points

### `DclgenColumnMerger` - L13-L136

```python
class DclgenColumnMerger()
```

### `DclgenColumnMerger.__init__` - L14-L15

```python
__init__(self, name_normalizer) -> None
```

### `DclgenColumnMerger.merge_sql_columns_with_cobol_hosts` - L17-L58

```python
merge_sql_columns_with_cobol_hosts(self, sql_columns: list[dict[str, object]], cobol_fields: list[dict[str, str]], fallback_table_name: str) -> list[DclgenColumn]
```

Observed calls (lexical order): `self._usable_host_fields`, `enumerate`, `self.names.normalize_sql_name`, `str`, `sql_column.get`, `str(sql_column.get('db2_type', '') or '').strip`, `bool`, `self._best_host_for_column`, `output.append`, `DclgenColumn`, `host.get`.

Control points:

- L26: `for (index, sql_column) in enumerate(sql_columns)`

### `DclgenColumnMerger.fallback_columns_from_cobol_fields` - L60-L86

```python
fallback_columns_from_cobol_fields(self, table_name: str, cobol_fields: list[dict[str, str]]) -> list[DclgenColumn]
```

Observed calls (lexical order): `self._usable_host_fields`, `field.get`, `output.append`, `DclgenColumn`, `self.names.normalize_cobol_name_to_db2`.

Control points:

- L67: `for field in self._usable_host_fields(cobol_fields)`
- L69: `if not host_name`

### `DclgenColumnMerger._usable_host_fields` - L88-L103

```python
_usable_host_fields(self, cobol_fields: list[dict[str, str]]) -> list[dict[str, str]]
```

Observed calls (lexical order): `field.get`, `str`, `str(field.get('name', '')).upper`, `any`, `name.endswith`, `output.append`.

Control points:

- L93: `for field in cobol_fields`
- L95: `if not name`
- L97: `if any((name.endswith(suffix) for suffix in DCLGEN_HOST_FIELD_SUFFIXES_TO_IGNORE))`

### `DclgenColumnMerger._best_host_for_column` - L105-L136

```python
_best_host_for_column(self, column_name: str, index: int, usable_hosts: list[dict[str, str]]) -> dict[str, str]
```

Observed calls (lexical order): `self.names.normalize_compare_name`, `host.get`, `len`, `NameNormalizer.to_cobol`.

Control points:

- L113: `for host in usable_hosts`
- L117: `if host_name == normalized_column`
- L120: `for host in usable_hosts`
- L124: `if normalized_column and normalized_column in host_name`
- L126: `if host_name and host_name in normalized_column`
- L129: `if index < len(usable_hosts)`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
