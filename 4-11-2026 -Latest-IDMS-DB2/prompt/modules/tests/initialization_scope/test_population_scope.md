# `tests/initialization_scope/test_population_scope.py`

Source: [tests/initialization_scope/test_population_scope.py](../../../../tests/initialization_scope/test_population_scope.py) | 314 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `666f74e628620948e82d703ffdc8fce21132057006fbd2094a65b3b234f39cbd`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> The second anchor: a paragraph that populates a DCLGEN group.

## Module-level bindings

`GROUP` (L27), `OTHER` (L28)

## Import declarations

```python
from __future__ import annotations
import pytest
from converter.generators.initialization.population_site_scanner import InitializationSite, PopulationSiteScanner
from rules.initialization_placement_rules import SCOPE_ROW
from converter.generators.initialization.scope_initializer import CursorScopedInitializer
```

## Local dependency notes

- [converter/generators/initialization/population_site_scanner.py](../../converter/generators/initialization/population_site_scanner.md)
- [converter/generators/initialization/scope_initializer.py](../../converter/generators/initialization/scope_initializer.md)
- [rules/initialization_placement_rules.py](../../rules/initialization_placement_rules.md)

## Symbol contracts and control points

### `_fixed` - L31-L36

```python
_fixed(body: str, number: int) -> str
```

One 80-column fixed-format record.

Observed calls (lexical order): `f'{body}'[:65].ljust`.

### `_comment` - L38-L49

```python
_comment(body: str, number: int) -> str
```

One 80-column fixed-format COMMENT record.

Observed calls (lexical order): `f'{body}'[:65].ljust`.

### `_program` - L51-L52

```python
_program(bodies: list[str]) -> list[str]
```

Observed calls (lexical order): `_fixed`, `enumerate`.

### `scanner` - L56-L57

```python
scanner() -> PopulationSiteScanner
```

Observed calls (lexical order): `PopulationSiteScanner`.

### `test_a_populating_paragraph_yields_a_site` - L63-L73

```python
test_a_populating_paragraph_yields_a_site(scanner) -> None
```

Observed calls (lexical order): `_program`, `scanner.sites`, `len`.

### `test_the_site_anchors_on_the_first_write` - L76-L84

```python
test_the_site_anchors_on_the_first_write(scanner) -> None
```

INITIALIZE must land above the first MOVE, not the second.

Observed calls (lexical order): `_program`, `scanner.sites`.

### `test_the_site_is_row_scoped` - L87-L94

```python
test_the_site_is_row_scoped(scanner) -> None
```

The paragraph is the per-record unit of work.

Observed calls (lexical order): `_program`, `scanner.sites`.

### `test_the_site_names_its_owning_paragraph` - L97-L103

```python
test_the_site_names_its_owning_paragraph(scanner) -> None
```

Observed calls (lexical order): `_program`, `scanner.sites`, `scanner.sites(lines)[0].owner.upper`.

### `test_a_population_site_resolves_without_a_cursor` - L109-L113

```python
test_a_population_site_resolves_without_a_cursor() -> None
```

CursorOpenSite.is_resolved needs a cursor; this one must not.

Observed calls (lexical order): `InitializationSite`.

### `test_a_site_without_a_group_is_unresolved` - L116-L118

```python
test_a_site_without_a_group_is_unresolved() -> None
```

Observed calls (lexical order): `InitializationSite`.

### `test_a_group_owned_by_a_cursor_is_excluded` - L124-L132

```python
test_a_group_owned_by_a_cursor_is_excluded(scanner) -> None
```

Observed calls (lexical order): `_program`, `scanner.sites`.

### `test_a_program_with_no_dclgen_write_yields_nothing` - L139-L145

```python
test_a_program_with_no_dclgen_write_yields_nothing(scanner) -> None
```

Observed calls (lexical order): `_program`, `scanner.sites`.

### `test_a_comment_is_never_a_site` - L148-L154

```python
test_a_comment_is_never_a_site(scanner) -> None
```

Observed calls (lexical order): `_program`, `_comment`, `lines.append`, `scanner.sites`.

### `test_a_non_dclgen_qualifier_is_not_a_site` - L157-L164

```python
test_a_non_dclgen_qualifier_is_not_a_site(scanner) -> None
```

OF VMBFAR is an IDMS record, not a DCLGEN group.

Observed calls (lexical order): `_program`, `scanner.sites`.

### `test_a_population_placement_is_not_reported_as_a_child_cursor` - L169-L190

```python
test_a_population_placement_is_not_reported_as_a_child_cursor() -> None
```

placed_row_scope claims a parent row that does not exist here.

Observed calls (lexical order): `'\n'.join`, `_program`, `CursorScopedInitializer`, `initializer.process`, `' '.join`.

### `test_the_summary_counts_the_population_site` - L193-L213

```python
test_the_summary_counts_the_population_site() -> None
```

It reported '0 run-level and 0 row-level' after placing one.

Observed calls (lexical order): `'\n'.join`, `_program`, `CursorScopedInitializer`, `initializer.process`, `any`.

### `test_a_group_read_as_a_move_source_is_not_a_site` - L218-L225

```python
test_a_group_read_as_a_move_source_is_not_a_site(scanner) -> None
```

710-JOB-IS-RESTART reads the row the SELECT just returned.

Observed calls (lexical order): `_program`, `scanner.sites`.

### `test_a_group_written_in_two_paragraphs_is_refused` - L231-L240

```python
test_a_group_written_in_two_paragraphs_is_refused(scanner) -> None
```

DCLDZ01RSTV carries its key from the control paragraph.

Observed calls (lexical order): `_program`, `scanner.sites`.

### `test_running_twice_places_one_initialize` - L242-L262

```python
test_running_twice_places_one_initialize() -> None
```

R3 makes INITIALIZE the first executable line; without R4 a second run would stack a duplicate on every pass.

Observed calls (lexical order): `'\n'.join`, `_program`, `CursorScopedInitializer`, `CursorScopedInitializer(source).process`, `CursorScopedInitializer(once).process`, `once.upper`, `once.upper().count`, `twice.upper`, `twice.upper().count`.

### `test_two_buffers_in_one_paragraph_are_both_cleared` - L265-L275

```python
test_two_buffers_in_one_paragraph_are_both_cleared(scanner) -> None
```

R3 anchors both on the first executable line.

Observed calls (lexical order): `_program`, `scanner.sites`, `sorted`.

### `test_a_group_written_in_one_paragraph_is_accepted` - L276-L283

```python
test_a_group_written_in_one_paragraph_is_accepted(scanner) -> None
```

Observed calls (lexical order): `_program`, `scanner.sites`.

### `test_a_write_inside_an_if_is_refused` - L289-L299

```python
test_a_write_inside_an_if_is_refused(scanner) -> None
```

INITIALIZE between IF and THEN is invalid COBOL.

Observed calls (lexical order): `_program`, `scanner.sites`.

### `test_a_wrapped_move_resolves_its_group` - L305-L314

```python
test_a_wrapped_move_resolves_its_group(scanner) -> None
```

Observed calls (lexical order): `_program`, `scanner.sites`, `len`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
