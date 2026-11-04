# `converter/pipeline/conversion/conversion_component_factory.py`

Source: [converter/pipeline/conversion/conversion_component_factory.py](../../../../../converter/pipeline/conversion/conversion_component_factory.py) | 679 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `b1b37a42606e6191372f60ae964dea554e3e4417368bb2e44aeeecfdd71223b9`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`__all__` (L679)

## Import declarations

```python
from __future__ import annotations
from converter.composers.cobol_cleanup_composer import CobolCleanupComposer
from converter.composers.cobol_formatter import CobolFormatter
from converter.composers.cursor_close_guarantee_composer import CursorCloseGuaranteeComposer
from converter.composers.cursor_order_cleanup_composer import CursorOrderCleanupComposer
from converter.composers.db2_date_comparison_composer import Db2DateComparisonComposer
from converter.composers.final_cobol_fix_composer import FinalCobolFixComposer, FinalCobolFixComposerConfig
from converter.composers.fixed_format_composer import FixedFormatComposer
from converter.composers.manual_layout_composer import ManualLayoutComposer
from converter.composers.manual_style_preserver import ManualStylePreserver
from converter.composers.record_materialisation_composer import RecordMaterialisationComposer
from converter.composers.restart.restart_line_utils import RestartLineUtils
from converter.composers.restart.restart_stage_adapter import RestartStageAdapter
from converter.composers.retrieval_commit_cleanup_composer import RetrievalCommitCleanupComposer
from converter.composers.sqlcode_wrapper_cleanup_composer import SqlcodeWrapperCleanupComposer
from converter.composers.unnecessary_comments_cleanup_composer import UnnecessaryCommentsCleanupComposer
from converter.composers.update_program_feedback_composer import UpdateProgramFeedbackComposer
from converter.composers.update_restart_skip_composer import UpdateRestartSkipComposer
from converter.domain.models import ConversionInput
from converter.generators.cursor_paragraph_generator import CursorParagraphGenerator
from converter.generators.db2_infrastructure_generator import Db2InfrastructureGenerator
from converter.generators.select_paragraph_generator import SelectParagraphGenerator
from converter.generators.sql_error_generator import SqlErrorGenerator
from converter.generators.sql_generator import SqlGenerator
from converter.generators.timestamp_generator import TimestampGenerator
from converter.pipeline.lrf_host_variable_population import setup_lrf_host_variable_population
from converter.repositories.copybook_repository import CopybookRepository
from converter.repositories.dclgen_repository import DclgenRepository
from converter.repositories.lrf_repository import LrfRepository
from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.column_name_resolver import ColumnNameResolver
from converter.resolvers.cursor_name_resolver import CursorNameResolver
from converter.resolvers.host_variable_resolver import HostVariableResolver
from converter.resolvers.lrf_path_resolver import LrfPathResolver
from converter.resolvers.record_context_resolver import RecordContextResolver
from converter.resolvers.table_name_resolver import TableNameResolver
from converter.transformers.cobol_transformer import CobolTransformer
from converter.analyzers.lr_access.lr_access_analyser import LrAccessAnalyser
from converter.transformers.field_reference_rewriter import FieldReferenceRewriter
from converter.transformers.idms_statement_transformer import IdmsStatementTransformer
from converter.transformers.lr_status_token_replacer import LrStatusTokenReplacer
from converter.rules.common_rules import TRANSFORMER_LR_STATUS_REPLACER, TRANSFORMER_LRF_PATH_EXPANDER, TRANSFORMER_LRF_UPDATE_EXPANDER
from converter.transformers.lrf_path_expander import LrfPathExpander
from patterns.idms_patterns import IDMS_WRITE_VERB_PATTERN
from rules.final_feedback_fix_rules import DEFAULT_DB2_DATE_EXTERNAL_FORMAT, ORDER_BY_COLUMNS_IN_SELECT_DEFAULT
from rules.idms_transformer_messages import TRANSFORMER_MESSAGES
from converter.transformers.lrf_update_expander import LrfUpdateExpander
```

## Local dependency notes

