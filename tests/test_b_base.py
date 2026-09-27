"""Начальные тесты программы b."""
import pytest


def test_b_base_01_is_even(number_filter):
    """B-B01: is_even(4,) -> True."""
    assert number_filter.is_even(4) is True

def test_b_base_02_is_odd(number_filter):
    """B-B02: is_odd(3,) -> True."""
    assert number_filter.is_odd(3) is True

def test_b_base_03_is_odd(number_filter):
    """B-B03: is_odd(4,) -> False."""
    assert number_filter.is_odd(4) is False

def test_b_base_04_is_prime(number_filter):
    """B-B04: is_prime(1,) -> False."""
    assert number_filter.is_prime(1) is False

def test_b_base_05_is_prime(number_filter):
    """B-B05: is_prime(7,) -> True."""
    assert number_filter.is_prime(7) is True

def test_b_base_06_is_prime(number_filter):
    """B-B06: is_prime(9,) -> False."""
    assert number_filter.is_prime(9) is False

def test_b_base_07_find_max(number_filter):
    """B-B07: find_max([3, 1, 8],) -> 8."""
    assert number_filter.find_max([3, 1, 8]) == 8

def test_b_base_08_find_max(number_filter):
    """B-B08: find_max([-4, -2, -9],) -> -2."""
    assert number_filter.find_max([-4, -2, -9]) == -2

def test_b_base_09_positive_numbers(number_filter):
    """B-B09: positive_numbers([-3, 2, -1, 5],) -> [2, 5]."""
    assert number_filter.positive_numbers([-3, 2, -1, 5]) == [2, 5]

def test_b_base_10_positive_numbers(number_filter):
    """B-B10: positive_numbers([],) -> []."""
    assert number_filter.positive_numbers([]) == []
