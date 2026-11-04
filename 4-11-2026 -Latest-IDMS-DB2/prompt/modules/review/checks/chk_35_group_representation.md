# `review/checks/chk_35_group_representation.py`

Source: [review/checks/chk_35_group_representation.py](../../../../review/checks/chk_35_group_representation.py) | 27 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `daf7eafe3a4cbe0950133cdd8b3c6275f7c06a865ae25abc59e7c7a9c690cc20`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Source-derived data representation safety, independent of paragraph names.

## Import declarations

```python
from mainframe.verification.group_representation_contract import audit_character_group_moves, audit_target_character_widths
from review.engine.check_base import BOTH, CRITICAL, Check
```

## Local dependency notes

- [mainframe/verification/group_representation_contract.py](../../mainframe/verification/group_representation_contract.md)
- [review/engine/check_base.py](../engine/check_base.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [tests/test_full_program_representation_audit.py](../../tests/test_full_program_representation_audit.md)

## Symbol contracts and control points

### `GroupRepresentationCheck` - L8-L27

```python
class GroupRepresentationCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-35'
TITLE = 'Character-host group representation and mapping agreement'
SEVERITY = CRITICAL
APPLIES_TO = BOTH
ORDER = 350
```

### `GroupRepresentationCheck.relevant` - L15-L16

```python
relevant(self, ctx, view)
```

Observed calls (lexical order): `bool`.

### `GroupRepresentationCheck.not_relevant_reason` - L18-L19

```python
not_relevant_reason(self)
```

### `GroupRepresentationCheck.review` - L21-L27

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `audit_character_group_moves`, `record.expect_none`, `audit_target_character_widths`.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
