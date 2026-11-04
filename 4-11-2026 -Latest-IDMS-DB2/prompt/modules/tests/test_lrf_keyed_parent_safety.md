# `tests/test_lrf_keyed_parent_safety.py`

Source: [tests/test_lrf_keyed_parent_safety.py](../../../tests/test_lrf_keyed_parent_safety.py) | 22 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `7fa90d42cabbacf7bb274e11a32d76df1dc352165def1d3e660ae62ecc668a3d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Safety contract for retrieval-side LRF-generated keyed parent reads.

## Symbol contracts and control points

### `test_lrf_calc_read_generates_executable_parent_select` - L4-L22

```python
test_lrf_calc_read_generates_executable_parent_select(statement_transformer)
```

Observed calls (lexical order): `transformer.transform_line`, `'\n'.join`, `'\n'.join(lines).upper`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
