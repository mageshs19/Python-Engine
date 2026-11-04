# `runners/audit_procedure_flow.py`

Source: [runners/audit_procedure_flow.py](../../../runners/audit_procedure_flow.py) | 36 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `d8a7113ce60c1abfecaff6131a609c685daa00e8a203ebac7e634360e3921fc9`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Print a generic PROCEDURE DIVISION control-flow audit for COBOL files.

## Import declarations

```python
from __future__ import annotations
import argparse
from pathlib import Path
from converter.analyzers.program_flow.procedure_control_flow_graph import ProcedureControlFlowGraphBuilder
```

## Local dependency notes

- [converter/analyzers/program_flow/procedure_control_flow_graph.py](../converter/analyzers/program_flow/procedure_control_flow_graph.md)

## Symbol contracts and control points

### `main` - L12-L32

```python
main() -> int
```

Observed calls (lexical order): `argparse.ArgumentParser`, `parser.add_argument`, `parser.parse_args`, `ProcedureControlFlowGraphBuilder`, `Path`, `path.is_file`, `print`, `builder.build`, `sum`, `len`, `bool`.

Control points:

- L18: `for raw in args.paths`
- L20: `if not path.is_file()`
- L29: `for diagnostic in graph.diagnostics`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
