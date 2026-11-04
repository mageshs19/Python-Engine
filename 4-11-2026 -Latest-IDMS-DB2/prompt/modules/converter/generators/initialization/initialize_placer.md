# `converter/generators/initialization/initialize_placer.py`

Source: [converter/generators/initialization/initialize_placer.py](../../../../../converter/generators/initialization/initialize_placer.py) | 122 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `10d1fd42a85133c3d5b80bb6194a0d7b5f11d9e19c980bd85d11c8f467c91372`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`__all__` (L122)

## Import declarations

```python
from __future__ import annotations
from typing import List
from converter.generators.initialization.cursor_scope_scanner import CursorOpenSite
from converter.generators.initialization.diagnostics import InitializationDiagnostics
from converter.generators.initialization.line_geometry import LineGeometry
from patterns.initialization_scope_patterns import INITIALIZE_PATTERN
from rules.initialization_placement_rules import EMIT_INITIALIZE_PERIOD, INITIALIZE_TEMPLATE, SCOPE_RUN, STATEMENT_TERMINATOR
```

## Local dependency notes

- [converter/generators/initialization/cursor_scope_scanner.py](cursor_scope_scanner.md)
- [converter/generators/initialization/diagnostics.py](diagnostics.md)
- [converter/generators/initialization/line_geometry.py](line_geometry.md)
- [patterns/initialization_scope_patterns.py](../../../patterns/initialization_scope_patterns.md)
- [rules/initialization_placement_rules.py](../../../rules/initialization_placement_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/enhancement/output_validator.py](../enhancement/output_validator.md)
- [converter/generators/initialization/__init__.py](__init__.md)
- [converter/generators/initialization/scope_initializer.py](scope_initializer.md)

## Symbol contracts and control points

### `InitializePlacer` - L21-L119

```python
class InitializePlacer()
```

### `InitializePlacer.__init__` - L23-L29

```python
__init__(self, diagnostics: InitializationDiagnostics, geometry: LineGeometry | None=None) -> None
```

Observed calls (lexical order): `LineGeometry`.

### `InitializePlacer.place` - L31-L49

```python
place(self, lines: List[str], sites: List[CursorOpenSite]) -> List[str]
```

Observed calls (lexical order): `list`, `sorted`, `self.already_placed`, `self.diagnostics.log`, `self.geometry.body`, `output.insert`, `self._statement`, `self._report`.

Control points:

- L37: `for site in sorted(sites, key=lambda item: item.index, reverse=True)`
- L38: `if not site.is_resolved`
- L40: `if self.already_placed(output, site)`

### `InitializePlacer.already_placed` - L51-L62

```python
already_placed(self, lines: List[str], site: CursorOpenSite) -> bool
```

Observed calls (lexical order): `self._previous_executable`, `INITIALIZE_PATTERN.match`, `self.geometry.body`, `match.group`, `match.group('group').upper`.

Control points:

- L57: `if position < 0`
- L60: `if not match`

### `InitializePlacer.verify` - L64-L73

```python
verify(self, lines: List[str], sites: List[CursorOpenSite]) -> List[str]
```

Observed calls (lexical order): `self.already_placed`.

### `InitializePlacer._statement` - L75-L79

```python
_statement(self, site: CursorOpenSite) -> str
```

Observed calls (lexical order): `INITIALIZE_TEMPLATE.format`, `self.geometry.statement`.

Control points:

- L77: `if EMIT_INITIALIZE_PERIOD`

### `InitializePlacer._report` - L81-L113

```python
_report(self, site: CursorOpenSite, lines: List[str]) -> None
```

Observed calls (lexical order): `self.geometry.body`, `self.diagnostics.log`, `getattr`.

Control points:

- L84: `if site.scope == SCOPE_RUN`

### `InitializePlacer._previous_executable` - L115-L119

```python
_previous_executable(self, lines: List[str], index: int) -> int
```

Observed calls (lexical order): `range`, `self.geometry.is_comment_or_blank`.

Control points:

- L116: `for position in range(index - 1, -1, -1)`
- L117: `if not self.geometry.is_comment_or_blank(lines[position])`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
