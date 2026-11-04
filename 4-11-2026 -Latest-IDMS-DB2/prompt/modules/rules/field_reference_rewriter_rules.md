# `rules/field_reference_rewriter_rules.py`

Source: [rules/field_reference_rewriter_rules.py](../../../rules/field_reference_rewriter_rules.py) | 98 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `b40c9406a0aba06f051eacc9916ff645f7e9a8d1d5e56370fb3cbcbdb2071247`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`FIELD_REFERENCE_REWRITE_RULES` (L12), `PROTECTED_BARE_PREFIXES` (L23), `DCLGEN_GROUP_PREFIX` (L48), `HOST_QUALIFIER_CONNECTOR` (L52), `HOST_REFERENCE_LEADING_CHAR` (L55), `HOST_OF_GROUP_TEMPLATE` (L58), `HOST_OF_SPLIT_PART_COUNT` (L61), `ENFORCE_FIXED_FORMAT_REWRITE` (L82), `ALLOW_REWRITE_WRAPPING` (L86), `FIELD_REFERENCE_GEOMETRY_MESSAGES` (L88), `COBOL_QUALIFIER` (L98)

## Import declarations

```python
from __future__ import annotations
```

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/transformers/field_reference/field_reference_host_resolver.py](../converter/transformers/field_reference/field_reference_host_resolver.md)
- [converter/transformers/field_reference_context_builder.py](../converter/transformers/field_reference_context_builder.md)
- [converter/transformers/field_reference_replacement_engine.py](../converter/transformers/field_reference_replacement_engine.md)
- [converter/transformers/field_reference_rewriter.py](../converter/transformers/field_reference_rewriter.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
