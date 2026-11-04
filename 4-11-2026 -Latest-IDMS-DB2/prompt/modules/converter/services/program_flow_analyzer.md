# `converter/services/program_flow_analyzer.py`

Source: [converter/services/program_flow_analyzer.py](../../../../converter/services/program_flow_analyzer.py) | 139 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `a9ee11ae3653cb0005b91fd2b7410b2c07771cc7e2bdae54035c00733cd109d2`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`__all__` (L132)

## Import declarations

```python
from __future__ import annotations
from converter.domain.models import DclgenColumn, IdmsOperation, SheetMappingRow
from converter.resolvers.cursor_name_resolver import CursorNameResolver
from converter.services.program_cursor_loop_analyzer import ProgramCursorLoopAnalyzer
from converter.services.program_date_usage_analyzer import ProgramDateUsageAnalyzer
from converter.services.program_flow_line_collector import ProgramFlowLineCollector
from converter.services.program_flow_models import CursorLoop, DateUsage, OutputWrite, ParagraphSpan, ProgramFlowAnalysis
from converter.services.program_output_write_analyzer import ProgramOutputWriteAnalyzer
from converter.services.program_paragraph_analyzer import ProgramParagraphAnalyzer
```

## Local dependency notes

- [converter/domain/models.py](../domain/models.md)
- [converter/resolvers/cursor_name_resolver.py](../resolvers/cursor_name_resolver.md)
- [converter/services/program_cursor_loop_analyzer.py](program_cursor_loop_analyzer.md)
- [converter/services/program_date_usage_analyzer.py](program_date_usage_analyzer.md)
- [converter/services/program_flow_line_collector.py](program_flow_line_collector.md)
- [converter/services/program_flow_models.py](program_flow_models.md)
- [converter/services/program_output_write_analyzer.py](program_output_write_analyzer.md)
- [converter/services/program_paragraph_analyzer.py](program_paragraph_analyzer.md)

## Symbol contracts and control points

### `ProgramFlowAnalyzer` - L29-L129

```python
class ProgramFlowAnalyzer()
```

Generic flow analyzer for diagnostics.

### `ProgramFlowAnalyzer.__init__` - L40-L57

```python
__init__(self, mapping_rows: list[SheetMappingRow] | None=None, dclgen_columns: list[DclgenColumn] | None=None) -> None
```

Observed calls (lexical order): `CursorNameResolver`, `ProgramFlowLineCollector`, `ProgramParagraphAnalyzer`, `ProgramCursorLoopAnalyzer`, `ProgramOutputWriteAnalyzer`, `ProgramDateUsageAnalyzer`.

### `ProgramFlowAnalyzer.analyze` - L59-L91

```python
analyze(self, cobol_text: str, operations: list[IdmsOperation] | None=None) -> ProgramFlowAnalysis
```

Observed calls (lexical order): `str`, `str(cobol_text or '').strip`, `ProgramFlowAnalysis`, `self.line_collector.logical_lines_with_numbers`, `self.paragraph_analyzer.paragraph_spans`, `self.cursor_loop_analyzer.cursor_loops`, `self.output_write_analyzer.output_writes`, `self.date_usage_analyzer.date_usages`, `self._diagnostics`.

Control points:

- L64: `if not str(cobol_text or '').strip()`

### `ProgramFlowAnalyzer._diagnostics` - L93-L129

```python
_diagnostics(self, *, paragraphs: list[ParagraphSpan], cursor_loops: list[CursorLoop], output_writes: list[OutputWrite], date_usages: list[DateUsage]) -> list[str]
```

Observed calls (lexical order): `diagnostics.append`, `len`.

Control points:

- L122: `for loop in cursor_loops[:5]`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
