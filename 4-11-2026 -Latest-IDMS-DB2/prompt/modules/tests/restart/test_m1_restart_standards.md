# `tests/restart/test_m1_restart_standards.py`

Source: [tests/restart/test_m1_restart_standards.py](../../../../tests/restart/test_m1_restart_standards.py) | 403 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `eee4e4e42109b35d4ecd7ea378fa074b3d67d78b2d8f78679c8d653fcee40a26`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> M1 contract tests: the standards layer holds shape, not names.

## Module-level bindings

`RULES_MODULES` (L46), `PLACEHOLDER` (L175), `ALL_TEMPLATES` (L177)

## Import declarations

```python
from __future__ import annotations
import ast
import inspect
import re
import pytest
from patterns import restart_patterns as pat
from rules import restart_standard_rules as std
from rules import restart_statement_templates as tpl
```

## Local dependency notes

- [patterns/__init__.py](../../patterns/__init__.md)
- [patterns/restart_patterns.py](../../patterns/restart_patterns.md)
- [rules/__init__.py](../../rules/__init__.md)
- [rules/restart_standard_rules.py](../../rules/restart_standard_rules.md)
- [rules/restart_statement_templates.py](../../rules/restart_statement_templates.md)

## Symbol contracts and control points

### `test_rules_modules_define_no_regex` - L54-L58

```python
test_rules_modules_define_no_regex(module)
```

rules/ is constants only. Regex belongs in patterns/.

Observed calls (lexical order): `inspect.getsource`.

### `test_modules_declare_all` - L62-L68

```python
test_modules_declare_all(module)
```

A duplicated export hides the name that was meant to be added.

Observed calls (lexical order): `getattr`, `isinstance`, `sorted`, `len`, `set`, `hasattr`.

Control points:

- L67: `for name in module.__all__`

### `test_no_constant_assigned_twice` - L72-L86

```python
test_no_constant_assigned_twice(module)
```

A second assignment silently overrides the reviewed value.

Observed calls (lexical order): `ast.parse`, `inspect.getsource`, `set`, `isinstance`, `duplicates.append`, `seen.add`.

Control points:

- L77: `for node in tree.body`
- L78: `if not isinstance(node, ast.Assign)`
- L80: `for target in node.targets`
- L81: `if not isinstance(target, ast.Name)`
- L83: `if target.id in seen`

### `test_patterns_module_defines_no_business_constants` - L89-L92

```python
test_patterns_module_defines_no_business_constants()
```

Observed calls (lexical order): `inspect.getsource`.

### `test_the_standards_layer_owns_no_retention_value` - L99-L103

```python
test_the_standards_layer_owns_no_retention_value()
```

The retention column is site data, supplied with the role.

Observed calls (lexical order): `inspect.getsource`.

### `test_the_standards_layer_owns_no_payload_length` - L106-L111

```python
test_the_standards_layer_owns_no_payload_length()
```

The length is measured from the source, never declared here.

Observed calls (lexical order): `inspect.getsource`.

### `test_status_values_are_distinct_single_characters` - L118-L121

```python
test_status_values_are_distinct_single_characters()
```

Observed calls (lexical order): `len`.

### `test_commit_threshold_fires_on_the_frequency_record` - L124-L125

```python
test_commit_threshold_fires_on_the_frequency_record()
```

### `test_restart_is_update_only` - L128-L130

```python
test_restart_is_update_only()
```

### `test_sqlcode_routing_values` - L133-L135

```python
test_sqlcode_routing_values()
```

### `test_sql_location_is_never_restated_in_the_error_branch` - L138-L140

```python
test_sql_location_is_never_restated_in_the_error_branch()
```

The reference writes it once, at paragraph entry.

### `test_the_commit_length_flag_defaults_to_the_manual` - L143-L148

```python
test_the_commit_length_flag_defaults_to_the_manual()
```

