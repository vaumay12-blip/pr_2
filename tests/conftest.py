"""Загрузка нужной версии модуля без изменения тестов."""
import importlib.util
from pathlib import Path
import pytest


def pytest_addoption(parser):
    parser.addoption("--module-dir", default=str(Path(__file__).resolve().parents[1]),
                     help="Каталог исходной, исправленной или мутированной версии")


@pytest.fixture(scope="session")
def module_loader(request):
    directory = Path(request.config.getoption("--module-dir"))
    def load(name):
        path = directory / (name + ".py")
        spec = importlib.util.spec_from_file_location("tested_" + name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    return load


@pytest.fixture(scope="session")
def calculator(module_loader):
    return module_loader("calculator")


@pytest.fixture(scope="session")
def number_filter(module_loader):
    return module_loader("number_filter")


@pytest.fixture(scope="session")
def converter(module_loader):
    return module_loader("converter")
