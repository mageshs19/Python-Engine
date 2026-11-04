# `tests/update_business_sql/test_structural_update_detection.py`

Source: [tests/update_business_sql/test_structural_update_detection.py](../../../../tests/update_business_sql/test_structural_update_detection.py) | 93 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `2682109936b111836fd3fad011505ecc23667e6d083a24f1afa7de58d744da04`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> The inline UPDATE is found by its shape, not by a comment.

## Module-level bindings

`BLOCK` (L40)

## Import declarations

```python
from __future__ import annotations
import pytest
from converter.postprocess.update_business_sql.update_sql_block_extractor import UpdateSqlBlockExtractor
```

## Local dependency notes

- [converter/postprocess/update_business_sql/update_sql_block_extractor.py](../../converter/postprocess/update_business_sql/update_sql_block_extractor.md)

## Symbol contracts and control points

### `_Host` - L23-L32

```python
class _Host(UpdateSqlBlockExtractor)
```

Smallest host that satisfies the mixin's detection path.

### `_Host._logical` - L27-L28

```python
_logical(line)
```

Observed calls (lexical order): `' '.join`, `str`, `str(line or '').split`.

### `_Host._is_comment_line` - L31-L32

```python
_is_comment_line(line)
```

Observed calls (lexical order): `str`, `str(line or '').lstrip`, `str(line or '').lstrip().startswith`.

### `extractor` - L36-L37

```python
extractor() -> _Host
```

Observed calls (lexical order): `_Host`.

### `test_a_block_without_any_anchor_is_still_found` - L59-L66

```python
test_a_block_without_any_anchor_is_still_found(extractor)
```

Observed calls (lexical order): `extractor._find_inline_update_block`, `len`.

### `test_the_structural_find_is_reported` - L69-L75

```python
test_the_structural_find_is_reported(extractor)
```

Observed calls (lexical order): `extractor._find_inline_update_block`, `len`, `any`.

### `test_a_paragraph_with_no_update_is_refused_out_loud` - L78-L85

```python
test_a_paragraph_with_no_update_is_refused_out_loud(extractor)
```

Observed calls (lexical order): `extractor._find_inline_update_block`, `len`, `any`.

### `test_the_marker_anchor_still_wins` - L88-L93

```python
test_the_marker_anchor_still_wins(extractor)
```

Observed calls (lexical order): `extractor._find_inline_update_block`, `len`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
