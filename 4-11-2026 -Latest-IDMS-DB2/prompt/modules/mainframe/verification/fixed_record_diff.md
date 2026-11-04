# `mainframe/verification/fixed_record_diff.py`

Source: [mainframe/verification/fixed_record_diff.py](../../../../mainframe/verification/fixed_record_diff.py) | 104 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `7fcaa5f24fd35d19eac7eb0052fcac04616f587ffc5b35c30554997e01bd4d74`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Byte-exact, order-sensitive verification of fixed-length batch output files.

## Import declarations

```python
from __future__ import annotations
import argparse
import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [tests/test_fixed_record_diff.py](../../tests/test_fixed_record_diff.md)

## Symbol contracts and control points

### `FileEvidence` - L17-L22

```python
class FileEvidence()
```

Declared class/data-model fields:

```python
path: str
bytes: int
records: int | None
sha256: str
aligned: bool
```

### `Comparison` - L26-L33

```python
class Comparison()
```

Declared class/data-model fields:

```python
passed: bool
record_size: int
manual: FileEvidence
generated: FileEvidence
first_mismatched_record: int | None
first_mismatched_byte: int | None
reason: str
```

### `_evidence` - L36-L44

```python
_evidence(path: Path, record_size: int, chunk_bytes: int=1024 * 1024) -> FileEvidence
```

Observed calls (lexical order): `hashlib.sha256`, `path.open`, `stream.read`, `digest.update`, `len`, `FileEvidence`, `digest.hexdigest`, `str`.

Control points:

- L40: `while (data := stream.read(chunk_bytes))`

### `compare` - L47-L80

```python
compare(manual: str | Path, generated: str | Path, record_size: int) -> Comparison
```

Compare records exactly, including padding and original file order.

Observed calls (lexical order): `isinstance`, `ValueError`, `Path`, `g.resolve`, `m.resolve`, `_evidence`, `Comparison`, `g.open`, `m.open`, `gs.read`, `ms.read`, `len`, `enumerate`, `next`, `zip`.

Control points:

- L54: `if not isinstance(record_size, int) or isinstance(record_size, bool) or record_size <= 0`
- L57: `if m.resolve() == g.resolve()`
- L60: `if not me.aligned or not ge.aligned`
- L63: `if me.bytes == ge.bytes and me.sha256 == ge.sha256`
- L67: `while True`
- L69: `if not left and (not right)`
- L72: `if left != right`
- L73: `if len(left) != len(right)`

Explicit raises: `ValueError('record_size must be a positive integer')`; `ValueError('manual and generated files must be different physical paths')`.

### `main` - L83-L100

```python
main(argv: list[str] | None=None) -> int
```

Observed calls (lexical order): `argparse.ArgumentParser`, `parser.add_argument`, `parser.parse_args`, `compare`, `parser.exit`, `asdict`, `json.dumps`, `args.report.parent.mkdir`, `args.report.write_text`, `print`.

Control points:

- L96: `if args.report`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
