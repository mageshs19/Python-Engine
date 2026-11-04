# `converter/composers/record_materialisation/record_redefines_renderer.py`

Source: [converter/composers/record_materialisation/record_redefines_renderer.py](../../../../../converter/composers/record_materialisation/record_redefines_renderer.py) | 141 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `6df4aa4e79f7c4406d050a0a23f9bcb9a6c16655d9a87c8b2203ca065ebd14bc`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Renders a REDEFINES entry, on one line or two.

## Module-level bindings

`REDEFINES_KEYWORD` (L40), `__all__` (L141)

## Import declarations

```python
from __future__ import annotations
from converter.composers.record_materialisation.record_layout_geometry import RecordLayoutGeometry
from rules.record_materialisation_rules import LAYOUT_MIN_NAME_GAP, REDEFINES_CONTINUATION_GAP, REDEFINES_HEAD_TEMPLATE, REDEFINES_INLINE_LIMIT, REDEFINES_TEMPLATE, WRAP_REDEFINES_ENTRY
```

## Local dependency notes

- [converter/composers/record_materialisation/record_layout_geometry.py](record_layout_geometry.md)
- [rules/record_materialisation_rules.py](../../../rules/record_materialisation_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/record_materialisation/record_layout_generator.py](record_layout_generator.md)

## Symbol contracts and control points

### `RecordRedefinesRenderer` - L43-L138

```python
class RecordRedefinesRenderer()
```

A REDEFINES entry. One line when it fits, two when it does not.

### `RecordRedefinesRenderer.__init__` - L46-L47

```python
__init__(self, geometry: RecordLayoutGeometry | None=None) -> None
```

Observed calls (lexical order): `RecordLayoutGeometry`.

### `RecordRedefinesRenderer.render` - L50-L86

```python
render(self, *, level: str, name: str, base: str, picture: str, indent: str) -> list[str]
```

Observed calls (lexical order): `str`, `str(picture or '').strip`, `self.geometry.cap`, `self.geometry.terminate`, `self.inline`, `len`, `self.wrapped`.

Control points:

- L61: `if not clean_picture`
- L75: `if not WRAP_REDEFINES_ENTRY`
- L77: `if len(single) <= REDEFINES_INLINE_LIMIT`

### `RecordRedefinesRenderer.inline` - L89-L109

```python
inline(self, *, level: str, name: str, base: str, picture: str, indent: str) -> str
```

CORRECTION 1. The gap before the picture is guaranteed.

Observed calls (lexical order): `self.geometry.gap_before`, `REDEFINES_TEMPLATE.format`, `self.geometry.cap`, `self.geometry.terminate`.

### `RecordRedefinesRenderer.wrapped` - L112-L138

```python
wrapped(self, *, level: str, name: str, base: str, picture: str, indent: str) -> list[str]
```

CORRECTION 5. Manual reference shape, two lines.

Observed calls (lexical order): `max`, `REDEFINES_HEAD_TEMPLATE.format`, `len`, `self.geometry.cap`, `self.geometry.terminate`.

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
