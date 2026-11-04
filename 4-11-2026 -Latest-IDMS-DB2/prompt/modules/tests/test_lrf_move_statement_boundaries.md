# `tests/test_lrf_move_statement_boundaries.py`

Source: [tests/test_lrf_move_statement_boundaries.py](../../../tests/test_lrf_move_statement_boundaries.py) | 43 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `1fbca5e7c15a63cc1a546a166aae99562fffcc22824409eb52944974b3472ae1`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> MOVE collectors must respect next-verb boundaries in period-free COBOL.

## Import declarations

```python
from converter.composers.lrf_group_move_decomposer import LrfGroupMoveDecomposer
```

## Local dependency notes

- [converter/composers/lrf_group_move_decomposer.py](../converter/composers/lrf_group_move_decomposer.md)

## Symbol contracts and control points

### `_line` - L5-L6

```python
_line(number: int, statement: str) -> str
```

### `_collector` - L9-L15

```python
_collector() -> LrfGroupMoveDecomposer
```

Observed calls (lexical order): `LrfGroupMoveDecomposer`.

### `test_write_from_is_not_consumed_by_preceding_period_free_move` - L18-L26

```python
test_write_from_is_not_consumed_by_preceding_period_free_move()
```

Observed calls (lexical order): `_line`, `_collector`, `_collector()._collect_move`.

### `test_continued_receiving_fields_remain_part_of_move` - L29-L37

```python
test_continued_receiving_fields_remain_part_of_move()
```

Observed calls (lexical order): `_line`, `_collector`, `_collector()._collect_move`.

### `test_other_cobol_verbs_terminate_multi_destination_collection` - L40-L43

```python
test_other_cobol_verbs_terminate_multi_destination_collection()
```

Observed calls (lexical order): `_line`, `_collector`, `_collector()._collect_move`.

Control points:

- L41: `for verb in ('READ FILE-A', 'REWRITE REC-A', 'CLOSE FILE-A', 'COMPUTE X = 2', 'ADD 1 TO X')`

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
