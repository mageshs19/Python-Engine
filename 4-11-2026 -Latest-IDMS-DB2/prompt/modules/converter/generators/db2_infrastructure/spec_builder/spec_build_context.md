# `converter/generators/db2_infrastructure/spec_builder/spec_build_context.py`

Source: [converter/generators/db2_infrastructure/spec_builder/spec_build_context.py](../../../../../../converter/generators/db2_infrastructure/spec_builder/spec_build_context.py) | 41 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `101972d644282cf213507b90a0d15f6226e3917a12f0253c744201a682d514a3`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Immutable input collected once for one cursor-spec build run.

## Module-level bindings

`__all__` (L41)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass
from converter.domain.models import IdmsOperation
```

## Local dependency notes

- [converter/domain/models.py](../../../domain/models.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure/spec_builder/cursor_spec_builder.py](cursor_spec_builder.md)
- [converter/generators/db2_infrastructure/spec_builder/spec_factory.py](spec_factory.md)
- [tests/spec_builder/test_cursor_spec_builder_lrf_extra_filters.py](../../../../tests/spec_builder/test_cursor_spec_builder_lrf_extra_filters.md)

## Symbol contracts and control points

### `SpecBuildContext` - L11-L38

```python
class SpecBuildContext()
```

Inputs shared by all cursor specifications in one program.

Declared class/data-model fields:

```python
operations: list[IdmsOperation]
field_usage_analysis: object
navigated_records: set[str]
materialised_records: set[str]
lrf_cursors: dict
```

### `SpecBuildContext.create` - L21-L38

```python
create(cls, operations: list[IdmsOperation] | None, cobol_text: str, field_usage_analysis, navigation, lrf, lrf_source_text: str | None=None) -> 'SpecBuildContext'
```

Observed calls (lexical order): `cls`, `list`, `navigation.navigated_records`, `navigation.materialised_records`, `lrf.cursors`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
