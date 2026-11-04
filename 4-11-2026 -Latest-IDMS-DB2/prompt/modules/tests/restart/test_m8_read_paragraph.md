# `tests/restart/test_m8_read_paragraph.py`

Source: [tests/restart/test_m8_read_paragraph.py](../../../../tests/restart/test_m8_read_paragraph.py) | 247 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `a7fca4856c1912e1ceb21d5e7e9e5345ce84a2756c4badcca520a6898fe7e637`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> M8 contract tests: the reader paragraph.

## Module-level bindings

`GENERATED_READER` (L25)

## Import declarations

```python
from __future__ import annotations
import dataclasses
import pytest
from converter.generators.restart.read_paragraph_builder import ROLE_READ, RestartReadParagraphBuilder
from converter.generators.restart.restart_config import RestartConfig, RestartProgramNames
from rules import restart_standard_rules as std
```

## Local dependency notes

- [converter/generators/restart/read_paragraph_builder.py](../../converter/generators/restart/read_paragraph_builder.md)
- [converter/generators/restart/restart_config.py](../../converter/generators/restart/restart_config.md)
- [rules/__init__.py](../../rules/__init__.md)
- [rules/restart_standard_rules.py](../../rules/restart_standard_rules.md)

## Symbol contracts and control points

### `builder` - L32-L33

```python
builder(config)
```

Observed calls (lexical order): `RestartReadParagraphBuilder`.

### `paragraph` - L37-L38

```python
paragraph(builder)
```

Observed calls (lexical order): `builder.build`.

### `_body` - L41-L42

```python
_body(paragraph)
```

Observed calls (lexical order): `line.strip`.

### `_text` - L45-L46

```python
_text(paragraph)
```

Observed calls (lexical order): `'\n'.join`, `paragraph.lines`.

### `test_the_paragraph_is_named_from_the_source` - L53-L55

```python
test_the_paragraph_is_named_from_the_source(config, paragraph)
```

Observed calls (lexical order): `paragraph.lines`.

### `test_the_role_is_not_a_restart_family_role` - L58-L62

```python
test_the_role_is_not_a_restart_family_role(paragraph)
```

### `test_a_debug_trace_is_carried` - L65-L66

```python
test_a_debug_trace_is_carried(config, paragraph)
```

### `test_no_placeholder_survives` - L69-L72

```python
test_no_placeholder_survives(paragraph)
```

Observed calls (lexical order): `_text`.

### `test_the_paragraph_closes_its_sentence` - L75-L76

```python
test_the_paragraph_closes_its_sentence(paragraph)
```

Observed calls (lexical order): `_body`, `_body(paragraph)[-1].endswith`.

### `test_the_scope_is_balanced` - L79-L82

```python
test_the_scope_is_balanced(paragraph)
```

Observed calls (lexical order): `' '.join`, `_body`, `body.count`, `body.startswith`.

### `test_the_record_is_initialised_before_the_read` - L89-L94

```python
test_the_record_is_initialised_before_the_read(config, paragraph)
```

Observed calls (lexical order): `_body`, `enumerate`, `l.startswith`, `next`.

### `test_the_read_names_the_file_and_the_record` - L97-L102

```python
test_the_read_names_the_file_and_the_record(config, paragraph)
```

Observed calls (lexical order): `_text`.

### `test_at_end_sets_the_88_level` - L105-L109

```python
test_at_end_sets_the_88_level(config, paragraph)
```

MOVE 'Y' TO SW-EOF was the shape the manual replaced.

Observed calls (lexical order): `_text`.

### `test_the_commit_counter_is_incremented` - L116-L117

```python
test_the_commit_counter_is_incremented(config, paragraph)
```

Observed calls (lexical order): `_body`.

### `test_the_input_counter_is_incremented` - L120-L121

```python
test_the_input_counter_is_incremented(config, paragraph)
```

Observed calls (lexical order): `_body`.

### `test_the_record_is_saved_for_the_checkpoint` - L124-L128

