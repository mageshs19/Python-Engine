# `tests/lrf/test_status_token_classifier.py`

Source: [tests/lrf/test_status_token_classifier.py](../../../../tests/lrf/test_status_token_classifier.py) | 194 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `4d136aebf3924228bb3843c6c07e5e677adc0dfbb750436947d38ffd5bb564f8`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> The LR-STATUS classifier: three classes, no default, no inversion.

## Module-level bindings

`QUOTE` (L38), `EMITTED_TOKENS` (L137)

## Import declarations

```python
from __future__ import annotations
import pytest
from converter.transformers.lrf_path_expander import LrfPathExpander
from rules.lrf_conversion_rules import END_OF_SET_TOKEN, LR_STATUS_TOKEN_SQLCODE, RECORD_FOUND_TOKEN, RECORD_NOT_FOUND_TOKEN, TOKENS_OWNED_DOWNSTREAM
```

## Local dependency notes

- [converter/transformers/lrf_path_expander.py](../../converter/transformers/lrf_path_expander.md)
- [rules/lrf_conversion_rules.py](../../rules/lrf_conversion_rules.md)

## Symbol contracts and control points

### `_classify` - L41-L42

```python
_classify(literal: str)
```

Observed calls (lexical order): `LrfPathExpander._status_token`.

### `test_literal_classifies_to_expected_token` - L61-L62

```python
test_literal_classifies_to_expected_token(literal, expected) -> None
```

Observed calls (lexical order): `_classify`.

### `test_found_is_not_end_of_set` - L65-L70

```python
test_found_is_not_end_of_set() -> None
```

The exact inversion. FOUND must never reach the 100 family.

Observed calls (lexical order): `_classify`.

### `test_not_found_is_tested_before_found` - L73-L76

```python
test_not_found_is_tested_before_found() -> None
```

FOUND is a substring of NOT-FOUND. Order is the whole defence.

Observed calls (lexical order): `_classify`.

### `test_unrecognised_literal_is_refused` - L84-L86

```python
test_unrecognised_literal_is_refused(literal) -> None
```

No default. An unknown literal must not be guessed.

Observed calls (lexical order): `_classify`.

### `test_negated_positive_is_refused` - L90-L92

```python
test_negated_positive_is_refused(literal) -> None
```

A negation that reaches a positive class is refused, not guessed.

Observed calls (lexical order): `_classify`.

### `test_underscore_form_is_normalised` - L95-L97

```python
test_underscore_form_is_normalised() -> None
```

cobol_name(), not .upper(). VMBFAS_EOA must still classify.

Observed calls (lexical order): `_classify`.

### `test_rewrite_preserves_negation` - L101-L105

```python
test_rewrite_preserves_negation() -> None
```

Observed calls (lexical order): `LrfPathExpander._rewrite_lr_status`.

### `test_rewrite_drops_the_literal_on_equality` - L108-L113

```python
test_rewrite_drops_the_literal_on_equality() -> None
```

Observed calls (lexical order): `LrfPathExpander._rewrite_lr_status`.

### `test_refused_condition_is_left_byte_for_byte` - L116-L121

```python
test_refused_condition_is_left_byte_for_byte() -> None
```

Observed calls (lexical order): `LrfPathExpander._rewrite_lr_status`.

### `test_hits_counts_resolved_rewrites_only` - L124-L133

```python
test_hits_counts_resolved_rewrites_only() -> None
```

A refusal reported as a rewrite is a false entry in the run log.

Observed calls (lexical order): `LrfPathExpander._rewrite_lr_status`.

### `test_every_emitted_token_has_an_owner` - L144-L157

```python
test_every_emitted_token_has_an_owner() -> None
```

Ownership is SPLIT, not absent.

Observed calls (lexical order): `set`.

### `test_ownership_does_not_overlap` - L160-L164

```python
test_ownership_does_not_overlap() -> None
```

Two owners of one rewrite is how the VM4BD420 defect happened: this pass runs first and silently claimed four native DB-END-OF-SET conditions the statement transformer already owned.

Observed calls (lexical order): `set`.

### `test_the_replacer_owns_only_the_success_token` - L167-L169

```python
test_the_replacer_owns_only_the_success_token() -> None
```

Observed calls (lexical order): `set`.

### `test_no_prefix_splits_correctly` - L182-L184

```python
test_no_prefix_splits_correctly(literal, expected) -> None
```

NO-X-FND is not found; NO-MORE-X is end of set. Same prefix.

Observed calls (lexical order): `_classify`.

### `test_abbreviated_combined_relation_is_refused` - L187-L194

```python
test_abbreviated_combined_relation_is_refused() -> None
```

Observed calls (lexical order): `LrfPathExpander._rewrite_lr_status`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
