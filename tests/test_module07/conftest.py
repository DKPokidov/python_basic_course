# tests/test_module07/conftest.py
"""
Утилиты для тестов module_07 (04_paradigms, 02_practice_functions_test_gdz_.ipynb)
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from tests.conftest import get_student_file  # noqa: E402,F401


def get_module07_file(filename):
    """Возвращает путь к файлу студента для module_07"""
    return get_student_file('module_07', filename)
