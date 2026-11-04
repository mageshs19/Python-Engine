# `patterns/initialization_scope_patterns.py`

Source: [patterns/initialization_scope_patterns.py](../../../patterns/initialization_scope_patterns.py) | 91 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `e722c955158801324ad3c1b8b40383085759768adc37a5f945a5bcee49a4f4eb`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`PROCEDURE_DIVISION_PATTERN` (L5), `DIVISION_PATTERN` (L10), `SECTION_HEADER_PATTERN` (L15), `PARAGRAPH_HEADER_PATTERN` (L20), `INITIALIZE_PATTERN` (L25), `DCLGEN_INCLUDE_PATTERN` (L30), `DCLGEN_REFERENCE_PATTERN` (L35), `HOST_GROUP_PATTERN` (L40), `PERFORM_OPEN_CURSOR_PATTERN` (L45), `FETCH_PARAGRAPH_HEADER_PATTERN` (L51), `CURSOR_PARAGRAPH_HEADER_PATTERN` (L56), `PERFORM_PARAGRAPH_PATTERN` (L62), `LITERAL_PROGRAM_MOVE_PATTERN` (L67), `COBOL_HOST_GROUP_PATTERN` (L71), `__all__` (L76)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (8)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/converter_pipeline_integration.py](../converter/generators/converter_pipeline_integration.md)
- [converter/generators/enhancement/output_validator.py](../converter/generators/enhancement/output_validator.md)
- [converter/generators/initialization/cursor_scope_scanner.py](../converter/generators/initialization/cursor_scope_scanner.md)
- [converter/generators/initialization/initialize_placer.py](../converter/generators/initialization/initialize_placer.md)
- [converter/generators/initialization/initialize_remover.py](../converter/generators/initialization/initialize_remover.md)
- [converter/generators/initialization/legacy_paragraph_remover.py](../converter/generators/initialization/legacy_paragraph_remover.md)
- [converter/generators/initialization/paragraph_index.py](../converter/generators/initialization/paragraph_index.md)
- [converter/generators/initialization/population_site_scanner.py](../converter/generators/initialization/population_site_scanner.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
