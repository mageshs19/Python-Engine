# `tests/test_program_kind_classification.py`

Source: [tests/test_program_kind_classification.py](../../../tests/test_program_kind_classification.py) | 46 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `29c439769d760814b117b15f7b020785e7d6b59646ab0a234899f365c7b6a5d0`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Program kind must be readable from FIXED-FORMAT source.

## Import declarations

```python
from __future__ import annotations
from patterns.idms_patterns import IDMS_WRITE_VERB_PATTERN
```

## Local dependency notes

- [patterns/idms_patterns.py](../patterns/idms_patterns.md)

## Symbol contracts and control points

### `_fixed` - L15-L16

```python
_fixed(seq: str, body: str) -> str
```

Observed calls (lexical order): `body[:65].ljust`.

### `test_a_sequenced_store_line_is_recognised` - L19-L20

```python
test_a_sequenced_store_line_is_recognised()
```

Observed calls (lexical order): `IDMS_WRITE_VERB_PATTERN.search`, `_fixed`.

### `test_a_sequenced_modify_line_is_recognised` - L23-L24

```python
test_a_sequenced_modify_line_is_recognised()
```

Observed calls (lexical order): `IDMS_WRITE_VERB_PATTERN.search`, `_fixed`.

### `test_a_sequenced_erase_line_is_recognised` - L27-L28

```python
test_a_sequenced_erase_line_is_recognised()
```

Observed calls (lexical order): `IDMS_WRITE_VERB_PATTERN.search`, `_fixed`.

### `test_a_retrieval_program_is_not_matched` - L31-L39

```python
test_a_retrieval_program_is_not_matched()
```

Observed calls (lexical order): `'\n'.join`, `_fixed`, `IDMS_WRITE_VERB_PATTERN.search`.

### `test_the_word_must_be_a_verb_not_a_substring` - L42-L46

```python
test_the_word_must_be_a_verb_not_a_substring()
```

RESTORE-COUNT must not classify a program as UPDATE.

Observed calls (lexical order): `IDMS_WRITE_VERB_PATTERN.search`, `_fixed`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
