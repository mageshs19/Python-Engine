# `tests/test_business_control_flag_analyzer.py`

Source: [tests/test_business_control_flag_analyzer.py](../../../tests/test_business_control_flag_analyzer.py) | 66 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `53494872339b4a501b78c979a4b47b906eba3c85810ff8642fce0c54b8d67346`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.composers.cleanup.business_control_flag_analyzer import BusinessControlFlagAnalyzer
```

## Local dependency notes

- [converter/composers/cleanup/business_control_flag_analyzer.py](../converter/composers/cleanup/business_control_flag_analyzer.md)

## Symbol contracts and control points

### `test_discovers_flag_declaration_and_trigger_condition_without_name_rule` - L6-L22

```python
test_discovers_flag_declaration_and_trigger_condition_without_name_rule()
```

Observed calls (lexical order): `BusinessControlFlagAnalyzer`, `BusinessControlFlagAnalyzer().analyze`.

### `test_discovery_returns_none_when_multiple_flags_have_equal_evidence` - L25-L38

```python
test_discovery_returns_none_when_multiple_flags_have_equal_evidence()
```

Observed calls (lexical order): `BusinessControlFlagAnalyzer`, `analyzer.discover_unique_yes_flag`, `source.splitlines`.

### `test_discovery_ignores_flags_not_assigned_in_the_requested_scope` - L41-L53

```python
test_discovery_ignores_flags_not_assigned_in_the_requested_scope()
```

Observed calls (lexical order): `BusinessControlFlagAnalyzer`, `analyzer.discover_unique_yes_flag`, `source.splitlines`.

### `test_flag_name_does_not_need_sw_status_prefix` - L56-L66

```python
test_flag_name_does_not_need_sw_status_prefix()
```

Observed calls (lexical order): `BusinessControlFlagAnalyzer`, `analyzer.discover_unique_yes_flag`, `source.splitlines`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
