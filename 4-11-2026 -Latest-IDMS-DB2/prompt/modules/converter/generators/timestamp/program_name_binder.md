# `converter/generators/timestamp/program_name_binder.py`

Source: [converter/generators/timestamp/program_name_binder.py](../../../../../converter/generators/timestamp/program_name_binder.py) | 103 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `fd5f17439dd59a747396a5c55d921f76020fb241f8fa62a14199ce4a5e4e0893`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`STATEMENT_TERMINATOR` (L21), `__all__` (L103)

## Import declarations

```python
from __future__ import annotations
from typing import List
from converter.generators.initialization.line_geometry import LineGeometry
from converter.generators.timestamp.timestamp_anchors import TimestampAnchors
from patterns.timestamp_patterns import constant_move_pattern, literal_move_pattern
from rules.timestamp_audit_rules import CS_PROGRAM_FIELD, ENFORCE_PROGRAM_NAME_CONSTANT, PROGRAM_NAME_FIELD, PROGRAM_NAME_MOVE_TEMPLATE, TIMESTAMP_MESSAGES
```

## Local dependency notes

- [converter/generators/initialization/line_geometry.py](../initialization/line_geometry.md)
- [converter/generators/timestamp/timestamp_anchors.py](timestamp_anchors.md)
- [patterns/timestamp_patterns.py](../../../patterns/timestamp_patterns.md)
- [rules/timestamp_audit_rules.py](../../../rules/timestamp_audit_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/timestamp/__init__.py](__init__.md)
- [converter/generators/timestamp_generator.py](../timestamp_generator.md)
- [tests/generated_fields/test_program_name_binding.py](../../../tests/generated_fields/test_program_name_binding.md)

## Symbol contracts and control points

### `ProgramNameBinder` - L24-L100

```python
class ProgramNameBinder()
```

### `ProgramNameBinder.__init__` - L26-L37

```python
__init__(self, geometry: LineGeometry | None=None, anchors: TimestampAnchors | None=None) -> None
```

Observed calls (lexical order): `LineGeometry`, `TimestampAnchors`, `literal_move_pattern`, `constant_move_pattern`.

### `ProgramNameBinder.bind` - L39-L81

```python
bind(self, lines: List[str]) -> List[str]
```

Observed calls (lexical order): `list`, `self.anchors.declaration_level`, `self._log`, `self.geometry.is_comment_or_blank`, `output.append`, `self.geometry.body`, `self.constant.match`, `self.literal.match`, `self._body`, `self.geometry.replace_body`.

Control points:

- L42: `if not ENFORCE_PROGRAM_NAME_CONSTANT`
- L45: `if not self.anchors.declaration_level(lines, CS_PROGRAM_FIELD)`
- L53: `for line in lines`
- L54: `if self.geometry.is_comment_or_blank(line)`
- L60: `if self.constant.match(body)`
- L65: `if not self.literal.match(body)`
- L72: `if rewritten`
- L78: `if already`

### `ProgramNameBinder._body` - L84-L91

```python
_body(original: str) -> str
```

Observed calls (lexical order): `PROGRAM_NAME_MOVE_TEMPLATE.format`, `str`, `str(original or '').rstrip`, `str(original or '').rstrip().endswith`.

Control points:

- L89: `if str(original or '').rstrip().endswith(STATEMENT_TERMINATOR)`

### `ProgramNameBinder._log` - L93-L100

```python
_log(self, key: str, **values) -> None
```

Observed calls (lexical order): `TIMESTAMP_MESSAGES.get`, `str`, `self.messages.append`, `template.format`.

Control points:

- L95: `if not template`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
