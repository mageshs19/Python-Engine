# `tests/restart/test_m7_process_injector.py`

Source: [tests/restart/test_m7_process_injector.py](../../../../tests/restart/test_m7_process_injector.py) | 309 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `4f93cbe58ac6f8496b49f6fc3079e5f9d88b2330a0871234cfd50988a712765d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> M7 contract tests: the business processing paragraph.

## Module-level bindings

`BUSINESS` (L25), `COMMIT_BLOCK` (L31)

## Import declarations

```python
from __future__ import annotations
import dataclasses
import pytest
from converter.composers.restart.process_paragraph_injector import ProcessParagraphInjector
from converter.generators.restart.restart_config import RestartConfig, RestartProgramNames
from rules import restart_standard_rules as std
```

## Local dependency notes

- [converter/composers/restart/process_paragraph_injector.py](../../converter/composers/restart/process_paragraph_injector.md)
- [converter/generators/restart/restart_config.py](../../converter/generators/restart/restart_config.md)
- [rules/__init__.py](../../rules/__init__.md)
- [rules/restart_standard_rules.py](../../rules/restart_standard_rules.md)

## Symbol contracts and control points

### `injector` - L39-L40

```python
injector(config)
```

Observed calls (lexical order): `ProcessParagraphInjector`.

### `_logical` - L43-L44

```python
_logical(lines)
```

Observed calls (lexical order): `' '.join`, `str`, `str(l).strip`, `str(l).upper`, `str(l).upper().split`.

### `test_the_commit_test_is_appended` - L51-L56

```python
test_the_commit_test_is_appended(config, injector)
```

Observed calls (lexical order): `_logical`, `injector.inject`.

### `test_the_commit_paragraph_is_performed` - L59-L61

```python
test_the_commit_paragraph_is_performed(config, injector)
```

Observed calls (lexical order): `_logical`, `injector.inject`, `config.paragraph`.

### `test_the_tail_read_is_appended` - L64-L66

```python
test_the_tail_read_is_appended(config, injector)
```

Observed calls (lexical order): `_logical`, `injector.inject`.

### `test_the_commit_test_is_closed` - L69-L71

```python
test_the_commit_test_is_closed(injector)
```

Observed calls (lexical order): `_logical`, `injector.inject`.

### `test_the_commit_test_precedes_the_tail_read` - L74-L81

```python
test_the_commit_test_precedes_the_tail_read(config, injector)
```

Observed calls (lexical order): `_logical`, `injector.inject`, `enumerate`, `l.startswith`, `next`.

### `test_the_business_lines_are_preserved` - L84-L87

```python
test_the_business_lines_are_preserved(injector)
```

Observed calls (lexical order): `_logical`, `injector.inject`.

Control points:

- L86: `for line in _logical(BUSINESS)`

### `test_the_business_lines_keep_their_order` - L90-L93

```python
test_the_business_lines_keep_their_order(injector)
```

Observed calls (lexical order): `_logical`, `injector.inject`, `body.index`, `sorted`.

### `test_the_injection_is_reported` - L96-L98

```python
test_the_injection_is_reported(injector)
```

Observed calls (lexical order): `injector.inject`, `any`.

### `test_no_placeholder_survives` - L101-L104

```python
test_no_placeholder_survives(injector)
```

Observed calls (lexical order): `'\n'.join`, `injector.inject`.

### `test_an_orphan_end_if_is_removed` - L111-L113

```python
test_an_orphan_end_if_is_removed(injector)
```

Observed calls (lexical order): `_logical`, `injector.inject`, `body.count`.

### `test_the_orphan_removal_is_reported` - L116-L118

```python
test_the_orphan_removal_is_reported(injector)
```

Observed calls (lexical order): `injector.inject`, `any`.

### `test_a_matched_end_if_is_kept` - L121-L129

```python
test_a_matched_end_if_is_kept(injector)
```

Observed calls (lexical order): `_logical`, `injector.inject`, `body.count`.

### `test_a_one_line_if_is_balanced` - L132-L135

```python
test_a_one_line_if_is_balanced(injector)
```

Observed calls (lexical order): `injector.inject`, `any`.

### `test_an_orphan_end_evaluate_is_removed` - L138-L140

```python
test_an_orphan_end_evaluate_is_removed(injector)
```

Observed calls (lexical order): `_logical`, `injector.inject`.

### `test_a_matched_end_evaluate_is_kept` - L143-L151

```python
test_a_matched_end_evaluate_is_kept(injector)
```

Observed calls (lexical order): `_logical`, `injector.inject`.

### `test_an_untracked_terminator_is_left_alone` - L154-L157

```python
test_an_untracked_terminator_is_left_alone(injector)
```

Observed calls (lexical order): `_logical`, `injector.inject`, `any`.

### `test_the_split_commit_block_is_removed` - L164-L167

```python
test_the_split_commit_block_is_removed(injector)
```

Observed calls (lexical order): `_logical`, `injector.inject`.

### `test_the_one_line_commit_block_is_removed` - L170-L174

```python
test_the_one_line_commit_block_is_removed(injector)
```

Observed calls (lexical order): `_logical`, `injector.inject`.

### `test_the_commit_removal_is_reported` - L177-L179

```python
test_the_commit_removal_is_reported(injector)
```

Observed calls (lexical order): `injector.inject`, `any`.

### `test_business_sql_is_never_removed` - L182-L193

```python
test_business_sql_is_never_removed(injector)
```

Observed calls (lexical order): `_logical`, `injector.inject`, `any`.

Control points:

- L191: `for line in _logical(lines)`

### `test_an_unterminated_exec_block_is_left_alone` - L196-L200

```python
test_an_unterminated_exec_block_is_left_alone(injector)
```

Observed calls (lexical order): `_logical`, `injector.inject`.

### `test_two_commit_blocks_are_both_removed` - L203-L208

```python
test_two_commit_blocks_are_both_removed(injector)
```

Observed calls (lexical order): `_logical`, `injector.inject`, `any`.

### `test_injecting_twice_appends_one_tail` - L215-L218

```python
test_injecting_twice_appends_one_tail(injector)
```

Observed calls (lexical order): `injector.inject`, `_logical`.

### `test_the_second_pass_reports_that_it_did_nothing` - L221-L224

```python
test_the_second_pass_reports_that_it_did_nothing(injector)
```

Observed calls (lexical order): `injector.inject`, `any`.

### `test_a_third_pass_is_still_stable` - L227-L231

```python
test_a_third_pass_is_still_stable(injector)
```

Observed calls (lexical order): `injector.inject`, `_logical`.

### `test_the_generated_shape_is_fully_repaired` - L238-L245

```python
test_the_generated_shape_is_fully_repaired(config, injector)
```

Observed calls (lexical order): `_logical`, `injector.inject`, `body.count`, `config.paragraph`.

### `test_the_repair_reports_every_decision` - L248-L253

```python
test_the_repair_reports_every_decision(injector)
```

Observed calls (lexical order): `injector.inject`, `' '.join`.

### `test_an_unusable_config_changes_nothing` - L260-L265

```python
test_an_unusable_config_changes_nothing(role)
```

Observed calls (lexical order): `ProcessParagraphInjector`, `RestartConfig.build`, `RestartProgramNames`, `injector.inject`.

### `test_a_missing_counter_changes_nothing` - L268-L272

```python
test_a_missing_counter_changes_nothing(role, complete_names)
```

Observed calls (lexical order): `dataclasses.replace`, `ProcessParagraphInjector`, `RestartConfig.build`, `injector.inject`, `any`.

### `test_an_empty_paragraph_is_safe` - L275-L278

```python
test_an_empty_paragraph_is_safe(injector)
```

Observed calls (lexical order): `_logical`, `injector.inject`, `body[-1].startswith`.

### `test_none_is_safe` - L281-L282

```python
test_none_is_safe(injector)
```

Observed calls (lexical order): `injector.inject`.

### `test_messages_are_reset_between_runs` - L289-L293

```python
test_messages_are_reset_between_runs(injector)
```

Observed calls (lexical order): `injector.inject`, `len`.

### `test_the_tail_is_stable` - L296-L297

```python
test_the_tail_is_stable(injector)
```

Observed calls (lexical order): `injector.tail`.

### `test_a_scope_emptied_by_the_commit_removal_is_removed` - L299-L303

```python
test_a_scope_emptied_by_the_commit_removal_is_removed(injector)
```

Observed calls (lexical order): `_logical`, `injector.inject`, `body.count`.

### `test_a_scope_with_a_body_is_never_touched` - L306-L309

```python
test_a_scope_with_a_body_is_never_touched(injector)
```

Observed calls (lexical order): `_logical`, `injector.inject`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
