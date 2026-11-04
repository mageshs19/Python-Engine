# `converter/postprocess/storage_include/storage_include_injector.py`

Source: [converter/postprocess/storage_include/storage_include_injector.py](../../../../../converter/postprocess/storage_include/storage_include_injector.py) | 380 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `f13d70e72d801c5a8612c9e11c6b8a5dfb5f171d39ddd6edf00c91cd5eb6e840`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> DCLGEN + copybook include injection and reference scanning.

## Import declarations

```python
from __future__ import annotations
from converter.generators.db2_infrastructure.include_renderer import IncludeRenderer
from patterns.update_storage_include_patterns import DCL_HOST_REFERENCE_PATTERN
from rules.update_restart_rules import UPDATE_RESTART_DIAGNOSTICS
from rules.update_storage_include_rules import COPY_EXISTS_BY_RECORD_TEMPLATE, COPY_EXISTS_TEMPLATE, COPY_INJECTED_TEMPLATE, DCL_GROUP_PREFIX, DCLGEN_INCLUDE_EXISTS_TEMPLATE, DCLGEN_INCLUDE_INJECTED_TEMPLATE, EXCLUDED_INCLUDE_NAMES, REFERENCED_DCLGEN_INJECTED_TEMPLATE, RESTART_DCLGEN_UNAVAILABLE, SKIP_DATA_DIVISION_COPYBOOK_TEMPLATE, SKIP_DATA_DIVISION_DCLGEN_TEMPLATE, SKIP_DATA_DIVISION_REFERENCED
import re
import os
```

## Local dependency notes

- [converter/generators/db2_infrastructure/include_renderer.py](../../generators/db2_infrastructure/include_renderer.md)
- [patterns/update_storage_include_patterns.py](../../../patterns/update_storage_include_patterns.md)
- [rules/update_restart_rules.py](../../../rules/update_restart_rules.md)
- [rules/update_storage_include_rules.py](../../../rules/update_storage_include_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/update_storage_include_manager.py](../update_storage_include_manager.md)

## Symbol contracts and control points

### `StorageIncludeInjector` - L76-L380

```python
class StorageIncludeInjector()
```

DCLGEN + copybook include injection and reference scanning.

### `StorageIncludeInjector.deduplicate_includes` - L82-L143

```python
deduplicate_includes(self, cobol_text: str, diagnostics: list) -> str
```

Remove ALL duplicate EXEC SQL INCLUDE statements.

Observed calls (lexical order): `os.path.expanduser`, `open`, `f.write`, `cobol_text.split`, `enumerate`, `re.search`, `match.group`, `match.group(1).upper`, `includes_found[include_name].append`, `set`, `includes_found.items`, `len`, `lines_to_remove.add`, `diagnostics.append`, `'\n'.join`.

Control points:

- L102: `for (i, line) in enumerate(lines)`
- L106: `if match`
- L109: `if include_name not in includes_found`
- L120: `for (include_name, line_indices) in includes_found.items()`
- L121: `if len(line_indices) > 1`
- L123: `for dup_idx in line_indices[1:]`
- L132: `if lines_to_remove`

### `StorageIncludeInjector.includes` - L149-L160

```python
includes(self) -> IncludeRenderer
```

Renderer and scanner shared with every other include emitter.

Observed calls (lexical order): `getattr`, `IncludeRenderer`.

Control points:

- L157: `if renderer is None`

### `StorageIncludeInjector.ensure_dclgen_include` - L165-L207

```python
ensure_dclgen_include(self, cobol_text, context, diagnostics)
```

Observed calls (lexical order): `diagnostics.append`, `self.includes.normalize`, `self.line_utils.lines`, `self.includes.existing`, `DCLGEN_INCLUDE_EXISTS_TEMPLATE.format`, `self._include_already_exists`, `self.line_utils.data_division_insert_line_index`, `SKIP_DATA_DIVISION_DCLGEN_TEMPLATE.format`, `self.includes.render`, `DCLGEN_INCLUDE_INJECTED_TEMPLATE.format`, `self.line_utils.join`.

