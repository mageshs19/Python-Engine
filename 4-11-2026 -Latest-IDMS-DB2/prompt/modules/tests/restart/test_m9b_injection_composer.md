# `tests/restart/test_m9b_injection_composer.py`

Source: [tests/restart/test_m9b_injection_composer.py](../../../../tests/restart/test_m9b_injection_composer.py) | 359 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `9554f4a5290bd8153398acab94607aa6439c432717b283d714e24e0f4a9214df`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> M9b - RestartInjectionComposer.

## Module-level bindings

`TOTALS` (L57), `HEADER` (L59), `PERFORM` (L60), `PERFORM_KEYWORDS` (L61), `INCLUDE_TEMPLATE` (L62), `WORKING_STORAGE` (L63)

## Import declarations

```python
from __future__ import annotations
import dataclasses
import re
import types
import pytest
import converter.composers.restart.restart_injection_composer as module
from converter.composers.restart.restart_injection_composer import NON_PARAGRAPH_WORDS, PROGRAM_KIND_RETRIEVAL, RestartInjectionComposer
from converter.generators.restart.restart_config import RestartConfig
from converter.generators.restart.restart_name_resolver import RestartNameResolver
from rules.restart_standard_rules import NOT_APPLICABLE_REASONS, RESTART_PARAGRAPH_ROLES, ROLE_COMMIT, ROLE_CONTROL
```

## Local dependency notes

- [converter/composers/restart/restart_injection_composer.py](../../converter/composers/restart/restart_injection_composer.md)
- [converter/generators/restart/restart_config.py](../../converter/generators/restart/restart_config.md)
- [converter/generators/restart/restart_name_resolver.py](../../converter/generators/restart/restart_name_resolver.md)
- [rules/restart_standard_rules.py](../../rules/restart_standard_rules.md)

## Symbol contracts and control points

### `prepared_lines` - L70-L86

```python
prepared_lines(source_lines, role)
```

The fixture program, guaranteed to reference the restart table.

Observed calls (lexical order): `str`, `str(role.table_name).upper`, `any`, `str(line).upper`, `list`, `enumerate`, `INCLUDE_TEMPLATE.format`, `out.insert`.

Control points:

- L78: `if any((table in str(line).upper() for line in source_lines))`
- L82: `for (index, line) in enumerate(out)`
- L83: `if WORKING_STORAGE in str(line).upper()`

### `source_text` - L90-L91

```python
source_text(prepared_lines)
```

Observed calls (lexical order): `'\n'.join`.

### `composer` - L95-L96

```python
composer(line_utils)
```

Observed calls (lexical order): `RestartInjectionComposer`.

### `resolved` - L100-L102

```python
resolved(line_utils, prepared_lines, role)
```

Observed calls (lexical order): `RestartNameResolver`, `RestartNameResolver(line_utils).resolve`, `RestartConfig.build`.

### `output` - L106-L108

```python
output(composer, source_text, role)
```

Observed calls (lexical order): `composer.compose`.

### `_logical` - L111-L118

```python
_logical(line_utils, text)
```

Observed calls (lexical order): `str`, `str(text).splitlines`, `line_utils.logical`, `str(line_utils.logical(raw) or '').strip`, `line_utils.is_comment`, `' '.join`, `body.upper`, `body.upper().split`, `out.append`.

Control points:

- L113: `for raw in str(text).splitlines()`
- L115: `if not body or line_utils.is_comment(body)`

### `_headers` - L121-L128

```python
_headers(line_utils, text)
```

Headers as the COMPOSER defines them - one vocabulary, one truth.

Observed calls (lexical order): `_logical`, `HEADER.match`, `match.group`, `match.group('name').upper`, `names.append`.

Control points:

- L124: `for body in _logical(line_utils, text)`
- L126: `if match and match.group('name').upper() not in NON_PARAGRAPH_WORDS`

### `_family` - L131-L132

```python
_family(config)
```

Observed calls (lexical order): `config.paragraph`, `config.paragraph(role).upper`.

### `test_every_restart_paragraph_is_declared_once` - L138-L141

```python
test_every_restart_paragraph_is_declared_once(line_utils, output, resolved)
```

Observed calls (lexical order): `_headers`, `_family`, `headers.count`.

Control points:

- L140: `for name in _family(resolved)`

### `test_the_family_is_spliced_in_role_order` - L144-L147

```python
test_the_family_is_spliced_in_role_order(line_utils, output, resolved)
```

Observed calls (lexical order): `_family`, `_headers`.

### `test_no_paragraph_header_is_duplicated` - L150-L152

```python
test_no_paragraph_header_is_duplicated(line_utils, output)
```

Observed calls (lexical order): `_headers`, `len`, `set`.

### `test_a_scope_terminator_is_not_classified_as_a_paragraph` - L159-L163

```python
test_a_scope_terminator_is_not_classified_as_a_paragraph(word)
```

END-EXEC. is a REAL line - it closes an SQL block. The contract is that it is never treated as a header, not that it is absent.

Observed calls (lexical order): `RestartInjectionComposer._is_not_a_paragraph`.

### `test_a_real_paragraph_name_is_never_excluded` - L166-L170

```python
test_a_real_paragraph_name_is_never_excluded()
```

Guards the next 'fix': a startswith('END-') rule would silently swallow a legitimate paragraph and truncate its span.

Observed calls (lexical order): `RestartInjectionComposer._is_not_a_paragraph`.

### `test_the_sql_block_terminator_survives_in_the_output` - L173-L177

```python
test_the_sql_block_terminator_survives_in_the_output(line_utils, output)
```