The reference writes the COUNTER length on commit, not the full payload. This asserts the POLICY VALUE; the behaviour that reads it is asserted by the config suite. One statement of intent, one place.

### `test_every_scheme_covers_every_role` - L155-L157

```python
test_every_scheme_covers_every_role()
```

Observed calls (lexical order): `std.PARAGRAPH_NUMBER_SCHEMES.items`, `set`.

Control points:

- L156: `for (scheme, mapping) in std.PARAGRAPH_NUMBER_SCHEMES.items()`

### `test_default_scheme_exists` - L160-L161

```python
test_default_scheme_exists()
```

### `test_every_scheme_number_is_covered_by_a_skip_prefix` - L164-L168

```python
test_every_scheme_number_is_covered_by_a_skip_prefix()
```

Observed calls (lexical order): `set`, `std.PARAGRAPH_NUMBER_SCHEMES.values`, `mapping.values`.

Control points:

- L166: `for mapping in std.PARAGRAPH_NUMBER_SCHEMES.values()`
- L167: `for number in mapping.values()`

### `test_templates_are_tuples_of_strings` - L190-L192

```python
test_templates_are_tuples_of_strings(template)
```

Observed calls (lexical order): `isinstance`, `all`.

### `test_templates_carry_no_hardcoded_names` - L196-L201

```python
test_templates_carry_no_hardcoded_names(template)
```

No DCLGEN group, table, program or host variable may appear.

Observed calls (lexical order): `' '.join`, `' '.join(template).upper`.

Control points:

- L199: `for token in ('DCLDZ', 'DZ01RST', 'DZBFAR', 'VMDZ', 'WS-TELLER', 'WS-NB-', 'VMDZ205I', 'OPERATIES')`

### `test_placeholders_are_snake_case` - L205-L208

```python
test_placeholders_are_snake_case(template)
```

Observed calls (lexical order): `PLACEHOLDER.finditer`, `match.group`, `match.group('name').islower`.

Control points:

- L206: `for line in template`
- L207: `for match in PLACEHOLDER.finditer(line)`

### `test_main_flow_order_is_fixed` - L211-L220

```python
test_main_flow_order_is_fixed()
```

Observed calls (lexical order): `body[0].startswith`, `body[-2].startswith`, `enumerate`, `next`.

### `test_restart_found_blocks_a_completed_run` - L223-L239

```python
test_restart_found_blocks_a_completed_run()
```

Token PRESENCE only.

Observed calls (lexical order): `' '.join`.

### `test_write_restart_initialises_the_key_and_zeroes_the_counter` - L242-L246

```python
test_write_restart_initialises_the_key_and_zeroes_the_counter()
```

Observed calls (lexical order): `' '.join`.

### `test_commit_saves_counter_and_key_before_updating` - L249-L255

```python
test_commit_saves_counter_and_key_before_updating()
```

Observed calls (lexical order): `enumerate`, `next`.

### `test_read_paragraph_increments_both_counters` - L258-L262

```python
test_read_paragraph_increments_both_counters()
```

Observed calls (lexical order): `' '.join`.

### `test_no_template_line_renders_into_area_a` - L265-L289

```python
test_no_template_line_renders_into_area_a() -> None
```

A continuation line's leading spaces are an ABSOLUTE offset from column 8. Two spaces put the body at column 10, inside Area A, and CHK-06.06 reported six such lines on a generated program.

Observed calls (lexical order): `getattr`, `isinstance`, `line.startswith`, `len`, `line.lstrip`, `offenders.append`, `'\n'.join`.

Control points:

- L276: `for name in tpl.__all__`
- L278: `if not isinstance(template, tuple)`
- L280: `for line in template`
- L281: `if not line or not line.startswith(' ')`
- L284: `if indent < floor`

### `test_open_input_captures_the_file_name` - L296-L299

```python
test_open_input_captures_the_file_name()
```

