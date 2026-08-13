# tests/test_module01/conftest.py
"""
Утилиты для тестов module_01
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from tests.conftest import run_student_code, get_student_file

def get_module01_file(filename):
    """Возвращает путь к файлу студента для module_01"""
    return get_student_file('module_01', filename)