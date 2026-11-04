# `rules/mapping_scope_rules.py`

Source: [rules/mapping_scope_rules.py](../../../rules/mapping_scope_rules.py) | 38 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `990b75d9a11635382c049bce2315df738dc10229c3302c3914cac38034d647d8`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Mapping validation scope rules.

## Module-level bindings

`ENFORCE_MAPPING_SCOPE_FILTER` (L24), `OUT_OF_SCOPE_TEMPLATE` (L29), `DIAG_SCOPE_APPLIED` (L35)

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/validators/mapping_scope_filter.py](../converter/validators/mapping_scope_filter.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
