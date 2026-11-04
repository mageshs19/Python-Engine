# `converter/generators/timestamp/timestamp_anchors.py`

Source: [converter/generators/timestamp/timestamp_anchors.py](../../../../../converter/generators/timestamp/timestamp_anchors.py) | 109 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `967f71775ef0290d4c02cd826259ff50125af19dbdde6108a21ebb95556bc146`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`NOT_FOUND` (L17), `__all__` (L109)

## Import declarations

```python
from __future__ import annotations
from typing import List
from converter.generators.initialization.line_geometry import LineGeometry
from patterns.timestamp_patterns import END_PROGRAM_PATTERN, LINKAGE_SECTION_PATTERN, PROCEDURE_DIVISION_PATTERN, STOP_RUN_PATTERN, WORKING_STORAGE_PATTERN, declaration_pattern, paragraph_header_pattern, perform_pattern
```

## Local dependency notes

- [converter/generators/initialization/line_geometry.py](../initialization/line_geometry.md)
- [patterns/timestamp_patterns.py](../../../patterns/timestamp_patterns.md)

## Importers (6)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/timestamp/__init__.py](__init__.md)
- [converter/generators/timestamp/cs_program_declarator.py](cs_program_declarator.md)
- [converter/generators/timestamp/program_name_binder.py](program_name_binder.md)
- [converter/generators/timestamp/timestamp_paragraph_builder.py](timestamp_paragraph_builder.md)
- [converter/generators/timestamp/timestamp_ws_builder.py](timestamp_ws_builder.md)
- [converter/generators/timestamp_generator.py](../timestamp_generator.md)

## Symbol contracts and control points

### `TimestampAnchors` - L20-L106

```python
class TimestampAnchors()
```

### `TimestampAnchors.__init__` - L22-L23

```python
__init__(self, geometry: LineGeometry | None=None) -> None
```

Observed calls (lexical order): `LineGeometry`.

### `TimestampAnchors.bodies` - L25-L26

```python
bodies(self, lines: List[str]) -> List[str]
```

Observed calls (lexical order): `self.geometry.body`.

### `TimestampAnchors.index_of` - L28-L34

```python
index_of(self, lines: List[str], pattern) -> int
```

Observed calls (lexical order): `enumerate`, `self.geometry.is_comment_or_blank`, `pattern.match`, `self.geometry.body`.

Control points:

- L29: `for (index, line) in enumerate(lines)`
- L30: `if self.geometry.is_comment_or_blank(line)`
- L32: `if pattern.match(self.geometry.body(line))`

### `TimestampAnchors.procedure_division_index` - L36-L37

```python
procedure_division_index(self, lines: List[str]) -> int
```

Observed calls (lexical order): `self.index_of`.

### `TimestampAnchors.working_storage_index` - L39-L40

```python
working_storage_index(self, lines: List[str]) -> int
```

Observed calls (lexical order): `self.index_of`.

### `TimestampAnchors.linkage_section_index` - L42-L43

```python
linkage_section_index(self, lines: List[str]) -> int
```

Observed calls (lexical order): `self.index_of`.

### `TimestampAnchors.stop_run_index` - L45-L46

```python
stop_run_index(self, lines: List[str]) -> int
```

Observed calls (lexical order): `self.index_of`.

### `TimestampAnchors.end_program_index` - L48-L49

```python
end_program_index(self, lines: List[str]) -> int
```

Observed calls (lexical order): `self.index_of`.

### `TimestampAnchors.working_storage_insert_index` - L51-L64

```python
working_storage_insert_index(self, lines: List[str]) -> int
```

Observed calls (lexical order): `self.linkage_section_index`, `self.procedure_division_index`, `self.working_storage_index`.

Control points:

- L53: `if linkage >= 0`
- L57: `if procedure >= 0`
- L61: `if working_storage >= 0`

### `TimestampAnchors.paragraph_insert_index` - L66-L70

```python
paragraph_insert_index(self, lines: List[str]) -> int
```

Observed calls (lexical order): `self.end_program_index`, `len`.

Control points:

- L68: `if end_program >= 0`

### `TimestampAnchors.first_statement_index` - L72-L76

```python
first_statement_index(self, lines: List[str], after: int) -> int
```

Observed calls (lexical order): `len`, `range`, `self.geometry.is_comment_or_blank`.

Control points:

- L73: `for index in range(after + 1, len(lines))`
- L74: `if not self.geometry.is_comment_or_blank(lines[index])`

### `TimestampAnchors.has_paragraph` - L78-L79

```python
has_paragraph(self, lines: List[str], name: str) -> bool
```

Observed calls (lexical order): `paragraph_header_pattern`, `self.index_of`.

### `TimestampAnchors.has_perform` - L81-L82

```python
has_perform(self, lines: List[str], name: str) -> bool
```

Observed calls (lexical order): `perform_pattern`, `self.index_of`.

### `TimestampAnchors.perform_count` - L84-L92

```python
perform_count(self, lines: List[str], name: str) -> int
```

Observed calls (lexical order): `perform_pattern`, `self.geometry.is_comment_or_blank`, `pattern.match`, `self.geometry.body`.

Control points:

- L87: `for line in lines`
- L88: `if self.geometry.is_comment_or_blank(line)`
- L90: `if pattern.match(self.geometry.body(line))`

### `TimestampAnchors.declaration_level` - L94-L102

```python
declaration_level(self, lines: List[str], field: str) -> str
```

Observed calls (lexical order): `declaration_pattern`, `self.geometry.is_comment_or_blank`, `pattern.match`, `self.geometry.body`, `match.group`.

Control points:

- L96: `for line in lines`
- L97: `if self.geometry.is_comment_or_blank(line)`
- L100: `if match`

### `TimestampAnchors.has_marker` - L104-L106

```python
has_marker(self, lines: List[str], marker: str) -> bool
```

Observed calls (lexical order): `str`, `str(marker or '').upper`, `any`, `str(line or '').upper`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
