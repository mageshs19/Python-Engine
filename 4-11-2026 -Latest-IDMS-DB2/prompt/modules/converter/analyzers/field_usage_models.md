# `converter/analyzers/field_usage_models.py`

Source: [converter/analyzers/field_usage_models.py](../../../../converter/analyzers/field_usage_models.py) | 20 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `5b83ca08f9b5ff30d5db1c6b2e9d9a964e7314811753f446a441bf08ca5d449c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass, field
```

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/analyzers/field_usage_analyzer.py](field_usage_analyzer.md)
- [converter/analyzers/field_usage_capture_service.py](field_usage_capture_service.md)
- [tests/test_cursor_group_projection.py](../../tests/test_cursor_group_projection.md)

## Symbol contracts and control points

### `FieldUsage` - L7-L14

```python
class FieldUsage()
```

Declared class/data-model fields:

```python
record_name: str
condition_fields: set[str] = field(default_factory=set)
output_fields: set[str] = field(default_factory=set)
move_source_fields: set[str] = field(default_factory=set)
move_target_fields: set[str] = field(default_factory=set)
dclgen_host_fields: set[str] = field(default_factory=set)
all_fields: set[str] = field(default_factory=set)
```

### `FieldUsageAnalysis` - L18-L20

```python
class FieldUsageAnalysis()
```

Declared class/data-model fields:

```python
usage_by_record: dict[str, FieldUsage] = field(default_factory=dict)
diagnostics: list[str] = field(default_factory=list)
```

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
