"""Дополнительные тесты программы b."""
import pytest


def test_b_extra_01_is_prime(number_filter):
    """B-E01: is_prime(2,) -> True."""
    assert number_filter.is_prime(2) is True

def test_b_extra_02_is_prime(number_filter):
    """B-E02: is_prime(0,) -> False."""
    assert number_filter.is_prime(0) is False

def test_b_extra_03_is_prime(number_filter):
    """B-E03: is_prime(-7,) -> False."""
    assert number_filter.is_prime(-7) is False

def test_b_extra_04_is_prime(number_filter):
    """B-E04: is_prime(4,) -> False."""
    assert number_filter.is_prime(4) is False

def test_b_extra_05_is_prime(number_filter):
    """B-E05: is_prime(25,) -> False."""
    assert number_filter.is_prime(25) is False

def test_b_extra_06_is_even(number_filter):
    """B-E06: is_even(0,) -> True."""
    assert number_filter.is_even(0) is True

def test_b_extra_07_is_even(number_filter):
    """B-E07: is_even(-4,) -> True."""
    assert number_filter.is_even(-4) is True

def test_b_extra_08_is_even(number_filter):
    """B-E08: is_even(3,) -> False."""
    assert number_filter.is_even(3) is False

def test_b_extra_09_is_odd(number_filter):
    """B-E09: is_odd(0,) -> False."""
    assert number_filter.is_odd(0) is False

def test_b_extra_10_is_odd(number_filter):
    """B-E10: is_odd(-3,) -> True."""
    assert number_filter.is_odd(-3) is True

def test_b_extra_11_find_max(number_filter):
    """B-E11: find_max([],) -> ValueError."""
    with pytest.raises(ValueError):
        number_filter.find_max([])

def test_b_extra_12_find_max(number_filter):
    """B-E12: find_max([5],) -> 5."""
    assert number_filter.find_max([5]) == 5

def test_b_extra_13_positive_numbers(number_filter):
    """B-E13: positive_numbers([-1, 0, 2, 2],) -> [2, 2]."""
    assert number_filter.positive_numbers([-1, 0, 2, 2]) == [2, 2]
