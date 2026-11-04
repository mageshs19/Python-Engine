# `tests/restart/test_m5_flow_builder.py`

Source: [tests/restart/test_m5_flow_builder.py](../../../../tests/restart/test_m5_flow_builder.py) | 325 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `8f2527fb0502779fb33b2602f308f7252e6bee4f58b3c54e680becb2210a101b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> M5 contract tests: the five restart flow paragraphs.

## Import declarations

```python
from __future__ import annotations
import dataclasses
import pytest
from converter.generators.restart.restart_config import RestartConfig
from converter.generators.restart.restart_flow_builder import FLOW_TEMPLATES, RestartFlowBuilder
from converter.generators.restart.restart_paragraph import RestartParagraph
from rules import restart_standard_rules as std
from converter.generators.restart.restart_config import RestartProgramNames
```

## Local dependency notes

- [converter/generators/restart/restart_config.py](../../converter/generators/restart/restart_config.md)
- [converter/generators/restart/restart_flow_builder.py](../../converter/generators/restart/restart_flow_builder.md)
- [converter/generators/restart/restart_paragraph.py](../../converter/generators/restart/restart_paragraph.md)
- [rules/__init__.py](../../rules/__init__.md)
- [rules/restart_standard_rules.py](../../rules/restart_standard_rules.md)

## Symbol contracts and control points

### `builder` - L29-L30

```python
builder(config)
```

Observed calls (lexical order): `RestartFlowBuilder`.

### `paragraphs` - L34-L35

```python
paragraphs(builder)
```

Observed calls (lexical order): `builder.build_all`.

### `_text` - L38-L39

```python
_text(paragraph: RestartParagraph) -> str
```

Observed calls (lexical order): `'\n'.join`, `paragraph.lines`.

### `test_five_paragraphs_are_produced` - L46-L53

```python
test_five_paragraphs_are_produced(paragraphs)
```

Observed calls (lexical order): `set`.

### `test_the_emission_order_is_fixed` - L56-L58

```python
test_the_emission_order_is_fixed(builder)
```

Observed calls (lexical order): `builder.build_all`.

### `test_each_header_matches_the_config` - L61-L64

```python
test_each_header_matches_the_config(config, paragraphs)
```

Observed calls (lexical order): `paragraphs.items`, `config.paragraph`, `paragraph.lines`.

Control points:

- L62: `for (role, paragraph) in paragraphs.items()`

### `test_each_paragraph_closes_its_sentence` - L67-L69

```python
test_each_paragraph_closes_its_sentence(paragraphs)
```

Observed calls (lexical order): `paragraphs.values`, `paragraph.executable`, `paragraph.executable()[-1].endswith`.

Control points:

- L68: `for paragraph in paragraphs.values()`

### `test_each_paragraph_carries_a_debug_trace` - L72-L74

```python
test_each_paragraph_carries_a_debug_trace(config, paragraphs)
```

Observed calls (lexical order): `paragraphs.items`, `config.paragraph`.

Control points:

- L73: `for (role, paragraph) in paragraphs.items()`

### `test_no_rendered_line_keeps_a_placeholder` - L77-L81

```python
test_no_rendered_line_keeps_a_placeholder(paragraphs)
```

Observed calls (lexical order): `paragraphs.values`, `_text`.

Control points:

- L78: `for paragraph in paragraphs.values()`

### `test_paragraphs_are_frozen` - L84-L86

```python
test_paragraphs_are_frozen(paragraphs)
```

Observed calls (lexical order): `pytest.raises`.

### `test_the_build_is_reported` - L89-L91

```python
test_the_build_is_reported(builder)
```

Observed calls (lexical order): `builder.build_all`, `any`.

### `test_build_by_role_returns_one_paragraph` - L94-L97

```python
test_build_by_role_returns_one_paragraph(builder)
```

Observed calls (lexical order): `builder.build`.

### `test_control_sets_the_whole_checkpoint_key` - L104-L111

```python
test_control_sets_the_whole_checkpoint_key(config, paragraphs)
```

Observed calls (lexical order): `_text`, `str`.

### `test_control_routes_every_sqlcode` - L114-L121

```python
test_control_routes_every_sqlcode(config, paragraphs)
```

Observed calls (lexical order): `_text`, `config.paragraph`.

### `test_control_performs_the_select` - L124-L126

```python
test_control_performs_the_select(config, paragraphs)
```

Observed calls (lexical order): `_text`, `config.paragraph`.

### `test_control_zeroes_the_commit_counter` - L129-L131

```python
test_control_zeroes_the_commit_counter(config, paragraphs)
```

Observed calls (lexical order): `_text`.

### `test_a_completed_previous_run_abends` - L138-L142

```python
test_a_completed_previous_run_abends(config, paragraphs)
```

Observed calls (lexical order): `_text`, `config.paragraph`.

### `test_a_completed_previous_run_never_merely_continues` - L145-L148

```python
test_a_completed_previous_run_never_merely_continues(paragraphs)
```

CONTINUE here is what allowed a double run.

Observed calls (lexical order): `paragraphs[std.ROLE_RESTART_FOUND].executable`.

### `test_a_resumed_run_replays_the_reader` - L151-L156

```python
test_a_resumed_run_replays_the_reader(config, paragraphs)
```

Observed calls (lexical order): `_text`.

### `test_a_resumed_run_restores_the_input_counter` - L159-L161

```python
test_a_resumed_run_restores_the_input_counter(config, paragraphs)
```

Observed calls (lexical order): `_text`.

### `test_restart_found_loads_the_payload_first` - L164-L170

```python
test_restart_found_loads_the_payload_first(config, paragraphs)
```

Observed calls (lexical order): `paragraphs[std.ROLE_RESTART_FOUND].executable`, `next`, `enumerate`, `l.startswith`.

### `test_write_restart_marks_the_run_incomplete` - L177-L180

```python
test_write_restart_marks_the_run_incomplete(config, paragraphs)
```

Observed calls (lexical order): `_text`.

### `test_write_restart_uses_the_supplied_retention` - L183-L186

```python
test_write_restart_uses_the_supplied_retention(config, paragraphs)
```

Observed calls (lexical order): `_text`.

### `test_write_restart_starts_at_record_zero` - L189-L193

```python
test_write_restart_starts_at_record_zero(config, paragraphs)
```

Observed calls (lexical order): `_text`.

### `test_write_restart_uses_the_measured_length` - L196-L199

```python
test_write_restart_uses_the_measured_length(config, paragraphs)
```

Observed calls (lexical order): `_text`, `str`.

### `test_write_restart_performs_the_insert` - L202-L204

```python
test_write_restart_performs_the_insert(config, paragraphs)
```

Observed calls (lexical order): `_text`, `config.paragraph`.

### `test_commit_resets_the_commit_counter` - L211-L214

```python
test_commit_resets_the_commit_counter(config, paragraphs)
```

Observed calls (lexical order): `_text`.

### `test_commit_saves_the_counter_and_the_last_record` - L217-L222

```python
test_commit_saves_the_counter_and_the_last_record(config, paragraphs)
```

Observed calls (lexical order): `_text`.

### `test_commit_marks_complete_only_at_eof` - L225-L229

```python
test_commit_marks_complete_only_at_eof(config, paragraphs)
```

Observed calls (lexical order): `_text`.

### `test_commit_uses_the_manual_commit_length` - L232-L234

```python
test_commit_uses_the_manual_commit_length(config, paragraphs)
```

Observed calls (lexical order): `_text`, `str`.

### `test_commit_updates_then_commits` - L237-L244

```python
test_commit_updates_then_commits(config, paragraphs)
```

Observed calls (lexical order): `paragraphs[std.ROLE_COMMIT].executable`, `next`, `enumerate`, `config.paragraph`.

### `test_abend_calls_the_resolved_module` - L251-L253

```python
test_abend_calls_the_resolved_module(config, paragraphs)
```

Observed calls (lexical order): `_text`.

### `test_an_unusable_config_writes_nothing` - L260-L269

```python
test_an_unusable_config_writes_nothing(role)
```

Observed calls (lexical order): `RestartFlowBuilder`, `RestartConfig.build`, `RestartProgramNames`, `builder.build_all`.

### `test_a_role_without_retention_writes_nothing` - L272-L276

```python
test_a_role_without_retention_writes_nothing(role, complete_names)
```

Observed calls (lexical order): `dataclasses.replace`, `RestartConfig.build`, `RestartFlowBuilder`, `builder.build_all`, `any`.

### `test_an_unmeasured_payload_writes_nothing` - L279-L283

```python
test_an_unmeasured_payload_writes_nothing(role, complete_names)
```

Observed calls (lexical order): `dataclasses.replace`, `RestartConfig.build`, `RestartFlowBuilder`, `builder.build_all`, `any`.

### `test_build_by_role_returns_none_when_refused` - L286-L294

```python
test_build_by_role_returns_none_when_refused(role)
```

Observed calls (lexical order): `RestartFlowBuilder`, `RestartConfig.build`, `RestartProgramNames`, `builder.build`.

### `test_building_twice_produces_identical_output` - L301-L304

```python
test_building_twice_produces_identical_output(config)
```

Observed calls (lexical order): `RestartFlowBuilder`, `RestartFlowBuilder(config).build_all`.

### `test_messages_are_reset_between_builds` - L307-L311

```python
test_messages_are_reset_between_builds(builder)
```

Observed calls (lexical order): `builder.build_all`, `len`.

### `test_a_different_scheme_only_renames_paragraphs` - L314-L325

```python
test_a_different_scheme_only_renames_paragraphs(role, complete_names)
```

Observed calls (lexical order): `RestartFlowBuilder`, `RestartFlowBuilder(RestartConfig.build(role, complete_names, std.SCHEME_SEVEN_SERIES)).build_all`, `RestartConfig.build`, `RestartFlowBuilder(RestartConfig.build(role, complete_names, std.SCHEME_EIGHT_SERIES)).build_all`, `zip`, `len`.

Control points:

- L323: `for (a, b) in zip(seven, eight)`

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
