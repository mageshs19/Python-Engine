# `converter/generators/restart/restart_main_flow_builder.py`

Source: [converter/generators/restart/restart_main_flow_builder.py](../../../../../converter/generators/restart/restart_main_flow_builder.py) | 218 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `7ce3970dff6682efc21201c441025c00fa1b9a056380e0006aca4e34ff854460`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Builds the mainline statement block of an update program.

## Module-level bindings

`TOTALS_MARKER` (L65), `STOP_RUN` (L66), `OPEN_PREFIX` (L67), `CLOSE_PREFIX` (L68), `__all__` (L212)

## Import declarations

```python
from __future__ import annotations
from typing import Sequence
from converter.generators.restart.restart_config import RestartConfig
from rules.restart_standard_rules import ROLE_COMMIT, ROLE_CONTROL
from rules.restart_statement_templates import MAIN_FLOW_TEMPLATE
```

## Local dependency notes

- [converter/generators/restart/restart_config.py](restart_config.md)
- [rules/restart_standard_rules.py](../../../rules/restart_standard_rules.md)
- [rules/restart_statement_templates.py](../../../rules/restart_statement_templates.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/restart/restart_injection_composer.py](../../composers/restart/restart_injection_composer.md)
- [tests/restart/test_m6_main_flow_builder.py](../../../tests/restart/test_m6_main_flow_builder.md)

## Symbol contracts and control points

### `RestartMainFlowBuilder` - L71-L209

```python
class RestartMainFlowBuilder()
```

Renders the mainline between OPEN INPUT and STOP RUN.

### `RestartMainFlowBuilder.__init__` - L74-L76

```python
__init__(self, config: RestartConfig) -> None
```

### `RestartMainFlowBuilder.build` - L82-L139

```python
build(self, totals: Sequence[str]=(), *, suppress_open: bool=False, suppress_prime_read: bool=False) -> tuple[str, ...]
```

The mainline lines, or an empty tuple when refused.

Observed calls (lexical order): `self._usable`, `self.config.placeholders`, `raw.strip`, `lines.extend`, `str`, `raw.format`, `' '.join`, `rendered.strip`, `rendered.strip().upper`, `rendered.strip().upper().split`, `body.startswith`, `dropped.append`, `prime_read.upper`, `lines.append`, `self._collapse_blanks`, `self.messages.append`.
Another 2 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L105: `if not self._usable()`
- L113: `for raw in MAIN_FLOW_TEMPLATE`
- L114: `if raw.strip() == TOTALS_MARKER`
- L121: `if suppress_open and body.startswith(OPEN_PREFIX)`
- L124: `if suppress_prime_read and body == prime_read.upper()`
- L132: `for statement in dropped`

### `RestartMainFlowBuilder._collapse_blanks` - L142-L156

```python
_collapse_blanks(lines: list[str]) -> list[str]
```

One separator, never two.

Observed calls (lexical order): `line.strip`, `out[-1].strip`, `out.append`, `out.pop`.

Control points:

- L150: `for line in lines`
- L151: `if not line.strip() and (not out or not out[-1].strip())`
- L154: `while out and (not out[-1].strip())`

### `RestartMainFlowBuilder.statements` - L158-L162

```python
statements(self, totals: Sequence[str]=()) -> tuple[str, ...]
```

The mainline with blank separator lines removed.

Observed calls (lexical order): `tuple`, `line.strip`, `self.build`.

### `RestartMainFlowBuilder._usable` - L168-L181

```python
_usable(self) -> bool
```

Observed calls (lexical order): `self.config.is_usable`, `self.config.missing`, `self.messages.append`.

Control points:

- L169: `if self.config.is_usable()`
- L172: `for name in self.config.missing()`
- L176: `if self.config.retention_days <= 0`

### `RestartMainFlowBuilder._report` - L187-L209

```python
_report(self, lines: list[str], totals: Sequence[str]) -> None
```

Observed calls (lexical order): `self.messages.append`, `self.config.paragraph`, `len`.

Control points:

- L201: `if totals`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
