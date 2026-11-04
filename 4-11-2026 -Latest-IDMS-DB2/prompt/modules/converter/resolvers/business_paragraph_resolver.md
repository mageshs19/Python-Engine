# `converter/resolvers/business_paragraph_resolver.py`

Source: [converter/resolvers/business_paragraph_resolver.py](../../../../converter/resolvers/business_paragraph_resolver.py) | 70 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `66b5d3ea6beac70c4396acfdff308cb82ee077ed4685c76168276cee5cedb578`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Resolves the business paragraph a cursor's row logic lives in.

## Module-level bindings

`NAVIGATION_MARKER_TEMPLATES` (L19)

## Import declarations

```python
from __future__ import annotations
from rules.idms_transformer_messages import CONVERTED_FIND_FIRST_TEMPLATE, CONVERTED_OBTAIN_FIRST_TEMPLATE, CONVERTED_OBTAIN_NEXT_TEMPLATE
```

## Local dependency notes

- [rules/idms_transformer_messages.py](../../rules/idms_transformer_messages.md)

## Symbol contracts and control points

### `marker_prefix` - L26-L34

```python
marker_prefix(template: str) -> str
```

The literal head of a template, up to its first placeholder.

Observed calls (lexical order): `str`, `str(template or '').split`, `' '.join`, `' '.join(head.split()).upper`, `head.split`.

### `BusinessParagraphResolver` - L37-L70

```python
class BusinessParagraphResolver()
```

### `BusinessParagraphResolver.__init__` - L39-L45

```python
__init__(self, line_utils, paragraph_index, log) -> None
```

Observed calls (lexical order): `tuple`, `marker_prefix`.

### `BusinessParagraphResolver.business_paragraph` - L47-L57

```python
business_paragraph(self, lines, cursor_set) -> str
```

Highest-confidence first. Never guesses.

Observed calls (lexical order): `self._paragraph_of_navigation_marker`, `self._paragraph_holding_perform`, `cursor_set.names.values`.

Control points:

- L50: `if name`
- L54: `if name and name not in cursor_set.names.values()`

### `BusinessParagraphResolver._paragraph_of_navigation_marker` - L59-L70

```python
_paragraph_of_navigation_marker(self, lines, cursor_set) -> str
```

Observed calls (lexical order): `enumerate`, `self.lines_utils.comment_body`, `' '.join`, `' '.join(body.split()).upper`, `body.split`, `compressed.startswith`, `self.paragraphs.enclosing_header`, `cursor_set.names.values`.

Control points:

- L60: `for (index, line) in enumerate(lines)`
- L62: `if not body`
- L65: `if not compressed.startswith(self._prefixes)`
- L68: `if header and header.name not in cursor_set.names.values()`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
