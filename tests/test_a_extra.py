"""Дополнительные тесты программы a."""
import pytest


def test_a_extra_01_divide(calculator):
    """A-E01: divide(7, 2) -> 3.5."""
    assert calculator.divide(7, 2) == pytest.approx(3.5, rel=1e-9, abs=1e-9)

def test_a_extra_02_divide(calculator):
    """A-E02: divide(-7, 2) -> -3.5."""
    assert calculator.divide(-7, 2) == pytest.approx(-3.5, rel=1e-9, abs=1e-9)

def test_a_extra_03_power(calculator):
    """A-E03: power(2, 3) -> 8."""
    assert calculator.power(2, 3) == 8

def test_a_extra_04_power(calculator):
    """A-E04: power(5, 0) -> 1."""
    assert calculator.power(5, 0) == 1

def test_a_extra_05_power(calculator):
    """A-E05: power(2, -2) -> 0.25."""
    assert calculator.power(2, -2) == pytest.approx(0.25, rel=1e-9, abs=1e-9)

def test_a_extra_06_power(calculator):
    """A-E06: power(0, -1) -> ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        calculator.power(0, -1)

def test_a_extra_07_subtract(calculator):
    """A-E07: subtract(-3, 2) -> -5."""
    assert calculator.subtract(-3, 2) == -5

def test_a_extra_08_multiply(calculator):
    """A-E08: multiply(0, 4) -> 0."""
    assert calculator.multiply(0, 4) == 0
