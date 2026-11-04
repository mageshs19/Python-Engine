# `runners/audit_business_operation_parity.py`

Source: [runners/audit_business_operation_parity.py](../../../runners/audit_business_operation_parity.py) | 82 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `7e39b4c592dc1f33b5e800aae9d4ba104221ac33e21643992e0e063c89b52c47`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Audit source IDMS DML family coverage in converted DB2 COBOL candidates.

## Module-level bindings

`DEFAULT_ROOT` (L9), `DEFAULT_PAIRS` (L10)

## Import declarations

```python
from __future__ import annotations
import argparse
from pathlib import Path
from converter.analyzers.program_flow.business_operation_parity_audit import BusinessOperationParityAuditor
```

## Local dependency notes

- [converter/analyzers/program_flow/business_operation_parity_audit.py](../converter/analyzers/program_flow/business_operation_parity_audit.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [tests/test_audit_business_operation_parity_runner.py](../tests/test_audit_business_operation_parity_runner.md)

## Symbol contracts and control points

### `latest_candidate` - L20-L23

```python
latest_candidate(output_dir: Path, target_prefix: str) -> Path | None
```

Return newest generated output regardless of timestamp/stable filename style.

Observed calls (lexical order): `output_dir.glob`, `path.is_file`, `max`, `path.stat`.

### `main` - L26-L78

```python
main() -> int
```

Observed calls (lexical order): `argparse.ArgumentParser`, `parser.add_argument`, `parser.parse_args`, `(args.workspace / 'Mapping Sheet').glob`, `sorted`, `len`, `parser.error`, `mapping_csv.is_file`, `BusinessOperationParityAuditor`, `bool`, `isinstance`, `latest_candidate`, `print`, `source_path.is_file`, `target_path.is_file`, `auditor.audit`.
Another 1 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L35: `if args.mapping`
- L37: `if len(mapping_files) == 1`
- L41: `if not mapping_csv.is_file()`
- L47: `if bool(args.source) != bool(args.output)`
- L50: `for (source_name, target_prefix) in pairs`
- L52: `if args.source and args.output`
- L58: `if target_path is None`
- L62: `if not source_path.is_file() or not target_path.is_file()`
- Another 2 conditions/loops exist in this source span.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
