# `catalogs/restart_trigger_catalog.py`

Source: [catalogs/restart_trigger_catalog.py](../../../catalogs/restart_trigger_catalog.py) | 71 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `a17896ce498dd90eba7135c65a2ff26fd25f197e2a8ff97f95300f3ec4b53dea`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Site vocabulary for detecting a legacy IDMS checkpoint.

## Module-level bindings

`LEGACY_CHECKPOINT_RECORDS` (L42), `LEGACY_CHECKPOINT_FIELDS` (L51), `CHECKPOINT_VERBS` (L60), `__all__` (L67)

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/resolvers/restart_context_builder.py](../converter/resolvers/restart_context_builder.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
