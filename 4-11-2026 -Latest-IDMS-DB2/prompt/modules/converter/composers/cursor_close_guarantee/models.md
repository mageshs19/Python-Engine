# `converter/composers/cursor_close_guarantee/models.py`

Source: [converter/composers/cursor_close_guarantee/models.py](../../../../../converter/composers/cursor_close_guarantee/models.py) | 97 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `1285da2d3297399e1e0beacc9bbf07a88d6f30f4ef6cdb8d062ce526e5c6f728`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Value objects for the cursor close-guarantee pass.

## Module-level bindings

`UNTIL_KEYWORD` (L21), `__all__` (L91)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass, field
from rules.cursor_close_guarantee_rules import OPERATION_CLOSE, OPERATION_FETCH, OPERATION_OPEN, REQUIRED_OPERATIONS
```

## Local dependency notes

- [rules/cursor_close_guarantee_rules.py](../../../rules/cursor_close_guarantee_rules.md)

## Importers (8)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cursor_close_guarantee/__init__.py](__init__.md)
- [converter/composers/cursor_close_guarantee/business_paragraph_resolver.py](business_paragraph_resolver.md)
- [converter/composers/cursor_close_guarantee/close_guarantor.py](close_guarantor.md)
- [converter/composers/cursor_close_guarantee/condition_normaliser.py](condition_normaliser.md)
- [converter/composers/cursor_close_guarantee/cursor_scanner.py](cursor_scanner.md)
- [converter/composers/cursor_close_guarantee/loop_finder.py](loop_finder.md)
- [converter/composers/cursor_close_guarantee/loop_synthesiser.py](loop_synthesiser.md)
- [converter/composers/cursor_close_guarantee/paragraph_index.py](paragraph_index.md)

## Symbol contracts and control points

### `ParagraphHeader` - L25-L29

```python
class ParagraphHeader()
```

One paragraph header line in the generated program.

Declared class/data-model fields:

```python
index: int = -1
name: str = ''
```

### `CursorParagraphSet` - L33-L59

```python
class CursorParagraphSet()
```

The generated OPEN / FETCH / CLOSE paragraph names of one cursor.

Declared class/data-model fields:

```python
cursor: str = ''
names: dict = field(default_factory=dict)
```

### `CursorParagraphSet.is_complete` - L40-L43

```python
is_complete(self) -> bool
```

Observed calls (lexical order): `all`.

### `CursorParagraphSet.open_name` - L46-L47

```python
open_name(self) -> str
```

Observed calls (lexical order): `self.names.get`.

### `CursorParagraphSet.fetch_name` - L50-L51

```python
fetch_name(self) -> str
```

Observed calls (lexical order): `self.names.get`.

### `CursorParagraphSet.close_name` - L54-L55

```python
close_name(self) -> str
```

Observed calls (lexical order): `self.names.get`.

### `CursorParagraphSet.remember` - L57-L59

```python
remember(self, operation: str, name: str) -> None
```

First occurrence wins; a duplicate header is never honoured.

Observed calls (lexical order): `self.names.setdefault`.

### `CursorPerform` - L63-L73

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

### `CursorPerform.has_until` - L72-L73

```python
has_until(self) -> bool
```

Observed calls (lexical order): `str`, `str(self.tail or '').upper`.

### `LoopShape` - L77-L88

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

### `LoopShape.has_condition` - L87-L88

```python
has_condition(self) -> bool
```

Observed calls (lexical order): `bool`, `str`, `str(self.condition or '').strip`.

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
