import pytest
from src.math_operations import subtract

def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2

def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2

def test_subtract_positive_and_negative():
    assert subtract(5, -3) == 8
    assert subtract(-5, 3) == -8

def test_subtract_zero():
    assert subtract(0, 0) == 0
    assert subtract(0, 7) == -7
    assert subtract(7, 0) == 7

def test_subtract_large_numbers():
    assert subtract(2_000_000, 1_000_000) == 1_000_000

def test_subtract_floats():
    assert subtract(3.8, 2.3) == pytest.approx(1.5)
    assert subtract(-1.1, 2.1) == pytest.approx(-3.2)
