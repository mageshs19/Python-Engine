# `converter/generators/select_paragraph_generator.py`

Source: [converter/generators/select_paragraph_generator.py](../../../../converter/generators/select_paragraph_generator.py) | 246 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `63f093ebf38dde549dd25756f184168dcd3d67a1b78bef0951e052b66202186e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> The legacy restart path, retired to a reporting role.

## Module-level bindings

`_OWNER_ROLE_KEY` (L75), `__all__` (L246)

## Import declarations

```python
from __future__ import annotations
from typing import Any, Optional
from patterns.sequence_patterns import is_fixed_format_line, logical_body
from rules.legacy_restart_rules import ENABLE_LEGACY_RESTART_GENERATOR, LEGACY_HANDLER_NUMBER_PREFIXES, LEGACY_RESTART_MESSAGES, REPORT_DANGLING_PERFORM, REPORT_LEGACY_RESIDUE, STAND_DOWN_REASONS
from rules.restart_standard_rules import RESTART_PARAGRAPH_NAMES
```

## Local dependency notes

- [patterns/sequence_patterns.py](../../patterns/sequence_patterns.md)
- [rules/legacy_restart_rules.py](../../rules/legacy_restart_rules.md)
- [rules/restart_standard_rules.py](../../rules/restart_standard_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)

## Symbol contracts and control points

### `SelectParagraphGenerator` - L78-L243

```python
class SelectParagraphGenerator()
```

Reports on legacy restart residue. Generates nothing.

### `SelectParagraphGenerator.__init__` - L81-L83

```python
__init__(self, line_utils: Any=None) -> None
```

### `SelectParagraphGenerator.apply` - L88-L113

```python
apply(self, cobol_text: str, program_id: Optional[str]=None, operations: list | None=None, *, is_update: Optional[bool]=None, restart_context: Any=None) -> tuple[str, list[str]]
```

Observed calls (lexical order): `str`, `text.strip`, `self._stood_down`, `self._say`, `self._decide`, `self._report_residue`.

Control points:

- L100: `if not text.strip()`
- L104: `if ENABLE_LEGACY_RESTART_GENERATOR`
- L109: `if REPORT_LEGACY_RESIDUE`

### `SelectParagraphGenerator._decide` - L118-L142

```python
_decide(self, text: str, is_update: Optional[bool], restart_context: Any) -> None
```

Observed calls (lexical order): `self._context_is_update`, `self._stood_down`, `self._owner_paragraph`.

Control points:

- L124: `if restart_context is not None`
- L125: `if not self._context_is_update(restart_context)`
- L132: `if owner_paragraph`
- L138: `if is_update is False`

### `SelectParagraphGenerator._context_is_update` - L145-L150

```python
_context_is_update(context: Any) -> bool
```

RestartRunContext exposes is_update. Duck-typed on purpose.

Observed calls (lexical order): `getattr`, `bool`.

Control points:

- L148: `if value is None`

### `SelectParagraphGenerator._owner_paragraph` - L152-L171

```python
_owner_paragraph(self, text: str) -> str
```

The first seven-series handler the owner pass would inject.

Observed calls (lexical order): `str`, `str(RESTART_PARAGRAPH_NAMES.get(_OWNER_ROLE_KEY, '')).strip`, `str(RESTART_PARAGRAPH_NAMES.get(_OWNER_ROLE_KEY, '')).strip().upper`, `RESTART_PARAGRAPH_NAMES.get`, `self._logical_lines`.

Control points:

- L164: `if not wanted`
- L168: `for line in self._logical_lines(text)`
- L169: `if line == header`

### `SelectParagraphGenerator._report_residue` - L176-L206

```python
_report_residue(self, text: str) -> None
```

Observed calls (lexical order): `self._logical_lines`, `set`, `line.endswith`, `defined.add`, `line.startswith`, `line.split`, `line.split()[1].rstrip`, `performed.get`, `sorted`, `name.startswith`, `self._say`, `len`.

Control points:

- L182: `for line in lines`
- L183: `if line.endswith('.') and ' ' not in line[:-1]`
- L185: `if line.startswith('PERFORM ')`
- L195: `if not residue`
- L201: `if not REPORT_DANGLING_PERFORM`
- L204: `for name in residue`
- L205: `if name in performed and name not in defined`

### `SelectParagraphGenerator._logical_lines` - L212-L223

```python
_logical_lines(text: str) -> list[str]
```

Observed calls (lexical order): `str`, `str(text or '').replace`, `str(text or '').replace('\r\n', '\n').replace`, `raw.split`, `logical_body`, `is_fixed_format_line`, `line.strip`, `' '.join`, `body.upper`, `body.upper().split`, `out.append`.

Control points:

- L215: `for line in raw.split('\n')`
- L221: `if body`

### `SelectParagraphGenerator._stood_down` - L228-L234

```python
_stood_down(self, key: str, **values: Any) -> None
```

Observed calls (lexical order): `STAND_DOWN_REASONS.get`, `reason.format`, `self._say`.

### `SelectParagraphGenerator._say` - L236-L243

```python
_say(self, key: str, **values: Any) -> None
```

Observed calls (lexical order): `LEGACY_RESTART_MESSAGES.get`, `self.messages.append`, `template.format`.

Control points:

- L238: `if not template`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
