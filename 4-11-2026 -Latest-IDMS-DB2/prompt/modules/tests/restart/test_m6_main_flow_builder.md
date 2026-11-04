# `tests/restart/test_m6_main_flow_builder.py`

Source: [tests/restart/test_m6_main_flow_builder.py](../../../../tests/restart/test_m6_main_flow_builder.py) | 258 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `557fe7994fc210a4550a153c9baadc0bae149d672b27264755163fcb2f470065`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> M6 contract tests: the mainline.

## Module-level bindings

`TOTALS` (L29)

## Import declarations

```python
from __future__ import annotations
import dataclasses
import pytest
from converter.generators.restart.restart_config import RestartConfig, RestartProgramNames
from converter.generators.restart.restart_main_flow_builder import STOP_RUN, RestartMainFlowBuilder
from rules import restart_standard_rules as std
```

## Local dependency notes

- [converter/generators/restart/restart_config.py](../../converter/generators/restart/restart_config.md)
- [converter/generators/restart/restart_main_flow_builder.py](../../converter/generators/restart/restart_main_flow_builder.md)
- [rules/__init__.py](../../rules/__init__.md)
- [rules/restart_standard_rules.py](../../rules/restart_standard_rules.md)

## Symbol contracts and control points

### `builder` - L36-L37

```python
builder(config)
```

Observed calls (lexical order): `RestartMainFlowBuilder`.

### `body` - L41-L42

```python
body(builder)
```

Observed calls (lexical order): `builder.statements`.

### `_index` - L45-L46

```python
_index(body, marker: str) -> int
```

Observed calls (lexical order): `enumerate`, `next`.

### `test_the_control_paragraph_is_performed` - L53-L54

```python
test_the_control_paragraph_is_performed(config, body)
```

Observed calls (lexical order): `config.paragraph`.

### `test_the_commit_paragraph_is_performed` - L57-L58

```python
test_the_commit_paragraph_is_performed(config, body)
```

Observed calls (lexical order): `config.paragraph`.

### `test_stop_run_is_the_last_statement` - L61-L62

```python
test_stop_run_is_the_last_statement(body)
```

### `test_stop_run_appears_exactly_once` - L65-L66

```python
test_stop_run_appears_exactly_once(body)
```

Observed calls (lexical order): `body.count`.

### `test_the_statement_order_is_fixed` - L73-L80

```python
test_the_statement_order_is_fixed(config, body)
```

Observed calls (lexical order): `_index`, `config.paragraph`.

### `test_control_runs_before_the_first_read` - L83-L87

```python
test_control_runs_before_the_first_read(config, body)
```

A read before repositioning would consume record one twice.

Observed calls (lexical order): `_index`, `config.paragraph`.

### `test_close_is_the_statement_before_stop_run` - L90-L91

```python
test_close_is_the_statement_before_stop_run(config, body)
```

### `test_the_file_is_opened_and_closed_once` - L94-L98

```python
test_the_file_is_opened_and_closed_once(config, body)
```

Observed calls (lexical order): `l.startswith`.

### `test_the_loop_drives_the_business_paragraph` - L105-L110

```python
test_the_loop_drives_the_business_paragraph(config, body)
```

### `test_the_loop_uses_the_88_level_not_a_literal` - L113-L118

```python
test_the_loop_uses_the_88_level_not_a_literal(config, body)
```

IF SW-EOF = 'Y' was the shape the manual replaced.

Observed calls (lexical order): `next`.

### `test_the_first_read_is_unconditional` - L121-L125

```python
test_the_first_read_is_unconditional(config, body)
```

The generated mainline wrapped it in an IF that could never fire.

Observed calls (lexical order): `any`, `l.startswith`.

### `test_no_totals_are_authored_by_default` - L132-L133

```python
test_no_totals_are_authored_by_default(builder)
```

Observed calls (lexical order): `any`, `builder.statements`.

### `test_supplied_totals_are_spliced_before_close` - L136-L140

