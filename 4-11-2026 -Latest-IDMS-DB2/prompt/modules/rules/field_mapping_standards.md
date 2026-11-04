# `rules/field_mapping_standards.py`

Source: [rules/field_mapping_standards.py](../../../rules/field_mapping_standards.py) | 191 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `d63273de48919c0a5a270720f5129375ebc85f290a3c696f89f81b49c493698c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Field Mapping and MOVE Statement Standards (Issue #2).

## Module-level bindings

`QUALIFIED_FIELD_MOVE_PATTERN` (L127), `UNQUALIFIED_FIELD_MOVE_PATTERN` (L131), `FIELD_MAPPING_VALIDATION_RULES` (L138), `FORBIDDEN_FIELD_MOVE_PATTERNS` (L152), `PREMOVE_ACTIONS` (L160), `FIELD_MAPPING_MESSAGES` (L170)

## Import declarations

```python
from __future__ import annotations
```

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
