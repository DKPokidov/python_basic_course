# tests/test_module09/conftest.py
"""
Утилиты для тестов module_09 (04_paradigms, 04_iterator_generator_tasks)
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from tests.conftest import get_student_file  # noqa: E402,F401


def get_module09_file(filename):
    """Возвращает путь к файлу студента для module_09"""
    return get_student_file('module_09', filename)
