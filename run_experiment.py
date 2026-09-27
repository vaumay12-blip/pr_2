"""Повторить все этапы работы: python run_experiment.py.

Логи, XML, JSON, HTML-покрытие и мутанты сохраняются в results.
Первый этап намеренно содержит проваленные тесты; это ожидаемый результат.
"""
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import xml.etree.ElementTree as ET
import coverage
import pytest

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"
ENV = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONIOENCODING="utf-8",
           PYTEST_DISABLE_PLUGIN_AUTOLOAD="1")


def execute(arguments, name, allowed=(0,)):
    process = subprocess.run([sys.executable, "-B", *arguments], cwd=ROOT, env=ENV,
                             capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=240)
    (RESULTS / (name + ".log")).write_text(process.stdout + process.stderr, encoding="utf-8")
    if process.returncode not in allowed:
        raise RuntimeError(f"Ошибка этапа {name}; см. results/{name}.log")
    return process


def main():
    RESULTS.mkdir(exist_ok=True)
    report = {"environment": {"python": platform.python_version(), "pytest": pytest.__version__,
                              "coverage": coverage.__version__, "platform": platform.platform()}, "stages": {}}
    for stage in ["buggy", "fixed", "improved"]:
        summary = {}
        for letter in "abc":
            name = f"{stage}_{letter}"
            paths = [f"tests/test_{letter}_base.py"]
            if stage == "improved":
                paths.append(f"tests/test_{letter}_extra.py")
            directory = ROOT / "buggy" if stage == "buggy" else ROOT
            xml = RESULTS / (name + ".xml")
            arguments = ["-m", "pytest", *paths, "--module-dir", str(directory), "-q", "--tb=short",
                         "--color=no", "-p", "no:cacheprovider", f"--junitxml={xml}"]
            execute(arguments, name, (0, 1) if stage == "buggy" else (0,))
            cases = ET.parse(xml).getroot().findall(".//testcase")
            failed = [x.attrib['name'] for x in cases if x.find('failure') is not None]
            errors = [x for x in cases if x.find('error') is not None or x.find('skipped') is not None]
            if errors or not cases or (stage == 'buggy' and len(failed) != 1):
                raise RuntimeError(f"Неожиданный результат {name}")
            summary[letter] = {"tests": len(cases), "failed": len(failed), "passed": len(cases)-len(failed), "failure_names": failed}
            print(f"{name}: {summary[letter]['passed']} passed, {len(failed)} failed", flush=True)
        report["stages"][stage] = summary
    for suite in ["base", "improved"]:
        paths = [f"tests/test_{letter}_base.py" for letter in "abc"]
        if suite == "improved":
            paths += [f"tests/test_{letter}_extra.py" for letter in "abc"]
        data_file = str(RESULTS / (".coverage_" + suite))
        execute(["-m", "coverage", "run", "--branch", f"--data-file={data_file}", "-m", "pytest", *paths,
                 "-q", "-p", "no:cacheprovider"], "coverage_run_"+suite)
        execute(["-m", "coverage", "report", f"--data-file={data_file}", "-m"], "coverage_"+suite)
        execute(["-m", "coverage", "json", f"--data-file={data_file}", "-o", str(RESULTS / ("coverage_"+suite+".json"))], "coverage_json_"+suite)
        execute(["-m", "coverage", "html", f"--data-file={data_file}", "-d", str(RESULTS / ("coverage_html_"+suite))], "coverage_html_"+suite)
        print(f"Coverage {suite}: saved", flush=True)
        execute(["mutation_runner.py", "--suite", suite], "mutation_"+suite)
        print((RESULTS / ("mutation_"+suite+".log")).read_text(encoding='utf-8').splitlines()[-1], flush=True)
    (RESULTS / "experiment.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print("Готово. Результаты: results/experiment.json")


if __name__ == "__main__":
    main()
