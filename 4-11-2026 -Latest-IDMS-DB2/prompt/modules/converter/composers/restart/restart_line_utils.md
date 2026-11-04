# `converter/composers/restart/restart_line_utils.py`

Source: [converter/composers/restart/restart_line_utils.py](../../../../../converter/composers/restart/restart_line_utils.py) | 143 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `6bebcb2efa2db5e7d02e66eca623e79f1dd7ee3475d1ddb50d19c692197be711`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> The line utility the restart package passes to its collaborators.

## Module-level bindings

`COMMENT_MARKERS` (L55), `INDICATOR_MARKERS` (L56), `SEQUENCE_WIDTH` (L57), `REQUIRED_METHODS` (L58), `__all__` (L137)

## Import declarations

```python
from __future__ import annotations
from converter.services.fixed_format_line_service import FixedFormatLineService
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](../../services/fixed_format_line_service.md)

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/restart/process_paragraph_injector.py](process_paragraph_injector.md)
- [converter/composers/restart/restart_storage_injector.py](restart_storage_injector.md)
- [converter/pipeline/conversion/conversion_component_factory.py](../../pipeline/conversion/conversion_component_factory.md)
- [tests/restart/test_m10d_line_utils.py](../../../tests/restart/test_m10d_line_utils.md)

## Symbol contracts and control points

### `RestartLineUtils` - L61-L134

```python
class RestartLineUtils()
```

Adapts the shared fixed-format service to the restart contract.

### `RestartLineUtils.__init__` - L64-L66

```python
__init__(self, fixed_format=None) -> None
```

Observed calls (lexical order): `FixedFormatLineService`, `self._verify`.

### `RestartLineUtils.logical` - L71-L74

```python
logical(self, line: str) -> str
```

Body of a code line; "" for a comment, control or stray line.

Observed calls (lexical order): `self._body`, `self._is_sequence_only`.

### `RestartLineUtils.is_comment` - L77-L79

```python
is_comment(text: str) -> bool
```

True when ALREADY-LOGICAL text carries its own marker.

Observed calls (lexical order): `str`, `str(text or '').lstrip`, `str(text or '').lstrip().startswith`.

### `RestartLineUtils.lines` - L85-L86

```python
lines(text: str) -> list[str]
```

Observed calls (lexical order): `str`, `str(text or '').splitlines`.

### `RestartLineUtils.join` - L89-L90

```python
join(lines) -> str
```

Observed calls (lexical order): `'\n'.join`, `str`.

### `RestartLineUtils._body` - L95-L102

```python
_body(self, line: str) -> str
```

Observed calls (lexical order): `self.fixed_format.is_comment_or_control_line`, `self.fixed_format.logical`, `str`, `str(self.fixed_format.logical(line) or '').strip`, `str(line or '').strip`, `text.startswith`.

Control points:

- L97: `if self.fixed_format.is_comment_or_control_line(line)`

### `RestartLineUtils._is_sequence_only` - L105-L118

```python
_is_sequence_only(body: str) -> bool
```

A body that is only a sequence area is not COBOL.

Observed calls (lexical order): `str`, `str(body or '').strip`, `candidate.endswith`, `candidate.strip`, `candidate.isdigit`, `len`.

Control points:

- L113: `if candidate.endswith('.')`
- L115: `if candidate[-1:] in INDICATOR_MARKERS`

### `RestartLineUtils._verify` - L124-L134

```python
_verify(fixed_format) -> None
```

Observed calls (lexical order): `callable`, `getattr`, `TypeError`, `type`.

Control points:

- L130: `if missing`

Explicit raises: `TypeError(f'RestartLineUtils needs a fixed-format service exposing {missing}; got {type(fixed_format).__name__}.')`.

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
