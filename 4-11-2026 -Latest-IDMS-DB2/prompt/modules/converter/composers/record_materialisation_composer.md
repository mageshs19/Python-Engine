# `converter/composers/record_materialisation_composer.py`

Source: [converter/composers/record_materialisation_composer.py](../../../../converter/composers/record_materialisation_composer.py) | 305 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `8e9abbc0573537109a78bccf183e4b6c64718f172361d388b0ffc453fde6dca3`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Materialises IDMS records referenced by whole-record MOVE statements.

## Module-level bindings

`DETAIL_SEPARATOR` (L77), `DETAIL_TEMPLATE` (L78), `MAX_DETAILS` (L79), `__all__` (L305)

## Import declarations

```python
from __future__ import annotations
from converter.composers.record_materialisation.record_block_writer import RecordBlockWriter
from converter.composers.record_materialisation.record_layout_generator import RecordLayoutGenerator
from converter.composers.record_materialisation.record_line_utils import RecordLineUtils
from converter.composers.record_materialisation.record_materialisation_guard import RecordMaterialisationGuard
from converter.composers.record_materialisation.record_move_generator import RecordMoveGenerator
from converter.composers.record_materialisation.record_move_scanner import RecordMoveScanner
from converter.composers.record_materialisation.record_plan_builder import RecordPlanBuilder
from converter.services.fixed_format_line_service import FixedFormatLineService
from rules.record_materialisation_rules import EMIT_TARGET_MEASUREMENT, ENFORCE_RECORD_MATERIALISATION, MAX_RECORD_MOVES, RECORD_MATERIALISATION_MESSAGES
```

## Local dependency notes

- [converter/composers/record_materialisation/record_block_writer.py](record_materialisation/record_block_writer.md)
- [converter/composers/record_materialisation/record_layout_generator.py](record_materialisation/record_layout_generator.md)
- [converter/composers/record_materialisation/record_line_utils.py](record_materialisation/record_line_utils.md)
- [converter/composers/record_materialisation/record_materialisation_guard.py](record_materialisation/record_materialisation_guard.md)
- [converter/composers/record_materialisation/record_move_generator.py](record_materialisation/record_move_generator.md)
- [converter/composers/record_materialisation/record_move_scanner.py](record_materialisation/record_move_scanner.md)
- [converter/composers/record_materialisation/record_plan_builder.py](record_materialisation/record_plan_builder.md)
- [converter/services/fixed_format_line_service.py](../services/fixed_format_line_service.md)
- [rules/record_materialisation_rules.py](../../rules/record_materialisation_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)

## Symbol contracts and control points

### `RecordMaterialisationComposer` - L82-L302

```python
class RecordMaterialisationComposer()
```

Expands every whole-record MOVE it can prove safe.

### `RecordMaterialisationComposer.__init__` - L85-L110

```python
__init__(self, *, mapping_repository, table_name_resolver, host_variable_resolver, fixed_format: FixedFormatLineService | None=None) -> None
```

Observed calls (lexical order): `RecordLineUtils`, `FixedFormatLineService`, `RecordMoveScanner`, `RecordMaterialisationGuard`, `RecordPlanBuilder`, `RecordBlockWriter`, `RecordLayoutGenerator`, `RecordMoveGenerator`.

### `RecordMaterialisationComposer.compose` - L115-L145

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text).replace`, `str(text).replace('\r\n', '\n').replace`, `set`, `range`, `current.split`, `self.scanner.find_move`, `handled.add`, `self._materialise`, `'\n'.join`, `self._report`, `current.rstrip`.

Control points:

- L119: `if not text or not ENFORCE_RECORD_MATERIALISATION`
- L127: `for _ in range(MAX_RECORD_MOVES)`
- L131: `if site is None`
- L138: `if rewritten is None`

### `RecordMaterialisationComposer._materialise` - L150-L199

```python
_materialise(self, lines: list[str], site) -> list[str] | None
```

Observed calls (lexical order): `self.guard.build_plan`, `self._refuse`, `self.scanner.find_target`, `self._refuse_key`, `self._log_key`, `self.guard.check_length`, `self.guard.check_movable`, `self._log`, `list`, `self.writer.replace_move`, `self.writer.expand_target`, `self._log_success`.

Control points:

- L152: `if refusal is not None`
- L158: `if not target.is_found`
- L168: `if EMIT_TARGET_MEASUREMENT`
- L180: `if refusal is not None`
- L185: `if advice is not None`

### `RecordMaterialisationComposer._log_success` - L204-L234

```python
_log_success(self, plan, target: str, declared_bytes: int) -> None
```

Observed calls (lexical order): `self._log_key`, `len`, `plan.remainder_bytes`.

Control points:

- L217: `if not declared_bytes`
- L226: `if remainder`

### `RecordMaterialisationComposer._report` - L236-L260

```python
_report(self, examined: int, applied: int) -> None
```

A no-op is always visible, and a refusal is never buried.

Observed calls (lexical order): `self._log_key`, `len`, `DETAIL_SEPARATOR.join`, `DETAIL_TEMPLATE.format`.

Control points:

- L238: `if examined == 0`
- L249: `if not self.refusals`

### `RecordMaterialisationComposer._refuse` - L265-L268

```python
_refuse(self, record: str, refusal) -> None
```

Log the reason AND remember it for the summary line.

Observed calls (lexical order): `self._log`, `self._reason_of`, `self.refusals.append`.

### `RecordMaterialisationComposer._refuse_key` - L270-L278

```python
_refuse_key(self, record: str, key: str, reason: str, **values) -> None
```

Observed calls (lexical order): `self._log_key`, `self.refusals.append`.

### `RecordMaterialisationComposer._reason_of` - L281-L285

```python
_reason_of(refusal) -> str
```

A short human reason, derived from the message key.

Observed calls (lexical order): `getattr`, `str`, `str(getattr(refusal, 'key', '') or 'refused').replace`, `str(getattr(refusal, 'key', '') or 'refused').replace('skipped_', '').replace`.

### `RecordMaterialisationComposer._log` - L290-L292

```python
_log(self, refusal) -> None
```

Observed calls (lexical order): `dict`, `getattr`, `self._log_key`.

### `RecordMaterialisationComposer._log_key` - L294-L302

```python
_log_key(self, key: str, **values) -> None
```

Observed calls (lexical order): `RECORD_MATERIALISATION_MESSAGES.get`, `self.messages.append`, `template.format`.

Control points:

- L296: `if not template`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
