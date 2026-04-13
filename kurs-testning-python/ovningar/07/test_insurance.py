import pytest

from insurance import calculate_premium


@pytest.mark.parametrize(
    "age,is_smoker,bmi,expected",
    [
        (24, False, 30, 1500),
        (24, False, 31, 1800),
        (24, True, 30, 2200),
        (24, True, 31, 2500),
        (25, False, 30, 1000),
        (25, False, 31, 1300),
        (25, True, 30, 1700),
        (25, True, 31, 2000),
    ],
)
def test_calculate_premium_decision_table(age, is_smoker, bmi, expected):
    assert calculate_premium(age, is_smoker, bmi) == expected
