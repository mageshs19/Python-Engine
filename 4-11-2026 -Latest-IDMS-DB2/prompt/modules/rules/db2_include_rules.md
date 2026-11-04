# `rules/db2_include_rules.py`

Source: [rules/db2_include_rules.py](../../../rules/db2_include_rules.py) | 72 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `3603892c7f9e0987f9a83b77f1deda22d5113a3efc7f7a2f9fe4751b0425de79`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> DB2 INCLUDE emission rules.

## Module-level bindings

`INCLUDE_SINGLE_LINE` (L37), `INCLUDE_SINGLE_TEMPLATE` (L39), `INCLUDE_BLOCK_OPEN` (L40), `INCLUDE_BLOCK_BODY_TEMPLATE` (L41), `INCLUDE_BLOCK_CLOSE` (L42), `IND_INCLUDE` (L48), `IND_INCLUDE_BODY` (L49), `INFRASTRUCTURE_INCLUDES` (L55), `INCLUDE_MESSAGES` (L62)

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure/include_renderer.py](../converter/generators/db2_infrastructure/include_renderer.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
