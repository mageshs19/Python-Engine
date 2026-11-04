# `converter/validators/production_validator.py`

Source: [converter/validators/production_validator.py](../../../../converter/validators/production_validator.py) | 285 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `b9dfefd1152470cca4dc3cf41a43fe984038539a9705aa2e45acddef1cca91fc`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.repositories.dclgen_repository import DclgenRepository
from converter.validators.compiler_safety_validator import CompilerSafetyValidator
from converter.services.name_normalizer import NameNormalizer
from patterns.sequence_patterns import strip_sequence_numbers
from patterns.sql_patterns import HOST_REFERENCE_PATTERN
from patterns.validation_patterns import ERROR_DB2_PATTERN, FORBIDDEN_EXECUTABLE_IDMS_PATTERNS, FORBIDDEN_IDMS_DECLARATIVE_PATTERNS, NO_FETCH_HOST_VARIABLES_PATTERN, TODO_DB2_PATTERN, TODO_HOST_VARIABLE_PATTERN, UNABLE_TO_DECLARE_CURSOR_PATTERN
from rules.db2_validation_rules import REQUIRED_DB2_TOKENS
from rules.validation_rules import PRODUCTION_VALIDATION_MESSAGES
```

## Local dependency notes

- [converter/repositories/dclgen_repository.py](../repositories/dclgen_repository.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)
- [converter/validators/compiler_safety_validator.py](compiler_safety_validator.md)
- [patterns/sequence_patterns.py](../../patterns/sequence_patterns.md)
- [patterns/sql_patterns.py](../../patterns/sql_patterns.md)
- [patterns/validation_patterns.py](../../patterns/validation_patterns.md)
- [rules/db2_validation_rules.py](../../rules/db2_validation_rules.md)
- [rules/validation_rules.py](../../rules/validation_rules.md)

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion_service.py](../pipeline/conversion_service.md)
- [tests/generated_fields/test_compiler_safety_validator.py](../../tests/generated_fields/test_compiler_safety_validator.md)
- [tests/test_compiler_safety_validator.py](../../tests/test_compiler_safety_validator.md)
- [tests/test_imports.py](../../tests/test_imports.md)
- [tests/test_validators.py](../../tests/test_validators.md)

## Symbol contracts and control points

### `ProductionValidator` - L19-L285

```python
class ProductionValidator()
```

Performs production-focused validation for generated DB2 COBOL.

### `ProductionValidator.__init__` - L34-L38

```python
__init__(self, dclgen_repository: DclgenRepository) -> None
```

### `ProductionValidator.validate` - L40-L59

```python
validate(self, converted_cobol_text: str) -> list[str]
```

Observed calls (lexical order): `str`, `text.strip`, `CompilerSafetyValidator`, `CompilerSafetyValidator().validate`, `messages.extend`, `self._validate_required_db2_tokens`, `self._validate_no_todo_or_generated_error`, `self._validate_forbidden_idms_patterns`, `self._validate_forbidden_idms_declaratives`, `self._validate_generated_dclgen_host_variables`.

Control points:

- L47: `if not text.strip()`

### `ProductionValidator._validate_required_db2_tokens` - L61-L80

```python
_validate_required_db2_tokens(self, text: str, messages: list[str]) -> None
```

Observed calls (lexical order): `text.upper`, `token.upper`, `NameNormalizer.normalize`, `NameNormalizer.normalize(token).lower`, `messages.append`.

Control points:

- L68: `for token in REQUIRED_DB2_TOKENS`
- L69: `if token.upper() in upper_text`
- L74: `if key in PRODUCTION_VALIDATION_MESSAGES`

### `ProductionValidator._validate_no_todo_or_generated_error` - L82-L110

```python
_validate_no_todo_or_generated_error(self, text: str, messages: list[str]) -> None
```

Observed calls (lexical order): `TODO_HOST_VARIABLE_PATTERN.search`, `messages.append`, `TODO_DB2_PATTERN.search`, `ERROR_DB2_PATTERN.search`, `UNABLE_TO_DECLARE_CURSOR_PATTERN.search`, `NO_FETCH_HOST_VARIABLES_PATTERN.search`.

Control points:

- L87: `if TODO_HOST_VARIABLE_PATTERN.search(text)`
- L92: `if TODO_DB2_PATTERN.search(text)`
- L97: `if ERROR_DB2_PATTERN.search(text)`
- L102: `if UNABLE_TO_DECLARE_CURSOR_PATTERN.search(text)`
- L107: `if NO_FETCH_HOST_VARIABLES_PATTERN.search(text)`

### `ProductionValidator._validate_forbidden_idms_patterns` - L112-L129

```python
_validate_forbidden_idms_patterns(self, text: str, messages: list[str]) -> None
```

Observed calls (lexical order): `enumerate`, `text.splitlines`, `self._logical_line`, `self._is_comment_or_blank`, `pattern.search`, `messages.append`.

Control points:

- L117: `for (line_number, line) in enumerate(text.splitlines(), start=1)`
- L120: `if self._is_comment_or_blank(logical)`
- L123: `for pattern in FORBIDDEN_EXECUTABLE_IDMS_PATTERNS`
- L124: `if pattern.search(logical)`

### `ProductionValidator._validate_forbidden_idms_declaratives` - L131-L148

```python
_validate_forbidden_idms_declaratives(self, text: str, messages: list[str]) -> None
```

Observed calls (lexical order): `enumerate`, `text.splitlines`, `self._logical_line`, `self._is_comment_or_blank`, `pattern.search`, `messages.append`.

Control points:

- L136: `for (line_number, line) in enumerate(text.splitlines(), start=1)`
- L139: `if self._is_comment_or_blank(logical)`
- L142: `for pattern in FORBIDDEN_IDMS_DECLARATIVE_PATTERNS`
- L143: `if pattern.search(logical)`

### `ProductionValidator._validate_generated_dclgen_host_variables` - L150-L178

```python
_validate_generated_dclgen_host_variables(self, converted_cobol_text: str, messages: list[str]) -> None
```

Observed calls (lexical order): `self._generated_dclgen_host_references`, `self._valid_dclgen_host_reference_keys`, `messages.append`, `sorted`.

Control points:

- L159: `if not generated_hosts`
- L164: `if not valid_hosts`
- L174: `for host in missing_hosts`

### `ProductionValidator._generated_dclgen_host_references` - L180-L209

```python
_generated_dclgen_host_references(self, converted_cobol_text: str) -> set[str]
```

Observed calls (lexical order): `set`, `str`, `str(converted_cobol_text or '').splitlines`, `str(raw or '').rstrip`, `self._is_fixed_format_comment`, `len`, `line[:6].isdigit`, `logical_lines.append`, `'\n'.join`, `HOST_REFERENCE_PATTERN.finditer`, `NameNormalizer.to_cobol`, `match.group`, `self._host_key`, `output.add`.

Control points:

- L191: `for raw in str(converted_cobol_text or '').splitlines()`
- L193: `if self._is_fixed_format_comment(line)`
- L195: `if len(line) >= 7 and line[:6].isdigit()`
- L200: `for match in HOST_REFERENCE_PATTERN.finditer('\n'.join(logical_lines))`
- L206: `if key`

### `ProductionValidator._valid_dclgen_host_reference_keys` - L211-L231

```python
_valid_dclgen_host_reference_keys(self) -> set[str]
```

Observed calls (lexical order): `set`, `self.dclgen_repository.all`, `NameNormalizer.normalize`, `NameNormalizer.to_cobol`, `self.dclgen_repository.group_for_table`, `self._host_key`, `output.add`.

Control points:

- L216: `for column in self.dclgen_repository.all()`
- L222: `if not table or not field`
- L228: `if key`

### `ProductionValidator._host_key` - L233-L244

```python
_host_key(self, group: str, field: str) -> str
```

Observed calls (lexical order): `NameNormalizer.to_cobol`.

Control points:

- L241: `if not clean_group or not clean_field`

### `ProductionValidator._logical_line` - L246-L255

```python
_logical_line(self, line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `self._is_fixed_format_comment`, `strip_sequence_numbers`, `strip_sequence_numbers(text).strip`.

Control points:

- L252: `if self._is_fixed_format_comment(text)`

### `ProductionValidator._is_fixed_format_comment` - L257-L271

```python
_is_fixed_format_comment(self, line: str) -> bool
```

Observed calls (lexical order): `str`, `len`, `text[:6].isdigit`, `text.strip`, `stripped.startswith`.

Control points:

- L263: `if len(text) >= 7 and text[:6].isdigit() and (text[6:7] in ('*', '/'))`
- L268: `if stripped.startswith('*') or stripped.startswith('/')`

### `ProductionValidator._is_comment_or_blank` - L273-L285

```python
_is_comment_or_blank(self, line: str) -> bool
```

Observed calls (lexical order): `str`, `str(line or '').strip`, `stripped.startswith`.

Control points:

- L279: `if not stripped`
- L282: `if stripped.startswith('*') or stripped.startswith('/')`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
