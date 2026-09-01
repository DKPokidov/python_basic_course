# tests/test_02_python_structures/conftest.py
"""
Конфигурация тестов для модуля 02_python_structures.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from tests.conftest import run_student_code, get_student_file  # noqa: E402,F401


def get_module03_file(filename):
    """Возвращает путь к файлу студента для модуля 03 (structures, task1-15)."""
    return get_student_file('module_03', filename)
