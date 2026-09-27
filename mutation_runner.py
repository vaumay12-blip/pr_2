"""Автоматические точечные AST-мутации и запуск pytest на каждом мутанте.

Создаются 16 заранее определённых одиночных мутаций. Это учебный инструмент,
а не MutPy: каталог ограничен указанными ниже операторами и константами.
Запуск: python mutation_runner.py --suite base (или improved).
"""
import argparse
import ast
import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
# id, модуль, функция, тип узла, исходное значение/оператор, замена
CATALOG = [
    ("A1", "calculator", "add", "BinOp", "Add", "Sub"),
    ("A2", "calculator", "subtract", "BinOp", "Sub", "Add"),
    ("A3", "calculator", "multiply", "BinOp", "Mult", "Div"),
    ("A4", "calculator", "divide", "BinOp", "Div", "FloorDiv"),
    ("A5", "calculator", "power", "BinOp", "Pow", "Mult"),
    ("B1", "number_filter", "is_even", "Compare", "Eq", "NotEq"),
    ("B2", "number_filter", "is_odd", "Compare", "NotEq", "Eq"),
    ("B3", "number_filter", "is_prime", "Compare", "Lt", "LtE"),
    ("B4", "number_filter", "find_max", "Compare", "Gt", "Lt"),
    ("B5", "number_filter", "positive_numbers", "Compare", "Gt", "GtE"),
    ("C1", "converter", "meters_to_kilometers", "BinOp", "Div", "Mult"),
    ("C2", "converter", "kilometers_to_meters", "BinOp", "Mult", "Div"),
    ("C3", "converter", "kilograms_to_grams", "Constant", 1000, 100),
    ("C4", "converter", "celsius_to_fahrenheit", "BinOp", "Add", "Sub"),
    ("C5", "converter", "fahrenheit_to_celsius", "BinOp", "Sub", "Add"),
    ("C6", "converter", "celsius_to_fahrenheit", "Constant", 9, 10),
]


def create_mutant(source, rule):
    """Изменить ровно один узел дерева только внутри указанной функции."""
    _, _, function, kind, old, new = rule
    tree = copy.deepcopy(ast.parse(source))
    matches = []
    for definition in tree.body:
        if isinstance(definition, ast.FunctionDef) and definition.name == function:
            for node in ast.walk(definition):
                if kind == "BinOp" and isinstance(node, ast.BinOp) and type(node.op).__name__ == old:
                    matches.append((node, "op"))
                elif kind == "Compare" and isinstance(node, ast.Compare) and len(node.ops) == 1 and type(node.ops[0]).__name__ == old:
                    matches.append((node, "ops"))
                elif kind == "Constant" and isinstance(node, ast.Constant) and node.value == old:
                    matches.append((node, "value"))
    if len(matches) != 1:
        raise ValueError(f"Ожидалась одна точка мутации для {rule[0]}, найдено {len(matches)}")
    node, attribute = matches[0]
    replacement = new if kind == "Constant" else getattr(ast, new)()
    setattr(node, attribute, [replacement] if attribute == "ops" else replacement)
    ast.fix_missing_locations(tree)
    compile(tree, "<mutant>", "exec")
    return ast.unparse(tree) + "\n"


def test_paths(letter, suite):
    paths = [f"tests/test_{letter.lower()}_base.py"]
    if suite == "improved":
        paths.append(f"tests/test_{letter.lower()}_extra.py")
    return paths


def run_pytest(paths, directory, log_path, xml_path):
    """Отдельный процесс предотвращает смешивание импортов разных версий."""
    command = [sys.executable, "-B", "-m", "pytest", *paths, "--module-dir", str(directory),
               "-q", "--tb=short", "--color=no", "-p", "no:cacheprovider", f"--junitxml={xml_path}"]
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONIOENCODING="utf-8",
                       PYTEST_DISABLE_PLUGIN_AUTOLOAD="1")
    try:
        process = subprocess.run(command, cwd=ROOT, env=environment, text=True,
                                 encoding="utf-8", errors="replace", capture_output=True, timeout=30)
    except subprocess.TimeoutExpired:
        return {"status": "timeout"}
    output = process.stdout + process.stderr
    log_path.write_text(output, encoding="utf-8")
    if not xml_path.exists():
        return {"status": "error", "returncode": process.returncode}
    cases = ET.parse(xml_path).getroot().findall(".//testcase")
    failures = [case.attrib["name"] for case in cases if case.find("failure") is not None]
    errors = [case.attrib["name"] for case in cases if case.find("error") is not None]
    skipped = [case.attrib["name"] for case in cases if case.find("skipped") is not None]
    if process.returncode == 0 and cases and not skipped:
        status = "survived"
    elif process.returncode == 1 and failures and not errors and not skipped:
        status = "killed"
    else:
        status = "error"
    return {"status": status, "tests": len(cases), "failed": failures, "errors": errors,
            "returncode": process.returncode}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--suite", choices=["base", "improved"], default="base")
    args = parser.parse_args()
    destination = ROOT / "results" / ("mutation_" + args.suite)
    destination.mkdir(parents=True, exist_ok=True)
    # Если немутированный код не проходит тесты, оценка мутантов бессмысленна.
    for letter in "abc":
        result = run_pytest(test_paths(letter, args.suite), ROOT,
                            destination / f"control_{letter}.log", destination / f"control_{letter}.xml")
        if result["status"] != "survived":
            raise RuntimeError(f"Контрольная версия {letter} не прошла тесты: {result}")
    results = []
    for rule in CATALOG:
        identifier, module, function, kind, old, new = rule
        directory = ROOT / "results" / "mutants" / identifier
        directory.mkdir(parents=True, exist_ok=True)
        mutant = create_mutant((ROOT / (module + ".py")).read_text(encoding="utf-8"), rule)
        (directory / (module + ".py")).write_text(mutant, encoding="utf-8")
        result = run_pytest(test_paths(identifier[0], args.suite), directory,
                            destination / (identifier + ".log"), destination / (identifier + ".xml"))
        result.update(id=identifier, module=module, function=function, kind=kind, old=old, new=new)
        results.append(result)
        print(f"{identifier}: {function}: {old} -> {new}: {result['status']}", flush=True)
    killed = sum(item["status"] == "killed" for item in results)
    survived = sum(item["status"] == "survived" for item in results)
    invalid = len(results) - killed - survived
    # Все выбранные мутации имеют различающий вход; эквивалентных в этом каталоге нет.
    report = {"suite": args.suite, "total": len(results), "killed": killed,
              "survived": survived, "invalid": invalid,
              "score": killed / len(results) * 100 if not invalid else None, "mutants": results}
    (ROOT / "results" / f"mutation_{args.suite}.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Total: {len(results)}; killed: {killed}; survived: {survived}; invalid: {invalid}")
    if invalid:
        raise SystemExit("Есть технические ошибки: mutation score не рассчитан")


if __name__ == "__main__":
    main()
