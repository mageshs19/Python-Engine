# `converter/composers/counter_declaration/counter_line_factory.py`

Source: [converter/composers/counter_declaration/counter_line_factory.py](../../../../../converter/composers/counter_declaration/counter_line_factory.py) | 71 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `4245939c63eddacac520a31d6a46cbc31ec2e695196fd96d47d3e5ef7d2a4e67`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Fixed-format line rendering for generated counter lines.

## Module-level bindings

`FALLBACK_COMMENT_PREFIX` (L16), `__all__` (L71)

## Import declarations

```python
from __future__ import annotations
from converter.services.fixed_format_line_service import FixedFormatLineService
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](../../services/fixed_format_line_service.md)

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/counter_declaration/__init__.py](__init__.md)
- [converter/composers/counter_declaration/counter_anchor.py](counter_anchor.md)
- [converter/composers/counter_declaration/counter_anchor_resolver.py](counter_anchor_resolver.md)
- [converter/composers/counter_declaration/counter_totals_writer.py](counter_totals_writer.md)
- [converter/services/generated_field_anchor.py](../../services/generated_field_anchor.md)

## Symbol contracts and control points

### `CounterLineFactory` - L19-L68

```python
class CounterLineFactory()
```

Builds statement, comment and blank lines from a template.

### `CounterLineFactory.__init__` - L22-L26

```python
__init__(self, fixed_format: FixedFormatLineService | None=None) -> None
```

Observed calls (lexical order): `FixedFormatLineService`.

### `CounterLineFactory.statement` - L29-L38

```python
statement(self, template: str, body: str) -> str
```

An executable line carrying `body` in columns 8-72.

Observed calls (lexical order): `self.fixed_format.split`, `self.fixed_format.build_or_none`.

### `CounterLineFactory.comment` - L40-L45

```python
comment(self, template: str, body: str) -> str
```

A comment line: '*' in column 7, text from column 8.

Observed calls (lexical order): `self.fixed_format.split`, `str`, `str(body or '').lstrip`, `str(body or '').lstrip('*').strip`, `self.fixed_format.build_or_none`.

### `CounterLineFactory.blank` - L47-L48

```python
blank(self, template: str) -> str
```

Observed calls (lexical order): `self.statement`.

### `CounterLineFactory.body_indent` - L50-L55

```python
body_indent(self, template: str) -> str
```

Leading spaces of the template's body, as a string.

Observed calls (lexical order): `self.fixed_format.body_indent`.

### `CounterLineFactory.logical` - L57-L61

```python
logical(self, line: str) -> str
```

Observed calls (lexical order): `self.fixed_format.logical`, `str`, `str(self.fixed_format.logical(line) or '').strip`, `str(line or '').strip`.

### `CounterLineFactory.is_skippable` - L63-L68

```python
is_skippable(self, line: str) -> bool
```

Comment, page-eject, debug or continuation line.

Observed calls (lexical order): `bool`, `self.fixed_format.is_comment_or_control_line`.

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
