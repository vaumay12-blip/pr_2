"""Консольный интерфейс фильтра чисел. Запуск: python app_b.py."""
from number_filter import is_even, is_odd, is_prime, find_max, positive_numbers


def main():
    operations = {"1": is_even, "2": is_odd, "3": is_prime, "4": find_max, "5": positive_numbers}
    while True:
        print("\nФильтр: 1 чётность; 2 нечётность; 3 простота; 4 максимум; 5 положительные; 0 выход")
        choice = input("Операция: ").strip()
        if choice == "0":
            break
        if choice not in operations:
            print("Выберите пункт от 0 до 5")
            continue
        try:
            if choice in ("4", "5"):
                argument = [int(item) for item in input("Целые числа через пробел: ").split()]
            else:
                argument = int(input("Целое число: "))
            print("Результат:", operations[choice](argument))
        except ValueError as error:
            print("Ошибка:", error)


if __name__ == "__main__":
    main()
