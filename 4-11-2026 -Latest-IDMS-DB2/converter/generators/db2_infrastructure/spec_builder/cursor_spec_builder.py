"""Facade for DB2 cursor specification construction.

The public API remains stable:

- build()
- include_names()
- spec_messages()
- _augment_select_columns()

Dependencies used only by build() or reporting are created lazily.
This preserves support for minimal owners used by augmentation tests.
"""

from __future__ import annotations

from converter.analyzers.field_usage_analyzer import FieldUsageAnalyzer
from converter.domain.models import IdmsOperation
from converter.generators.db2_infrastructure.spec_builder.spec_build_context import (
    SpecBuildContext,
)
from converter.generators.db2_infrastructure.spec_builder.spec_factory import (
    SpecFactory,
)
from converter.generators.db2_infrastructure.spec_builder.spec_lrf_scanner import (
    SpecLrfScanner,
)
from converter.generators.db2_infrastructure.spec_builder.spec_navigation_scanner import (
    SpecNavigationScanner,
)
from converter.generators.db2_infrastructure.spec_builder.spec_parent_classifier import (
    SpecParentClassifier,
)
from converter.generators.db2_infrastructure.spec_builder.spec_relationship_policy import (
    SpecRelationshipPolicy,
)
from converter.generators.db2_infrastructure.spec_builder.spec_reporter import (
    SpecReporter,
)
from converter.generators.db2_infrastructure.spec_builder.spec_select_augmenter import (
    SpecSelectAugmenter,
)
from converter.generators.db2_infrastructure.spec_builder.spec_where_builder import (
    SpecWhereBuilder,
)
from converter.services.name_normalizer import NameNormalizer


