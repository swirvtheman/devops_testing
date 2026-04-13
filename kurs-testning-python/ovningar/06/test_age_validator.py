import pytest

from age_validator import validate_age


def test_barn_boundaries():
    assert validate_age(0) == "barn"
    assert validate_age(12) == "barn"


def test_ungdom_boundaries():
    assert validate_age(13) == "ungdom"
    assert validate_age(17) == "ungdom"


def test_vuxen_boundaries():
    assert validate_age(18) == "vuxen"
    assert validate_age(64) == "vuxen"


def test_senior_boundaries():
    assert validate_age(65) == "senior"
    assert validate_age(150) == "senior"


def test_invalid_range_raises_value_error():
    with pytest.raises(ValueError):
        validate_age(-1)
    with pytest.raises(ValueError):
        validate_age(151)


@pytest.mark.parametrize("bad_value", [12.5, None, "jonas"])
def test_invalid_types_raise_value_error(bad_value):
    with pytest.raises(ValueError):
        validate_age(bad_value)
