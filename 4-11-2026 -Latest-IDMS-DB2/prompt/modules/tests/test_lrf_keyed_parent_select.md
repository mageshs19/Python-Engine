# `tests/test_lrf_keyed_parent_select.py`

Source: [tests/test_lrf_keyed_parent_select.py](../../../tests/test_lrf_keyed_parent_select.py) | 47 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `df69f1c418df97a60f9a5c1981ed99ebb28fea8a9c7d88af0b1bf3bc33ccb286`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Executable SQL contract for retrieval-side LRF keyed parent reads.

## Symbol contracts and control points

### `test_lrf_parent_select_populates_mapped_record_and_uses_key` - L4-L22

```python
test_lrf_parent_select_populates_mapped_record_and_uses_key(transformer_context)
```

Observed calls (lexical order): `transformer_context['statement_transformer'].sql_generator.select_by_key`, `'\n'.join`, `'\n'.join(sql).upper`.

### `test_ordinary_obtain_calc_keeps_legacy_update_behavior` - L25-L31

```python
test_ordinary_obtain_calc_keeps_legacy_update_behavior(transformer_context)
```

Observed calls (lexical order): `transformer_context['statement_transformer'].sql_generator.select_by_key`, `'\n'.join`, `'\n'.join(sql).upper`.

### `test_lrf_parent_select_sets_sql_location_before_sql_and_not_inside_when_other` - L34-L47

```python
test_lrf_parent_select_sets_sql_location_before_sql_and_not_inside_when_other(transformer_context)
```

Observed calls (lexical order): `transformer_context['statement_transformer'].sql_generator.select_by_key`, `'\n'.join`, `'\n'.join(sql).upper`, `text.index`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
