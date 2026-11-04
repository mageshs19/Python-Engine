# `tests/test_residual_idms_error_clause_cleanup.py`

Source: [tests/test_residual_idms_error_clause_cleanup.py](../../../tests/test_residual_idms_error_clause_cleanup.py) | 43 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `07364b6795371d812f62aba33b85d76a921981f6419f96878d3c52f22155aaad`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.composers.cleanup.cleanup_message_collector import CleanupMessageCollector
from converter.composers.cleanup.residual_idms_error_clause_cleanup import ResidualIdmsErrorClauseCleanup
```

## Local dependency notes

- [converter/composers/cleanup/cleanup_message_collector.py](../converter/composers/cleanup/cleanup_message_collector.md)
- [converter/composers/cleanup/residual_idms_error_clause_cleanup.py](../converter/composers/cleanup/residual_idms_error_clause_cleanup.md)

## Symbol contracts and control points

### `test_removes_known_idms_status_handler_pair` - L5-L17

```python
test_removes_known_idms_status_handler_pair()
```

Observed calls (lexical order): `CleanupMessageCollector`, `ResidualIdmsErrorClauseCleanup`, `cleanup.apply`, `any`.

### `test_removes_orphaned_clause_when_prior_cleanup_reports_removed_handler` - L20-L31

```python
test_removes_orphaned_clause_when_prior_cleanup_reports_removed_handler()
```

Observed calls (lexical order): `CleanupMessageCollector`, `ResidualIdmsErrorClauseCleanup`, `cleanup.apply`.

### `test_unknown_handler_is_preserved_and_reported` - L34-L43

```python
test_unknown_handler_is_preserved_and_reported()
```

Observed calls (lexical order): `CleanupMessageCollector`, `ResidualIdmsErrorClauseCleanup`, `cleanup.apply`, `any`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
