# `rules/sql_error_rules.py`

Source: [rules/sql_error_rules.py](../../../rules/sql_error_rules.py) | 52 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `08f7e057fd910b9c2ce37dfe629939456eb8496ae68ecc74b9d40d921ce02900`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> SQLERROR routine constants.

## Module-level bindings

`SQL_ERROR_PARAGRAPH_NAME` (L11), `LEGACY_SQL_ERROR_PARAGRAPH_NAME` (L12), `SQL_ERROR_INCLUDE_NAME` (L13), `EMIT_SQL_ERROR_PARAGRAPH_HEADER` (L19), `SQL_ERROR_BANNER` (L21), `IND_STATEMENT` (L24), `IND_SQL_BODY` (L25), `OLD_BLOCK_BODY_TOKENS` (L32), `SQL_ERROR_MESSAGES` (L44)

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/sql_error_generator.py](../converter/generators/sql_error_generator.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
