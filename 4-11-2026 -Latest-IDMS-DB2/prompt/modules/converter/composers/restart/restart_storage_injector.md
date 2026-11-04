# `converter/composers/restart/restart_storage_injector.py`

Source: [converter/composers/restart/restart_storage_injector.py](../../../../../converter/composers/restart/restart_storage_injector.py) | 452 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `21edab89f3d99cfa9a4a4be239c12196bbc01627234127e893655892f98d2106`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Places the generated restart working storage into the program.

## Module-level bindings

`WORKING_STORAGE_TOKEN` (L96), `GROUP_LEVEL` (L97), `GROUP_TERMINATOR_LEVELS` (L101), `GROUP_TERMINATOR_TOKENS` (L102), `GROUP_SOURCES` (L113), `INCLUDE_NAME_ATTRIBUTES` (L121), `INCLUDE_INDENT` (L124), `MESSAGE_PREFIX` (L126), `__all__` (L447)

## Import declarations

```python
from __future__ import annotations
from catalogs.output_sections import INCLUDE_STATEMENT_TEMPLATE
from catalogs.restart_storage_catalog import DATE_GROUP, HELP_GROUP, SWITCH_GROUP
from converter.composers.restart.restart_line_utils import RestartLineUtils
from converter.generators.restart.restart_config import RestartConfig
from converter.generators.restart.restart_storage_builder import RestartStorageBuilder
```

## Local dependency notes

- [catalogs/output_sections.py](../../../catalogs/output_sections.md)
- [catalogs/restart_storage_catalog.py](../../../catalogs/restart_storage_catalog.md)
- [converter/composers/restart/restart_line_utils.py](restart_line_utils.md)
- [converter/generators/restart/restart_config.py](../../generators/restart/restart_config.md)
- [converter/generators/restart/restart_storage_builder.py](../../generators/restart/restart_storage_builder.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/restart/restart_injection_composer.py](restart_injection_composer.md)
- [tests/restart/test_m11b_storage_injector.py](../../../tests/restart/test_m11b_storage_injector.md)
- [tests/restart/test_m3_name_resolver.py](../../../tests/restart/test_m3_name_resolver.md)

## Symbol contracts and control points

### `RestartStorageInjector` - L129-L444

```python
class RestartStorageInjector()
```

Inserts the restart storage and its include, once, in the right section.

### `RestartStorageInjector.__init__` - L133-L136

```python
__init__(self, config: RestartConfig, line_utils=None) -> None
```

Observed calls (lexical order): `RestartLineUtils`.

### `RestartStorageInjector.inject` - L141-L168

```python
inject(self, lines: list[str]) -> list[str]
```

Return the program with any MISSING storage or include added.

Observed calls (lexical order): `list`, `RestartStorageBuilder`, `builder.build`, `self.messages.extend`, `self._say`, `self._working_storage_index`, `plan.extend`, `self._plan_include`, `self._plan_groups`, `self._apply`.

Control points:

- L147: `if not builder.build()`
- L153: `if anchor < 0`
- L164: `if not plan`

### `RestartStorageInjector._plan_include` - L173-L192

```python
_plan_include(self, lines: list[str], anchor: int) -> list[tuple[int, list[str]]]
```

Observed calls (lexical order): `self._include_member`, `self._say`, `self._declares_include`, `INCLUDE_STATEMENT_TEMPLATE.format`.

Control points:

- L179: `if not member`
- L186: `if self._declares_include(lines, member)`

### `RestartStorageInjector._include_member` - L194-L200

```python
_include_member(self) -> str
```

Observed calls (lexical order): `getattr`, `str`, `str(getattr(role, attribute, '') or '').strip`, `str(getattr(role, attribute, '') or '').strip().upper`.

Control points:

- L196: `for attribute in INCLUDE_NAME_ATTRIBUTES`
- L198: `if value`

### `RestartStorageInjector._declares_include` - L202-L210

```python
_declares_include(self, lines: list[str], member: str) -> bool
```

Observed calls (lexical order): `member.upper`, `self._logical`, `logical.startswith`, `wanted.rstrip`.

Control points:

- L204: `for line in lines`
- L206: `if logical.startswith(wanted) or logical == wanted.rstrip()`
- L208: `if logical.startswith(f'EXEC SQL INCLUDE {member.upper()}')`

### `RestartStorageInjector._plan_groups` - L215-L270

```python
_plan_groups(self, lines: list[str], builder: RestartStorageBuilder, anchor: int) -> list[tuple[int, list[str]]]
```

Observed calls (lexical order): `self._declared_groups`, `self._declared_names`, `getattr`, `getattr(builder, source)`, `str`, `str(line).strip`, `self._missing_subtrees`, `self._say`, `self._group_end_index`, `plan.append`, `len`, `self._subtree_names`, `str(getattr(self.config.names, anchor_field, '') or '').upper`.

Control points:

