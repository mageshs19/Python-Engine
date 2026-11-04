# `converter/generators/cursor_paragraph/cursor_key_diagnostics.py`

Source: [converter/generators/cursor_paragraph/cursor_key_diagnostics.py](../../../../../converter/generators/cursor_paragraph/cursor_key_diagnostics.py) | 202 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `b761e728e1473d774de47857a47b84fb6370ea89f598b00f9a0951d7162c03b4`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`HOST_OF_SEPARATOR` (L28), `__all__` (L202)

## Import declarations

```python
from __future__ import annotations
from converter.generators.cursor_paragraph.join_key_label_resolver import JoinKeyLabelResolver
from converter.services.name_normalizer import NameNormalizer
from rules.cursor_paragraph_rules import ALIGN_KEY_QUALIFIER, BODY_FIRST_COLUMN, EMIT_KEY_DIAGNOSTICS, HOST_GROUP_SEPARATOR, HOST_REFERENCE_PREFIX, IND_KEY_CONTINUATION, IND_WHEN_BODY, KEY_BODY_END_COLUMN, KEY_DIAGNOSTIC_LIMIT, KEY_DISPLAY_LITERAL_TEMPLATE, KEY_DISPLAY_TEMPLATE, KEY_LABEL_MIN_WIDTH, KEY_LABEL_SOURCE, KEY_LABEL_SOURCE_MAPPING, KEY_QUALIFIER_TEMPLATE, SKIP_UNQUALIFIED_KEY_HOSTS, TOKEN_OF, WRAP_KEY_DISPLAY
```

## Local dependency notes

- [converter/generators/cursor_paragraph/join_key_label_resolver.py](join_key_label_resolver.md)
- [converter/services/name_normalizer.py](../../services/name_normalizer.md)
- [rules/cursor_paragraph_rules.py](../../../rules/cursor_paragraph_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/cursor_paragraph/cursor_error_branch.py](cursor_error_branch.md)
- [converter/generators/cursor_paragraph/cursor_paragraph_body_builder.py](cursor_paragraph_body_builder.md)
- [tests/cursor_contract/test_join_key_labels.py](../../../tests/cursor_contract/test_join_key_labels.md)

## Symbol contracts and control points

### `KeyDiagnosticsBuilder` - L31-L199

```python
class KeyDiagnosticsBuilder()
```

Renders the driving-key DISPLAY lines of a child cursor's WHEN OTHER branch.

### `KeyDiagnosticsBuilder.__init__` - L54-L66

```python
__init__(self, label_resolver: JoinKeyLabelResolver | None=None) -> None
```

Observed calls (lexical order): `ValueError`.

Control points:

- L58: `if label_resolver is None`

Explicit raises: `ValueError("KeyDiagnosticsBuilder requires a JoinKeyLabelResolver built over the run's MappingRepository. Substituting an empty resolver degrades every drivi...`.

### `KeyDiagnosticsBuilder.messages` - L69-L70

```python
messages(self) -> list[str]
```

### `KeyDiagnosticsBuilder.lines_for_where` - L72-L75

```python
lines_for_where(self, conditions: list[str]) -> list[str]
```

Observed calls (lexical order): `self._render`, `self._host_of_condition`.

### `KeyDiagnosticsBuilder.lines_for_hosts` - L77-L78

```python
lines_for_hosts(self, hosts: list[str]) -> list[str]
```

Observed calls (lexical order): `list`, `self._render`.

### `KeyDiagnosticsBuilder._render` - L80-L111

```python
_render(self, raw_hosts: list[str]) -> list[str]
```

Observed calls (lexical order): `set`, `self._split`, `seen.add`, `pairs.append`, `self._label`, `len`, `max`, `label.ljust`, `lines.extend`, `self._pair_lines`.

Control points:

- L81: `if not EMIT_KEY_DIAGNOSTICS`
- L87: `for raw in raw_hosts`
- L89: `if not host or host in seen`
- L91: `if not group and SKIP_UNQUALIFIED_KEY_HOSTS`
- L97: `if 0 < KEY_DIAGNOSTIC_LIMIT <= len(pairs)`
- L100: `if not pairs`
- L109: `for (label, host, group) in pairs`

### `KeyDiagnosticsBuilder._pair_lines` - L113-L139

```python
_pair_lines(self, label: str, host: str, group: str) -> list[str]
```

Observed calls (lexical order): `KEY_DISPLAY_TEMPLATE.format`, `self._fits`, `out.append`, `self._qualifier_line`, `KEY_QUALIFIER_TEMPLATE.format`, `KEY_DISPLAY_LITERAL_TEMPLATE.format`.

Control points:

- L117: `if self._fits(inline) or not WRAP_KEY_DISPLAY`
- L119: `if group`
- L134: `if group`

### `KeyDiagnosticsBuilder._fits` - L142-L143

```python
_fits(line: str) -> bool
```

Observed calls (lexical order): `len`.

### `KeyDiagnosticsBuilder._qualifier_line` - L146-L161

```python
_qualifier_line(cls, display: str, host: str, qualifier: str) -> str
```

Observed calls (lexical order): `len`, `cls._fits`.

Control points:

- L152: `if not ALIGN_KEY_QUALIFIER`
- L158: `if not cls._fits(aligned)`

### `KeyDiagnosticsBuilder._label` - L163-L175

```python
_label(self, host: str, group: str) -> str
```

Observed calls (lexical order): `NameNormalizer.to_cobol`, `self.label_resolver.label_for`, `self.label_resolver.table_of`, `NameNormalizer.normalize`.

Control points:

- L164: `if KEY_LABEL_SOURCE != KEY_LABEL_SOURCE_MAPPING`

### `KeyDiagnosticsBuilder._split` - L178-L193

```python
_split(reference: str) -> tuple[str, str]
```

Observed calls (lexical order): `str`, `str(reference or '').strip`, `str(reference or '').strip().lstrip`, `text.upper`, `upper.partition`, `group.strip`, `host.strip`.

Control points:

- L180: `if not text`
- L185: `if HOST_OF_SEPARATOR in upper`
- L189: `if HOST_GROUP_SEPARATOR in upper`

### `KeyDiagnosticsBuilder._host_of_condition` - L196-L199

```python
_host_of_condition(condition: str) -> str
```

Observed calls (lexical order): `str`, `text.partition`, `(right or text).strip`.

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
