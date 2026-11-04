# `converter/generators/restart/restart_totals_resolver.py`

Source: [converter/generators/restart/restart_totals_resolver.py](../../../../../converter/generators/restart/restart_totals_resolver.py) | 160 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `f2259933f36192a8088a914659976511248c5783169d38465a4c29888ed222e4`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Builds the end-of-run DISPLAY totals for a restart mainline.

## Module-level bindings

`SENTENCE_TERMINATOR` (L37), `_ADD_VERBS` (L42), `__all__` (L160)

## Import declarations

```python
from __future__ import annotations
from typing import List, Sequence
from rules.counter_rules import COUNTER_ADD_TEMPLATE, COUNTER_DISPLAY_TEMPLATE, COUNTER_TOTAL_LABEL_BY_SUFFIX, COUNTER_TOTAL_LABEL_DEFAULT, COUNTER_TOTAL_MESSAGES, COUNTER_TOTAL_NAME_PREFIX
```

## Local dependency notes

- [rules/counter_rules.py](../../../rules/counter_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/restart/restart_stage_adapter.py](../../composers/restart/restart_stage_adapter.md)
- [converter/pipeline/conversion/conversion_pipeline_steps.py](../../pipeline/conversion/conversion_pipeline_steps.md)

## Symbol contracts and control points

### `RestartTotalsResolver` - L48-L157

```python
class RestartTotalsResolver()
```

One DISPLAY per counter the program increments.

### `RestartTotalsResolver.__init__` - L51-L53

```python
__init__(self, line_utils=None) -> None
```

### `RestartTotalsResolver.resolve` - L55-L96

```python
resolve(self, lines: Sequence[str], guaranteed: Sequence[str]=()) -> tuple[str, ...]
```

Totals for every counter the program increments.

Observed calls (lexical order): `self._incremented_counters`, `str`, `str(raw or '').strip`, `str(raw or '').strip().upper`, `name.startswith`, `names.append`, `self._say`, `self._label`, `labels.values`, `len`, `max`, `tuple`, `labels[name].ljust`, `self._display`, `', '.join`.

Control points:

- L76: `for raw in guaranteed or ()`
- L78: `if not name.startswith(COUNTER_TOTAL_NAME_PREFIX)`
- L80: `if name in names`
- L85: `if not names`

### `RestartTotalsResolver._incremented_counters` - L100-L114

```python
_incremented_counters(self, lines: Sequence[str]) -> List[str]
```

Observed calls (lexical order): `self._body`, `body.startswith`, `body[len(verb):].strip`, `body[len(verb):].strip().rstrip`, `len`, `name.split`, `name.split(' ')[0].upper`, `name.startswith`, `found.append`.

Control points:

- L103: `for line in lines`
- L105: `for verb in _ADD_VERBS`
- L106: `if not body.startswith(verb)`
- L110: `if name.startswith(COUNTER_TOTAL_NAME_PREFIX) and name not in found`

### `RestartTotalsResolver._label` - L116-L125

```python
_label(self, name: str) -> str
```

Observed calls (lexical order): `sorted`, `name.endswith`, `len`, `COUNTER_TOTAL_LABEL_BY_SUFFIX[suffix].format`, `COUNTER_TOTAL_LABEL_DEFAULT.format`.

Control points:

- L117: `for suffix in sorted(COUNTER_TOTAL_LABEL_BY_SUFFIX, key=len, reverse=True)`
- L118: `if not name.endswith(suffix)`

### `RestartTotalsResolver._display` - L127-L131

```python
_display(self, name: str, label: str) -> str
```

Observed calls (lexical order): `COUNTER_DISPLAY_TEMPLATE.format`, `line.rstrip`, `line.rstrip().endswith`.

Control points:

- L129: `if not line.rstrip().endswith(SENTENCE_TERMINATOR)`

### `RestartTotalsResolver._body` - L133-L141

```python
_body(self, line: str) -> str
```

Observed calls (lexical order): `self.line_utils.logical`, `str`, `self._fixed_body`, `' '.join`, `str(raw or '').upper`, `str(raw or '').upper().split`.

Control points:

- L134: `if self.line_utils is not None`

### `RestartTotalsResolver._fixed_body` - L144-L148

```python
_fixed_body(line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`.

Control points:

- L146: `if len(text) >= 72 and text[:6].strip().isdigit()`

### `RestartTotalsResolver._say` - L150-L157

```python
_say(self, key: str, **values: object) -> None
```

Observed calls (lexical order): `COUNTER_TOTAL_MESSAGES.get`, `self.messages.append`, `template.format`.

Control points:

- L152: `if not template`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
