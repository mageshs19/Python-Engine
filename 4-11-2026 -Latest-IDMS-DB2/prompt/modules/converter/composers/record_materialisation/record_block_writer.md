# `converter/composers/record_materialisation/record_block_writer.py`

Source: [converter/composers/record_materialisation/record_block_writer.py](../../../../../converter/composers/record_materialisation/record_block_writer.py) | 123 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `acf8002d1d67934e38ba055459c5e9a0189b6971fc462d9bd7ba02e311a87177`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Rewrites the MOVE statement and expands the target field.

## Module-level bindings

`__all__` (L123)

## Import declarations

```python
from __future__ import annotations
from converter.composers.record_materialisation.record_line_utils import RecordLineUtils
from rules.record_materialisation_rules import MOVE_INDENT, RECORD_GROUP_LEVEL_STEP
```

## Local dependency notes

- [converter/composers/record_materialisation/record_line_utils.py](record_line_utils.md)
- [rules/record_materialisation_rules.py](../../../rules/record_materialisation_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/record_materialisation/__init__.py](__init__.md)
- [converter/composers/record_materialisation_composer.py](../record_materialisation_composer.md)
- [tests/test_mapping_filler_layout_regression.py](../../../tests/test_mapping_filler_layout_regression.md)

## Symbol contracts and control points

### `RecordBlockWriter` - L42-L120

```python
class RecordBlockWriter()
```

Produces the replacement lines. Decides nothing.

### `RecordBlockWriter.__init__` - L45-L54

```python
__init__(self, *, layout_generator, move_generator, line_utils: RecordLineUtils | None=None) -> None
```

Observed calls (lexical order): `RecordLineUtils`.

### `RecordBlockWriter.replace_move` - L57-L79

```python
replace_move(self, lines: list[str], index: int, plan) -> list[str]
```

Swap the whole-record MOVE for the field-by-field block.

Observed calls (lexical order): `self.lines.body_indent`, `self.move_generator.generate`, `body.lstrip`, `stripped.startswith`, `rendered.extend`, `self.lines.emit`, `stripped.lstrip`.

Control points:

- L68: `for body in self.move_generator.generate(plan)`
- L70: `if stripped.startswith('*')`

### `RecordBlockWriter.expand_target` - L82-L120

```python
expand_target(self, lines: list[str], index: int, target: str, plan, *, target_level: int=0, declared_bytes: int=0) -> list[str]
```

Replace `05 F-FORM PIC X(478).` with the real layout.

Observed calls (lexical order): `self.lines.logical`, `body.split`, `self.lines.body_indent`, `self.lines.level_of`, `list`, `self.lines.emit`, `self.layout_generator.generate`, `rendered.extend`, `self.lines.emit_generated`, `self.layout_generator.remainder_line`, `plan.remainder_bytes`.

Control points:

- L105: `for text in self.layout_generator.generate(plan, base_level=base_level, base_indent=indent)`
- L113: `for text in self.layout_generator.remainder_line(level=base_level + RECORD_GROUP_LEVEL_STEP, byte_count=plan.remainder_bytes(declared_bytes), base_indent=indent)`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
