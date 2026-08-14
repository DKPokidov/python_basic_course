# tests/test_module04/conftest.py
"""
Утилиты для тестов module_04 (03_control_flow, 01_practice_control_flow_gdz.ipynb)
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from tests.conftest import run_student_code, get_student_file  # noqa: E402,F401


def get_module04_file(filename):
    """Возвращает путь к файлу студента для module_04"""
    return get_student_file('module_04', filename)
