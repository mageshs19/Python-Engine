# `tests/test_lrf_source_access_comment_safety.py`

Source: [tests/test_lrf_source_access_comment_safety.py](../../../tests/test_lrf_source_access_comment_safety.py) | 52 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `ba91cad57e7586a03f294f0ab506d9c931b23cb6cf1e768a5e1528e2cf892c84`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.composers.bounded_lrf_singleton_rewriter import BoundedLrfSingletonRewriter
```

## Local dependency notes

- [converter/composers/bounded_lrf_singleton_rewriter.py](../converter/composers/bounded_lrf_singleton_rewriter.md)

## Symbol contracts and control points

### `test_source_access_scanner_ignores_idms_tokens_inside_quoted_literals` - L4-L10

```python
test_source_access_scanner_ignores_idms_tokens_inside_quoted_literals()
```

Observed calls (lexical order): `BoundedLrfSingletonRewriter._source_accesses`, `BoundedLrfSingletonRewriter._source_proves_first_only`.

### `test_source_access_scanner_ignores_inline_comments` - L13-L18

```python
test_source_access_scanner_ignores_inline_comments()
```

Observed calls (lexical order): `BoundedLrfSingletonRewriter._source_accesses`, `BoundedLrfSingletonRewriter._source_proves_first_only`.

### `test_real_executable_next_still_blocks_first_only_proof` - L21-L29

```python
test_real_executable_next_still_blocks_first_only_proof()
```

Observed calls (lexical order): `BoundedLrfSingletonRewriter._source_accesses`, `BoundedLrfSingletonRewriter._source_proves_first_only`.

### `test_source_access_scanner_detects_next_wrapped_across_physical_lines` - L32-L41

```python
test_source_access_scanner_detects_next_wrapped_across_physical_lines()
```

Observed calls (lexical order): `BoundedLrfSingletonRewriter._source_accesses`, `BoundedLrfSingletonRewriter._source_proves_first_only`.

### `test_source_access_scanner_does_not_detect_wrapped_tokens_inside_literals_or_comments` - L44-L52

```python
test_source_access_scanner_does_not_detect_wrapped_tokens_inside_literals_or_comments()
```

Observed calls (lexical order): `BoundedLrfSingletonRewriter._source_accesses`, `BoundedLrfSingletonRewriter._source_proves_first_only`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
