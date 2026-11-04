# `tests/workspace_fixtures.py`

Source: [tests/workspace_fixtures.py](../../../tests/workspace_fixtures.py) | 22 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `533c022aa5b17d143a320e409fe49021627011ff4d9379d0ebdac4be9d942c82`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Locate bundled integration inputs without historical timestamp assumptions.

## Module-level bindings

`WORKSPACE` (L4)

## Import declarations

```python
from pathlib import Path
```

## Importers (6)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [tests/test_lrf_select_projection_analysis.py](test_lrf_select_projection_analysis.md)
- [tests/test_lrf_vmdz4310_latest_artifact.py](test_lrf_vmdz4310_latest_artifact.md)
- [tests/test_manual_storage_parity_composer.py](test_manual_storage_parity_composer.md)
- [tests/test_mapping_filler_layout_regression.py](test_mapping_filler_layout_regression.md)
- [tests/test_vmdz1526_lrf_update_integration.py](test_vmdz1526_lrf_update_integration.md)
- [tests/test_vmdz4310_manual_reference_parity.py](test_vmdz4310_manual_reference_parity.md)

## Symbol contracts and control points

### `mapping_export` - L7-L10

```python
mapping_export()
```

Observed calls (lexical order): `(WORKSPACE / 'Mapping Sheet').glob`, `sorted`, `len`.

### `generated_program` - L13-L16

```python
generated_program(program)
```

Observed calls (lexical order): `(WORKSPACE / 'Output').glob`, `list`, `max`, `p.stat`.

### `expanded_program` - L19-L22

```python
expanded_program(program)
```

Observed calls (lexical order): `path.is_file`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