```python
test_the_record_is_saved_for_the_checkpoint(config, paragraph)
```

Observed calls (lexical order): `_body`.

### `test_the_four_statements_are_guarded_by_not_eof` - L131-L142

```python
test_the_four_statements_are_guarded_by_not_eof(config, paragraph)
```

At end of file there is no record to count or save.

Observed calls (lexical order): `_body`, `next`, `enumerate`, `l.startswith`.

Control points:

- L138: `for statement in ('ADD +1 TO', 'MOVE ')`

### `test_every_required_statement_is_present` - L145-L148

```python
test_every_required_statement_is_present(builder, paragraph)
```

Observed calls (lexical order): `_text`, `_text(paragraph).upper`, `builder.required_statements`, `statement.upper`.

Control points:

- L147: `for statement in builder.required_statements()`

### `test_four_statements_are_required` - L151-L152

```python
test_four_statements_are_required(builder)
```

Observed calls (lexical order): `builder.required_statements`, `len`.

### `test_the_generated_reader_is_missing_all_four` - L159-L160

```python
test_the_generated_reader_is_missing_all_four(builder)
```

Observed calls (lexical order): `builder.missing_statements`, `len`.

### `test_the_generated_reader_needs_a_rebuild` - L163-L164

```python
test_the_generated_reader_needs_a_rebuild(builder)
```

Observed calls (lexical order): `builder.needs_rebuild`.

### `test_every_gap_is_reported` - L167-L170

```python
test_every_gap_is_reported(builder)
```

Observed calls (lexical order): `builder.needs_rebuild`, `len`, `all`.

### `test_a_complete_reader_needs_no_rebuild` - L173-L174

```python
test_a_complete_reader_needs_no_rebuild(builder, paragraph)
```

Observed calls (lexical order): `builder.needs_rebuild`, `list`, `paragraph.lines`.

### `test_a_partial_reader_reports_only_its_gaps` - L177-L187

```python
test_a_partial_reader_reports_only_its_gaps(config, builder)
```

Observed calls (lexical order): `builder.missing_statements`, `len`, `any`.

### `test_whitespace_differences_do_not_count_as_missing` - L190-L193

```python
test_whitespace_differences_do_not_count_as_missing(config, builder)
```

Observed calls (lexical order): `builder.missing_statements`, `any`.

### `test_an_empty_reader_is_missing_everything` - L196-L197

```python
test_an_empty_reader_is_missing_everything(builder)
```

Observed calls (lexical order): `builder.missing_statements`, `len`.

### `test_an_unusable_config_renders_nothing` - L204-L209

```python
test_an_unusable_config_renders_nothing(role)
```

Observed calls (lexical order): `RestartReadParagraphBuilder`, `RestartConfig.build`, `RestartProgramNames`, `builder.build`.

### `test_a_missing_save_area_renders_nothing` - L212-L216

```python
test_a_missing_save_area_renders_nothing(role, complete_names)
```

Observed calls (lexical order): `dataclasses.replace`, `RestartConfig.build`, `RestartReadParagraphBuilder`, `builder.build`, `any`.

### `test_a_role_without_retention_renders_nothing` - L219-L225

```python
test_a_role_without_retention_renders_nothing(role, complete_names)
```

Observed calls (lexical order): `dataclasses.replace`, `RestartReadParagraphBuilder`, `RestartConfig.build`, `builder.build`, `any`.

### `test_building_twice_produces_identical_output` - L232-L235

```python
test_building_twice_produces_identical_output(config)
```

Observed calls (lexical order): `RestartReadParagraphBuilder`, `RestartReadParagraphBuilder(config).build`.

### `test_messages_are_reset_between_builds` - L238-L242

```python
test_messages_are_reset_between_builds(builder)
```

Observed calls (lexical order): `builder.build`, `len`.

### `test_the_build_is_reported` - L245-L247

```python
test_the_build_is_reported(builder)
```

Observed calls (lexical order): `builder.build`, `any`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
