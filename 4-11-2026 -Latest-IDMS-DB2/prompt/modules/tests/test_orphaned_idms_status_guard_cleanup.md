# `tests/test_orphaned_idms_status_guard_cleanup.py`

Source: [tests/test_orphaned_idms_status_guard_cleanup.py](../../../tests/test_orphaned_idms_status_guard_cleanup.py) | 21 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `bf8b8a33204ac7d6326cc76740b4041f6d6745694a609fd717a962051113b665`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.composers.cleanup.cleanup_message_collector import CleanupMessageCollector
from converter.composers.cleanup.orphaned_idms_status_guard_cleanup import OrphanedIdmsStatusGuardCleanup
```

## Local dependency notes

- [converter/composers/cleanup/cleanup_message_collector.py](../converter/composers/cleanup/cleanup_message_collector.md)
- [converter/composers/cleanup/orphaned_idms_status_guard_cleanup.py](../converter/composers/cleanup/orphaned_idms_status_guard_cleanup.md)

## Symbol contracts and control points

### `test_removes_only_obsolete_bind_ready_status_guard` - L5-L21

```python
test_removes_only_obsolete_bind_ready_status_guard()
```

Observed calls (lexical order): `CleanupMessageCollector`, `OrphanedIdmsStatusGuardCleanup`, `OrphanedIdmsStatusGuardCleanup(messages).apply`, `output.splitlines`, `len`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
