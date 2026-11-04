# `converter/generators/initialization/scope_initializer.py`

Source: [converter/generators/initialization/scope_initializer.py](../../../../../converter/generators/initialization/scope_initializer.py) | 241 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `04f18238a2120edaab48c3e1f58f40ea01237fec63243e4f2e546b9315726530`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Places INITIALIZE <DCLGEN group> at the right scope.

## Module-level bindings

`__all__` (L241)

## Import declarations

```python
from __future__ import annotations
from typing import List, Sequence, Set
from converter.generators.initialization.cursor_scope_scanner import CursorScopeScanner
from converter.generators.initialization.diagnostics import InitializationDiagnostics
from converter.generators.initialization.initialize_placer import InitializePlacer
from converter.generators.initialization.initialize_remover import InitializeRemover
from converter.generators.initialization.legacy_paragraph_remover import LegacyParagraphRemover
from converter.generators.initialization.line_geometry import LineGeometry
from converter.generators.initialization.paragraph_index import ParagraphIndex
from converter.generators.initialization.population_site_scanner import PopulationSiteScanner
from rules.initialization_placement_rules import ENFORCE_CURSOR_SCOPED_INITIALIZATION, REMOVE_LEGACY_STARTUP_PARAGRAPH, SCOPE_ROW, SCOPE_RUN
```

## Local dependency notes

- [converter/generators/initialization/cursor_scope_scanner.py](cursor_scope_scanner.md)
- [converter/generators/initialization/diagnostics.py](diagnostics.md)
- [converter/generators/initialization/initialize_placer.py](initialize_placer.md)
- [converter/generators/initialization/initialize_remover.py](initialize_remover.md)
- [converter/generators/initialization/legacy_paragraph_remover.py](legacy_paragraph_remover.md)
- [converter/generators/initialization/line_geometry.py](line_geometry.md)
- [converter/generators/initialization/paragraph_index.py](paragraph_index.md)
- [converter/generators/initialization/population_site_scanner.py](population_site_scanner.md)
- [rules/initialization_placement_rules.py](../../../rules/initialization_placement_rules.md)

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/enhancement/enhancement_pipeline.py](../enhancement/enhancement_pipeline.md)
- [converter/generators/initialization/__init__.py](__init__.md)
- [converter/generators/initialization_centralizer.py](../initialization_centralizer.md)
- [tests/initialization_scope/conftest.py](../../../tests/initialization_scope/conftest.md)
- [tests/initialization_scope/test_population_scope.py](../../../tests/initialization_scope/test_population_scope.md)

## Symbol contracts and control points

### `CursorScopedInitializer` - L89-L235

```python
class CursorScopedInitializer()
```

Clears every DCLGEN group once per unit of work, or refuses.

### `CursorScopedInitializer.__init__` - L99-L114

```python
__init__(self, program_text: str) -> None
```

Observed calls (lexical order): `set`, `InitializationDiagnostics`, `LineGeometry`, `ParagraphIndex`, `CursorScopeScanner`, `PopulationSiteScanner`, `InitializeRemover`, `LegacyParagraphRemover`, `InitializePlacer`.

### `CursorScopedInitializer.messages` - L117-L118

```python
messages(self) -> List[str]
```

Observed calls (lexical order): `self.diagnostics.all`.

### `CursorScopedInitializer.process` - L123-L193

```python
process(self) -> str
```

Observed calls (lexical order): `str`, `text.strip`, `self.diagnostics.reset`, `self.geometry.split`, `self.scanner.dclgen_groups`, `self.diagnostics.log`, `self.paragraphs.procedure_division_index`, `self._initialization_sites`, `self.scanner.open_sites`, `self.scanner.unresolved_cursors`, `list`, `self.legacy.remove`, `self.remover.remove`, `self.placer.place`, `self._unplaced_groups`, `', '.join`.
Another 3 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L125: `if not text.strip() or not ENFORCE_CURSOR_SCOPED_INITIALIZATION`
- L132: `if not self.dclgen_groups`
- L136: `if self.paragraphs.procedure_division_index(lines) < 0`
- L141: `if not sites`
- L145: `if not self.scanner.open_sites(lines)`
- L153: `for cursor in self.scanner.unresolved_cursors(lines)`
- L157: `if REMOVE_LEGACY_STARTUP_PARAGRAPH`
- L161: `if removed`
- Another 2 conditions/loops exist in this source span.

### `CursorScopedInitializer._initialization_sites` - L198-L217

```python
_initialization_sites(self, lines: Sequence[str]) -> List[object]
```

Cursor sites first, then population sites for the rest.

Observed calls (lexical order): `list`, `self.scanner.resolved_sites`, `self.population.sites`.

### `CursorScopedInitializer._groups_at` - L220-L226

```python
_groups_at(sites, scope) -> Set[str]
```

Observed calls (lexical order): `str`, `str(scope or '').upper`, `str(site.scope or '').upper`.

### `CursorScopedInitializer._unplaced_groups` - L228-L235

```python
_unplaced_groups(self, lines, sites) -> List[str]
```

Groups that were planned but do not appear in the output.

Observed calls (lexical order): `self.geometry.logical_text`, `sorted`.

### `initialize_by_cursor_scope` - L237-L238

```python
initialize_by_cursor_scope(program_text: str) -> str
```

Observed calls (lexical order): `CursorScopedInitializer`, `CursorScopedInitializer(program_text).process`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
