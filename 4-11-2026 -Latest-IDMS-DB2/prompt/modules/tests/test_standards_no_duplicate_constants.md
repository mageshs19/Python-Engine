# `tests/test_standards_no_duplicate_constants.py`

Source: [tests/test_standards_no_duplicate_constants.py](../../../tests/test_standards_no_duplicate_constants.py) | 84 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `5ade2f2e7574ef47fa9633edc4f14369fc4885473c40d83360e59fb1298d68bd`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> No module may declare the same constant twice.

## Module-level bindings

`ROOT` (L22), `SCANNED` (L23)

## Import declarations

```python
from __future__ import annotations
import ast
import pathlib
from collections import defaultdict
```

## Symbol contracts and control points

### `_duplicates` - L26-L43

```python
_duplicates(path: pathlib.Path) -> list[str]
```

Observed calls (lexical order): `ast.parse`, `path.read_text`, `defaultdict`, `isinstance`, `_target_names`, `seen[name].append`, `seen.items`, `sorted`, `len`.

Control points:

- L33: `for node in tree.body`
- L34: `if not isinstance(node, (ast.Assign, ast.AugAssign, ast.AnnAssign))`
- L36: `for name in _target_names(node)`

### `_target_names` - L45-L71

```python
_target_names(node: ast.AST) -> list[str]
```

Constant-like assignment targets, including dict entries.

Observed calls (lexical order): `getattr`, `isinstance`, `target.id.isupper`, `names.append`, `target.value.id.isupper`, `ast.unparse`.

Control points:

- L59: `for target in targets`
- L60: `if isinstance(target, ast.Name) and target.id.isupper()`
- L62: `if isinstance(target, ast.Subscript) and isinstance(target.value, ast.Name) and target.value.id.isupper()`

### `test_no_module_declares_a_constant_twice` - L73-L84

```python
test_no_module_declares_a_constant_twice()
```

Observed calls (lexical order): `base.is_dir`, `base.rglob`, `_duplicates`, `offenders.extend`, `'\n'.join`.

Control points:

- L75: `for folder in SCANNED`
- L77: `if not base.is_dir()`
- L79: `for path in base.rglob('*.py')`

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
