# `rules/unnecessary_comments_rules.py`

Source: [rules/unnecessary_comments_rules.py](../../../rules/unnecessary_comments_rules.py) | 29 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `186f59cc7031927391aef374434718e1ea7d8d3143b784b0b53172794a101225`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Generated comment cleanup policy.

## Module-level bindings

`REMOVE_NOISE_MARKERS` (L15), `REMOVE_TRACE_MARKERS` (L20), `MARKER_CLEANUP_MESSAGE` (L23), `__all__` (L25)

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/unnecessary_comments_cleanup_composer.py](../converter/composers/unnecessary_comments_cleanup_composer.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
