# `converter/composers/fixed_format_sequence_manager.py`

Source: [converter/composers/fixed_format_sequence_manager.py](../../../../converter/composers/fixed_format_sequence_manager.py) | 313 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `d872766cd647538b71d22d97a84faebb36fe2a93c1540d243f03bb1beaf91c98`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Fixed-format COBOL sequence manager.

## Import declarations

```python
from __future__ import annotations
import re
from dataclasses import dataclass
from patterns.fixed_format_patterns import LEFT_SEQUENCE_PATTERN, RIGHT_SEQUENCE_PATTERN
from rules.fixed_format_rules import DEFAULT_LEFT_START, DEFAULT_LEFT_STEP, DEFAULT_RIGHT_START, DEFAULT_RIGHT_STEP, TOTAL_WIDTH
```

## Local dependency notes

- [patterns/fixed_format_patterns.py](../../patterns/fixed_format_patterns.md)
- [rules/fixed_format_rules.py](../../rules/fixed_format_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/fixed_format_composer.py](fixed_format_composer.md)

## Symbol contracts and control points

### `FixedFormatSequenceState` - L51-L71

```python
class FixedFormatSequenceState()
```

Declared class/data-model fields:

```python
left_current: int
left_step: int
right_current: int
right_step: int
```

### `FixedFormatSequenceState.current_left` - L57-L60

```python
current_left(self) -> str
```

### `FixedFormatSequenceState.current_right` - L62-L65

```python
current_right(self) -> str
```

### `FixedFormatSequenceState.advance` - L67-L71

```python
advance(self) -> None
```

### `FixedFormatSequenceManager` - L74-L313

```python
class FixedFormatSequenceManager()
```

Generic sequence manager.

Declared class/data-model fields:

```python
MIN_MANUAL_RIGHT_SEQUENCE = 10000
MIN_MANUAL_RIGHT_STEP = 10000
```

### `FixedFormatSequenceManager.create_state` - L93-L140

```python
create_state(self, lines: list[str], left_start: int | None=None, left_step: int | None=None, right_start: int | None=None, right_step: int | None=None) -> FixedFormatSequenceState
```

Observed calls (lexical order): `self._left_sequence_values`, `self._right_sequence_values`, `self._first_positive`, `self._detect_manual_right_start`, `FixedFormatSequenceState`.

### `FixedFormatSequenceManager._left_sequence_values` - L142-L163

```python
_left_sequence_values(self, lines: list[str]) -> list[int]
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[:6].isdigit`, `int`, `values.append`, `LEFT_SEQUENCE_PATTERN.match`, `match.group`, `left.isdigit`.

Control points:

- L148: `for line in lines`
- L151: `if len(text) >= TOTAL_WIDTH and text[:6].isdigit()`
- L157: `if match`
- L160: `if left.isdigit()`

### `FixedFormatSequenceManager._right_sequence_values` - L165-L186

```python
_right_sequence_values(self, lines: list[str]) -> list[int]
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[72:80].isdigit`, `int`, `values.append`, `RIGHT_SEQUENCE_PATTERN.match`, `match.group`, `right.isdigit`.

Control points:

- L171: `for line in lines`
- L174: `if len(text) >= TOTAL_WIDTH and text[72:80].isdigit()`
- L180: `if match`
- L183: `if right.isdigit()`

### `FixedFormatSequenceManager._first_positive` - L188-L197

```python
_first_positive(self, values: list[int], default_value: int) -> int
```

Control points:

- L193: `for value in values`
- L194: `if value > 0`

### `FixedFormatSequenceManager._detect_step` - L199-L212

```python
_detect_step(self, values: list[int], default_step: int) -> int
```

Observed calls (lexical order): `self._positive_differences`, `self._most_common_difference`.

Control points:

- L206: `if not differences`

### `FixedFormatSequenceManager._detect_manual_right_start` - L214-L256

```python
_detect_manual_right_start(self, values: list[int]) -> int
```

Detect manual right sequence start value with validation.

Observed calls (lexical order): `len`, `self._positive_differences`, `min`, `max`.

Control points:

- L231: `if not manual_values`
- L241: `if first_value > 100000 or first_value % 10000 != 0`
- L246: `if len(manual_values) > 1`
- L248: `if differences`
- L253: `if max_diff > min_diff * 2`

### `FixedFormatSequenceManager._detect_manual_right_step` - L258-L281

```python
_detect_manual_right_step(self, values: list[int]) -> int
```

Observed calls (lexical order): `self._positive_differences`, `self._most_common_difference`.

Control points:

- L270: `if not differences`
- L278: `if step < self.MIN_MANUAL_RIGHT_STEP`

### `FixedFormatSequenceManager._positive_differences` - L283-L295

```python
_positive_differences(self, values: list[int]) -> list[int]
```

Observed calls (lexical order): `len`, `range`, `differences.append`.

Control points:

- L289: `for index in range(1, len(values))`
- L292: `if difference > 0`

### `FixedFormatSequenceManager._most_common_difference` - L297-L313

```python
_most_common_difference(self, differences: list[int], default_step: int) -> int
```

Observed calls (lexical order): `counts.get`, `sorted`, `counts.items`.

Control points:

- L302: `if not differences`
- L307: `for difference in differences`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
