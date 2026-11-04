# `rules/update_storage_include_rules.py`

Source: [rules/update_storage_include_rules.py](../../../rules/update_storage_include_rules.py) | 61 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `3dd8369a1cb6a14f13224111027819d6adc45da0b7578c4bea2fa64b6d29cc89`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`EXCLUDED_INCLUDE_NAMES` (L7), `DCL_GROUP_PREFIX` (L10), `WS_ANCHOR_01_TEMPLATE` (L13), `DATE_WS_ANCHORS` (L14), `CS_PROGRAM_77_TEMPLATE` (L17), `PROGRAM_NAME_MOVE_REPLACEMENT_TEMPLATE` (L20), `SKIP_DATA_DIVISION_WS` (L23), `SKIP_DATA_DIVISION_DATE_WS` (L27), `SKIP_DATA_DIVISION_DCLGEN_TEMPLATE` (L31), `SKIP_DATA_DIVISION_REFERENCED` (L35), `SKIP_DATA_DIVISION_COPYBOOK_TEMPLATE` (L39), `RESTART_DCLGEN_UNAVAILABLE` (L43), `DCLGEN_INCLUDE_EXISTS_TEMPLATE` (L47), `DCLGEN_INCLUDE_INJECTED_TEMPLATE` (L48), `REFERENCED_DCLGEN_INJECTED_TEMPLATE` (L49), `COPY_EXISTS_TEMPLATE` (L50), `COPY_EXISTS_BY_RECORD_TEMPLATE` (L51), `COPY_INJECTED_TEMPLATE` (L54), `DATE_WS_EXISTS_UNDER_OTHER_GROUP` (L56)

## Import declarations

```python
from __future__ import annotations
```

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/storage_include/storage_include_injector.py](../converter/postprocess/storage_include/storage_include_injector.md)
- [converter/postprocess/storage_include/storage_ws_injector.py](../converter/postprocess/storage_include/storage_ws_injector.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
