# `patterns/dynamic_metadata_patterns.py`

Source: [patterns/dynamic_metadata_patterns.py](../../../patterns/dynamic_metadata_patterns.py) | 194 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `121e279f9aabceb90d1310f712c7bcb3c5d1f5e569a24a2083f574561de3ec6e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Regex for the dynamic update-program metadata resolver.

## Module-level bindings

`PROGRAM_RE` (L44), `SELECT_RE` (L49), `READ_RE` (L54), `COPY_RE` (L59), `FIELD_USE_RE` (L64), `MOVE_FIELD_RE` (L69), `SELECT_LINE_RE` (L74), `FD_LINE_RE` (L79), `RECORD_CONTAINS_RE` (L84), `FD_RECORD_01_RE` (L89), `SECTION_END_RE` (L94), `READ_LINE_RE` (L99), `EOF_UNTIL_RE` (L108), `EOF_IF_RE` (L113), `EOF_MOVE_RE` (L118), `EOF_CONDITION_REF_RE` (L131), `EOF_ANY_MOVE_RE` (L138), `DECLARED_88_RE` (L146), `RELATIONAL_HEAD_RE` (L153), `QUALIFIER_RE` (L161), `PIC_LENGTH_RE` (L166), `PROCEDURE_DIVISION_RE` (L173), `AT_END_SET_TRUE_RE` (L181), `CONDITION_WORD_TEMPLATE` (L188), `WRITE_TO_NAME_TEMPLATE` (L192)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/legacy_eof_condition_rewriter.py](../converter/postprocess/legacy_eof_condition_rewriter.md)
- [converter/postprocess/update_cobol_file_resolver.py](../converter/postprocess/update_cobol_file_resolver.md)
- [converter/postprocess/update_copybook_resolver.py](../converter/postprocess/update_copybook_resolver.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