- [converter/analyzers/lr_access/lr_access_analyser.py](../../analyzers/lr_access/lr_access_analyser.md)
- [converter/composers/cobol_cleanup_composer.py](../../composers/cobol_cleanup_composer.md)
- [converter/composers/cobol_formatter.py](../../composers/cobol_formatter.md)
- [converter/composers/cursor_close_guarantee_composer.py](../../composers/cursor_close_guarantee_composer.md)
- [converter/composers/cursor_order_cleanup_composer.py](../../composers/cursor_order_cleanup_composer.md)
- [converter/composers/db2_date_comparison_composer.py](../../composers/db2_date_comparison_composer.md)
- [converter/composers/final_cobol_fix_composer.py](../../composers/final_cobol_fix_composer.md)
- [converter/composers/fixed_format_composer.py](../../composers/fixed_format_composer.md)
- [converter/composers/manual_layout_composer.py](../../composers/manual_layout_composer.md)
- [converter/composers/manual_style_preserver.py](../../composers/manual_style_preserver.md)
- [converter/composers/record_materialisation_composer.py](../../composers/record_materialisation_composer.md)
- [converter/composers/restart/restart_line_utils.py](../../composers/restart/restart_line_utils.md)
- [converter/composers/restart/restart_stage_adapter.py](../../composers/restart/restart_stage_adapter.md)
- [converter/composers/retrieval_commit_cleanup_composer.py](../../composers/retrieval_commit_cleanup_composer.md)
- [converter/composers/sqlcode_wrapper_cleanup_composer.py](../../composers/sqlcode_wrapper_cleanup_composer.md)
- [converter/composers/unnecessary_comments_cleanup_composer.py](../../composers/unnecessary_comments_cleanup_composer.md)
- [converter/composers/update_program_feedback_composer.py](../../composers/update_program_feedback_composer.md)
- [converter/composers/update_restart_skip_composer.py](../../composers/update_restart_skip_composer.md)
- [converter/domain/models.py](../../domain/models.md)
- [converter/generators/cursor_paragraph_generator.py](../../generators/cursor_paragraph_generator.md)
- [converter/generators/db2_infrastructure_generator.py](../../generators/db2_infrastructure_generator.md)
- [converter/generators/select_paragraph_generator.py](../../generators/select_paragraph_generator.md)
- [converter/generators/sql_error_generator.py](../../generators/sql_error_generator.md)
- [converter/generators/sql_generator.py](../../generators/sql_generator.md)
- [converter/generators/timestamp_generator.py](../../generators/timestamp_generator.md)
- [converter/pipeline/lrf_host_variable_population.py](../lrf_host_variable_population.md)
- [converter/repositories/copybook_repository.py](../../repositories/copybook_repository.md)
- [converter/repositories/dclgen_repository.py](../../repositories/dclgen_repository.md)
- [converter/repositories/lrf_repository.py](../../repositories/lrf_repository.md)
- [converter/repositories/mapping_repository.py](../../repositories/mapping_repository.md)
- [converter/resolvers/column_name_resolver.py](../../resolvers/column_name_resolver.md)
- [converter/resolvers/cursor_name_resolver.py](../../resolvers/cursor_name_resolver.md)
- [converter/resolvers/host_variable_resolver.py](../../resolvers/host_variable_resolver.md)
- [converter/resolvers/lrf_path_resolver.py](../../resolvers/lrf_path_resolver.md)
- [converter/resolvers/record_context_resolver.py](../../resolvers/record_context_resolver.md)
- [converter/resolvers/table_name_resolver.py](../../resolvers/table_name_resolver.md)
- [converter/rules/common_rules.py](../../rules/common_rules.md)
- [converter/transformers/cobol_transformer.py](../../transformers/cobol_transformer.md)
- [converter/transformers/field_reference_rewriter.py](../../transformers/field_reference_rewriter.md)
- [converter/transformers/idms_statement_transformer.py](../../transformers/idms_statement_transformer.md)
- [converter/transformers/lr_status_token_replacer.py](../../transformers/lr_status_token_replacer.md)
- [converter/transformers/lrf_path_expander.py](../../transformers/lrf_path_expander.md)
- [converter/transformers/lrf_update_expander.py](../../transformers/lrf_update_expander.md)
- [patterns/idms_patterns.py](../../../patterns/idms_patterns.md)
- [rules/final_feedback_fix_rules.py](../../../rules/final_feedback_fix_rules.md)
- [rules/idms_transformer_messages.py](../../../rules/idms_transformer_messages.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion_service.py](../conversion_service.md)

## Symbol contracts and control points

### `ConversionComponentFactory` - L97-L676

```python
class ConversionComponentFactory()
```

Builds repositories, resolvers, generators, transformers, composers.

### `ConversionComponentFactory.__init__` - L258-L268

```python
__init__(self) -> None
```

### `ConversionComponentFactory._remember_source` - L273-L277

```python
_remember_source(self, conversion_input: ConversionInput | None) -> None
```

Record the SOURCE program text for kind classification.

Observed calls (lexical order): `getattr`, `str`, `bool`, `text.strip`.

### `ConversionComponentFactory._program_is_update` - L279-L301

```python
_program_is_update(self, conversion_input: ConversionInput | None=None) -> bool
```

True when the SOURCE contains IDMS write verbs.

Observed calls (lexical order): `getattr`, `str`, `text.strip`, `IDMS_WRITE_VERB_PATTERN.search`, `bool`.

Control points:

- L292: `if conversion_input is not None`
- L294: `if text.strip()`
- L297: `if not self._source_known`

### `ConversionComponentFactory._repositories` - L306-L322

```python
_repositories(self, conversion_input: ConversionInput) -> dict[str, object]
```

