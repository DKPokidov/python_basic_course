# tests/test_module08/conftest.py
"""
Утилиты для тестов module_08 (04_paradigms, 03_practice_OOP_gdz.ipynb)
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from tests.conftest import get_student_file  # noqa: E402,F401


def get_module08_file(filename):
    """Возвращает путь к файлу студента для module_08"""
    return get_student_file('module_08', filename)
