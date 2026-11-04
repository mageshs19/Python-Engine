# `tests/test_lrf_two_stage_contract_v26.py`

Source: [tests/test_lrf_two_stage_contract_v26.py](../../../tests/test_lrf_two_stage_contract_v26.py) | 35 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `a622c25ee1f0e6dcc836f4a27fd636a9421f33a259f5781323e5658800c3197f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`ROOT` (L3), `PIPELINE` (L4)

## Import declarations

```python
from pathlib import Path
from patterns.cursor_spec.lrf_comment_patterns import LRF_ACCESS_MARKER_PROBE
```

## Local dependency notes

- [patterns/cursor_spec/lrf_comment_patterns.py](../patterns/cursor_spec/lrf_comment_patterns.md)

## Symbol contracts and control points

### `test_source_proven_sql_lowering_is_part_of_standard_two_stage_path` - L7-L13

```python
test_source_proven_sql_lowering_is_part_of_standard_two_stage_path()
```

Observed calls (lexical order): `PIPELINE.read_text`.

### `test_lrf_normalization_still_precedes_db2_transform` - L16-L21

```python
test_lrf_normalization_still_precedes_db2_transform()
```

Observed calls (lexical order): `PIPELINE.read_text`, `source.index`.

### `test_lrf_marker_probe_only_flags_access_markers_not_update_markers` - L24-L35

```python
test_lrf_marker_probe_only_flags_access_markers_not_update_markers()
```

Observed calls (lexical order): `LRF_ACCESS_MARKER_PROBE.search`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
