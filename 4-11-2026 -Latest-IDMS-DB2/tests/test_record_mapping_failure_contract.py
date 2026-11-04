import pytest
from converter.composers.record_materialisation.record_plan_builder import (
    RecordPlanBuilder, RecordMappingLookupError
)


class FailRepo:
    def rows_for_record(self, record):
        raise OSError('CSV not readable')


class EmptyRepo:
    def rows_for_record(self, record):
        return []


def builder(repo):
    return RecordPlanBuilder(mapping_repository=repo,
                             table_name_resolver=lambda _: '',
                             host_variable_resolver=lambda *_: '')


def test_io_failure_is_not_silently_interpreted_as_no_fields():
    with pytest.raises(RecordMappingLookupError, match='CSV not readable'):
        builder(FailRepo())._rows('SOME-RECORD')


def test_truly_unmapped_record_is_still_empty():
    assert builder(EmptyRepo())._rows('SOME-RECORD') == []
