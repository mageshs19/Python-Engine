# `tests/test_retrieval_commit_continue_guard.py`

Source: [tests/test_retrieval_commit_continue_guard.py](../../../tests/test_retrieval_commit_continue_guard.py) | 215 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `537a3ec2d14e1a7a884bbc6cef5c4f0b083bc25243a03738e69bbaf9e83564ca`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> The COMMIT removal must never empty a paragraph.

## Module-level bindings

`LEFT_WIDTH` (L27), `BODY_WIDTH` (L28), `RIGHT_WIDTH` (L29), `LINE_WIDTH` (L30)

## Import declarations

```python
from __future__ import annotations
from converter.composers.retrieval_commit_cleanup_composer import RetrievalCommitCleanupComposer
```

## Local dependency notes

- [converter/composers/retrieval_commit_cleanup_composer.py](../converter/composers/retrieval_commit_cleanup_composer.md)

## Symbol contracts and control points

### `_fixed` - L33-L39

```python
_fixed(seq: str, body: str, indicator: str=' ') -> str
```

One 80-column fixed-format record.

Observed calls (lexical order): `str`, `str(seq).zfill`, `f'{left}00'[:RIGHT_WIDTH].ljust`, `body[:BODY_WIDTH].ljust`, `len`.

### `_paragraph` - L42-L43

```python
_paragraph(seq: str, name: str) -> str
```

Observed calls (lexical order): `_fixed`.

### `_statement` - L46-L47

```python
_statement(seq: str, body: str) -> str
```

Observed calls (lexical order): `_fixed`.

### `_comment` - L50-L51

```python
_comment(seq: str, body: str) -> str
```

Observed calls (lexical order): `_fixed`.

### `_commit_block` - L54-L60

```python
_commit_block(start: int) -> list[str]
```

Observed calls (lexical order): `_statement`.

### `_compose` - L63-L65

```python
_compose(lines: list[str]) -> tuple[str, list[str]]
```

Observed calls (lexical order): `RetrievalCommitCleanupComposer`, `'\n'.join`, `composer.compose`.

### `test_continue_is_added_when_the_paragraph_is_emptied` - L71-L81

```python
test_continue_is_added_when_the_paragraph_is_emptied()
```

Observed calls (lexical order): `_compose`, `_paragraph`, `_commit_block`, `any`.

### `test_a_following_comment_does_not_rescue_the_paragraph` - L84-L95

```python
test_a_following_comment_does_not_rescue_the_paragraph()
```

A comment is not executable.

Observed calls (lexical order): `_compose`, `_paragraph`, `_commit_block`, `_comment`.

### `test_end_of_program_after_the_removal_adds_continue` - L98-L106

```python
test_end_of_program_after_the_removal_adds_continue()
```

Observed calls (lexical order): `_compose`, `_paragraph`, `_commit_block`.

### `test_a_following_section_header_is_a_boundary` - L109-L118

```python
test_a_following_section_header_is_a_boundary()
```

Observed calls (lexical order): `_compose`, `_paragraph`, `_commit_block`, `_fixed`.

### `test_continue_is_not_added_when_a_statement_follows` - L124-L134

```python
test_continue_is_not_added_when_a_statement_follows()
```

Observed calls (lexical order): `_compose`, `_paragraph`, `_commit_block`, `_statement`, `any`.

### `test_exit_does_not_count_as_a_paragraph_boundary` - L137-L147

```python
test_exit_does_not_count_as_a_paragraph_boundary()
```

EXIT. belongs to the paragraph, so the paragraph is NOT empty.

Observed calls (lexical order): `_compose`, `_paragraph`, `_commit_block`, `_statement`.

### `test_goback_does_not_count_as_a_paragraph_boundary` - L150-L159

```python
test_goback_does_not_count_as_a_paragraph_boundary()
```

Observed calls (lexical order): `_compose`, `_paragraph`, `_commit_block`, `_statement`.

### `test_the_generated_pair_keeps_the_sequence_area` - L165-L183

```python
test_the_generated_pair_keeps_the_sequence_area()
```

Observed calls (lexical order): `_compose`, `_paragraph`, `_commit_block`, `result.split`, `line[:LEFT_WIDTH].isdigit`, `len`.

Control points:

- L181: `for line in generated`

### `test_continue_lands_in_area_b` - L186-L198

```python
test_continue_lands_in_area_b()
```

CONTINUE. must start at column 12, not Area A.

Observed calls (lexical order): `_compose`, `_paragraph`, `_commit_block`, `next`, `result.split`, `line.index`.

### `test_an_update_program_is_untouched` - L201-L211

```python
test_an_update_program_is_untouched()
```

Observed calls (lexical order): `'\n'.join`, `_paragraph`, `_commit_block`, `RetrievalCommitCleanupComposer`, `composer.compose`, `any`.

### `test_empty_text_is_safe` - L214-L215

```python
test_empty_text_is_safe()
```

Observed calls (lexical order): `RetrievalCommitCleanupComposer`, `RetrievalCommitCleanupComposer().compose`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
