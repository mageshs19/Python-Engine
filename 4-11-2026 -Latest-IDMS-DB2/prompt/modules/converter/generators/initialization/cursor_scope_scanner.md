# `converter/generators/initialization/cursor_scope_scanner.py`

Source: [converter/generators/initialization/cursor_scope_scanner.py](../../../../../converter/generators/initialization/cursor_scope_scanner.py) | 143 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `416dcf2104ce38b9f1ff39505c10f61dca42af394f21552fc18591ca1abcc620`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`__all__` (L143)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Set
from converter.generators.initialization.line_geometry import LineGeometry
from converter.generators.initialization.paragraph_index import MAINLINE_NAME, ParagraphIndex
from patterns.initialization_scope_patterns import DCLGEN_INCLUDE_PATTERN, DCLGEN_REFERENCE_PATTERN, FETCH_PARAGRAPH_HEADER_PATTERN, HOST_GROUP_PATTERN, PERFORM_OPEN_CURSOR_PATTERN
from rules.initialization_placement_rules import DCLGEN_GROUP_PREFIX, SCOPE_ROW, SCOPE_RUN
```

## Local dependency notes

- [converter/generators/initialization/line_geometry.py](line_geometry.md)
- [converter/generators/initialization/paragraph_index.py](paragraph_index.md)
- [patterns/initialization_scope_patterns.py](../../../patterns/initialization_scope_patterns.md)
- [rules/initialization_placement_rules.py](../../../rules/initialization_placement_rules.md)

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/enhancement/output_validator.py](../enhancement/output_validator.md)
- [converter/generators/initialization/__init__.py](__init__.md)
- [converter/generators/initialization/initialize_placer.py](initialize_placer.md)
- [converter/generators/initialization/scope_initializer.py](scope_initializer.md)

## Symbol contracts and control points

### `CursorOpenSite` - L26-L36

```python
class CursorOpenSite()
```

Declared class/data-model fields:

```python
index: int
cursor: str
group: str
indent: str
owner: str
scope: str
```

### `CursorOpenSite.is_resolved` - L35-L36

```python
is_resolved(self) -> bool
```

Observed calls (lexical order): `bool`.

### `CursorScopeScanner` - L39-L140

```python
class CursorScopeScanner()
```

### `CursorScopeScanner.__init__` - L41-L47

```python
__init__(self, geometry: LineGeometry | None=None, paragraphs: ParagraphIndex | None=None) -> None
```

Observed calls (lexical order): `LineGeometry`, `ParagraphIndex`.

### `CursorScopeScanner.dclgen_groups` - L49-L64

```python
dclgen_groups(self, lines: List[str]) -> Set[str]
```

Observed calls (lexical order): `set`, `self.geometry.is_comment_or_blank`, `self.geometry.body`, `pattern.finditer`, `found.add`, `match.group`, `match.group('group').upper`, `group.startswith`.

Control points:

- L51: `for line in lines`
- L52: `if self.geometry.is_comment_or_blank(line)`
- L55: `for pattern in (DCLGEN_INCLUDE_PATTERN, DCLGEN_REFERENCE_PATTERN)`
- L59: `for match in pattern.finditer(body)`

### `CursorScopeScanner.fetch_group_map` - L66-L82

```python
fetch_group_map(self, lines: List[str]) -> Dict[str, str]
```

Observed calls (lexical order): `enumerate`, `self.paragraphs.is_paragraph_header`, `FETCH_PARAGRAPH_HEADER_PATTERN.match`, `self.geometry.body`, `header.group`, `header.group('cursor').upper`, `self._group_in_span`.

Control points:

- L68: `for (index, line) in enumerate(lines)`
- L69: `if not self.paragraphs.is_paragraph_header(line)`
- L74: `if not header`
- L77: `if cursor in mapping`
- L80: `if group`

### `CursorScopeScanner.open_sites` - L84-L111

```python
open_sites(self, lines: List[str]) -> List[CursorOpenSite]
```

Observed calls (lexical order): `self.fetch_group_map`, `enumerate`, `self.geometry.is_comment_or_blank`, `PERFORM_OPEN_CURSOR_PATTERN.match`, `self.geometry.body`, `match.group`, `match.group('cursor').upper`, `self.paragraphs.owner_of`, `sites.append`, `CursorOpenSite`, `groups.get`, `self.geometry.indent_of`.

Control points:

- L87: `for (index, line) in enumerate(lines)`
- L88: `if self.geometry.is_comment_or_blank(line)`
- L93: `if not match`

### `CursorScopeScanner.resolved_sites` - L113-L114

```python
resolved_sites(self, lines: List[str]) -> List[CursorOpenSite]
```

Observed calls (lexical order): `self.open_sites`.

### `CursorScopeScanner.unresolved_cursors` - L116-L121

```python
unresolved_cursors(self, lines: List[str]) -> List[str]
```

Observed calls (lexical order): `self.open_sites`.

### `CursorScopeScanner.scoped_groups` - L123-L128

```python
scoped_groups(self, lines: List[str], scope: str) -> Set[str]
```

Observed calls (lexical order): `self.resolved_sites`, `str`, `str(scope or '').upper`.

### `CursorScopeScanner._group_in_span` - L130-L140

```python
_group_in_span(self, lines: List[str], start: int) -> str
```

Observed calls (lexical order): `self.paragraphs.span_of`, `range`, `self.geometry.is_comment_or_blank`, `HOST_GROUP_PATTERN.search`, `self.geometry.body`, `match.group`, `match.group('group').upper`.

Control points:

- L132: `if span_start < 0`
- L134: `for index in range(span_start + 1, span_end + 1)`
- L135: `if self.geometry.is_comment_or_blank(lines[index])`
- L138: `if match`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
