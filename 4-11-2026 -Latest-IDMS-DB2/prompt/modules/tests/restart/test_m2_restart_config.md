# `tests/restart/test_m2_restart_config.py`

Source: [tests/restart/test_m2_restart_config.py](../../../../tests/restart/test_m2_restart_config.py) | 271 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `c6a349b83c59b1cfcd656d2628f943a7540f43c97d60cd5fe7b8bf9ead464e1c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> M2 contract tests: config renders names, never invents them.

## Module-level bindings

`PLACEHOLDER` (L22), `ALL_TEMPLATES` (L24)

## Import declarations

```python
from __future__ import annotations
import dataclasses
import re
import pytest
from catalogs import restart_paragraph_catalog as cat
from converter.generators.restart import restart_config as config_module
from converter.generators.restart.restart_config import RestartConfig, RestartProgramNames, build_paragraph_names
from rules import restart_standard_rules as std
from rules import restart_statement_templates as tpl
import rules.restart_standard_rules as std
```

## Local dependency notes

- [catalogs/__init__.py](../../catalogs/__init__.md)
- [catalogs/restart_paragraph_catalog.py](../../catalogs/restart_paragraph_catalog.md)
- [converter/generators/restart/__init__.py](../../converter/generators/restart/__init__.md)
- [converter/generators/restart/restart_config.py](../../converter/generators/restart/restart_config.md)
- [rules/__init__.py](../../rules/__init__.md)
- [rules/restart_standard_rules.py](../../rules/restart_standard_rules.md)
- [rules/restart_statement_templates.py](../../rules/restart_statement_templates.md)

## Symbol contracts and control points

### `_template_placeholders` - L36-L41

```python
_template_placeholders() -> set[str]
```

Observed calls (lexical order): `set`, `PLACEHOLDER.finditer`, `m.group`, `names.update`.

Control points:

- L38: `for template in ALL_TEMPLATES`
- L39: `for line in template`

### `_render` - L44-L46

```python
_render(template, config) -> list[str]
```

Observed calls (lexical order): `config.placeholders`, `line.format`.

### `test_config_supplies_every_template_placeholder` - L53-L55

```python
test_config_supplies_every_template_placeholder(config)
```

Observed calls (lexical order): `_template_placeholders`, `config.placeholders`, `set`.

### `test_every_template_renders_without_keyerror` - L58-L62

```python
test_every_template_renders_without_keyerror(config)
```

Observed calls (lexical order): `config.placeholders`, `line.format`.

Control points:

- L60: `for template in ALL_TEMPLATES`
- L61: `for line in template`

### `test_rendered_output_contains_no_leftover_placeholder` - L65-L70

```python
test_rendered_output_contains_no_leftover_placeholder(config)
```

Observed calls (lexical order): `config.placeholders`, `'\n'.join`, `line.format`.

Control points:

- L67: `for template in ALL_TEMPLATES`

### `test_config_is_frozen` - L77-L79

```python
test_config_is_frozen(config)
```

Observed calls (lexical order): `pytest.raises`.

### `test_names_are_frozen` - L82-L84

```python
test_names_are_frozen(complete_names)
```

Observed calls (lexical order): `pytest.raises`.

### `test_with_names_returns_a_new_object` - L87-L92

```python
test_with_names_returns_a_new_object(config, complete_names)
```

Observed calls (lexical order): `dataclasses.replace`, `config.with_names`.

### `test_both_schemes_produce_a_name_for_every_role` - L99-L103

```python
test_both_schemes_produce_a_name_for_every_role(role)
```

Observed calls (lexical order): `build_paragraph_names`, `set`, `all`, `names.values`.

Control points:

- L100: `for scheme in std.PARAGRAPH_NUMBER_SCHEMES`

### `test_paragraph_names_are_unique_within_a_scheme` - L106-L109

```python
test_paragraph_names_are_unique_within_a_scheme(role)
```

Observed calls (lexical order): `build_paragraph_names`, `len`, `names.values`, `set`.

Control points:

- L107: `for scheme in std.PARAGRAPH_NUMBER_SCHEMES`

### `test_sql_paragraphs_carry_the_restart_table_name` - L112-L115

```python
test_sql_paragraphs_carry_the_restart_table_name(role)
```

Observed calls (lexical order): `build_paragraph_names`, `names[role_key].endswith`.

Control points:

- L114: `for role_key in cat.TABLE_SUFFIXED_ROLES`

### `test_non_sql_paragraphs_do_not_carry_the_table_name` - L118-L123

```python
test_non_sql_paragraphs_do_not_carry_the_table_name(role)
```

Observed calls (lexical order): `build_paragraph_names`.

Control points:

- L120: `for role_key in std.RESTART_PARAGRAPH_ROLES`
- L121: `if role_key in cat.TABLE_SUFFIXED_ROLES`

### `test_every_paragraph_name_is_a_valid_cobol_name` - L126-L130

```python
test_every_paragraph_name_is_a_valid_cobol_name(role)
```

Observed calls (lexical order): `re.compile`, `build_paragraph_names`, `build_paragraph_names(role, scheme).values`, `valid.match`.

Control points:

- L128: `for scheme in std.PARAGRAPH_NUMBER_SCHEMES`
- L129: `for name in build_paragraph_names(role, scheme).values()`

### `test_switching_scheme_changes_only_the_numbers` - L133-L143

```python
test_switching_scheme_changes_only_the_numbers(role, complete_names)
```

Observed calls (lexical order): `RestartConfig.build`, `seven.paragraph`, `suffix`, `eight.paragraph`.

Control points:

- L140: `for role_key in std.RESTART_PARAGRAPH_ROLES`

### `test_switching_scheme_changes_only_the_numbers.suffix` - L137-L138

```python
suffix(name: str) -> str
```

Observed calls (lexical order): `name.split`.

### `test_an_unknown_scheme_is_refused` - L146-L148

```python
test_an_unknown_scheme_is_refused(role, complete_names)
```

Observed calls (lexical order): `pytest.raises`, `RestartConfig.build`.

### `test_restart_querynos_are_distinct` - L155-L161

```python
test_restart_querynos_are_distinct(config)
```

Observed calls (lexical order): `len`, `set`.

### `test_the_payload_length_is_measured_not_declared` - L168-L172

```python
test_the_payload_length_is_measured_not_declared(config)
```

### `test_commit_length_follows_the_manual_by_default` - L175-L177

```python
test_commit_length_follows_the_manual_by_default(config)
```

### `test_the_full_length_flag_is_honoured` - L180-L184

```python
test_the_full_length_flag_is_honoured(config, monkeypatch)
```

Observed calls (lexical order): `monkeypatch.setattr`.

### `test_a_shorter_restart_key_produces_a_shorter_length` - L187-L192

```python
test_a_shorter_restart_key_produces_a_shorter_length(role, complete_names)
```

1215 was never a constant; it is this program's measurement.

Observed calls (lexical order): `dataclasses.replace`, `RestartConfig.build`.

### `test_an_unmeasured_payload_is_refused` - L195-L199

```python
test_an_unmeasured_payload_is_refused(role, complete_names)
```

Observed calls (lexical order): `dataclasses.replace`, `RestartConfig.build`, `config.is_usable`, `config.missing`.

### `test_retention_comes_from_the_role` - L206-L208

```python
test_retention_comes_from_the_role(config)
```

### `test_a_role_without_retention_is_refused` - L211-L213

```python
test_a_role_without_retention_is_refused(role, complete_names)
```

Observed calls (lexical order): `dataclasses.replace`, `RestartConfig.build`, `RestartConfig.build(bare, complete_names).is_usable`.

### `test_an_empty_name_is_reported_as_missing` - L220-L225

```python
test_an_empty_name_is_reported_as_missing()
```

Observed calls (lexical order): `RestartProgramNames`, `names.missing`, `names.is_complete`.

### `test_a_complete_name_set_reports_nothing_missing` - L228-L230

```python
test_a_complete_name_set_reports_nothing_missing(complete_names)
```

Observed calls (lexical order): `complete_names.missing`, `complete_names.is_complete`.

### `test_a_config_with_missing_names_is_not_usable` - L233-L236

```python
test_a_config_with_missing_names_is_not_usable(role)
```

Observed calls (lexical order): `RestartConfig.build`, `RestartProgramNames`, `config.is_usable`, `config.missing`, `len`.

### `test_whitespace_only_counts_as_missing` - L239-L241

```python
test_whitespace_only_counts_as_missing()
```

Observed calls (lexical order): `RestartProgramNames`, `names.missing`.

### `test_a_zero_size_counts_as_missing` - L244-L246

```python
test_a_zero_size_counts_as_missing()
```

Observed calls (lexical order): `RestartProgramNames`, `names.missing`.

### `test_control_routes_sqlcode_to_the_right_paragraphs` - L253-L256

```python
test_control_routes_sqlcode_to_the_right_paragraphs(config)
```

Observed calls (lexical order): `' '.join`, `_render`.

### `test_payload_length_is_never_invented` - L260-L265

```python
test_payload_length_is_never_invented(config) -> None
```

Either the full measurement, or the read-count picture. Nothing else.

### `test_the_full_payload_flag_decides_both_lengths` - L268-L271

```python
test_the_full_payload_flag_decides_both_lengths() -> None
```

The flag is the single decision point for the whole family.

Observed calls (lexical order): `isinstance`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
