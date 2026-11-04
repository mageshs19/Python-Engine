# `converter/generators/db2_infrastructure/spec_builder/spec_navigation_scanner.py`

Source: [converter/generators/db2_infrastructure/spec_builder/spec_navigation_scanner.py](../../../../../../converter/generators/db2_infrastructure/spec_builder/spec_navigation_scanner.py) | 73 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `d43d604df2ca7f059b6e4d6a4a05660ae1dd41a2c86b3ddde5084cb1116e2084`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Which records does this program position, and which are copied whole?

## Module-level bindings

`NAVIGATION_VERB_PREFIXES` (L18), `__all__` (L73)

## Import declarations

```python
from __future__ import annotations
from converter.domain.models import IdmsOperation
from converter.generators.db2_infrastructure.spec_builder.spec_fixed_format import bodies_of
from converter.services.name_normalizer import NameNormalizer
from patterns.record_materialisation_patterns import WHOLE_RECORD_MOVE_PATTERN
```

## Local dependency notes

- [converter/domain/models.py](../../../domain/models.md)
- [converter/generators/db2_infrastructure/spec_builder/spec_fixed_format.py](spec_fixed_format.md)
- [converter/services/name_normalizer.py](../../../services/name_normalizer.md)
- [patterns/record_materialisation_patterns.py](../../../../patterns/record_materialisation_patterns.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure/spec_builder/cursor_spec_builder.py](cursor_spec_builder.md)
- [tests/spec_builder/test_cursor_spec_builder_lrf_extra_filters.py](../../../../tests/spec_builder/test_cursor_spec_builder_lrf_extra_filters.md)

## Symbol contracts and control points

### `SpecNavigationScanner` - L21-L70

```python
class SpecNavigationScanner()
```

Read-only program scans.

### `SpecNavigationScanner.navigated_records` - L25-L45

```python
navigated_records(operations: list[IdmsOperation] | None) -> set[str]
```

Records positioned by an OBTAIN/FIND anywhere in the program.

Observed calls (lexical order): `set`, `getattr`, `str`, `str(getattr(operation, 'operation', '') or '').upper`, `verb.startswith`, `NameNormalizer.normalize`, `records.add`.

Control points:

- L34: `for operation in operations or []`
- L36: `if not verb.startswith(NAVIGATION_VERB_PREFIXES)`
- L42: `if record`

### `SpecNavigationScanner.materialised_records` - L48-L70

```python
materialised_records(cobol_text: str) -> set[str]
```

Records copied whole via 'MOVE <record> TO <target>'.

Observed calls (lexical order): `set`, `bodies_of`, `WHOLE_RECORD_MOVE_PATTERN.match`, `NameNormalizer.normalize`, `match.group`, `records.add`.

Control points:

- L58: `for body in bodies_of(cobol_text)`
- L59: `if not body`
- L63: `if not match`
- L67: `if record`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
