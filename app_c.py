"""Консольный интерфейс конвертера. Запуск: python app_c.py."""
import math
from converter import (meters_to_kilometers, kilometers_to_meters, kilograms_to_grams,
                       celsius_to_fahrenheit, fahrenheit_to_celsius)


def main():
    operations = {"1": meters_to_kilometers, "2": kilometers_to_meters, "3": kilograms_to_grams,
                  "4": celsius_to_fahrenheit, "5": fahrenheit_to_celsius}
    while True:
        print("\nКонвертер: 1 м -> км; 2 км -> м; 3 кг -> г; 4 C -> F; 5 F -> C; 0 выход")
        choice = input("Операция: ").strip()
        if choice == "0":
            break
        if choice not in operations:
            print("Выберите пункт от 0 до 5")
            continue
        try:
            value = float(input("Значение: "))
            if not math.isfinite(value):
                raise ValueError("Введите конечное число")
            print("Результат:", operations[choice](value))
        except (ValueError, OverflowError) as error:
            print("Ошибка:", error)


if __name__ == "__main__":
    main()
