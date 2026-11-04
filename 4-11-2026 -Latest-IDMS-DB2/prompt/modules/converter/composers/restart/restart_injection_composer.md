# `converter/composers/restart/restart_injection_composer.py`

Source: [converter/composers/restart/restart_injection_composer.py](../../../../../converter/composers/restart/restart_injection_composer.py) | 732 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `b6a50379189f6c464d858934240d27e6bddb1ae2e8ae3c1b5d6c69641effbd78`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Orchestrates the restart injection for one update program.

## Module-level bindings

`PROGRAM_KIND_RETRIEVAL` (L174), `PROGRAM_KIND_UPDATE` (L175), `MESSAGE_PREFIX` (L177), `ROLE_TOKEN_ATTRIBUTES` (L181), `ROLE_ESTABLISHES_APPLICABILITY` (L191), `SCAN_COMMENTS_FOR_RESTART_REFERENCE` (L195), `SHARED_CLEANUP_METHODS` (L197), `POSITIONAL_KINDS` (L199), `_Span` (L205), `__all__` (L719)

## Import declarations

```python
from __future__ import annotations
import inspect
from typing import Any, Iterable, Sequence
from converter.composers.restart.legacy_restart_cleanup import LegacyRestartCleanup
from converter.composers.restart.process_paragraph_injector import ProcessParagraphInjector
from converter.composers.restart.restart_injection_geometry import END_PROGRAM, MAINLINE_LABEL, NON_PARAGRAPH_WORDS, SCOPE_REPORT_PREFIXES, SCOPE_TERMINATOR_WORDS, RestartParagraphGeometry, Span
from converter.composers.restart.restart_storage_injector import RestartStorageInjector
from converter.generators.restart.read_paragraph_builder import RestartReadParagraphBuilder
from converter.generators.restart.restart_config import RestartConfig
from converter.generators.restart.restart_flow_builder import RestartFlowBuilder
from converter.generators.restart.restart_main_flow_builder import RestartMainFlowBuilder
from converter.generators.restart.restart_name_resolver import RestartNameResolver
from converter.generators.restart.restart_sql_builder import RestartSqlBuilder
from rules.restart_standard_rules import NOT_APPLICABLE_REASONS, RESTART_DIAGNOSTICS, RESTART_PARAGRAPH_ROLES, ROLE_COMMIT, ROLE_CONTROL
```

## Local dependency notes

- [converter/composers/restart/legacy_restart_cleanup.py](legacy_restart_cleanup.md)
- [converter/composers/restart/process_paragraph_injector.py](process_paragraph_injector.md)
- [converter/composers/restart/restart_injection_geometry.py](restart_injection_geometry.md)
- [converter/composers/restart/restart_storage_injector.py](restart_storage_injector.md)
- [converter/generators/restart/read_paragraph_builder.py](../../generators/restart/read_paragraph_builder.md)
- [converter/generators/restart/restart_config.py](../../generators/restart/restart_config.md)
- [converter/generators/restart/restart_flow_builder.py](../../generators/restart/restart_flow_builder.md)
- [converter/generators/restart/restart_main_flow_builder.py](../../generators/restart/restart_main_flow_builder.md)
- [converter/generators/restart/restart_name_resolver.py](../../generators/restart/restart_name_resolver.md)
- [converter/generators/restart/restart_sql_builder.py](../../generators/restart/restart_sql_builder.md)
- [rules/restart_standard_rules.py](../../../rules/restart_standard_rules.md)

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/restart/restart_stage_adapter.py](restart_stage_adapter.md)
- [converter/resolvers/restart_context_builder.py](../../resolvers/restart_context_builder.md)
- [tests/restart/_checklist.py](../../../tests/restart/_checklist.md)
- [tests/restart/test_m10c_golden_output.py](../../../tests/restart/test_m10c_golden_output.md)
- [tests/restart/test_m9b_injection_composer.py](../../../tests/restart/test_m9b_injection_composer.md)

## Symbol contracts and control points

### `RestartInjectionComposer` - L208-L716

```python
class RestartInjectionComposer(RestartParagraphGeometry)
```

Applies the complete restart family to one converted program.

### `RestartInjectionComposer.__init__` - L211-L221

```python
__init__(self, line_utils, *, scheme: str | None=None, shared_cleanups: Iterable[Any]=()) -> None
```

Observed calls (lexical order): `tuple`.

### `RestartInjectionComposer.compose` - L226-L263

```python
compose(self, text: str, *, role: Any=None, program_kind: str=PROGRAM_KIND_UPDATE, totals: Sequence[str]=()) -> tuple[str, list[str]]
```

Return (converted text, messages). Never raises on refusal.

