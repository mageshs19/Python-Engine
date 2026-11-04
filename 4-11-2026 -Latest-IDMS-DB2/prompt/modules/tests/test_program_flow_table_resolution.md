# `tests/test_program_flow_table_resolution.py`

Source: [tests/test_program_flow_table_resolution.py](../../../tests/test_program_flow_table_resolution.py) | 44 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `4324743661f678e3605fe94682682be202569d7f9a4a47508c4e564d3fdcf8d1`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Program-flow diagnostics must use the shared DB2 table resolver.

## Import declarations

```python
from converter.analyzers.program_flow.program_flow_analyzer import ProgramFlowAnalyzer
from converter.domain.models import IdmsOperation
```

## Local dependency notes

- [converter/analyzers/program_flow/program_flow_analyzer.py](../converter/analyzers/program_flow/program_flow_analyzer.md)
- [converter/domain/models.py](../converter/domain/models.md)

## Symbol contracts and control points

### `FakeTableResolver` - L7-L9

```python
class FakeTableResolver()
```

### `FakeTableResolver.table_for_record` - L8-L9

```python
table_for_record(self, record_name: str) -> str
```

Observed calls (lexical order): `{'VMBEVEF': 'DZBEVEFTV'}.get`.

### `test_flow_analyzer_resolves_record_to_db2_table_and_uses_table_cursor_name` - L12-L32

```python
test_flow_analyzer_resolves_record_to_db2_table_and_uses_table_cursor_name()
```

Observed calls (lexical order): `FakeTableResolver`, `ProgramFlowAnalyzer`, `analyzer.analyze`, `IdmsOperation`, `len`, `any`, `item.lower`.

### `test_flow_analyzer_reports_missing_table_mapping_without_inventing_one` - L35-L44

```python
test_flow_analyzer_reports_missing_table_mapping_without_inventing_one()
```

Observed calls (lexical order): `FakeTableResolver`, `ProgramFlowAnalyzer`, `analyzer.analyze`, `IdmsOperation`, `any`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
