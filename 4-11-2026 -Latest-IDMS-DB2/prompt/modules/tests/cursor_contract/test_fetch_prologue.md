# `tests/cursor_contract/test_fetch_prologue.py`

Source: [tests/cursor_contract/test_fetch_prologue.py](../../../../tests/cursor_contract/test_fetch_prologue.py) | 46 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `ff2ba1c165038334ee029c7768e70738f76969d98f3cdcb0996990a77d341996`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
```

## Symbol contracts and control points

### `test_fetch_paragraph_does_not_initialize_the_dclgen_group` - L4-L5

```python
test_fetch_paragraph_does_not_initialize_the_dclgen_group(fetch)
```

Observed calls (lexical order): `any`, `body.startswith`, `fetch`.

### `test_fetch_paragraph_rearms_the_not_eoc_flag` - L8-L9

```python
test_fetch_paragraph_rearms_the_not_eoc_flag(fetch, names)
```

Observed calls (lexical order): `fetch`.

### `test_fetch_paragraph_still_issues_the_fetch` - L12-L13

```python
test_fetch_paragraph_still_issues_the_fetch(fetch, names)
```

Observed calls (lexical order): `fetch`.

### `test_host_group_is_read_from_the_of_form` - L16-L18

```python
test_host_group_is_read_from_the_of_form(fetch, names)
```

Observed calls (lexical order): `fetch`.

### `test_no_empty_initialize_when_the_group_cannot_be_derived` - L21-L24

```python
test_no_empty_initialize_when_the_group_cannot_be_derived(fetch, names)
```

Observed calls (lexical order): `fetch`, `any`, `body.startswith`.

### `test_open_paragraph_gains_no_initialize` - L27-L29

```python
test_open_paragraph_gains_no_initialize(cursor_paragraph, names)
```

Observed calls (lexical order): `cursor_paragraph`, `any`, `body.startswith`.

### `test_close_paragraph_gains_no_initialize` - L32-L34

```python
test_close_paragraph_gains_no_initialize(cursor_paragraph, names)
```

Observed calls (lexical order): `cursor_paragraph`, `any`, `body.startswith`.

### `test_paragraph_is_one_sentence` - L37-L40

```python
test_paragraph_is_one_sentence(fetch)
```

Observed calls (lexical order): `fetch`, `lines.count`.

### `test_the_fetch_builder_shares_the_facade_collaborators` - L43-L46

```python
test_the_fetch_builder_shares_the_facade_collaborators(paragraphs)
```

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
