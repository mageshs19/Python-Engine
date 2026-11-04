# `converter/analyzers/program_flow/__init__.py`

Source: [converter/analyzers/program_flow/__init__.py](../../../../../converter/analyzers/program_flow/__init__.py) | 97 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `0d880e475d9e18687d3c3b098caa21a14e1b37b8c934888373deb89265f26c6a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Program flow analysis package.

## Module-level bindings

`__all__` (L80)

## Import declarations

```python
from __future__ import annotations
from converter.analyzers.program_flow.flow_models import CursorLoop, DateUsage, LogicalLine, OutputWrite, ParagraphSpan, ProgramFlowAnalysis
from converter.analyzers.program_flow.flow_line_reader import FlowLineReader
from converter.analyzers.program_flow.flow_paragraph_scanner import FlowParagraphScanner
from converter.analyzers.program_flow.flow_cursor_loop_scanner import FlowCursorLoopScanner
from converter.analyzers.program_flow.flow_write_scanner import FlowWriteScanner
from converter.analyzers.program_flow.flow_date_scanner import FlowDateScanner
from converter.analyzers.program_flow.flow_diagnostics import FlowDiagnostics
from converter.analyzers.program_flow.program_flow_analyzer import ProgramFlowAnalyzer
```

## Local dependency notes

- [converter/analyzers/program_flow/flow_cursor_loop_scanner.py](flow_cursor_loop_scanner.md)
- [converter/analyzers/program_flow/flow_date_scanner.py](flow_date_scanner.md)
- [converter/analyzers/program_flow/flow_diagnostics.py](flow_diagnostics.md)
- [converter/analyzers/program_flow/flow_line_reader.py](flow_line_reader.md)
- [converter/analyzers/program_flow/flow_models.py](flow_models.md)
- [converter/analyzers/program_flow/flow_paragraph_scanner.py](flow_paragraph_scanner.md)
- [converter/analyzers/program_flow/flow_write_scanner.py](flow_write_scanner.md)
- [converter/analyzers/program_flow/program_flow_analyzer.py](program_flow_analyzer.md)

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
