# `converter/postprocess/update_main_flow_rewriter.py`

Source: [converter/postprocess/update_main_flow_rewriter.py](../../../../converter/postprocess/update_main_flow_rewriter.py) | 246 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `d8a988f4205337d0985e72d5fcba4e9f0424b124724d0fb59f80532433a8ee2b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.postprocess.dynamic_metadata_resolver import UpdateProgramContext
from converter.postprocess.main_flow.main_flow_line_utils import MainFlowLineUtils
from converter.postprocess.main_flow.main_flow_locators import MainFlowLocators
from converter.postprocess.main_flow.main_flow_paragraph_resolver import MainFlowParagraphResolver
from converter.postprocess.update_postprocess_line_utils import UpdatePostprocessLineUtils
from rules.update_restart_rules import MAIN_FLOW_CLOSE_LOOKBACK, MAIN_FLOW_DIAGNOSTICS, MAIN_FLOW_INITIALIZE_HELP_TEMPLATE, MAIN_FLOW_OPEN_LOOKBACK, MAIN_FLOW_PERFORM_READ_BODY, MAIN_FLOW_PERFORM_READ_BODY_DOT, MAIN_FLOW_RESTART_TEMPLATE_LINES, MAIN_FLOW_SET_NOT_EOF_TEMPLATE, RESTART_PARAGRAPH_NAMES, UPDATE_MAIN_DATE_INITIALIZATION_LINES, UPDATE_RESTART_DIAGNOSTICS, UPDATE_RESTART_WS_NAMES, UPDATE_SUMMARY_DISPLAY_TEMPLATES
```

## Local dependency notes

- [converter/postprocess/dynamic_metadata_resolver.py](dynamic_metadata_resolver.md)
- [converter/postprocess/main_flow/main_flow_line_utils.py](main_flow/main_flow_line_utils.md)
- [converter/postprocess/main_flow/main_flow_locators.py](main_flow/main_flow_locators.md)
- [converter/postprocess/main_flow/main_flow_paragraph_resolver.py](main_flow/main_flow_paragraph_resolver.md)
- [converter/postprocess/update_postprocess_line_utils.py](update_postprocess_line_utils.md)
- [rules/update_restart_rules.py](../../rules/update_restart_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/update_program_enhancer.py](update_program_enhancer.md)

## Symbol contracts and control points

### `UpdateMainFlowRewriter` - L31-L246

```python
class UpdateMainFlowRewriter(MainFlowLineUtils, MainFlowParagraphResolver, MainFlowLocators)
```

Rewrites update-program main restart flow only.

### `UpdateMainFlowRewriter.__init__` - L44-L45

```python
__init__(self, *, line_utils: UpdatePostprocessLineUtils) -> None
```

### `UpdateMainFlowRewriter.replace_legacy_restart_main_flow` - L47-L118

```python
replace_legacy_restart_main_flow(self, cobol_text, context, diagnostics)
```

Observed calls (lexical order): `diagnostics.append`, `self.line_utils.lines`, `self._find_open_input_index`, `self._find_stop_run_index`, `self._has_legacy_restart_between`, `self._ensure_main_initialization_before_open`, `self.line_utils.join`, `self._resolve_process_paragraph_from_main_flow`, `self._resolve_first_business_paragraph`, `self._main_restart_flow_lines`, `self._ensure_summary_display_before_close`, `self.ensure_processing_paragraph_reads_next`.

Control points:

- L50: `if not context.restart_dclgen`
- L58: `if open_index < 0`
- L63: `if stop_index < 0`
- L67: `if not self._has_legacy_restart_between(lines=lines, start_index=open_index + 1, end_index=stop_index)`
- L90: `if not process_paragraph`

### `UpdateMainFlowRewriter.ensure_processing_paragraph_reads_next` - L120-L169

```python
ensure_processing_paragraph_reads_next(self, *, cobol_text, process_paragraph, diagnostics)
```

Observed calls (lexical order): `diagnostics.append`, `self.line_utils.lines`, `self.line_utils.find_paragraph_range`, `MAIN_FLOW_DIAGNOSTICS['process_not_found'].format`, `self._paragraph_contains_perform_read_flat_file`, `MAIN_FLOW_DIAGNOSTICS['already_reads_next'].format`, `self._read_next_insert_plan`, `MAIN_FLOW_DIAGNOSTICS['no_insertion_point'].format`, `self._line_like`, `MAIN_FLOW_DIAGNOSTICS['read_inserted'].format`, `self.line_utils.join`.

Control points:

- L123: `if not process_paragraph`
- L129: `if not paragraph_range`
- L138: `if self._paragraph_contains_perform_read_flat_file(lines[start:end])`
- L149: `if insert_index < 0`

### `UpdateMainFlowRewriter._ensure_main_initialization_before_open` - L171-L199

```python
_ensure_main_initialization_before_open(self, *, lines, open_index, context, diagnostics)
```

Observed calls (lexical order): `MAIN_FLOW_SET_NOT_EOF_TEMPLATE.format`, `MAIN_FLOW_INITIALIZE_HELP_TEMPLATE.format`, `'\n'.join`, `self._logical`, `self._logical(line).upper`, `max`, `body.upper`, `body.upper().rstrip`, `existing_region.replace`, `self._line_like`, `diagnostics.append`.

Control points:

- L190: `if not missing_bodies`

### `UpdateMainFlowRewriter._ensure_summary_display_before_close` - L201-L234

```python
_ensure_summary_display_before_close(self, *, lines, file_name, diagnostics)
```

Observed calls (lexical order): `self._find_close_input_index`, `'\n'.join`, `self._logical`, `self._logical(line).upper`, `max`, `template.format`, `body.upper`, `body.upper().rstrip`, `existing_region.replace`, `self._line_like`, `diagnostics.append`.

Control points:

- L206: `if close_index < 0`
- L225: `if not missing_bodies`

### `UpdateMainFlowRewriter._main_restart_flow_lines` - L236-L246

```python
_main_restart_flow_lines(self, *, context, process_paragraph)
```

Observed calls (lexical order): `template.format`.

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
