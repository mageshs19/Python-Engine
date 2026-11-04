# `patterns/cursor_spec/lrf_comment_patterns.py`

Source: [patterns/cursor_spec/lrf_comment_patterns.py](../../../../patterns/cursor_spec/lrf_comment_patterns.py) | 80 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `974a13fbe1e12d2ff1cd7964ef43b6a27e69796e70a06bf0ad98845013004342`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Regex for the generated LRF expansion comments.

## Module-level bindings

`_MODE` (L33), `_NAME` (L34), `LRF_ACCESS_MARKER_PROBE` (L36), `LRF_EXPANSION_PATTERN` (L41), `LRF_EXPANSION_WRAPPED_PATTERN` (L47), `LRF_EXPANSION_WRAPPED_NO_ARROW_PATTERN` (L53), `LRF_CONTINUATION_ARROW_PATTERN` (L60), `LRF_CONTINUATION_RECORD_PATTERN` (L67), `__all__` (L73)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/lrf_host_variable_populator.py](../../converter/generators/lrf_host_variable_populator.md)
- [converter/resolvers/lrf_cursor_where_resolver.py](../../converter/resolvers/lrf_cursor_where_resolver.md)
- [tests/test_lrf_two_stage_contract_v26.py](../../tests/test_lrf_two_stage_contract_v26.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
