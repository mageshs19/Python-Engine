# `review/engine/check_base.py`

Source: [review/engine/check_base.py](../../../../review/engine/check_base.py) | 119 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `16971f2baf5979e5a52b069a404be02f1793bc8b263d8ac443ddad1aac8114b0`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Base class and recorder for a single code review check.

## Module-level bindings

`CRITICAL` (L9), `MAJOR` (L10), `MINOR` (L11), `BOTH` (L13), `RETRIEVAL` (L14), `UPDATE` (L15)

## Import declarations

```python
from __future__ import annotations
from review.engine.cobol_view import CobolView, Line
from review.engine.context import ReviewContext
from review.engine.models import Criterion, Finding, Outcome
```

## Local dependency notes

- [review/engine/cobol_view.py](cobol_view.md)
- [review/engine/context.py](context.md)
- [review/engine/models.py](models.md)

## Importers (39)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [review/checks/chk_01_line_layout.py](../checks/chk_01_line_layout.md)
- [review/checks/chk_02_db2_infrastructure.py](../checks/chk_02_db2_infrastructure.md)
- [review/checks/chk_03_residual_idms.py](../checks/chk_03_residual_idms.md)
- [review/checks/chk_04_program_header.py](../checks/chk_04_program_header.md)
- [review/checks/chk_05_sql_error_routing.py](../checks/chk_05_sql_error_routing.md)
- [review/checks/chk_06_area_alignment.py](../checks/chk_06_area_alignment.md)
- [review/checks/chk_07_sequence_continuity.py](../checks/chk_07_sequence_continuity.md)
- [review/checks/chk_08_dclgen_include_integrity.py](../checks/chk_08_dclgen_include_integrity.md)
- [review/checks/chk_09_record_retrieval_conversion.py](../checks/chk_09_record_retrieval_conversion.md)
- [review/checks/chk_10_record_modification_conversion.py](../checks/chk_10_record_modification_conversion.md)
- [review/checks/chk_11_sqlcode_commit_conversion.py](../checks/chk_11_sqlcode_commit_conversion.md)
- [review/checks/chk_12_cursor_declaration.py](../checks/chk_12_cursor_declaration.md)
- [tests/test_full_program_representation_audit.py](../../tests/test_full_program_representation_audit.md)
- 26 further importers are recorded in [the source manifest](../../../source_manifest.json).

## Symbol contracts and control points

### `_finding` - L18-L23

```python
_finding(item) -> Finding
```

Observed calls (lexical order): `isinstance`, `Finding`, `item.body.rstrip`, `str`.

Control points:

- L19: `if isinstance(item, Line)`
- L21: `if isinstance(item, Finding)`

### `Recorder` - L27-L94

```python
class Recorder()
```

Collects criterion outcomes for one check.

### `Recorder.__init__` - L30-L33

```python
__init__(self, check_id: str, limit: int=10) -> None
```

### `Recorder._add` - L35-L44

```python
_add(self, num, desc, outcome, note='', findings=None) -> None
```

Observed calls (lexical order): `self.criteria.append`, `Criterion`, `_finding`, `list`.

### `Recorder.ok` - L46-L47

```python
ok(self, num, desc) -> None
```

Observed calls (lexical order): `self._add`.

### `Recorder.pass_all` - L51-L64

```python
pass_all(self, num, desc) -> None
```

Record a criterion as passing with nothing to report.

Observed calls (lexical order): `self.ok`.

### `Recorder.fail` - L66-L67

```python
fail(self, num, desc, note='', findings=None) -> None
```

Observed calls (lexical order): `self._add`.

### `Recorder.skip` - L69-L70

```python
skip(self, num, desc, reason='') -> None
```

Observed calls (lexical order): `self._add`.

### `Recorder.expect` - L72-L76

```python
expect(self, num, desc, condition, note='', findings=None) -> None
```

Observed calls (lexical order): `self.ok`, `self.fail`.

Control points:

- L73: `if condition`

### `Recorder.expect_none` - L78-L85

```python
expect_none(self, num, desc, offenders, note='') -> None
```

Observed calls (lexical order): `list`, `self.expect`, `len`.

### `Recorder.expect_all` - L87-L94

```python
expect_all(self, num, desc, missing, note='') -> None
```

Observed calls (lexical order): `list`, `self.expect`, `', '.join`, `str`.

### `Check` - L97-L119

```python
class Check()
```

Base class for every code review check.

Declared class/data-model fields:

```python
CHECK_ID: str = ''
TITLE: str = ''
SEVERITY: str = MAJOR
APPLIES_TO: str = BOTH
NEEDS: tuple[str, ...] = ('converted_cobol',)
ORDER: int = 0
```

### `Check.applies` - L107-L109

```python
applies(self, ctx: ReviewContext) -> bool
```

Observed calls (lexical order): `str`, `str(self.APPLIES_TO).upper`, `str(ctx.program_kind).upper`.

### `Check.relevant` - L111-L113

```python
relevant(self, ctx: ReviewContext, view: CobolView) -> bool
```

Override when the check only makes sense for some programs.

### `Check.not_relevant_reason` - L115-L116

```python
not_relevant_reason(self) -> str
```

### `Check.review` - L118-L119

```python
review(self, ctx: ReviewContext, view: CobolView, record: Recorder) -> None
```

Explicit raises: `NotImplementedError`.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
