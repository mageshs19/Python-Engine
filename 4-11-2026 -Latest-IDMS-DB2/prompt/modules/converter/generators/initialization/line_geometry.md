# `converter/generators/initialization/line_geometry.py`

Source: [converter/generators/initialization/line_geometry.py](../../../../../converter/generators/initialization/line_geometry.py) | 110 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `914659b17a697caa57e82839abf8fe9e0b21716b2b00511505d981cea8913af5`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`__all__` (L110)

## Import declarations

```python
from __future__ import annotations
from typing import List
from rules.initialization_placement_rules import BODY_END, BODY_START, COMMENT_INDICATORS, LINE_WIDTH, SEQUENCE_WIDTH, STATEMENT_INDENT, ACTIVE_INDICATORS
```

## Local dependency notes

- [rules/initialization_placement_rules.py](../../../rules/initialization_placement_rules.md)

## Importers (20)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/analyzers/lr_access/lrf_key_binding_planner.py](../../analyzers/lr_access/lrf_key_binding_planner.md)
- [converter/composers/lrf_group_move_decomposer.py](../../composers/lrf_group_move_decomposer.md)
- [converter/composers/lrf_key_binding_composer.py](../../composers/lrf_key_binding_composer.md)
- [converter/generators/converter_pipeline_integration.py](../converter_pipeline_integration.md)
- [converter/generators/enhancement/output_validator.py](../enhancement/output_validator.md)
- [converter/generators/initialization/__init__.py](__init__.md)
- [converter/generators/initialization/cursor_scope_scanner.py](cursor_scope_scanner.md)
- [converter/generators/initialization/initialize_placer.py](initialize_placer.md)
- [converter/generators/initialization/initialize_remover.py](initialize_remover.md)
- [converter/generators/initialization/legacy_paragraph_remover.py](legacy_paragraph_remover.md)
- [converter/generators/initialization/paragraph_index.py](paragraph_index.md)
- [converter/generators/initialization/population_site_scanner.py](population_site_scanner.md)
- [tests/initialization_scope/conftest.py](../../../tests/initialization_scope/conftest.md)
- 7 further importers are recorded in [the source manifest](../../../../source_manifest.json).

## Symbol contracts and control points

### `LineGeometry` - L16-L107

```python
class LineGeometry()
```

### `LineGeometry.split` - L19-L25

```python
split(text: str) -> List[str]
```

Observed calls (lexical order): `str`, `str(text or '').replace`, `str(text or '').replace('\r\n', '\n').replace`, `str(text or '').replace('\r\n', '\n').replace('\r', '\n').split`.

### `LineGeometry.join` - L28-L29

```python
join(lines: List[str]) -> str
```

Observed calls (lexical order): `'\n'.join`.

### `LineGeometry.is_fixed` - L32-L36

```python
is_fixed(line: str) -> bool
```

Observed calls (lexical order): `str`, `len`, `text[:SEQUENCE_WIDTH].isdigit`.

Control points:

- L34: `if len(text) <= BODY_START`

### `LineGeometry.body` - L39-L45

```python
body(cls, line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `cls.is_fixed`, `text[BODY_START:BODY_END].strip`, `text.strip`.

Control points:

- L41: `if not text`
- L43: `if cls.is_fixed(text)`

### `LineGeometry.indicator` - L48-L55

```python
indicator(cls, line: str) -> str
```

Observed calls (lexical order): `str`, `cls.is_fixed`, `text.lstrip`.

Control points:

- L50: `if cls.is_fixed(text)`
- L53: `if stripped[:1] in COMMENT_INDICATORS`

### `LineGeometry.is_comment` - L58-L59

```python
is_comment(cls, line: str) -> bool
```

Observed calls (lexical order): `cls.indicator`.

### `LineGeometry.is_comment_or_blank` - L62-L65

```python
is_comment_or_blank(cls, line: str) -> bool
```

Observed calls (lexical order): `cls.is_comment`, `cls.body`.

Control points:

- L63: `if cls.is_comment(line)`

### `LineGeometry.indent_of` - L68-L76

```python
indent_of(cls, line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `cls.is_fixed`, `region.lstrip`, `len`.

Control points:

- L70: `if cls.is_fixed(text)`

### `LineGeometry.statement` - L79-L80

```python
statement(cls, body: str, indent: str=STATEMENT_INDENT) -> str
```

Observed calls (lexical order): `str`, `str(body or '').strip`.

### `LineGeometry.replace_body` - L83-L95

```python
replace_body(cls, line: str, body: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `str(body or '').strip`, `cls.is_fixed`, `cls.indent_of`, `cls.statement`, `f'{cls.indent_of(text)}{clean}'[:width].ljust`.

Control points:

- L86: `if not cls.is_fixed(text)`
- L90: `if mark not in ACTIVE_INDICATORS`

### `LineGeometry.logical_bodies` - L98-L103

```python
logical_bodies(cls, lines: List[str]) -> List[str]
```

Observed calls (lexical order): `cls.body`, `cls.is_comment_or_blank`.

### `LineGeometry.logical_text` - L106-L107

```python
logical_text(cls, lines: List[str]) -> str
```

Observed calls (lexical order): `'\n'.join`, `'\n'.join(cls.logical_bodies(lines)).upper`, `cls.logical_bodies`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
