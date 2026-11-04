# `converter/generators/db2_infrastructure/spec_builder/spec_fixed_format.py`

Source: [converter/generators/db2_infrastructure/spec_builder/spec_fixed_format.py](../../../../../../converter/generators/db2_infrastructure/spec_builder/spec_fixed_format.py) | 44 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `6fbff8311eff24d069208673ba3f7272f0b97bc9e86342bc6c3b70caba0d2e94`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Extracts the body of one fixed-format source record.

## Module-level bindings

`__all__` (L44)

## Import declarations

```python
from __future__ import annotations
from rules.cursor_spec import BODY_END_INDEX, BODY_START_INDEX
```

## Local dependency notes

- [rules/cursor_spec/__init__.py](../../../../rules/cursor_spec/__init__.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure/spec_builder/spec_lrf_scanner.py](spec_lrf_scanner.md)
- [converter/generators/db2_infrastructure/spec_builder/spec_navigation_scanner.py](spec_navigation_scanner.md)

## Symbol contracts and control points

### `body_of` - L23-L32

```python
body_of(record: str) -> str
```

Columns 8-72 of a fixed-format record, stripped.

Observed calls (lexical order): `str`, `str(record or '').rstrip`, `len`, `text[BODY_START_INDEX:BODY_END_INDEX].strip`.

Control points:

- L30: `if len(text) <= BODY_START_INDEX`

### `bodies_of` - L35-L41

```python
bodies_of(cobol_text: str) -> list[str]
```

Every record of a program reduced to its body, order preserved.

Observed calls (lexical order): `body_of`, `str`, `str(cobol_text or '').split`.

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
