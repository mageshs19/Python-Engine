# `patterns/cursor_spec/__init__.py`

Source: [patterns/cursor_spec/__init__.py](../../../../patterns/cursor_spec/__init__.py) | 60 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `88a1db03f2e032e1fd1c551acf20530edb4ac502357b8403b5f190f135c7f41d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Regex for the generated LRF expansion comments.

## Module-level bindings

`_MODE` (L33), `_NAME` (L34), `LRF_EXPANSION_PATTERN` (L36), `LRF_EXPANSION_WRAPPED_PATTERN` (L42), `LRF_CONTINUATION_RECORD_PATTERN` (L51), `__all__` (L56)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure/spec_builder/spec_lrf_scanner.py](../../converter/generators/db2_infrastructure/spec_builder/spec_lrf_scanner.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
