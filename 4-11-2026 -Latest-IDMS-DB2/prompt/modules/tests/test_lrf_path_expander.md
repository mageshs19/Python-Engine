# `tests/test_lrf_path_expander.py`

Source: [tests/test_lrf_path_expander.py](../../../tests/test_lrf_path_expander.py) | 382 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `49f0143663d654f642f3c68881a9a99a9e96a921f35cec68f2641f858bbf4d4d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> LRF path expansion tests.

## Module-level bindings

`SUBSCHEMA` (L20), `COMMENT_INDICATORS` (L44)

## Import declarations

```python
from converter.parsers.lrf_parser import LrfParser
from converter.repositories.lrf_repository import LrfRepository
from converter.resolvers.lrf_path_resolver import LrfPathResolver
from converter.transformers.lrf_path_expander import LrfPathExpander
from rules.lrf_conversion_rules import LRF_PARENT_NOT_FOUND_TOKEN, RECORD_NOT_FOUND_TOKEN
```

## Local dependency notes

- [converter/parsers/lrf_parser.py](../converter/parsers/lrf_parser.md)
- [converter/repositories/lrf_repository.py](../converter/repositories/lrf_repository.md)
- [converter/resolvers/lrf_path_resolver.py](../converter/resolvers/lrf_path_resolver.md)
- [converter/transformers/lrf_path_expander.py](../converter/transformers/lrf_path_expander.md)
- [rules/lrf_conversion_rules.py](../rules/lrf_conversion_rules.md)

## Symbol contracts and control points

### `_expander` - L48-L54

```python
_expander()
```

Observed calls (lexical order): `LrfParser`, `LrfParser().parse`, `LrfPathResolver`, `LrfRepository`, `LrfPathExpander`.

### `_is_comment` - L57-L61

```python
_is_comment(line: str) -> bool
```

Observed calls (lexical order): `str`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`, `text.lstrip`, `text.lstrip().startswith`.

Control points:

- L59: `if len(text) >= 7 and text[:6].strip().isdigit()`

### `_executable` - L64-L69

```python
_executable(output: str) -> str
```

Only the executable lines - comments and audit trail removed.

Observed calls (lexical order): `'\n'.join`, `str`, `str(output or '').splitlines`, `_is_comment`, `line.strip`.

### `_comments` - L72-L77

```python
_comments(output: str) -> str
```

Only the comment lines.

Observed calls (lexical order): `'\n'.join`, `str`, `str(output or '').splitlines`, `_is_comment`.

### `test_parser_reads_logical_record_and_paths` - L81-L91

```python
test_parser_reads_logical_record_and_paths()
```

Observed calls (lexical order): `LrfParser`, `LrfParser().parse`, `len`.

### `test_obtain_first_is_expanded_to_classic_idms` - L95-L106

```python
test_obtain_first_is_expanded_to_classic_idms()
```

Observed calls (lexical order): `_expander`, `_expander().expand`, `_executable`.

### `test_expansion_keeps_an_audit_trail` - L109-L119

```python
test_expansion_keeps_an_audit_trail()
```

Observed calls (lexical order): `_expander`, `_expander().expand`, `_comments`.

### `test_obtain_next_is_expanded_without_parent_access` - L122-L130

```python
test_obtain_next_is_expanded_without_parent_access()
```

Observed calls (lexical order): `_executable`, `_expander`, `_expander().expand`.

### `test_obtain_first_emits_parent_access_for_join_path` - L133-L144

```python
test_obtain_first_emits_parent_access_for_join_path()
```

Observed calls (lexical order): `_executable`, `_expander`, `_expander().expand`, `code.index`.

### `test_expanded_names_use_cobol_hyphens_never_underscores` - L147-L155

```python
test_expanded_names_use_cobol_hyphens_never_underscores()
```

Observed calls (lexical order): `_expander`, `_expander().expand`.

### `test_lr_status_condition_becomes_end_of_set_token` - L159-L167

```python
test_lr_status_condition_becomes_end_of_set_token()
```

Observed calls (lexical order): `_executable`, `_expander`, `_expander().expand`.

