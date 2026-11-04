# `converter/parsers/sheet_mapping/sheet_mapping_row_mapper.py`

Source: [converter/parsers/sheet_mapping/sheet_mapping_row_mapper.py](../../../../../converter/parsers/sheet_mapping/sheet_mapping_row_mapper.py) | 102 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `1293386ded9df5a889077ed4acdc304254e9d7385cb53bc72923fda2652074ab`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from catalogs.sheet_mapping_schema import SHEET_MAPPING_CANONICAL_COLUMNS, SHEET_MAPPING_FIELD_ALIASES, SHEET_MAPPING_HEADER_DETECTION_GROUPS, SHEET_MAPPING_MODEL_FIELD_MAP
from converter.domain.models import SheetMappingRow
from rules.sheet_mapping_parser_rules import DIAG_SHEET_NORMALIZED_CELLS_TEMPLATE, HEADER_DEBUG_ROW_LIMIT, HEADER_SCAN_ROW_LIMIT
```

## Local dependency notes

- [catalogs/sheet_mapping_schema.py](../../../catalogs/sheet_mapping_schema.md)
- [converter/domain/models.py](../../domain/models.md)
- [rules/sheet_mapping_parser_rules.py](../../../rules/sheet_mapping_parser_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/parsers/sheet_mapping_parser.py](../sheet_mapping_parser.md)

## Symbol contracts and control points

### `SheetMappingRowMapper` - L17-L102

```python
class SheetMappingRowMapper()
```

Header detection, row-to-dict, and dict-to-model mapping.

### `SheetMappingRowMapper._row_to_dict` - L24-L32

```python
_row_to_dict(self, headers: list[str], row: tuple) -> dict[str, str]
```

Observed calls (lexical order): `enumerate`, `self._cell_to_string`, `len`.

Control points:

- L26: `for (index, header) in enumerate(headers)`
- L28: `if not clean_header`

### `SheetMappingRowMapper._find_header_row` - L34-L71

```python
_find_header_row(self, rows: list[tuple], sheet_title: str) -> int
```

Observed calls (lexical order): `self._normalize_header`, `enumerate`, `self._cell_to_string`, `self.diagnostics.append`, `DIAG_SHEET_NORMALIZED_CELLS_TEMPLATE.format`, `sorted`, `self._row_has_any_header`.

Control points:

- L37: `for (index, row) in enumerate(rows[:HEADER_SCAN_ROW_LIMIT])`
- L44: `if index < HEADER_DEBUG_ROW_LIMIT`
- L53: `if first_canonical in normalized_cells`
- L56: `if self._row_has_any_header(normalized_cells=normalized_cells, aliases=SHEET_MAPPING_HEADER_DETECTION_GROUPS[0])`
- L62: `if self._row_has_any_header(normalized_cells=normalized_cells, aliases=SHEET_MAPPING_HEADER_DETECTION_GROUPS[1]) and self._row_has_any_header(normalized_cells=normalized_cells, ali...`

### `SheetMappingRowMapper._row_has_any_header` - L73-L78

```python
_row_has_any_header(self, normalized_cells: set[str], aliases: list[str]) -> bool
```

Observed calls (lexical order): `any`, `self._normalize_header`.

### `SheetMappingRowMapper._to_mapping_row` - L80-L85

```python
_to_mapping_row(self, raw_row: dict[str, str]) -> SheetMappingRow
```

Observed calls (lexical order): `self._get`, `SHEET_MAPPING_MODEL_FIELD_MAP.items`, `SheetMappingRow`.

### `SheetMappingRowMapper._get` - L87-L96

```python
_get(self, row: dict[str, str], canonical_name: str) -> str
```

Observed calls (lexical order): `SHEET_MAPPING_FIELD_ALIASES.get`, `row.items`, `self._normalize_header`, `normalized_lookup.get`, `str`, `str(value).strip`.

Control points:

- L92: `for alias in aliases`
- L94: `if value is not None`

### `SheetMappingRowMapper._has_useful_content` - L98-L102

```python
_has_useful_content(self, row: SheetMappingRow) -> bool
```

Observed calls (lexical order): `any`, `getattr`, `str`, `str(getattr(row, field_name) or '').strip`.

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
