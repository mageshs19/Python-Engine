# `rules/restart_storage_templates.py`

Source: [rules/restart_storage_templates.py](../../../rules/restart_storage_templates.py) | 115 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `a4ad56c2244acdc3b0d0d18524d66c441eacba812bbe0d04272ed80978f78ca8`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Working-storage SHAPES for the restart family.

## Module-level bindings

`ENFORCE_RESTART_STORAGE` (L26), `EOF_TRUE_VALUE` (L31), `EOF_FALSE_VALUE` (L32), `COMMIT_COUNTER_PICTURE` (L39), `INPUT_COUNTER_PICTURE` (L40), `SWITCH_GROUP_TEMPLATE` (L49), `HELP_GROUP_TEMPLATE` (L56), `AUDIT_MOVE_TEMPLATE` (L75), `RESTART_STORAGE_MESSAGES` (L83), `__all__` (L105)

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/restart/restart_storage_builder.py](../converter/generators/restart/restart_storage_builder.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
