# `converter/parsers/sheet_mapping/sheet_mapping_diagnostics.py`

Source: [converter/parsers/sheet_mapping/sheet_mapping_diagnostics.py](../../../../../converter/parsers/sheet_mapping/sheet_mapping_diagnostics.py) | 28 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `726e2136dbfc6aa0d1a901b4c7346d4fb0c134bde6dae92b0d5b53053e87613f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.domain.models import SheetMappingRow
from rules.sheet_mapping_parser_rules import POPULATION_DIAGNOSTIC_SPEC, USEFUL_CONTEXT_GROUPS, USEFUL_CONTEXT_LABEL
```

## Local dependency notes

- [converter/domain/models.py](../../domain/models.md)
- [rules/sheet_mapping_parser_rules.py](../../../rules/sheet_mapping_parser_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/parsers/sheet_mapping_parser.py](../sheet_mapping_parser.md)

## Symbol contracts and control points

### `SheetMappingDiagnostics` - L11-L28

```python
class SheetMappingDiagnostics()
```

Population diagnostics driven by a spec (no per-metric repetition).

### `SheetMappingDiagnostics._add_population_diagnostics` - L14-L24

```python
_add_population_diagnostics(self, rows: list[SheetMappingRow]) -> None
```

Observed calls (lexical order): `self._any_attr_set`, `sum`, `self.diagnostics.append`, `all`.

Control points:

- L15: `for (label, attrs) in POPULATION_DIAGNOSTIC_SPEC`

### `SheetMappingDiagnostics._any_attr_set` - L27-L28

```python
_any_attr_set(row: SheetMappingRow, attrs: list[str]) -> bool
```

Observed calls (lexical order): `any`, `getattr`, `str`, `str(getattr(row, attr, '') or '').strip`.

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
