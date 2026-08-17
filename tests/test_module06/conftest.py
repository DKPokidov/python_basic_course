# tests/test_module06/conftest.py
"""
Утилиты для тестов module_06 (04_paradigms, 01_practice_functions_gdz.ipynb)
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from tests.conftest import run_student_code, get_student_file  # noqa: E402,F401


def get_module06_file(filename):
    """Возвращает путь к файлу студента для module_06"""
    return get_student_file('module_06', filename)
