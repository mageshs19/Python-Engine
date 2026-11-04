# `rules/lrf_populator_rules.py`

Source: [rules/lrf_populator_rules.py](../../../rules/lrf_populator_rules.py) | 277 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `37c6b4e8b4aebfef5ab3ba2c8188646bd35ed1e11952d3fb18059b2b23350b58`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> LRF host-variable populator rules, geometry and diagnostics.

## Module-level bindings

`ENABLE_LRF_HOST_POPULATION` (L37), `ALLOW_AREA_SWEEP_PATHS` (L41), `REFUSE_ON_UNRESOLVED_PATH` (L44), `LRF_LEFT_SEQUENCE_WIDTH` (L50), `LRF_RIGHT_SEQUENCE_WIDTH` (L51), `LRF_BODY_WIDTH` (L52), `LRF_RECORD_WIDTH` (L53), `LRF_COMMENT_INDICATOR` (L57), `LRF_BLANK_INDICATOR` (L58), `LRF_STATEMENT_INDENT` (L61), `LRF_COMMENT_INDENT` (L62), `ENFORCE_LRF_BODY_WIDTH` (L67), `LRF_COMMAND_RECORD_ATTRIBUTES` (L77), `LRF_COMMAND_WITHIN_ATTRIBUTES` (L84), `LRF_CURSOR_BY_RECORD_METHODS` (L92), `LRF_TABLE_BY_RECORD_METHODS` (L96), `LRF_CURSOR_BY_TABLE_METHODS` (L102), `LRF_HOST_GROUP_BY_TABLE_METHODS` (L107), `LRF_PATH_COMMAND_ATTRIBUTES` (L112), `LRF_AREA_NAME_PREFIXES` (L117), `LRF_POPULATOR_MESSAGES` (L123), `__all__` (L258)

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/lrf_host_variable_populator.py](../converter/generators/lrf_host_variable_populator.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
