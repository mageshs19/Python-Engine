# `tests/spec_builder/test_cursor_spec_builder_lrf_extra_filters.py`

Source: [tests/spec_builder/test_cursor_spec_builder_lrf_extra_filters.py](../../../../tests/spec_builder/test_cursor_spec_builder_lrf_extra_filters.py) | 113 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `9fa590750e0a1e485596f5b246eaa8ecf486bde13dd1a246b47bc18aac70f266`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from types import SimpleNamespace
from converter.generators.db2_infrastructure.spec_builder.cursor_spec_builder import CursorSpecBuilder
from converter.generators.db2_infrastructure.spec_builder.spec_build_context import SpecBuildContext
from converter.generators.db2_infrastructure.spec_builder.spec_lrf_scanner import SpecLrfScanner
from converter.generators.db2_infrastructure.spec_builder.spec_navigation_scanner import SpecNavigationScanner
```

## Local dependency notes

- [converter/generators/db2_infrastructure/spec_builder/cursor_spec_builder.py](../../converter/generators/db2_infrastructure/spec_builder/cursor_spec_builder.md)
- [converter/generators/db2_infrastructure/spec_builder/spec_build_context.py](../../converter/generators/db2_infrastructure/spec_builder/spec_build_context.md)
- [converter/generators/db2_infrastructure/spec_builder/spec_lrf_scanner.py](../../converter/generators/db2_infrastructure/spec_builder/spec_lrf_scanner.md)
- [converter/generators/db2_infrastructure/spec_builder/spec_navigation_scanner.py](../../converter/generators/db2_infrastructure/spec_builder/spec_navigation_scanner.md)

## Symbol contracts and control points

### `fixed` - L8-L9

```python
fixed(body, indicator=' ')
```

### `Mapping` - L12-L18

```python
class Mapping()
```

### `Mapping.__init__` - L13-L14

```python
__init__(self, rows)
```

### `Mapping.rows_for_record` - L16-L18

```python
rows_for_record(self, record)
```

### `_builder` - L21-L25

```python
_builder(mapping)
```

Observed calls (lexical order): `CursorSpecBuilder.__new__`, `SimpleNamespace`.

### `_source` - L28-L46

```python
_source()
```

Observed calls (lexical order): `'\n'.join`, `fixed`.

### `test_actual_modular_cursor_spec_builder_adds_both_vmdz1526_path_filters` - L49-L78

```python
test_actual_modular_cursor_spec_builder_adds_both_vmdz1526_path_filters()
```

Observed calls (lexical order): `Mapping`, `SimpleNamespace`, `_builder`, `_source`, `builder._apply_lrf_extra_filters`, `len`.

### `test_lrf_extra_filter_mapping_failure_fails_closed_in_real_spec_path` - L81-L88

```python
test_lrf_extra_filter_mapping_failure_fails_closed_in_real_spec_path()
```

Observed calls (lexical order): `Mapping`, `_builder`, `_source`, `builder._apply_lrf_extra_filters`, `any`.

### `test_lrf_scanner_uses_expanded_source_when_transformed_output_drops_markers` - L91-L113

```python
test_lrf_scanner_uses_expanded_source_when_transformed_output_drops_markers()
```

Observed calls (lexical order): `SpecBuildContext.create`, `object`, `SpecNavigationScanner`, `SpecLrfScanner`, `_source`, `SpecLrfScanner().cursors`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
