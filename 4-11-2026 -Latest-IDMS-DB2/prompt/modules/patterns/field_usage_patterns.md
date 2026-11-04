# `patterns/field_usage_patterns.py`

Source: [patterns/field_usage_patterns.py](../../../patterns/field_usage_patterns.py) | 64 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `8cf87094f185bc614f9ed0244cf085f2d9c3c4c0d564b7b13aa9c3d1cb6547de`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Field usage regex patterns.

## Module-level bindings

`QUALIFIED_REFERENCE_PATTERN` (L19), `DCLGEN_OF_PATTERN` (L25), `DCLGEN_DOT_PATTERN` (L31), `MOVE_STATEMENT_PATTERN` (L36), `CONDITION_STATEMENT_PATTERN` (L41), `OUTPUT_STATEMENT_PATTERN` (L46), `COMMENT_OR_BLANK_PATTERN` (L51), `EXEC_SQL_START_PATTERN` (L56), `EXEC_SQL_END_PATTERN` (L61)

## Import declarations

```python
import re
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/transformers/qualified_reference_transformer.py](../converter/transformers/qualified_reference_transformer.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
