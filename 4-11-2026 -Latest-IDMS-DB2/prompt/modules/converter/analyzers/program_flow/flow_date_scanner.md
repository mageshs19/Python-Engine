# `converter/analyzers/program_flow/flow_date_scanner.py`

Source: [converter/analyzers/program_flow/flow_date_scanner.py](../../../../../converter/analyzers/program_flow/flow_date_scanner.py) | 77 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `23c60228819e6fb3dfd05e6348c5ed03944838c6fea628dc6b2b211bdbce30bf`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Finds lines that touch a date or timestamp.

## Module-level bindings

`__all__` (L77)

## Import declarations

```python
from __future__ import annotations
from converter.analyzers.program_flow.flow_models import DateUsage, LogicalLine
from rules.program_flow_rules import DATE_TOKEN_PREFIXES, DATE_TOKENS, TOKEN_DELIMITERS, USAGE_TYPE_DATE_TOKEN
```

## Local dependency notes

- [converter/analyzers/program_flow/flow_models.py](flow_models.md)
- [rules/program_flow_rules.py](../../../rules/program_flow_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/analyzers/program_flow/__init__.py](__init__.md)
- [converter/analyzers/program_flow/program_flow_analyzer.py](program_flow_analyzer.md)

## Symbol contracts and control points

### `FlowDateScanner` - L34-L74

```python
class FlowDateScanner()
```

Reports date/timestamp touches, one entry per line.

### `FlowDateScanner.usages` - L37-L57

```python
usages(self, lines: list[LogicalLine]) -> list[DateUsage]
```

Observed calls (lexical order): `self._first_date_token`, `output.append`, `DateUsage`.

Control points:

- L40: `for line in lines or []`
- L41: `if line.is_comment`
- L45: `if not token`

### `FlowDateScanner._first_date_token` - L60-L66

```python
_first_date_token(cls, upper_body: str) -> str
```

Observed calls (lexical order): `cls._tokens`, `token.startswith`.

Control points:

- L61: `for token in cls._tokens(upper_body)`
- L62: `if token in DATE_TOKENS`
- L64: `if token.startswith(DATE_TOKEN_PREFIXES)`

### `FlowDateScanner._tokens` - L69-L74

```python
_tokens(upper_body: str) -> list[str]
```

Split on COBOL word delimiters. Hyphens are part of a name.

Observed calls (lexical order): `str`, `text.replace`, `text.split`.

Control points:

- L72: `for delimiter in TOKEN_DELIMITERS`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
