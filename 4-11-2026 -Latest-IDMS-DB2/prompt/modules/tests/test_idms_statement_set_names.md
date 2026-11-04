# `tests/test_idms_statement_set_names.py`

Source: [tests/test_idms_statement_set_names.py](../../../tests/test_idms_statement_set_names.py) | 65 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `8854822919a1d49391f3b505f710307cef782e1fb147da5599329b993abcf952`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> IDMS name rendering in generated *DB2: comments.

## Symbol contracts and control points

### `test_set_name_keeps_idms_spelling_in_the_comment` - L17-L21

```python
test_set_name_keeps_idms_spelling_in_the_comment(transform_line)
```

Observed calls (lexical order): `transform_line`.

### `test_record_name_keeps_cobol_spelling_in_the_comment` - L24-L28

```python
test_record_name_keeps_cobol_spelling_in_the_comment(transform_line)
```

Observed calls (lexical order): `transform_line`.

### `test_obtain_next_keeps_idms_spelling` - L31-L34

```python
test_obtain_next_keeps_idms_spelling(transform_line)
```

Observed calls (lexical order): `transform_line`.

### `test_opened_set_is_still_the_normalized_key` - L37-L40

```python
test_opened_set_is_still_the_normalized_key(transform_line)
```

Observed calls (lexical order): `transform_line`.

### `test_unmapped_record_never_emits_an_empty_cursor_perform` - L43-L48

```python
test_unmapped_record_never_emits_an_empty_cursor_perform(transform_line)
```

Observed calls (lexical order): `transform_line`.

### `test_find_first_without_a_record_is_kept_and_commented` - L51-L55

```python
test_find_first_without_a_record_is_kept_and_commented(transform_line)
```

Observed calls (lexical order): `transform_line`.

### `test_obtain_outside_procedure_division_is_only_commented` - L58-L65

```python
test_obtain_outside_procedure_division_is_only_commented(transform_line)
```

Observed calls (lexical order): `transform_line`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
