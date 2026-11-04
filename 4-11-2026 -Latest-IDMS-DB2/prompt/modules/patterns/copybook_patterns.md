# `patterns/copybook_patterns.py`

Source: [patterns/copybook_patterns.py](../../../patterns/copybook_patterns.py) | 42 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `b2515463a6519b6365602d33bd9d2633f4c1026757a332648cbcd2b0b6cf7e9d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Copybook regex patterns.

## Module-level bindings

`COPYBOOK_FIELD_PATTERN` (L11), `COPYBOOK_PIC_PATTERN` (L19), `COPYBOOK_USAGE_PATTERN` (L26), `COPYBOOK_OCCURS_PATTERN` (L33), `COPYBOOK_COMMENT_OR_SKIP_PATTERN` (L39)

## Import declarations

```python
import re
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/parsers/copybook_parser.py](../converter/parsers/copybook_parser.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
