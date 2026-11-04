# `rules/update_restart_skip_rules.py`

Source: [rules/update_restart_skip_rules.py](../../../rules/update_restart_skip_rules.py) | 49 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `cb41893a800fb680f88cfaf632b59f384fcde7f934621a6c157094ae378bc120`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`MISSING_MAPPING_MARKERS` (L7), `RESTART_CONTROL_HINTS` (L22), `REPLACEMENT_BLOCK_TEMPLATES` (L33), `EMIT_MANUAL_REDESIGN_MESSAGE` (L43), `MANUAL_REDESIGN_MESSAGE_TEMPLATE` (L45)

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/update_restart_skip_composer.py](../converter/composers/update_restart_skip_composer.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