class CursorSpecBuilder:
    """Builds and augments DB2 cursor specification dictionaries."""

    def __init__(self, owner) -> None:
        self.owner = owner

        self.navigation = SpecNavigationScanner()
        self.lrf = SpecLrfScanner()
        self.parent_classifier = SpecParentClassifier()

        self.where = SpecWhereBuilder(
            dclgen_repository=getattr(
                owner,
                "dclgen_repository",
                None,
            ),
        )
        self.augmenter = SpecSelectAugmenter(
            host_variable_resolver=owner.host_variable_resolver,
            where_builder=self.where,
        )

        self._relationship_policy: SpecRelationshipPolicy | None = None
        self._factory: SpecFactory | None = None
        self._reporter: SpecReporter | None = None

        self.messages: list[str] = []

    @property
    def relationship_policy(self) -> SpecRelationshipPolicy:
        """Create relationship policy only for a complete build."""
        if self._relationship_policy is None:
            resolver = getattr(
                self.owner,
                "relationship_resolver",
                None,
            )
            if resolver is None:
                raise AttributeError(
                    "CursorSpecBuilder.build() requires "
                    "owner.relationship_resolver"
                )

            self._relationship_policy = SpecRelationshipPolicy(
                relationship_resolver=resolver,
                where_builder=self.where,
            )

        return self._relationship_policy

    @property
    def factory(self) -> SpecFactory:
        """Create the spec factory only when build() is called."""
        if self._factory is None:
            self._factory = SpecFactory(
                owner=self.owner,
                relationship_policy=self.relationship_policy,
                parent_classifier=self.parent_classifier,
            )

        return self._factory

    @property
    def reporter(self) -> SpecReporter:
        """Create reporter only when report output is requested."""
        if self._reporter is None:
            line_utils = getattr(self.owner, "line_utils", None)
            if line_utils is None:
                raise AttributeError(
                    "Cursor reporting requires owner.line_utils"
                )

            self._reporter = SpecReporter(line_utils)

        return self._reporter

    def build(
        self,
        operations: list[IdmsOperation],
        cobol_text: str = "",
        field_usage_analysis=None,
        lrf_source_text: str | None = None,
    ) -> list[dict[str, object]]:
        """Build and augment cursor specifications."""
        self._reset_messages()

        usage = field_usage_analysis
        if usage is None:
            usage = self._field_usage(cobol_text)

        context = SpecBuildContext.create(
            operations=operations,
            cobol_text=cobol_text,
            field_usage_analysis=usage,
            navigation=self.navigation,
            lrf=self.lrf,
            lrf_source_text=lrf_source_text,
        )

        specs = self.factory.build(context)
        self._apply_lrf_extra_filters(
            specs,
            lrf_source_text if lrf_source_text is not None else cobol_text,
        )
        self._augment_select_columns(specs)

        self.messages.extend(self.relationship_policy.messages)
        self.messages.extend(self.where.messages)

        return specs

    def _apply_lrf_extra_filters(
        self,
        specs: list[dict[str, object]],
        cobol_text: str,
    ) -> None:
        """Push source-proven LRF path filters into the actual cursor specs.

        The older LRF-aware builder patch is not used by this modular
        ``CursorSpecBuilder``.  Without this integration, the scanner sees the
        LRF FIRST marker but the generated cursor keeps only the parent/child
        relationship predicates; business path filters such as
        ``CT-RK-TEVPR = '0168'`` and ``CT-RK-TGDSV = '0219'`` are lost.

        Filters are mapped through the Sheet Mapping repository. If a source
        filter exists but cannot be mapped unambiguously, use ``1 = 0`` rather
        than silently widening the database access.
        """
        if not specs or not cobol_text:
            return

        from converter.resolvers.lrf_cursor_where_resolver import (
            LrfCursorWhereResolver,
        )

        resolver = LrfCursorWhereResolver(
            mapping_repository=getattr(self.owner, "mapping_repository", None)
        )
        lrf_info_by_record = resolver.extract_lrf_cursors_from_cobol(cobol_text)
        if not lrf_info_by_record:
            return

        for spec in specs:
            record = NameNormalizer.normalize(spec.get("record_name", ""))
            info = lrf_info_by_record.get(record)
            if not info:
                continue

            extra_text = str(info.get("extra_filters", "") or "").strip()
            if not extra_text:
                continue

            conditions = resolver.extra_filter_conditions_for_lrf_cursor(
                record, info
            )
            existing = list(spec.get("where_conditions", []) or [])
            if conditions is None:
                # Fail closed: never emit an unfiltered or partially filtered
                # LRF cursor when source-proven business predicates are lost.
                if "1 = 0" not in existing:
                    existing.append("1 = 0")
                spec["where_conditions"] = existing
                self.messages.extend(resolver.messages)
                continue

            seen = {str(item).strip().upper() for item in existing}
            for condition in conditions:
                key = str(condition).strip().upper()
                if key and key not in seen:
                    existing.append(condition)
                    seen.add(key)
            spec["where_conditions"] = existing

        self.messages.extend(resolver.messages)

    def _augment_select_columns(
        self,
        specs: list[dict[str, object]],
    ) -> None:
        """Backward-compatible select-column augmentation entry point."""
        self.augmenter.augment(specs)

    def include_names(
        self,
        cursor_specs: list[dict[str, object]],
    ) -> list[str]:
        """Return DCLGEN include names."""
        return self.reporter.include_names(cursor_specs)

    def spec_messages(
        self,
        cursor_specs: list[dict[str, object]],
    ) -> list[str]:
        """Return completed-spec diagnostics."""
        return self.reporter.messages(cursor_specs)

    def _field_usage(self, cobol_text: str):
        mapping_repository = getattr(
            self.owner,
            "mapping_repository",
            None,
        )
        table_name_resolver = getattr(
            self.owner,
            "table_name_resolver",
            None,
        )

        if mapping_repository is None:
            raise AttributeError(
                "CursorSpecBuilder.build() requires "
                "owner.mapping_repository"
            )

        if table_name_resolver is None:
            raise AttributeError(
                "CursorSpecBuilder.build() requires "
                "owner.table_name_resolver"
            )

        return FieldUsageAnalyzer(
            mapping_repository=mapping_repository,
            table_name_resolver=table_name_resolver,
        ).analyze(cobol_text)

    def _reset_messages(self) -> None:
        self.messages = []
        self.where.messages = []

        if self._relationship_policy is not None:
            self._relationship_policy.messages = []


__all__ = ["CursorSpecBuilder"]