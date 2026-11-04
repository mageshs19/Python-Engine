# `converter/composers/record_materialisation/record_entry_renderer.py`

Source: [converter/composers/record_materialisation/record_entry_renderer.py](../../../../../converter/composers/record_materialisation/record_entry_renderer.py) | 236 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `8cd0eed131ff0ed9cc657d425cbeeea144c8240f1bf5f8f8ef8e0deb41d1cd91`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Renders a group entry and an elementary entry.

## Module-level bindings

`__all__` (L236)

## Import declarations

```python
from __future__ import annotations
from converter.composers.record_materialisation.record_layout_geometry import RecordLayoutGeometry
from rules.record_materialisation_rules import ELEMENTARY_ITEM_TEMPLATE, GROUP_ITEM_TEMPLATE
```

## Local dependency notes

- [converter/composers/record_materialisation/record_layout_geometry.py](record_layout_geometry.md)
- [rules/record_materialisation_rules.py](../../../rules/record_materialisation_rules.md)

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/record_materialisation/record_layout_generator.py](record_layout_generator.md)
- [tests/generated_fields/test_db2_code_fixes.py](../../../tests/generated_fields/test_db2_code_fixes.md)
- [tests/generated_fields/test_record_comp3_preservation.py](../../../tests/generated_fields/test_record_comp3_preservation.md)
- [tests/test_db2_code_fixes.py](../../../tests/test_db2_code_fixes.md)

## Symbol contracts and control points

### `RecordEntryRenderer` - L106-L233

```python
class RecordEntryRenderer()
```

One data description entry, group or elementary.

### `RecordEntryRenderer.__init__` - L109-L110

```python
__init__(self, geometry: RecordLayoutGeometry | None=None) -> None
```

Observed calls (lexical order): `RecordLayoutGeometry`.

### `RecordEntryRenderer.group` - L113-L121

```python
group(self, *, level: str, name: str, indent: str) -> str
```

`06 VMBFAS.`

Observed calls (lexical order): `GROUP_ITEM_TEMPLATE.format`, `self.clean_name`, `self.geometry.cap`, `self.geometry.terminate`.

### `RecordEntryRenderer.elementary` - L124-L157

```python
elementary(self, *, level: str, name: str, picture: str, indent: str) -> str
```

`07 CT-RK-TGDSV PIC X(4).`

Observed calls (lexical order): `str`, `str(picture or '').strip`, `self.clean_name`, `self.group`, `self.geometry.name_width`, `ELEMENTARY_ITEM_TEMPLATE.format`, `self.geometry.cap`, `self.geometry.terminate`.

Control points:

- L140: `if not clean_picture`

### `RecordEntryRenderer.picture_of` - L161-L193

```python
picture_of(item) -> str
```

'PIC S9(13)V99' + 'COMP-3' -> 'PIC S9(13)V99 VALUE ZEROES'.

Observed calls (lexical order): `getattr`, `str`, `usage.strip`, `usage.strip().upper`, `f'{picture} {usage}'.strip`, `picture.strip`, `RecordEntryRenderer._is_redefinition`, `any`, `result.upper`.

Control points:

- L178: `if usage and usage.strip().upper() not in excluded_usage`
- L185: `if RecordEntryRenderer._is_redefinition(item)`
- L189: `if result and 'PIC' in result and ('VALUE' not in result)`
- L190: `if any((pic in result.upper() for pic in ['PIC 9', 'PIC S9']))`

### `RecordEntryRenderer.record_picture_of` - L196-L209

```python
record_picture_of(item) -> str
```

Return a record field's original PIC and USAGE without rewriting it.

Observed calls (lexical order): `getattr`, `str`, `str(getattr(item, 'picture', '') or '').strip`, `str(getattr(item, 'usage', '') or '').strip`, `picture.upper`, `usage.upper`, `f'{picture} {usage}'.strip`.

Control points:

- L205: `if not picture`
- L207: `if not usage or usage.upper() in picture.upper()`

### `RecordEntryRenderer._is_redefinition` - L212-L229

```python
_is_redefinition(item) -> bool
```

True only on EVIDENCE, never on a duck-typed truthy value.

Observed calls (lexical order): `getattr`, `isinstance`, `bool`, `redefines.strip`.

Control points:

- L223: `if isinstance(flag, bool)`
- L227: `if not isinstance(redefines, str)`

### `RecordEntryRenderer.clean_name` - L232-L233

```python
clean_name(name: str) -> str
```

Observed calls (lexical order): `str`, `str(name or '').strip`, `str(name or '').strip().upper`.

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
