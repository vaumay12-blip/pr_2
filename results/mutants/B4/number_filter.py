"""Программа b. Проверки целых чисел и обработка списков."""

def is_even(n: int) -> bool:
    """Вернуть True для чётного целого числа, включая ноль."""
    return n % 2 == 0

def is_odd(n: int) -> bool:
    """Вернуть True для нечётного целого числа."""
    return n % 2 != 0

def is_prime(n: int) -> bool:
    """Проверить простоту перебором делителей до квадратного корня."""
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True

def find_max(numbers: list[int]) -> int:
    """Найти максимум непустого списка; пустой список вызывает ValueError."""
    if not numbers:
        raise ValueError('Список не должен быть пустым')
    maximum = numbers[0]
    for number in numbers[1:]:
        if number < maximum:
            maximum = number
    return maximum

def positive_numbers(numbers: list[int]) -> list[int]:
    """Создать список строго положительных чисел, сохранив порядок и повторы."""
    return [number for number in numbers if number > 0]
