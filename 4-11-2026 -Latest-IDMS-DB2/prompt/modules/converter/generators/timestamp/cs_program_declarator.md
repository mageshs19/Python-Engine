# `converter/generators/timestamp/cs_program_declarator.py`

Source: [converter/generators/timestamp/cs_program_declarator.py](../../../../../converter/generators/timestamp/cs_program_declarator.py) | 116 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `2283af47df825db4f6cfb7616349b83beec4a31dd26afda64b1a5db4632b3984`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`__all__` (L116)

## Import declarations

```python
from __future__ import annotations
from typing import List
from converter.generators.initialization.diagnostics import InitializationDiagnostics
from converter.generators.initialization.line_geometry import LineGeometry
from converter.generators.timestamp.program_id_resolver import ProgramIdResolver
from converter.generators.timestamp.timestamp_anchors import TimestampAnchors
from converter.services.generated_field_anchor import GeneratedFieldAnchorResolver
from rules.timestamp_audit_rules import CS_PROGRAM_FIELD, CS_PROGRAM_NAME_COLUMN, CS_PROGRAM_PICTURE, CS_PROGRAM_PICTURE_COLUMN, CS_PROGRAM_VALUE_COLUMN, TIMESTAMP_MESSAGES
```

## Local dependency notes

- [converter/generators/initialization/diagnostics.py](../initialization/diagnostics.md)
- [converter/generators/initialization/line_geometry.py](../initialization/line_geometry.md)
- [converter/generators/timestamp/program_id_resolver.py](program_id_resolver.md)
- [converter/generators/timestamp/timestamp_anchors.py](timestamp_anchors.md)
- [converter/services/generated_field_anchor.py](../../services/generated_field_anchor.md)
- [rules/timestamp_audit_rules.py](../../../rules/timestamp_audit_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/timestamp/__init__.py](__init__.md)
- [converter/generators/timestamp_generator.py](../timestamp_generator.md)
- [tests/generated_fields/conftest.py](../../../tests/generated_fields/conftest.md)

## Symbol contracts and control points

### `CsProgramDeclarator` - L28-L113

```python
class CsProgramDeclarator()
```

### `CsProgramDeclarator.__init__` - L30-L43

```python
__init__(self, diagnostics=None, geometry: LineGeometry | None=None, anchors: TimestampAnchors | None=None, field_anchor: GeneratedFieldAnchorResolver | None=None, program_ids: ProgramIdResolver | None=None) -> None
```

Observed calls (lexical order): `InitializationDiagnostics`, `LineGeometry`, `TimestampAnchors`, `GeneratedFieldAnchorResolver`, `ProgramIdResolver`.

### `CsProgramDeclarator.declare` - L45-L87

```python
declare(self, lines: List[str], target_program_id: str) -> List[str]
```

Observed calls (lexical order): `self.anchors.declaration_level`, `self._log`, `list`, `self.program_ids.resolve_with_fallback`, `self.anchors.bodies`, `self.field_anchor.resolve`, `self.messages.append`, `self.diagnostics.messages.append`, `self._render`.

Control points:

- L53: `if existing`
- L67: `for message in self.field_anchor.messages`
- L71: `if not anchor.is_usable`

### `CsProgramDeclarator._render` - L89-L96

```python
_render(self, level: str, indent: str, program_id: str) -> str
```

Observed calls (lexical order): `self.program_ids.padded`, `self._pad`, `str`.

### `CsProgramDeclarator._pad` - L99-L102

```python
_pad(text: str, column: int) -> str
```

Observed calls (lexical order): `str`, `int`, `len`, `max`.

### `CsProgramDeclarator._log` - L104-L113

```python
_log(self, key: str, **values) -> None
```

Observed calls (lexical order): `TIMESTAMP_MESSAGES.get`, `str`, `template.format`, `self.messages.append`, `self.diagnostics.messages.append`.

Control points:

- L106: `if not template`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
