# `mainframe/verification/record_write_contract.py`

Source: [mainframe/verification/record_write_contract.py](../../../../mainframe/verification/record_write_contract.py) | 116 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `20b297295906ec4d5f364cc8cf7ca5fe2366d7c0a1078e8240cd2e074f78e49e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Static fixed-record size integrity checks driven by WRITE statements.

## Module-level bindings

`_FD` (L14), `_REC` (L15), `_EXPLICIT` (L16), `_WRITE` (L17)

## Import declarations

```python
from __future__ import annotations
import re
from dataclasses import dataclass
from .cobol_storage_layout import group_byte_length
```

## Local dependency notes

- [mainframe/verification/cobol_storage_layout.py](cobol_storage_layout.md)

## Importers (6)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/verification/copybook_provenance.py](copybook_provenance.md)
- [mainframe/verification/record_population_contract.py](record_population_contract.md)
- [mainframe/zowe_semantic_release_gate.py](../zowe_semantic_release_gate.md)
- [tests/test_copybook_provenance_and_occurs.py](../../tests/test_copybook_provenance_and_occurs.md)
- [tests/test_record_write_contract.py](../../tests/test_record_write_contract.md)
- [tests/test_zowe_semantic_release_gate.py](../../tests/test_zowe_semantic_release_gate.md)

## Symbol contracts and control points

### `RecordWriteFinding` - L21-L25

```python
class RecordWriteFinding()
```

Declared class/data-model fields:

```python
level: str
record: str
buffer: str
reason: str
```

### `_code` - L28-L31

```python
_code(line: str) -> str
```

Observed calls (lexical order): `len`, `line[:6].isdigit`, `line[7:72].strip`, `line.lstrip`, `line.lstrip().startswith`, `line.strip`.

Control points:

- L29: `if len(line) >= 7 and line[:6].isdigit()`

### `_mask_quoted_literals` - L34-L53

```python
_mask_quoted_literals(text: str) -> str
```

Ignore COBOL DISPLAY/error text; only executable WRITE verbs count.

Observed calls (lexical order): `list`, `len`, `''.join`.

Control points:

- L39: `while pos < len(result)`
- L41: `if quote`
- L43: `if char == quote`
- L44: `if pos + 1 < len(result) and result[pos + 1] == quote`
- L49: `if char in ("'", '"')`

### `audit_fixed_record_writes` - L56-L116

```python
audit_fixed_record_writes(text: str) -> tuple[RecordWriteFinding, ...]
```

Observed calls (lexical order): `_code`, `text.splitlines`, `re.match`, `_FD.match`, `match.group`, `match.group(1).upper`, `_EXPLICIT.search`, `declared.group`, `int`, `_REC.match`, `first.group`, `first.group(1).upper`, `group_byte_length`, `re.search`, `_WRITE.finditer`, `_mask_quoted_literals`.
Another 4 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L63: `for code in lines`
- L64: `if re.match('^WORKING-STORAGE\\s+SECTION\\b', code, re.I)`
- L67: `if match`
- L70: `if not in_fd`
- L73: `if declared`
- L76: `if first and (not first_rec)`
- L78: `if fd in fd_record_size`
- L89: `for code in lines`
- Another 8 conditions/loops exist in this source span.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
