
"""Builds DB2 statement bodies: INSERT / UPDATE / DELETE / SELECT-skip / MOVE."""

from __future__ import annotations

from converter.generators.db2_infrastructure.sql_location_move_builder import (
    SqlLocationMoveBuilder,
)
from converter.services.name_normalizer import NameNormalizer
from rules.sql_location_rules import (
    LEGACY_OPERATION_DELETE,
    LEGACY_OPERATION_INSERT,
    LEGACY_OPERATION_UPDATE,
    LEGACY_RECORD_LOCATION_TEMPLATE,
)
from rules.update_sql_cleanup_rules import UPDATE_QUERYNO


class SqlStatementBuilder:
    def __init__(
        self,
        column_resolver,
        line_builder,
        date_builder,
        host_variable_resolver,
        mapping_repository,
        update_plan_resolver,
    ) -> None:
        self.column_resolver = column_resolver
        self.line_builder = line_builder
        self.date_builder = date_builder
        self.host_variable_resolver = host_variable_resolver
        self.mapping_repository = mapping_repository
        self.update_plan_resolver = update_plan_resolver
        self.messages: list[str] = []

    def _sqlcode_evaluate_block(self, operation: str, table: str) -> list[str]:
        """Manual-standard SQLCODE handling shared by INSERT/UPDATE/DELETE."""
        return [
            f"   QUERYNO {UPDATE_QUERYNO}",
            "END-EXEC",
            "EVALUATE SQLCODE",
            "    WHEN 0",
            "         CONTINUE",
            "    WHEN OTHER",
            f"         DISPLAY 'ERROR ON {operation} {table}'",
            "         PERFORM SQLERROR",
            "END-EVALUATE",
            ".",
        ]

    def select_by_key(
        self,
        record_name: str,
        *,
        for_lrf_parent: bool = False,
        required_columns: list[str] | tuple[str, ...] | set[str] | None = None,
        status_handling: bool = True,
        read_kind: str = "LRF keyed parent",
    ) -> list[str]:
        """Render a keyed SELECT when a retrieval needs a mapped record.

        Ordinary UPDATE positioning reads retain their legacy behavior unless
        ``for_lrf_parent`` is explicitly true.  An LRF-generated CALC parent
        read is not redundant: it populates the DCLGEN fields used by later
        business MOVEs, so it must SELECT the mapped row into host variables.

        The method fails closed if any mapped result column or host variable
        is missing. It must never emit a comment/CONTINUE that looks like a
        successful read.
        """
        self.messages = []
        record = NameNormalizer.normalize(record_name)
        table = self.column_resolver.resolved_table_for_record(record)

        if not record or not table:
            return self.line_builder.missing_sql(
                operation="OBTAIN CALC",
                record_name=record_name,
                reason="missing Sheet Mapping or DCLGEN table metadata",
            )

        key_columns = self.column_resolver.key_columns_for_record(
            record_name=record,
            table_name=table,
        )
        if not key_columns:
            return self.line_builder.missing_sql(
                operation="OBTAIN CALC",
                record_name=record,
                reason="missing key column metadata",
            )

        if not for_lrf_parent:
            return [
                f"*DB2: Removed OBTAIN CALC SELECT for "
                f"{NameNormalizer.to_cobol(record)}.",
                "*DB2: Direct UPDATE will use mapped composite key WHERE clause.",
                "CONTINUE.",
            ]

        # Build the projection from THIS IDMS record's field-backed mapping
        # rows. When the pipeline supplies source-proven required columns,
        # intersect with that set: record mapping metadata says what CAN be
        # selected, not what this program actually USES. `None` retains the
        # public API's historical record-scoped fallback for direct callers;
        # an explicit empty set is deliberately NOT treated as fallback.
        rows_for_record = getattr(self.mapping_repository, "rows_for_record", None)
        if not callable(rows_for_record):
            return self.line_builder.missing_sql(
                operation="LRF keyed parent SELECT",
                record_name=record,
                reason="mapping repository cannot provide record-scoped field provenance",
            )

        mapped_columns: list[str] = []
        seen_columns: set[str] = set()
        try:
            record_rows = rows_for_record(record) or []
        except Exception as exc:  # noqa: BLE001
            return self.line_builder.missing_sql(
                operation="LRF keyed parent SELECT",
                record_name=record,
                reason=f"record-scoped mapping lookup failed ({type(exc).__name__})",
            )

        required = (
            {NameNormalizer.normalize(column) for column in required_columns}
            if required_columns is not None
            else None
        )
        if required is not None and not required:
            return self.line_builder.missing_sql(
                operation="LRF keyed parent SELECT",
                record_name=record,
                reason="source analysis found no provable downstream fields; keyed read retained",
            )

        for row in record_rows:
            source_field = str(
                getattr(row, "cobol_zone", "")
                or getattr(row, "reference_field_name_copybook", "")
                or ""
            ).strip()
            column = NameNormalizer.normalize(
                getattr(row, "new_db2_field_name", "")
                or getattr(row, "cross_application_db2_field_name", "")
            )
            if not source_field or not column or column in seen_columns:
                continue
            if required is not None and column not in required:
                continue
            seen_columns.add(column)
            mapped_columns.append(column)

        available_record_columns = {
            NameNormalizer.normalize(
                getattr(row, "new_db2_field_name", "")
                or getattr(row, "cross_application_db2_field_name", "")
            )
            for row in record_rows
        }
        available_record_columns.discard("")
        if required is not None and not required.issubset(available_record_columns):
            # A required field without a field-backed mapping cannot safely be
            # silently omitted from SELECT INTO.
            return self.line_builder.missing_sql(
                operation="LRF keyed parent SELECT",
                record_name=record,
                reason="one or more source-used fields have no field-backed mapping",
            )

        select_columns = self.column_resolver.filter_to_existing_dclgen_columns(
            table_name=table,
            columns=mapped_columns,
        )
        if required is not None and set(select_columns) != set(mapped_columns):
            return self.line_builder.missing_sql(
                operation="LRF keyed parent SELECT",
                record_name=record,
                reason="a source-used column is absent from DCLGEN; keyed read retained",
            )
        select_hosts = self.host_variable_resolver.host_references_for_columns(
            table_name=table,
            columns=select_columns,
        )
        if (
            not select_columns
            or len(select_hosts) != len(select_columns)
            or len(key_columns) != len(
                self.line_builder.where_lines(
                    table_name=table,
                    key_columns=key_columns,
                    indent="       ",
                )
            )
        ):
            return self.line_builder.missing_sql(
                operation="LRF keyed parent SELECT",
                record_name=record,
                reason=(
                    "mapped SELECT columns, DCLGEN host variables, or key "
                    "host variables are incomplete; source access retained"
                ),
            )

        record_display = NameNormalizer.to_cobol(record)
        lines = [
            f"*DB2: Converted {read_kind} read for {record_display}.",
            f"MOVE 'SELECT-{record_display}' TO SQL-LOCATION.",
            "EXEC SQL",
            "   SELECT",
        ]
        lines.extend(self.line_builder.sql_column_list(select_columns, "      "))
        lines.append("   INTO")
        lines.extend(self.line_builder.host_variable_list(select_hosts, "      "))
        lines.extend([f"   FROM {table}", "   WHERE"])
        lines.extend(
            self.line_builder.where_lines(
                table_name=table,
                key_columns=key_columns,
                indent="      ",
            )
        )
        lines.extend([f"   QUERYNO {UPDATE_QUERYNO}", "END-EXEC"])
        if status_handling:
            lines.extend(
                [
                    "EVALUATE SQLCODE",
                    "    WHEN 0",
                    "         CONTINUE",
                    "    WHEN 100",
                    f"         DISPLAY 'NO DATA FOUND FOR SELECT {table}'",
                    "         PERFORM SQLERROR",
                    "    WHEN OTHER",
                    "         DISPLAY 'ERROR ON LRF KEYED PARENT SELECT '",
                    f"                 '{table}'",
                    "         PERFORM SQLERROR",
                    "END-EVALUATE",
                    ".",
                ]
            )
        return lines

    def insert(
        self,
        record_name: str,
        paragraph: str = "",
    ) -> list[str]:
        """Render a metadata-driven INSERT with sequence and audit defaults.

        A column and its value are planned together. This avoids the previous
        failure mode where a missing host variable silently shortened VALUES
        and misaligned it with the INSERT column list.
        """
        self.messages = []
        record = NameNormalizer.normalize(record_name)
        table = self.column_resolver.resolved_table_for_record(record)
        if not record or not table:
            return self.line_builder.missing_sql(
                operation="INSERT", record_name=record_name,
                reason="missing Sheet Mapping or DCLGEN table metadata",
            )

        columns = self.column_resolver.insert_columns_for_record(record, table)
        if not columns:
            return self.line_builder.missing_sql(
                operation="INSERT", record_name=record, reason="missing insert columns"
            )

        sequence_key = self.column_resolver.sequence_key_for_record(record, table)
        sequence_column = sequence_name = ""
        sequence_precision = 0
        if sequence_key:
            sequence_column, sequence_name, sequence_precision = sequence_key
            if not sequence_name or sequence_precision <= 0:
                return self.line_builder.missing_sql(
                    operation="INSERT", record_name=record,
                    reason=(
                        f"sequence-key metadata for {sequence_column} is incomplete; "
                        "sequence name/decimal precision could not be resolved"
                    ),
                )
            if sequence_column not in columns:
                columns.append(sequence_column)

        values: list[str] = []
        for column in columns:
            if sequence_key and column == sequence_column:
                values.append(
                    f"RIGHT(DIGITS(NEXT VALUE FOR {sequence_name}), {sequence_precision})"
                )
                continue
            host = self.host_variable_resolver.host_reference_for_column(
                table_name=table, column_name=column
            )
            if not host:
                return self.line_builder.missing_sql(
                    operation="INSERT", record_name=record,
                    reason=f"no DCLGEN host variable for required INSERT column {column}",
                )
            values.append(host)

        record_label = NameNormalizer.to_cobol(record)
        location = str(paragraph or "").strip() or LEGACY_RECORD_LOCATION_TEMPLATE.format(
            operation=LEGACY_OPERATION_INSERT, record=record_label
        )
        lines: list[str] = [f"*DB2: Converted STORE for {record_label}."]
        sql_location = SqlLocationMoveBuilder().sentence(location)
        if sql_location:
            lines.append(sql_location)

        lines.extend(self._insert_default_moves(table, columns))
        lines.extend(["EXEC SQL", f"   INSERT INTO {table}", "      ("])
        lines.extend(self.line_builder.sql_column_list(columns, indent="       "))
        lines.extend(["      )", "   VALUES", "      ("])
        lines.extend(self.line_builder.host_variable_list(values, indent="       "))
        lines.extend(["      )", *self._sqlcode_evaluate_block("INSERT", table)])
        return lines

    def _insert_default_moves(self, table: str, columns: list[str]) -> list[str]:
        """Initialize conventional audit/technical columns for a new row.

        These rules apply only when the corresponding columns are actually in
        the INSERT plan; programs/tables without them are byte-for-byte outside
        this behavior. DCLGEN remains the authority for host spelling.
        """
        moves: list[str] = []
        defaults = (
            ("TS_CREATE", "TS-TIMESTAMP"),
            ("TS_UPDATE", "'9999-12-31-23.59.59.999999'"),
            ("ID_USERID", "CS-PROGRAM"),
        )
        for prefix, source in defaults:
            column = next((name for name in columns if NameNormalizer.normalize(name).startswith(prefix)), "")
            if not column:
                continue
            host = self.host_variable_resolver.host_reference_for_column(table, column)
            if host:
                moves.append(f"MOVE {source} TO {self._cobol_move_target(host)}.")
        technical_key = next((name for name in columns if "IDMSKEY" in NameNormalizer.normalize(name)), "")
        if technical_key:
            host = self.host_variable_resolver.host_reference_for_column(table, technical_key)
            if host:
                moves.append(f"MOVE ZERO TO {self._cobol_move_target(host)}.")
        return moves

    @staticmethod
    def _cobol_move_target(host_reference: str) -> str:
        """Convert a DB2 host reference to a COBOL data-name reference."""
        value = str(host_reference or "").strip().lstrip(":")
        if "." in value:
            group, field = value.split(".", 1)
            if group and field:
                return f"{field} OF {group}"
        return value

    def update(
        self,
        record_name: str,
        changed_source_fields: list[str] | None = None,
        paragraph: str = "",
    ) -> list[str]:
        """The converted MODIFY block, SQL-LOCATION included.

        CORRECTION - this method rendered the MOVE itself
        -------------------------------------------------
        Same defect and same remedy as insert(): the inline f-string

            f"MOVE 'UPDATE-{NameNormalizer.to_cobol(record)}' "
            f"TO SQL-LOCATION."

        was the third of three independent emitters. One renderer now
        owns the form; `paragraph` is optional and keyword-last so no
        existing positional call site changes meaning.
        """
        self.messages = []
        record = NameNormalizer.normalize(record_name)
        plan = self.update_plan_resolver.resolve(
            record_name=record,
            changed_source_fields=changed_source_fields or [],
        )
        self.messages.extend(plan.diagnostics)

        if plan.table_name:
            plan.key_columns = self.column_resolver.key_columns_for_record(
                record_name=record,
                table_name=plan.table_name,
            )

        if not plan.is_complete:
            return self.line_builder.missing_sql(
                operation="UPDATE",
                record_name=record,
                reason="incomplete conservative UPDATE metadata",
            )

        set_lines = self.line_builder.set_lines(
            table_name=plan.table_name,
            columns=plan.update_columns,
            indent="      ",
        )
        where_lines = self.line_builder.where_lines(
            table_name=plan.table_name,
            key_columns=plan.key_columns,
            indent="      ",
        )
        if not set_lines or not where_lines:
            return self.line_builder.missing_sql(
                operation="UPDATE",
                record_name=record,
                reason="missing SET or WHERE host variables in DCLGEN",
            )

        record_label = NameNormalizer.to_cobol(record)

        location = str(paragraph or "").strip()
        if not location:
            location = LEGACY_RECORD_LOCATION_TEMPLATE.format(
                operation=LEGACY_OPERATION_UPDATE,
                record=record_label,
            )

        lines: list[str] = [
            f"*DB2: Converted MODIFY for {record_label}.",
        ]

        sql_location = SqlLocationMoveBuilder().sentence(location)
        if sql_location:
            lines.append(sql_location)

        lines.extend(
            [
                "EXEC SQL",
                f"   UPDATE {plan.table_name}",
                "   SET",
            ]
        )
        lines.extend(set_lines)
        lines.append("   WHERE")
        lines.extend(where_lines)
        lines.extend(self._sqlcode_evaluate_block("UPDATE", plan.table_name))
        return lines
    
    def delete(
        self,
        record_name: str,
        paragraph: str = "",
    ) -> list[str]:
        """The converted ERASE block, SQL-LOCATION included.

        CORRECTION - the fourth inline emitter
        --------------------------------------
        insert() and update() were unified first because they were the
        two the artefact exposed. delete() carried the identical defect

            f"MOVE 'DELETE-{NameNormalizer.to_cobol(record)}' "
            f"TO SQL-LOCATION."

        and was only found by grepping the WHOLE file for the emitted
        text after the first two were fixed - not by reading the ranges
        the defect report pointed at. Same remedy, same optional
        `paragraph`, same byte-for-byte fallback.

        commit() and rollback() are deliberately NOT unified here. They
        have no record and no paragraph, the manual reference emits no
        MOVE before COMMIT at all, and retrieval_commit_cleanup_composer
        matches the literal "MOVE 'COMMIT' TO SQL-LOCATION" to find and
        remove the block. That is a separate decision with a consumer
        attached - see defect NEW-14.
        """
        self.messages = []
        record = NameNormalizer.normalize(record_name)
        table = self.column_resolver.resolved_table_for_record(record)

        if not record or not table:
            return self.line_builder.missing_sql(
                operation="DELETE",
                record_name=record_name,
                reason="missing Sheet Mapping or DCLGEN table metadata",
            )

        key_columns = self.column_resolver.key_columns_for_record(
            record_name=record,
            table_name=table,
        )
        where_lines = self.line_builder.where_lines(
            table_name=table,
            key_columns=key_columns,
            indent="      ",
        )
        if not where_lines:
            return self.line_builder.missing_sql(
                operation="DELETE",
                record_name=record,
                reason="missing DELETE key host variables in DCLGEN",
            )

        record_label = NameNormalizer.to_cobol(record)

        location = str(paragraph or "").strip()
        if not location:
            location = LEGACY_RECORD_LOCATION_TEMPLATE.format(
                operation=LEGACY_OPERATION_DELETE,
                record=record_label,
            )

        lines: list[str] = [
            f"*DB2: Converted ERASE for {record_label}.",
        ]

        sql_location = SqlLocationMoveBuilder().sentence(location)
        if sql_location:
            lines.append(sql_location)

        lines.extend(
            [
                "EXEC SQL",
                f"   DELETE FROM {table}",
                "   WHERE",
            ]
        )
        lines.extend(where_lines)
        lines.extend(self._sqlcode_evaluate_block("DELETE", table))
        return lines
    
    def commit(self) -> list[str]:
        return [
            "MOVE 'COMMIT' TO SQL-LOCATION.",
            "EXEC SQL",
            "   COMMIT",
            "END-EXEC.",
        ]

    def rollback(self) -> list[str]:
        return [
            "MOVE 'ROLLBACK' TO SQL-LOCATION.",
            "EXEC SQL",
            "   ROLLBACK",
            "END-EXEC.",
        ]

    def changed_field_move(
        self,
        record_name: str,
        source_value: str,
        target_source_field: str,
    ) -> list[str]:
        record = NameNormalizer.normalize(record_name)
        table = self.column_resolver.resolved_table_for_record(record)
        column = self.mapping_repository.column_for_source_field(
            record_name=record,
            source_field_name=target_source_field,
        )
        column = NameNormalizer.normalize(column)

        if not table or not column:
            return [
                f"*DB2: Conversion skipped for MOVE target "
                f"{target_source_field}.",
                "*DB2: Missing Sheet Mapping or DCLGEN metadata.",
                "CONTINUE.",
            ]

        host_key = self.host_variable_resolver.host_reference_key(
            table_name=table,
            column_name=column,
        )
        if not host_key:
            return [
                f"*DB2: Conversion skipped for MOVE target "
                f"{target_source_field}.",
                "*DB2: Missing DCLGEN host variable.",
                "CONTINUE.",
            ]

        if self.date_builder.is_db2_date_column(column):
            return self.date_builder.date_ymd8_to_db2_external_move(
                source_value=source_value,
                host_key=host_key,
            )

        return [f"MOVE {source_value} TO {host_key}"]

    def missing_mapping(
        self,
        record_name: str,
        reason: str,
    ) -> list[str]:
        return self.line_builder.missing_sql(
            operation="DB2",
            record_name=record_name,
            reason=reason,
        )