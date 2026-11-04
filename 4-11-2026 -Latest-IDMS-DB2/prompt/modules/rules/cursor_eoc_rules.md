# `rules/cursor_eoc_rules.py`

Source: [rules/cursor_eoc_rules.py](../../../rules/cursor_eoc_rules.py) | 44 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `77f4a91dfad656aba485cf499ec64f309846352a51af32872f74e771cb63554b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> The end-of-cursor vocabulary. ONE definition.

## Module-level bindings

`LEGACY_EOC_CONDITIONS` (L29), `EOC_CONDITION_TEMPLATE` (L37), `EOC_CONDITION_SUFFIX` (L38), `__all__` (L40)

## Import declarations

```python
from __future__ import annotations
```

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [patterns/cursor_flow_patterns.py](../patterns/cursor_flow_patterns.md)
- [rules/cursor_close_guarantee_rules.py](cursor_close_guarantee_rules.md)
- [rules/cursor_loop_rules.py](cursor_loop_rules.md)
- [tests/test_eoc_vocabulary_agrees_across_the_review_boundary.py](../tests/test_eoc_vocabulary_agrees_across_the_review_boundary.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
