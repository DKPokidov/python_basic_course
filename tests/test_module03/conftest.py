# tests/test_module03/conftest.py
"""
Утилиты для тестов module_03 (02_python_structures)
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from tests.conftest import run_student_code, get_student_file  # noqa: E402,F401


def get_module03_file(filename):
    """Возвращает путь к файлу студента для module_03"""
    return get_student_file('module_03', filename)