```python
test_supplied_totals_are_spliced_before_close(config, builder)
```

Observed calls (lexical order): `builder.statements`, `_index`.

Control points:

- L138: `for line in TOTALS`

### `test_supplied_totals_are_spliced_after_the_commit` - L143-L146

```python
test_supplied_totals_are_spliced_after_the_commit(config, builder)
```

Observed calls (lexical order): `builder.statements`, `_index`, `config.paragraph`.

### `test_supplied_totals_are_unchanged` - L149-L151

```python
test_supplied_totals_are_unchanged(builder)
```

Observed calls (lexical order): `builder.statements`, `l.startswith`, `list`.

### `test_the_totals_decision_is_reported` - L154-L158

```python
test_the_totals_decision_is_reported(builder)
```

Observed calls (lexical order): `builder.build`, `any`.

### `test_no_placeholder_survives` - L165-L168

```python
test_no_placeholder_survives(builder)
```

Observed calls (lexical order): `'\n'.join`, `builder.build`.

### `test_every_statement_closes_its_sentence` - L171-L173

```python
test_every_statement_closes_its_sentence(body)
```

Observed calls (lexical order): `line.endswith`.

Control points:

- L172: `for line in body`

### `test_blank_separators_are_present_in_the_raw_build` - L176-L178

```python
test_blank_separators_are_present_in_the_raw_build(builder)
```

Readability is part of the manual reference layout.

Observed calls (lexical order): `any`, `builder.build`.

### `test_an_unusable_config_builds_nothing` - L185-L190

```python
test_an_unusable_config_builds_nothing(role)
```

Observed calls (lexical order): `RestartMainFlowBuilder`, `RestartConfig.build`, `RestartProgramNames`, `builder.build`.

### `test_a_role_without_retention_builds_nothing` - L193-L197

```python
test_a_role_without_retention_builds_nothing(role, complete_names)
```

Observed calls (lexical order): `dataclasses.replace`, `RestartConfig.build`, `RestartMainFlowBuilder`, `builder.build`, `any`.

### `test_an_unmeasured_payload_builds_nothing` - L200-L204

```python
test_an_unmeasured_payload_builds_nothing(role, complete_names)
```

Observed calls (lexical order): `dataclasses.replace`, `RestartConfig.build`, `RestartMainFlowBuilder`, `builder.build`, `any`.

### `test_a_missing_process_paragraph_builds_nothing` - L207-L211

```python
test_a_missing_process_paragraph_builds_nothing(role, complete_names)
```

Observed calls (lexical order): `dataclasses.replace`, `RestartConfig.build`, `RestartMainFlowBuilder`, `builder.build`, `any`.

### `test_building_twice_produces_identical_output` - L218-L221

```python
test_building_twice_produces_identical_output(config)
```

Observed calls (lexical order): `RestartMainFlowBuilder`, `RestartMainFlowBuilder(config).build`.

### `test_messages_are_reset_between_builds` - L224-L228

```python
test_messages_are_reset_between_builds(builder)
```

Observed calls (lexical order): `builder.build`, `len`.

### `test_a_different_scheme_changes_only_the_performed_names` - L231-L243

```python
test_a_different_scheme_changes_only_the_performed_names(role, complete_names)
```

Observed calls (lexical order): `RestartMainFlowBuilder`, `RestartMainFlowBuilder(RestartConfig.build(role, complete_names, std.SCHEME_SEVEN_SERIES)).statements`, `RestartConfig.build`, `RestartMainFlowBuilder(RestartConfig.build(role, complete_names, std.SCHEME_EIGHT_SERIES)).statements`, `len`.

### `test_the_mainline_performs_only_resolved_paragraphs` - L246-L258

```python
test_the_mainline_performs_only_resolved_paragraphs(config, body)
```

Observed calls (lexical order): `line.split`, `line.split()[1].rstrip`, `line.startswith`, `config.paragraph`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
