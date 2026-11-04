# `tests/restart/test_m4_sql_builder.py`

Source: [tests/restart/test_m4_sql_builder.py](../../../../tests/restart/test_m4_sql_builder.py) | 503 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `623db134e88fc2ae0370eec3781395b1628e4297839953d2f3653933af801eba`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> M4 contract tests: the three restart SQL paragraphs.

## Import declarations

```python
from __future__ import annotations
import ast
import dataclasses
import inspect
import pytest
from catalogs import restart_paragraph_catalog as cat
from converter.generators.restart import restart_sql_builder as builder_module
from converter.generators.restart.restart_sql_builder import RestartSqlBuilder, SqlParagraph, VERB_INSERT, VERB_SELECT, VERB_UPDATE
from rules import restart_sql_templates as sqltpl
from rules import restart_standard_rules as std
from converter.generators.restart.restart_config import RestartConfig
```

## Local dependency notes

- [catalogs/__init__.py](../../catalogs/__init__.md)
- [catalogs/restart_paragraph_catalog.py](../../catalogs/restart_paragraph_catalog.md)
- [converter/generators/restart/__init__.py](../../converter/generators/restart/__init__.md)
- [converter/generators/restart/restart_config.py](../../converter/generators/restart/restart_config.md)
- [converter/generators/restart/restart_sql_builder.py](../../converter/generators/restart/restart_sql_builder.md)
- [rules/__init__.py](../../rules/__init__.md)
- [rules/restart_sql_templates.py](../../rules/restart_sql_templates.md)
- [rules/restart_standard_rules.py](../../rules/restart_standard_rules.md)

## Symbol contracts and control points

### `builder` - L27-L28

```python
builder(config)
```

Observed calls (lexical order): `RestartSqlBuilder`.

### `paragraphs` - L32-L33

```python
paragraphs(builder)
```

Observed calls (lexical order): `builder.build_all`.

### `_joined` - L36-L37

```python
_joined(paragraph: SqlParagraph) -> str
```

Observed calls (lexical order): `'\n'.join`, `paragraph.lines`.

### `_bodies` - L40-L41

```python
_bodies(paragraph: SqlParagraph) -> list[str]
```

Observed calls (lexical order): `line.strip`.

### `_when_other_block` - L44-L47

```python
_when_other_block(bodies: list[str]) -> list[str]
```

Observed calls (lexical order): `bodies.index`, `sqltpl.WHEN_OTHER.strip`.

### `test_sql_templates_define_no_regex` - L54-L57

```python
test_sql_templates_define_no_regex()
```

Observed calls (lexical order): `inspect.getsource`.

### `test_sql_templates_all_is_sorted_and_complete` - L60-L64

```python
test_sql_templates_all_is_sorted_and_complete()
```

Observed calls (lexical order): `sorted`, `len`, `set`, `hasattr`.

Control points:

- L63: `for name in sqltpl.__all__`

### `test_catalog_all_is_sorted_and_free_of_duplicates` - L67-L72

```python
test_catalog_all_is_sorted_and_free_of_duplicates()
```

A duplicated export hides the name that was meant to be added.

Observed calls (lexical order): `sorted`, `len`, `set`, `hasattr`.

Control points:

- L71: `for name in cat.__all__`

### `test_sql_templates_assign_no_constant_twice` - L75-L87

```python
test_sql_templates_assign_no_constant_twice()
```

Observed calls (lexical order): `ast.parse`, `inspect.getsource`, `set`, `isinstance`, `duplicates.append`, `seen.add`.

Control points:

- L79: `for node in tree.body`
- L80: `if not isinstance(node, ast.Assign)`
- L82: `for target in node.targets`
- L83: `if isinstance(target, ast.Name)`
- L84: `if target.id in seen`

### `test_sql_templates_carry_no_site_names` - L90-L99

```python
test_sql_templates_carry_no_site_names()
```

Prose is held to the same rule as code.

Observed calls (lexical order): `inspect.getsource`, `inspect.getsource(sqltpl).upper`.

Control points:

- L98: `for token in ('DCLDZ', 'DZ01RST', 'DZBFAR', 'VMDZ', 'NM_ID_RS')`

### `test_three_paragraphs_are_produced` - L105-L110

```python
test_three_paragraphs_are_produced(paragraphs)
```

Observed calls (lexical order): `set`.

### `test_each_paragraph_header_matches_the_config` - L113-L115

```python
test_each_paragraph_header_matches_the_config(config, paragraphs)
```

