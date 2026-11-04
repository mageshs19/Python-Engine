# `review/engine/statements.py`

Source: [review/engine/statements.py](../../../../review/engine/statements.py) | 77 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `35a9d77a5154125bc9c66d2f12cf462327bf01a84eded2ac295381cb17c23eb0`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Joins COBOL statements that span several physical lines.

## Module-level bindings

`MAX_CONTINUATION_LINES` (L31), `SENTENCE_TERMINATOR` (L32), `__all__` (L77)

## Import declarations

```python
from __future__ import annotations
from review.engine import sql_blocks as sql
from review.standards import cobol_standards as std
```

## Local dependency notes

- [review/engine/__init__.py](__init__.md)
- [review/engine/sql_blocks.py](sql_blocks.md)
- [review/standards/__init__.py](../standards/__init__.md)
- [review/standards/cobol_standards.py](../standards/cobol_standards.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [review/checks/chk_15_nested_cursor_processing.py](../checks/chk_15_nested_cursor_processing.md)
- [review/checks/chk_33_doubly_driven_paragraph.py](../checks/chk_33_doubly_driven_paragraph.md)

## Symbol contracts and control points

### `_starts_statement` - L35-L41

```python
_starts_statement(text: str) -> bool
```

Observed calls (lexical order): `text.split`, `text.split()[0].rstrip`, `text.split()[0].rstrip(SENTENCE_TERMINATOR).upper`, `text.rstrip`, `text.rstrip().endswith`.

Control points:

- L36: `if not text`
- L39: `if word in std.NON_PARAGRAPH_WORDS`

### `joined_statements` - L44-L74

```python
joined_statements(view) -> list[tuple[int, str]]
```

\[(index of first physical line, whole statement text), ...\].

Observed calls (lexical order): `enumerate`, `sql.norm`, `_starts_statement`, `len`, `' '.join`, `out.append`, `buffer.append`, `text.rstrip`, `text.rstrip().endswith`.

Control points:

- L53: `for (index, line) in enumerate(view.code)`
- L55: `if not text`
- L58: `if not buffer or _starts_statement(text) or len(buffer) > MAX_CONTINUATION_LINES`
- L61: `if buffer`
- L67: `if text.rstrip().endswith(SENTENCE_TERMINATOR)`
- L71: `if buffer`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
