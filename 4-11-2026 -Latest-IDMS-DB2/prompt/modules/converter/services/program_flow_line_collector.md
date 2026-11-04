# `converter/services/program_flow_line_collector.py`

Source: [converter/services/program_flow_line_collector.py](../../../../converter/services/program_flow_line_collector.py) | 29 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `71849584ce4bb864e8e03769f4dff0eb859f4794b8db766c1281efc034dd5dc8`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from patterns.sequence_patterns import strip_sequence_numbers
```

## Local dependency notes

- [patterns/sequence_patterns.py](../../patterns/sequence_patterns.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/services/program_flow_analyzer.py](program_flow_analyzer.md)

## Symbol contracts and control points

### `ProgramFlowLineCollector` - L6-L29

```python
class ProgramFlowLineCollector()
```

Converts COBOL source text into line-numbered logical lines.

### `ProgramFlowLineCollector.logical_lines_with_numbers` - L16-L29

```python
logical_lines_with_numbers(self, cobol_text: str) -> list[tuple[int, str, str]]
```

Observed calls (lexical order): `enumerate`, `str`, `str(cobol_text or '').splitlines`, `strip_sequence_numbers`, `output.append`, `raw_line.rstrip`.

Control points:

- L22: `for (line_number, raw_line) in enumerate(str(cobol_text or '').splitlines(), start=1)`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
