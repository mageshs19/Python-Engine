# `patterns/naming_patterns.py`

Source: [patterns/naming_patterns.py](../../../patterns/naming_patterns.py) | 38 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `f216389758132332f5ded885b07c4e1157d9b7e3cac721aa25f4c4e8233320b6`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Naming patterns and naming helpers.

## Module-level bindings

`NON_DB2_NAME_CHARACTER_PATTERN` (L11), `NON_COMPACT_NAME_CHARACTER_PATTERN` (L17), `MULTIPLE_UNDERSCORE_PATTERN` (L23), `DCL_PREFIX_PATTERN` (L29), `FOUR_DIGIT_RECORD_SUFFIX_PATTERN` (L35)

## Import declarations

```python
import re
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/services/name_normalizer.py](../converter/services/name_normalizer.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
