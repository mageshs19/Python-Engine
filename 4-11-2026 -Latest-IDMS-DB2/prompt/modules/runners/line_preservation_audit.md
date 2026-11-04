# `runners/line_preservation_audit.py`

Source: [runners/line_preservation_audit.py](../../../runners/line_preservation_audit.py) | 284 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `7cc85535331c4f3d21702df0a0e7354c7fa46c9bc8861d3ea15c2ff77911bfaa`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Line-preservation audit tool.

## Module-level bindings

`CURRENT_FILE` (L39), `SRC_DIR` (L40), `PROJECT_ROOT` (L41), `_CONVERTIBLE_PATTERNS` (L108), `_QUALIFIED_REF_PATTERN` (L148)

## Import declarations

```python
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path
```

## Symbol contracts and control points

### `_strip_sequence_area` - L49-L74

```python
_strip_sequence_area(line: str) -> str
```

Return the COBOL body (columns 8-72 area), handling fixed-format: - cols 1-6 : sequence number - col 7 : indicator (* / D) - cols 8-72 : body - cols 73-80: right sequence

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `str(line or '').rstrip('\n').rstrip`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`, `text[7:72].strip`, `body[-8:].strip`, `body[-8:].strip().isdigit`, `body.strip`, `text.strip`.

Control points:

- L60: `if len(text) >= 72 and text[:6].strip().isdigit()`
- L64: `if len(text) > 6 and text[:6].strip().isdigit()`
- L67: `if len(body) >= 8 and body[-8:].strip().isdigit()`
- L70: `if body[:1] in ('*', '/', 'D')`

### `_indicator` - L77-L82

```python
_indicator(line: str) -> str
```

Return the column-7 indicator char, or '' if not fixed-format.

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`.

Control points:

- L80: `if len(text) >= 7 and text[:6].strip().isdigit()`

### `_is_comment_or_blank` - L85-L94

```python
_is_comment_or_blank(line: str) -> bool
```

Observed calls (lexical order): `_indicator`, `_strip_sequence_area`, `body.startswith`.

Control points:

- L87: `if ind in ('*', '/')`
- L90: `if not body`
- L92: `if body.startswith('*') or body.startswith('/')`

### `_norm` - L97-L103

```python
_norm(body: str) -> str
```

Collapse internal whitespace and drop a trailing period so that re-indentation and period differences are not treated as changes.

Observed calls (lexical order): `re.sub`, `re.sub('\\s+', ' ', str(body or '').strip()).upper`, `str`, `str(body or '').strip`, `text.rstrip`.

### `_is_convertible` - L154-L163

```python
_is_convertible(body: str) -> bool
```

Observed calls (lexical order): `pattern.search`, `_QUALIFIED_REF_PATTERN.search`, `body.upper`.

Control points:

- L155: `for pattern in _CONVERTIBLE_PATTERNS`
- L156: `if pattern.search(body)`
- L159: `if match`
- L161: `if ' OF DCL' not in upper and ' IN DCL' not in upper`

### `audit` - L166-L202

```python
audit(input_text: str, output_text: str) -> dict
```

Observed calls (lexical order): `input_text.splitlines`, `_norm`, `_strip_sequence_area`, `output_text.splitlines`, `_is_comment_or_blank`, `enumerate`, `_is_convertible`, `convertible.append`, `preserved_ok.append`, `preserved_missing.append`, `len`.

Control points:

- L179: `for (index, raw) in enumerate(input_lines, start=1)`
- L180: `if _is_comment_or_blank(raw)`
- L186: `if _is_convertible(body)`
- L190: `if _norm(body) in output_bodies`

### `print_report` - L205-L244

```python
print_report(report: dict, verbose: bool=False) -> None
```

Observed calls (lexical order): `print`, `len`.

Control points:

- L226: `if report['preserved_missing']`
- L229: `for (line_number, body) in report['preserved_missing']`
- L236: `if verbose`
- L239: `for (line_number, body) in report['convertible']`

### `main` - L247-L280

```python
main() -> None
```

Observed calls (lexical order): `argparse.ArgumentParser`, `parser.add_argument`, `parser.parse_args`, `Path`, `Path(args.input).read_text`, `Path(args.output).read_text`, `audit`, `print_report`, `sys.exit`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
