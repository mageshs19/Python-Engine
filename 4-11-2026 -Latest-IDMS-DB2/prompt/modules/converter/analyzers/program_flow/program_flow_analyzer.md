# `converter/analyzers/program_flow/program_flow_analyzer.py`

Source: [converter/analyzers/program_flow/program_flow_analyzer.py](../../../../../converter/analyzers/program_flow/program_flow_analyzer.py) | 105 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `d2dcb59aad9363ed4f9b63eaff9e67023ea7beaab124d974d237ea6b6e17e109`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Generic flow analyzer for diagnostics.

## Module-level bindings

`__all__` (L105)

## Import declarations

```python
from __future__ import annotations
from converter.analyzers.program_flow.flow_cursor_loop_scanner import FlowCursorLoopScanner
from converter.analyzers.program_flow.flow_date_scanner import FlowDateScanner
from converter.analyzers.program_flow.flow_diagnostics import FlowDiagnostics
from converter.analyzers.program_flow.flow_line_reader import FlowLineReader
from converter.analyzers.program_flow.flow_models import ProgramFlowAnalysis
from converter.analyzers.program_flow.flow_paragraph_scanner import FlowParagraphScanner
from converter.analyzers.program_flow.flow_write_scanner import FlowWriteScanner
from converter.domain.models import DclgenColumn, IdmsOperation, SheetMappingRow
from converter.resolvers.cursor_name_resolver import CursorNameResolver
from rules.program_flow_rules import FLOW_MESSAGES
```

## Local dependency notes

- [converter/analyzers/program_flow/flow_cursor_loop_scanner.py](flow_cursor_loop_scanner.md)
- [converter/analyzers/program_flow/flow_date_scanner.py](flow_date_scanner.md)
- [converter/analyzers/program_flow/flow_diagnostics.py](flow_diagnostics.md)
- [converter/analyzers/program_flow/flow_line_reader.py](flow_line_reader.md)
- [converter/analyzers/program_flow/flow_models.py](flow_models.md)
- [converter/analyzers/program_flow/flow_paragraph_scanner.py](flow_paragraph_scanner.md)
- [converter/analyzers/program_flow/flow_write_scanner.py](flow_write_scanner.md)
- [converter/domain/models.py](../../domain/models.md)
- [converter/resolvers/cursor_name_resolver.py](../../resolvers/cursor_name_resolver.md)
- [rules/program_flow_rules.py](../../../rules/program_flow_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/analyzers/program_flow/__init__.py](__init__.md)
- [converter/analyzers/program_flow_analyzer.py](../program_flow_analyzer.md)
- [tests/test_program_flow_table_resolution.py](../../../tests/test_program_flow_table_resolution.md)

## Symbol contracts and control points

### `ProgramFlowAnalyzer` - L43-L102

```python
class ProgramFlowAnalyzer()
```

Read-only program flow analysis.

### `ProgramFlowAnalyzer.__init__` - L46-L62

```python
__init__(self, mapping_rows: list[SheetMappingRow] | None=None, dclgen_columns: list[DclgenColumn] | None=None, table_name_resolver=None) -> None
```

Observed calls (lexical order): `FlowLineReader`, `FlowParagraphScanner`, `FlowCursorLoopScanner`, `CursorNameResolver`, `FlowWriteScanner`, `FlowDateScanner`.

### `ProgramFlowAnalyzer.analyze` - L64-L102

```python
analyze(self, cobol_text: str, operations: list[IdmsOperation] | None=None) -> ProgramFlowAnalysis
```

Observed calls (lexical order): `str`, `str(cobol_text or '').strip`, `ProgramFlowAnalysis`, `self.reader.read`, `self.paragraphs.spans`, `self.paragraphs.name_by_line`, `self.cursors.loops`, `self.writes.scan`, `self.dates.usages`, `FlowDiagnostics`, `report.counts`, `len`, `report.extend`, `report.loop_samples`, `report.drain`.

Control points:

- L69: `if not str(cobol_text or '').strip()`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
