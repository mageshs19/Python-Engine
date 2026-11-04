# `converter/generators/boilerplate_generator.py`

Source: [converter/generators/boilerplate_generator.py](../../../../converter/generators/boilerplate_generator.py) | 217 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `e13ea3bc8d9f07c36349b93c8ad0498069ba5d869e65f6f5c784d286404e1c6e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`__all__` (L217)

## Import declarations

```python
from __future__ import annotations
import re
from converter.generators.db2_infrastructure.include_renderer import IncludeRenderer
from converter.services.cobol_area_alignment_service import CobolAreaAlignmentService
from rules.boilerplate_rules import BOILERPLATE_DCLGEN_INCLUDES, BOILERPLATE_END_PROGRAM, BOILERPLATE_INCLUDE_INDENT, BOILERPLATE_MESSAGES
```

## Local dependency notes

- [converter/generators/db2_infrastructure/include_renderer.py](db2_infrastructure/include_renderer.md)
- [converter/services/cobol_area_alignment_service.py](../services/cobol_area_alignment_service.md)
- [rules/boilerplate_rules.py](../../rules/boilerplate_rules.md)

## Symbol contracts and control points

### `BoilerplateGenerator` - L22-L214

```python
class BoilerplateGenerator()
```

Adds final boilerplate: DCLGEN includes and END PROGRAM statement.

Declared class/data-model fields:

```python
WORKING_STORAGE_PATTERN = re.compile('^\\s*(?:\\d{6}\\s+)?WORKING-STORAGE\\s+SECTION\\.\\s*(?:\\d{8})?\\s*$', flags=re.IGNORECASE | re.MULTILINE)
PROCEDURE_DIVISION_PATTERN = re.compile('^\\s*(?:\\d{6}\\s+)?PROCEDURE\\s+DIVISION\\b.*\\.?\\s*(?:\\d{8})?\\s*$', flags=re.IGNORECASE | re.MULTILINE)
END_PROGRAM_PATTERN = re.compile('^\\s*(?:\\d{6}\\s+)?END\\s+PROGRAM\\b.*\\.?\\s*(?:\\d{8})?\\s*$', flags=re.IGNORECASE | re.MULTILINE)
STOP_RUN_PATTERN = re.compile('^\\s*(?:\\d{6}\\s+)?STOP\\s+RUN\\.?\\s*(?:\\d{8})?\\s*$', flags=re.IGNORECASE)
EXEC_SQL_INCLUDE_PATTERN = re.compile('^\\s*EXEC\\s+SQL\\s+INCLUDE\\s+\\w+\\s+END-EXEC', flags=re.IGNORECASE)
```

### `BoilerplateGenerator.__init__` - L57-L62

```python
__init__(self, line_utils=None) -> None
```

Observed calls (lexical order): `CobolAreaAlignmentService`.

### `BoilerplateGenerator.apply` - L64-L82

```python
apply(self, cobol_text: str, operations: list | None=None) -> tuple[str, list[str]]
```

Apply boilerplate enhancements to COBOL text.

Observed calls (lexical order): `str`, `self._ensure_dclgen_includes`, `self._ensure_end_program`, `text.rstrip`.

Control points:

- L73: `if not text`

### `BoilerplateGenerator._ensure_dclgen_includes` - L84-L141

```python
_ensure_dclgen_includes(self, text: str) -> str
```

Ensure DCLGEN and DB2 infrastructure includes are present.

Observed calls (lexical order): `text.splitlines`, `self._find_pattern_index`, `self.messages.append`, `self._includes_exist`, `self._build_include_block`, `BOILERPLATE_MESSAGES['includes_added'].format`, `len`, `'\n'.join`.

Control points:

- L94: `if ws_index < 0`
- L106: `if pd_index < 0`
- L114: `if includes_exist`

### `BoilerplateGenerator._ensure_end_program` - L143-L166

```python
_ensure_end_program(self, text: str) -> str
```

Ensure END PROGRAM statement is present at end of program.

Observed calls (lexical order): `text.splitlines`, `self._logical_line`, `self.END_PROGRAM_PATTERN.match`, `self.messages.append`, `lines[-1].strip`, `'\n'.join`.

Control points:

- L148: `for line in lines`
- L150: `if self.END_PROGRAM_PATTERN.match(logical)`
- L157: `if lines and (not lines[-1].strip())`

### `BoilerplateGenerator._includes_exist` - L168-L179

```python
_includes_exist(self, lines: list[str], start_index: int, end_index: int) -> bool
```

Check if EXEC SQL INCLUDE statements exist in range.

Observed calls (lexical order): `len`, `min`, `range`, `self._logical_line`, `self.EXEC_SQL_INCLUDE_PATTERN.match`.

Control points:

- L175: `for i in range(start_index, min(end_index, len(lines)))`
- L177: `if self.EXEC_SQL_INCLUDE_PATTERN.match(logical)`

### `BoilerplateGenerator._build_include_block` - L181-L192

```python
_build_include_block(self) -> list[str]
```

Build the DCLGEN include block lines.

Observed calls (lexical order): `includes.append`.

Control points:

- L185: `for include_name in BOILERPLATE_DCLGEN_INCLUDES`

### `BoilerplateGenerator._find_pattern_index` - L194-L204

```python
_find_pattern_index(self, lines: list[str], pattern: re.Pattern) -> int
```

Find the first line matching the pattern.

Observed calls (lexical order): `enumerate`, `self._logical_line`, `pattern.match`.

Control points:

- L200: `for (index, line) in enumerate(lines)`
- L202: `if pattern.match(logical)`

### `BoilerplateGenerator._logical_line` - L206-L214

```python
_logical_line(self, line: str) -> str
```

Extract logical COBOL line (remove sequence area).

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`, `text[6:].strip`, `text.strip`.

Control points:

- L211: `if len(text) > 6 and text[:6].strip().isdigit()`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
