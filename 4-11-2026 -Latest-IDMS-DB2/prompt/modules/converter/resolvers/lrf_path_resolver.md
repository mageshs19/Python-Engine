# `converter/resolvers/lrf_path_resolver.py`

Source: [converter/resolvers/lrf_path_resolver.py](../../../../converter/resolvers/lrf_path_resolver.py) | 322 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `405fd5e67393faed0c2406f38981a96cfc9f995aca51b7be6707e5061ec2b304`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Turns an LRF path keyword into a concrete access plan.

## Module-level bindings

`RETURN_PREFIX` (L66), `CALC_KEY_TOKEN` (L71), `NAVIGATION_VERBS` (L73), `__all__` (L322)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass, field
from rules.lrf_conversion_rules import STATUS_END_OF_SET, STATUS_NOT_FOUND, STATUS_SET_EMPTY
```

## Local dependency notes

- [rules/lrf_conversion_rules.py](../../rules/lrf_conversion_rules.md)

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)
- [tests/test_lrf_keyword_scope_safety.py](../../tests/test_lrf_keyword_scope_safety.md)
- [tests/test_lrf_path_expander.py](../../tests/test_lrf_path_expander.md)
- [tests/test_lrf_update_expander.py](../../tests/test_lrf_update_expander.md)

## Symbol contracts and control points

### `cobol_name` - L76-L78

```python
cobol_name(value: str) -> str
```

UPPERCASE COBOL/IDMS form: hyphens, never underscores.

Observed calls (lexical order): `str`, `str(value or '').strip`, `str(value or '').strip().upper`, `str(value or '').strip().upper().replace`.

### `LrfAccessStep` - L82-L110

```python
class LrfAccessStep()
```

One renderable IDMS access line.

Declared class/data-model fields:

```python
verb: str = ''
scope: str = ''
record_name: str = ''
within_name: str = ''
where_clause: str = ''
```

### `LrfAccessStep.is_renderable` - L92-L98

```python
is_renderable(self) -> bool
```

A SET or AREA access: both a record and a container.

Observed calls (lexical order): `bool`.

### `LrfAccessStep.is_calc` - L101-L105

```python
is_calc(self) -> bool
```

A keyed access: a record, no container, a CALCKEY clause.

Observed calls (lexical order): `str`, `str(self.where_clause or '').upper`.

Control points:

- L103: `if not self.record_name or self.within_name`

### `LrfAccessStep.is_resolvable` - L108-L110

```python
is_resolvable(self) -> bool
```

Either shape. Used for reporting, never for rendering.

### `LrfAccessPlan` - L114-L134

```python
class LrfAccessPlan()
```

Everything the expander needs for one path keyword.

Declared class/data-model fields:

```python
keyword: str = ''
logical_record: str = ''
path_group_verb: str = ''
parent: LrfAccessStep | None = None
calc_parent: LrfAccessStep | None = None
driving: LrfAccessStep | None = None
end_of_set_literals: set[str] = field(default_factory=set)
not_found_literals: set[str] = field(default_factory=set)
element_records: list[str] = field(default_factory=list)
```

### `LrfAccessPlan.is_usable` - L128-L129

```python
is_usable(self) -> bool
```

Observed calls (lexical order): `bool`.

### `LrfAccessPlan.has_parent_access` - L132-L134

```python
has_parent_access(self) -> bool
```

True when the path positions a parent before the driving step.

Observed calls (lexical order): `bool`.

### `LrfPathResolver` - L137-L319

```python
class LrfPathResolver()
```

Resolves a path keyword into an LrfAccessPlan.

### `LrfPathResolver.__init__` - L140-L148

```python
__init__(self, *, lrf_repository=None, mapping_repository=None) -> None
```

### `LrfPathResolver.is_empty` - L151-L157

```python
is_empty(self) -> bool
```

Observed calls (lexical order): `bool`, `self.lrf_repository.is_empty`.

Control points:

- L152: `if self.lrf_repository is None`

### `LrfPathResolver.plan_for_keyword` - L159-L220

```python
plan_for_keyword(self, keyword: str, logical_record_name: str | None=None) -> LrfAccessPlan | None
```

Observed calls (lexical order): `self.is_empty`, `self.lrf_repository.path_for_keyword`, `LrfAccessPlan`, `cobol_name`, `str`, `str(path.path_group_verb or '').upper`, `self._element_records`, `self._collect_literals`, `str(command.verb or '').upper`, `steps.append`, `LrfAccessStep`, `str(command.scope or '').upper`, `str(command.where_clause or '').strip`, `len`, `self._attach_calc_parent`.

Control points:

- L164: `if self.is_empty()`
- L174: `if path is None`
- L189: `for command in path.commands or []`
- L193: `if verb not in NAVIGATION_VERBS`
- L206: `if not steps`
- L211: `if renderable`
- L213: `if len(renderable) > 1`

### `LrfPathResolver.record_is_mapped` - L222-L249

```python
record_is_mapped(self, record_name: str) -> bool
```

True when Sheet Mapping knows this IDMS record.

Observed calls (lexical order): `cobol_name`, `getattr`, `method`, `isinstance`, `bool`, `result.strip`.

Control points:

- L224: `if self.mapping_repository is None`
- L228: `if not record`
- L231: `for probe in ('db2_table_for_record', 'table_for_record', 'has_record', 'record_exists')`
- L238: `if method is None`
- L244: `if isinstance(result, bool)`
- L246: `if isinstance(result, str)`

### `LrfPathResolver._attach_calc_parent` - L252-L287

```python
_attach_calc_parent(self, plan: LrfAccessPlan, steps: list[LrfAccessStep]) -> None
```

Record a KEYED parent that precedes the driving step.

Observed calls (lexical order): `self._log`.

Control points:

- L262: `if plan.parent is not None or plan.driving is None`
- L265: `for step in steps`
- L266: `if step is plan.driving`
- L268: `if not step.is_calc`
- L281: `if preceding`

### `LrfPathResolver._element_records` - L289-L293

```python
_element_records(self, logical_record_name: str) -> list
```

Observed calls (lexical order): `self.lrf_repository.element_records`.

### `LrfPathResolver._collect_literals` - L296-L305

```python
_collect_literals(command, plan: LrfAccessPlan) -> None
```

Observed calls (lexical order): `getattr`, `actions.items`, `LrfPathResolver._return_literal`, `str`, `plan.end_of_set_literals.add`, `plan.not_found_literals.add`.

Control points:

- L298: `for (status, action) in actions.items()`
- L300: `if not literal`
- L302: `if str(status) == STATUS_END_OF_SET`
- L304: `if str(status) in (STATUS_NOT_FOUND, STATUS_SET_EMPTY)`

### `LrfPathResolver._return_literal` - L308-L312

```python
_return_literal(action: str) -> str
```

Observed calls (lexical order): `str`, `str(action or '').strip`, `str(action or '').strip().upper`, `text.startswith`, `cobol_name`, `len`.

Control points:

- L310: `if not text.startswith(RETURN_PREFIX)`

### `LrfPathResolver._log` - L314-L319

```python
_log(self, key: str, **values) -> None
```

Plain-text diagnostics. This resolver owns no message catalogue.

Observed calls (lexical order): `' '.join`, `sorted`, `values.items`, `self.messages.append`.

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
