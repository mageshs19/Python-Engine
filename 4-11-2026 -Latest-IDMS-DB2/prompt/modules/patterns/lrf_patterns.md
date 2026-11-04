# `patterns/lrf_patterns.py`

Source: [patterns/lrf_patterns.py](../../../patterns/lrf_patterns.py) | 67 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `87587278e1d3887a8dd6b10fa7ff995e99527514e0afd37cf7c6bea13381a3c2`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Regex for the IDMS subschema Logical Record Facility (LRF) source.

## Module-level bindings

`SUBSCHEMA_HEADER_PATTERN` (L9), `LOGICAL_RECORD_PATTERN` (L15), `ELEMENTS_ARE_PATTERN` (L20), `COMMENTS_PATTERN` (L21), `QUOTED_TEXT_PATTERN` (L22), `PATH_GROUP_PATTERN` (L24), `SELECT_KEYWORD_PATTERN` (L29), `FIND_OBTAIN_PATTERN` (L34), `ERASE_PATTERN` (L41), `IF_SET_EMPTY_PATTERN` (L43), `WHERE_PATTERN` (L48), `ON_STATUS_PATTERN` (L50), `ELEMENT_NAME_PATTERN` (L55), `COPY_IDMS_LR_PATTERN` (L58), `LR_QUALIFIED_FIELD_PATTERN` (L64)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/parsers/lrf_parser.py](../converter/parsers/lrf_parser.md)
- [converter/ui/conversion_actions.py](../converter/ui/conversion_actions.md)
- [runners/batch/program_converter.py](../runners/batch/program_converter.md)
- [runners/retrieval/retrieval_program_converter.py](../runners/retrieval/retrieval_program_converter.md)
- [runners/update/update_program_converter.py](../runners/update/update_program_converter.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
