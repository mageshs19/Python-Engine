# `converter/composers/fixed_format_sequence_stripper.py`

Source: [converter/composers/fixed_format_sequence_stripper.py](../../../../converter/composers/fixed_format_sequence_stripper.py) | 112 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `b3a06c353b60be7434a60f556c7afbf978913ec4ca7c0da709ae5eb1ec8a4394`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from patterns.fixed_format_patterns import COBOL_IDENTIFIER_TOKEN_PATTERN, RIGHT_SEQUENCE_WITH_SPACES_PATTERN, TRAILING_TIGHT_RIGHT_SEQUENCE_PATTERN, TRUE_LEFT_SEQUENCE_PATTERN
from rules.fixed_format_rules import COBOL_STATEMENT_STARTERS, RIGHT_SEQUENCE_GENERATED_PREFIX, TOTAL_WIDTH
```

## Local dependency notes

- [patterns/fixed_format_patterns.py](../../patterns/fixed_format_patterns.md)
- [rules/fixed_format_rules.py](../../rules/fixed_format_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/fixed_format_line_parser.py](fixed_format_line_parser.md)

## Symbol contracts and control points

### `FixedFormatSequenceStripper` - L16-L112

```python
class FixedFormatSequenceStripper()
```

Strips loose left/right sequence numbers from non-fixed COBOL lines.

### `FixedFormatSequenceStripper.remove_loose_sequence_numbers` - L23-L27

```python
remove_loose_sequence_numbers(self, line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `self.remove_loose_right_sequence`, `self.remove_loose_left_sequence`, `text.rstrip`.

### `FixedFormatSequenceStripper.remove_loose_left_sequence` - L29-L39

```python
remove_loose_left_sequence(self, line: str) -> str
```

Observed calls (lexical order): `str`, `TRUE_LEFT_SEQUENCE_PATTERN.match`, `match.group`, `left.isdigit`, `len`, `body.lstrip`.

Control points:

- L32: `if not match`
- L37: `if not left.isdigit() or len(left) != 6`

### `FixedFormatSequenceStripper.remove_loose_right_sequence` - L41-L63

```python
remove_loose_right_sequence(self, line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `RIGHT_SEQUENCE_WITH_SPACES_PATTERN.match`, `spaced.group`, `str(spaced.group('body') or '').rstrip`, `self._looks_like_spaced_right_sequence`, `TRAILING_TIGHT_RIGHT_SEQUENCE_PATTERN.match`, `str(tight.group('body') or '').rstrip`, `tight.group`, `self._looks_like_tight_right_sequence`.

Control points:

- L45: `if spaced`
- L49: `if self._looks_like_spaced_right_sequence(body=body, spaces=spaces, right=right, original=text)`
- L55: `if tight`
- L58: `if self._looks_like_tight_right_sequence(body=body, right=right, original=text)`

### `FixedFormatSequenceStripper._looks_like_spaced_right_sequence` - L65-L76

```python
_looks_like_spaced_right_sequence(self, body: str, spaces: str, right: str, original: str) -> bool
```

Observed calls (lexical order): `self._is_eight_digit_sequence`, `len`.

Control points:

- L68: `if not self._is_eight_digit_sequence(right)`
- L70: `if not body`
- L72: `if len(original) >= TOTAL_WIDTH`
- L74: `if len(spaces) >= 2`

### `FixedFormatSequenceStripper._looks_like_tight_right_sequence` - L78-L97

```python
_looks_like_tight_right_sequence(self, body: str, right: str, original: str) -> bool
```

Observed calls (lexical order): `self._is_eight_digit_sequence`, `len`, `original[72:80].isdigit`, `body.strip`, `body.strip().upper`, `body_upper.startswith`, `right.startswith`, `self._body_ends_like_cobol_identifier`.

Control points:

- L81: `if not self._is_eight_digit_sequence(right)`
- L83: `if not body`
- L85: `if len(original) >= TOTAL_WIDTH and original[72:80].isdigit()`
- L89: `if not body_upper`
- L91: `if body_upper.startswith(COBOL_STATEMENT_STARTERS)`
- L93: `if right.startswith(RIGHT_SEQUENCE_GENERATED_PREFIX) and self._body_ends_like_cobol_identifier(body)`

### `FixedFormatSequenceStripper._is_eight_digit_sequence` - L99-L101

```python
_is_eight_digit_sequence(self, value: str) -> bool
```

Observed calls (lexical order): `str`, `len`, `text.isdigit`.

### `FixedFormatSequenceStripper._body_ends_like_cobol_identifier` - L103-L112

```python
_body_ends_like_cobol_identifier(self, body: str) -> bool
```

Observed calls (lexical order): `str`, `str(body or '').rstrip`, `text[-1].isdigit`, `text.split`, `COBOL_IDENTIFIER_TOKEN_PATTERN.fullmatch`, `bool`.

Control points:

- L105: `if not text`
- L107: `if text[-1].isdigit()`
- L109: `if text[-1] in {"'", '"'}`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
