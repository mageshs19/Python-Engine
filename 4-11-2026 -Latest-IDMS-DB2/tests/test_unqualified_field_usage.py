from converter.analyzers.field_usage_analyzer import FieldUsageAnalyzer
from converter.domain.models import SheetMappingRow
from converter.repositories.mapping_repository import MappingRepository


class _Tables:
    def table_for_record(self, record):
        return {"VMBEFF": "DZBEFFTV", "VMBEVEF": "DZEVEFTV"}.get(record, "")


def _analyzer(rows):
    return FieldUsageAnalyzer(MappingRepository(rows), _Tables())


def test_unqualified_unique_source_fields_are_attributed_to_owning_record():
    rows = [
        SheetMappingRow(cobol_record_idms="VMBEFF", cobol_zone="02 AM-CN-STOCK", new_db2_record="DZBEFFTB", new_db2_field_name="AM_CNSTK_479BEFF"),
        SheetMappingRow(cobol_record_idms="VMBEVEF", cobol_zone="02 DA-CR-EVENT-PROD", new_db2_record="DZEVEFTB", new_db2_field_name="DA_CREVTPD_479EVEF"),
    ]
    result = _analyzer(rows).analyze("""
       PROCEDURE DIVISION.
           MOVE AM-CN-STOCK TO OUT-AMOUNT.
           IF DA-CR-EVENT-PROD < WS-DATE
              CONTINUE
           END-IF.
    """)
    assert "AM-CN-STOCK" in result.usage_by_record["VMBEFF"].all_fields
    assert "DA-CR-EVENT-PROD" in result.usage_by_record["VMBEVEF"].condition_fields


def test_ambiguous_unqualified_source_field_is_not_guessed():
    rows = [
        SheetMappingRow(cobol_record_idms="VMBEFF", cobol_zone="02 STATUS", new_db2_record="DZBEFFTB", new_db2_field_name="STATUS_A"),
        SheetMappingRow(cobol_record_idms="VMBEVEF", cobol_zone="02 STATUS", new_db2_record="DZEVEFTB", new_db2_field_name="STATUS_B"),
    ]
    result = _analyzer(rows).analyze("""
       PROCEDURE DIVISION.
           IF STATUS = 'A'
              CONTINUE
           END-IF.
    """)
    assert not result.usage_by_record
