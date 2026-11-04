# `tests/cursor_where/test_join_resolver.py`

Source: [tests/cursor_where/test_join_resolver.py](../../../../tests/cursor_where/test_join_resolver.py) | 176 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `9ecdb5ccca19f1139b4e9766ee9a76c9f1190f1c0aed84fdf81dca4451f41167`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CursorJoinResolver - predicate resolution.

## Import declarations

```python
from __future__ import annotations
from converter.resolvers.cursor_join_resolver import CursorJoinResolver
from rules.cursor_declaration_rules import EMIT_DRIVING_KEY_PREDICATE
from tests.cursor_where._support import CHILD_GROUP, CHILD_RECORD, ColumnNameResolver, Condition, EXPECTED_PREDICATE, FOREIGN_COLUMN, HostVariableResolver, LegacyRelationshipResolver, PARENT_GROUP, PartialCondition, RelationshipResolver, Resolution, join
```

## Local dependency notes

- [converter/resolvers/cursor_join_resolver.py](../../converter/resolvers/cursor_join_resolver.md)
- [rules/cursor_declaration_rules.py](../../rules/cursor_declaration_rules.md)
- [tests/cursor_where/_support.py](_support.md)

## Symbol contracts and control points

### `test_driving_key_fallback_constants_are_importable` - L34-L36

```python
test_driving_key_fallback_constants_are_importable()
```

The fallback used names it never imported and raised NameError.

### `test_fallback_path_never_raises_name_error` - L39-L46

```python
test_fallback_path_never_raises_name_error()
```

D-1 is about NOT RAISING.

Observed calls (lexical order): `RelationshipResolver`, `join`, `isinstance`, `resolver.where_conditions`.

### `test_resolver_never_calls_a_missing_host_method` - L50-L63

```python
test_resolver_never_calls_a_missing_host_method()
```

host_for_command/host_for_column do not exist on the resolver.

Observed calls (lexical order): `HostVariableResolver`, `hasattr`, `CursorJoinResolver`, `RelationshipResolver`, `Resolution`, `ColumnNameResolver`, `resolver.where_conditions`.

### `test_driving_key_predicate_targets_the_parent_group` - L67-L69

```python
test_driving_key_predicate_targets_the_parent_group()
```

Observed calls (lexical order): `RelationshipResolver`, `Resolution`, `join`, `resolver.where_conditions`.

### `test_driving_key_predicate_is_never_self_referential` - L72-L76

```python
test_driving_key_predicate_is_never_self_referential()
```

'KY_SIFORM = :DCLDZBFASTV.KY-SIFORM' is a filter, not a join.

Observed calls (lexical order): `RelationshipResolver`, `Resolution`, `join`, `resolver.where_conditions`.

Control points:

- L75: `for predicate in resolver.where_conditions(CHILD_RECORD)`

### `test_no_parent_side_refuses_instead_of_guessing` - L79-L86

```python
test_no_parent_side_refuses_instead_of_guessing()
```

Observed calls (lexical order): `join`, `RelationshipResolver`, `Resolution`, `resolver.where_conditions`, `any`.

### `test_caller_supplied_driving_host_is_honoured` - L89-L100

```python
test_caller_supplied_driving_host_is_honoured()
```

The LRF path keyword can supply the parent host directly.

Observed calls (lexical order): `join`, `RelationshipResolver`, `Resolution`, `resolver.where_conditions`.

### `test_legacy_facade_method_name_is_tolerated` - L104-L112

```python
test_legacy_facade_method_name_is_tolerated()
```

Observed calls (lexical order): `CursorJoinResolver`, `LegacyRelationshipResolver`, `Condition`, `Resolution`, `ColumnNameResolver`, `HostVariableResolver`, `resolver.where_conditions`.

### `test_a_condition_without_child_table_is_skipped_not_fatal` - L116-L124

```python
test_a_condition_without_child_table_is_skipped_not_fatal()
```

Observed calls (lexical order): `join`, `RelationshipResolver`, `PartialCondition`, `Resolution`, `resolver.where_conditions`, `any`.

### `test_relationship_predicate_is_preferred_over_the_fallback` - L128-L137

```python
test_relationship_predicate_is_preferred_over_the_fallback()
```

Observed calls (lexical order): `join`, `RelationshipResolver`, `Resolution`, `Condition`, `resolver.where_conditions`.

### `test_duplicate_predicates_are_collapsed` - L140-L146

```python
test_duplicate_predicates_are_collapsed()
```

Observed calls (lexical order): `join`, `RelationshipResolver`, `Condition`, `Resolution`, `len`, `resolver.where_conditions`.

### `test_a_predicate_without_a_parent_host_is_skipped_and_reported` - L149-L159

```python
test_a_predicate_without_a_parent_host_is_skipped_and_reported()
```

Observed calls (lexical order): `join`, `RelationshipResolver`, `Resolution`, `Condition`, `resolver.where_conditions`, `any`.

### `test_an_empty_record_name_returns_no_predicate` - L162-L163

```python
test_an_empty_record_name_returns_no_predicate()
```

Observed calls (lexical order): `RelationshipResolver`, `join`, `join(RelationshipResolver()).where_conditions`.

### `test_diagnostics_are_reset_between_calls` - L166-L176

```python
test_diagnostics_are_reset_between_calls()
```

Observed calls (lexical order): `join`, `RelationshipResolver`, `Resolution`, `resolver.where_conditions`, `len`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
