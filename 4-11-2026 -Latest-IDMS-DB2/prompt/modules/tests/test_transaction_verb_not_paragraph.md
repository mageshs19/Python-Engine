# `tests/test_transaction_verb_not_paragraph.py`

Source: [tests/test_transaction_verb_not_paragraph.py](../../../tests/test_transaction_verb_not_paragraph.py) | 23 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `630652d80bbbb0e0ed632dbd9a3309876e26034602715782693d5803c536c4d2`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.composers.procedure_indent.indent_models import LineClassifier
from rules.procedure_indent_rules import NON_PARAGRAPH_SINGLE_WORDS
```

## Local dependency notes

- [converter/composers/procedure_indent/indent_models.py](../converter/composers/procedure_indent/indent_models.md)
- [rules/procedure_indent_rules.py](../rules/procedure_indent_rules.md)

## Symbol contracts and control points

### `test_rollback_and_commit_are_exempt_single_words` - L9-L11

```python
test_rollback_and_commit_are_exempt_single_words() -> None
```

### `test_rollback_is_not_area_a_header` - L14-L15

```python
test_rollback_is_not_area_a_header() -> None
```

Observed calls (lexical order): `LineClassifier.is_area_a_header`.

### `test_commit_is_not_area_a_header` - L18-L19

```python
test_commit_is_not_area_a_header() -> None
```

Observed calls (lexical order): `LineClassifier.is_area_a_header`.

### `test_real_paragraph_still_reads_as_header` - L22-L23

```python
test_real_paragraph_still_reads_as_header() -> None
```

Observed calls (lexical order): `LineClassifier.is_area_a_header`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
