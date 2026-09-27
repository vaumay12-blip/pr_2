ПРАКТИЧЕСКАЯ РАБОТА 2 — МОДУЛЬНОЕ И МУТАЦИОННОЕ ТЕСТИРОВАНИЕ

Откройте терминал в этом каталоге code. Требуется Python 3.10 или новее.
Проверено на Python 3.12.14, pytest 9.1.1, coverage.py 7.16.1.

БЫСТРЫЙ ЗАПУСК
1. Создать окружение: python -m venv .venv
2. Активировать в Windows: .venv\Scripts\activate
   В Linux/macOS: source .venv/bin/activate
3. Установить зависимости: python -m pip install -r requirements.txt
4. Полностью повторить эксперимент: python run_experiment.py

Если команда python недоступна в Windows, попробуйте py вместо python.
Для запуска приложений pytest и coverage не нужны: достаточно Python.

ТРИ ОТДЕЛЬНЫХ ПРИЛОЖЕНИЯ
python app_a.py — калькулятор
python app_b.py — фильтр чисел
python app_c.py — конвертер единиц
Для выхода выберите 0. Дробные значения вводите через точку.

ФАЙЛЫ
calculator.py, number_filter.py, converter.py — исправленные вычислительные модули.
app_a.py, app_b.py, app_c.py — отдельные консольные интерфейсы.
buggy/ — исходные версии с намеренными ошибками; не исправляйте их для демонстрации.
tests/test_a_base.py, test_b_base.py, test_c_base.py — 29 начальных тестов.
tests/test_a_extra.py, test_b_extra.py, test_c_extra.py — 30 дополнительных тестов.
tests/conftest.py — загрузка выбранной версии модуля.
mutation_runner.py — собственный учебный инструмент автоматических AST-мутаций.
run_experiment.py — автоматическое повторение всех этапов.
.coveragerc — область измерения покрытия; сохраняйте этот файл при копировании проекта.
pytest.ini — настройки поиска тестов.
requirements.txt — зависимости с проверенными версиями.
results/ — фактические результаты выполненного эксперимента.

НАМЕРЕННЫЕ ОШИБКИ
A: subtract выполняет a + b вместо a - b.
B: is_even проверяет n % 2 != 0 вместо n % 2 == 0.
C: celsius_to_fahrenheit вычитает 32 вместо прибавления.

ОТДЕЛЬНЫЕ ЗАПУСКИ
python -m pytest tests/test_a_base.py --module-dir buggy -q
python -m pytest tests/test_b_base.py --module-dir buggy -q
python -m pytest tests/test_c_base.py --module-dir buggy -q
Ожидаемые результаты: A — 8 passed, 1 failed; B и C — 9 passed, 1 failed.
Код завершения 1 в этих трёх командах ожидаем: тест нашёл заданную ошибку.

python -m pytest tests/test_a_base.py -q
python -m pytest tests/test_b_base.py -q
python -m pytest tests/test_c_base.py -q
Исправленные версии: 9, 10 и 10 успешных тестов соответственно.

python -m pytest -q
Все окончательные тесты: 59 passed (A — 17, B — 23, C — 19).

python mutation_runner.py --suite base
16 мутантов: 11 убито, 5 выжило, score 68,75 %.
python mutation_runner.py --suite improved
16 мутантов: 16 убито, 0 выжило, score 100 %.
Это собственный ограниченный каталог мутаций, не запуск MutPy.

ПРОСМОТР РЕЗУЛЬТАТОВ
results/experiment.json — версии среды и количество тестов по этапам.
results/buggy_a.log и аналогичные — исходные ошибки.
results/fixed_a.log и аналогичные — повторное тестирование после исправления.
results/improved_a.log и аналогичные — расширенные тесты.
results/mutation_base.json, mutation_improved.json — результаты каждого мутанта.
results/mutation_base/, mutation_improved/ — логи и XML для каждого мутанта.
results/mutants/ — отдельные Python-файлы всех 16 мутантов.
results/coverage_base.json, coverage_improved.json — покрытие по модулям.
results/coverage_html_base/index.html — начальное покрытие (открыть в браузере).
results/coverage_html_improved/index.html — итоговое покрытие.
results/console_a.log и аналогичные — сохранённые сценарии проверки интерфейсов.
Повторный запуск run_experiment.py обновляет результаты автоматического эксперимента.
Логи console_*.log относятся к отдельной проверке интерфейсов и им не обновляются.

ГРАНИЦЫ ПОКРЫТИЯ
Измеряются только calculator.py, number_filter.py и converter.py.
До расширения: 50/51 строк (98,04 %), 19/20 ветвей (95 %).
После расширения: 51/51 строк и 20/20 ветвей (100 %).
Итоговая колонка Cover в текстовом отчёте coverage объединяет строки и ветви.
Отдельные проценты строк и ветвей приведены в JSON и в отчёте Word.
100 % не означает отсутствие любых возможных ошибок: каталог мутантов ограничен.

РАСПРЕДЕЛЕНИЕ РОЛЕЙ
Участник a разрабатывает A и тестирует B.
Участник b разрабатывает B и тестирует C.
Участник c разрабатывает C и тестирует A.

ДОКУМЕНТАЦИЯ ИНСТРУМЕНТОВ
https://docs.pytest.org/en/stable/reference/reference.html
https://coverage.readthedocs.io/en/latest/commands/cmd_json.html
https://docs.python.org/3/library/ast.html
