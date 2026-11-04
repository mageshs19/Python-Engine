"""Safely decompose LRF 1:N group references into DB2 host-field operations.

A group-name substitution cannot represent a group mapped to multiple DB2
columns. This pass expands only when mapping metadata proves component order,
component widths, and the destination copybook width. Unprovable layouts remain
unchanged and are reported as production blockers.
"""
from __future__ import annotations

import re

from converter.generators.initialization.line_geometry import LineGeometry
from converter.services.fixed_format_line_service import FixedFormatLineService
from converter.services.name_normalizer import NameNormalizer
from rules.move_alignment_rules import STATEMENT_OPENERS


class LrfGroupMoveDecomposer:
    _FIELD_LEVEL = re.compile(r"^\s*(?P<level>\d{1,2})\s+(?P<name>[A-Z0-9-]+)", re.I)
    _MOVE_GROUP_TO_TARGET = re.compile(
        r"^MOVE\s+(?P<field>[A-Z][A-Z0-9-]*)\s+OF\s+(?P<record>[A-Z][A-Z0-9-]*)\s+"
        r"TO\s+(?P<target>[A-Z][A-Z0-9-]*)(?:\s+OF\s+(?P<target_record>[A-Z][A-Z0-9-]*))?\s*\.?$",
        re.I,
    )
    _MOVE_TO_GROUP = re.compile(
        r"^MOVE\s+(?P<source>[A-Z][A-Z0-9-]*|SPACES|SPACE|ZEROES|ZEROS|ZERO)\s+TO\s+"
        r"(?P<field>[A-Z][A-Z0-9-]*)\s+OF\s+(?P<record>[A-Z][A-Z0-9-]*)\s*\.?$",
        re.I,
    )
    _MOVE_SPACES_TO_RECORD = re.compile(
        r"^MOVE\s+(?:SPACES|SPACE)\s+TO\s+"
        r"(?P<records>[A-Z][A-Z0-9-]*(?:\s+[A-Z][A-Z0-9-]*)*)\s*\.?$",
        re.I,
    )
    _MOVE_SIMPLE_SOURCE_MULTI_TARGET = re.compile(
        r"^MOVE\s+(?P<source>'(?:''|[^'])*'|[A-Z][A-Z0-9-]*|[0-9]+)\s+TO\s+(?P<targets>.+?)\s*\.?$",
        re.I,
    )
    _MOVE_TARGET = re.compile(
        r"(?P<field>[A-Z][A-Z0-9-]*)(?:\s+OF\s+(?P<record>[A-Z][A-Z0-9-]*))?",
        re.I,
    )
    _DISPLAY_PREFIX = re.compile(r"^DISPLAY\b", re.I)
    _PICTURE_WIDTH = re.compile(r"\b(?:PIC|PICTURE)\s+(.+)$", re.I)
    _TYPE_WIDTH = re.compile(r"\b(?:CHAR|CHARACTER|DECIMAL|NUMERIC|INTEGER)\s*\(\s*(\d+)", re.I)

    def __init__(self, *, mapping_repository, dclgen_repository, copybook_repository, table_name_resolver, host_variable_resolver):
        self.mapping = mapping_repository
        self.dclgen = dclgen_repository
        self.copybooks = copybook_repository
        self.tables = table_name_resolver
        self.hosts = host_variable_resolver
        self.geometry = LineGeometry()
        self.fixed = FixedFormatLineService()
        self.messages: list[str] = []
        self.resolved_group_references: set[tuple[str, str]] = set()
        self._generated_helpers: dict[tuple[str, str], dict[str, object]] = {}
        self._explicit_target_groups: set[tuple[str, str]] = set()

    def apply(self, text: str, parent_records: set[str] | None = None) -> str:
        self.messages = []
        self.resolved_group_references = set()
        self._generated_helpers = {}
        self._explicit_target_groups = set()
        parents = {NameNormalizer.normalize(x) for x in (parent_records or set())}
        lines = self.geometry.split(text)
        lrf_records = set(parents) | self._child_records_from_comments(lines)
        for candidate_index, _candidate_line in enumerate(lines):
            candidate_statement, _candidate_consumed = self._collect_move(
                lines, candidate_index
            )
            if not candidate_statement:
                continue
            explicit = self._MOVE_GROUP_TO_TARGET.match(candidate_statement)
            if not explicit:
                continue
            explicit_record = NameNormalizer.normalize(explicit.group("target_record"))
            explicit_field = NameNormalizer.normalize(explicit.group("target"))
            if explicit_record in lrf_records:
                self._explicit_target_groups.add((explicit_record, explicit_field))
        output: list[str] = []
        index = 0
        last_assembled: tuple[str, str, str, str, int] | None = None
        decomposed = 0
        removed_redundant = 0

        while index < len(lines):
            line = lines[index]
            body = self.geometry.body(line)
            upper = body.upper().strip()
            if not body or self.geometry.is_comment(line):
                output.append(line)
                index += 1
                continue

            statement, consumed = self._collect_move(lines, index)
            if last_assembled is not None:
                candidate = self._MOVE_GROUP_TO_TARGET.match(statement) if statement else None
                if not candidate or (NameNormalizer.normalize(candidate.group("record")),
                                     NameNormalizer.normalize(candidate.group("field"))) != last_assembled[:2]:
                    last_assembled = None
            if statement:
                whole_record_clear = self._MOVE_SPACES_TO_RECORD.match(statement)
                if whole_record_clear:
                    records = [
                        NameNormalizer.normalize(name)
                        for name in whole_record_clear.group("records").split()
                    ]
                    # Whole-record MOVE SPACES is a COBOL data operation, not
                    # an LRF-only keyword. Resolve every target through Sheet
                    # Mapping + DCLGEN; this safely covers LRF and non-LRF records
                    # while leaving unmapped records untouched.
                    if records:
                        groups: list[str] = []
                        unresolved = ""
                        for record in records:
                            table = self.tables.table_for_record(record)
                            dcl_group = self.hosts.group_for_table(table) if table else ""
                            if not dcl_group:
                                unresolved = record
                                break
                            if dcl_group not in groups:
                                groups.append(dcl_group)
                        if not unresolved and groups:
                            # IDMS clears may name multiple record buffers on one
                            # MOVE. Initialize every mapped DCLGEN group together;
                            # dropping only the first target leaves stale NOT NULL
                            # columns (and can change subsequent INSERT values).
                            generated = f"INITIALIZE {' '.join(groups)}."
                            output.extend(self._render_generated_statement(line, generated))
                            for record in records:
                                self.resolved_group_references.add((record, record))
                            decomposed += 1
                            index += consumed
                            continue
                        self.messages.append(
                            f"LRF whole-record clear: {unresolved or ', '.join(records)} "
                            "has no resolved DCLGEN group; MOVE SPACES was left for review."
                        )

                # A group item is alphanumeric in COBOL even when the copybook
                # supplies a canonical elementary numeric view named GROUP-R.
                # If that direct child and the DCLGEN numeric target have the
                # same precision, use the elementary view so COBOL performs a
                # numeric-to-numeric move. Refuse ambiguous or mismatched cases.
                numeric_group_move = self._narrow_numeric_group_source(statement)
                if numeric_group_move:
                    output.extend(self._render_generated_statement(line, numeric_group_move))
                    self.messages.append(
                        "COBOL MOVE: used a direct, precision-matched numeric elementary view of a group source."
                    )
                    decomposed += 1
                    index += consumed
                    continue

                # COBOL permits one MOVE source to multiple receiving fields,
                # for example ``MOVE 0 TO FIELD-A OF REC FIELD-B OF REC``.
                # Field-reference rewriting can change both receivers to
                # DCLGEN names but must not leave the second receiver as a bare
                # COBOL statement. Split only simple, unambiguous source forms;
                # complex expressions and CORRESPONDING moves remain untouched.
                if not whole_record_clear:
                    multi_move = self._MOVE_SIMPLE_SOURCE_MULTI_TARGET.match(statement)
                    if multi_move:
                        targets_text = multi_move.group("targets").strip()
                        if targets_text.endswith("."):
                            targets_text = targets_text[:-1].rstrip()
                        targets: list[str] = []
                        cursor = 0
                        while cursor < len(targets_text):
                            while cursor < len(targets_text) and targets_text[cursor].isspace():
                                cursor += 1
                            if cursor >= len(targets_text):
                                break
                            target_match = self._MOVE_TARGET.match(targets_text, cursor)
                            if not target_match:
                                targets = []
                                break
                            target = target_match.group("field")
                            if target_match.group("record"):
                                target += " OF " + target_match.group("record")
                            targets.append(target)
                            cursor = target_match.end()
                        if len(targets) > 1:
                            generated = [
                                f"MOVE {multi_move.group('source')} TO {target}."
                                for target in targets
                            ]
                            for generated_statement in generated:
                                output.extend(self._render_generated_statement(line, generated_statement))
                            decomposed += 1
                            index += consumed
                            continue

                move_to_group = self._MOVE_TO_GROUP.match(statement)
                if move_to_group:
                    record = NameNormalizer.normalize(move_to_group.group("record"))
                    field = NameNormalizer.normalize(move_to_group.group("field"))
                    source = str(move_to_group.group("source") or "").strip().upper()
                    components, reason = self._group_components(record, field)

                    # The parent key input is already split by the proven
                    # LRF-key planner. Keep the DCLGEN MOVEs and remove the
                    # unexecutable IDMS record-group MOVE.
                    if record in parents and self._has_generated_key_split(
                        lines, record, source
                    ):
                        output.append(
                            f"*DB2: Removed IDMS composite-key MOVE; generated DCLGEN component MOVEs populate the keyed SELECT."
                        )
                        removed_redundant += 1
                        self.resolved_group_references.add((record, field))
                        index += consumed
                        continue

                    # MOVE SPACES to a CALC key group is redundant only when
                    # every mapped key component is explicitly assigned before
                    # the keyed SELECT. Never remove it on name similarity alone.
                    if source in {"SPACES", "SPACE"} and record in parents and components:
                        if self._all_components_assigned_before_select(lines, record, components):
                            output.append(
                                "*DB2: Removed redundant key-group clear; all mapped CALC key components are initialized and assigned before SELECT."
                            )
                            removed_redundant += 1
                            self.resolved_group_references.add((record, field))
                            index += consumed
                            continue

                move_from_group = self._MOVE_GROUP_TO_TARGET.match(statement)
                if move_from_group:
                    record = NameNormalizer.normalize(move_from_group.group("record"))
                    field = NameNormalizer.normalize(move_from_group.group("field"))
                    target = NameNormalizer.to_cobol(move_from_group.group("target"))
                    target_record = NameNormalizer.normalize(move_from_group.group("target_record"))

                    # A mapped IDMS group destination can represent several
                    # DB2 columns. Split the source bytes through a generated
                    # REDEFINES helper, then move each proven component into
                    # its DCLGEN host field. This is the same deterministic
                    # operation for NR-CI (1+5) and NR-ID-STOCK-CD (12+1).
                    split_target_record = target_record or self._infer_target_record(
                        target, lrf_records
                    )
                    if split_target_record:
                        components, _reason = self._group_components(
                            split_target_record, NameNormalizer.normalize(target)
                        )
                        source_width = self._copybook_width(field)
                        component_widths = [int(item.get("width") or 0) for item in components]
                        if (
                            len(components) > 1
                            and source_width > 0
                            and all(component_widths)
                            and sum(component_widths) == source_width
                        ):
                            helper = self._helper_for_split(
                                split_target_record,
                                NameNormalizer.normalize(target),
                                source_width,
                                components,
                            )
                            source_ref = f"{NameNormalizer.to_cobol(move_from_group.group('field'))} OF {NameNormalizer.to_cobol(record)}"
                            generated = [f"MOVE {source_ref} TO {helper['raw']}. ".rstrip()]
                            for component_index, item in enumerate(components, start=1):
                                generated.append(
                                    f"MOVE {helper['components'][component_index - 1]} "
                                    f"TO {item['host']} OF {item['dcl_group']}."
                                )
                            for generated_statement in generated:
                                output.extend(self._render_generated_statement(line, generated_statement))
                            self.resolved_group_references.add(
                                (NameNormalizer.normalize(split_target_record), NameNormalizer.normalize(target))
                            )
                            decomposed += 1
                            index += consumed
                            continue

                    # Field-reference normalization can drop the target IDMS
                    # record qualifier from a composite CALC-key MOVE. If the
                    # planner has already emitted the metadata-proven component
                    # slices for exactly one parent record, remove the now
                    # unexecutable whole-group MOVE rather than leaving an
                    # unresolved IDMS data name in the DB2 COBOL.
                    if not target_record and parents:
                        matching_parents = []
                        source_field = NameNormalizer.to_cobol(move_from_group.group("field"))
                        for parent in parents:
                            parent_components, _parent_reason = self._group_components(parent, target)
                            if len(parent_components) > 1 and self._has_generated_key_split(
                                lines, parent, source_field
                            ):
                                matching_parents.append(parent)
                        if len(matching_parents) == 1:
                            output.append(
                                "*DB2: Removed unqualified IDMS composite-key MOVE; "
                                "metadata-proven DCLGEN component MOVEs populate the keyed SELECT."
                            )
                            removed_redundant += 1
                            self.resolved_group_references.add((matching_parents[0], NameNormalizer.normalize(target)))
                            index += consumed
                            continue

                    components, reason = self._group_components(record, field)
                    if len(components) > 1:
                        target_width = self._copybook_width(target)
                        # If an immediately preceding MOVE has assembled the
                        # same logical group into a numeric DISPLAY alias,
                        # use that proven value for the padded alphanumeric
                        # recipient. This reproduces COBOL's numeric->X MOVE
                        # semantics and needs no synthetic helper fields.
                        previous = last_assembled
                        last_assembled = None
                        if previous is not None:
                            prev_record, prev_field, alias, prev_qualifier, prev_width = previous
                            pic = self.copybooks.effective_picture_for(target).upper().replace(" ", "")
                            if (prev_record == record and prev_field == field
                                    and prev_qualifier == target_record
                                    and target_width == prev_width + 1
                                    and re.fullmatch(r"(?:X|A)\(\d+\)", pic)):
                                src = NameNormalizer.to_cobol(alias)
                                dst = target
                                if target_record:
                                    q = NameNormalizer.to_cobol(target_record)
                                    src += f" OF {q}"
                                    dst += f" OF {q}"
                                output.extend(self._render_generated_statement(line, f"MOVE {src} TO {dst}."))
                                self.resolved_group_references.add((record, field))
                                decomposed += 1
                                index += consumed
                                continue
                        widths = [item["width"] for item in components]
                        source_width = sum(widths)
                        target_picture = self.copybooks.effective_picture_for(target).upper().replace(" ", "")
                        exact_width = bool(target_width and all(widths) and source_width == target_width)
                        pad_alphanumeric = bool(
                            target_width and all(widths) and source_width < target_width
                            and target_picture.startswith(("X(", "A("))
                        )
                        if exact_width or pad_alphanumeric:
                            target_ref = self._reference_modification_base(target)
                            target_qualifier = NameNormalizer.to_cobol(target_record) if target_record else ""
                            # COBOL qualification belongs to the identifier,
                            # BEFORE reference modification: ITEM OF REC(1:12),
                            # never ITEM(1:12) OF REC.  Where the copybook has
                            # proven direct child fields of identical width,
                            # move into those fields instead. This preserves
                            # numeric receiving types and avoids fragile slices.
                            typed_children = self._width_matched_children(target, widths) if exact_width else []
                            offset = 1
                            generated = []
                            for component_index, (component, width) in enumerate(zip(components, widths)):
                                if typed_children:
                                    receiver = typed_children[component_index]
                                    if target_qualifier:
                                        receiver += f" OF {target_qualifier}"
                                else:
                                    receiver = target_ref
                                    if target_qualifier:
                                        receiver += f" OF {target_qualifier}"
                                    receiver += f"({offset}:{width})"
                                generated.append(
                                    f"MOVE {component['host']} OF {component['dcl_group']} TO {receiver}."
                                )
                                offset += width
                            if pad_alphanumeric:
                                receiver = target_ref
                                if target_qualifier:
                                    receiver += f" OF {target_qualifier}"
                                receiver += f"({source_width + 1}:{target_width - source_width})"
                                generated.append(f"MOVE SPACES TO {receiver}.")
                            for generated_statement in generated:
                                output.extend(self._render_generated_statement(line, generated_statement))
                            decomposed += 1
                            self.resolved_group_references.add((record, field))
                            if exact_width and typed_children and target_record:
                                # REDEFINES of an elementary numeric item is
                                # the compiler-proven typed alias, not a guess.
                                alias = self.copybooks.redefines_for(target)
                                alias_pic = self.copybooks.picture_for(alias).upper().replace(" ", "")
                                if (alias and self._copybook_width(alias) == source_width
                                        and re.fullmatch(r"9(?:\(\d+\)|9*)", alias_pic)):
                                    last_assembled = (record, field, alias, target_record, source_width)
                            index += consumed
                            continue
                        self.messages.append(
                            f"LRF group move: {field} OF {record} maps to {len(components)} DB2 columns, "
                            f"but destination width {target_width} does not prove component widths {widths}; left unchanged."
                        )

            # Whole-record DISPLAY is a diagnostic dump, not business logic.
            # Replace the removed IDMS record with its generated DCLGEN group.
            if self._DISPLAY_PREFIX.match(upper):
                whole_display = re.match(r"^DISPLAY\s+(?P<record>[A-Z][A-Z0-9-]*)\s*\.?$", upper)
                if whole_display:
                    record = NameNormalizer.normalize(whole_display.group("record"))
                    if record in lrf_records:
                        table = self.tables.table_for_record(record)
                        group = self.hosts.group_for_table(table) if table else ""
                        if group:
                            left = line[:6] if self.fixed.is_fixed_line(line) else ""
                            indicator = line[6] if self.fixed.is_fixed_line(line) and len(line) > 6 else " "
                            right = line[72:80] if self.fixed.is_fixed_line(line) and len(line) >= 80 else ""
                            indent = self.geometry.indent_of(line) or "       "
                            output.extend(self.fixed.emit(left, indicator, f"{indent}DISPLAY {group}", right))
                            self.resolved_group_references.add((record, record))
                            decomposed += 1
                            index += 1
                            continue

                display_groups = self._group_references_in_display(body, lrf_records)
                if len(display_groups) == 1:
                    field, record = display_groups[0]
                    components, _reason = self._group_components(record, field)
                    match = re.search(
                        rf"\b{re.escape(NameNormalizer.to_cobol(field))}\s+OF\s+{re.escape(NameNormalizer.to_cobol(record))}\b",
                        body,
                        re.I,
                    )
                    if len(components) > 1 and match and not body[match.end():].strip():
                        prefix = body[:match.start()].rstrip()
                        left = line[:6] if self.fixed.is_fixed_line(line) else ""
                        indicator = line[6] if self.fixed.is_fixed_line(line) and len(line) > 6 else " "
                        right = line[72:80] if self.fixed.is_fixed_line(line) and len(line) >= 80 else ""
                        indent = self.geometry.indent_of(line) or "       "
                        # Keep the original message and emit each key component
                        # on a separate DISPLAY. This avoids fragile wrapped
                        # multi-operand DISPLAY syntax in fixed-format COBOL.
                        output.extend(self.fixed.emit(left, indicator, prefix, right))
                        for component_index, item in enumerate(components, start=1):
                            display_body = (
                                f"{indent}DISPLAY 'K{component_index}=' "
                                f"{item['host']} OF {item['dcl_group']}"
                            )
                            output.extend(self.fixed.emit(left, " ", display_body, right))
                        decomposed += 1
                        self.resolved_group_references.add((record, field))
                        index += 1
                        continue
                updated = body
                for field, record in display_groups:
                    components, _reason = self._group_components(record, field)
                    if len(components) > 1:
                        replacement = " ".join(
                            f"{item['host']} OF {item['dcl_group']}" for item in components
                        )
                        updated = re.sub(
                            rf"\b{re.escape(NameNormalizer.to_cobol(field))}\s+OF\s+{re.escape(NameNormalizer.to_cobol(record))}\b",
                            replacement,
                            updated,
                            count=1,
                            flags=re.I,
                        )
                if updated != body:
                    output.extend(self.fixed.replace_body_wrapped(line, updated))
                    decomposed += 1
                    index += 1
                    continue

            output.append(line)
            index += 1

        result = self.geometry.join(output)
        result = self._insert_helper_declarations(result)
        residual = self._residual_lrf_record_references(result, lrf_records)
        if residual:
            self.messages.append(
                "LRF production gate: BLOCKED; executable IDMS record references remain after group decomposition: "
                + ", ".join(sorted(residual))
                + ". Generated COBOL is review-only until each reference is mapped or explicitly refused."
            )
        residual_tokens = self._residual_lrf_access_tokens(result)
        if residual_tokens:
            self.messages.append(
                "LRF production gate: BLOCKED; executable LRF/IDMS access or status tokens remain: "
                + ", ".join(sorted(residual_tokens))
                + ". Generated COBOL is review-only."
            )
        if decomposed:
            self.messages.append(
                f"LRF group decomposition: expanded {decomposed} proven multi-column group reference(s)."
            )
        if removed_redundant:
            self.messages.append(
                f"LRF group decomposition: removed {removed_redundant} redundant IDMS key-group statement(s)."
            )
        return result

    def _render_generated_statement(self, source_line: str, statement: str) -> list[str]:
        """Emit generated statements in fixed format with correct continuation indicators."""
        if self.fixed.is_fixed_line(source_line):
            left = source_line[:6]
            indicator = source_line[6] if len(source_line) > 6 else " "
            right = source_line[72:80] if len(source_line) >= 80 else ""
            indent = self.geometry.indent_of(source_line) or "       "
            return self.fixed.emit(left, indicator, f"{indent}{statement}", right)
        indent = self.geometry.indent_of(source_line)
        return [f"{indent}{statement}"]

    def filter_resolved_field_diagnostics(self, messages: list[str]) -> list[str]:
        """Drop earlier 1:N warnings for group references this pass proved and expanded."""
        pattern = re.compile(r"Field decomposition: (?P<field>[A-Z0-9_-]+) OF (?P<record>[A-Z0-9_-]+)", re.I)
        output = []
        for message in messages:
            match = pattern.search(str(message or ""))
            if match:
                pair = (
                    NameNormalizer.normalize(match.group("record")),
                    NameNormalizer.normalize(match.group("field")),
                )
                if pair in self.resolved_group_references:
                    continue
            output.append(message)
        return output

    @staticmethod
    def _numeric_picture_digits(picture: str) -> int:
        text = str(picture or "").upper().replace(" ", "")
        if not text or not re.fullmatch(r"[S9VP()+\-.,0-9]+", text) or "9" not in text:
            return 0
        expanded = re.sub(r"([S9VP])\((\d+)\)", lambda m: m.group(1) * int(m.group(2)), text)
        return expanded.count("9")

    def _narrow_numeric_group_source(self, statement: str) -> str:
        """Narrow a group source only when its GROUP-R numeric view is proven."""
        match = re.match(
            r"^MOVE\s+(?P<source>[A-Z][A-Z0-9-]*)\s+TO\s+"
            r"(?P<target>[A-Z][A-Z0-9-]*)\s+OF\s+(?P<group>DCL[A-Z][A-Z0-9-]*)\s*\.?$",
            str(statement or "").strip(), re.I,
        )
        if not match:
            return ""
        source = NameNormalizer.normalize(match.group("source"))
        target = NameNormalizer.normalize(match.group("target"))
        target_group = NameNormalizer.normalize(match.group("group"))
        source_field = self.copybooks.find(source)
        if source_field is None or str(getattr(source_field, "picture", "") or "").strip():
            return ""
        child = self.copybooks.find(source + "-R")
        if child is None:
            return ""
        parent = self.copybooks.parent_for(child.name)
        if parent is None or NameNormalizer.normalize(parent.name) != source:
            return ""
        source_digits = self._numeric_picture_digits(getattr(child, "picture", ""))
        if not source_digits:
            return ""

        table = target_group[3:] if target_group.startswith("DCL") else ""
        target_column = next((
            column for column in self.dclgen.all()
            if NameNormalizer.normalize(getattr(column, "table_name", "")) == table
            and NameNormalizer.normalize(getattr(column, "cobol_host_name", "") or getattr(column, "column_name", "")) == target
        ), None)
        if target_column is None:
            return ""
        db2_type = str(getattr(target_column, "db2_type", "") or "").upper().strip()
        host_picture = str(getattr(target_column, "cobol_picture", "") or "").upper().strip()
        usage = str(getattr(target_column, "cobol_usage", "") or "").upper().strip()
        numeric_target = bool(
            re.match(r"^(?:DECIMAL|NUMERIC|INTEGER|SMALLINT|BIGINT)\b", db2_type)
            or ("9" in host_picture and any(token in usage for token in ("COMP", "PACKED")))
        )
        precision_match = re.search(r"\b(?:DECIMAL|NUMERIC)\s*\(\s*(\d+)", db2_type)
        target_digits = int(precision_match.group(1)) if precision_match else self._numeric_picture_digits(host_picture)
        if not numeric_target or target_digits != source_digits:
            return ""
        return f"MOVE {NameNormalizer.to_cobol(child.name)} TO {match.group('target')} OF {match.group('group')}."

    def _collect_move(self, lines: list[str], start: int) -> tuple[str, int]:
        body = self.geometry.body(lines[start]).strip()
        if not re.match(r"^MOVE\b", body, re.I):
            return "", 1
        parts = [body]
        consumed = 1
        while "." not in parts[-1] and start + consumed < len(lines) and consumed < 4:
            next_line = lines[start + consumed]
            next_body = self.geometry.body(next_line).strip()
            if not next_body or self.geometry.is_comment(next_line):
                break
            # In period-free COBOL a fresh statement still ends the MOVE.
            # Do not swallow a WRITE ... FROM, READ, or another verb into
            # receiving-item tokens; this previously deleted physical output
            # writes and emitted illegal MOVE ... TO WRITE/FROM statements.
            if next_body.split(maxsplit=1)[0].rstrip('.').upper() in STATEMENT_OPENERS:
                break
            parts.append(next_body)
            consumed += 1
        return " ".join(parts), consumed

    def _infer_target_record(self, field: str, lrf_records: set[str]) -> str:
        """Infer an omitted target qualifier only when one LRF record owns the group."""
        normalized_field = NameNormalizer.normalize(field)
        candidates = []
        for record in sorted(lrf_records):
            # Only infer an omitted qualifier when another source statement
            # explicitly proves this field belongs to that same LRF record.
            # A similarly named working-storage group (for example DB-NR-CI)
            # must not be redirected into DCLGEN just because a mapping row
            # with that name exists.
            if (record, normalized_field) not in self._explicit_target_groups:
                continue
            components, _reason = self._group_components(record, normalized_field)
            if len(components) > 1:
                candidates.append(record)
        return candidates[0] if len(candidates) == 1 else ""

    def _helper_for_split(
        self,
        record: str,
        field: str,
        source_width: int,
        components: list[dict],
    ) -> dict[str, object]:
        key = (NameNormalizer.normalize(record), NameNormalizer.normalize(field))
        if key in self._generated_helpers:
            return self._generated_helpers[key]

        number = len(self._generated_helpers) + 1
        base = f"WS-LRF-SPLIT-{number}"
        raw = f"{base}-RAW"
        redefine = f"{base}-R"
        component_names = [f"{base}-C{index}" for index in range(1, len(components) + 1)]
        declarations = [
            f"01 {base}.",
            f"    05 {raw} PIC X({source_width}).",
            f"    05 {redefine} REDEFINES {raw}.",
        ]
        for name, component in zip(component_names, components):
            width = int(component["width"])
            data_type = str(component.get("data_type", "") or "").upper()
            pic = f"9({width})" if any(token in data_type for token in ("DECIMAL", "NUMERIC", "INTEGER")) else f"X({width})"
            declarations.append(f"      10 {name} PIC {pic}.")

        helper = {
            "raw": raw,
            "components": component_names,
            "declarations": declarations,
        }
        self._generated_helpers[key] = helper
        return helper

    def _insert_helper_declarations(self, text: str) -> str:
        if not self._generated_helpers:
            return text
        lines = str(text or "").splitlines()
        procedure_index = next(
            (index for index, line in enumerate(lines)
             if re.search(r"\bPROCEDURE\s+DIVISION\b", self.geometry.body(line), re.I)),
            None,
        )
        if procedure_index is None:
            self.messages.append("LRF group decomposition: helper declarations were needed but PROCEDURE DIVISION was not found.")
            return text
        declarations: list[str] = []
        for helper in self._generated_helpers.values():
            declarations.extend(helper["declarations"])
        lines[procedure_index:procedure_index] = declarations + [""]
        return self.geometry.join(lines)

    def _group_components(self, record: str, group_field: str) -> tuple[list[dict], str]:
        rows = self.mapping.rows_for_record(record)
        nodes = []
        for row in rows:
            zone = str(getattr(row, "cobol_zone", "") or "").strip()
            match = self._FIELD_LEVEL.match(zone)
            if not match:
                continue
            field_name = NameNormalizer.normalize(match.group("name"))
            column = NameNormalizer.normalize(
                getattr(row, "new_db2_field_name", "")
                or getattr(row, "cross_application_db2_field_name", "")
            )
            table = self.tables.resolve_table(
                getattr(row, "new_db2_record", "")
                or getattr(row, "cross_application_db2_table", "")
            )
            nodes.append({
                "level": int(match.group("level")),
                "field": field_name,
                "redefines": bool(re.search(r"\bREDEFINES\b", zone, re.I)),
                "filler": field_name == "FILLER",
                "column": column,
                "table": table,
                "data_type": str(
                    getattr(row, "new_db2_data_type", "")
                    or getattr(row, "cross_application_db2_data_type", "")
                    or ""
                ),
                "row": row,
            })

        target_index = next((i for i, node in enumerate(nodes) if node["field"] == group_field), -1)
        if target_index < 0:
            return [], f"group {group_field} is absent from mapping"
        group_node = nodes[target_index]
        if group_node["column"]:
            table = group_node["table"]
            host = self.hosts.host_for_column(table, group_node["column"]) if table else ""
            return ([{"column": group_node["column"], "table": table, "host": host, "dcl_group": self.hosts.group_for_table(table), "width": self._row_width(group_node["row"]), "data_type": group_node["data_type"]}] if host else []), ""

        components: list[dict] = []
        unmapped_leaves: list[str] = []
        group_level = group_node["level"]
        index = target_index + 1
        while index < len(nodes) and nodes[index]["level"] > group_level:
            node = nodes[index]
            if node["redefines"] or node["filler"]:
                index = self._skip_subtree(nodes, index)
                continue
            if node["column"]:
                table = node["table"] or self.tables.table_for_record(record)
                host = self.hosts.host_for_column(table, node["column"]) if table else ""
                width = self._row_width(node["row"])
                if host and width:
                    components.append({
                        "column": node["column"], "table": table, "host": host,
                        "dcl_group": self.hosts.group_for_table(table), "width": width,
                        "data_type": node["data_type"],
                    })
                index = self._skip_subtree(nodes, index)
                continue
            # An unmapped group must be traversed so mapped grandchildren are
            # not lost. An unmapped non-FILLER leaf, however, means a split
            # would silently drop source bytes and must be refused.
            next_level = nodes[index + 1]["level"] if index + 1 < len(nodes) else 0
            if next_level <= node["level"]:
                unmapped_leaves.append(node["field"])
            index += 1
        if unmapped_leaves:
            return [], "unmapped non-FILLER leaf/leafs: " + ", ".join(unmapped_leaves)
        return components, ""

    @staticmethod
    def _skip_subtree(nodes: list[dict], index: int) -> int:
        level = nodes[index]["level"]
        index += 1
        while index < len(nodes) and nodes[index]["level"] > level:
            index += 1
        return index

    def _row_width(self, row) -> int:
        raw = str(getattr(row, "length_of_field_bytes", "") or "").strip()
        if raw.isdigit():
            return int(raw)
        dtype = str(
            getattr(row, "new_db2_data_type", "")
            or getattr(row, "cross_application_db2_data_type", "")
            or ""
        )
        match = self._TYPE_WIDTH.search(dtype)
        return int(match.group(1)) if match else 0

    def _copybook_width(self, field: str) -> int:
        picture = self.copybooks.effective_picture_for(field)
        if not picture:
            return int(self.copybooks.group_width_for(field) or 0)
        picture = re.sub(r"\s+", "", picture.upper())
        total = 0
        for token in re.findall(r"(?:S?9|X|A|N|Z|\*|\$)(?:\((\d+)\))?", picture):
            total += int(token) if token else 1
        # The previous regex returns repeat counts only; count picture tokens
        # separately to handle simple forms such as PIC 99 or PIC X(13).
        expanded = re.sub(r"(S?9|X|A|N|Z|\*|\$)\((\d+)\)", lambda m: m.group(1) * int(m.group(2)), picture)
        return sum(1 for char in expanded if char in "9XANZ*$")

    def _width_matched_children(self, target: str, widths: list[int]) -> list[str]:
        """Use source-defined COBOL receiving items when boundaries agree.

        Numeric elementary children preserve numeric MOVE semantics (rather
        than treating their bytes as alpha slices). Refuse missing/redefined/
        variable-sized or mismatched children: fall back to qualified refmod.
        """
        if not widths or not hasattr(self.copybooks, "direct_children_for"):
            return []
        children = self.copybooks.direct_children_for(target)
        if len(children) != len(widths):
            return []
        result: list[str] = []
        for child, width in zip(children, widths):
            if str(getattr(child, "occurs", "") or "").strip():
                return []
            if str(getattr(child, "redefines", "") or "").strip():
                return []
            if self._copybook_width(child.name) != width:
                return []
            result.append(NameNormalizer.to_cobol(child.name))
        return result

    def _reference_modification_base(self, target: str) -> str:
        field = self.copybooks.find(target)
        if field is None:
            return target
        if not str(getattr(field, "picture", "") or "").strip():
            return target
        parent = self.copybooks.parent_for(target)
        if (
            parent
            and not str(getattr(parent, "picture", "") or "").strip()
            and len(self.copybooks.direct_children_for(parent.name)) == 1
            and NameNormalizer.normalize(self.copybooks.direct_children_for(parent.name)[0].name)
                == NameNormalizer.normalize(target)
        ):
            return NameNormalizer.to_cobol(parent.name)
        return target

    def _has_generated_key_split(self, lines: list[str], record: str, source: str) -> bool:
        marker = f"LRF keyed parent read for {NameNormalizer.to_cobol(record)}"
        joined = "\n".join(self.geometry.body(line).upper() for line in lines)
        marker_index = joined.find(marker.upper())
        if marker_index < 0:
            return False
        before_select = joined[marker_index:]
        return bool(re.search(rf"\bMOVE\s+{re.escape(source.upper())}\(\d+:\d+\)\s+TO\s+[A-Z0-9-]+\s+OF\s+DCL[A-Z0-9-]+", before_select, re.I))

    def _all_components_assigned_before_select(self, lines: list[str], record: str, components: list[dict]) -> bool:
        marker = f"Converted LRF keyed parent read for {NameNormalizer.to_cobol(record)}"
        joined = "\n".join(self.geometry.body(line).upper() for line in lines)
        marker_index = joined.find(marker.upper())
        if marker_index < 0:
            return False
        before = joined[:marker_index]
        for item in components:
            if not re.search(rf"\bTO\s+{re.escape(item['host'].upper())}\s+OF\s+{re.escape(item['dcl_group'].upper())}\b", before, re.I):
                return False
        return True

    def _group_references_in_display(self, body: str, lrf_records: set[str]) -> list[tuple[str, str]]:
        output = []
        for match in re.finditer(r"\b(?P<field>[A-Z][A-Z0-9-]*)\s+OF\s+(?P<record>[A-Z][A-Z0-9-]*)\b", body, re.I):
            record = NameNormalizer.normalize(match.group("record"))
            field = NameNormalizer.normalize(match.group("field"))
            if record in lrf_records:
                output.append((field, record))
        return output

    def _child_records_from_comments(self, lines: list[str]) -> set[str]:
        output = set()
        pattern = re.compile(r"->\s+(?P<child>[A-Z0-9-]+)\s+WITHIN\s+(?P<parent>[A-Z0-9-]+)-", re.I)
        for line in lines:
            if not self.geometry.is_comment(line):
                continue
            match = pattern.search(self.geometry.body(line))
            if match:
                output.add(NameNormalizer.normalize(match.group("child")))
                output.add(NameNormalizer.normalize(match.group("parent")))
        return output

    def _residual_lrf_access_tokens(self, text: str) -> set[str]:
        residual: set[str] = set()
        patterns = {
            "OBTAIN": re.compile(r"\bOBTAIN\s+(?:FIRST|NEXT|CALC)\b", re.I),
            "LR-STATUS": re.compile(r"\bLR-STATUS\b", re.I),
            "DB-REC-NOT-FOUND": re.compile(r"\bDB-REC-NOT-FOUND\b", re.I),
            "DB-END-OF-SET": re.compile(r"\bDB-END-OF-SET\b", re.I),
            "DB-LRF-PARENT-NOT-FOUND": re.compile(r"\bDB-LRF-PARENT-NOT-FOUND\b", re.I),
        }
        for line in text.splitlines():
            if self.geometry.is_comment(line):
                continue
            body = self.geometry.body(line)
            for label, pattern in patterns.items():
                if pattern.search(body):
                    residual.add(label)
        return residual

    def _residual_lrf_record_references(self, text: str, records: set[str]) -> set[str]:
        residual = set()
        for line in text.splitlines():
            if self.geometry.is_comment(line):
                continue
            body = self.geometry.body(line)
            for match in re.finditer(r"\b(?:OF|IN)\s+(?P<record>[A-Z][A-Z0-9-]*)\b", body, re.I):
                record = NameNormalizer.normalize(match.group("record"))
                if record in records:
                    residual.add(NameNormalizer.to_cobol(record))
            whole_record = re.match(
                r"^\s*(?:DISPLAY|INITIALIZE|READ|WRITE|DELETE|REWRITE|MOVE|OBTAIN|FIND|ERASE)\s+"
                r"(?P<record>[A-Z][A-Z0-9-]*)\b",
                body,
                re.I,
            )
            if whole_record:
                record = NameNormalizer.normalize(whole_record.group("record"))
                if record in records:
                    residual.add(NameNormalizer.to_cobol(record))
        return residual


__all__ = ["LrfGroupMoveDecomposer"]
