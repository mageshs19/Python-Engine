# `converter/services/program_flow_models.py`

Source: [converter/services/program_flow_models.py](../../../../converter/services/program_flow_models.py) | 96 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `2d8152aeea6ba76f14f5f4360281ec36df5e2a24974f8897f2303689b5ec2020`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass, field
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [converter/services/name_normalizer.py](name_normalizer.md)

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/services/program_cursor_loop_analyzer.py](program_cursor_loop_analyzer.md)
- [converter/services/program_date_usage_analyzer.py](program_date_usage_analyzer.md)
- [converter/services/program_flow_analyzer.py](program_flow_analyzer.md)
- [converter/services/program_output_write_analyzer.py](program_output_write_analyzer.md)
- [converter/services/program_paragraph_analyzer.py](program_paragraph_analyzer.md)

## Symbol contracts and control points

### `ParagraphSpan` - L9-L13

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

### `CursorLoop` - L17-L29

```python
class CursorLoop()
```

Declared class/data-model fields:

```python
record_name: str = ''
set_name: str = ''
operation: str = ''
operation_line: int = 0
process_paragraph: str = ''
perform_line: int = 0
until_line: int = 0
loop_type: str = 'unknown'
cursor_name: str = ''
open_paragraph: str = ''
fetch_paragraph: str = ''
close_paragraph: str = ''
```

### `OutputWrite` - L33-L37

```python
class OutputWrite()
```

Declared class/data-model fields:

```python
output_record: str = ''
paragraph_name: str = ''
write_line: int = 0
move_lines: list[str] = field(default_factory=list)
```

### `DateUsage` - L41-L47

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

### `ProgramFlowAnalysis` - L51-L96

```python
class ProgramFlowAnalysis()
```

Declared class/data-model fields:

```python
paragraphs: list[ParagraphSpan] = field(default_factory=list)
cursor_loops: list[CursorLoop] = field(default_factory=list)
output_writes: list[OutputWrite] = field(default_factory=list)
date_usages: list[DateUsage] = field(default_factory=list)
diagnostics: list[str] = field(default_factory=list)
```

### `ProgramFlowAnalysis.process_paragraph_for_cursor` - L58-L72

```python
process_paragraph_for_cursor(self, cursor_name: str) -> str
```

Observed calls (lexical order): `NameNormalizer.normalize`, `NameNormalizer.to_cobol`.

Control points:

- L64: `for loop in self.cursor_loops`
- L69: `if loop_cursor == cursor`

### `ProgramFlowAnalysis.loop_for_set` - L74-L84

```python
loop_for_set(self, set_name: str) -> CursorLoop | None
```

Observed calls (lexical order): `NameNormalizer.normalize`.

Control points:

- L80: `for loop in self.cursor_loops`
- L81: `if NameNormalizer.normalize(loop.set_name) == target`

### `ProgramFlowAnalysis.loop_for_record` - L86-L96

```python
loop_for_record(self, record_name: str) -> CursorLoop | None
```

Observed calls (lexical order): `NameNormalizer.normalize`.

Control points:

- L92: `for loop in self.cursor_loops`
- L93: `if NameNormalizer.normalize(loop.record_name) == target`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
