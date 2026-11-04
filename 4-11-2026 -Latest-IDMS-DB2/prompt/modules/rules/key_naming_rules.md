# `rules/key_naming_rules.py`

Source: [rules/key_naming_rules.py](../../../rules/key_naming_rules.py) | 17 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `50f4585c040a70f3d1401cf56e056cb2286b1d1d7c233552f984f7d5fdaceddb`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Column-name prefix vocabulary. Constants only.

## Module-level bindings

`IDENTITY_KEY_PREFIXES` (L9), `__all__` (L17)

## Import declarations

```python
from __future__ import annotations
```

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/resolvers/access_type_classifier.py](../converter/resolvers/access_type_classifier.md)
- [converter/resolvers/cursor_order_by_resolver.py](../converter/resolvers/cursor_order_by_resolver.md)
- [rules/update_sql_cleanup_rules.py](update_sql_cleanup_rules.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
