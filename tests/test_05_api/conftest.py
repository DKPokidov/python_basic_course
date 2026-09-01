# tests/test_05_api/conftest.py
"""
Конфигурация тестов для модуля 05_api.
"""

import sys
import os
import importlib.util

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from tests.conftest import get_student_file  # noqa: E402,F401


def load_student_code(student_file):
    """Загружает код студента как модуль Python."""
    spec = importlib.util.spec_from_file_location("student_module", student_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def get_module10_file(filename):
    """Возвращает путь к файлу студента для модуля 10 (API, task1-4)."""
    return get_student_file('module_10', filename)
