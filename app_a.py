"""Консольный интерфейс калькулятора. Запуск: python app_a.py."""
import math
from calculator import add, subtract, multiply, divide, power


def main():
    operations = {"1": add, "2": subtract, "3": multiply, "4": divide, "5": power}
    while True:
        print("\nКалькулятор: 1 +; 2 -; 3 *; 4 /; 5 степень; 0 выход")
        choice = input("Операция: ").strip()
        if choice == "0":
            break
        if choice not in operations:
            print("Выберите пункт от 0 до 5")
            continue
        try:
            a = float(input("Первое число: "))
            b = int(input("Целая степень: ")) if choice == "5" else float(input("Второе число: "))
            if not math.isfinite(a) or not math.isfinite(b):
                raise ValueError("Введите конечные числа")
            print("Результат:", operations[choice](a, b))
        except (ValueError, ZeroDivisionError, OverflowError) as error:
            print("Ошибка:", error)


if __name__ == "__main__":
    main()
