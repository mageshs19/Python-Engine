# `tests/test_lrf_update_expander.py`

Source: [tests/test_lrf_update_expander.py](../../../tests/test_lrf_update_expander.py) | 403 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `6aca7e408ae9f96e4260d0f2d8720fb75ccebc0d2d2f1e34fdabc13b9dfe0787`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> LRF update (MODIFY / STORE) expansion tests.

## Module-level bindings

`SUBSCHEMA` (L21), `COMMENT_INDICATORS` (L51)

## Import declarations

```python
from converter.parsers.lrf_parser import LrfParser
from converter.repositories.lrf_repository import LrfRepository
from converter.resolvers.lrf_path_resolver import LrfPathResolver
from converter.transformers.lrf_update_expander import LrfUpdateExpander
```

## Local dependency notes

- [converter/parsers/lrf_parser.py](../converter/parsers/lrf_parser.md)
- [converter/repositories/lrf_repository.py](../converter/repositories/lrf_repository.md)
- [converter/resolvers/lrf_path_resolver.py](../converter/resolvers/lrf_path_resolver.md)
- [converter/transformers/lrf_update_expander.py](../converter/transformers/lrf_update_expander.md)

## Symbol contracts and control points

### `_expander` - L55-L61

```python
_expander(mapping_repository=None)
```

Observed calls (lexical order): `LrfParser`, `LrfParser().parse`, `LrfPathResolver`, `LrfRepository`, `LrfUpdateExpander`.

### `_is_comment` - L64-L68

```python
_is_comment(line: str) -> bool
```

