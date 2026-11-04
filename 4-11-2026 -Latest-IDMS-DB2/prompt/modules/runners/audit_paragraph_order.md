# `runners/audit_paragraph_order.py`

Source: [runners/audit_paragraph_order.py](../../../runners/audit_paragraph_order.py) | 44 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `e4af14e1907b6bdc5115efa221cacecb8fcda810529a07f718252e8d4c76b32f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Compare original IDMS and converted DB2 COBOL paragraph source order.

## Import declarations

```python
from __future__ import annotations
import argparse
from pathlib import Path
from converter.analyzers.program_flow.paragraph_order_audit import ParagraphOrderAuditor
```

## Local dependency notes

- [converter/analyzers/program_flow/paragraph_order_audit.py](../converter/analyzers/program_flow/paragraph_order_audit.md)

## Symbol contracts and control points

### `main` - L10-L40

```python
main() -> int
```

Observed calls (lexical order): `argparse.ArgumentParser`, `parser.add_argument`, `parser.parse_args`, `ParagraphOrderAuditor`, `print`, `item.split`, `Path`, `converted.is_file`, `original.is_file`, `auditor.audit`, `len`.

Control points:

- L19: `for item in args.pair`
- L20: `if '=' not in item`
- L26: `if not original.is_file() or not converted.is_file()`
- L37: `for diagnostic in result.diagnostics`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
