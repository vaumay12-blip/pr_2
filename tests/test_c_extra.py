"""Дополнительные тесты программы c."""
import pytest


def test_c_extra_01_celsius_to_fahrenheit(converter):
    """C-E01: celsius_to_fahrenheit(100,) -> 212."""
    assert converter.celsius_to_fahrenheit(100) == 212

def test_c_extra_02_celsius_to_fahrenheit(converter):
    """C-E02: celsius_to_fahrenheit(-40,) -> -40."""
    assert converter.celsius_to_fahrenheit(-40) == -40

def test_c_extra_03_celsius_to_fahrenheit(converter):
    """C-E03: celsius_to_fahrenheit(37,) -> 98.6."""
    assert converter.celsius_to_fahrenheit(37) == pytest.approx(98.6, rel=1e-9, abs=1e-9)

def test_c_extra_04_meters_to_kilometers(converter):
    """C-E04: meters_to_kilometers(0,) -> 0."""
    assert converter.meters_to_kilometers(0) == 0

def test_c_extra_05_meters_to_kilometers(converter):
    """C-E05: meters_to_kilometers(0.5,) -> 0.0005."""
    assert converter.meters_to_kilometers(0.5) == pytest.approx(0.0005, rel=1e-9, abs=1e-9)

def test_c_extra_06_kilometers_to_meters(converter):
    """C-E06: kilometers_to_meters(0,) -> 0."""
    assert converter.kilometers_to_meters(0) == 0

def test_c_extra_07_kilograms_to_grams(converter):
    """C-E07: kilograms_to_grams(0,) -> 0."""
    assert converter.kilograms_to_grams(0) == 0

def test_c_extra_08_kilograms_to_grams(converter):
    """C-E08: kilograms_to_grams(0.001,) -> 1."""
    assert converter.kilograms_to_grams(0.001) == 1

def test_c_extra_09_fahrenheit_to_celsius(converter):
    """C-E09: fahrenheit_to_celsius(98.6,) -> 37."""
    assert converter.fahrenheit_to_celsius(98.6) == 37
