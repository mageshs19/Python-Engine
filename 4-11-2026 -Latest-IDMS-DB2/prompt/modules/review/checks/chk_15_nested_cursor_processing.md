# `review/checks/chk_15_nested_cursor_processing.py`

Source: [review/checks/chk_15_nested_cursor_processing.py](../../../../review/checks/chk_15_nested_cursor_processing.py) | 186 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `969e0f969cf93eed508ae0d76e285c63d3b9f2352fe1b26d6ef2fbc6806cf74b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-15 Nested cursor processing.

## Import declarations

```python
from __future__ import annotations
import re
from review.engine import cursors, sql_blocks as sql
from review.engine.check_base import MAJOR, BOTH, Check
from review.standards import cobol_standards as std
from review.engine import statements as stmt
```

## Local dependency notes

- [review/engine/__init__.py](../engine/__init__.md)
- [review/engine/check_base.py](../engine/check_base.md)
- [review/engine/cursors.py](../engine/cursors.md)
- [review/engine/sql_blocks.py](../engine/sql_blocks.md)
- [review/engine/statements.py](../engine/statements.md)
- [review/standards/__init__.py](../standards/__init__.md)
- [review/standards/cobol_standards.py](../standards/cobol_standards.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [tests/test_business_parity_review_rules_v128.py](../../tests/test_business_parity_review_rules_v128.md)

## Symbol contracts and control points

### `NestedCursorProcessingCheck` - L12-L186

```python
class NestedCursorProcessingCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-15'
TITLE = 'Nested cursor processing'
SEVERITY = MAJOR
APPLIES_TO = BOTH
ORDER = 150
```

### `NestedCursorProcessingCheck.relevant` - L19-L20

```python
relevant(self, ctx, view) -> bool
```

Observed calls (lexical order): `cursors.paragraph_sets`, `len`.

### `NestedCursorProcessingCheck.not_relevant_reason` - L22-L23

```python
not_relevant_reason(self) -> str
```

### `NestedCursorProcessingCheck.review` - L25-L143

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `cursors.paragraph_sets`, `self._split`, `cursors.performed_names`, `record.expect`, `bool`, `len`, `sets.items`, `sorted`, `incomplete.append`, `record.expect_all`, `record.skip`, `children.values`, `set`, `', '.join`, `group.get`, `performed.get`.
Another 7 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L44: `for (name, group) in sorted(sets.items())`
- L45: `for operation in std.CURSOR_OPERATIONS`
- L46: `if operation not in group`
- L54: `if not children`
- L82: `for (name, group) in sorted(sets.items())`
- L84: `if open_para is None`
- L87: `if count > 1`
- L94: `if not std.ENFORCE_CHILD_FETCH_EARLY_STOP`
- Another 5 conditions/loops exist in this source span.

### `NestedCursorProcessingCheck._source_requires_business_early_stop` - L148-L168

```python
_source_requires_business_early_stop(ctx) -> bool
```

Return True only for source traversal with a compound stop rule.

Observed calls (lexical order): `getattr`, `str`, `str(getattr(ctx, 'source_cobol', '') or '').upper`, `source.strip`, `' '.join`, `line.strip`, `source.splitlines`, `re.finditer`, `match.group`, `re.search`.

Control points:

- L157: `if not source.strip()`
- L160: `for match in re.finditer('\\bPERFORM(?:\\s+[A-Z0-9-]+)?\\s+UNTIL\\s+(.+?)(?:\\.|\\bEND-PERFORM\\b)', logical, re.IGNORECASE)`
- L166: `if re.search('\\b(?:OR|AND)\\b', condition, re.IGNORECASE)`

### `NestedCursorProcessingCheck._split` - L171-L186

```python
_split(sets)
```

Observed calls (lexical order): `sets.items`, `sorted`, `pair[1].get`.

Control points:

- L181: `if ordered`
- L184: `for (name, group) in ordered[1:]`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
