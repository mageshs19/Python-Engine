# `patterns/field_usage_analysis_patterns.py`

Source: [patterns/field_usage_analysis_patterns.py](../../../patterns/field_usage_analysis_patterns.py) | 71 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `c47140676306550fe618bfa2ed62d9dff4f739232a0c530dcbf5a5a1afb6e0df`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`QUALIFIED_REFERENCE_PATTERN` (L13), `DCLGEN_OF_PATTERN` (L20), `DCLGEN_DOT_PATTERN` (L27), `MOVE_PATTERN` (L33), `CONDITION_PATTERN` (L39), `DIVISION_PATTERN` (L45), `COMMENT_PATTERN` (L51), `EXEC_SQL_START_PATTERN` (L57), `EXEC_SQL_END_PATTERN` (L63), `BARE_IDENTIFIER_PATTERN` (L68)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/analyzers/field_usage_analyzer.py](../converter/analyzers/field_usage_analyzer.md)
- [converter/analyzers/field_usage_capture_service.py](../converter/analyzers/field_usage_capture_service.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
