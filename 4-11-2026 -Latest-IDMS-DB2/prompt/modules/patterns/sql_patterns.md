# `patterns/sql_patterns.py`

Source: [patterns/sql_patterns.py](../../../patterns/sql_patterns.py) | 122 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `c2bc8c4147434c76d3a28c3c9ad297d6f37fa5a96b5c93a730e63849aef2526d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> SQL regex patterns and formatting keyword groups.

## Module-level bindings

`EXEC_SQL_PATTERN` (L11), `END_EXEC_PATTERN` (L17), `INCLUDE_PATTERN` (L23), `SELECT_SQL_PATTERN` (L29), `FROM_SQL_PATTERN` (L35), `WHERE_SQL_PATTERN` (L41), `UPDATE_SQL_PATTERN` (L47), `INSERT_SQL_PATTERN` (L53), `DELETE_SQL_PATTERN` (L59), `OPEN_CURSOR_PATTERN` (L65), `FETCH_CURSOR_PATTERN` (L71), `CLOSE_CURSOR_PATTERN` (L77), `HOST_REFERENCE_PATTERN` (L83), `SQL_KEYWORDS_ZERO_INDENT` (L89), `SQL_KEYWORDS_LEVEL_1` (L95), `SQL_KEYWORDS_LEVEL_2` (L119)

## Import declarations

```python
import re
```

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/validators/production_validator.py](../converter/validators/production_validator.md)
- [tests/test_patterns.py](../tests/test_patterns.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
