# `tests/spec_builder/test_select_augmentation.py`

Source: [tests/spec_builder/test_select_augmentation.py](../../../../tests/spec_builder/test_select_augmentation.py) | 54 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `589ec2fe7bf4ed19bcc8f9f300c772908dc551b9955cc24be0fd650967b0ac61`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Tests for cross-spec SELECT-column augmentation.

## Import declarations

```python
from __future__ import annotations
```

## Symbol contracts and control points

### `test_child_order_by_key_is_added_to_select` - L6-L21

```python
test_child_order_by_key_is_added_to_select(augmenter)
```

Observed calls (lexical order): `augmenter.augment`.

### `test_order_by_key_is_not_added_twice` - L24-L39

```python
test_order_by_key_is_not_added_twice(augmenter)
```

Observed calls (lexical order): `augmenter.augment`, `spec['select_columns'].count`.

### `test_host_variables_are_resynchronised_after_augmentation` - L42-L54

```python
test_host_variables_are_resynchronised_after_augmentation(augmenter)
```

Observed calls (lexical order): `augmenter.augment`, `len`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