Control points:

- L167: `if not role`
- L172: `if not include_name`
- L180: `if include_name in self.includes.existing(lines)`
- L187: `if self._include_already_exists(cobol_text, include_name)`
- L194: `if insert_index < 0`

### `StorageIncludeInjector._include_already_exists` - L209-L231

```python
_include_already_exists(self, cobol_text: str, include_name: str) -> bool
```

Check if EXEC SQL INCLUDE exists in any form.

Observed calls (lexical order): `re.escape`, `re.search`.

Control points:

- L223: `if re.search(pattern1, cobol_text, re.IGNORECASE | re.DOTALL)`
- L228: `if re.search(pattern2, cobol_text, re.IGNORECASE)`

### `StorageIncludeInjector.ensure_referenced_dclgen_includes` - L236-L290

```python
ensure_referenced_dclgen_includes(self, cobol_text, diagnostics)
```

Observed calls (lexical order): `self.line_utils.lines`, `self._referenced_dclgen_includes`, `self.includes.missing`, `self._include_already_exists`, `missing_filtered.append`, `diagnostics.append`, `self.line_utils.data_division_insert_line_index`, `include_lines.extend`, `self.includes.render`, `REFERENCED_DCLGEN_INJECTED_TEMPLATE.format`, `self.line_utils.join`.

Control points:

- L249: `if not missing`
- L255: `for include_name in missing`
- L257: `if not self._include_already_exists(cobol_text, include_name)`
- L264: `if not missing_filtered`
- L268: `if insert_index < 0`
- L273: `for include_name in missing_filtered`
- L284: `if not include_lines`

### `StorageIncludeInjector.ensure_copybook_include` - L295-L341

```python
ensure_copybook_include(self, cobol_text, context, diagnostics)
```

A COPY member, not an EXEC SQL include.

Observed calls (lexical order): `self.line_utils.contains_copy`, `diagnostics.append`, `COPY_EXISTS_TEMPLATE.format`, `COPY_EXISTS_BY_RECORD_TEMPLATE.format`, `self.line_utils.lines`, `self.line_utils.data_division_insert_line_index`, `SKIP_DATA_DIVISION_COPYBOOK_TEMPLATE.format`, `self.generator.copybook_include`, `self.generator.copybook_include(context).splitlines`, `COPY_INJECTED_TEMPLATE.format`, `self.line_utils.join`.

Control points:

- L304: `if self.line_utils.contains_copy(cobol_text, include_name)`
- L313: `if record_name != include_name and self.line_utils.contains_copy(cobol_text, record_name)`
- L323: `if insert_index < 0`

### `StorageIncludeInjector._existing_exec_sql_includes` - L346-L353

```python
_existing_exec_sql_includes(self, cobol_text) -> set[str]
```

Every include already present, WHICHEVER shape carries it.

Observed calls (lexical order): `self.includes.existing`, `self.line_utils.lines`.

### `StorageIncludeInjector._referenced_dclgen_includes` - L355-L380

```python
_referenced_dclgen_includes(self, cobol_text) -> list[str]
```

Include names implied by DCLGEN host group references.

Observed calls (lexical order): `set`, `DCL_HOST_REFERENCE_PATTERN.finditer`, `match.group`, `str`, `str(match.group('group') or '').strip`, `str(match.group('group') or '').strip().upper`, `group_name.startswith`, `len`, `seen.add`, `output.append`.

Control points:

- L364: `for match in DCL_HOST_REFERENCE_PATTERN.finditer(cobol_text)`
- L367: `if not group_name.startswith(DCL_GROUP_PREFIX)`
- L372: `if not include_name or include_name in EXCLUDED_INCLUDE_NAMES`
- L374: `if include_name in seen`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
