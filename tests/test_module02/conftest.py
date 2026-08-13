# tests/test_module02/conftest.py
"""
Утилиты для тестов module_02
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from tests.conftest import run_student_code, get_student_file

def get_module02_file(filename):
    """Возвращает путь к файлу студента для module_02"""
    return get_student_file('module_02', filename)