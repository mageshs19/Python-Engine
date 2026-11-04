# `rules/update_char_literal_rules.py`

Source: [rules/update_char_literal_rules.py](../../../rules/update_char_literal_rules.py) | 27 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `7e920769fd8e09d286cdeaa625afb62ddf04b7fa9c31f6a4646c6568ad8d2806`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`UPDATE_CHAR_LITERAL_RULES` (L8), `CHAR_DB2_TYPE_PREFIXES` (L19), `CHAR_PICTURE_PREFIX` (L22), `CHAR_LITERAL_QUOTED_DIAGNOSTIC` (L25)

## Import declarations

```python
from __future__ import annotations
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/update_char_literal_quoter.py](../converter/postprocess/update_char_literal_quoter.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
