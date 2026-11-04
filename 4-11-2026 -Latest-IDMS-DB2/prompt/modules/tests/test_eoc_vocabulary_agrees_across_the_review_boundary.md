# `tests/test_eoc_vocabulary_agrees_across_the_review_boundary.py`

Source: [tests/test_eoc_vocabulary_agrees_across_the_review_boundary.py](../../../tests/test_eoc_vocabulary_agrees_across_the_review_boundary.py) | 42 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `fec5546fa77d636a9a4bc9d8b4f0bdfe96482fe88ee76c672ac53ec0d1a3452e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> The converter and the reviewer must know the same EOC vocabulary.

## Import declarations

```python
from __future__ import annotations
from review.standards import cobol_standards as std
from rules.cursor_eoc_rules import LEGACY_EOC_CONDITIONS
import inspect
```

## Local dependency notes

- [review/standards/__init__.py](../review/standards/__init__.md)
- [review/standards/cobol_standards.py](../review/standards/cobol_standards.md)
- [rules/cursor_eoc_rules.py](../rules/cursor_eoc_rules.md)

## Symbol contracts and control points

### `test_every_converter_condition_has_a_reviewer_statement` - L24-L33

```python
test_every_converter_condition_has_a_reviewer_statement() -> None
```

Observed calls (lexical order): `', '.join`.

### `test_review_does_not_import_the_converter` - L36-L42

```python
test_review_does_not_import_the_converter() -> None
```

The one-way boundary, asserted rather than trusted.

Observed calls (lexical order): `inspect.getsource`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