Observed calls (lexical order): `str`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`, `text.lstrip`, `text.lstrip().startswith`.

Control points:

- L66: `if len(text) >= 7 and text[:6].strip().isdigit()`

### `_executable` - L71-L75

```python
_executable(output: str) -> str
```

Observed calls (lexical order): `'\n'.join`, `str`, `str(output or '').splitlines`, `_is_comment`, `line.strip`.

### `_comments` - L78-L82

```python
_comments(output: str) -> str
```

Observed calls (lexical order): `'\n'.join`, `str`, `str(output or '').splitlines`, `_is_comment`.

### `test_modify_is_expanded_to_classic_idms` - L86-L96

```python
test_modify_is_expanded_to_classic_idms()
```

Observed calls (lexical order): `_executable`, `_expander`, `_expander().expand`.

### `test_modify_expansion_keeps_an_audit_trail` - L99-L108

```python
test_modify_expansion_keeps_an_audit_trail()
```

Observed calls (lexical order): `_comments`, `_expander`, `_expander().expand`.

### `test_expanded_names_use_cobol_hyphens_never_underscores` - L111-L116

```python
test_expanded_names_use_cobol_hyphens_never_underscores()
```

Observed calls (lexical order): `_expander`, `_expander().expand`.

### `test_store_into_single_element_lr_is_expanded` - L119-L145

```python
test_store_into_single_element_lr_is_expanded()
```

A STORE keyword whose logical record has one element is unambiguous.

Observed calls (lexical order): `LrfParser`, `LrfParser().parse`, `LrfPathResolver`, `LrfRepository`, `LrfUpdateExpander`, `_executable`, `expander.expand`.

### `test_store_exact_element_keyword_resolves_multi_element_logical_record` - L149-L180

```python
test_store_exact_element_keyword_resolves_multi_element_logical_record()
```

ST-<element> is precise even when the LR contains several elements.

Observed calls (lexical order): `LrfParser`, `LrfParser().parse`, `LrfPathResolver`, `LrfRepository`, `LrfUpdateExpander`, `expander.expand`, `_executable`, `_comments`.

### `test_store_with_multiple_elements_is_kept_for_manual_review` - L183-L196

```python
test_store_with_multiple_elements_is_kept_for_manual_review()
```

Observed calls (lexical order): `_expander`, `_expander().expand`, `_comments`, `_executable`.

### `test_unknown_keyword_is_kept_and_commented` - L199-L208

```python
test_unknown_keyword_is_kept_and_commented()
```

Observed calls (lexical order): `_expander`, `_expander().expand`, `_comments`, `_executable`.

### `test_unmapped_record_is_kept_for_manual_review` - L211-L223

```python
test_unmapped_record_is_kept_for_manual_review()
```

Observed calls (lexical order): `_NoRecordMapping`, `_expander`, `_expander(mapping_repository=_NoRecordMapping()).expand`, `_comments`, `_executable`.

### `test_unmapped_record_is_kept_for_manual_review._NoRecordMapping` - L212-L214

```python
class _NoRecordMapping()
```

### `test_unmapped_record_is_kept_for_manual_review._NoRecordMapping.has_record` - L213-L214

```python
has_record(self, _record)
```

### `test_without_lrf_metadata_source_is_unchanged` - L227-L237

```python
test_without_lrf_metadata_source_is_unchanged()
```

Observed calls (lexical order): `LrfPathResolver`, `LrfRepository`, `LrfUpdateExpander`, `expander.expand`.

### `test_program_without_lrf_update_syntax_is_unchanged` - L240-L246

```python
test_program_without_lrf_update_syntax_is_unchanged()
```

Observed calls (lexical order): `_expander`, `_expander().expand`.

### `test_no_path_resolver_returns_source_unchanged` - L249-L255

```python
test_no_path_resolver_returns_source_unchanged()
```

Observed calls (lexical order): `LrfUpdateExpander`, `expander.expand`.

### `test_data_division_lines_are_never_touched` - L259-L265

```python
test_data_division_lines_are_never_touched()
```

Observed calls (lexical order): `_expander`, `_expander().expand`, `_executable`.

### `test_comment_lines_are_never_expanded` - L268-L274

```python
test_comment_lines_are_never_expanded()
```

Observed calls (lexical order): `_expander`, `_expander().expand`, `_executable`.

### `test_mismatched_source_logical_record_is_retained` - L277-L288

```python
test_mismatched_source_logical_record_is_retained()
```

A keyword must not authorize rewriting a different LR name.

Observed calls (lexical order): `_expander`, `_expander().expand`, `_executable`, `_comments`.

### `test_modify_cannot_use_store_path_keyword` - L291-L302

```python
test_modify_cannot_use_store_path_keyword()
```

Path-group verb is part of the contract, not just the keyword.

Observed calls (lexical order): `_expander`, `_expander().expand`, `_executable`, `_comments`.

### `test_multiline_store_where_keyword_is_joined_and_expanded` - L305-L335

```python
test_multiline_store_where_keyword_is_joined_and_expanded()
```

Observed calls (lexical order): `LrfParser`, `LrfParser().parse`, `LrfUpdateExpander`, `LrfPathResolver`, `LrfRepository`, `expander.expand`, `_executable`, `_comments`.

### `test_multiline_modify_keyword_on_next_line_is_expanded` - L338-L348

```python
test_multiline_modify_keyword_on_next_line_is_expanded()
```

Observed calls (lexical order): `_expander`, `_expander().expand`, `_executable`.

### `test_multiline_update_with_extra_predicate_fails_closed_and_keeps_all_lines` - L351-L364

```python
test_multiline_update_with_extra_predicate_fails_closed_and_keeps_all_lines()
```

Observed calls (lexical order): `_expander`, `_expander().expand`, `_comments`, `_executable`.

### `test_multiline_update_fixed_format_preserves_columns_and_sequence_areas` - L367-L403

```python
test_multiline_update_fixed_format_preserves_columns_and_sequence_areas()
```

Observed calls (lexical order): `LrfParser`, `LrfParser().parse`, `LrfUpdateExpander`, `LrfPathResolver`, `LrfRepository`, `'\n'.join`, `fixed`, `expander.expand`, `out.splitlines`, `len`, `any`, `all`, `line[72:80].isdigit`, `line[:6].isdigit`.

### `test_multiline_update_fixed_format_preserves_columns_and_sequence_areas.fixed` - L386-L387

```python
fixed(sequence: int, body: str, indicator: str=' ') -> str
```

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
