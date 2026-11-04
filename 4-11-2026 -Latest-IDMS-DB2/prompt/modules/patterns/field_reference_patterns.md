# `patterns/field_reference_patterns.py`

Source: [patterns/field_reference_patterns.py](../../../patterns/field_reference_patterns.py) | 20 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `bc57d6816829a336bab15c1442b176c9b7b923cf226a70fc669668f88c53a759`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`QUALIFIED_REFERENCE_PATTERN` (L4), `REDEFINES_PATTERN` (L11), `STRING_LITERAL_PATTERN` (L17)

## Import declarations

```python
import re
```

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
