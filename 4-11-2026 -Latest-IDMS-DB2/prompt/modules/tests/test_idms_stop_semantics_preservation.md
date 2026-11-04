# `tests/test_idms_stop_semantics_preservation.py`

Source: [tests/test_idms_stop_semantics_preservation.py](../../../tests/test_idms_stop_semantics_preservation.py) | 33 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `321bccdf3fadda05283094c8abcfe82e3b3c2131eee3dcd42c9341a1bd1d6e60`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> IDMS-STOP may carry program-specific rollback and abend semantics.

## Import declarations

```python
from patterns.cobol_transformer_patterns import IDMS_ABORT_PARAGRAPH_PATTERN
```

## Local dependency notes

- [patterns/cobol_transformer_patterns.py](../patterns/cobol_transformer_patterns.md)

## Symbol contracts and control points

### `test_idms_stop_paragraph_is_not_treated_as_orphan_idms_abort` - L6-L8

```python
test_idms_stop_paragraph_is_not_treated_as_orphan_idms_abort()
```

Observed calls (lexical order): `IDMS_ABORT_PARAGRAPH_PATTERN.match`.

### `test_perform_idms_stop_is_retained_instead_of_silently_removed` - L11-L20

```python
test_perform_idms_stop_is_retained_instead_of_silently_removed(transformer_context)
```

Observed calls (lexical order): `transformer.transform_line`, `'\n'.join`, `'\n'.join(lines).upper`.

### `test_rollback_is_emitted_as_db2_sql` - L23-L33

```python
test_rollback_is_emitted_as_db2_sql(transformer_context)
```

Observed calls (lexical order): `transformer.transform_line`, `'\n'.join`, `'\n'.join(lines).upper`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
