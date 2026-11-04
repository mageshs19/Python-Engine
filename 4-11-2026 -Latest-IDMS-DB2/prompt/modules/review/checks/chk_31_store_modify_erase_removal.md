# `review/checks/chk_31_store_modify_erase_removal.py`

Source: [review/checks/chk_31_store_modify_erase_removal.py](../../../../review/checks/chk_31_store_modify_erase_removal.py) | 108 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `904de9e3ec6fcb5edf76dfe3f163dd67ee86334987fbdc7ba759168f389ec1b3`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-31 STORE/MODIFY/ERASE removal - IDMS update operations.

## Import declarations

```python
from __future__ import annotations
from review.engine import metadata as meta
from review.engine.check_base import CRITICAL, BOTH, Check
from review.standards import cobol_standards as std
```

## Local dependency notes

- [review/engine/__init__.py](../engine/__init__.md)
- [review/engine/check_base.py](../engine/check_base.md)
- [review/engine/metadata.py](../engine/metadata.md)
- [review/standards/__init__.py](../standards/__init__.md)
- [review/standards/cobol_standards.py](../standards/cobol_standards.md)

## Symbol contracts and control points

### `StoreModifyEraseRemovalCheck` - L22-L108

```python
class StoreModifyEraseRemovalCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-31'
TITLE = 'STORE/MODIFY/ERASE removal - IDMS update operations'
SEVERITY = CRITICAL
APPLIES_TO = BOTH
ORDER = 310
```

### `StoreModifyEraseRemovalCheck.relevant` - L29-L34

```python
relevant(self, ctx, view) -> bool
```

Observed calls (lexical order): `any`, `view.logical_text`.

### `StoreModifyEraseRemovalCheck.not_relevant_reason` - L36-L37

```python
not_relevant_reason(self) -> str
```

### `StoreModifyEraseRemovalCheck.review` - L39-L108

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `l.logical.strip`, `l.logical.strip().startswith`, `record.expect_none`, `any`, `record.fail`, `record.ok`.

Control points:

- L98: `if store_residual or modify_residual or erase_residual`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