Observed calls (lexical order): `self._remember_source`, `MappingRepository`, `DclgenRepository`, `CopybookRepository`, `LrfRepository`, `getattr`.

### `ConversionComponentFactory._resolvers` - L327-L364

```python
_resolvers(self, repositories: dict[str, object]) -> dict[str, object]
```

Observed calls (lexical order): `TableNameResolver`, `ColumnNameResolver`, `HostVariableResolver`, `RecordContextResolver`, `CursorNameResolver`, `LrfPathResolver`, `repositories.get`.

### `ConversionComponentFactory._generators` - L369-L411

```python
_generators(self, repositories, resolvers) -> dict[str, object]
```

Observed calls (lexical order): `SqlErrorGenerator`, `SqlGenerator`, `Db2InfrastructureGenerator`, `CursorParagraphGenerator`, `self._wire_lrf_host_variable_population`, `TimestampGenerator`, `SelectParagraphGenerator`.

### `ConversionComponentFactory._wire_lrf_host_variable_population` - L416-L461

```python
_wire_lrf_host_variable_population(self, *, cursor_paragraph_generator, repositories, resolvers) -> bool
```

Attach the LRF host-variable populator. Report every outcome.

Observed calls (lexical order): `setup_lrf_host_variable_population`, `repositories.get`, `self._report_lrf_wiring`, `type`.

Control points:

- L452: `if attached is False`

### `ConversionComponentFactory._report_lrf_wiring` - L463-L474

```python
_report_lrf_wiring(self, cursor_paragraph_generator, text: str) -> None
```

Send a wiring diagnostic to the component that lost the feature.

Observed calls (lexical order): `self.messages.append`, `getattr`, `isinstance`, `messages.append`.

Control points:

- L473: `if isinstance(messages, list)`

### `ConversionComponentFactory._transformers` - L479-L532

```python
_transformers(self, repositories, resolvers, generators, conversion_input: ConversionInput | None=None) -> dict[str, object]
```

Build the transformer map.

Observed calls (lexical order): `IdmsStatementTransformer`, `self._apply_commit_policy`, `CobolTransformer`, `LrAccessAnalyser`, `FieldReferenceRewriter`, `LrfPathExpander`, `LrfUpdateExpander`, `LrStatusTokenReplacer`.

### `ConversionComponentFactory._apply_commit_policy` - L534-L565

```python
_apply_commit_policy(self, *, transformer, conversion_input: ConversionInput | None=None) -> None
```

Observed calls (lexical order): `self._program_is_update`, `getattr`, `messages.append`, `TRANSFORMER_MESSAGES['program_kind'].format`.

Control points:

- L549: `if messages is None`
- L552: `if not published`

### `ConversionComponentFactory._composers` - L570-L585

```python
_composers(self, repositories, resolvers, conversion_input: ConversionInput | None=None) -> dict[str, object]
```

Observed calls (lexical order): `composers.update`, `self._formatting_composers`, `self._cursor_composers`, `self._cleanup_composers`, `self._update_composers`, `self._restart_composers`, `self._final_fix_composers`.

### `ConversionComponentFactory._formatting_composers` - L587-L593

```python
_formatting_composers(self) -> dict[str, object]
```

Observed calls (lexical order): `CobolFormatter`, `FixedFormatComposer`, `ManualLayoutComposer`, `ManualStylePreserver`.

### `ConversionComponentFactory._cursor_composers` - L595-L604

```python
_cursor_composers(self) -> dict[str, object]
```

Observed calls (lexical order): `CursorCloseGuaranteeComposer`, `CursorOrderCleanupComposer`, `SqlcodeWrapperCleanupComposer`, `Db2DateComparisonComposer`.

### `ConversionComponentFactory._cleanup_composers` - L606-L634

```python
_cleanup_composers(self, repositories, resolvers, conversion_input: ConversionInput | None=None) -> dict[str, object]
```

Observed calls (lexical order): `CobolCleanupComposer`, `RetrievalCommitCleanupComposer`, `self._program_is_update`, `UnnecessaryCommentsCleanupComposer`, `UpdateRestartSkipComposer`, `RecordMaterialisationComposer`.

### `ConversionComponentFactory._update_composers` - L636-L644

```python
_update_composers(self, repositories, resolvers) -> dict[str, object]
```

Observed calls (lexical order): `UpdateProgramFeedbackComposer`.

### `ConversionComponentFactory._restart_composers` - L646-L664

```python
_restart_composers(self, repositories, resolvers) -> dict[str, object]
```

Restart control injection for an update program.

Observed calls (lexical order): `RestartStageAdapter`, `RestartLineUtils`.

### `ConversionComponentFactory._final_fix_composers` - L666-L676

```python
_final_fix_composers(self) -> dict[str, object]
```

Observed calls (lexical order): `FinalCobolFixComposer`, `FinalCobolFixComposerConfig`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
