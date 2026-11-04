# `tests/test_lrf_keyword_scope_safety.py`

Source: [tests/test_lrf_keyword_scope_safety.py](../../../tests/test_lrf_keyword_scope_safety.py) | 94 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `1be54296ee0d10a87ba70cef9f2c2c26e661bf03ca209ea14f26628a29399119`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> A path keyword must never resolve against a different logical record.

## Import declarations

```python
from converter.domain.models import LogicalRecord, LrfPath
from converter.repositories.lrf_repository import LrfRepository
from converter.resolvers.lrf_path_resolver import LrfPathResolver
from converter.domain.models import LrfPathCommand
from converter.transformers.lrf_path_expander import LrfPathExpander
```

## Local dependency notes

- [converter/domain/models.py](../converter/domain/models.md)
- [converter/repositories/lrf_repository.py](../converter/repositories/lrf_repository.md)
- [converter/resolvers/lrf_path_resolver.py](../converter/resolvers/lrf_path_resolver.md)
- [converter/transformers/lrf_path_expander.py](../converter/transformers/lrf_path_expander.md)

## Symbol contracts and control points

### `_record` - L7-L22

```python
_record(lr_name: str, keyword: str, driving: str) -> LogicalRecord
```

Observed calls (lexical order): `LogicalRecord`, `LrfPath`, `LrfPathCommand`.

### `test_duplicate_keyword_resolves_using_explicit_logical_record_scope` - L25-L37

```python
test_duplicate_keyword_resolves_using_explicit_logical_record_scope()
```

Observed calls (lexical order): `LrfRepository`, `_record`, `repo.path_for_keyword`.

### `test_duplicate_keyword_without_scope_is_refused_as_ambiguous` - L40-L47

```python
test_duplicate_keyword_without_scope_is_refused_as_ambiguous()
```

Observed calls (lexical order): `LrfRepository`, `_record`, `repo.path_for_keyword`, `LrfPathResolver`, `LrfPathResolver(lrf_repository=repo).plan_for_keyword`.

### `test_unknown_logical_record_does_not_fall_back_to_other_lr` - L50-L56

```python
test_unknown_logical_record_does_not_fall_back_to_other_lr()
```

Observed calls (lexical order): `LrfRepository`, `_record`, `repo.path_for_keyword`, `LrfPathResolver`, `LrfPathResolver(lrf_repository=repo).plan_for_keyword`.

### `test_expander_uses_the_source_logical_record_not_first_matching_keyword` - L59-L78

```python
test_expander_uses_the_source_logical_record_not_first_matching_keyword()
```

Observed calls (lexical order): `LrfRepository`, `_record`, `LrfPathExpander`, `LrfPathResolver`, `expander.expand`, `'\n'.join`, `output.splitlines`, `len`.

### `test_expander_refuses_keyword_when_source_lr_is_unresolved` - L81-L94

```python
test_expander_refuses_keyword_when_source_lr_is_unresolved()
```

Observed calls (lexical order): `LrfRepository`, `_record`, `LrfPathExpander`, `LrfPathResolver`, `expander.expand`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
