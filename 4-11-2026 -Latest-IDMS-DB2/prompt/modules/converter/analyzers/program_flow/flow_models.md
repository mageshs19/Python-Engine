# `converter/analyzers/program_flow/flow_models.py`

Source: [converter/analyzers/program_flow/flow_models.py](../../../../../converter/analyzers/program_flow/flow_models.py) | 126 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `2313dd662e0b77c1a436f4575e71881388f02f033f9a7fec5c0798fc686ef34f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Value objects for one program flow analysis.

## Module-level bindings

`__all__` (L123)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass, field
from converter.services.name_normalizer import NameNormalizer
from rules.program_flow_rules import LOOP_TYPE_UNKNOWN
```

## Local dependency notes

- [converter/services/name_normalizer.py](../../services/name_normalizer.md)
- [rules/program_flow_rules.py](../../../rules/program_flow_rules.md)

## Importers (9)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/analyzers/program_flow/__init__.py](__init__.md)
- [converter/analyzers/program_flow/flow_cursor_loop_scanner.py](flow_cursor_loop_scanner.md)
- [converter/analyzers/program_flow/flow_date_scanner.py](flow_date_scanner.md)
- [converter/analyzers/program_flow/flow_diagnostics.py](flow_diagnostics.md)
- [converter/analyzers/program_flow/flow_line_reader.py](flow_line_reader.md)
- [converter/analyzers/program_flow/flow_paragraph_scanner.py](flow_paragraph_scanner.md)
- [converter/analyzers/program_flow/flow_write_scanner.py](flow_write_scanner.md)
- [converter/analyzers/program_flow/program_flow_analyzer.py](program_flow_analyzer.md)
- [converter/analyzers/program_flow_analyzer.py](../program_flow_analyzer.md)

## Symbol contracts and control points

### `LogicalLine` - L17-L36

```python
class LogicalLine()
```

One source record reduced to its executable body.

Declared class/data-model fields:

```python
number: int = 0
logical: str = ''
raw: str = ''
is_comment: bool = False
```

### `LogicalLine.body` - L31-L32

```python
body(self) -> str
```

Observed calls (lexical order): `self.logical.strip`.

### `LogicalLine.upper` - L35-L36

```python
upper(self) -> str
```

Observed calls (lexical order): `self.body.upper`.

### `ParagraphSpan` - L40-L44

```python
class ParagraphSpan()
```

Declared class/data-model fields:

```python
name: str
start_line: int
end_line: int
lines: list[str] = field(default_factory=list)
```

### `CursorLoop` - L48-L61

```python
class CursorLoop()
```

Declared class/data-model fields:

```python
record_name: str = ''
table_name: str = ''
set_name: str = ''
operation: str = ''
operation_line: int = 0
process_paragraph: str = ''
perform_line: int = 0
until_line: int = 0
loop_type: str = LOOP_TYPE_UNKNOWN
cursor_name: str = ''
open_paragraph: str = ''
fetch_paragraph: str = ''
close_paragraph: str = ''
```

### `OutputWrite` - L65-L70

```python
class OutputWrite()
```

Declared class/data-model fields:

```python
output_record: str = ''
paragraph_name: str = ''
write_line: int = 0
verb: str = ''
move_lines: list[str] = field(default_factory=list)
```

### `DateUsage` - L74-L80

```python
class DateUsage()
```

Declared class/data-model fields:

```python
host_field: str = ''
dclgen_group: str = ''
idms_record: str = ''
line_number: int = 0
line_text: str = ''
usage_type: str = ''
```

### `ProgramFlowAnalysis` - L84-L120

```python
class ProgramFlowAnalysis()
```

Declared class/data-model fields:

```python
paragraphs: list[ParagraphSpan] = field(default_factory=list)
cursor_loops: list[CursorLoop] = field(default_factory=list)
output_writes: list[OutputWrite] = field(default_factory=list)
idms_writes: list[OutputWrite] = field(default_factory=list)
date_usages: list[DateUsage] = field(default_factory=list)
diagnostics: list[str] = field(default_factory=list)
```

### `ProgramFlowAnalysis.process_paragraph_for_cursor` - L92-L97

```python
process_paragraph_for_cursor(self, cursor_name: str) -> str
```

Observed calls (lexical order): `self._cobol`.

Control points:

- L94: `for loop in self.cursor_loops`
- L95: `if self._cobol(loop.cursor_name) == wanted`

### `ProgramFlowAnalysis.loop_for_set` - L99-L100

```python
loop_for_set(self, set_name: str) -> CursorLoop | None
```

Observed calls (lexical order): `self._first`.

### `ProgramFlowAnalysis.loop_for_record` - L102-L103

```python
loop_for_record(self, record_name: str) -> CursorLoop | None
```

Observed calls (lexical order): `self._first`.

### `ProgramFlowAnalysis.loop_for_table` - L105-L106

```python
loop_for_table(self, table_name: str) -> CursorLoop | None
```

Observed calls (lexical order): `self._first`.

### `ProgramFlowAnalysis._first` - L109-L116

```python
_first(self, reader, wanted: str) -> CursorLoop | None
```

Observed calls (lexical order): `NameNormalizer.normalize`, `reader`.

Control points:

- L111: `if not target`
- L113: `for loop in self.cursor_loops`
- L114: `if NameNormalizer.normalize(reader(loop)) == target`

### `ProgramFlowAnalysis._cobol` - L119-L120

```python
_cobol(value: str) -> str
```

Observed calls (lexical order): `NameNormalizer.normalize`, `NameNormalizer.to_cobol`.

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
