# `converter/services/program_date_usage_analyzer.py`

Source: [converter/services/program_date_usage_analyzer.py](../../../../converter/services/program_date_usage_analyzer.py) | 34 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `43603c2572d14f23b6c5c04c4bc7b92aa4c9a25b57e0c1da4e3fdf5eab3f47e8`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.services.program_flow_models import DateUsage
from rules.program_flow_rules import DATE_TOKENS
```

## Local dependency notes

- [converter/services/program_flow_models.py](program_flow_models.md)
- [rules/program_flow_rules.py](../../rules/program_flow_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/services/program_flow_analyzer.py](program_flow_analyzer.md)

## Symbol contracts and control points

### `ProgramDateUsageAnalyzer` - L7-L34

```python
class ProgramDateUsageAnalyzer()
```

Detects basic date/time/timestamp usage hints for diagnostics.

### `ProgramDateUsageAnalyzer.date_usages` - L14-L34

```python
date_usages(self, logical_lines: list[tuple[int, str, str]]) -> list[DateUsage]
```

Observed calls (lexical order): `logical.upper`, `any`, `output.append`, `DateUsage`.

Control points:

- L20: `for (line_number, logical, raw_line) in logical_lines`
- L23: `if not any((token in upper for token in DATE_TOKENS))`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
