# LOCATION: converter/generators/sql/sql_column_resolver.py
# ACTION: CREATE NEW FILE

"""SQL column resolution: table, key columns, insert columns, DCLGEN filter."""

from __future__ import annotations

import re

from converter.services.name_normalizer import NameNormalizer


class SqlColumnResolver:
    def __init__(
        self,
        mapping_repository,
        dclgen_repository,
        table_name_resolver,
    ) -> None:
        self.mapping_repository = mapping_repository
        self.dclgen_repository = dclgen_repository
        self.table_name_resolver = table_name_resolver

    def resolved_table_for_record(self, record_name: str) -> str:
        mapped_table = self.mapping_repository.db2_table_for_record(
            record_name
        )
        if not mapped_table:
            return ""
        return self.table_name_resolver.resolve_table(mapped_table)

    def key_columns_for_record(
        self,
        record_name: str,
        table_name: str,
    ) -> list[str]:
        """
        Key columns for SQL WHERE. Composite PK / CALC keys required; FK /
        FOREIGN columns never included; Sheet Mapping order preserved.
        """
        columns: list[str] = []

        if hasattr(self.mapping_repository, "rows_for_record"):
            columns = self._key_columns_from_mapping_rows(record_name)

        if not columns and hasattr(
            self.mapping_repository,
            "primary_key_columns_for_record",
        ):
            columns = self.mapping_repository.primary_key_columns_for_record(
                record_name
            )

        return self.filter_to_existing_dclgen_columns(
            table_name=table_name,
            columns=columns,
        )

    def _key_columns_from_mapping_rows(
        self,
        record_name: str,
    ) -> list[str]:
        output: list[str] = []
        seen: set[str] = set()

        for row in self.mapping_repository.rows_for_record(record_name):
            idms_key = NameNormalizer.normalize(getattr(row, "idms_key", ""))
            db2_key = NameNormalizer.normalize(getattr(row, "db2_key", ""))
            relation = NameNormalizer.normalize(getattr(row, "relation", ""))
            column = NameNormalizer.normalize(
                getattr(row, "new_db2_field_name", "")
                or getattr(row, "cross_application_db2_field_name", "")
            )
            if not column:
                continue

            combined_text = " ".join([idms_key, db2_key, relation])
            padded_text = f" {combined_text} "

            if "FOREIGN" in combined_text:
                continue
            if " FK " in padded_text:
                continue

            is_key_column = (
                "PRIMARY" in db2_key
                or db2_key == "KEY"
                or "PRIMARY" in idms_key
                or idms_key == "KEY"
                or "CALC" in idms_key
            )
            if not is_key_column:
                continue
            if column in seen:
                continue

            seen.add(column)
            output.append(column)

        return output

    def insert_columns_for_record(
        self,
        record_name: str,
        table_name: str,
    ) -> list[str]:
        # Sheet Mapping may name the base table (e.g. DZEVEFTB), while
        # DCLGEN resolves the runtime target to its view/table alias
        # (e.g. DZEVEFTV). Query mapping columns with the original mapped
        # table, then validate those columns against the resolved DCLGEN
        # target. Querying Sheet Mapping with the resolved alias returns an
        # empty list and silently turns STORE into CONTINUE instead of INSERT.
        mapped_table = self.mapping_repository.db2_table_for_record(
            record_name
        )
        columns = self.mapping_repository.db2_columns_for_table(
            mapped_table or table_name
        )
        columns = self.filter_to_existing_dclgen_columns(table_name, columns)

        # Preserve mapped insert audit columns. The manual COBOL contract sets
        # TS_CREATE, TS_UPDATE and ID_USERID on INSERT; dropping TS_UPDATE can
        # violate NOT NULL constraints and changes the legacy record semantics.
        # A narrow generic exception also includes an unmapped technical IDMS
        # key when the DCLGEN declares it (e.g. NS_IDMSKEY). Other unmapped
        # DCLGEN columns remain excluded, preserving Sheet Mapping authority.
        technical = self._unmapped_technical_idms_key_columns(
            table_name=table_name, mapped_columns=columns
        )
        return self._unique([*columns, *technical])

    def sequence_key_for_record(
        self, record_name: str, table_name: str
    ) -> tuple[str, str, int] | None:
        """Return (column, sequence, precision) for a mapped sequence key.

        The sequence is inferred only when Sheet Mapping explicitly marks a
        primary-key field as an auto-increment/sequence key. For the established
        DB2 naming convention, base tables ending in TB use the corresponding
        SQ sequence. Unknown conventions fail closed rather than guessing.
        """
        rows_for_record = getattr(self.mapping_repository, "rows_for_record", None)
        if not callable(rows_for_record):
            return None
        rows = rows_for_record(record_name) or []
        for row in rows:
            column = NameNormalizer.normalize(
                getattr(row, "new_db2_field_name", "")
                or getattr(row, "cross_application_db2_field_name", "")
            )
            if not column:
                continue
            key_kind = " ".join(
                str(getattr(row, attr, "") or "")
                for attr in ("db2_key", "idms_key", "remarks", "hopex_expression_type_remark")
            ).upper()
            sequence_key = (
                ("PRIMARY" in key_kind or "KEY" in key_kind)
                and ("INCREMENT" in key_kind and "SEQ" in key_kind)
            )
            if not sequence_key:
                continue
            base_table = NameNormalizer.normalize(
                self.mapping_repository.db2_table_for_record(record_name)
            )
            sequence = ""
            explicit = re.search(
                r"\bSEQUENCE\s*(?:NAME)?\s*[:=]\s*([A-Z][A-Z0-9_]*)",
                key_kind,
            )
            if explicit:
                sequence = explicit.group(1)
            elif base_table.endswith("TB"):
                sequence = base_table[:-2] + "SQ"
            if not sequence:
                return (column, "", self._numeric_precision(table_name, column, row))
            return (column, sequence, self._numeric_precision(table_name, column, row))
        return None

    def _numeric_precision(self, table_name: str, column: str, mapping_row) -> int:
        type_text = str(getattr(mapping_row, "new_db2_data_type", "") or "")
        if not type_text:
            for dcl_column in getattr(self.dclgen_repository, "columns_for_table", lambda _t: [])(
                self.table_name_resolver.resolve_table(table_name)
            ) or []:
                if NameNormalizer.normalize(getattr(dcl_column, "column_name", "")) == column:
                    type_text = str(getattr(dcl_column, "db2_type", "") or "")
                    break
        match = re.search(r"\bDECIMAL\s*\(\s*(\d+)", type_text, re.I)
        return int(match.group(1)) if match else 0

    def _unmapped_technical_idms_key_columns(
        self, table_name: str, mapped_columns: list[str]
    ) -> list[str]:
        resolved = self.table_name_resolver.resolve_table(table_name)
        columns_for_table = getattr(self.dclgen_repository, "columns_for_table", None)
        if not resolved or not callable(columns_for_table):
            return []
        mapped = set(mapped_columns)
        output: list[str] = []
        for column in columns_for_table(resolved) or []:
            name = NameNormalizer.normalize(getattr(column, "column_name", ""))
            if name and name not in mapped and "IDMSKEY" in name:
                output.append(name)
        return output

    def minimal_select_columns(
        self,
        record_name: str,
        table_name: str,
        key_columns: list[str],
    ) -> list[str]:
        return self.filter_to_existing_dclgen_columns(
            table_name=table_name,
            columns=key_columns,
        )

    def filter_to_existing_dclgen_columns(
        self,
        table_name: str,
        columns: list[str],
    ) -> list[str]:
        resolved_table = self.table_name_resolver.resolve_table(table_name)
        if not resolved_table:
            return []

        dclgen_columns = set(
            self.dclgen_repository.column_names_for_table(resolved_table)
        )
        if not dclgen_columns:
            return []

        output: list[str] = []
        for column in columns:
            normalized = NameNormalizer.normalize(column)
            if not normalized:
                continue
            if normalized not in dclgen_columns:
                continue
            output.append(normalized)

        return self._unique(output)

    def _unique(self, values: list[str]) -> list[str]:
        output: list[str] = []
        seen: set[str] = set()
        for value in values:
            normalized = NameNormalizer.normalize(value)
            if not normalized or normalized in seen:
                continue
            seen.add(normalized)
            output.append(normalized)
        return output