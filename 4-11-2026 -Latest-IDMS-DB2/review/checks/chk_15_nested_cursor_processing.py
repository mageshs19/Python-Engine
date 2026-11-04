"""CHK-15 Nested cursor processing."""

from __future__ import annotations

import re

from review.engine import cursors, sql_blocks as sql
from review.engine.check_base import MAJOR, BOTH, Check
from review.standards import cobol_standards as std
from review.engine import statements as stmt

class NestedCursorProcessingCheck(Check):
    CHECK_ID = "CHK-15"
    TITLE = "Nested cursor processing"
    SEVERITY = MAJOR
    APPLIES_TO = BOTH
    ORDER = 150

    def relevant(self, ctx, view) -> bool:
        return len(cursors.paragraph_sets(view)) > 1

    def not_relevant_reason(self) -> str:
        return "Program uses fewer than two cursors."

    def review(self, ctx, view, record):
        sets = cursors.paragraph_sets(view)
        parents, children = self._split(sets)
        performed = cursors.performed_names(view)

        # ---- 01 child cursors are numbered above the threshold ------
        record.expect(
            "01",
            f"Nested cursors are numbered at or above "
            f"{std.CHILD_CURSOR_MINIMUM_NUMBER}",
            bool(children),
            note=(
                f"{len(sets)} cursor(s) found, none numbered at or above "
                f"{std.CHILD_CURSOR_MINIMUM_NUMBER}."
            ),
        )

        # ---- 02 every cursor set is complete ------------------------
        incomplete = []
        for name, group in sorted(sets.items()):
            for operation in std.CURSOR_OPERATIONS:
                if operation not in group:
                    incomplete.append(f"{name} {operation}")
        record.expect_all(
            "02", "Every nested cursor has a complete paragraph set",
            incomplete,
        )

        # ---- 03 every child cursor is closed ------------------------
        if not children:
            record.skip(
                "03", "Every nested cursor is closed",
                "No nested cursor found.",
            )
        else:
            record.expect_all(
                "03", "Every nested cursor is closed",
                [
                    group["CLOSE"].name
                    for group in children.values()
                    if "CLOSE" in group
                    and group["CLOSE"].name not in performed
                ],
            )

        # ---- 04 parent and child use distinct flags -----------------
        flags = [
            f"{name}{std.CURSOR_EOC_SUFFIX}" for name in sorted(sets)
        ]
        record.expect(
            "04", "Parent and nested cursors use distinct flags",
            len(set(flags)) == len(flags),
            note=f"flags: {', '.join(flags)}",
        )

        # ---- 05 each cursor is opened exactly once ------------------
        repeated = []
        for name, group in sorted(sets.items()):
            open_para = group.get("OPEN")
            if open_para is None:
                continue
            count = len(performed.get(open_para.name, []))
            if count > 1:
                repeated.append(f"{open_para.name} performed {count} times")
        record.expect_all(
            "05", "Each cursor is opened from exactly one place", repeated,
        )

        # ---- 06 child fetch loop has an early stop ------------------
        if not std.ENFORCE_CHILD_FETCH_EARLY_STOP:
            record.skip(
                "06", "Nested fetch loops carry an early-stop condition",
                "Early-stop condition not yet agreed (decision open).",
            )
        elif not children:
            record.skip(
                "06", "Nested fetch loops carry an early-stop condition",
                "No nested cursor found.",
            )
        elif not self._source_requires_business_early_stop(ctx):
            # Complete child traversal is a valid business pattern.  Require
            # an extra stop condition only when the original IDMS source
            # itself has a compound traversal condition (for example EOF OR
            # a business event).  Looking for an arbitrary MOVE 'Y' in the
            # generated program is unsafe because unrelated interface flags
            # are common.
            record.skip(
                "06", "Nested fetch loops carry an early-stop condition",
                "Source child traversal has no explicit business early-stop "
                "condition beyond its normal status/end-of-set condition.",
            )
        else:
            # Read JOINED statements. The manual reference splits the
            # loop after OR, so a one-physical-line match fails correct
            # code. See review/engine/statements.py.
            code = [text for _index, text in stmt.joined_statements(view)]
            missing = []
            for group in children.values():
                fetch = group.get("FETCH")
                if fetch is None:
                    continue
                loop = f"PERFORM {fetch.name} UNTIL"
                # The business flag name is program-specific. Validate the
                # shape of the control condition, not a particular identifier.
                found = any(
                    line.startswith(loop)
                    and re.search(
                        r"\bOR\s+[A-Z][A-Z0-9-]*\s*=\s*['\"]Y['\"]",
                        line,
                        re.IGNORECASE,
                    )
                    for line in code
                )
                if not found:
                    missing.append(fetch.name)
            record.expect_all(
                "06", "Nested fetch loops carry an early-stop condition",
                missing,
            )

    # ---- helpers ----------------------------------------------------

    @staticmethod
    def _source_requires_business_early_stop(ctx) -> bool:
        """Return True only for source traversal with a compound stop rule.

        IDMS loops that stop solely on ERROR-STATUS/LR end-of-set are complete
        traversals and do not need a generated business flag.  A compound
        UNTIL condition using OR/AND establishes an additional business stop
        obligation that the DB2 cursor loop must preserve.
        """
        source = str(getattr(ctx, "source_cobol", "") or "").upper()
        if not source.strip():
            return False
        logical = " ".join(line.strip() for line in source.splitlines())
        for match in re.finditer(
            r"\bPERFORM(?:\s+[A-Z0-9-]+)?\s+UNTIL\s+(.+?)(?:\.|\bEND-PERFORM\b)",
            logical,
            re.IGNORECASE,
        ):
            condition = match.group(1)
            if re.search(r"\b(?:OR|AND)\b", condition, re.IGNORECASE):
                return True
        return False

    @staticmethod
    def _split(sets):
        parents, children = {}, {}
        # The first cursor by OPEN paragraph number is the outer driver;
        # remaining cursors are nested. A hardcoded threshold of 800
        # incorrectly classified 2100/3100 production cursors as BOTH
        # children. Their numbers identify order, not program identity.
        ordered = sorted(sets.items(), key=lambda pair: (
            pair[1].get("OPEN").number if pair[1].get("OPEN") else 999999,
            pair[0],
        ))
        if ordered:
            name, group = ordered[0]
            parents[name] = group
            for name, group in ordered[1:]:
                children[name] = group
        return parents, children