### `test_not_found_literal_becomes_record_not_found_token` - L170-L178

```python
test_not_found_literal_becomes_record_not_found_token()
```

Observed calls (lexical order): `_executable`, `_expander`, `_expander().expand`.

### `test_of_lr_qualifier_is_stripped` - L182-L190

```python
test_of_lr_qualifier_is_stripped()
```

Observed calls (lexical order): `_executable`, `_expander`, `_expander().expand`.

### `test_unknown_keyword_is_kept_and_commented` - L194-L206

```python
test_unknown_keyword_is_kept_and_commented()
```

Observed calls (lexical order): `_expander`, `_expander().expand`, `_comments`, `_executable`.

### `test_without_lrf_metadata_source_is_unchanged` - L210-L220

```python
test_without_lrf_metadata_source_is_unchanged()
```

Observed calls (lexical order): `LrfPathResolver`, `LrfRepository`, `LrfPathExpander`, `expander.expand`.

### `test_program_without_lrf_syntax_is_unchanged` - L223-L229

```python
test_program_without_lrf_syntax_is_unchanged()
```

Observed calls (lexical order): `_expander`, `_expander().expand`.

### `test_no_path_resolver_returns_source_unchanged` - L232-L238

```python
test_no_path_resolver_returns_source_unchanged()
```

Observed calls (lexical order): `LrfPathExpander`, `expander.expand`.

### `test_data_division_lines_are_never_touched` - L242-L248

```python
test_data_division_lines_are_never_touched()
```

Observed calls (lexical order): `_expander`, `_expander().expand`.

### `test_comment_lines_are_never_expanded` - L251-L257

```python
test_comment_lines_are_never_expanded()
```

Observed calls (lexical order): `_expander`, `_expander().expand`, `_executable`.

### `_fixed_line` - L259-L260

```python
_fixed_line(seq: int, body: str) -> str
```

### `test_fixed_format_lrf_is_detected_without_status_or_of_lr` - L263-L273

```python
test_fixed_format_lrf_is_detected_without_status_or_of_lr()
```

Observed calls (lexical order): `'\n'.join`, `_fixed_line`, `_expander`, `_expander().expand`, `_executable`.

### `test_lrf_where_can_start_on_next_fixed_format_line` - L276-L287

```python
test_lrf_where_can_start_on_next_fixed_format_line()
```

Observed calls (lexical order): `'\n'.join`, `_fixed_line`, `_expander`, `_expander().expand`, `_executable`.

### `test_incomplete_obtain_does_not_consume_following_perform` - L290-L299

```python
test_incomplete_obtain_does_not_consume_following_perform()
```

Observed calls (lexical order): `'\n'.join`, `_fixed_line`, `_expander`, `_expander().expand`.

### `test_unterminated_wrapped_lrf_does_not_swallow_next_statement` - L302-L316

```python
test_unterminated_wrapped_lrf_does_not_swallow_next_statement()
```

Observed calls (lexical order): `'\n'.join`, `_fixed_line`, `_expander`, `_expander().expand`.

### `test_lrf_parent_not_found_status_is_distinct_from_child_not_found` - L319-L327

```python
test_lrf_parent_not_found_status_is_distinct_from_child_not_found()
```

Observed calls (lexical order): `_expander`, `expander._status_token`.

### `test_subschema_status_metadata_overrides_literal_name_heuristics` - L330-L354

```python
test_subschema_status_metadata_overrides_literal_name_heuristics()
```

The ON-status RETURN meaning wins over suffix-based guessing.

Observed calls (lexical order): `SUBSCHEMA.replace`, `LrfParser`, `LrfParser().parse`, `LrfPathResolver`, `LrfRepository`, `LrfPathExpander`, `expander.expand`.

### `test_conflicting_subschema_status_meanings_are_refused` - L357-L382

```python
test_conflicting_subschema_status_meanings_are_refused()
```

A literal with conflicting ON-status meanings must not be guessed.

Observed calls (lexical order): `SUBSCHEMA.replace`, `LrfParser`, `LrfParser().parse`, `LrfPathResolver`, `LrfRepository`, `LrfPathExpander`, `expander.expand`, `any`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
