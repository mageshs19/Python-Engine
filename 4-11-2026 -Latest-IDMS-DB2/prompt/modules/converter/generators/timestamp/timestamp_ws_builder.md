# `converter/generators/timestamp/timestamp_ws_builder.py`

Source: [converter/generators/timestamp/timestamp_ws_builder.py](../../../../../converter/generators/timestamp/timestamp_ws_builder.py) | 62 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `903d5777c5e8a8f4e2c61edb40ca6cf55bb6ffc4cb5b6d1bbf0e1a37547692dc`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`MARKER_LINE_TEMPLATE` (L16), `__all__` (L62)

## Import declarations

```python
from __future__ import annotations
from typing import List
from converter.generators.initialization.line_geometry import LineGeometry
from converter.generators.timestamp.timestamp_anchors import NOT_FOUND, TimestampAnchors
from rules.timestamp_audit_rules import TIMESTAMP_MESSAGES, TIMESTAMP_WS_LINES, TIMESTAMP_WS_MARKER
```

## Local dependency notes

- [converter/generators/initialization/line_geometry.py](../initialization/line_geometry.md)
- [converter/generators/timestamp/timestamp_anchors.py](timestamp_anchors.md)
- [rules/timestamp_audit_rules.py](../../../rules/timestamp_audit_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/timestamp/__init__.py](__init__.md)
- [converter/generators/timestamp_generator.py](../timestamp_generator.md)

## Symbol contracts and control points

### `TimestampWorkingStorageBuilder` - L19-L59

```python
class TimestampWorkingStorageBuilder()
```

### `TimestampWorkingStorageBuilder.__init__` - L21-L28

```python
__init__(self, geometry: LineGeometry | None=None, anchors: TimestampAnchors | None=None) -> None
```

Observed calls (lexical order): `LineGeometry`, `TimestampAnchors`.

### `TimestampWorkingStorageBuilder.block` - L30-L33

```python
block(self) -> List[str]
```

Observed calls (lexical order): `MARKER_LINE_TEMPLATE.format`, `lines.extend`.

### `TimestampWorkingStorageBuilder.ensure` - L35-L50

```python
ensure(self, lines: List[str]) -> List[str]
```

Observed calls (lexical order): `self.anchors.has_marker`, `self._log`, `list`, `self.block`, `self.anchors.working_storage_insert_index`.

Control points:

- L38: `if self.anchors.has_marker(lines, TIMESTAMP_WS_MARKER)`
- L45: `if index == NOT_FOUND`

### `TimestampWorkingStorageBuilder._log` - L52-L59

```python
_log(self, key: str, **values) -> None
```

Observed calls (lexical order): `TIMESTAMP_MESSAGES.get`, `str`, `self.messages.append`, `template.format`.

Control points:

- L54: `if not template`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
