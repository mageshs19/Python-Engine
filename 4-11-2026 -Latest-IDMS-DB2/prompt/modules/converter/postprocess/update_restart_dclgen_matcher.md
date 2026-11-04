# `converter/postprocess/update_restart_dclgen_matcher.py`

Source: [converter/postprocess/update_restart_dclgen_matcher.py](../../../../converter/postprocess/update_restart_dclgen_matcher.py) | 230 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `4cce33e9d5ae20ecc24ca8731dbe134d788b1380a4ecf4f709412cb3447c33d5`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from typing import Optional
from converter.postprocess.update_metadata_models import compact
```

## Local dependency notes

- [converter/postprocess/update_metadata_models.py](update_metadata_models.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/update_restart_dclgen_resolver.py](update_restart_dclgen_resolver.md)
- [converter/postprocess/update_restart_dclgen_role_builder.py](update_restart_dclgen_role_builder.md)

## Symbol contracts and control points

### `UpdateRestartDclgenMatcher` - L8-L230

```python
class UpdateRestartDclgenMatcher()
```

Finds restart columns or COBOL host fields using token matching.

### `UpdateRestartDclgenMatcher.find_optional_col` - L23-L39

```python
find_optional_col(self, *, rows: list[dict[str, str]], tokens: list[str], fallback_tokens: Optional[list[str]]=None, exclude_tokens: Optional[list[str]]=None) -> str
```

Observed calls (lexical order): `self.find_col`.

### `UpdateRestartDclgenMatcher.find_optional_field` - L41-L57

```python
find_optional_field(self, *, rows: list[dict[str, str]], tokens: list[str], fallback_tokens: Optional[list[str]]=None, exclude_tokens: Optional[list[str]]=None) -> str
```

Observed calls (lexical order): `self.find_field`.

### `UpdateRestartDclgenMatcher.find_col` - L59-L73

```python
find_col(self, *, rows: list[dict[str, str]], tokens: list[str], fallback_tokens: Optional[list[str]]=None, exclude_tokens: Optional[list[str]]=None) -> str
```

Observed calls (lexical order): `self.find_by_key`.

### `UpdateRestartDclgenMatcher.find_field` - L75-L89

```python
find_field(self, *, rows: list[dict[str, str]], tokens: list[str], fallback_tokens: Optional[list[str]]=None, exclude_tokens: Optional[list[str]]=None) -> str
```

Observed calls (lexical order): `self.find_by_key`.

### `UpdateRestartDclgenMatcher.find_by_key` - L91-L135

```python
find_by_key(self, *, rows: list[dict[str, str]], key: str, tokens: list[str], fallback_tokens: Optional[list[str]]=None, exclude_tokens: Optional[list[str]]=None) -> str
```

Observed calls (lexical order): `enumerate`, `row.get`, `str`, `str(row.get(key, '') or '').strip`, `self._searchable_row_text`, `self._has_excluded_token`, `self._match_score`, `scored.append`, `ValueError`, `scored.sort`.

Control points:

- L105: `for (index, row) in enumerate(rows)`
- L108: `if not value`
- L113: `if self._has_excluded_token(searchable=searchable, exclude_tokens=exclude_tokens)`
- L125: `if score > 0`
- L128: `if not scored`

Explicit raises: `ValueError(f'Unable to resolve restart field using tokens {tokens}')`.

### `UpdateRestartDclgenMatcher.score_rows_for_restart` - L137-L157

```python
score_rows_for_restart(self, *, rows: list[dict[str, str]], token_sets: list[list[str]]) -> int
```

Observed calls (lexical order): `self._searchable_row_text`, `compact`, `self._token_set_found`, `len`.

Control points:

- L145: `for row in rows`
- L148: `for tokens in token_sets`
- L151: `if self._token_set_found(searchable=searchable, tokens=tokens)`

### `UpdateRestartDclgenMatcher._searchable_row_text` - L159-L175

```python
_searchable_row_text(self, *, row: dict[str, str], primary_key: str) -> str
```

Observed calls (lexical order): `row.get`, `' '.join`, `compact`, `str`.

### `UpdateRestartDclgenMatcher._match_score` - L177-L204

```python
_match_score(self, *, searchable: str, tokens: list[str], fallback_tokens: list[str]) -> int
```

Observed calls (lexical order): `compact`, `self._token_set_found`, `len`.

Control points:

- L186: `if self._token_set_found(searchable=searchable, tokens=tokens)`
- L198: `if self._token_set_found(searchable=searchable, tokens=fallback_tokens)`

### `UpdateRestartDclgenMatcher._token_set_found` - L206-L217

```python
_token_set_found(self, *, searchable: str, tokens: list[str]) -> bool
```

Observed calls (lexical order): `compact`, `all`.

Control points:

- L214: `if not compact_tokens`

### `UpdateRestartDclgenMatcher._has_excluded_token` - L219-L230

```python
_has_excluded_token(self, *, searchable: str, exclude_tokens: list[str]) -> bool
```

Observed calls (lexical order): `compact`, `any`.

Control points:

- L227: `if not compact_tokens`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
