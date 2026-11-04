# `converter/composers/program_identity_initializer.py`

Source: [converter/composers/program_identity_initializer.py](../../../../converter/composers/program_identity_initializer.py) | 75 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `00231d1e9347ecb2c7caf3db691f9c8560776accd330700f9390c407706f69e2`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Initialize SQL diagnostic identity at procedure entry, without naming business paragraphs.

## Import declarations

```python
from __future__ import annotations
import re
from converter.services.fixed_format_line_service import FixedFormatLineService
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](../services/fixed_format_line_service.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/services/final_generated_output_service.py](../services/final_generated_output_service.md)
- [tests/test_full_program_representation_audit.py](../../tests/test_full_program_representation_audit.md)

## Symbol contracts and control points

### `_body` - L12-L19

```python
_body(raw: str) -> str
```

Observed calls (lexical order): `len`, `raw[:6].isdigit`, `raw[:7].isspace`, `raw.lstrip`, `raw.lstrip().startswith`, `re.split`, `re.split('\\*>', raw, maxsplit=1)[0].strip`.

Control points:

- L13: `if len(raw) >= 7 and (raw[:6].isdigit() or raw[:7].isspace())`
- L14: `if raw[6] in '*/Dd'`
- L17: `if raw.lstrip().startswith(('*', '/'))`

### `ProgramIdentityInitializer` - L22-L75

```python
class ProgramIdentityInitializer()
```

### `ProgramIdentityInitializer.__init__` - L23-L24

```python
__init__(self) -> None
```

### `ProgramIdentityInitializer.compose` - L26-L75

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `text.splitlines`, `_body`, `enumerate`, `next`, `re.match`, `' '.join`, `re.search`, `constant.group`, `constant.group(1).upper`, `program.group`, `program.group(1).upper`, `re.sub`, `bodies[procedure].endswith`, `self.messages.append`, `len`, `re.fullmatch`.
Another 8 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L32: `if procedure is None`
- L39: `if not (program and constant and (program.group(1).upper() == constant.group(1).upper()) and re.search('\\bEXEC\\s+SQL\\s+INCLUDE\\s+SQLERRWS\\s+END-EXEC\\b', data, re.I))`
- L46: `if re.search('\\bTO\\s+PROGRAM-NAME\\b', masked, re.I)`
- L50: `if not bodies[procedure].endswith('.') or re.search('\\bDECLARATIVES\\b', masked, re.I)`
- L54: `while insertion < len(lines) and (not bodies[insertion])`
- L57: `while insertion < len(lines)`
- L59: `if re.fullmatch('[A-Z0-9][A-Z0-9-]*(?:\\s+SECTION)?\\.', b, re.I)`
- L60: `if b.upper() in {'GOBACK.', 'EXIT.', 'CONTINUE.'}`
- Another 2 conditions/loops exist in this source span.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
