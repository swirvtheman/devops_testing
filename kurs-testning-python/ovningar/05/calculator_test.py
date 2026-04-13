from calculator import Calculator
from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


@pytest.fixture
def calc():
    return Calculator()


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (-5, -3, -8),
        (1.5, 2.5, 4.0),
    ],
)
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),
        (0, 0, 0),
        (-1, 1, -2),
        (-5, -3, -2),
        (4.0, 2.5, 1.5),
    ],
)
def test_subtract(calc, a, b, expected):
    assert calc.subtract(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (0, 7, 0),
        (-2, 3, -6),
        (-2, -4, 8),
        (1.5, 2.0, 3.0),
    ],
)
def test_multiply(calc, a, b, expected):
    assert calc.multiply(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2),
        (0, 5, 0),
        (-6, 3, -2),
        (-8, -2, 4),
        (7.5, 2.5, 3.0),
    ],
)
def test_divide(calc, a, b, expected):
    assert calc.divide(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("a", [1, 0, -1, 3.14, 100])
def test_divide_by_zero_raises_value_error(calc, a):
    with pytest.raises(ValueError, match="Kan inte dividera med noll"):
        calc.divide(a, 0)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 8),
        (5, 0, 1),
        (3, 1, 3),
        (4, 0.5, 2),
        (2, -1, 0.5),
    ],
)
def test_power(calc, a, b, expected):
    assert calc.power(a, b) == pytest.approx(expected)
