"""Начальные тесты программы a."""
import pytest


def test_a_base_01_add(calculator):
    """A-B01: add(2, 3) -> 5."""
    assert calculator.add(2, 3) == 5

def test_a_base_02_add(calculator):
    """A-B02: add(-2, 3) -> 1."""
    assert calculator.add(-2, 3) == 1

def test_a_base_03_add(calculator):
    """A-B03: add(0, 0) -> 0."""
    assert calculator.add(0, 0) == 0

def test_a_base_04_subtract(calculator):
    """A-B04: subtract(8, 3) -> 5."""
    assert calculator.subtract(8, 3) == 5

def test_a_base_05_multiply(calculator):
    """A-B05: multiply(3, 4) -> 12."""
    assert calculator.multiply(3, 4) == 12

def test_a_base_06_multiply(calculator):
    """A-B06: multiply(-2, 3) -> -6."""
    assert calculator.multiply(-2, 3) == -6

def test_a_base_07_divide(calculator):
    """A-B07: divide(8, 2) -> 4."""
    assert calculator.divide(8, 2) == 4

def test_a_base_08_divide(calculator):
    """A-B08: divide(5, 0) -> ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        calculator.divide(5, 0)

def test_a_base_09_power(calculator):
    """A-B09: power(2, 2) -> 4."""
    assert calculator.power(2, 2) == 4
