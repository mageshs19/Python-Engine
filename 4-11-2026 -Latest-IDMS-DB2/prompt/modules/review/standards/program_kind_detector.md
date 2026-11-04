# `review/standards/program_kind_detector.py`

Source: [review/standards/program_kind_detector.py](../../../../review/standards/program_kind_detector.py) | 152 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `dcdd0862da1144eac3c45a63eb2c174dfa8bdd76fec6e3e18a251a625c23e2df`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Source-based program-kind detection for the review step.

## Module-level bindings

`_UPDATE_IDMS_PATTERNS` (L74), `_RETRIEVAL_IDMS_PATTERNS` (L75), `_EXEC_SQL_WINDOW` (L86), `_NOT_NAME_BEFORE` (L92), `_NOT_NAME_AFTER` (L93), `_DB2_OBJECT` (L99), `_EXEC_SQL_WRITE_PATTERN` (L101), `_EXEC_SQL_READ_PATTERN` (L113), `__all__` (L152)

## Import declarations

```python
from __future__ import annotations
import re
from review.engine.context import KIND_RETRIEVAL, KIND_UNKNOWN, KIND_UPDATE
from review.standards.cobol_standards import CURSOR_DECLARE_VERB, RETRIEVAL_SQL_VERBS, WRITE_SQL_VERBS
from patterns.idms_patterns import ERASE_PATTERN, FIND_CURRENT_PATTERN, FIND_FIRST_PATTERN, MODIFY_PATTERN, OBTAIN_CALC_PATTERN, OBTAIN_CALC_REVERSED_PATTERN, OBTAIN_FIRST_NEXT_PATTERN, STORE_PATTERN, USAGE_MODE_PATTERN
```

## Local dependency notes

- [patterns/idms_patterns.py](../../patterns/idms_patterns.md)
- [review/engine/context.py](../engine/context.md)
- [review/standards/cobol_standards.py](cobol_standards.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [review/runner/review_file.py](../runner/review_file.md)
- [tests/test_program_kind_detector.py](../../tests/test_program_kind_detector.md)

## Symbol contracts and control points

### `_has_update_evidence` - L122-L125

```python
_has_update_evidence(text: str) -> bool
```

Observed calls (lexical order): `_EXEC_SQL_WRITE_PATTERN.search`, `any`, `pattern.search`.

Control points:

- L123: `if _EXEC_SQL_WRITE_PATTERN.search(text)`

### `_has_retrieval_evidence` - L128-L131

```python
_has_retrieval_evidence(text: str) -> bool
```

Observed calls (lexical order): `_EXEC_SQL_READ_PATTERN.search`, `any`, `pattern.search`.

Control points:

- L129: `if _EXEC_SQL_READ_PATTERN.search(text)`

### `detect_program_kind` - L134-L149

```python
detect_program_kind(converted_cobol: str, source_cobol: str='') -> str
```

Return KIND_UPDATE, KIND_RETRIEVAL or KIND_UNKNOWN from program text.

Observed calls (lexical order): `str`, `USAGE_MODE_PATTERN.search`, `explicit.group`, `explicit.group(1).upper`, `_has_update_evidence`, `_has_retrieval_evidence`.

Control points:

- L139: `if explicit`
- L145: `if _has_update_evidence(text)`
- L147: `if _has_retrieval_evidence(text)`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