Observed calls (lexical order): `paragraphs.items`, `config.paragraph`, `paragraph.lines`.

Control points:

- L114: `for (role, paragraph) in paragraphs.items()`

### `test_each_paragraph_ends_with_a_lone_period` - L118-L120

```python
test_each_paragraph_ends_with_a_lone_period(paragraphs)
```

Observed calls (lexical order): `paragraphs.values`.

Control points:

- L119: `for paragraph in paragraphs.values()`

### `test_no_scope_terminator_carries_a_period` - L123-L127

```python
test_no_scope_terminator_carries_a_period(paragraphs)
```

A period inside EVALUATE closes the scope and orphans END-EVALUATE.

Observed calls (lexical order): `paragraphs.values`, `_bodies`.

Control points:

- L125: `for paragraph in paragraphs.values()`
- L126: `for line in _bodies(paragraph)`

### `test_only_one_period_per_paragraph` - L130-L133

```python
test_only_one_period_per_paragraph(paragraphs)
```

Observed calls (lexical order): `paragraphs.values`, `_bodies`, `len`.

Control points:

- L131: `for paragraph in paragraphs.values()`

### `test_each_paragraph_carries_a_debug_trace` - L136-L138

```python
test_each_paragraph_carries_a_debug_trace(config, paragraphs)
```

Observed calls (lexical order): `paragraphs.items`, `config.paragraph`.

Control points:

- L137: `for (role, paragraph) in paragraphs.items()`

### `test_exec_sql_is_balanced` - L141-L145

```python
test_exec_sql_is_balanced(paragraphs)
```

Observed calls (lexical order): `paragraphs.values`, `_bodies`, `body.count`.

Control points:

- L142: `for paragraph in paragraphs.values()`

### `test_evaluate_is_balanced` - L148-L152

```python
test_evaluate_is_balanced(paragraphs)
```

Observed calls (lexical order): `paragraphs.values`, `_bodies`, `body.count`.

Control points:

- L149: `for paragraph in paragraphs.values()`

### `test_evaluate_follows_end_exec` - L155-L160

```python
test_evaluate_follows_end_exec(paragraphs)
```

Observed calls (lexical order): `paragraphs.values`, `_bodies`, `body.index`.

Control points:

- L156: `for paragraph in paragraphs.values()`

### `test_paragraphs_are_frozen` - L163-L165

```python
test_paragraphs_are_frozen(paragraphs)
```

Observed calls (lexical order): `pytest.raises`.

### `test_sql_location_is_off_by_default` - L172-L176

```python
test_sql_location_is_off_by_default(paragraphs)
```

The manual reference writes it in the business paragraph only.

Observed calls (lexical order): `paragraphs.values`, `_joined`.

Control points:

- L175: `for paragraph in paragraphs.values()`

### `test_sql_location_is_never_written_in_the_error_branch` - L179-L180

```python
test_sql_location_is_never_written_in_the_error_branch()
```

### `located` - L184-L188

```python
located(config, monkeypatch)
```

Observed calls (lexical order): `monkeypatch.setattr`, `RestartSqlBuilder`, `RestartSqlBuilder(config).build_all`.

### `test_when_enabled_it_is_written_once_at_paragraph_entry` - L191-L196

```python
test_when_enabled_it_is_written_once_at_paragraph_entry(located)
```

Observed calls (lexical order): `located.values`, `_bodies`, `l.endswith`, `len`, `body.index`.

Control points:

- L192: `for paragraph in located.values()`

### `test_when_enabled_the_error_branch_does_not_restate_it` - L199-L202

```python
test_when_enabled_the_error_branch_does_not_restate_it(located)
```

Observed calls (lexical order): `located.values`, `_bodies`, `_when_other_block`, `any`, `l.endswith`.

Control points:

- L200: `for paragraph in located.values()`

### `test_when_enabled_the_value_is_the_paragraph_number` - L205-L208

```python
test_when_enabled_the_value_is_the_paragraph_number(config, located)
```

Observed calls (lexical order): `located.items`, `config.paragraph`, `config.paragraph(role).split`, `_joined`.

Control points:

- L206: `for (role, paragraph) in located.items()`

### `test_select_reads_every_column` - L215-L218

```python
test_select_reads_every_column(config, paragraphs)
```

Observed calls (lexical order): `_joined`, `config.role.columns`.

Control points:

- L217: `for column in config.role.columns()`

### `test_select_binds_every_host_field` - L221-L225

