import pytest
from calculator import Calculator


def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5


def test_add_negative():
    calc = Calculator()
    assert calc.add(-1, -1) == -2


def test_subtract():
    calc = Calculator()
    assert calc.subtract(10, 4) == 6


def test_multiply():
    calc = Calculator()
    assert calc.multiply(3, 4) == 12


def test_divide():
    calc = Calculator()
    assert calc.divide(8, 2) == 4


def test_divide_float():
    calc = Calculator()
    assert calc.divide(7, 2) == 3.5


def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(10, 0)
