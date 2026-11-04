# `tests/test_generic_unused_copybook_and_group_move.py`

Source: [tests/test_generic_unused_copybook_and_group_move.py](../../../tests/test_generic_unused_copybook_and_group_move.py) | 65 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `5a8b1f6fc18c26bc7a6ba2b27a118c6bb6314a0902a3c66b31b098c8c204e32b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Generic safety contracts for data-dependent COPYs and composite MOVEs.

## Import declarations

```python
from __future__ import annotations
from pathlib import Path
from converter.composers.unused_copybook_pruner import UnusedCopybookPruner
from converter.domain.models import CopybookField
from converter.repositories.copybook_repository import CopybookRepository
from converter.composers.lrf_group_move_decomposer import LrfGroupMoveDecomposer
```

## Local dependency notes

- [converter/composers/lrf_group_move_decomposer.py](../converter/composers/lrf_group_move_decomposer.md)
- [converter/composers/unused_copybook_pruner.py](../converter/composers/unused_copybook_pruner.md)
- [converter/domain/models.py](../converter/domain/models.md)
- [converter/repositories/copybook_repository.py](../converter/repositories/copybook_repository.md)

## Symbol contracts and control points

### `fixed` - L12-L13

```python
fixed(body: str) -> str
```

### `test_prune_derived_copy_only_when_all_source_fields_are_dead` - L16-L25

```python
test_prune_derived_copy_only_when_all_source_fields_are_dead()
```

Observed calls (lexical order): `fixed`, `UnusedCopybookPruner`, `pruner.apply`.

### `test_keep_live_and_unknown_copybook_and_comments` - L28-L38

```python
test_keep_live_and_unknown_copybook_and_comments()
```

Observed calls (lexical order): `fixed`, `UnusedCopybookPruner`, `UnusedCopybookPruner({'VMBD77': source}).apply`, `UnusedCopybookPruner({}).apply`, `UnusedCopybookPruner({'VMBD77': fixed('COPY ANOTHER.')}).apply`.

Control points:

- L30: `for statement in ('DISPLAY SOURCE-ONLY.', 'MOVE ZERO TO VMBD77-R01.')`

### `test_generic_typed_children_require_exact_width_match` - L41-L55

```python
test_generic_typed_children_require_exact_width_match()
```

Observed calls (lexical order): `CopybookField`, `CopybookRepository`, `object.__new__`, `decomposer._width_matched_children`.

### `test_real_source_copybook_is_unused_in_generated_layout` - L58-L65

```python
test_real_source_copybook_is_unused_in_generated_layout()
```

Observed calls (lexical order): `Path`, `Path(__file__).resolve`, `(root / 'mainframe/workspace/Output').glob`, `next`, `UnusedCopybookPruner`, `UnusedCopybookPruner({'VMBD05': src.read_text(encoding='utf-8')}).apply`, `src.read_text`, `generated.read_text`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