- L225: `for (group, source, anchor_field) in GROUP_SOURCES`
- L229: `if not rendered`
- L232: `if group in declared_groups`
- L234: `if not missing`
- L242: `if end < 0`
- L260: `if field and field in declared_names`

### `RestartStorageInjector._missing_subtrees` - L275-L286

```python
_missing_subtrees(self, rendered: list[str], declared_names: set[str]) -> list[str]
```

Rendered members whose head name is not already declared.

Observed calls (lexical order): `self._subtrees`, `out.extend`.

Control points:

- L282: `for (name, block) in self._subtrees(rendered)`
- L283: `if name in declared_names`

### `RestartStorageInjector._subtrees` - L288-L323

```python
_subtrees(self, rendered: list[str]) -> list[tuple[str, list[str]]]
```

Split a rendered group into its top-level subordinates.

Observed calls (lexical order): `list`, `self._level_of`, `subtrees.append`, `self._name_of`, `current.append`.

Control points:

- L295: `if not body`
- L299: `for line in body`
- L301: `if level`
- L304: `if not child_level`
- L311: `for line in body`
- L312: `if self._level_of(line) == child_level`
- L313: `if current`
- L318: `if current`
- Another 1 conditions/loops exist in this source span.

### `RestartStorageInjector._subtree_names` - L325-L326

```python
_subtree_names(self, block: list[str]) -> list[str]
```

Observed calls (lexical order): `self._subtrees`.

### `RestartStorageInjector._working_storage_index` - L331-L335

```python
_working_storage_index(self, lines: list[str]) -> int
```

Observed calls (lexical order): `enumerate`, `self._logical`, `self._logical(line).startswith`.

Control points:

- L332: `for (index, line) in enumerate(lines)`
- L333: `if self._logical(line).startswith(WORKING_STORAGE_TOKEN)`

### `RestartStorageInjector._group_end_index` - L337-L364

```python
_group_end_index(self, lines: list[str], group: str) -> int
```

Index just past the last line of `group`.

Observed calls (lexical order): `group.upper`, `enumerate`, `self._logical`, `self._level_of`, `self._name_of`, `len`, `range`, `logical.startswith`.

Control points:

- L345: `for (index, line) in enumerate(lines)`
- L347: `if self._level_of(logical) == GROUP_LEVEL and self._name_of(logical) == wanted`
- L353: `if start < 0`
- L356: `for index in range(start + 1, len(lines))`
- L358: `if not logical`
- L360: `if self._level_of(logical) in GROUP_TERMINATOR_LEVELS`
- L362: `if logical.startswith(GROUP_TERMINATOR_TOKENS)`

### `RestartStorageInjector._apply` - L367-L392

```python
_apply(lines: list[str], plan: list[tuple[int, list[str]]]) -> list[str]
```

Apply insertions highest index first, so none invalidates another.

Observed calls (lexical order): `list`, `sorted`, `enumerate`, `len`, `max`, `min`.

Control points:

- L389: `for (_position, (index, block)) in ordered`

### `RestartStorageInjector._declared_names` - L397-L404

```python
_declared_names(self, lines: list[str]) -> set[str]
```

Every data name the program declares, at any level.

Observed calls (lexical order): `set`, `self._logical`, `self._name_of`, `found.add`.

Control points:

- L400: `for line in lines`
- L402: `if name`

### `RestartStorageInjector._declared_groups` - L406-L416

```python
_declared_groups(self, lines: list[str]) -> set[str]
```

Every 01-level group name the program already declares.

Observed calls (lexical order): `set`, `self._logical`, `self._level_of`, `self._name_of`, `found.add`.

Control points:

- L409: `for line in lines`
- L411: `if self._level_of(logical) != GROUP_LEVEL`
- L414: `if name`

### `RestartStorageInjector._logical` - L421-L425

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `self.line_utils.logical`, `str`, `self.line_utils.is_comment`, `' '.join`, `body.upper`, `body.upper().split`.

Control points:

- L423: `if self.line_utils.is_comment(body)`

### `RestartStorageInjector._level_of` - L427-L433

```python
_level_of(self, text: str) -> str
```

The level number of a data description line, or "".

Observed calls (lexical order): `self._logical`, `text.isupper`, `logical.split`, `len`, `parts[0].isdigit`.

Control points:

- L431: `if len(parts) >= 2 and parts[0].isdigit()`

### `RestartStorageInjector._name_of` - L435-L441

```python
_name_of(self, text: str) -> str
```

The data name of a data description line, or "".

Observed calls (lexical order): `self._logical`, `text.isupper`, `logical.split`, `len`, `parts[0].isdigit`, `parts[1].rstrip`, `parts[1].rstrip('.').upper`.

Control points:

- L439: `if len(parts) >= 2 and parts[0].isdigit()`

### `RestartStorageInjector._say` - L443-L444

```python
_say(self, message: str) -> None
```

Observed calls (lexical order): `self.messages.append`.

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