The proof the span was not cut: END-EXEC. is still there, and the paragraph that owns it is still whole.

Observed calls (lexical order): `_logical`, `any`, `line.startswith`.

### `test_the_control_paragraph_is_performed` - L179-L182

```python
test_the_control_paragraph_is_performed(line_utils, output, resolved)
```

Observed calls (lexical order): `_logical`, `resolved.paragraph`, `any`, `line.startswith`.

### `test_the_commit_paragraph_is_performed` - L185-L188

```python
test_the_commit_paragraph_is_performed(line_utils, output, resolved)
```

Observed calls (lexical order): `_logical`, `resolved.paragraph`, `any`, `line.startswith`.

### `test_stop_run_is_written_exactly_once` - L191-L193

```python
test_stop_run_is_written_exactly_once(line_utils, output)
```

Observed calls (lexical order): `_logical`, `len`, `line.startswith`.

### `test_stop_run_closes_the_mainline` - L196-L201

```python
test_stop_run_closes_the_mainline(line_utils, output)
```

Fall-through into the restart family is the defect M6 closed.

Observed calls (lexical order): `_logical`, `enumerate`, `line.startswith`, `next`, `len`, `HEADER.match`.

### `test_every_perform_resolves_to_a_declared_paragraph` - L204-L216

```python
test_every_perform_resolves_to_a_declared_paragraph(line_utils, output, resolved)
```

Observed calls (lexical order): `_headers`, `set`, `str`, `str(resolved.names.error_paragraph or '').upper`, `_logical`, `PERFORM.match`, `match.group`, `match.group('name').upper`.

Control points:

- L209: `for line in _logical(line_utils, output)`
- L211: `if not match`
- L214: `if target in exempt or target in PERFORM_KEYWORDS`

### `test_the_supplied_totals_reach_the_output` - L219-L220

```python
test_the_supplied_totals_reach_the_output(output)
```

Observed calls (lexical order): `TOTALS[0].strip`.

### `test_the_run_is_reported` - L223-L225

```python
test_the_run_is_reported(composer, source_text, role)
```

Observed calls (lexical order): `composer.compose`, `any`.

### `test_the_legacy_cleanup_is_given_the_config` - L228-L244

```python
test_the_legacy_cleanup_is_given_the_config(monkeypatch, line_utils, source_text, role)
```

Pins the collaborator contract that an earlier cut guessed.

Observed calls (lexical order): `monkeypatch.setattr`, `RestartInjectionComposer`, `RestartInjectionComposer(line_utils).compose`, `seen['config'].is_usable`.

### `test_the_legacy_cleanup_is_given_the_config._Spy` - L235-L238

```python
class _Spy(real)
```

### `test_the_legacy_cleanup_is_given_the_config._Spy.__init__` - L236-L238

```python
__init__(self, config, line_utils)
```

Observed calls (lexical order): `super`, `super().__init__`.

### `test_a_retrieval_program_is_returned_unchanged` - L250-L255

```python
test_a_retrieval_program_is_returned_unchanged(composer, source_text, role)
```

Observed calls (lexical order): `composer.compose`, `any`.

### `test_a_missing_role_is_refused` - L258-L262

```python
test_a_missing_role_is_refused(composer, source_text)
```

How the pipeline says 'this is not a restart program'.

Observed calls (lexical order): `composer.compose`, `any`.

### `test_a_role_with_no_token_falls_back_to_the_text` - L265-L280

```python
test_a_role_with_no_token_falls_back_to_the_text(composer, prepared_lines, role)
```

A role carrying no restart-table token cannot establish applicability, so the text scan decides - and refuses.

Observed calls (lexical order): `str`, `str(role.table_name).upper`, `'\n'.join`, `str(line).upper`, `types.SimpleNamespace`, `composer.compose`, `any`.

### `test_a_resolved_role_overrides_a_missing_text_reference` - L283-L297

```python
test_a_resolved_role_overrides_a_missing_text_reference(composer, prepared_lines, role)
```

The fix. The role is the authority; the text has not been written yet. The decision is reported, never silent.

Observed calls (lexical order): `str`, `str(role.table_name).upper`, `'\n'.join`, `str(line).upper`, `composer.compose`, `any`.

### `test_an_unusable_config_leaves_the_source_untouched` - L300-L315

```python
test_an_unusable_config_leaves_the_source_untouched(composer, prepared_lines, role)
```

Cripple a PROGRAM-owned name.

Observed calls (lexical order): `'\n'.join`, `str`, `composer.compose`, `any`.

### `test_a_role_without_retention_emits_no_paragraph` - L318-L324

```python
test_a_role_without_retention_emits_no_paragraph(composer, source_text, role)
```

Observed calls (lexical order): `dataclasses.replace`, `composer.compose`, `any`.

### `test_initialisation_before_open_input_survives` - L327-L350

```python
test_initialisation_before_open_input_survives(composer, prepared_lines, role)
```

The flow template begins at OPEN INPUT.

Observed calls (lexical order): `str`, `str(line).upper`, `seeded.append`, `composer.compose`, `'\n'.join`, `any`.

Control points:

- L339: `for line in prepared_lines`
- L340: `if not placed and 'OPEN INPUT' in str(line).upper()`

### `test_the_flow_still_starts_at_open_input` - L353-L359

```python
test_the_flow_still_starts_at_open_input(composer, line_utils, source_text, role)
```

Preserving the prefix must not duplicate the OPEN.

Observed calls (lexical order): `composer.compose`, `_logical`, `l.startswith`, `len`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
