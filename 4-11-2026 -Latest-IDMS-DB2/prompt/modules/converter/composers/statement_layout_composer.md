# `converter/composers/statement_layout_composer.py`

Source: [converter/composers/statement_layout_composer.py](../../../../converter/composers/statement_layout_composer.py) | 207 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `be7941a6d6779930457115b4f981b5e405d05fc5cc9fb15079ae4d19625440cd`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Inserts a blank line before a paragraph header.

## Module-level bindings

`BLANK_BODY` (L40), `BLANK_INDICATOR` (L41), `INDICATOR_COLUMN` (L42), `__all__` (L207)

## Import declarations

```python
from __future__ import annotations
from converter.services.fixed_format_line_service import FixedFormatLineService
from rules.statement_layout_rules import BLANK_LINE_BEFORE_PARAGRAPH, ENFORCE_STATEMENT_LAYOUT, NON_PARAGRAPH_WORDS, SENTENCE_TERMINATOR, SEPARATOR_INDICATORS, SKIPPABLE_INDICATORS, SQL_BLOCK_END, SQL_BLOCK_START, STATEMENT_LAYOUT_MESSAGES, PROCEDURE_DIVISION_TOKEN
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](../services/fixed_format_line_service.md)
- [rules/statement_layout_rules.py](../../rules/statement_layout_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/registry.py](../pipeline/registry.md)

## Symbol contracts and control points

### `StatementLayoutComposer` - L45-L204

```python
class StatementLayoutComposer()
```

Separates paragraphs with a blank line.

### `StatementLayoutComposer.__init__` - L48-L53

```python
__init__(self, fixed_format: FixedFormatLineService | None=None) -> None
```

Observed calls (lexical order): `FixedFormatLineService`.

### `StatementLayoutComposer.compose` - L58-L109

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `str`, `source.replace`, `source.replace('\r\n', '\n').replace`, `source.replace('\r\n', '\n').replace('\r', '\n').split`, `self._track_sql`, `self._body`, `self._body(line).upper`, `output.append`, `self._is_paragraph_header`, `self._last_populated`, `self._is_separator`, `self._clone`, `self.messages.append`, `STATEMENT_LAYOUT_MESSAGES['blank_inserted'].format`, `'\n'.join`, `'\n'.join(output).rstrip`.

Control points:

- L62: `if not source or not ENFORCE_STATEMENT_LAYOUT`
- L65: `if not BLANK_LINE_BEFORE_PARAGRAPH`
- L80: `for line in lines`
- L83: `if not in_procedure`
- L84: `if PROCEDURE_DIVISION_TOKEN in self._body(line).upper()`
- L89: `if in_sql or not self._is_paragraph_header(line)`
- L95: `if previous is not None and (not self._is_separator(previous))`
- L97: `if blank is not None`

### `StatementLayoutComposer._is_paragraph_header` - L114-L144

```python
_is_paragraph_header(self, line: str) -> bool
```

A single name ending in a period, starting in Area A.

Observed calls (lexical order): `self._is_skippable`, `self._body`, `body[:1].isspace`, `body.strip`, `name.endswith`, `len`, `name[:-len(SENTENCE_TERMINATOR)].upper`, `name[0].isalnum`.

Control points:

- L123: `if self._is_skippable(line)`
- L127: `if not body`
- L131: `if body[:1].isspace()`
- L135: `if not name.endswith(SENTENCE_TERMINATOR)`
- L137: `if ' ' in name`
- L141: `if not name or name in NON_PARAGRAPH_WORDS`

### `StatementLayoutComposer._is_separator` - L146-L156

```python
_is_separator(self, line: str) -> bool
```

Blank, comment or page eject - already separates.

Observed calls (lexical order): `str`, `text.strip`, `self._body`, `self._body(text).strip`, `len`.

Control points:

- L150: `if not text.strip()`
- L152: `if not self._body(text).strip()`

### `StatementLayoutComposer._is_skippable` - L158-L167

```python
_is_skippable(self, line: str) -> bool
```

Observed calls (lexical order): `str`, `text.strip`, `self.fixed_format.is_fixed_line`, `len`.

Control points:

- L161: `if not text.strip()`
- L163: `if not self.fixed_format.is_fixed_line(text)`

### `StatementLayoutComposer._track_sql` - L170-L178

```python
_track_sql(line: str, in_sql: bool) -> bool
```

Observed calls (lexical order): `str`, `str(line or '').upper`.

Control points:

- L173: `if SQL_BLOCK_START in upper`
- L175: `if in_sql and SQL_BLOCK_END in upper`

### `StatementLayoutComposer._body` - L183-L188

```python
_body(self, line: str) -> str
```

Observed calls (lexical order): `self.fixed_format.split`, `str`, `str(body or '').rstrip`.

### `StatementLayoutComposer._clone` - L190-L197

```python
_clone(self, template: str, body: str) -> str | None
```

Observed calls (lexical order): `self.fixed_format.split`, `self.fixed_format.build_or_none`.

### `StatementLayoutComposer._last_populated` - L200-L204

```python
_last_populated(output: list[str]) -> str | None
```

Observed calls (lexical order): `reversed`, `str`, `str(line or '').strip`.

Control points:

- L201: `for line in reversed(output)`
- L202: `if str(line or '').strip()`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
