# tests/test_01_python_basics/conftest.py
"""
Конфигурация тестов для модуля 01_python_basics.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from tests.conftest import run_student_code, get_student_file  # noqa: E402,F401


def get_module01_file(filename):
    """Возвращает путь к файлу студента для модуля 01 (intro, task1-9)."""
    return get_student_file('module_01', filename)


def get_module02_file(filename):
    """Возвращает путь к файлу студента для модуля 02 (intro, task10-15)."""
    return get_student_file('module_02', filename)
