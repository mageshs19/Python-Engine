# `review/checks/chk_36_production_evidence.py`

Source: [review/checks/chk_36_production_evidence.py](../../../../review/checks/chk_36_production_evidence.py) | 26 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `8c0d67dc9ec14a55a53de1bfdadff6c861bd2c1f561379653a527d43fb2bb653`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> A production review cannot silently skip missing source/schema evidence.

## Import declarations

```python
import re
from review.engine.check_base import BOTH, CRITICAL, Check
```

## Local dependency notes

- [review/engine/check_base.py](../engine/check_base.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [tests/test_full_program_representation_audit.py](../../tests/test_full_program_representation_audit.md)

## Symbol contracts and control points

### `ProductionEvidenceCheck` - L6-L26

```python
class ProductionEvidenceCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-36'
TITLE = 'Per-program production review evidence'
SEVERITY = CRITICAL
APPLIES_TO = BOTH
ORDER = 360
```

### `ProductionEvidenceCheck.relevant` - L13-L14

```python
relevant(self, ctx, view)
```

### `ProductionEvidenceCheck.not_relevant_reason` - L16-L17

```python
not_relevant_reason(self)
```

### `ProductionEvidenceCheck.review` - L19-L26

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `bool`, `ctx.source_cobol.strip`, `record.expect`, `any`, `re.search`, `re.match`, `record.expect_none`.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