Observed calls (lexical order): `str`, `self._lines`, `self._not_applicable`, `self._say`, `list`, `RestartNameResolver`, `RestartNameResolver(self.line_utils).resolve`, `self.messages.extend`, `self._config`, `config.is_usable`, `self._refuse`, `self._diagnostic`, `self._clean`, `self._storage`, `self._mainline`, `self._reader`.
Another 3 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L240: `if reason`
- L248: `if not config.is_usable()`
- L253: `if self.scheme`

### `RestartInjectionComposer._not_applicable` - L268-L293

```python
_not_applicable(self, lines: list[str], role: Any, kind: str) -> str
```

Observed calls (lexical order): `str`, `str(kind or '').strip`, `str(kind or '').strip().lower`, `self._role_tokens`, `self._say`, `', '.join`, `self._references_restart_table`.

Control points:

- L269: `if str(kind or '').strip().lower() != PROGRAM_KIND_UPDATE`
- L272: `if role is None`
- L277: `if tokens and ROLE_ESTABLISHES_APPLICABILITY`
- L284: `if not tokens`
- L290: `if not self._references_restart_table(lines, role)`

### `RestartInjectionComposer._role_tokens` - L296-L303

```python
_role_tokens(role: Any) -> list[str]
```

Every restart-table token the role carries, upper-cased.

Observed calls (lexical order): `getattr`, `str`, `str(getattr(role, attribute, '') or '').strip`, `str(getattr(role, attribute, '') or '').strip().upper`, `seen.append`.

Control points:

- L299: `for attribute in ROLE_TOKEN_ATTRIBUTES`
- L301: `if token and token not in seen`

### `RestartInjectionComposer._references_restart_table` - L305-L317

```python
_references_restart_table(self, lines: list[str], role: Any) -> bool
```

Fallback evidence: does the text mention the restart table?

Observed calls (lexical order): `self._role_tokens`, `' '.join`, `reader`, `any`.

Control points:

- L308: `if not tokens`

### `RestartInjectionComposer._config` - L322-L325

```python
_config(self, role: Any, names) -> RestartConfig
```

Observed calls (lexical order): `RestartConfig.build`.

Control points:

- L323: `if self.scheme is None`

### `RestartInjectionComposer._refuse` - L327-L334

```python
_refuse(self, config: RestartConfig) -> None
```

Observed calls (lexical order): `config.missing`, `self._say`.

Control points:

- L328: `for name in config.missing()`
- L330: `if config.retention_days <= 0`

### `RestartInjectionComposer._clean` - L339-L346

```python
_clean(self, lines: list[str], config: RestartConfig) -> list[str]
```

Observed calls (lexical order): `LegacyRestartCleanup`, `cleanup.clean`, `list`, `getattr`, `self.messages.extend`, `len`, `self._diagnostic`.

Control points:

- L344: `if removed > 0`

### `RestartInjectionComposer._storage` - L351-L361

```python
_storage(self, lines: list[str], config: RestartConfig) -> list[str]
```

Declare the fields the generated paragraphs will reference.

Observed calls (lexical order): `RestartStorageInjector`, `injector.inject`, `self.messages.extend`.

### `RestartInjectionComposer._mainline` - L366-L427

```python
_mainline(self, lines: list[str], config: RestartConfig, totals: Sequence[str]) -> list[str]
```

Replace the terminating paragraph's flow with the generated one.

Observed calls (lexical order): `self._mainline_span`, `self._replacement_start`, `self._say`, `self._suppress_open`, `self._suppress_prime_read`, `RestartMainFlowBuilder`, `builder.build`, `self.messages.extend`, `self._diagnostic`, `config.paragraph`, `list`.

Control points:

- L380: `if span is None`
- L386: `if preserved > 0`
- L397: `if suppress_open`
- L403: `if suppress_read`
- L417: `if not body`

### `RestartInjectionComposer._mainline_span` - L429-L456

```python
_mainline_span(self, lines: list[str]) -> Span | None
```

The paragraph that TERMINATES the program. See CORRECTION 6.

Observed calls (lexical order): `self._termination_index`, `self._say`, `self._spans`, `self._procedure_index`, `self._insert_index`, `Span`.

Control points:

- L432: `if index < 0`
- L437: `for span in spans`
- L438: `if span.header <= index < span.end`
- L445: `if start < 0 or index <= start`
- L448: `if index >= end`

### `RestartInjectionComposer._replacement_start` - L458-L493

```python
_replacement_start(self, lines: list[str], span: Span, config: RestartConfig) -> int
```

Where the generated flow replaces the mainline body.

