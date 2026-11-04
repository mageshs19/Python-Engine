# `converter/analyzers/program_flow/flow_diagnostics.py`

Source: [converter/analyzers/program_flow/flow_diagnostics.py](../../../../../converter/analyzers/program_flow/flow_diagnostics.py) | 57 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `b14adebe799a5a12ab59238217bcbde4433050242a59aedfb129d9b5a3bb9bcc`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Assembles the analyzer's diagnostic report.

## Module-level bindings

`__all__` (L57)

## Import declarations

```python
from __future__ import annotations
from converter.analyzers.program_flow.flow_models import CursorLoop
from rules.program_flow_rules import FLOW_MESSAGES, LOOP_SAMPLE_LIMIT
```

## Local dependency notes

- [converter/analyzers/program_flow/flow_models.py](flow_models.md)
- [rules/program_flow_rules.py](../../../rules/program_flow_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/analyzers/program_flow/__init__.py](__init__.md)
- [converter/analyzers/program_flow/program_flow_analyzer.py](program_flow_analyzer.md)

## Symbol contracts and control points

### `FlowDiagnostics` - L16-L54

```python
class FlowDiagnostics()
```

Collects analyzer messages in report order.

### `FlowDiagnostics.__init__` - L19-L20

```python
__init__(self) -> None
```

### `FlowDiagnostics.add` - L22-L29

```python
add(self, key: str, **values) -> None
```

Observed calls (lexical order): `FLOW_MESSAGES.get`, `self.messages.append`, `template.format`.

Control points:

- L24: `if not template`

### `FlowDiagnostics.extend` - L31-L34

```python
extend(self, messages: list[str] | None) -> None
```

Observed calls (lexical order): `self.messages.append`.

Control points:

- L32: `for message in messages or []`
- L33: `if message`

### `FlowDiagnostics.counts` - L36-L39

```python
counts(self, **named_counts: int) -> None
```

One count line per key, in the order given.

Observed calls (lexical order): `named_counts.items`, `self.add`.

Control points:

- L38: `for (key, count) in named_counts.items()`

### `FlowDiagnostics.loop_samples` - L41-L49

```python
loop_samples(self, loops: list[CursorLoop]) -> None
```

Observed calls (lexical order): `self.add`.

Control points:

- L42: `for loop in (loops or [])[:LOOP_SAMPLE_LIMIT]`

### `FlowDiagnostics.drain` - L51-L54

```python
drain(self) -> list[str]
```

Observed calls (lexical order): `list`.

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
