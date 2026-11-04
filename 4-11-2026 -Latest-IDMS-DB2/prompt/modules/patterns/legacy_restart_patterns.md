# `patterns/legacy_restart_patterns.py`

Source: [patterns/legacy_restart_patterns.py](../../../patterns/legacy_restart_patterns.py) | 267 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `2e62169b03265a33a82ff1cf0d200e05ff2c9ae6794568f17809ba1a299c9791`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Regex for the legacy restart generator.

## Module-level bindings

`IDENTIFICATION_DIVISION_PATTERN` (L36), `DATA_DIVISION_PATTERN` (L39), `PROCEDURE_DIVISION_PATTERN` (L42), `FILE_SECTION_PATTERN` (L45), `WORKING_STORAGE_PATTERN` (L48), `LINKAGE_SECTION_PATTERN` (L51), `WORKING_STORAGE_END_PATTERN` (L56), `PROGRAM_ID_PATTERN` (L64), `LEVEL_01_PATTERN` (L72), `LEVEL_77_PATTERN` (L73), `ANY_LEVEL_PATTERN` (L75), `LEVEL_88_TRUE_PATTERN` (L82), `PICTURE_SIZE_PATTERN` (L87), `PARAGRAPH_HEADER_PATTERN` (L95), `TERMINATION_PATTERN` (L99), `CLOSE_STATEMENT_PATTERN` (L103), `OPEN_STATEMENT_PATTERN` (L107), `PERFORM_PATTERN` (L112), `PERFORM_UNTIL_PATTERN` (L116), `EXECUTABLE_START_PATTERN` (L122), `AT_END_MOVE_PATTERN` (L132), `AT_END_SET_PATTERN` (L138), `EXEC_SQL_OPEN_PATTERN` (L146), `EXEC_SQL_CLOSE_PATTERN` (L149), `SQL_INCLUDE_PATTERN` (L152), `SQL_VERB_PATTERN` (L156), `CONVERTED_UPDATE_MARKER_PATTERN` (L165), `KEEP_MARKER_PATTERN` (L171), `SEQUENCE_BLEED_PATTERN` (L181), `LONE_PERIOD_PATTERN` (L184), `__all__` (L231)

## Import declarations

```python
from __future__ import annotations
import re
```

## Symbol contracts and control points

### `paragraph_pattern` - L189-L194

```python
paragraph_pattern(name: str) -> re.Pattern[str]
```

Match exactly the paragraph header ``<name>.``

Observed calls (lexical order): `re.compile`, `re.escape`, `str`, `str(name or '').strip`.

### `perform_pattern` - L197-L202

```python
perform_pattern(name: str) -> re.Pattern[str]
```

Match a PERFORM of exactly this paragraph.

Observed calls (lexical order): `re.compile`, `re.escape`, `str`, `str(name or '').strip`.

### `group_header_pattern` - L205-L210

```python
group_header_pattern(name: str) -> re.Pattern[str]
```

Match ``01 <name>`` at any 01-level spelling.

Observed calls (lexical order): `re.compile`, `re.escape`, `str`, `str(name or '').strip`.

### `data_name_pattern` - L213-L219

```python
data_name_pattern(name: str) -> re.Pattern[str]
```

Match a whole-word reference to one data name.

Observed calls (lexical order): `re.compile`, `re.escape`, `str`, `str(name or '').strip`.

### `include_pattern` - L222-L228

```python
include_pattern(name: str) -> re.Pattern[str]
```

Match an EXEC SQL INCLUDE of exactly this member.

Observed calls (lexical order): `re.compile`, `re.escape`, `str`, `str(name or '').strip`.

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
