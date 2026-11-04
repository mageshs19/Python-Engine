# `tests/test_program_kind_detector.py`

Source: [tests/test_program_kind_detector.py](../../../tests/test_program_kind_detector.py) | 123 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `e37e5c25a72b74a2f10bb0a1139f3d10fe26e480fb7f27684fc8dbf311b6bfe6`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Regression tests for source-based program-kind detection.

## Import declarations

```python
from __future__ import annotations
from review.engine.context import KIND_RETRIEVAL, KIND_UNKNOWN, KIND_UPDATE
from review.standards.program_kind_detector import detect_program_kind
```

## Local dependency notes

- [review/engine/context.py](../review/engine/context.md)
- [review/standards/program_kind_detector.py](../review/standards/program_kind_detector.md)

## Symbol contracts and control points

### `test_idms_write_verb_in_kept_comment_means_update` - L19-L21

```python
test_idms_write_verb_in_kept_comment_means_update() -> None
```

Observed calls (lexical order): `detect_program_kind`.

### `test_idms_modify_verb_means_update` - L24-L26

```python
test_idms_modify_verb_means_update() -> None
```

Observed calls (lexical order): `detect_program_kind`.

### `test_exec_sql_insert_means_update` - L29-L31

```python
test_exec_sql_insert_means_update() -> None
```

Observed calls (lexical order): `detect_program_kind`.

### `test_cursor_declare_means_retrieval` - L34-L36

```python
test_cursor_declare_means_retrieval() -> None
```

Observed calls (lexical order): `detect_program_kind`.

### `test_idms_obtain_means_retrieval` - L39-L41

```python
test_idms_obtain_means_retrieval() -> None
```

Observed calls (lexical order): `detect_program_kind`.

### `test_write_intent_wins_over_a_read` - L44-L49

```python
test_write_intent_wins_over_a_read() -> None
```

Observed calls (lexical order): `detect_program_kind`.

### `test_store_paragraph_name_is_not_a_write` - L52-L55

```python
test_store_paragraph_name_is_not_a_write() -> None
```

Observed calls (lexical order): `detect_program_kind`.

### `test_display_literal_update_is_not_a_write` - L58-L60

```python
test_display_literal_update_is_not_a_write() -> None
```

Observed calls (lexical order): `detect_program_kind`.

### `test_explicit_usage_mode_in_source_wins` - L63-L66

```python
test_explicit_usage_mode_in_source_wins() -> None
```

Observed calls (lexical order): `detect_program_kind`.

### `test_no_evidence_is_unknown` - L69-L70

```python
test_no_evidence_is_unknown() -> None
```

Observed calls (lexical order): `detect_program_kind`.

### `test_audit_host_variable_is_not_a_write` - L72-L81

```python
test_audit_host_variable_is_not_a_write() -> None
```

TS-UPDATE-479BFAR must not make a retrieval cursor look like a write.

Observed calls (lexical order): `detect_program_kind`.

### `test_real_sql_update_is_still_a_write` - L84-L91

```python
test_real_sql_update_is_still_a_write() -> None
```

Observed calls (lexical order): `detect_program_kind`.

### `test_audit_host_variable_is_not_a_write` - L94-L103

```python
test_audit_host_variable_is_not_a_write() -> None
```

TS-UPDATE-479BFAR must not make a retrieval cursor look like a write.

Observed calls (lexical order): `detect_program_kind`.

### `test_real_sql_update_is_still_a_write` - L106-L113

```python
test_real_sql_update_is_still_a_write() -> None
```

Observed calls (lexical order): `detect_program_kind`.

### `test_real_sql_insert_into_is_still_a_write` - L116-L123

```python
test_real_sql_insert_into_is_still_a_write() -> None
```

Observed calls (lexical order): `detect_program_kind`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
