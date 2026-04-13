# test_triangle.py
import pytest
from triangle import classify_triangle

def test_liksidig():
    assert classify_triangle(3, 3, 3) == "liksidig"

def test_likbent_ab():
    assert classify_triangle(3, 3, 2) == "likbent"

def test_likbent_bc():
    assert classify_triangle(2, 3, 3) == "likbent"

def test_likbent_ac():
    assert classify_triangle(3, 2, 3) == "likbent"

def test_oliksidig():
    assert classify_triangle(3, 4, 5) == "oliksidig"

def test_negativ_sida():
    with pytest.raises(ValueError, match="positiva"):
        classify_triangle(-1, 2, 3)

def test_noll():
    with pytest.raises(ValueError, match="positiva"):
        classify_triangle(0, 2, 3)

def test_ogiltig_triangel():
    with pytest.raises(ValueError, match="giltig"):
        classify_triangle(1, 1, 10)

