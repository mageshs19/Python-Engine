# `tests/test_name_derivation.py`

Source: [tests/test_name_derivation.py](../../../tests/test_name_derivation.py) | 37 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `8f9730ec0018d7f092aa338980f8c5a7e707ca38c10ab7df0a805e873907d9d6`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.services.name_derivation_resolver import NameDerivationResolver
```

## Local dependency notes

- [converter/services/name_derivation_resolver.py](../converter/services/name_derivation_resolver.md)

## Symbol contracts and control points

### `_r` - L6-L7

```python
_r()
```

Observed calls (lexical order): `NameDerivationResolver`.

### `test_program_id_with_site_char` - L10-L12

```python
test_program_id_with_site_char()
```

Observed calls (lexical order): `_r`, `_r().derive`.

### `test_record_name_without_site_char` - L15-L17

```python
test_record_name_without_site_char()
```

Observed calls (lexical order): `_r`, `_r().derive`.

### `test_generic_vm_bd_name` - L20-L21

```python
test_generic_vm_bd_name()
```

Observed calls (lexical order): `_r`, `_r().derive`.

### `test_non_matching_name_unchanged` - L24-L25

```python
test_non_matching_name_unchanged()
```

Observed calls (lexical order): `_r`, `_r().derive`.

### `test_empty_and_none_safe` - L28-L30

```python
test_empty_and_none_safe()
```

Observed calls (lexical order): `_r`, `_r().derive`.

### `test_is_derivable_flags` - L33-L37

```python
test_is_derivable_flags()
```

Observed calls (lexical order): `_r`, `r.is_derivable`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
