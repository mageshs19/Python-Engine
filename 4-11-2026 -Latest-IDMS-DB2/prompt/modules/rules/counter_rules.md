# `rules/counter_rules.py`

Source: [rules/counter_rules.py](../../../rules/counter_rules.py) | 115 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `565cb7e897da4b0e9b6b2cc5cef9084a8868af74a6dc13eb5009a251ac5a2747`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Row counter and program-name constant rules.

## Module-level bindings

`EMIT_PROGRAM_NAME_CONSTANT` (L17), `PROGRAM_CONSTANT_NAME` (L19), `PROGRAM_CONSTANT_TEMPLATE` (L22), `PROGRAM_NAME_TARGET_FIELD` (L26), `PROGRAM_NAME_MOVE_TEMPLATE` (L29), `PROGRAM_CONSTANT_STYLE_NOTE` (L32), `EMIT_ROW_COUNTERS` (L41), `COUNTER_NAME_TEMPLATE` (L43), `COUNTER_PICTURE` (L44), `COUNTER_DECLARATION_TEMPLATE` (L45), `OUTPUT_COUNTER_NAME` (L48), `OUTPUT_COUNTER_TOKEN` (L49), `COUNTER_ADD_TEMPLATE` (L51), `EMIT_COUNTER_TOTALS` (L56), `COUNTER_DISPLAY_TEMPLATE` (L58), `COUNTER_LABEL_WIDTH` (L59), `COUNTER_LABEL_FETCH_TEMPLATE` (L60), `COUNTER_LABEL_OUTPUT` (L61), `COUNTER_TOTALS_ANCHOR` (L65), `COUNTER_MESSAGES` (L70), `COUNTER_TOTAL_NAME_PREFIX` (L85), `COUNTER_TOTAL_LABEL_BY_SUFFIX` (L89), `COUNTER_TOTAL_LABEL_DEFAULT` (L93), `COUNTER_TOTAL_MESSAGES` (L95), `COUNTER_TOTAL_GUARANTEED_ROLES` (L106)

## Import declarations

```python
from __future__ import annotations
```

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/restart/restart_stage_adapter.py](../converter/composers/restart/restart_stage_adapter.md)
- [converter/generators/counter_generator.py](../converter/generators/counter_generator.md)
- [converter/generators/restart/restart_totals_resolver.py](../converter/generators/restart/restart_totals_resolver.md)
- [rules/counter_declaration_rules.py](counter_declaration_rules.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
