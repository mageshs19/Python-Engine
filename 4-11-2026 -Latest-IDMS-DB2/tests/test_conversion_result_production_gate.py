from converter.domain.models import ConversionResult


def test_conversion_result_marks_lrf_blocker_as_not_promotable():
    blocked = ConversionResult(validation_messages=[
        "LRF production gate: BLOCKED; executable IDMS record references remain."
    ])
    safe = ConversionResult(validation_messages=["LRF key binding: generated metadata-proven input split(s)."])
    assert blocked.production_blocked is True
    assert safe.production_blocked is False
