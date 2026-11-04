# `tests/test_manual_direct_update_parity.py`

Source: [tests/test_manual_direct_update_parity.py](../../../tests/test_manual_direct_update_parity.py) | 97 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `bc59ed65424fce711ad573463b32569e5acd43b22a33741dcda442c333d5cfff`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Generic manual-DB2 equivalence evidence must never hide a source conflict.

## Module-level bindings

`SOURCE` (L6), `REVIEWS` (L38)

## Import declarations

```python
from converter.analyzers.program_flow.business_operation_parity_audit import OperationParityReview
from mainframe.verification.manual_direct_update_parity import manually_confirmed_direct_updates
```

## Local dependency notes

- [converter/analyzers/program_flow/business_operation_parity_audit.py](../converter/analyzers/program_flow/business_operation_parity_audit.md)
- [mainframe/verification/manual_direct_update_parity.py](../mainframe/verification/manual_direct_update_parity.md)

## Symbol contracts and control points

### `program` - L17-L36

```python
program(sql_code="\n EVALUATE SQLCODE\n WHEN 0 ADD 1 TO WS-UPDATED\n WHEN OTHER\n DISPLAY 'ERROR ON UPDATE'\n PERFORM SQLERROR\n END-EVALUATE\n", where='ACCOUNT_ID = :DCLCUSTOMER.ACCOUNT-ID', set_expr='MODIFIED = :DCLCUSTOMER.MODIFIED')
```

### `check` - L44-L47

```python
check(source=SOURCE, generated=None, manual=None, reviews=REVIEWS)
```

Observed calls (lexical order): `program`, `manually_confirmed_direct_updates`.

### `test_identical_manual_db2_update_with_unconditional_source_pair_is_manual_parity` - L50-L53

```python
test_identical_manual_db2_update_with_unconditional_source_pair_is_manual_parity()
```

Observed calls (lexical order): `check`.

### `test_reordered_set_and_key_predicates_are_equivalent_when_pairs_match` - L56-L61

```python
test_reordered_set_and_key_predicates_are_equivalent_when_pairs_match()
```

Observed calls (lexical order): `program`, `check`.

### `test_mismatched_update_key_or_updated_value_remains_blocked` - L64-L71

```python
test_mismatched_update_key_or_updated_value_remains_blocked()
```

Observed calls (lexical order): `program`, `check`.

Control points:

- L65: `for manual in (program(where='OTHER_ID = :DCLCUSTOMER.ACCOUNT-ID'), program(set_expr='MODIFIED = :DCLCUSTOMER.WRONG'), program(where='ACCOUNT_ID = :DCLCUSTOMER.ACCOUNT-ID OR FLAG = ...`

### `test_source_explicit_not_found_or_fetched_value_dependency_is_never_waived` - L74-L82

```python
test_source_explicit_not_found_or_fetched_value_dependency_is_never_waived()
```

Observed calls (lexical order): `SOURCE.replace`, `check`.

Control points:

- L80: `for source in sources`

### `test_wrong_manual_program_or_different_sqlcode_action_never_waived` - L85-L90

```python
test_wrong_manual_program_or_different_sqlcode_action_never_waived()
```

Observed calls (lexical order): `check`, `program`, `program().replace`.

### `test_unrelated_business_reviews_stay_blocked_after_local_manual_evidence` - L93-L97

```python
test_unrelated_business_reviews_stay_blocked_after_local_manual_evidence()
```

Observed calls (lexical order): `OperationParityReview`, `check`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
