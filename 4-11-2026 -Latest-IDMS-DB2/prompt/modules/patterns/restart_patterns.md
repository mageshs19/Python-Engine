# `patterns/restart_patterns.py`

Source: [patterns/restart_patterns.py](../../../patterns/restart_patterns.py) | 225 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `1edef18517b7ecbee92b280de708ff7a752cbbd2eb8756cb7085ecc13acaa598`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Restart / checkpoint regex patterns.

## Module-level bindings

`PARAGRAPH_HEADER_PATTERN` (L49), `PARAGRAPH_NUMBER_PATTERN` (L55), `PROCEDURE_DIVISION_PATTERN` (L59), `WORKING_STORAGE_PATTERN` (L64), `FILE_SECTION_PATTERN` (L69), `LINKAGE_SECTION_PATTERN` (L74), `OPEN_INPUT_PATTERN` (L83), `CLOSE_FILE_PATTERN` (L88), `STOP_RUN_PATTERN` (L93), `PERFORM_UNTIL_PATTERN` (L101), `PERFORM_SIMPLE_PATTERN` (L108), `LEVEL_88_PATTERN` (L117), `ELEMENTARY_ITEM_PATTERN` (L123), `PICTURE_SIZE_PATTERN` (L131), `FD_PATTERN` (L136), `READ_INTO_PATTERN` (L141), `SQL_INCLUDE_PATTERN` (L150), `LEVEL_77_HEADER_PATTERN` (L156), `VALUE_LINE_PATTERN` (L163), `LEVEL_77_WITH_VALUE_PATTERN` (L175), `INLINE_COMMIT_PATTERN` (L182), `ORPHAN_SCOPE_TERMINATOR_PATTERN` (L187), `DOUBLE_PERIOD_PATTERN` (L192), `TRAILING_SEQUENCE_LEAK_PATTERN` (L196), `__all__` (L200)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (6)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/restart/legacy_restart_cleanup.py](../converter/composers/restart/legacy_restart_cleanup.md)
- [converter/composers/restart/process_paragraph_injector.py](../converter/composers/restart/process_paragraph_injector.md)
- [converter/composers/restart/restart_injection_geometry.py](../converter/composers/restart/restart_injection_geometry.md)
- [converter/generators/restart/restart_name_resolver.py](../converter/generators/restart/restart_name_resolver.md)
- [converter/generators/restart/restart_sql_builder.py](../converter/generators/restart/restart_sql_builder.md)
- [tests/restart/test_m1_restart_standards.py](../tests/restart/test_m1_restart_standards.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
