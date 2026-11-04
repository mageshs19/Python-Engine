# `rules/field_usage_rules.py`

Source: [rules/field_usage_rules.py](../../../rules/field_usage_rules.py) | 27 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `ebaea5e59440e8a41d03d6ba17a5de24ab40eddbfd6e3c92c16095fe6c1af2cd`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`FIELD_USAGE_ANALYSIS_RULES` (L12), `DCLGEN_GROUP_PREFIX` (L22), `OUTPUT_TARGET_PREFIXES` (L25)

## Import declarations

```python
from __future__ import annotations
```

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/analyzers/field_usage_capture_service.py](../converter/analyzers/field_usage_capture_service.md)
- [converter/analyzers/field_usage_context_mapper.py](../converter/analyzers/field_usage_context_mapper.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
