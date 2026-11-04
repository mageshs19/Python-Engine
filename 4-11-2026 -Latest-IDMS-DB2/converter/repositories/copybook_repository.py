import re

from converter.domain.models import CopybookField
from converter.services.name_normalizer import NameNormalizer


class CopybookRepository:
    """
    Repository wrapper for optional copybook fields.
    """

    def __init__(
        self,
        fields: list[CopybookField] | None = None,
    ) -> None:
        self.fields = fields or []

    def all(
        self,
    ) -> list[CopybookField]:
        return list(self.fields)

    def count(
        self,
    ) -> int:
        return len(self.fields)

    def names(
        self,
    ) -> list[str]:
        values = {
            NameNormalizer.normalize(field.name)
            for field in self.fields
            if NameNormalizer.normalize(field.name)
        }

        return sorted(values)

    def find(
        self,
        field_name: str,
    ) -> CopybookField | None:
        target = NameNormalizer.normalize(field_name)

        if not target:
            return None

        for field in self.fields:
            if NameNormalizer.normalize(field.name) == target:
                return field

        return None

    def picture_for(
        self,
        field_name: str,
    ) -> str:
        field = self.find(field_name)

        if field is None:
            return ""

        return field.picture

    def usage_for(
        self,
        field_name: str,
    ) -> str:
        field = self.find(field_name)

        if field is None:
            return ""

        return field.usage

    def occurs_for(
        self,
        field_name: str,
    ) -> str:
        field = self.find(field_name)

        if field is None:
            return ""

        return field.occurs


    def redefines_for(self, field_name: str) -> str:
        field = self.find(field_name)
        return str(getattr(field, "redefines", "") or "").strip().upper() if field else ""

    def effective_picture_for(self, field_name: str) -> str:
        """Return a field PIC or the PIC of its REDEFINES base, if provable."""
        current = str(field_name or "").strip().upper()
        seen: set[str] = set()
        while current and current not in seen:
            seen.add(current)
            field = self.find(current)
            if field is None:
                return ""
            picture = str(getattr(field, "picture", "") or "").strip().upper()
            if picture:
                return picture
            current = str(getattr(field, "redefines", "") or "").strip().upper()
        return ""

    def group_width_for(self, field_name: str) -> int:
        """Compute a group width from its non-redefined descendants when possible."""
        target = self.find(field_name)
        if target is None:
            return 0
        effective = self.effective_picture_for(field_name)
        if effective:
            return self._picture_width(effective)
        try:
            target_index = next(i for i, item in enumerate(self.fields) if item is target)
            target_level = int(str(target.level or "0"))
        except (StopIteration, ValueError):
            return 0
        total = 0
        index = target_index + 1
        while index < len(self.fields):
            field = self.fields[index]
            try:
                level = int(str(field.level or "0"))
            except ValueError:
                index += 1
                continue
            if level <= target_level:
                break
            if str(getattr(field, "redefines", "") or "").strip():
                base_level = level
                index += 1
                while index < len(self.fields):
                    try:
                        child_level = int(str(self.fields[index].level or "0"))
                    except ValueError:
                        index += 1
                        continue
                    if child_level <= base_level:
                        break
                    index += 1
                continue
            if str(getattr(field, "picture", "") or "").strip():
                total += self._picture_width(field.picture)
                base_level = level
                index += 1
                while index < len(self.fields):
                    try:
                        child_level = int(str(self.fields[index].level or "0"))
                    except ValueError:
                        index += 1
                        continue
                    if child_level <= base_level:
                        break
                    index += 1
                continue
            index += 1
        return total

    @staticmethod
    def _picture_width(picture: str) -> int:
        text = str(picture or "").upper().replace(" ", "")
        expanded = re.sub(
            r"(S?9|X|A|N|Z|\*|\$)\((\d+)\)",
            lambda match: match.group(1) * int(match.group(2)),
            text,
        )
        # Usage COMP-3 storage width is not the number of picture digits; for
        # layout group width, the PIC describes logical display positions only
        # when the item is DISPLAY. Group aliases used for output layouts are
        # DISPLAY fields. Refuse binary/packed group arithmetic here.
        return sum(1 for char in expanded if char in "9XANZ*$")

    def direct_children_for(self, field_name: str) -> list[CopybookField]:
        """Return direct layout children of a group, excluding REDEFINES branches."""
        target = self.find(field_name)
        if target is None:
            return []
        try:
            target_index = next(i for i, item in enumerate(self.fields) if item is target)
            target_level = int(str(target.level or "0"))
        except (StopIteration, ValueError):
            return []
        children: list[CopybookField] = []
        index = target_index + 1
        while index < len(self.fields):
            field = self.fields[index]
            try:
                level = int(str(field.level or "0"))
            except ValueError:
                index += 1
                continue
            if level <= target_level:
                break
            if str(getattr(field, "redefines", "") or "").strip():
                branch_level = level
                index += 1
                while index < len(self.fields):
                    try:
                        child_level = int(str(self.fields[index].level or "0"))
                    except ValueError:
                        index += 1
                        continue
                    if child_level <= branch_level:
                        break
                    index += 1
                continue
            # A direct child is the first item at the next level below the
            # group; skip its descendants after recording it.
            children.append(field)
            branch_level = level
            index += 1
            while index < len(self.fields):
                try:
                    child_level = int(str(self.fields[index].level or "0"))
                except ValueError:
                    index += 1
                    continue
                if child_level <= branch_level:
                    break
                index += 1
        return children

    def parent_for(self, field_name: str) -> CopybookField | None:
        """Return the nearest preceding lower-level field in the flattened layout."""
        target = self.find(field_name)
        if target is None:
            return None
        try:
            target_index = next(i for i, item in enumerate(self.fields) if item is target)
            target_level = int(str(target.level or "0"))
        except (StopIteration, ValueError):
            return None
        for candidate in reversed(self.fields[:target_index]):
            try:
                candidate_level = int(str(candidate.level or "0"))
            except ValueError:
                continue
            if candidate_level < target_level:
                return candidate
        return None

    def has_field(
        self,
        field_name: str,
    ) -> bool:
        return self.find(field_name) is not None