# `patterns/sheet_mapping_patterns.py`

Source: [patterns/sheet_mapping_patterns.py](../../../patterns/sheet_mapping_patterns.py) | 26 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `4960fb114837239db6c044ef6c70b8ef943b962e4d545c481bef16e05a7792e4`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Sheet Mapping regex patterns.

## Module-level bindings

`HEADER_NON_ALPHANUMERIC_PATTERN` (L11), `HEADER_WHITESPACE_PATTERN` (L17), `CELL_WHITESPACE_PATTERN` (L23)

## Import declarations

```python
import re
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/parsers/sheet_mapping/sheet_mapping_cell_utils.py](../converter/parsers/sheet_mapping/sheet_mapping_cell_utils.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
