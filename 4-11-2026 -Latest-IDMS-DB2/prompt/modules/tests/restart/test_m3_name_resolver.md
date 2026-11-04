# `tests/restart/test_m3_name_resolver.py`

Source: [tests/restart/test_m3_name_resolver.py](../../../../tests/restart/test_m3_name_resolver.py) | 643 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `18d232fb4b6cb768fbc39ebb63632ba61f43a1cd33dc467bf175c2ca3847095d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> M3 contract tests: the resolver reads names, or refuses.

## Module-level bindings

`PROCESS_LOOP_MARKER` (L87), `GENERATOR_OWNED` (L91), `BARE_PROGRAM` (L102), `PARTIAL_GROUP_PROGRAM` (L127)

## Import declarations

```python
from __future__ import annotations
import pytest
from catalogs.restart_storage_catalog import GENERATED_STORAGE_FIELDS
from converter.composers.restart.restart_storage_injector import RestartStorageInjector
from converter.generators.restart.restart_config import RestartConfig
from converter.generators.restart.restart_name_resolver import RestartNameResolver
from converter.generators.restart.restart_config import RestartProgramNames
```

## Local dependency notes

- [catalogs/restart_storage_catalog.py](../../catalogs/restart_storage_catalog.md)
- [converter/composers/restart/restart_storage_injector.py](../../converter/composers/restart/restart_storage_injector.md)
- [converter/generators/restart/restart_config.py](../../converter/generators/restart/restart_config.md)
- [converter/generators/restart/restart_name_resolver.py](../../converter/generators/restart/restart_name_resolver.md)

## Symbol contracts and control points

### `resolve` - L152-L156

```python
resolve(line_utils)
```

### `resolve._resolve` - L153-L154

```python
_resolve(lines)
```

Observed calls (lexical order): `RestartNameResolver`, `RestartNameResolver(line_utils).resolve`.

### `_index_of` - L159-L164

```python
_index_of(lines: list[str], marker: str) -> int
```

Position of the first line containing the marker.

Observed calls (lexical order): `enumerate`, `next`.

### `_logical` - L167-L173

```python
_logical(line_utils, lines) -> list[str]
```

Observed calls (lexical order): `line_utils.logical`, `str`, `str(line_utils.logical(raw) or '').strip`, `' '.join`, `body.upper`, `body.upper().split`, `out.append`.

Control points:

- L169: `for raw in lines`
- L171: `if body`

### `_declared_text` - L176-L179

```python
_declared_text(line_utils, config, lines) -> str
```

Everything the storage injector leaves declared, as one string.

Observed calls (lexical order): `RestartStorageInjector`, `' '.join`, `_logical`, `injector.inject`, `list`.

### `_assert_promise_kept` - L182-L192

```python
_assert_promise_kept(line_utils, role, resolve, lines) -> None
```

Every SUPPLIED name must appear in the injected storage.

Observed calls (lexical order): `resolve`, `RestartConfig.build`, `_declared_text`, `getattr`, `isinstance`.

Control points:

- L189: `for key in report.defaulted`
- L191: `if isinstance(value, str) and value`

### `test_a_complete_program_resolves_every_name` - L199-L202

```python
test_a_complete_program_resolves_every_name(resolve, source_lines)
```

Observed calls (lexical order): `resolve`, `names.is_complete`.

### `test_a_complete_program_needs_no_defaults` - L205-L208

```python
test_a_complete_program_needs_no_defaults(resolve, source_lines)
```

Every name is MEASURED when the program carries it.

Observed calls (lexical order): `resolve`.

### `test_file_and_record_come_from_the_read_statement` - L211-L214

```python
test_file_and_record_come_from_the_read_statement(resolve, source_lines)
```

Observed calls (lexical order): `resolve`.

### `test_eof_conditions_come_from_the_88_levels` - L217-L220

```python
test_eof_conditions_come_from_the_88_levels(resolve, source_lines)
```

Observed calls (lexical order): `resolve`.

### `test_the_reader_paragraph_is_found` - L223-L225

```python
test_the_reader_paragraph_is_found(resolve, source_lines)
```

Observed calls (lexical order): `resolve`.

### `test_the_business_paragraph_is_found` - L228-L230

```python
test_the_business_paragraph_is_found(resolve, source_lines)
```

Observed calls (lexical order): `resolve`.

### `test_working_storage_names_are_resolved` - L233-L243

```python
test_working_storage_names_are_resolved(resolve, source_lines)
```

Observed calls (lexical order): `resolve`.

### `test_the_payload_sizes_are_read_from_the_pictures` - L250-L253

```python
test_the_payload_sizes_are_read_from_the_pictures(resolve, source_lines)
```

Observed calls (lexical order): `resolve`.

### `test_a_different_layout_produces_a_different_length` - L256-L269

```python
test_a_different_layout_produces_a_different_length(resolve, source_lines)
```

1215 was never a constant; it is this program's measurement.

Observed calls (lexical order): `line.replace`, `resolve`.

### `test_a_group_item_is_named_but_not_measured` - L272-L275

```python
test_a_group_item_is_named_but_not_measured(resolve, source_lines)
```

WS-RESTART-REC is a group; it has no picture to measure.

Observed calls (lexical order): `resolve`.

### `test_a_comp_3_counter_is_measured_by_its_digits` - L278-L287

```python
test_a_comp_3_counter_is_measured_by_its_digits(resolve, source_lines)
```

Usage is not length. PIC 9(15) is fifteen digits either way.

Observed calls (lexical order): `line.replace`, `resolve`.

### `test_an_undeclared_payload_field_is_supplied` - L294-L307

```python
test_an_undeclared_payload_field_is_supplied(resolve, source_lines)
```

Was: refused. KY-RESTART is created by M5, so it is supplied.

Observed calls (lexical order): `resolve`.

### `test_an_undeclared_counter_is_supplied` - L310-L317

```python
test_an_undeclared_counter_is_supplied(resolve, source_lines)
```

Was: 'an undeclared default is never emitted'.

Observed calls (lexical order): `resolve`.

### `test_a_supplied_name_says_so` - L320-L326

```python
test_a_supplied_name_says_so(resolve, source_lines)
```

Observed calls (lexical order): `resolve`, `any`.

### `test_the_eof_pair_is_built_when_the_program_has_no_88_levels` - L329-L350

```python
test_the_eof_pair_is_built_when_the_program_has_no_88_levels(resolve)
```

VMDZ1567 uses a bare 77-level switch. Refusing here would stop the whole family over a naming style.

Observed calls (lexical order): `resolve`.

### `test_the_eof_pair_is_refused_without_a_record_name` - L353-L358

```python
test_the_eof_pair_is_refused_without_a_record_name(resolve)
```

It is BUILT from the record name. No record, no pair.

Observed calls (lexical order): `resolve`.

### `test_a_program_owned_name_is_never_supplied` - L365-L372

```python
test_a_program_owned_name_is_never_supplied(resolve, source_lines)
```

The guard that matters. CS-PROGRAM belongs to the program.

Observed calls (lexical order): `resolve`.

### `test_a_refusal_is_reported_with_a_reason` - L375-L381

```python
test_a_refusal_is_reported_with_a_reason(resolve, source_lines)
```

Observed calls (lexical order): `resolve`, `any`.

### `test_no_generator_owned_name_is_ever_refused` - L384-L394

```python
test_no_generator_owned_name_is_ever_refused(resolve)
```

The two sets are disjoint, whatever the program looks like.

Observed calls (lexical order): `resolve`, `set`.

### `test_an_empty_program_refuses_every_program_owned_name` - L397-L410

```python
test_an_empty_program_refuses_every_program_owned_name(resolve)
```

Observed calls (lexical order): `resolve`, `names.is_complete`, `len`.

Control points:

- L401: `for key in ('file_name', 'record_name', 'read_paragraph', 'process_paragraph', 'program_constant', 'error_paragraph', 'abend_module')`

### `test_an_empty_program_resolves_nothing_it_does_not_own` - L413-L415

```python
test_an_empty_program_resolves_nothing_it_does_not_own(resolve)
```

Observed calls (lexical order): `resolve`, `set`.

### `test_a_program_with_no_procedure_division_refuses_paragraphs` - L418-L426

```python
test_a_program_with_no_procedure_division_refuses_paragraphs(resolve)
```

Observed calls (lexical order): `resolve`.

### `test_a_bare_program_supplies_every_generator_owned_name` - L433-L440

```python
test_a_bare_program_supplies_every_generator_owned_name(resolve)
```

The pipeline case: no restart storage anywhere.

Observed calls (lexical order): `resolve`, `getattr`.

Control points:

- L436: `for key in GENERATED_STORAGE_FIELDS`

### `test_every_supplied_name_is_actually_declared` - L443-L452

```python
test_every_supplied_name_is_actually_declared(line_utils, resolve, role)
```

Supplying a name is a PROMISE that M5 declares it.

Observed calls (lexical order): `_assert_promise_kept`.

### `test_a_partial_group_is_completed` - L455-L463

```python
test_a_partial_group_is_completed(line_utils, resolve, role)
```

A group header present with its members missing.

Observed calls (lexical order): `_assert_promise_kept`.

### `test_an_infrastructure_paragraph_is_never_chosen_as_business` - L469-L479

```python
test_an_infrastructure_paragraph_is_never_chosen_as_business(resolve, source_lines)
```

Observed calls (lexical order): `list`, `_index_of`, `lines.insert`, `resolve`.

### `test_every_numbering_scheme_is_treated_as_infrastructure` - L496-L497

```python
test_every_numbering_scheme_is_treated_as_infrastructure(paragraph)
```

Observed calls (lexical order): `RestartNameResolver._is_infrastructure`.

### `test_a_business_paragraph_is_not_infrastructure` - L500-L502

```python
test_a_business_paragraph_is_not_infrastructure()
```

Observed calls (lexical order): `RestartNameResolver._is_infrastructure`.

### `test_a_loop_on_the_wrong_condition_is_rejected` - L505-L512

```python
test_a_loop_on_the_wrong_condition_is_rejected(resolve, source_lines)
```

Observed calls (lexical order): `line.replace`, `resolve`, `names.missing`.

### `test_the_error_paragraph_requires_its_include` - L519-L521

```python
test_the_error_paragraph_requires_its_include(resolve, source_lines)
```

Observed calls (lexical order): `resolve`.

### `test_a_missing_include_refuses_the_error_paragraph` - L524-L528

```python
test_a_missing_include_refuses_the_error_paragraph(resolve, source_lines)
```

Observed calls (lexical order): `resolve`.

### `test_the_one_line_include_form_is_accepted` - L531-L540

```python
test_the_one_line_include_form_is_accepted(resolve)
```

Observed calls (lexical order): `resolve`.

### `test_another_include_does_not_satisfy_the_error_paragraph` - L543-L553

```python
test_another_include_does_not_satisfy_the_error_paragraph(resolve)
```

Observed calls (lexical order): `resolve`.

### `test_comment_lines_are_ignored` - L560-L574

```python
test_comment_lines_are_ignored(resolve, source_lines)
```

The comment must sit where the resolver actually LOOKS.

Observed calls (lexical order): `list`, `_index_of`, `lines.insert`, `resolve`.

### `test_the_sequence_area_never_leaks_into_a_name` - L577-L585

```python
test_the_sequence_area_never_leaks_into_a_name(resolve, source_lines)
```

Observed calls (lexical order): `resolve`, `value[:1].isdigit`.

Control points:

- L579: `for value in (names.file_name, names.record_name, names.process_paragraph, names.read_paragraph)`

### `test_free_format_input_is_accepted` - L588-L608

```python
test_free_format_input_is_accepted(resolve)
```

Observed calls (lexical order): `resolve`.

### `test_resolution_is_repeatable` - L615-L618

```python
test_resolution_is_repeatable(resolve, source_lines)
```

Observed calls (lexical order): `resolve`.

### `test_a_default_does_not_accumulate_across_runs` - L621-L627

```python
test_a_default_does_not_accumulate_across_runs(line_utils, source_lines)
```

One resolver instance, two calls: the defaulted list is reset.

Observed calls (lexical order): `RestartNameResolver`, `resolver.resolve`.

### `test_the_report_lists_every_resolved_name` - L630-L633

```python
test_the_report_lists_every_resolved_name(resolve, source_lines)
```

Observed calls (lexical order): `resolve`.

Control points:

- L632: `for key in names.REQUIRED`

### `test_eighteen_entries_are_required` - L636-L643

```python
test_eighteen_entries_are_required()
```

Sixteen names plus two measurements.

Observed calls (lexical order): `len`, `set`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
