import pytest
from src.math_operations import subtract

def test_subtract_positive_numbers():
    assert subtract(5, 2) == 3
    assert subtract(200, 100) == 100

def test_subtract_negative_numbers():
    assert subtract(-5, -2) == -3
    assert subtract(-200, -100) == -100

def test_subtract_mixed_sign_numbers():
    assert subtract(-1, 1) == -2
    assert subtract(100, -50) == 150

def test_subtract_zero():
    assert subtract(0, 0) == 0
    assert subtract(0, 5) == -5
    assert subtract(5, 0) == 5

def test_subtract_floats():
    assert subtract(5.5, 2.2) == pytest.approx(3.3)
    assert subtract(-1.5, 2.5) == pytest.approx(-4.0)
