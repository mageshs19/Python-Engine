# `tests/test_name_normalizer.py`

Source: [tests/test_name_normalizer.py](../../../tests/test_name_normalizer.py) | 21 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `b3bc8c60e0a48c590541ecd147bea61d106a7b1a99c41b96c782ab3e6b0d8d91`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [converter/services/name_normalizer.py](../converter/services/name_normalizer.md)

## Symbol contracts and control points

### `test_normalize_replaces_hyphen_with_underscore` - L4-L5

```python
test_normalize_replaces_hyphen_with_underscore()
```

Observed calls (lexical order): `NameNormalizer.normalize`.

### `test_to_cobol_replaces_underscore_with_hyphen` - L8-L9

```python
test_to_cobol_replaces_underscore_with_hyphen()
```

Observed calls (lexical order): `NameNormalizer.to_cobol`.

### `test_remove_record_suffix_removes_four_digit_suffix` - L12-L13

```python
test_remove_record_suffix_removes_four_digit_suffix()
```

Observed calls (lexical order): `NameNormalizer.remove_record_suffix`.

### `test_compact_removes_non_alphanumeric_characters` - L16-L17

```python
test_compact_removes_non_alphanumeric_characters()
```

Observed calls (lexical order): `NameNormalizer.compact`.

### `test_normalize_none_returns_empty_string` - L20-L21

```python
test_normalize_none_returns_empty_string()
```

Observed calls (lexical order): `NameNormalizer.normalize`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
