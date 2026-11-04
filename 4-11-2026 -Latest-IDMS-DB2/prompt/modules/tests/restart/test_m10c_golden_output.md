# `tests/restart/test_m10c_golden_output.py`

Source: [tests/restart/test_m10c_golden_output.py](../../../../tests/restart/test_m10c_golden_output.py) | 211 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `62430bff49c151b0f5a2ad41b26af314ed1e5b1ff13c1ee46ffd5a35d8e463d2`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> M10c - the generated program is free of every recorded defect.

## Module-level bindings

`TOTALS` (L43), `LEGACY_TOKENS` (L44), `BANNED_TEXTS` (L45), `WORKING_STORAGE` (L46), `INCLUDE_TEMPLATE` (L47), `GOLDEN_ENV` (L48), `CHECK_IDS` (L49)

## Import declarations

```python
from __future__ import annotations
import os
import pathlib
import pytest
from converter.composers.restart.restart_injection_composer import RestartInjectionComposer
from converter.generators.restart.restart_config import RestartConfig
from converter.generators.restart.restart_name_resolver import RestartNameResolver
from rules.restart_standard_rules import ROLE_COMMIT, ROLE_CONTROL
from tests.restart._checklist import RestartChecklist
```

## Local dependency notes

- [converter/composers/restart/restart_injection_composer.py](../../converter/composers/restart/restart_injection_composer.md)
- [converter/generators/restart/restart_config.py](../../converter/generators/restart/restart_config.md)
- [converter/generators/restart/restart_name_resolver.py](../../converter/generators/restart/restart_name_resolver.md)
- [rules/restart_standard_rules.py](../../rules/restart_standard_rules.md)
- [tests/restart/_checklist.py](_checklist.md)

## Symbol contracts and control points

### `prepared_lines` - L60-L68

```python
prepared_lines(source_lines, role)
```

Observed calls (lexical order): `str`, `str(role.table_name).upper`, `list`, `any`, `str(line).upper`, `enumerate`, `INCLUDE_TEMPLATE.format`, `out.insert`.

Control points:

- L63: `if not any((table in str(line).upper() for line in out))`
- L64: `for (index, line) in enumerate(out)`
- L65: `if WORKING_STORAGE in str(line).upper()`

### `resolved` - L72-L74

```python
resolved(line_utils, prepared_lines, role)
```

Observed calls (lexical order): `RestartNameResolver`, `RestartNameResolver(line_utils).resolve`, `RestartConfig.build`.

### `generated` - L78-L82

```python
generated(line_utils, prepared_lines, role)
```

Observed calls (lexical order): `RestartInjectionComposer`, `RestartInjectionComposer(line_utils).compose`, `'\n'.join`.

### `checklist` - L86-L92

```python
checklist(line_utils, resolved)
```

Observed calls (lexical order): `RestartChecklist`.

### `_inject` - L98-L105

```python
_inject(text: str, statement: str) -> str
```

Put one bad line immediately after PROCEDURE DIVISION.

Observed calls (lexical order): `text.splitlines`, `out.append`, `line.upper`, `'\n'.join`.

Control points:

- L101: `for line in text.splitlines()`
- L103: `if 'PROCEDURE DIVISION' in line.upper()`

### `_inject_into` - L108-L116

```python
_inject_into(text: str, paragraph: str, statement: str) -> str
```

Put one bad line immediately after a paragraph header.

Observed calls (lexical order): `str`, `str(paragraph).upper`, `text.splitlines`, `out.append`, `line.strip`, `line.strip().upper`, `line.strip().upper().endswith`, `'\n'.join`.

Control points:

- L112: `for line in text.splitlines()`
- L114: `if line.strip().upper().endswith(header)`

### `test_the_generated_program_has_no_findings` - L122-L124

```python
test_the_generated_program_has_no_findings(checklist, generated)
```

Observed calls (lexical order): `checklist.inspect`, `'\n'.join`.

### `test_no_single_defect_class_is_present` - L128-L131

```python
test_no_single_defect_class_is_present(checklist, generated, prefix)
```

One assertion per checklist line, so a failure names the defect.

Observed calls (lexical order): `checklist.inspect`, `f.startswith`, `'\n'.join`.

### `test_an_injected_defect_is_detected` - L150-L152

```python
test_an_injected_defect_is_detected(checklist, generated, statement, expected)
```

Observed calls (lexical order): `_inject`, `checklist.inspect`, `any`, `f.startswith`.

### `test_a_per_record_commit_is_detected` - L155-L162

```python
test_a_per_record_commit_is_detected(checklist, generated, resolved)
```

The defect is a COMMIT STATEMENT inside the business paragraph.

Observed calls (lexical order): `_inject_into`, `any`, `checklist.inspect`, `f.startswith`.

### `test_performing_the_commit_paragraph_is_not_a_commit` - L165-L173

```python
test_performing_the_commit_paragraph_is_not_a_commit(checklist, generated, resolved)
```

M7's tail performs a paragraph whose NAME contains COMMIT.

Observed calls (lexical order): `generated.upper`, `resolved.paragraph`, `any`, `checklist.inspect`, `f.startswith`.

### `test_a_removed_stop_run_is_detected` - L176-L180

```python
test_a_removed_stop_run_is_detected(checklist, generated)
```

Observed calls (lexical order): `'\n'.join`, `generated.splitlines`, `line.upper`, `any`, `checklist.inspect`, `f.startswith`.

### `test_a_removed_control_perform_is_detected` - L183-L190

```python
test_a_removed_control_perform_is_detected(checklist, generated, resolved)
```

Observed calls (lexical order): `resolved.paragraph`, `'\n'.join`, `generated.splitlines`, `line.upper`, `any`, `checklist.inspect`, `f.startswith`.

### `test_a_missing_config_is_reported_not_passed` - L193-L196

```python
test_a_missing_config_is_reported_not_passed(line_utils, generated)
```

A skipped check must never read as a clean bill of health.

Observed calls (lexical order): `RestartChecklist`, `any`, `bare.inspect`, `f.startswith`.

### `test_a_generated_artefact_passes_the_checklist` - L202-L211

```python
test_a_generated_artefact_passes_the_checklist(checklist)
```

Observed calls (lexical order): `os.environ.get`, `pytest.skip`, `pathlib.Path`, `source.exists`, `checklist.inspect`, `source.read_text`, `'\n'.join`.

Control points:

- L204: `if not path`
- L207: `if not source.exists()`

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
