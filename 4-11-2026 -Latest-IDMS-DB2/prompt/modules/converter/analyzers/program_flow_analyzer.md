# `converter/analyzers/program_flow_analyzer.py`

Source: [converter/analyzers/program_flow_analyzer.py](../../../../converter/analyzers/program_flow_analyzer.py) | 57 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `a6c42b6a07708e40354de86b816c1d5347d7d61cee115069cfe8ec4d4046af4a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Backward-compatible import point.

## Module-level bindings

`__all__` (L49)

## Import declarations

```python
from __future__ import annotations
from converter.analyzers.program_flow.flow_models import CursorLoop, DateUsage, LogicalLine, OutputWrite, ParagraphSpan, ProgramFlowAnalysis
from converter.analyzers.program_flow.program_flow_analyzer import ProgramFlowAnalyzer
```

## Local dependency notes

- [converter/analyzers/program_flow/flow_models.py](program_flow/flow_models.md)
- [converter/analyzers/program_flow/program_flow_analyzer.py](program_flow/program_flow_analyzer.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_pipeline.py](../pipeline/conversion/conversion_pipeline.md)

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
