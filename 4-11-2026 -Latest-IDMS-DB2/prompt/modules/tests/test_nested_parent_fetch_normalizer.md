# `tests/test_nested_parent_fetch_normalizer.py`

Source: [tests/test_nested_parent_fetch_normalizer.py](../../../tests/test_nested_parent_fetch_normalizer.py) | 117 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `730968a6f16d70ea711949f8926e0d1d0e1805cb025ab6324512c25a56a47ea8`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Reusable nested parent loop semantics, not a program-specific COBOL patch.

## Module-level bindings

`ROOT` (L11), `FIXTURE` (L12)

## Import declarations

```python
import re
from pathlib import Path
from converter.composers.cursor_close_guarantee.nested_parent_fetch_normalizer import NestedParentFetchNormalizer, _body
```

## Local dependency notes

- [converter/composers/cursor_close_guarantee/nested_parent_fetch_normalizer.py](../converter/composers/cursor_close_guarantee/nested_parent_fetch_normalizer.md)

## Symbol contracts and control points

### `_sample` - L15-L58

```python
_sample()
```

### `test_successful_parent_fetch_calls_exactly_one_business_paragraph` - L61-L74

```python
test_successful_parent_fetch_calls_exactly_one_business_paragraph()
```

Observed calls (lexical order): `_sample`, `NestedParentFetchNormalizer`, `normalizer.apply`, `_body`, `_body(line).upper`, `result.splitlines`, `lines.count`.

### `test_renaming_cursor_business_paragraph_and_child_is_supported` - L77-L85

```python
test_renaming_cursor_business_paragraph_and_child_is_supported()
```

Observed calls (lexical order): `_sample`, `_sample().replace`, `_sample().replace('APARENT', 'PARENTX').replace`, `_sample().replace('APARENT', 'PARENTX').replace('BCHILD', 'EVENTX').replace`, `NestedParentFetchNormalizer`, `normalizer.apply`.

### `test_rejects_ambiguous_graph_without_touching_source` - L88-L91

```python
test_rejects_ambiguous_graph_without_touching_source()
```

Observed calls (lexical order): `_sample`, `_sample().replace`, `NestedParentFetchNormalizer`, `NestedParentFetchNormalizer().apply`.

### `test_rejects_existing_row_business_link` - L94-L97

```python
test_rejects_existing_row_business_link()
```

Observed calls (lexical order): `_sample`, `_sample().replace`, `NestedParentFetchNormalizer`, `NestedParentFetchNormalizer().apply`.

### `test_real_nested_parent_cursor_fixture` - L100-L117

```python
test_real_nested_parent_cursor_fixture()
```

Observed calls (lexical order): `(ROOT / 'tests/fixtures/parent_nested_cursor_before_normalization.cbl').read_text`, `NestedParentFetchNormalizer`, `normalizer.apply`, `len`, `'\n'.join`, `_body`, `_body(line).upper`, `result.splitlines`, `re.findall`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
