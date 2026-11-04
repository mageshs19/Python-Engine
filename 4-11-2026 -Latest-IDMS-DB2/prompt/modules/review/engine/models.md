# `review/engine/models.py`

Source: [review/engine/models.py](../../../../review/engine/models.py) | 188 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `eca6de221b6113574d7bb60152da1dabd595c2eb3c05e1761a30b53a5b8131bd`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Code review result models. Data only.

## Module-level bindings

`_RANK` (L22)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
```

## Importers (6)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [review/engine/__init__.py](__init__.md)
- [review/engine/check_base.py](check_base.md)
- [review/engine/reviewer.py](reviewer.md)
- [review/report/csv_writer.py](../report/csv_writer.md)
- [review/report/text_writer.py](../report/text_writer.md)
- [review/ui/review_panel.py](../ui/review_panel.md)

## Symbol contracts and control points

### `Outcome` - L14-L18

```python
class Outcome(str, Enum)
```

Declared class/data-model fields:

```python
PASS = 'PASS'
FAIL = 'FAIL'
SKIPPED = 'SKIPPED'
BLOCKED = 'BLOCKED'
```

### `worst` - L30-L37

```python
worst(items: list[Outcome]) -> Outcome
```

Strict reduction: the most severe outcome in the list.

Observed calls (lexical order): `max`.

### `Finding` - L41-L49

```python
class Finding()
```

Declared class/data-model fields:

```python
line_number: int = 0
text: str = ''
message: str = ''
```

### `Finding.render` - L46-L49

```python
render(self) -> str
```

Control points:

- L47: `if self.line_number`

### `Criterion` - L53-L58

```python
class Criterion()
```

Declared class/data-model fields:

```python
criterion_id: str
description: str
outcome: Outcome
note: str = ''
findings: list[Finding] = field(default_factory=list)
```

### `CheckResult` - L62-L126

```python
class CheckResult()
```

Declared class/data-model fields:

```python
check_id: str
title: str
severity: str
criteria: list[Criterion] = field(default_factory=list)
```

### `CheckResult.outcome` - L69-L88

```python
outcome(self) -> Outcome
```

A check is SKIPPED only when nothing was actually scored.

Control points:

- L80: `if not outcomes`
- L82: `if Outcome.FAIL in outcomes`
- L84: `if Outcome.BLOCKED in outcomes`
- L86: `if Outcome.PASS in outcomes`

### `CheckResult._count` - L90-L91

```python
_count(self, outcome: Outcome) -> int
```

Observed calls (lexical order): `sum`.

### `CheckResult.passed` - L94-L95

```python
passed(self) -> int
```

Observed calls (lexical order): `self._count`.

### `CheckResult.failed` - L98-L99

```python
failed(self) -> int
```

Observed calls (lexical order): `self._count`.

### `CheckResult.skipped` - L102-L103

```python
skipped(self) -> int
```

Observed calls (lexical order): `self._count`.

### `CheckResult.blocked` - L106-L107

```python
blocked(self) -> int
```

Observed calls (lexical order): `self._count`.

### `CheckResult.total` - L110-L111

```python
total(self) -> int
```

Observed calls (lexical order): `len`.

### `CheckResult.failures` - L114-L115

```python
failures(self) -> list[Criterion]
```

### `CheckResult.skips` - L118-L119

```python
skips(self) -> list[Criterion]
```

### `CheckResult.note` - L122-L126

```python
note(self) -> str
```

Control points:

- L123: `for c in self.criteria`
- L124: `if c.note`

### `ReviewResult` - L130-L188

```python
class ReviewResult()
```

Declared class/data-model fields:

```python
program_name: str = ''
program_kind: str = ''
source_file: str = ''
reviewed_at: datetime = field(default_factory=datetime.now)
checks: list[CheckResult] = field(default_factory=list)
```

### `ReviewResult._by` - L138-L139

```python
_by(self, outcome: Outcome) -> list[CheckResult]
```

### `ReviewResult.total` - L142-L143

```python
total(self) -> int
```

Observed calls (lexical order): `len`.

### `ReviewResult.passed` - L146-L147

```python
passed(self) -> int
```

Observed calls (lexical order): `len`, `self._by`.

### `ReviewResult.failed` - L150-L151

```python
failed(self) -> int
```

Observed calls (lexical order): `len`, `self._by`.

### `ReviewResult.skipped` - L154-L155

```python
skipped(self) -> int
```

Observed calls (lexical order): `len`, `self._by`.

### `ReviewResult.blocked` - L158-L159

```python
blocked(self) -> int
```

Observed calls (lexical order): `len`, `self._by`.

### `ReviewResult.failed_checks` - L162-L163

```python
failed_checks(self) -> list[CheckResult]
```

Observed calls (lexical order): `self._by`.

### `ReviewResult.failed_at` - L165-L167

```python
failed_at(self, severity: str) -> list[CheckResult]
```

Observed calls (lexical order): `str`, `str(severity or '').upper`, `c.severity.upper`.

### `ReviewResult.criteria_passed` - L171-L172

```python
criteria_passed(self) -> int
```

Observed calls (lexical order): `sum`.

### `ReviewResult.criteria_failed` - L175-L176

```python
criteria_failed(self) -> int
```

Observed calls (lexical order): `sum`.

### `ReviewResult.criteria_skipped` - L179-L180

```python
criteria_skipped(self) -> int
```

Observed calls (lexical order): `sum`.

### `ReviewResult.criteria_blocked` - L183-L184

```python
criteria_blocked(self) -> int
```

Observed calls (lexical order): `sum`.

### `ReviewResult.criteria_total` - L187-L188

```python
criteria_total(self) -> int
```

Observed calls (lexical order): `sum`.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
