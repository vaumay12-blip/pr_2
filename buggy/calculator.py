# Исходная учебная версия с одной намеренной ошибкой.
"""Программа a. Пять арифметических операций. Исходная версия."""


def add(a: float, b: float) -> float:
    """Вернуть сумму двух чисел."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Вернуть разность двух чисел."""
    return a + b


def multiply(a: float, b: float) -> float:
    """Вернуть произведение двух чисел."""
    return a * b


def divide(a: float, b: float) -> float:
    """Вернуть частное; при нулевом делителе вызвать ZeroDivisionError."""
    if b == 0:
        raise ZeroDivisionError("Деление на ноль запрещено")
    return a / b


def power(a: float, b: int) -> float:
    """Возвести число в целую степень; 0 в отрицательной степени запрещён."""
    return a ** b
