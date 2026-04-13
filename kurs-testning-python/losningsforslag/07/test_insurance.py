# test_insurance.py
import pytest
from insurance import calculate_premium

@pytest.mark.parametrize("age,smoker,bmi,expected", [
    (20, True,  35.0, 2500),   # Under 25, rökare, BMI>30
    (20, True,  25.0, 2200),   # Under 25, rökare, BMI<=30
    (20, False, 35.0, 1800),   # Under 25, ej rökare, BMI>30
    (20, False, 25.0, 1500),   # Under 25, ej rökare, BMI<=30
    (30, True,  35.0, 2000),   # 25+, rökare, BMI>30
    (30, True,  25.0, 1700),   # 25+, rökare, BMI<=30
    (30, False, 35.0, 1300),   # 25+, ej rökare, BMI>30
    (30, False, 25.0, 1000),   # 25+, ej rökare, BMI<=30
])
def test_premium_decision_table(age, smoker, bmi, expected):
    assert calculate_premium(age, smoker, bmi) == expected