Observed calls (lexical order): `self._open_input_index_within`, `self._perform_index_within`, `min`.

### `RestartInjectionComposer._suppress_open` - L495-L508

```python
_suppress_open(self, lines: list[str], start: int, span: Span) -> tuple[bool, int]
```

Does the program already OPEN the file outside the region?

Observed calls (lexical order): `self._open_input_index`.

### `RestartInjectionComposer._suppress_prime_read` - L510-L534

```python
_suppress_prime_read(self, lines: list[str], start: int, span: Span, config: RestartConfig) -> tuple[bool, int]
```

Does an initialisation already prime the reader? CORRECTION 7.

Observed calls (lexical order): `self._span_named`, `excluded.append`, `self._statement_index_outside`.

Control points:

- L526: `if process is not None`

### `RestartInjectionComposer._reader` - L539-L563

```python
_reader(self, lines: list[str], config: RestartConfig) -> tuple[list[str], list[Any]]
```

Observed calls (lexical order): `RestartReadParagraphBuilder`, `self._span_named`, `builder.build`, `self.messages.extend`, `self._say`, `self._needs_rebuild`, `list`, `paragraph.lines`.

Control points:

- L547: `if span is None`
- L556: `if not self._needs_rebuild(builder, lines[span.start:span.end])`

### `RestartInjectionComposer._needs_rebuild` - L566-L577

```python
_needs_rebuild(builder: Any, body: list[str]) -> bool
```

Ask M8 using the arity it declares, measured once.

Observed calls (lexical order): `inspect.signature`, `inspect.signature(method).parameters.values`, `bool`, `method`.

### `RestartInjectionComposer._process` - L582-L599

```python
_process(self, lines: list[str], config: RestartConfig) -> list[str]
```

Observed calls (lexical order): `self._span_named`, `self._say`, `self._report_span`, `ProcessParagraphInjector`, `injector.inject`, `self.messages.extend`, `list`.

Control points:

- L584: `if span is None`

### `RestartInjectionComposer._report_span` - L601-L613

```python
_report_span(self, span: Span, body: list[str]) -> None
```

Say what the repair pass was given, not what we assume.

Observed calls (lexical order): `self._say`, `self._logical`, `logical.startswith`.

### `RestartInjectionComposer._splice` - L618-L650

```python
_splice(self, lines: list[str], config: RestartConfig, appended: list[Any]) -> list[str]
```

Observed calls (lexical order): `RestartSqlBuilder`, `RestartFlowBuilder`, `flow.build_all`, `list`, `sql.build_all`, `self.messages.extend`, `self._in_role_order`, `self._drop`, `str`, `str(p.name).upper`, `rendered.append`, `paragraph.lines`, `rendered.extend`, `self._insert_index`, `str(head[-1]).strip`, `head.pop`.
Another 2 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L631: `if not ordered`
- L637: `for paragraph in ordered`
- L646: `while head and (not str(head[-1]).strip())`

### `RestartInjectionComposer._in_role_order` - L653-L665

```python
_in_role_order(paragraphs: list[Any]) -> list[Any]
```

Observed calls (lexical order): `ordered.extend`.

### `RestartInjectionComposer._drop` - L667-L681

```python
_drop(self, lines: list[str], names: set[str]) -> list[str]
```

Observed calls (lexical order): `set`, `self._spans`, `span.name.upper`, `str`, `str(lines[start - 1]).strip`, `doomed.update`, `range`, `self._say`, `enumerate`.

Control points:

- L669: `for span in self._spans(lines)`
- L670: `if span.name.upper() not in names`
- L673: `while start > 0 and (not str(lines[start - 1]).strip())`
- L677: `if not doomed`

### `RestartInjectionComposer._hand_off` - L686-L705

```python
_hand_off(self, lines: list[str]) -> tuple[str, list[str]]
```

Observed calls (lexical order): `self._join`, `callable`, `getattr`, `self._say`, `call`, `isinstance`, `self.messages.extend`, `list`.

Control points:

- L688: `for cleanup in self.shared_cleanups`
- L690: `if call is None`
- L691: `for attribute in SHARED_CLEANUP_METHODS`
- L693: `if callable(candidate)`
- L696: `if call is None`
- L702: `if isinstance(result, str) and result`

### `RestartInjectionComposer._say` - L710-L711

```python
_say(self, message: str) -> None
```

Observed calls (lexical order): `self.messages.append`.

### `RestartInjectionComposer._diagnostic` - L713-L716

```python
_diagnostic(self, key: str, **values) -> None
```

Observed calls (lexical order): `RESTART_DIAGNOSTICS.get`, `str`, `self.messages.append`, `template.format`.

Control points:

- L715: `if template`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