```python
test_select_binds_every_host_field(config, paragraphs)
```

Observed calls (lexical order): `_joined`, `config.role.host_fields`.

Control points:

- L224: `for field in config.role.host_fields()`

### `test_select_column_and_into_counts_match` - L228-L233

```python
test_select_column_and_into_counts_match(config, paragraphs)
```

INTO hosts only. WHERE predicates also reference the group.

Observed calls (lexical order): `_bodies`, `config.role.columns`, `len`.

### `test_select_references_the_group_once_per_column_and_key` - L236-L242

```python
test_select_references_the_group_once_per_column_and_key(config, paragraphs)
```

Six INTO hosts plus three key predicates.

Observed calls (lexical order): `_joined`, `config.role.columns`, `config.role.key_pairs`, `len`, `text.count`.

### `test_select_treats_not_found_as_normal` - L244-L247

```python
test_select_treats_not_found_as_normal(paragraphs)
```

Observed calls (lexical order): `_bodies`.

### `test_select_names_the_table_in_from` - L250-L253

```python
test_select_names_the_table_in_from(config, paragraphs)
```

Observed calls (lexical order): `_joined`.

### `test_select_binds_the_payload_group_not_a_subfield` - L256-L262

```python
test_select_binds_the_payload_group_not_a_subfield(config, paragraphs)
```

DB2 binds the whole VARCHAR, not the -LEN / -TEXT subfields.

Observed calls (lexical order): `_joined`.

### `test_update_sets_payload_and_status_only` - L269-L275

```python
test_update_sets_payload_and_status_only(config, paragraphs)
```

Observed calls (lexical order): `_bodies`, `l.startswith`, `len`, `' '.join`.

### `test_update_never_sets_a_key_column` - L278-L283

```python
test_update_never_sets_a_key_column(config, paragraphs)
```

Observed calls (lexical order): `_bodies`, `l.startswith`, `' '.join`, `config.role.key_pairs`.

Control points:

- L282: `for (column, _field) in config.role.key_pairs()`

### `test_update_treats_not_found_as_an_error` - L286-L288

```python
test_update_treats_not_found_as_an_error(paragraphs)
```

Observed calls (lexical order): `_bodies`.

### `test_update_names_the_table` - L291-L294

```python
test_update_names_the_table(config, paragraphs)
```

Observed calls (lexical order): `_joined`.

### `test_insert_binds_the_host_structure_group` - L307-L309

```python
test_insert_binds_the_host_structure_group(config, paragraphs)
```

Observed calls (lexical order): `_joined`.

### `test_insert_binds_the_group_exactly_once` - L312-L314

```python
test_insert_binds_the_group_exactly_once(config, paragraphs)
```

Observed calls (lexical order): `_joined`, `text.count`.

### `test_insert_does_not_list_individual_columns` - L317-L321

```python
test_insert_does_not_list_individual_columns(config, paragraphs)
```

Regression guard: the INSERT must not expand into a column list.

Observed calls (lexical order): `_joined`, `config.role.columns`.

Control points:

- L320: `for column in config.role.columns()`

### `test_insert_does_not_qualify_the_group_with_a_field` - L324-L329

```python
test_insert_does_not_qualify_the_group_with_a_field(config, paragraphs)
```

Regression guard: no :{group}.{field} form for this statement.

Observed calls (lexical order): `_joined`, `config.role.host_fields`.

Control points:

- L328: `for field in config.role.host_fields()`

### `test_insert_parentheses_are_balanced` - L332-L334

```python
test_insert_parentheses_are_balanced(paragraphs)
```

Observed calls (lexical order): `_joined`, `text.count`.

### `test_insert_has_a_values_host_clause` - L337-L342

```python
test_insert_has_a_values_host_clause(config, paragraphs)
```

Observed calls (lexical order): `_bodies`, `sqltpl.INSERT_VALUES_HOST.format`, `sqltpl.INSERT_VALUES_HOST.format(group=config.role.host_record).strip`.

### `test_insert_names_the_table` - L345-L348

```python
test_insert_names_the_table(config, paragraphs)
```

Observed calls (lexical order): `_joined`.

### `test_insert_has_no_where_clause` - L351-L353

```python
test_insert_has_no_where_clause(paragraphs)
```

Observed calls (lexical order): `_bodies`, `any`, `line.startswith`.

### `test_the_key_predicates_are_complete` - L363-L367

```python
test_the_key_predicates_are_complete(config, paragraphs, role_key)
```

