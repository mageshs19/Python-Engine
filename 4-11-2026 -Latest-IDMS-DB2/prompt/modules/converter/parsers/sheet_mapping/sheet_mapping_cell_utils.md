# `converter/parsers/sheet_mapping/sheet_mapping_cell_utils.py`

Source: [converter/parsers/sheet_mapping/sheet_mapping_cell_utils.py](../../../../../converter/parsers/sheet_mapping/sheet_mapping_cell_utils.py) | 34 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `ac337b62be78dabdb020e6b4d7c471b2a3c37e78b97695e6e1b28fe31d5d2f3b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from patterns.sheet_mapping_patterns import CELL_WHITESPACE_PATTERN, HEADER_NON_ALPHANUMERIC_PATTERN, HEADER_WHITESPACE_PATTERN
```

## Local dependency notes

- [patterns/sheet_mapping_patterns.py](../../../patterns/sheet_mapping_patterns.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/parsers/sheet_mapping_parser.py](../sheet_mapping_parser.md)

## Symbol contracts and control points

### `SheetMappingCellUtils` - L10-L34

```python
class SheetMappingCellUtils()
```

Cell and header text normalization helpers.

### `SheetMappingCellUtils._cell_to_string` - L17-L26

```python
_cell_to_string(self, value) -> str
```

Observed calls (lexical order): `str`, `text.replace`, `CELL_WHITESPACE_PATTERN.sub`, `text.strip`.

Control points:

- L18: `if value is None`

### `SheetMappingCellUtils._normalize_header` - L28-L34

```python
_normalize_header(self, value: str) -> str
```

Observed calls (lexical order): `self._cell_to_string`, `text.upper`, `text.replace`, `HEADER_NON_ALPHANUMERIC_PATTERN.sub`, `HEADER_WHITESPACE_PATTERN.sub`, `text.strip`.

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
