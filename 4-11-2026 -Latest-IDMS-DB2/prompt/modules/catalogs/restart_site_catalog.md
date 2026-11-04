# `catalogs/restart_site_catalog.py`

Source: [catalogs/restart_site_catalog.py](../../../catalogs/restart_site_catalog.py) | 56 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `818468d931251d0842740eaf955b8eaf1388d1e543a083229aec4de1fc93cc69`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Site metadata the restart generator may not author.

## Module-level bindings

`RESTART_RETENTION_DAYS` (L39), `RESTART_DCLGEN_MEMBER` (L43), `INFRASTRUCTURE_DCLGEN_MEMBERS` (L48), `__all__` (L52)

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/resolvers/restart_context_builder.py](../converter/resolvers/restart_context_builder.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
