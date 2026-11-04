# `tests/lrf/test_lr_status_token_replacer.py`

Source: [tests/lrf/test_lr_status_token_replacer.py](../../../../tests/lrf/test_lr_status_token_replacer.py) | 131 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `034d9053f793cb862dea900e4c7024ec0bcba58505df62296783a97e32fc039c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> The DB-REC-FOUND -> SQLCODE substitution, and its refusals.

## Import declarations

```python
from __future__ import annotations
import pytest
from converter.transformers.lr_status_token_replacer import LrStatusTokenReplacer
from rules.lrf_conversion_rules import END_OF_SET_TOKEN, LR_STATUS_TOKEN_SQLCODE, RECORD_FOUND_TOKEN, RECORD_NOT_FOUND_TOKEN, TOKENS_OWNED_DOWNSTREAM
```

## Local dependency notes

- [converter/transformers/lr_status_token_replacer.py](../../converter/transformers/lr_status_token_replacer.md)
- [rules/lrf_conversion_rules.py](../../rules/lrf_conversion_rules.md)

## Symbol contracts and control points

### `_fixed` - L27-L29

```python
_fixed(body: str, seq: str='001000', right: str='01000000') -> str
```

Observed calls (lexical order): `len`, `body.ljust`.

### `_program` - L32-L35

```python
_program(*bodies: str) -> str
```

Observed calls (lexical order): `_fixed`, `lines.extend`, `'\n'.join`.

### `_bodies` - L38-L39

```python
_bodies(text: str) -> list[str]
```

Observed calls (lexical order): `line[7:72].strip`, `text.splitlines`.

### `test_record_found_becomes_sqlcode_0` - L43-L49

```python
test_record_found_becomes_sqlcode_0() -> None
```

Observed calls (lexical order): `LrStatusTokenReplacer`, `LrStatusTokenReplacer().apply`, `_program`, `_bodies`.

### `test_negation_is_carried_through_unchanged` - L52-L56

```python
test_negation_is_carried_through_unchanged() -> None
```

Observed calls (lexical order): `LrStatusTokenReplacer`, `LrStatusTokenReplacer().apply`, `_program`, `_bodies`.

### `test_tokens_owned_elsewhere_are_left_intact` - L61-L65

```python
test_tokens_owned_elsewhere_are_left_intact(token) -> None
```

VM4BD420 carried four native DB-END-OF-SET conditions and this pass claimed all of them. The statement transformer owns them.

Observed calls (lexical order): `_program`, `LrStatusTokenReplacer`, `LrStatusTokenReplacer().apply`.

### `test_on_clause_is_never_disarmed` - L68-L72

```python
test_on_clause_is_never_disarmed() -> None
```

ON DB-REC-NOT-FOUND must survive to ON_DB_REC_NOT_FOUND_PATTERN. Rewriting it to 'ON SQLCODE = 100' leaves a residual IDMS clause.

Observed calls (lexical order): `_program`, `LrStatusTokenReplacer`, `LrStatusTokenReplacer().apply`.

### `test_mixed_program_converts_only_the_owned_token` - L75-L84

```python
test_mixed_program_converts_only_the_owned_token() -> None
```

Observed calls (lexical order): `LrStatusTokenReplacer`, `LrStatusTokenReplacer().apply`, `_program`, `_bodies`.

### `test_fixed_format_columns_are_preserved` - L88-L97

```python
test_fixed_format_columns_are_preserved() -> None
```

Observed calls (lexical order): `LrStatusTokenReplacer`, `LrStatusTokenReplacer().apply`, `_program`, `out.splitlines`, `len`, `line[0:6].isdigit`, `line[72:80].isdigit`.

Control points:

- L94: `for line in changed`

### `test_program_without_tokens_is_returned_byte_for_byte` - L101-L103

```python
test_program_without_tokens_is_returned_byte_for_byte() -> None
```

Observed calls (lexical order): `_program`, `LrStatusTokenReplacer`, `LrStatusTokenReplacer().apply`.

### `test_tokens_before_procedure_division_are_untouched` - L106-L113

```python
test_tokens_before_procedure_division_are_untouched() -> None
```

Observed calls (lexical order): `'\n'.join`, `_fixed`, `LrStatusTokenReplacer`, `LrStatusTokenReplacer().apply`.

### `test_comment_lines_are_untouched` - L116-L124

```python
test_comment_lines_are_untouched() -> None
```

Observed calls (lexical order): `'\n'.join`, `_fixed`, `f'DB2: {RECORD_FOUND_TOKEN} audit'.ljust`, `LrStatusTokenReplacer`, `LrStatusTokenReplacer().apply`.

### `test_replacement_is_reported` - L127-L131

```python
test_replacement_is_reported() -> None
```

Observed calls (lexical order): `LrStatusTokenReplacer`, `_program`, `replacer.apply`, `any`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
