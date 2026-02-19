import pytest
from src.math_operations import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_positive_and_negative():
    assert add(5, -3) == 2

def test_add_zero():
    assert add(0, 0) == 0
    assert add(0, 7) == 7
    assert add(7, 0) == 7

def test_add_large_numbers():
    assert add(1_000_000, 2_000_000) == 3_000_000

def test_add_floats():
    assert add(1.5, 2.3) == pytest.approx(3.8)
    assert add(-1.1, 2.1) == pytest.approx(1.0)
