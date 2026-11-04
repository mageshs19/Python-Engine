# `converter/composers/counter_declaration/counter_anchor_resolver.py`

Source: [converter/composers/counter_declaration/counter_anchor_resolver.py](../../../../../converter/composers/counter_declaration/counter_anchor_resolver.py) | 77 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `2ae54fe340981e3e40e226ed74c335175625cfc87e4e5285202b90b8156bd5b3`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`__all__` (L77)

## Import declarations

```python
from __future__ import annotations
from converter.composers.counter_declaration.counter_anchor import CounterAnchor, CounterAnchorFinder
from converter.composers.counter_declaration.counter_line_factory import CounterLineFactory
from converter.services.generated_field_anchor import GeneratedFieldAnchorResolver
from converter.services.working_storage_group_selector import WorkingStorageGroupSelector
from rules.structural_safety_rules import ENFORCE_SAFE_COUNTER_GROUP, STRUCTURAL_SAFETY_MESSAGES
```

## Local dependency notes

- [converter/composers/counter_declaration/counter_anchor.py](counter_anchor.md)
- [converter/composers/counter_declaration/counter_line_factory.py](counter_line_factory.md)
- [converter/services/generated_field_anchor.py](../../services/generated_field_anchor.md)
- [converter/services/working_storage_group_selector.py](../../services/working_storage_group_selector.md)
- [rules/structural_safety_rules.py](../../../rules/structural_safety_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/counter_declaration/__init__.py](__init__.md)

## Symbol contracts and control points

### `CounterAnchorResolver` - L22-L74

```python
class CounterAnchorResolver()
```

### `CounterAnchorResolver.__init__` - L24-L40

```python
__init__(self, line_factory: CounterLineFactory | None=None, selector: WorkingStorageGroupSelector | None=None, finder: CounterAnchorFinder | None=None, field_anchor: GeneratedFieldAnchorResolver | None=None) -> None
```

Observed calls (lexical order): `CounterLineFactory`, `WorkingStorageGroupSelector`, `CounterAnchorFinder`, `GeneratedFieldAnchorResolver`.

### `CounterAnchorResolver.resolve` - L42-L69

```python
resolve(self, lines: list[str]) -> tuple[list[str], CounterAnchor | None]
```

Observed calls (lexical order): `self.selector.analyze`, `self.finder.anchor_for`, `self.field_anchor.resolve`, `self.messages.extend`, `list`, `CounterAnchor`.

Control points:

- L48: `if not ENFORCE_SAFE_COUNTER_GROUP`
- L51: `if group is None`
- L60: `if not anchor.is_usable`

### `CounterAnchorResolver._log` - L71-L74

```python
_log(self, key: str, **values) -> None
```

Observed calls (lexical order): `STRUCTURAL_SAFETY_MESSAGES.get`, `str`, `self.messages.append`, `template.format`.

Control points:

- L73: `if template`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
