import pytest
from src.math_operations import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_zero():
    assert add(0, 5) == 5
    assert add(5, 0) == 5
    assert add(0, 0) == 0

def test_add_positive_and_negative():
    assert add(10, -3) == 7
    assert add(-7, 4) == -3

def test_add_floats():
    assert add(1.5, 2.5) == 4.0
    assert add(-1.1, 1.1) == 0.0

def test_add_large_numbers():
    assert add(1_000_000_000, 2_000_000_000) == 3_000_000_000
