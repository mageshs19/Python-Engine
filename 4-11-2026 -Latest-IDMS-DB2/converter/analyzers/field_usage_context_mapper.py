from __future__ import annotations

from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.table_name_resolver import TableNameResolver
from converter.services.name_normalizer import NameNormalizer
from rules.field_usage_rules import DCLGEN_GROUP_PREFIX


class FieldUsageContextMapper:
    """
    Builds reusable record and DCLGEN-group context for field usage analysis.
    """

    def __init__(
        self,
        *,
        mapping_repository: MappingRepository,
        table_name_resolver: TableNameResolver,
    ) -> None:
        self.mapping_repository = mapping_repository
        self.table_name_resolver = table_name_resolver

    def mapping_records(
        self,
    ) -> set[str]:
        try:
            return {
                NameNormalizer.normalize(record)
                for record in self.mapping_repository.records()
                if NameNormalizer.normalize(record)
            }
        except Exception:
            return set()

    def unique_source_field_to_record_map(self) -> dict[str, str]:
        """Map an unqualified COBOL field to one record only when unique.

        Legacy IDMS programs often reference fields without ``OF record``
        because copybook data names are globally unique in that program.  A
        cursor still has to fetch those fields.  Ambiguous names are omitted
        deliberately; guessing a record would widen the wrong cursor.
        """
        owners: dict[str, set[str]] = {}
        for record in self.mapping_records():
            for row in self.mapping_repository.rows_for_record(record) or []:
                for raw in (
                    getattr(row, "cobol_zone", ""),
                    getattr(row, "reference_field_name_copybook", ""),
                ):
                    text = " ".join(str(raw or "").replace(".", " ").split())
                    if not text:
                        continue
                    parts = text.split()
                    if len(parts) > 1 and parts[0].isdigit():
                        parts = parts[1:]
                    if not parts:
                        continue
                    field = NameNormalizer.normalize(parts[0])
                    if field:
                        owners.setdefault(field, set()).add(record)
        return {field: next(iter(records)) for field, records in owners.items() if len(records) == 1}

    def group_to_record_map(
        self,
    ) -> dict[str, str]:
        output: dict[str, str] = {}

        for record in self.mapping_records():
            normalized_record = NameNormalizer.normalize(record)
            table = self.table_name_resolver.table_for_record(normalized_record)

            if not table:
                continue

            group = DCLGEN_GROUP_PREFIX + NameNormalizer.to_cobol(table)
            output[NameNormalizer.normalize(group)] = normalized_record

        return output