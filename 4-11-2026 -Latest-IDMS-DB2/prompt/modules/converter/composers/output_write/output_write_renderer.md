# `converter/composers/output_write/output_write_renderer.py`

Source: [converter/composers/output_write/output_write_renderer.py](../../../../../converter/composers/output_write/output_write_renderer.py) | 118 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `a916b68391978fda77a23c3ded332970f1cfa47821ebed2911b526fb5cf0363c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Renders the call site and the extracted write paragraph.

## Module-level bindings

`__all__` (L118)

## Import declarations

```python
from __future__ import annotations
from converter.composers.output_write.output_write_line_utils import OutputWriteLineUtils
from rules.output_write_paragraph_rules import BLANK_LINE, COUNTER_ADD_TEMPLATE, EMIT_OUTPUT_COUNTER_INCREMENT, EMIT_PAGE_EJECT_BEFORE_PARAGRAPH, IND_STATEMENT, OUTPUT_COUNTER_NAME, PAGE_EJECT_INDICATOR, PARAGRAPH_TERMINATOR, PERFORM_TEMPLATE, WRITE_PARAGRAPH_HEADER_TEMPLATE
```

## Local dependency notes

- [converter/composers/output_write/output_write_line_utils.py](output_write_line_utils.md)
- [rules/output_write_paragraph_rules.py](../../../rules/output_write_paragraph_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/output_write/__init__.py](__init__.md)
- [converter/composers/output_write/output_write_extractor.py](output_write_extractor.md)

## Symbol contracts and control points

### `OutputWriteRenderer` - L28-L115

```python
class OutputWriteRenderer()
```

Builds the replacement call site and the new paragraph.

### `OutputWriteRenderer.__init__` - L31-L35

```python
__init__(self, line_utils: OutputWriteLineUtils | None=None) -> None
```

Observed calls (lexical order): `OutputWriteLineUtils`.

### `OutputWriteRenderer.call_site_lines` - L38-L52

```python
call_site_lines(self, template: str, indent: str, paragraph: str) -> list[str]
```

Observed calls (lexical order): `PERFORM_TEMPLATE.format`, `bodies.append`, `COUNTER_ADD_TEMPLATE.format`, `self.lines.clone`.

Control points:

- L46: `if EMIT_OUTPUT_COUNTER_INCREMENT`

### `OutputWriteRenderer.paragraph_lines` - L55-L79

```python
paragraph_lines(self, template: str, paragraph: str, body: list[str]) -> list[str]
```

Observed calls (lexical order): `self.lines.clone`, `out.append`, `WRITE_PARAGRAPH_HEADER_TEMPLATE.format`, `out.extend`, `self.reindented_body`.

Control points:

- L63: `if EMIT_PAGE_EJECT_BEFORE_PARAGRAPH`

### `OutputWriteRenderer.reindented_body` - L81-L115

```python
reindented_body(self, body: list[str]) -> list[str]
```

Re-anchor the lifted body to Area B, preserving relative depth.

Observed calls (lexical order): `self.lines.executable_lines`, `list`, `min`, `len`, `self.lines.body_indent`, `self.lines.last_executable_index`, `enumerate`, `self.lines.body_text`, `self.lines.is_skippable`, `out.append`, `max`, `body_text.endswith`, `out.extend`, `self.lines.replace_body_wrapped`.

Control points:

- L89: `if not executable`
- L98: `for (position, line) in enumerate(body)`
- L101: `if not text or self.lines.is_skippable(line)`
- L108: `if position == last_index and (not body_text.endswith(PARAGRAPH_TERMINATOR))`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
