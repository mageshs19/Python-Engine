# `patterns/dclgen_patterns.py`

Source: [patterns/dclgen_patterns.py](../../../patterns/dclgen_patterns.py) | 71 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `26be471a8d73592b85f114e6478587ad1013591b47b80b38e91b7285a1f9c364`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> DCLGEN regex patterns.

## Module-level bindings

`DECLARE_TABLE_PATTERN` (L11), `DECLARE_TABLE_ALT_PATTERN` (L17), `DCLGEN_TABLE_COMMENT_PATTERN` (L23), `COBOL_GROUP_PATTERN` (L29), `COBOL_FIELD_PATTERN` (L35), `DCLGEN_PIC_PATTERN` (L42), `DCLGEN_USAGE_PATTERN` (L49), `SQL_NAME_CLEANUP_PATTERN` (L56), `MULTIPLE_UNDERSCORE_PATTERN` (L62), `VALID_SQL_COLUMN_NAME_PATTERN` (L68)

## Import declarations

```python
import re
```

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/parsers/dclgen/cobol_host_field_parser.py](../converter/parsers/dclgen/cobol_host_field_parser.md)
- [converter/parsers/dclgen/sql_declare_parser.py](../converter/parsers/dclgen/sql_declare_parser.md)
- [converter/parsers/dclgen/sql_name_normalizer.py](../converter/parsers/dclgen/sql_name_normalizer.md)
- [tests/test_patterns.py](../tests/test_patterns.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
