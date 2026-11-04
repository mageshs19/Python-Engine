# LOCATION: converter/repositories/lrf_repository.py
# ACTION: CREATE NEW FILE
"""Read-only lookups over parsed LRF metadata."""

from __future__ import annotations

from converter.domain.models import LogicalRecord, LrfPath
from converter.services.name_normalizer import NameNormalizer
from rules.lrf_rules import PATH_GROUP_ERASE, PATH_GROUP_OBTAIN


class LrfRepository:
    def __init__(self, logical_records: list[LogicalRecord] | None = None) -> None:
        self._records = list(logical_records or [])
        self._by_name = {
            NameNormalizer.normalize(r.logical_record_name): r
            for r in self._records
        }

    def is_empty(self) -> bool:
        return not self._records

    def names(self) -> list[str]:
        return [r.logical_record_name for r in self._records]

    def get(self, logical_record_name: str) -> LogicalRecord | None:
        return self._by_name.get(NameNormalizer.normalize(logical_record_name))

    def element_records(self, logical_record_name: str) -> list[str]:
        record = self.get(logical_record_name)
        return list(record.element_records) if record else []

    def path_for_keyword(
        self,
        keyword: str,
        logical_record_name: str | None = None,
    ) -> LrfPath | None:
        """Resolve a keyword without silently crossing logical-record scope.

        Some subschemas can contain the same keyword under different logical
        records. When the caller knows the LR, use that scope. When it does
        not, return a path only if the keyword resolves uniquely; choosing the
        first matching path would silently convert against unrelated metadata.
        """
        wanted = NameNormalizer.normalize(keyword)
        wanted_lr = NameNormalizer.normalize(logical_record_name or "")
        matches = [
            path
            for record in self._records
            if not wanted_lr
            or NameNormalizer.normalize(record.logical_record_name) == wanted_lr
            for path in record.paths
            if NameNormalizer.normalize(path.keyword) == wanted
        ]
        if len(matches) != 1:
            return None
        return matches[0]

    def obtain_paths(self, logical_record_name: str) -> list[LrfPath]:
        return self._paths(logical_record_name, PATH_GROUP_OBTAIN)

    def erase_paths(self, logical_record_name: str) -> list[LrfPath]:
        return self._paths(logical_record_name, PATH_GROUP_ERASE)

    def owns_record(self, record_name: str) -> list[str]:
        """Which logical records include this IDMS record as an element."""
        wanted = NameNormalizer.normalize(record_name)
        return [
            r.logical_record_name
            for r in self._records
            if any(NameNormalizer.normalize(e) == wanted for e in r.element_records)
        ]

    def _paths(self, logical_record_name: str, verb: str) -> list[LrfPath]:
        record = self.get(logical_record_name)
        if not record:
            return []
        return [p for p in record.paths if p.path_group_verb == verb]