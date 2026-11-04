# `converter/services/program_output_write_analyzer.py`

Source: [converter/services/program_output_write_analyzer.py](../../../../converter/services/program_output_write_analyzer.py) | 57 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `02af9f853a853b3e38f1f853c3c712c8c09a22655356f347dce8ab12487a1d3f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.services.name_normalizer import NameNormalizer
from converter.services.program_flow_models import OutputWrite, ParagraphSpan
from converter.services.program_paragraph_analyzer import ProgramParagraphAnalyzer
from rules.program_flow_rules import WRITE_TOKENS
```

## Local dependency notes

- [converter/services/name_normalizer.py](name_normalizer.md)
- [converter/services/program_flow_models.py](program_flow_models.md)
- [converter/services/program_paragraph_analyzer.py](program_paragraph_analyzer.md)
- [rules/program_flow_rules.py](../../rules/program_flow_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/services/program_flow_analyzer.py](program_flow_analyzer.md)

## Symbol contracts and control points

### `ProgramOutputWriteAnalyzer` - L11-L57

```python
class ProgramOutputWriteAnalyzer()
```

Detects basic output write statements for diagnostics.

### `ProgramOutputWriteAnalyzer.__init__` - L18-L22

```python
__init__(self, paragraph_analyzer: ProgramParagraphAnalyzer | None=None) -> None
```

Observed calls (lexical order): `ProgramParagraphAnalyzer`.

### `ProgramOutputWriteAnalyzer.output_writes` - L24-L46

```python
output_writes(self, logical_lines: list[tuple[int, str, str]], paragraphs: list[ParagraphSpan]) -> list[OutputWrite]
```

Observed calls (lexical order): `self.paragraph_analyzer.paragraph_name_by_line`, `logical.strip`, `logical.strip().upper`, `any`, `upper.startswith`, `output.append`, `OutputWrite`, `self.first_word_after_operation`, `paragraph_by_line.get`.

Control points:

- L32: `for (line_number, logical, _raw_line) in logical_lines`
- L35: `if not any((upper.startswith(token) for token in WRITE_TOKENS))`

### `ProgramOutputWriteAnalyzer.first_word_after_operation` - L48-L57

```python
first_word_after_operation(self, upper_line: str) -> str
```

Observed calls (lexical order): `upper_line.split`, `len`, `NameNormalizer.normalize`, `parts[1].rstrip`.

Control points:

- L54: `if len(parts) < 2`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
