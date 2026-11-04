# `rules/db2_date_conversion_standards.py`

Source: [rules/db2_date_conversion_standards.py](../../../rules/db2_date_conversion_standards.py) | 244 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `fb552b5b7bb2224785f6f332716d37e5706cf223af5dba82a14b098fcb2e251e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Enhanced DB2 Date Conversion Standards (Issue #1).

## Module-level bindings

`ENFORCE_DATE_CONVERSION_STANDARD` (L131), `ENFORCE_DATE_CONVERSION_TIMING` (L132), `DB2_DATE_EDGE_CASES` (L137), `DATE_CONVERSION_WORKING_STORAGE_COMMENT` (L153), `DATE_CONVERSION_WORK_FIELDS` (L155), `HELPER_FIELD_TEMPLATE` (L177), `HELPER_NAMING_CONVENTION` (L179), `DATE_CONVERSION_SEQUENCE` (L184), `CONVERSION_TIMING_RULE` (L204), `VALIDATION_CHECKS` (L214), `DATE_CONVERSION_MESSAGES` (L225)

## Import declarations

```python
from __future__ import annotations
```

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
