# `converter/services/program_paragraph_analyzer.py`

Source: [converter/services/program_paragraph_analyzer.py](../../../../converter/services/program_paragraph_analyzer.py) | 63 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `c78f07f83b7e05c3d4186cfb1238038677ec4f7ef34d291016f5c86874c6a603`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.services.program_flow_models import ParagraphSpan
from patterns.cobol_patterns import PARAGRAPH_PATTERN, PROCEDURE_DIVISION_PATTERN
```

## Local dependency notes

- [converter/services/program_flow_models.py](program_flow_models.md)
- [patterns/cobol_patterns.py](../../patterns/cobol_patterns.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/services/program_flow_analyzer.py](program_flow_analyzer.md)
- [converter/services/program_output_write_analyzer.py](program_output_write_analyzer.md)

## Symbol contracts and control points

### `ProgramParagraphAnalyzer` - L7-L63

```python
class ProgramParagraphAnalyzer()
```

Detects Procedure Division paragraph spans.

### `ProgramParagraphAnalyzer.paragraph_spans` - L14-L51

```python
paragraph_spans(self, logical_lines: list[tuple[int, str, str]]) -> list[ParagraphSpan]
```

Observed calls (lexical order): `PROCEDURE_DIVISION_PATTERN.match`, `PARAGRAPH_PATTERN.match`, `logical.strip`, `paragraphs.append`, `ParagraphSpan`, `match.group`, `match.group('name').upper`, `current.lines.append`.

Control points:

- L22: `for (line_number, logical, raw_line) in logical_lines`
- L23: `if PROCEDURE_DIVISION_PATTERN.match(logical)`
- L26: `if not inside_procedure`
- L31: `if match`
- L32: `if current is not None`
- L44: `if current is not None`
- L48: `if current is not None`

### `ProgramParagraphAnalyzer.paragraph_name_by_line` - L53-L63

```python
paragraph_name_by_line(self, paragraphs: list[ParagraphSpan]) -> dict[int, str]
```

Observed calls (lexical order): `range`.

Control points:

- L59: `for paragraph in paragraphs`
- L60: `for line_number in range(paragraph.start_line, paragraph.end_line + 1)`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
