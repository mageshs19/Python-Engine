# `review/engine/cursors.py`

Source: [review/engine/cursors.py](../../../../review/engine/cursors.py) | 243 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `324da839b252701227e7ef22b141a07ad0bb79fde9a4da9a2bfea5c4742a2dbd`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Shared cursor parsing for checks.

## Module-level bindings

`DECLARE` (L42), `PARAGRAPH` (L45), `PERFORM` (L50), `CURSOR_VERB` (L53), `SCOPE_TERMINATORS` (L61), `__all__` (L229)

## Import declarations

```python
from __future__ import annotations
import re
from dataclasses import dataclass
from review.engine import sql_blocks as sql
```

## Local dependency notes

- [review/engine/__init__.py](__init__.md)
- [review/engine/sql_blocks.py](sql_blocks.md)

## Importers (8)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [review/checks/chk_12_cursor_declaration.py](../checks/chk_12_cursor_declaration.md)
- [review/checks/chk_13_cursor_paragraph_structure.py](../checks/chk_13_cursor_paragraph_structure.md)
- [review/checks/chk_14_end_of_cursor_handling.py](../checks/chk_14_end_of_cursor_handling.md)
- [review/checks/chk_15_nested_cursor_processing.py](../checks/chk_15_nested_cursor_processing.md)
- [review/checks/chk_21_where_clause_child_cursor.py](../checks/chk_21_where_clause_child_cursor.md)
- [review/checks/chk_26_order_by_logic_python.py](../checks/chk_26_order_by_logic_python.md)
- [review/checks/chk_27_cursor_lifecycle.py](../checks/chk_27_cursor_lifecycle.md)
- [review/checks/chk_33_doubly_driven_paragraph.py](../checks/chk_33_doubly_driven_paragraph.md)

## Symbol contracts and control points

### `CursorParagraph` - L69-L88

```python
class CursorParagraph()
```

One generated cursor paragraph header.

Declared class/data-model fields:

```python
number: int
operation: str
cursor: str
line_number: int
name: str
```

### `CursorParagraph.render` - L78-L79

```python
render(self) -> str
```

Observed calls (lexical order): `str`.

### `CursorParagraph.__str__` - L81-L88

```python
__str__(self) -> str
```

One readable evidence line.

### `declared_cursors` - L91-L100

```python
declared_cursors(view) -> dict[str, sql.SqlBlock]
```

Cursor name -> its DECLARE block.

Observed calls (lexical order): `sql.sql_blocks`, `DECLARE.search`, `match.group`, `match.group('cursor').upper`, `out.setdefault`.

Control points:

- L94: `for block in sql.sql_blocks(view)`
- L95: `if block.verb != 'DECLARE'`
- L98: `if match`

### `declare_blocks` - L103-L104

```python
declare_blocks(view) -> list[sql.SqlBlock]
```

Observed calls (lexical order): `sql.sql_blocks`.

### `cursor_paragraphs` - L107-L122

```python
cursor_paragraphs(view) -> list[CursorParagraph]
```

Every generated cursor paragraph header, in source order.

Observed calls (lexical order): `sql.norm`, `PARAGRAPH.match`, `CursorParagraph`, `out.append`, `int`, `match.group`, `match.group('operation').upper`, `match.group('cursor').upper`, `logical.rstrip`.

Control points:

- L110: `for line in view.code`
- L113: `if not match`

### `paragraph_sets` - L125-L130

```python
paragraph_sets(view) -> dict[str, dict[str, CursorParagraph]]
```

Cursor name -> {OPEN: para, FETCH: para, CLOSE: para}.

Observed calls (lexical order): `cursor_paragraphs`, `out.setdefault`.

Control points:

- L128: `for para in cursor_paragraphs(view)`

### `performed_names` - L133-L140

```python
performed_names(view) -> dict[str, list]
```

Performed paragraph name -> the lines that perform it.

Observed calls (lexical order): `PERFORM.match`, `sql.norm`, `match.group`, `match.group('name').upper`, `out.setdefault`, `out.setdefault(match.group('name').upper(), []).append`.

Control points:

- L136: `for line in view.code`
- L138: `if match`

### `cursors_used` - L143-L153

```python
cursors_used(view, operation: str) -> set[str]
```

Cursor names appearing in an EXEC SQL OPEN / FETCH / CLOSE.

Observed calls (lexical order): `str`, `str(operation or '').upper`, `set`, `sql.sql_blocks`, `CURSOR_VERB.search`, `match.group`, `match.group('cursor').upper`, `out.add`.

Control points:

- L147: `for block in sql.sql_blocks(view)`
- L148: `if block.verb != wanted`
- L151: `if match`

### `open_statements` - L156-L163

```python
open_statements(view) -> list[sql.SqlBlock]
```

Every EXEC SQL OPEN block, in source order.

Observed calls (lexical order): `sql.sql_blocks`.

### `close_statements` - L166-L173

```python
close_statements(view) -> list[sql.SqlBlock]
```

Every EXEC SQL CLOSE block, in source order.

Observed calls (lexical order): `sql.sql_blocks`.

### `cursor_name` - L176-L183

```python
cursor_name(block) -> str
```

The cursor named by an OPEN / FETCH / CLOSE block.

Observed calls (lexical order): `CURSOR_VERB.search`, `getattr`, `match.group`, `match.group('cursor').upper`.

### `is_paragraph_header` - L186-L201

```python
is_paragraph_header(logical: str, stop_words) -> bool
```

A single word plus a period that is not a scope terminator.

Observed calls (lexical order): `str`, `str(logical or '').strip`, `text.endswith`, `frozenset`.

Control points:

- L194: `if not text.endswith('.') or ' ' in text`
- L197: `if not name`
- L199: `if name in SCOPE_TERMINATORS`

### `paragraph_body` - L204-L226

```python
paragraph_body(view, para: CursorParagraph, stop_words=None) -> list[str]
```

Normalised lines of a paragraph, up to the next paragraph header.

Observed calls (lexical order): `frozenset`, `next`, `enumerate`, `sql.norm`, `PARAGRAPH.match`, `is_paragraph_header`, `out.append`.

Control points:

- L215: `if start < 0`
- L219: `for line in code[start + 1:]`
- L221: `if PARAGRAPH.match(logical)`
- L223: `if is_paragraph_header(logical, words)`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
