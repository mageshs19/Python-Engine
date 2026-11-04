# `converter/composers/cursor_guarantee/cursor_models.py`

Source: [converter/composers/cursor_guarantee/cursor_models.py](../../../../../converter/composers/cursor_guarantee/cursor_models.py) | 238 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `559e53ae573101c0a5988d942be32452daf7dd9b0991a8f56a37ec0eb592daaa`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Regex, value objects and the diagnostic log. The passive parts.

## Module-level bindings

`COMMENT_INDICATORS` (L37), `UNTIL_KEYWORD` (L38), `PARAGRAPH_NAME_TEMPLATE` (L41), `_NAME` (L51), `PARAGRAPH_HEADER_PATTERN` (L53), `SECTION_HEADER_PATTERN` (L58), `CURSOR_PARAGRAPH_HEADER_PATTERN` (L64), `PERFORM_CURSOR_PARAGRAPH_PATTERN` (L76), `PERFORM_PARAGRAPH_PATTERN` (L84), `PERFORM_INLINE_WITH_UNTIL_PATTERN` (L89), `PERFORM_SPAN_PATTERN` (L95), `PERFORM_SPAN_WITH_UNTIL_PATTERN` (L101), `UNTIL_ONLY_PATTERN` (L108), `WHEN_ZERO_PATTERN` (L113), `CONTINUE_PATTERN` (L118), `__all__` (L218)

## Import declarations

```python
from __future__ import annotations
import re
from dataclasses import dataclass, field
from rules.cursor_close_guarantee_rules import CURSOR_CLOSE_GUARANTEE_MESSAGES, OPERATION_CLOSE, OPERATION_FETCH, OPERATION_OPEN, REQUIRED_OPERATIONS
```

## Local dependency notes

- [rules/cursor_close_guarantee_rules.py](../../../rules/cursor_close_guarantee_rules.md)

## Importers (6)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cursor_close_guarantee_composer.py](../cursor_close_guarantee_composer.md)
- [converter/composers/cursor_guarantee/__init__.py](__init__.md)
- [converter/composers/cursor_guarantee/cursor_lines.py](cursor_lines.md)
- [converter/composers/cursor_guarantee/cursor_repair.py](cursor_repair.md)
- [converter/composers/cursor_guarantee/cursor_scanner.py](cursor_scanner.md)
- [tests/pipeline/test_single_owner_transformations.py](../../../tests/pipeline/test_single_owner_transformations.md)

## Symbol contracts and control points

### `ParagraphHeader` - L128-L132

```python
class ParagraphHeader()
```

One paragraph header line.

Declared class/data-model fields:

```python
index: int = -1
name: str = ''
```

### `CursorParagraphSet` - L136-L156

```python
class CursorParagraphSet()
```

The OPEN / FETCH / CLOSE paragraph names of one cursor.

Declared class/data-model fields:

```python
cursor: str = ''
names: dict = field(default_factory=dict)
```

### `CursorParagraphSet.is_complete` - L143-L144

```python
is_complete(self) -> bool
```

Observed calls (lexical order): `all`.

### `CursorParagraphSet.open_name` - L147-L148

```python
open_name(self) -> str
```

Observed calls (lexical order): `self.names.get`.

### `CursorParagraphSet.fetch_name` - L151-L152

```python
fetch_name(self) -> str
```

Observed calls (lexical order): `self.names.get`.

### `CursorParagraphSet.close_name` - L155-L156

```python
close_name(self) -> str
```

Observed calls (lexical order): `self.names.get`.

### `CursorPerform` - L160-L170

```python
class CursorPerform()
```

One PERFORM of a generated cursor paragraph.

Declared class/data-model fields:

```python
index: int = -1
operation: str = ''
paragraph: str = ''
tail: str = ''
```

### `CursorPerform.has_until` - L169-L170

```python
has_until(self) -> bool
```

Observed calls (lexical order): `str`, `str(self.tail or '').upper`.

### `LoopShape` - L174-L185

```python
class LoopShape()
```

A business driving loop found in the generated flow.

Declared class/data-model fields:

```python
perform_index: int = -1
until_index: int = -1
end_index: int = -1
condition: str = ''
terminated: bool = False
```

### `LoopShape.has_condition` - L184-L185

```python
has_condition(self) -> bool
```

Observed calls (lexical order): `bool`, `str`, `str(self.condition or '').strip`.

### `MessageLog` - L188-L215

```python
class MessageLog()
```

Ordered diagnostics for one conversion run.

### `MessageLog.__init__` - L199-L200

```python
__init__(self) -> None
```

### `MessageLog.reset` - L202-L203

```python
reset(self) -> None
```

### `MessageLog.log` - L205-L215

```python
log(self, key: str, **values) -> None
```

Observed calls (lexical order): `CURSOR_CLOSE_GUARANTEE_MESSAGES.get`, `self.messages.append`, `template.format`.

Control points:

- L208: `if not template`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
