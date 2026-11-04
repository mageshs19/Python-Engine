# `review/checks/chk_07_sequence_continuity.py`

Source: [review/checks/chk_07_sequence_continuity.py](../../../../review/checks/chk_07_sequence_continuity.py) | 153 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `2f4bd88a634f07509ab811904689328c70a8f6919cf76200181370f29cde273a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-07 Sequence numbering continuity.

## Import declarations

```python
from __future__ import annotations
from collections import Counter
from review.engine.check_base import MAJOR, BOTH, Check
from review.standards import cobol_standards as std
```

## Local dependency notes

- [review/engine/check_base.py](../engine/check_base.md)
- [review/standards/__init__.py](../standards/__init__.md)
- [review/standards/cobol_standards.py](../standards/cobol_standards.md)

## Symbol contracts and control points

### `SequenceContinuityCheck` - L11-L153

```python
class SequenceContinuityCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-07'
TITLE = 'Sequence numbering continuity'
SEVERITY = MAJOR
APPLIES_TO = BOTH
ORDER = 70
```

### `SequenceContinuityCheck.relevant` - L18-L19

```python
relevant(self, ctx, view) -> bool
```

Observed calls (lexical order): `any`.

### `SequenceContinuityCheck.not_relevant_reason` - L21-L22

```python
not_relevant_reason(self) -> str
```

### `SequenceContinuityCheck.review` - L24-L80

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `view.sequence`, `record.expect_none`, `self._ascending`, `self._step`, `record.skip`, `record.expect`, `bool`, `self._unique`, `len`.

Control points:

- L50: `if not std.ENFORCE_SEQUENCE_START`

### `SequenceContinuityCheck._ascending` - L84-L99

```python
_ascending(record, num: str, description: str, values: list[int]) -> None
```

Observed calls (lexical order): `len`, `record.skip`, `zip`, `record.expect_all`, `', '.join`.

Control points:

- L85: `if len(values) < 2`

### `SequenceContinuityCheck._step` - L102-L134

```python
_step(record, num: str, label: str, values: list[int], expected: int) -> None
```

Observed calls (lexical order): `record.skip`, `len`, `zip`, `item.endswith`, `item.split`, `record.expect_all`, `', '.join`.

Control points:

- L111: `if not std.ENFORCE_SEQUENCE_STEP`
- L114: `if len(values) < 2`
- L123: `if wrong and std.ALLOW_SEQUENCE_GAPS`

### `SequenceContinuityCheck._unique` - L137-L153

```python
_unique(record, num: str, label: str, values: list[int]) -> None
```

Observed calls (lexical order): `record.skip`, `Counter`, `Counter(values).items`, `sorted`, `record.expect_all`, `len`.

Control points:

- L139: `if not values`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
