# `review/checks/chk_34_generated_structure.py`

Source: [review/checks/chk_34_generated_structure.py](../../../../review/checks/chk_34_generated_structure.py) | 20 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `4d4a4109035ffe99ab2e10a44ed30b9dada64bca8b71bbf2b44c0a380c2b8e7c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Independent structural release gate over the final generated COBOL.

## Import declarations

```python
from __future__ import annotations
from converter.validators.generated_cobol_release_validator import validate_generated_cobol
from review.engine.check_base import BOTH, CRITICAL, Check
```

## Local dependency notes

- [converter/validators/generated_cobol_release_validator.py](../../converter/validators/generated_cobol_release_validator.md)
- [review/engine/check_base.py](../engine/check_base.md)

## Symbol contracts and control points

### `GeneratedStructureCheck` - L8-L20

```python
class GeneratedStructureCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-34'
TITLE = 'Generated COBOL release structure and semantic safety'
SEVERITY = CRITICAL
APPLIES_TO = BOTH
ORDER = 340
```

### `GeneratedStructureCheck.review` - L15-L20

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `validate_generated_cobol`, `record.expect_none`.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
