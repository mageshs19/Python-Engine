from __future__ import annotations

from converter.analyzers.field_usage_analyzer import FieldUsageAnalysis
from converter.repositories.mapping_repository import MappingRepository
from converter.services.name_normalizer import NameNormalizer


class CursorFieldUsageColumnSelector:
    """
    Resolves cursor SELECT columns from procedure field usage.

    This helper maps COBOL source fields or DCLGEN host fields back to DB2
    columns using Sheet Mapping metadata.
    """

    def __init__(
        self,
        mapping_repository: MappingRepository,
    ) -> None:
        self.mapping_repository = mapping_repository

    def columns_from_field_usage(
        self,
        record_name: str,
        field_usage_analysis: FieldUsageAnalysis | None,
    ) -> list[str]:
        if field_usage_analysis is None:
            return []

        usage = field_usage_analysis.usage_by_record.get(
            NameNormalizer.normalize(record_name)
        )

        if usage is None:
            return []

        output: list[str] = []

        # Sort the field set so SELECT/FETCH column order is deterministic
        # run-to-run (a set iterates in a hash-seed-dependent order).
        for field_name in sorted(usage.all_fields):
            column = self.column_for_source_or_host_field(
                record_name=record_name,
                source_or_host_field=field_name,
            )

            if column:
                output.append(column)
                continue

            # A source group can have no DB2 column of its own while its
            # mapped descendants do. The LRF group-move decomposer expands
            # such a MOVE after cursor specs are built, so the SELECT must
            # project the descendant columns before that later rewrite.
            # Example: MOVE NR-CI OF VMBEVEF ... becomes moves from
            # NR-CI-1-POS and NR-CI-2-6-POS. Selecting only fields visible
            # in the original group reference silently leaves those hosts
            # unpopulated. This is mapping-driven, not program-specific.
            output.extend(
                self.columns_for_group_field(
                    record_name=record_name,
                    source_group_field=field_name,
                )
            )

        return self._unique(output)

    def column_for_source_or_host_field(
        self,
        record_name: str,
        source_or_host_field: str,
    ) -> str:
        record = NameNormalizer.normalize(record_name)
        source = NameNormalizer.normalize(source_or_host_field)

        if not record or not source:
            return ""

        rows = self.mapping_repository.rows_for_record(record)

        for row in rows:
            target_column = NameNormalizer.normalize(
                getattr(row, "new_db2_field_name", "")
                or getattr(row, "cross_application_db2_field_name", "")
            )

            if not target_column:
                continue

            source_candidates = {
                NameNormalizer.normalize(
                    self.extract_source_field(getattr(row, "cobol_zone", ""))
                ),
                NameNormalizer.normalize(
                    self.extract_source_field(
                        getattr(row, "reference_field_name_copybook", "")
                    )
                ),
                target_column,
                NameNormalizer.normalize(NameNormalizer.to_cobol(target_column)),
            }

            source_candidates = {
                candidate
                for candidate in source_candidates
                if candidate
            }

            if source in source_candidates:
                return target_column

        return ""


    def columns_for_group_field(
        self,
        *,
        record_name: str,
        source_group_field: str,
    ) -> list[str]:
        """Return mapped descendant columns for a source group without a column.

        Mapping rows retain COBOL level numbers in ``cobol_zone``. A group
        row is expandable only when it has no target DB2 column; descendants
        are collected until the next row at the same or a shallower level.
        This avoids treating a single-column field as a group and keeps the
        expansion bounded to the group declared by the mapping sheet.
        """
        record = NameNormalizer.normalize(record_name)
        source = NameNormalizer.normalize(source_group_field)
        if not record or not source:
            return []

        rows = self.mapping_repository.rows_for_record(record) or []
        group_index = -1
        group_level = -1

        for index, row in enumerate(rows):
            zone = str(getattr(row, "cobol_zone", "") or "").strip()
            level, field = self._level_and_field(zone)
            if field != source:
                continue
            target = NameNormalizer.normalize(
                getattr(row, "new_db2_field_name", "")
                or getattr(row, "cross_application_db2_field_name", "")
            )
            # Only a target-less source group can be expanded to children.
            if target or level is None:
                continue
            group_index, group_level = index, level
            break

        if group_index < 0:
            return []

        columns: list[str] = []
        for row in rows[group_index + 1:]:
            level, _field = self._level_and_field(
                str(getattr(row, "cobol_zone", "") or "")
            )
            if level is not None and level <= group_level:
                break
            target = NameNormalizer.normalize(
                getattr(row, "new_db2_field_name", "")
                or getattr(row, "cross_application_db2_field_name", "")
            )
            source_field = self.extract_source_field(
                getattr(row, "cobol_zone", "")
            ) or self.extract_source_field(
                getattr(row, "reference_field_name_copybook", "")
            )
            if target and source_field:
                columns.append(target)

        return self._unique(columns)

    @staticmethod
    def _level_and_field(value: str) -> tuple[int | None, str]:
        text = str(value or "").strip().replace(".", " ")
        tokens = text.split()
        if not tokens:
            return None, ""
        if tokens[0].isdigit() and len(tokens) > 1:
            return int(tokens[0]), NameNormalizer.normalize(tokens[1])
        return None, NameNormalizer.normalize(tokens[0])

    def extract_source_field(
        self,
        value: str,
    ) -> str:
        text = str(value or "").strip()

        if not text:
            return ""

        text = text.replace(".", " ")
        tokens = text.split()

        if tokens and tokens[0].isdigit() and len(tokens) > 1:
            return tokens[1]

        if tokens:
            return tokens[0]

        return ""

    def _unique(
        self,
        values: list[str],
    ) -> list[str]:
        output: list[str] = []
        seen: set[str] = set()

        for value in values:
            normalized = NameNormalizer.normalize(value)

            if not normalized:
                continue

            if normalized in seen:
                continue

            seen.add(normalized)
            output.append(normalized)

        return output