Observed calls (lexical order): `_joined`, `config.role.key_pairs`.

Control points:

- L366: `for (column, host) in config.role.key_pairs()`

### `test_exactly_three_predicates` - L373-L376

```python
test_exactly_three_predicates(config, paragraphs, role_key)
```

Observed calls (lexical order): `_bodies`, `l.startswith`, `config.role.key_pairs`, `len`.

### `test_the_error_text_names_the_verb_and_table` - L387-L393

```python
test_the_error_text_names_the_verb_and_table(config, paragraphs, role_key, verb)
```

Observed calls (lexical order): `_bodies`, `_when_other_block`, `any`.

### `test_select_and_update_each_carry_a_queryno` - L404-L407

```python
test_select_and_update_each_carry_a_queryno(paragraphs)
```

Observed calls (lexical order): `_bodies`, `any`, `line.startswith`.

Control points:

- L405: `for role in (std.ROLE_SELECT, std.ROLE_UPDATE)`

### `test_insert_carries_no_queryno` - L410-L412

```python
test_insert_carries_no_queryno(paragraphs)
```

Observed calls (lexical order): `_bodies`, `any`, `line.startswith`.

### `test_the_queryno_precedes_end_exec` - L415-L421

```python
test_the_queryno_precedes_end_exec(paragraphs)
```

Observed calls (lexical order): `_bodies`, `next`, `enumerate`, `l.startswith`, `body.index`.

Control points:

- L416: `for role in (std.ROLE_SELECT, std.ROLE_UPDATE)`

### `test_the_two_querynos_are_distinct` - L424-L431

```python
test_the_two_querynos_are_distinct(paragraphs)
```

Observed calls (lexical order): `next`, `_bodies`, `l.startswith`, `line.split`, `numbers.append`, `len`, `set`.

Control points:

- L426: `for role in (std.ROLE_SELECT, std.ROLE_UPDATE)`

### `test_each_queryno_matches_the_config` - L434-L442

```python
test_each_queryno_matches_the_config(config, paragraphs)
```

Observed calls (lexical order): `paragraphs.items`, `_joined`.

Control points:

- L439: `for (role, paragraph) in paragraphs.items()`
- L440: `if role not in expected`

### `test_perform_error_paragraph_is_the_last_statement` - L449-L452

```python
test_perform_error_paragraph_is_the_last_statement(config, paragraphs)
```

Observed calls (lexical order): `paragraphs.values`, `_bodies`, `_when_other_block`.

Control points:

- L450: `for paragraph in paragraphs.values()`

### `test_the_error_branch_has_exactly_two_statements` - L455-L458

```python
test_the_error_branch_has_exactly_two_statements(paragraphs)
```

DISPLAY then PERFORM. Nothing else, by default.

Observed calls (lexical order): `paragraphs.values`, `_bodies`, `_when_other_block`, `len`.

Control points:

- L457: `for paragraph in paragraphs.values()`

### `test_continue_is_the_normal_branch_body` - L461-L464

```python
test_continue_is_the_normal_branch_body(paragraphs)
```

Observed calls (lexical order): `paragraphs.values`, `_bodies`, `sqltpl.BRANCH_CONTINUE.strip`.

Control points:

- L462: `for paragraph in paragraphs.values()`

### `test_the_build_is_reported` - L471-L473

```python
test_the_build_is_reported(builder)
```

Observed calls (lexical order): `builder.build_all`, `any`.

### `test_messages_are_reset_between_builds` - L476-L480

```python
test_messages_are_reset_between_builds(builder)
```

Observed calls (lexical order): `builder.build_all`, `len`.

### `test_building_twice_produces_identical_output` - L483-L486

```python
test_building_twice_produces_identical_output(config)
```

Observed calls (lexical order): `RestartSqlBuilder`, `RestartSqlBuilder(config).build_all`.

### `test_a_different_scheme_changes_only_the_paragraph_names` - L489-L503

```python
test_a_different_scheme_changes_only_the_paragraph_names(role, complete_names)
```

Observed calls (lexical order): `RestartSqlBuilder`, `RestartSqlBuilder(RestartConfig.build(role, complete_names, std.SCHEME_SEVEN_SERIES)).build_all`, `RestartConfig.build`, `RestartSqlBuilder(RestartConfig.build(role, complete_names, std.SCHEME_EIGHT_SERIES)).build_all`, `zip`.

Control points:

- L501: `for (a, b) in zip(seven, eight)`

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
