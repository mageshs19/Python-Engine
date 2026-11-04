# `tests/spec_builder/test_parent_classifier.py`

Source: [tests/spec_builder/test_parent_classifier.py](../../../../tests/spec_builder/test_parent_classifier.py) | 18 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `2bbc86dbbe572f80084b82f40787cb93c1174a93c35743accfcaeea20d29cf6d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.generators.db2_infrastructure.spec_builder.spec_parent_classifier import SpecParentClassifier
```

## Local dependency notes

- [converter/generators/db2_infrastructure/spec_builder/spec_parent_classifier.py](../../converter/generators/db2_infrastructure/spec_builder/spec_parent_classifier.md)

## Symbol contracts and control points

### `test_cursor_without_where_is_parent_even_at_910` - L6-L9

```python
test_cursor_without_where_is_parent_even_at_910()
```

Observed calls (lexical order): `SpecParentClassifier`, `classifier.is_parent`.

### `test_cursor_with_where_is_child_even_at_710` - L12-L18

```python
test_cursor_with_where_is_child_even_at_710()
```

Observed calls (lexical order): `SpecParentClassifier`, `classifier.is_parent`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
