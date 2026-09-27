"""Начальные тесты программы c."""
import pytest


def test_c_base_01_meters_to_kilometers(converter):
    """C-B01: meters_to_kilometers(1500,) -> 1.5."""
    assert converter.meters_to_kilometers(1500) == pytest.approx(1.5, rel=1e-9, abs=1e-9)

def test_c_base_02_meters_to_kilometers(converter):
    """C-B02: meters_to_kilometers(-1,) -> ValueError."""
    with pytest.raises(ValueError):
        converter.meters_to_kilometers(-1)

def test_c_base_03_kilometers_to_meters(converter):
    """C-B03: kilometers_to_meters(2.5,) -> 2500."""
    assert converter.kilometers_to_meters(2.5) == 2500

def test_c_base_04_kilometers_to_meters(converter):
    """C-B04: kilometers_to_meters(-1,) -> ValueError."""
    with pytest.raises(ValueError):
        converter.kilometers_to_meters(-1)

def test_c_base_05_kilograms_to_grams(converter):
    """C-B05: kilograms_to_grams(2,) -> 2000."""
    assert converter.kilograms_to_grams(2) == 2000

def test_c_base_06_kilograms_to_grams(converter):
    """C-B06: kilograms_to_grams(-1,) -> ValueError."""
    with pytest.raises(ValueError):
        converter.kilograms_to_grams(-1)

def test_c_base_07_celsius_to_fahrenheit(converter):
    """C-B07: celsius_to_fahrenheit(0,) -> 32."""
    assert converter.celsius_to_fahrenheit(0) == 32

def test_c_base_08_fahrenheit_to_celsius(converter):
    """C-B08: fahrenheit_to_celsius(32,) -> 0."""
    assert converter.fahrenheit_to_celsius(32) == 0

def test_c_base_09_fahrenheit_to_celsius(converter):
    """C-B09: fahrenheit_to_celsius(212,) -> 100."""
    assert converter.fahrenheit_to_celsius(212) == 100

def test_c_base_10_fahrenheit_to_celsius(converter):
    """C-B10: fahrenheit_to_celsius(-40,) -> -40."""
    assert converter.fahrenheit_to_celsius(-40) == -40
