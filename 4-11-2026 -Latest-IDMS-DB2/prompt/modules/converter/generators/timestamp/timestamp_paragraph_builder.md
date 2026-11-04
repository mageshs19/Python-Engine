# `converter/generators/timestamp/timestamp_paragraph_builder.py`

Source: [converter/generators/timestamp/timestamp_paragraph_builder.py](../../../../../converter/generators/timestamp/timestamp_paragraph_builder.py) | 164 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `701feac658cd4c587ee23e1939df32898405eebbe672c6908297d358cd934c97`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`SOURCE_MOVE_PREFIX` (L26), `__all__` (L164)

## Import declarations

```python
from __future__ import annotations
from typing import List
import re
from converter.generators.initialization.line_geometry import LineGeometry
from converter.generators.timestamp.timestamp_anchors import NOT_FOUND, TimestampAnchors
from rules.timestamp_audit_rules import EMIT_TIMESTAMP_DEBUG_LINE, TIMESTAMP_MESSAGES, TIMESTAMP_MOVE_ALIGN_COLUMN, TIMESTAMP_MOVE_FIELDS, TIMESTAMP_PARAGRAPH_DEBUG_TEMPLATE, TIMESTAMP_PARAGRAPH_DISPLAY, TIMESTAMP_PARAGRAPH_FIELD_MOVE_TEMPLATE, TIMESTAMP_PARAGRAPH_HEADER_TEMPLATE, TIMESTAMP_PARAGRAPH_NAME, TIMESTAMP_PARAGRAPH_SOURCE_MOVE, TIMESTAMP_PARAGRAPH_TERMINATOR, TIMESTAMP_PERFORM_TEMPLATE
```

## Local dependency notes

- [converter/generators/initialization/line_geometry.py](../initialization/line_geometry.md)
- [converter/generators/timestamp/timestamp_anchors.py](timestamp_anchors.md)
- [rules/timestamp_audit_rules.py](../../../rules/timestamp_audit_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/timestamp/__init__.py](__init__.md)
- [converter/generators/timestamp_generator.py](../timestamp_generator.md)
- [tests/test_generic_final_sql_location_and_timestamp_regression.py](../../../tests/test_generic_final_sql_location_and_timestamp_regression.md)

## Symbol contracts and control points

### `TimestampParagraphBuilder` - L29-L161

```python
class TimestampParagraphBuilder()
```

### `TimestampParagraphBuilder.__init__` - L31-L40

```python
__init__(self, geometry: LineGeometry | None=None, anchors: TimestampAnchors | None=None, paragraph_name: str=TIMESTAMP_PARAGRAPH_NAME) -> None
```

Observed calls (lexical order): `LineGeometry`, `TimestampAnchors`.

### `TimestampParagraphBuilder.block` - L42-L59

```python
block(self) -> List[str]
```

Observed calls (lexical order): `TIMESTAMP_PARAGRAPH_HEADER_TEMPLATE.format`, `lines.append`, `TIMESTAMP_PARAGRAPH_DEBUG_TEMPLATE.format`, `self._move_line`.

Control points:

- L48: `if EMIT_TIMESTAMP_DEBUG_LINE`
- L55: `for field in TIMESTAMP_MOVE_FIELDS`

### `TimestampParagraphBuilder.ensure_paragraph` - L61-L76

```python
ensure_paragraph(self, lines: List[str]) -> List[str]
```

Observed calls (lexical order): `self.anchors.has_paragraph`, `self._log`, `list`, `self.block`, `self.anchors.paragraph_insert_index`, `len`.

Control points:

- L64: `if self.anchors.has_paragraph(lines, self.paragraph_name)`
- L73: `if index >= len(lines)`

### `TimestampParagraphBuilder.ensure_perform` - L78-L99

```python
ensure_perform(self, lines: List[str]) -> List[str]
```

Observed calls (lexical order): `self.anchors.perform_count`, `self._log`, `list`, `self.anchors.procedure_division_index`, `self._initialization_entry`, `self.anchors.first_statement_index`, `TIMESTAMP_PERFORM_TEMPLATE.format`.

Control points:

- L81: `if self.anchors.perform_count(lines, self.paragraph_name) > 0`
- L86: `if division == NOT_FOUND`
- L90: `if index == NOT_FOUND`
- L92: `if index == NOT_FOUND`

### `TimestampParagraphBuilder._initialization_entry` - L101-L144

```python
_initialization_entry(self, lines: List[str], division: int) -> int
```

Put timestamp in a proven, mainline-performed initialization paragraph.

Observed calls (lexical order): `len`, `range`, `self.geometry.is_comment_or_blank`, `str`, `self.geometry.body`, `self.geometry.body(raw).strip`, `self.geometry.body(raw).strip().upper`, `raw[:6].isdigit`, `area.lstrip`, `re.fullmatch`, `match.group`, `match.group(1).startswith`, `names.append`, `re.search`, `name.endswith`, `' '.join`.
Another 2 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L112: `for index in range(division + 1, len(lines))`
- L113: `if self.geometry.is_comment_or_blank(lines[index])`
- L118: `if len(area) - len(area.lstrip()) > 3`
- L121: `if match and (not match.group(1).startswith('END-'))`
- L123: `if len(names) < 2`
- L129: `if len(init_candidates) != 1`
- L138: `if not re.search('\\bPERFORM\\s+' + re.escape(init_name) + '\\b', main_code)`
- L140: `if init_index <= main_end - 1`

### `TimestampParagraphBuilder._move_line` - L146-L152

```python
_move_line(self, field: str) -> str
```

Observed calls (lexical order): `SOURCE_MOVE_PREFIX.format`, `len`, `max`, `TIMESTAMP_PARAGRAPH_FIELD_MOVE_TEMPLATE.format`.

### `TimestampParagraphBuilder._log` - L154-L161

```python
_log(self, key: str, **values) -> None
```

Observed calls (lexical order): `TIMESTAMP_MESSAGES.get`, `str`, `self.messages.append`, `template.format`.

Control points:

- L156: `if not template`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
