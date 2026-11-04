# `converter/generators/initialization/legacy_paragraph_remover.py`

Source: [converter/generators/initialization/legacy_paragraph_remover.py](../../../../../converter/generators/initialization/legacy_paragraph_remover.py) | 148 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `30391b6ae401cb032af7d8580751c0f61c760f5ae1e1dbd22d89583ac6b8654f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`__all__` (L148)

## Import declarations

```python
from __future__ import annotations
from typing import List, Set, Tuple
from converter.generators.initialization.diagnostics import InitializationDiagnostics
from converter.generators.initialization.line_geometry import LineGeometry
from converter.generators.initialization.paragraph_index import ParagraphIndex
from patterns.initialization_scope_patterns import INITIALIZE_PATTERN, PERFORM_PARAGRAPH_PATTERN
from rules.initialization_placement_rules import SALVAGE_LEGACY_STARTUP_STATEMENTS, STARTUP_PARAGRAPH_NAME, STATEMENT_TERMINATOR
```

## Local dependency notes

- [converter/generators/initialization/diagnostics.py](diagnostics.md)
- [converter/generators/initialization/line_geometry.py](line_geometry.md)
- [converter/generators/initialization/paragraph_index.py](paragraph_index.md)
- [patterns/initialization_scope_patterns.py](../../../patterns/initialization_scope_patterns.md)
- [rules/initialization_placement_rules.py](../../../rules/initialization_placement_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/initialization/__init__.py](__init__.md)
- [converter/generators/initialization/scope_initializer.py](scope_initializer.md)

## Symbol contracts and control points

### `LegacyParagraphRemover` - L23-L145

```python
class LegacyParagraphRemover()
```

### `LegacyParagraphRemover.__init__` - L25-L33

```python
__init__(self, diagnostics: InitializationDiagnostics, geometry: LineGeometry | None=None, paragraphs: ParagraphIndex | None=None) -> None
```

Observed calls (lexical order): `LineGeometry`, `ParagraphIndex`.

### `LegacyParagraphRemover.remove` - L35-L73

```python
remove(self, lines: List[str]) -> List[str]
```

Observed calls (lexical order): `self.paragraphs.span_named`, `self._perform_indexes`, `list`, `self._salvage`, `self._mainline_keys`, `enumerate`, `self._inside`, `output.extend`, `self._render`, `self.diagnostics.log`, `output.append`.

Control points:

- L38: `if span[0] < 0 and (not performs)`
- L46: `for (index, line) in enumerate(lines)`
- L47: `if self._inside(span, index)`
- L49: `if index in performs`
- L50: `if not emitted`
- L63: `if span[0] >= 0`
- L68: `if performs`

### `LegacyParagraphRemover._perform_indexes` - L75-L84

```python
_perform_indexes(self, lines: List[str]) -> Set[int]
```

Observed calls (lexical order): `STARTUP_PARAGRAPH_NAME.upper`, `set`, `enumerate`, `self.geometry.is_comment_or_blank`, `PERFORM_PARAGRAPH_PATTERN.match`, `self.geometry.body`, `match.group`, `match.group('paragraph').upper`, `found.add`.

Control points:

- L78: `for (index, line) in enumerate(lines)`
- L79: `if self.geometry.is_comment_or_blank(line)`
- L82: `if match and match.group('paragraph').upper() == target`

### `LegacyParagraphRemover._salvage` - L86-L102

```python
_salvage(self, lines: List[str], span: Tuple[int, int]) -> List[str]
```

Observed calls (lexical order): `range`, `self.geometry.is_comment_or_blank`, `self.geometry.body`, `INITIALIZE_PATTERN.match`, `body.rstrip`, `body.rstrip().rstrip`, `body.rstrip().rstrip(STATEMENT_TERMINATOR).strip`, `out.append`.

Control points:

- L91: `if not SALVAGE_LEGACY_STARTUP_STATEMENTS or span[0] < 0`
- L94: `for index in range(span[0] + 1, span[1] + 1)`
- L96: `if self.geometry.is_comment_or_blank(line)`
- L99: `if INITIALIZE_PATTERN.match(body)`

### `LegacyParagraphRemover._mainline_keys` - L104-L113

```python
_mainline_keys(self, lines: List[str]) -> Set[str]
```

Observed calls (lexical order): `self.paragraphs.mainline_span`, `set`, `range`, `self.geometry.is_comment_or_blank`, `keys.add`, `self._key`, `self.geometry.body`.

Control points:

- L106: `if start < 0`
- L109: `for index in range(start + 1, end + 1)`
- L110: `if self.geometry.is_comment_or_blank(lines[index])`

### `LegacyParagraphRemover._render` - L115-L136

```python
_render(self, template: str, salvage: List[str], known: Set[str]) -> List[str]
```

Observed calls (lexical order): `self.geometry.indent_of`, `set`, `self._key`, `self.diagnostics.log`, `seen.add`, `out.append`, `self.geometry.statement`.

Control points:

- L124: `for body in salvage`
- L126: `if not key or key in known or key in seen`

### `LegacyParagraphRemover._inside` - L139-L140

```python
_inside(span: Tuple[int, int], index: int) -> bool
```

### `LegacyParagraphRemover._key` - L143-L145

```python
_key(body: str) -> str
```

Observed calls (lexical order): `str`, `str(body or '').upper`, `str(body or '').upper().rstrip`, `str(body or '').upper().rstrip().rstrip`, `' '.join`, `text.split`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