Observed calls (lexical order): `pat.OPEN_INPUT_PATTERN.match`, `pat.OPEN_INPUT_PATTERN.match('OPEN INPUT OPERATIES.').group`.

### `test_perform_until_captures_paragraph_and_condition` - L302-L307

```python
test_perform_until_captures_paragraph_and_condition()
```

Observed calls (lexical order): `pat.PERFORM_UNTIL_PATTERN.match`, `match.group`.

### `test_perform_until_supports_the_span_form` - L310-L314

```python
test_perform_until_supports_the_span_form()
```

Observed calls (lexical order): `pat.PERFORM_UNTIL_PATTERN.match`, `match.group`.

### `test_read_into_captures_file_and_record` - L317-L320

```python
test_read_into_captures_file_and_record()
```

Observed calls (lexical order): `pat.READ_INTO_PATTERN.match`, `match.group`.

### `test_level_88_captures_name_and_value` - L323-L326

```python
test_level_88_captures_name_and_value()
```

Observed calls (lexical order): `pat.LEVEL_88_PATTERN.match`, `match.group`.

### `test_the_77_picture_pattern_actually_matches` - L329-L337

```python
test_the_77_picture_pattern_actually_matches()
```

It once read X$8$, where the dollar sign is an anchor.

Observed calls (lexical order): `pat.LEVEL_77_WITH_VALUE_PATTERN.match`, `match.group`.

### `test_picture_size_is_measured` - L349-L350

```python
test_picture_size_is_measured(clause, size)
```

Observed calls (lexical order): `pat.PICTURE_SIZE_PATTERN.match`, `pat.PICTURE_SIZE_PATTERN.match(clause).group`.

### `test_a_picture_without_a_repeat_has_no_size` - L353-L354

```python
test_a_picture_without_a_repeat_has_no_size()
```

Observed calls (lexical order): `pat.PICTURE_SIZE_PATTERN.match`.

### `test_elementary_item_captures_name_and_picture` - L357-L360

```python
test_elementary_item_captures_name_and_picture()
```

Observed calls (lexical order): `pat.ELEMENTARY_ITEM_PATTERN.match`, `match.group`, `match.group('picture').startswith`.

### `test_the_paragraph_number_is_captured` - L363-L366

```python
test_the_paragraph_number_is_captured()
```

Observed calls (lexical order): `pat.PARAGRAPH_NUMBER_PATTERN.match`, `pat.PARAGRAPH_NUMBER_PATTERN.match('700-SELECT-DZ01RSTV').group`.

### `test_a_paragraph_without_a_number_has_none` - L369-L370

```python
test_a_paragraph_without_a_number_has_none()
```

Observed calls (lexical order): `pat.PARAGRAPH_NUMBER_PATTERN.match`.

### `test_the_include_pattern_accepts_both_shapes` - L380-L381

```python
test_the_include_pattern_accepts_both_shapes(line)
```

Observed calls (lexical order): `pat.SQL_INCLUDE_PATTERN.match`, `pat.SQL_INCLUDE_PATTERN.match(line).group`.

### `test_double_period_is_detected` - L384-L386

```python
test_double_period_is_detected()
```

Observed calls (lexical order): `pat.DOUBLE_PERIOD_PATTERN.search`.

### `test_trailing_sequence_leak_is_detected` - L389-L393

```python
test_trailing_sequence_leak_is_detected()
```

Observed calls (lexical order): `pat.TRAILING_SEQUENCE_LEAK_PATTERN.search`, `match.group`.

### `test_orphan_scope_terminator_is_detected` - L396-L398

```python
test_orphan_scope_terminator_is_detected()
```

Observed calls (lexical order): `pat.ORPHAN_SCOPE_TERMINATOR_PATTERN.match`.

### `test_paragraph_header_rejects_a_statement` - L401-L403

```python
test_paragraph_header_rejects_a_statement()
```

Observed calls (lexical order): `pat.PARAGRAPH_HEADER_PATTERN.match`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
