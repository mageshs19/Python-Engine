# `tests/test_rules_no_duplicate_constants.py`

Source: [tests/test_rules_no_duplicate_constants.py](../../../tests/test_rules_no_duplicate_constants.py) | 83 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `66ff739da78fb9cad32e12e054e9d0e48cde33ec347cf6d7c1aaaf8de72bf2a1`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> A module-level name assigned twice is a silent, order-dependent bug.

## Module-level bindings

`RULES_DIR` (L15), `RULE_FILES` (L16)

## Import declarations

```python
from __future__ import annotations
import ast
from collections import Counter
from pathlib import Path
import pytest
from rules import cursor_declaration_rules
from string import Formatter
from rules import record_materialisation_rules
```

## Local dependency notes

- [rules/__init__.py](../rules/__init__.md)
- [rules/cursor_declaration_rules.py](../rules/cursor_declaration_rules.md)
- [rules/record_materialisation_rules.py](../rules/record_materialisation_rules.md)

## Symbol contracts and control points

### `_module_level_assignments` - L19-L31

```python
_module_level_assignments(path: Path) -> Counter
```

Observed calls (lexical order): `ast.parse`, `path.read_text`, `Counter`, `isinstance`.

Control points:

- L22: `for node in tree.body`
- L24: `if isinstance(node, ast.Assign)`
- L26: `if isinstance(node, ast.AnnAssign) and node.value is not None`
- L28: `for target in targets`
- L29: `if isinstance(target, ast.Name)`

### `test_no_rule_constant_is_assigned_twice` - L35-L37

```python
test_no_rule_constant_is_assigned_twice(path: Path) -> None
```

Observed calls (lexical order): `_module_level_assignments`, `_module_level_assignments(path).items`, `sorted`.

### `test_order_by_message_catalogues_do_not_collide` - L40-L45

```python
test_order_by_message_catalogues_do_not_collide() -> None
```

The resolver merges both dicts; a shared key would shadow one.

Observed calls (lexical order): `set`, `sorted`.

### `test_every_key_width_message_has_the_placeholders_the_resolver_supplies` - L48-L59

```python
test_every_key_width_message_has_the_placeholders_the_resolver_supplies() -> None
```

Observed calls (lexical order): `cursor_declaration_rules.ORDER_BY_KEY_MESSAGES.items`, `Formatter`, `Formatter().parse`.

Control points:

- L57: `for (key, template) in cursor_declaration_rules.ORDER_BY_KEY_MESSAGES.items()`

### `test_queryno_first_matches_the_manual_reference` - L62-L67

```python
test_queryno_first_matches_the_manual_reference() -> None
```

### `test_queryno_template_keeps_the_number_placeholder` - L70-L73

```python
test_queryno_template_keeps_the_number_placeholder() -> None
```

cursor_declare_builder renders with .format(number=...).

Observed calls (lexical order): `cursor_declaration_rules.QUERYNO_TEMPLATE.format`.

### `test_sentinels_are_re_exported_not_redeclared` - L76-L82

```python
test_sentinels_are_re_exported_not_redeclared() -> None
```

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
