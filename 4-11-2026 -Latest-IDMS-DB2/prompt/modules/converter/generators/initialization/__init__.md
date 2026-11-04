# `converter/generators/initialization/__init__.py`

Source: [converter/generators/initialization/__init__.py](../../../../../converter/generators/initialization/__init__.py) | 41 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `25c16bd6eadab246b97ada4f866bcb07c31a93a2e0b5a7099032deafdf223849`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`__all__` (L29)

## Import declarations

```python
from __future__ import annotations
from converter.generators.initialization.cursor_scope_scanner import CursorOpenSite, CursorScopeScanner
from converter.generators.initialization.diagnostics import InitializationDiagnostics
from converter.generators.initialization.initialize_placer import InitializePlacer
from converter.generators.initialization.initialize_remover import InitializeRemover
from converter.generators.initialization.legacy_paragraph_remover import LegacyParagraphRemover
from converter.generators.initialization.line_geometry import LineGeometry
from converter.generators.initialization.paragraph_index import MAINLINE_NAME, ParagraphIndex
from converter.generators.initialization.scope_initializer import CursorScopedInitializer, initialize_by_cursor_scope
```

## Local dependency notes

- [converter/generators/initialization/cursor_scope_scanner.py](cursor_scope_scanner.md)
- [converter/generators/initialization/diagnostics.py](diagnostics.md)
- [converter/generators/initialization/initialize_placer.py](initialize_placer.md)
- [converter/generators/initialization/initialize_remover.py](initialize_remover.md)
- [converter/generators/initialization/legacy_paragraph_remover.py](legacy_paragraph_remover.md)
- [converter/generators/initialization/line_geometry.py](line_geometry.md)
- [converter/generators/initialization/paragraph_index.py](paragraph_index.md)
- [converter/generators/initialization/scope_initializer.py](scope_initializer.md)

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
