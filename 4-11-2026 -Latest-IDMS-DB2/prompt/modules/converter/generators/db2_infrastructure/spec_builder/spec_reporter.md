# `converter/generators/db2_infrastructure/spec_builder/spec_reporter.py`

Source: [converter/generators/db2_infrastructure/spec_builder/spec_reporter.py](../../../../../../converter/generators/db2_infrastructure/spec_builder/spec_reporter.py) | 70 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `4698593b60c67213f257e6712a2cf06f9705d2ca947362908f3d3a2d28b47941`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Include names and spec-quality diagnostics.

## Module-level bindings

`__all__` (L70)

## Import declarations

```python
from __future__ import annotations
from converter.services.name_normalizer import NameNormalizer
from rules.cursor_spec import SPEC_CURSOR_NAME, SPEC_HOST_VARIABLES, SPEC_MESSAGES, SPEC_RECORD_NAME, SPEC_SELECT_COLUMNS, SPEC_TABLE_NAME
```

## Local dependency notes

- [converter/services/name_normalizer.py](../../../services/name_normalizer.md)
- [rules/cursor_spec/__init__.py](../../../../rules/cursor_spec/__init__.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure/spec_builder/cursor_spec_builder.py](cursor_spec_builder.md)

## Symbol contracts and control points

### `SpecReporter` - L18-L67

```python
class SpecReporter()
```

Reads finished specs. Changes nothing.

### `SpecReporter.__init__` - L21-L22

```python
__init__(self, line_utils) -> None
```

### `SpecReporter.include_names` - L24-L42

```python
include_names(self, specs: list[dict[str, object]]) -> list[str]
```

Observed calls (lexical order): `set`, `NameNormalizer.normalize`, `spec.get`, `str`, `self.line_utils.normalize_include_name`, `seen.add`, `output.append`.

Control points:

- L28: `for spec in specs or []`
- L32: `if not table`
- L36: `if not include or include in seen`

### `SpecReporter.messages` - L45-L67

```python
messages(specs: list[dict[str, object]]) -> list[str]
```

Observed calls (lexical order): `spec.get`, `str`, `SPEC_MESSAGES.get`, `output.append`, `template.format`.

Control points:

- L48: `for spec in specs or []`
- L58: `for (key, value) in checks`
- L59: `if value`
- L62: `if template`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
