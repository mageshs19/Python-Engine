# `converter/generators/initialization/paragraph_index.py`

Source: [converter/generators/initialization/paragraph_index.py](../../../../../converter/generators/initialization/paragraph_index.py) | 107 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `bbe7b22a9da9071144da2fa06a7735b4f58a7bb4237e61f3f8ceab41127eadc9`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`MAINLINE_NAME` (L14), `__all__` (L107)

## Import declarations

```python
from __future__ import annotations
from typing import List, Tuple
from converter.generators.initialization.line_geometry import LineGeometry
from patterns.initialization_scope_patterns import DIVISION_PATTERN, PARAGRAPH_HEADER_PATTERN, PROCEDURE_DIVISION_PATTERN, SECTION_HEADER_PATTERN
from rules.initialization_placement_rules import NON_PARAGRAPH_WORDS
```

## Local dependency notes

- [converter/generators/initialization/line_geometry.py](line_geometry.md)
- [patterns/initialization_scope_patterns.py](../../../patterns/initialization_scope_patterns.md)
- [rules/initialization_placement_rules.py](../../../rules/initialization_placement_rules.md)

## Importers (6)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/enhancement/output_validator.py](../enhancement/output_validator.md)
- [converter/generators/initialization/__init__.py](__init__.md)
- [converter/generators/initialization/cursor_scope_scanner.py](cursor_scope_scanner.md)
- [converter/generators/initialization/legacy_paragraph_remover.py](legacy_paragraph_remover.md)
- [converter/generators/initialization/population_site_scanner.py](population_site_scanner.md)
- [converter/generators/initialization/scope_initializer.py](scope_initializer.md)

## Symbol contracts and control points

### `ParagraphIndex` - L17-L104

```python
class ParagraphIndex()
```

### `ParagraphIndex.__init__` - L19-L20

```python
__init__(self, geometry: LineGeometry | None=None) -> None
```

Observed calls (lexical order): `LineGeometry`.

### `ParagraphIndex.is_paragraph_header` - L22-L33

```python
is_paragraph_header(self, line: str) -> bool
```

Observed calls (lexical order): `self.geometry.is_comment_or_blank`, `self.geometry.body`, `DIVISION_PATTERN.match`, `SECTION_HEADER_PATTERN.match`, `PARAGRAPH_HEADER_PATTERN.match`, `match.group`, `match.group('name').upper`.

Control points:

- L23: `if self.geometry.is_comment_or_blank(line)`
- L26: `if DIVISION_PATTERN.match(body)`
- L28: `if SECTION_HEADER_PATTERN.match(body)`
- L31: `if not match`

### `ParagraphIndex.paragraph_name` - L35-L41

```python
paragraph_name(self, line: str) -> str
```

Observed calls (lexical order): `self.geometry.body`, `PARAGRAPH_HEADER_PATTERN.match`, `SECTION_HEADER_PATTERN.match`, `match.group`, `match.group('name').upper`.

### `ParagraphIndex.procedure_division_index` - L43-L49

```python
procedure_division_index(self, lines: List[str]) -> int
```

Observed calls (lexical order): `enumerate`, `self.geometry.is_comment_or_blank`, `PROCEDURE_DIVISION_PATTERN.match`, `self.geometry.body`.

Control points:

- L44: `for (index, line) in enumerate(lines)`
- L45: `if self.geometry.is_comment_or_blank(line)`
- L47: `if PROCEDURE_DIVISION_PATTERN.match(self.geometry.body(line))`

### `ParagraphIndex.first_statement_index` - L51-L55

```python
first_statement_index(self, lines: List[str], after: int) -> int
```

Observed calls (lexical order): `len`, `range`, `self.geometry.is_comment_or_blank`.

Control points:

- L52: `for index in range(after + 1, len(lines))`
- L53: `if not self.geometry.is_comment_or_blank(lines[index])`

### `ParagraphIndex.headers` - L57-L62

```python
headers(self, lines: List[str]) -> List[Tuple[int, str]]
```

Observed calls (lexical order): `self.paragraph_name`, `enumerate`, `self.is_paragraph_header`.

### `ParagraphIndex.header_index` - L64-L69

```python
header_index(self, lines: List[str], name: str) -> int
```

Observed calls (lexical order): `str`, `str(name or '').upper`, `self.headers`.

Control points:

- L66: `for (index, header) in self.headers(lines)`
- L67: `if header == target`

### `ParagraphIndex.span_of` - L71-L77

```python
span_of(self, lines: List[str], start: int) -> Tuple[int, int]
```

Observed calls (lexical order): `len`, `range`, `self.is_paragraph_header`.

Control points:

- L72: `if start < 0 or start >= len(lines)`
- L74: `for index in range(start + 1, len(lines))`
- L75: `if self.is_paragraph_header(lines[index])`

### `ParagraphIndex.span_named` - L79-L80

```python
span_named(self, lines: List[str], name: str) -> Tuple[int, int]
```

Observed calls (lexical order): `self.header_index`, `self.span_of`.

### `ParagraphIndex.mainline_span` - L82-L89

```python
mainline_span(self, lines: List[str]) -> Tuple[int, int]
```

Observed calls (lexical order): `self.procedure_division_index`, `len`, `range`, `self.is_paragraph_header`.

Control points:

- L84: `if start < 0`
- L86: `for index in range(start + 1, len(lines))`
- L87: `if self.is_paragraph_header(lines[index])`

### `ParagraphIndex.owner_of` - L91-L101

```python
owner_of(self, lines: List[str], index: int) -> str
```

Observed calls (lexical order): `len`, `range`, `self.is_paragraph_header`, `self.paragraph_name`, `PROCEDURE_DIVISION_PATTERN.match`, `self.geometry.body`.

Control points:

- L92: `if index < 0 or index >= len(lines)`
- L94: `for position in range(index, -1, -1)`
- L95: `if self.is_paragraph_header(lines[position])`
- L97: `if PROCEDURE_DIVISION_PATTERN.match(self.geometry.body(lines[position]))`

### `ParagraphIndex.is_mainline` - L103-L104

```python
is_mainline(self, lines: List[str], index: int) -> bool
```

Observed calls (lexical order): `self.owner_of`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
