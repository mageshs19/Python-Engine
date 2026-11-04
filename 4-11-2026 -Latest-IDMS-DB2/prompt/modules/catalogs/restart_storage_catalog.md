# `catalogs/restart_storage_catalog.py`

Source: [catalogs/restart_storage_catalog.py](../../../catalogs/restart_storage_catalog.py) | 153 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `589215b678b047567525f3b955a59356329a01cba43e34022772da59dd07e229`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Site vocabulary for the restart working storage.

## Module-level bindings

`SWITCH_GROUP` (L48), `HELP_GROUP` (L49), `DATE_GROUP` (L50), `EOF_SWITCH_PREFIX` (L58), `EOF_CONDITION_SUFFIX` (L59), `NOT_EOF_CONDITION_SUFFIX` (L60), `GENERATED_STORAGE_FIELDS` (L72), `GENERATED_EOF_CONDITIONS` (L84), `DEFAULT_READ_COUNT_SIZE` (L104), `DEFAULT_RESTART_KEY_SIZE` (L105), `DATE_GROUP_LINES` (L113), `__all__` (L141)

## Import declarations

```python
from __future__ import annotations
```

## Importers (7)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/restart/restart_stage_adapter.py](../converter/composers/restart/restart_stage_adapter.md)
- [converter/composers/restart/restart_storage_injector.py](../converter/composers/restart/restart_storage_injector.md)
- [converter/generators/restart/restart_name_resolver.py](../converter/generators/restart/restart_name_resolver.md)
- [converter/generators/restart/restart_storage_builder.py](../converter/generators/restart/restart_storage_builder.md)
- [tests/restart/test_m11_storage_builder.py](../tests/restart/test_m11_storage_builder.md)
- [tests/restart/test_m11b_storage_injector.py](../tests/restart/test_m11b_storage_injector.md)
- [tests/restart/test_m3_name_resolver.py](../tests/restart/test_m3_name_resolver.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
