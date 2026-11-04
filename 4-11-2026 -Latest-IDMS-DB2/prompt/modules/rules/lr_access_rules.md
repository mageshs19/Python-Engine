# `rules/lr_access_rules.py`

Source: [rules/lr_access_rules.py](../../../rules/lr_access_rules.py) | 156 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `22b32cc10840397b0a385d27270c61fc1cc80f59c7ee6fd656bf64ab7f88f50b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> LR access classification vocabulary.

## Module-level bindings

`ENABLE_LR_ACCESS_ANALYSIS` (L46), `ENABLE_BOUNDED_SEARCH_RENDERING` (L50), `ENABLE_FIRST_ONLY_RENDERING` (L51), `ENABLE_LOOP_REMOVAL` (L52), `KIND_KEYED_READ` (L55), `KIND_FIRST_ONLY` (L56), `KIND_BOUNDED_SEARCH` (L57), `KIND_SWEEP` (L58), `KIND_DEFAULT` (L61), `LOOP_INLINE` (L64), `LOOP_PARAGRAPH` (L65), `LOOP_THRU` (L66), `LOOP_NONE` (L67), `END_OF_SET_CONDITIONS` (L75), `END_OF_SET_STATUS_FIELDS` (L89), `END_OF_SET_FLAG_SUFFIX` (L96), `CONDITION_CONNECTORS` (L99), `LR_ACCESS_MESSAGES` (L102), `__all__` (L137)

## Import declarations

```python
from __future__ import annotations
```

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/analyzers/lr_access/lr_access_analyser.py](../converter/analyzers/lr_access/lr_access_analyser.md)
- [converter/analyzers/lr_access/lr_access_models.py](../converter/analyzers/lr_access/lr_access_models.md)
- [converter/transformers/cobol_transformer.py](../converter/transformers/cobol_transformer.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
