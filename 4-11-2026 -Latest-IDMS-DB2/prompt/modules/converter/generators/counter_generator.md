# `converter/generators/counter_generator.py`

Source: [converter/generators/counter_generator.py](../../../../converter/generators/counter_generator.py) | 191 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `7902f10c8e6926cd21c5c29c02378eff2d71a4cb9fe571fd3e5e6f82211d0f28`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Row counter and program-name constant generator.

## Import declarations

```python
from __future__ import annotations
from converter.services.name_normalizer import NameNormalizer
from rules.counter_rules import COUNTER_ADD_TEMPLATE, COUNTER_DECLARATION_TEMPLATE, COUNTER_DISPLAY_TEMPLATE, COUNTER_LABEL_FETCH_TEMPLATE, COUNTER_LABEL_OUTPUT, COUNTER_LABEL_WIDTH, COUNTER_MESSAGES, COUNTER_NAME_TEMPLATE, COUNTER_PICTURE, EMIT_COUNTER_TOTALS, EMIT_PROGRAM_NAME_CONSTANT, EMIT_ROW_COUNTERS, OUTPUT_COUNTER_NAME, PROGRAM_CONSTANT_NAME, PROGRAM_CONSTANT_TEMPLATE, PROGRAM_NAME_MOVE_TEMPLATE, PROGRAM_NAME_TARGET_FIELD
```

## Local dependency notes

- [converter/services/name_normalizer.py](../services/name_normalizer.md)
- [rules/counter_rules.py](../../rules/counter_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/cursor_paragraph/cursor_fetch_paragraph.py](cursor_paragraph/cursor_fetch_paragraph.md)

## Symbol contracts and control points

### `CounterGenerator` - L45-L191

```python
class CounterGenerator()
```

Builds counter declarations, increments and end-of-run totals.

### `CounterGenerator.__init__` - L48-L49

```python
__init__(self) -> None
```

### `CounterGenerator.counter_name_for_table` - L55-L82

```python
counter_name_for_table(table_name: str) -> str
```

Derive WS-NB-<token>-COUNT from a DB2 table name.

Observed calls (lexical order): `NameNormalizer.normalize`, `str`, `token.endswith`, `len`, `token.strip`, `COUNTER_NAME_TEMPLATE.format`.

Control points:

- L63: `if not table`
- L67: `for suffix in ('_TV', '_TB')`
- L68: `if token.endswith(suffix)`
- L72: `if token.endswith('TV') or token.endswith('TB')`
- L75: `if len(token) > 2`
- L79: `if not token`

### `CounterGenerator.declarations` - L87-L120

```python
declarations(self, program_id: str, table_names: list[str]) -> list[str]
```

Lines to append inside the existing 01 work group.

Observed calls (lexical order): `self._counter_names`, `lines.append`, `COUNTER_DECLARATION_TEMPLATE.format`, `self.messages.append`, `COUNTER_MESSAGES['declared_counter'].format`, `PROGRAM_CONSTANT_TEMPLATE.format`, `NameNormalizer.to_cobol`, `COUNTER_MESSAGES['declared_program_constant'].format`.

Control points:

- L96: `if EMIT_ROW_COUNTERS`
- L97: `for name in self._counter_names(table_names)`
- L107: `if EMIT_PROGRAM_NAME_CONSTANT and program_id`

### `CounterGenerator.increment` - L126-L129

```python
increment(counter_name: str) -> str
```

Observed calls (lexical order): `COUNTER_ADD_TEMPLATE.format`.

Control points:

- L127: `if not EMIT_ROW_COUNTERS or not counter_name`

### `CounterGenerator.program_name_move` - L135-L141

```python
program_name_move() -> str
```

Observed calls (lexical order): `PROGRAM_NAME_MOVE_TEMPLATE.format`.

Control points:

- L136: `if not EMIT_PROGRAM_NAME_CONSTANT`

### `CounterGenerator.totals` - L146-L173

```python
totals(self, table_names: list[str]) -> list[str]
```

Observed calls (lexical order): `self.counter_name_for_table`, `name.replace`, `name.replace('WS-NB-', '').replace`, `COUNTER_LABEL_FETCH_TEMPLATE.format`, `lines.append`, `COUNTER_DISPLAY_TEMPLATE.format`, `label.ljust`, `COUNTER_LABEL_OUTPUT.ljust`, `self.messages.append`, `COUNTER_MESSAGES['counter_totals_added'].format`, `len`.

Control points:

- L147: `if not EMIT_COUNTER_TOTALS`
- L151: `for table in table_names`
- L153: `if not name`

### `CounterGenerator._counter_names` - L178-L191

```python
_counter_names(self, table_names: list[str]) -> list[str]
```

Observed calls (lexical order): `set`, `self.counter_name_for_table`, `seen.add`, `out.append`.

Control points:

- L182: `for table in table_names`
- L184: `if name and name not in seen`
- L188: `if OUTPUT_COUNTER_NAME not in seen`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
