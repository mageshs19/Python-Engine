# `converter/composers/restart/restart_injection_geometry.py`

Source: [converter/composers/restart/restart_injection_geometry.py](../../../../../converter/composers/restart/restart_injection_geometry.py) | 356 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `8101e11e082fbaeef936a786442c3a7f180c9aacd35ce4ec866bbcf1c700b090`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Where things are in a converted COBOL program.

## Module-level bindings

`END_PROGRAM` (L87), `MAINLINE_LABEL` (L88), `SCOPE_REPORT_PREFIXES` (L93), `PERFORM_VERB` (L97), `SCOPE_TERMINATOR_WORDS` (L102), `NON_PARAGRAPH_WORDS` (L127), `__all__` (L347)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass
from typing import Sequence
from patterns.restart_patterns import OPEN_INPUT_PATTERN, PARAGRAPH_HEADER_PATTERN, PROCEDURE_DIVISION_PATTERN, STOP_RUN_PATTERN
from rules.restart_cleanup_rules import NON_PARAGRAPH_DOTTED_LINES
```

## Local dependency notes

- [patterns/restart_patterns.py](../../../patterns/restart_patterns.md)
- [rules/restart_cleanup_rules.py](../../../rules/restart_cleanup_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/restart/restart_injection_composer.py](restart_injection_composer.md)

## Symbol contracts and control points

### `Span` - L142-L148

```python
class Span()
```

One paragraph: header line, first body line, first line after.

Declared class/data-model fields:

```python
name: str
header: int
start: int
end: int
```

### `RestartParagraphGeometry` - L151-L344

```python
class RestartParagraphGeometry()
```

Locates paragraphs and boundaries. Expects ``self.line_utils``.

### `RestartParagraphGeometry._logical` - L157-L166

```python
_logical(self, line: str) -> str
```

Columns 8-72, upper-cased. Comments return "".

Observed calls (lexical order): `self.line_utils.logical`, `str`, `str(self.line_utils.logical(line) or '').strip`, `self.line_utils.is_comment`, `' '.join`, `text.upper`, `text.upper().split`.

Control points:

- L164: `if not text or self.line_utils.is_comment(text)`

### `RestartParagraphGeometry._logical_any` - L168-L177

```python
_logical_any(self, line: str) -> str
```

Like _logical, but KEEPS comment lines.

Observed calls (lexical order): `self.line_utils.logical`, `str`, `str(self.line_utils.logical(line) or '').strip`, `' '.join`, `text.upper`, `text.upper().split`.

Control points:

- L175: `if not text`

### `RestartParagraphGeometry._lines` - L179-L182

```python
_lines(self, text: str) -> list[str]
```

Observed calls (lexical order): `self._has_text_helpers`, `list`, `self.line_utils.lines`, `str`, `str(text or '').splitlines`.

Control points:

- L180: `if self._has_text_helpers()`

### `RestartParagraphGeometry._join` - L184-L187

```python
_join(self, lines: list[str]) -> str
```

Observed calls (lexical order): `self._has_text_helpers`, `list`, `self.line_utils.join`, `str`, `'\n'.join`.

Control points:

- L185: `if self._has_text_helpers()`

### `RestartParagraphGeometry._has_text_helpers` - L189-L194

```python
_has_text_helpers(self) -> bool
```

Split and join must come from the SAME source or the round trip loses idempotence.

Observed calls (lexical order): `callable`, `getattr`.

### `RestartParagraphGeometry._spans` - L199-L217

```python
_spans(self, lines: list[str]) -> list[Span]
```

Observed calls (lexical order): `self._headers`, `self._insert_index`, `enumerate`, `len`, `spans.append`, `Span`, `max`, `min`.

Control points:

- L203: `for (position, (index, name)) in enumerate(headers)`

### `RestartParagraphGeometry._headers` - L219-L238

```python
_headers(self, lines: list[str]) -> list[tuple[int, str]]
```

Observed calls (lexical order): `enumerate`, `self._logical`, `PROCEDURE_DIVISION_PATTERN.match`, `PARAGRAPH_HEADER_PATTERN.match`, `match.group`, `match.group('name').upper`, `self._is_not_a_paragraph`, `found.append`.

Control points:

- L222: `for (index, line) in enumerate(lines)`
- L224: `if not logical`
- L226: `if PROCEDURE_DIVISION_PATTERN.match(logical)`
- L229: `if not started`
- L232: `if not match`
- L235: `if self._is_not_a_paragraph(name)`

### `RestartParagraphGeometry._is_not_a_paragraph` - L241-L246

```python
_is_not_a_paragraph(name: str) -> bool
```

END-EXEC. / END-IF. / EXIT. wear the header SHAPE but head nothing.

Observed calls (lexical order): `str`, `str(name or '').strip`, `str(name or '').strip().upper`, `str(name or '').strip().upper().rstrip`.

### `RestartParagraphGeometry._span_named` - L248-L255

```python
_span_named(self, lines: list[str], name: str) -> Span | None
```

Observed calls (lexical order): `str`, `str(name or '').strip`, `str(name or '').strip().upper`, `self._spans`, `span.name.upper`.

Control points:

- L250: `if not target`
- L252: `for span in self._spans(lines)`
- L253: `if span.name.upper() == target`

### `RestartParagraphGeometry._procedure_index` - L257-L262

```python
_procedure_index(self, lines: list[str]) -> int
```

Observed calls (lexical order): `enumerate`, `self._logical`, `PROCEDURE_DIVISION_PATTERN.match`.

Control points:

- L258: `for (index, line) in enumerate(lines)`
- L260: `if logical and PROCEDURE_DIVISION_PATTERN.match(logical)`

### `RestartParagraphGeometry._open_input_index` - L264-L269

```python
_open_input_index(self, lines: list[str]) -> int
```

Observed calls (lexical order): `enumerate`, `self._logical`, `OPEN_INPUT_PATTERN.match`.

Control points:

- L265: `for (index, line) in enumerate(lines)`
- L267: `if logical and OPEN_INPUT_PATTERN.match(logical)`

### `RestartParagraphGeometry._open_input_index_within` - L271-L287

```python
_open_input_index_within(self, lines: list[str], start: int, end: int) -> int
```

The OPEN INPUT line inside \[start, end), or -1.

Observed calls (lexical order): `len`, `max`, `min`, `range`, `self._logical`, `OPEN_INPUT_PATTERN.match`.

Control points:

- L283: `for index in range(max(0, start), min(end, len(lines)))`
- L285: `if logical and OPEN_INPUT_PATTERN.match(logical)`

### `RestartParagraphGeometry._termination_index` - L292-L298

```python
_termination_index(self, lines: list[str]) -> int
```

The line that terminates the program, or -1. CORRECTION C.

Observed calls (lexical order): `enumerate`, `self._logical`, `STOP_RUN_PATTERN.match`.

Control points:

- L294: `for (index, line) in enumerate(lines)`
- L296: `if logical and STOP_RUN_PATTERN.match(logical)`

### `RestartParagraphGeometry._perform_index_within` - L300-L315

```python
_perform_index_within(self, lines: list[str], start: int, end: int, paragraph: str) -> int
```

The first PERFORM of `paragraph` inside \[start, end), or -1.

Observed calls (lexical order): `str`, `str(paragraph or '').strip`, `str(paragraph or '').strip().upper`, `len`, `max`, `min`, `range`, `self._logical`, `body.startswith`.

Control points:

- L309: `if not target`
- L311: `for index in range(max(0, start), min(end, len(lines)))`
- L313: `if body.startswith(PERFORM_VERB) and target in body`

### `RestartParagraphGeometry._statement_index_outside` - L317-L338

```python
_statement_index_outside(self, lines: list[str], excluded: Sequence[tuple[int, int]], statement: str) -> int
```

First occurrence of `statement` outside every excluded range.

Observed calls (lexical order): `' '.join`, `str`, `str(statement or '').strip`, `str(statement or '').strip().upper`, `str(statement or '').strip().upper().split`, `enumerate`, `any`, `self._logical`.

Control points:

- L331: `if not target`
- L333: `for (index, line) in enumerate(lines)`
- L334: `if any((start <= index < end for start, end in excluded))`
- L336: `if self._logical(line) == target`

### `RestartParagraphGeometry._insert_index` - L340-L344

```python
_insert_index(self, lines: list[str]) -> int
```

Observed calls (lexical order): `enumerate`, `self._logical`, `self._logical(line).startswith`, `len`.

Control points:

- L341: `for (index, line) in enumerate(lines)`
- L342: `if self._logical(line).startswith(END_PROGRAM)`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
