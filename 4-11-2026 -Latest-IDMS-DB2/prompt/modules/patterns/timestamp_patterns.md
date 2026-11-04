# `patterns/timestamp_patterns.py`

Source: [patterns/timestamp_patterns.py](../../../patterns/timestamp_patterns.py) | 112 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `affbd614f68ec53b038981f320f78608f6109001182462ecf95d39124f36c911`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`PROCEDURE_DIVISION_PATTERN` (L5), `WORKING_STORAGE_PATTERN` (L10), `LINKAGE_SECTION_PATTERN` (L15), `END_PROGRAM_PATTERN` (L20), `STOP_RUN_PATTERN` (L25), `EXEC_SQL_PATTERN` (L30), `END_EXEC_PATTERN` (L35), `DB2_WRITE_OPERATION_PATTERN` (L40), `COBOL_WRITE_OPERATION_PATTERN` (L45), `LEVEL_ENTRY_PATTERN` (L50), `STANDALONE_LEVEL_PATTERN` (L55), `__all__` (L95)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/timestamp/program_name_binder.py](../converter/generators/timestamp/program_name_binder.md)
- [converter/generators/timestamp/timestamp_anchors.py](../converter/generators/timestamp/timestamp_anchors.md)
- [converter/generators/timestamp_generator.py](../converter/generators/timestamp_generator.md)

## Symbol contracts and control points

### `declaration_pattern` - L61-L65

```python
declaration_pattern(field: str) -> re.Pattern
```

Observed calls (lexical order): `re.compile`, `re.escape`, `str`.

### `paragraph_header_pattern` - L68-L72

```python
paragraph_header_pattern(name: str) -> re.Pattern
```

Observed calls (lexical order): `re.compile`, `re.escape`, `str`.

### `perform_pattern` - L75-L79

```python
perform_pattern(name: str) -> re.Pattern
```

Observed calls (lexical order): `re.compile`, `re.escape`, `str`.

### `literal_move_pattern` - L81-L85

```python
literal_move_pattern(field: str) -> re.Pattern
```

Observed calls (lexical order): `re.compile`, `re.escape`, `str`.

### `constant_move_pattern` - L88-L93

```python
constant_move_pattern(constant: str, field: str) -> re.Pattern
```

Observed calls (lexical order): `re.compile`, `re.escape`, `str`.

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
