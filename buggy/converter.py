# Исходная учебная версия с одной намеренной ошибкой.
"""Программа c. Преобразование длины, массы и температуры."""


def meters_to_kilometers(value: float) -> float:
    """Перевести неотрицательные метры в километры."""
    if value < 0:
        raise ValueError("Длина не может быть отрицательной")
    return value / 1000


def kilometers_to_meters(value: float) -> float:
    """Перевести неотрицательные километры в метры."""
    if value < 0:
        raise ValueError("Длина не может быть отрицательной")
    return value * 1000


def kilograms_to_grams(value: float) -> float:
    """Перевести неотрицательные килограммы в граммы."""
    if value < 0:
        raise ValueError("Масса не может быть отрицательной")
    return value * 1000


def celsius_to_fahrenheit(value: float) -> float:
    """Преобразовать температуру по формуле F = C * 9 / 5 + 32."""
    return value * 9 / 5 - 32


def fahrenheit_to_celsius(value: float) -> float:
    """Преобразовать температуру по формуле C = (F - 32) * 5 / 9."""
    return (value - 32) * 5 / 9
