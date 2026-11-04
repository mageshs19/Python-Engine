# `converter/composers/counter_declaration/counter_anchor.py`

Source: [converter/composers/counter_declaration/counter_anchor.py](../../../../../converter/composers/counter_declaration/counter_anchor.py) | 112 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `894dc5e83c166bd3bcf459479ad544582232d78ec0124b764fbcae7d2b333605`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> The place a counter declaration will be written.

## Module-level bindings

`__all__` (L112)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass
from converter.composers.counter_declaration.counter_line_factory import CounterLineFactory
from patterns.counter_declaration_patterns import GROUP_HEADER_PATTERN, SECTION_OR_DIVISION_PATTERN, SUBORDINATE_ENTRY_PATTERN
```

## Local dependency notes

- [converter/composers/counter_declaration/counter_line_factory.py](counter_line_factory.md)
- [patterns/counter_declaration_patterns.py](../../../patterns/counter_declaration_patterns.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/counter_declaration/__init__.py](__init__.md)
- [converter/composers/counter_declaration/counter_anchor_resolver.py](counter_anchor_resolver.md)

## Symbol contracts and control points

### `CounterAnchor` - L33-L44

```python
class CounterAnchor()
```

Where and how a counter declaration is rendered.

Declared class/data-model fields:

```python
insert_index: int = -1
template_line: str = ''
level: str = ''
indent: str = ''
group: str = ''
```

### `CounterAnchor.is_usable` - L43-L44

```python
is_usable(self) -> bool
```

Observed calls (lexical order): `bool`.

### `CounterAnchorFinder` - L47-L109

```python
class CounterAnchorFinder()
```

Locates the first subordinate entry of an 01 group.

### `CounterAnchorFinder.__init__` - L50-L54

```python
__init__(self, line_factory: CounterLineFactory | None=None) -> None
```

Observed calls (lexical order): `CounterLineFactory`.

### `CounterAnchorFinder.first_child` - L56-L88

```python
first_child(self, lines: list[str], header_index: int) -> tuple[int, str] | None
```

(index, level) of the group's first subordinate entry.

Observed calls (lexical order): `len`, `range`, `self.lines.is_skippable`, `self.lines.logical`, `GROUP_HEADER_PATTERN.match`, `SECTION_OR_DIVISION_PATTERN.match`, `SUBORDINATE_ENTRY_PATTERN.match`, `match.group`.

Control points:

- L66: `for index in range(header_index + 1, len(lines))`
- L69: `if self.lines.is_skippable(line)`
- L73: `if not logical`
- L76: `if GROUP_HEADER_PATTERN.match(logical)`
- L79: `if SECTION_OR_DIVISION_PATTERN.match(logical)`
- L83: `if match`

### `CounterAnchorFinder.anchor_for` - L90-L109

```python
anchor_for(self, lines: list[str], header_index: int, group_name: str) -> CounterAnchor | None
```

Observed calls (lexical order): `self.first_child`, `CounterAnchor`, `self.lines.body_indent`.

Control points:

- L97: `if child is None`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
