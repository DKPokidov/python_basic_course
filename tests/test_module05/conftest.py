# tests/test_module05/conftest.py
"""
Утилиты для тестов module_05 (03_control_flow, 02_practice_control_flow_gdz.ipynb)
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from tests.conftest import run_student_code, get_student_file  # noqa: E402,F401


def get_module05_file(filename):
    """Возвращает путь к файлу студента для module_05"""
    return get_student_file('module_05', filename)
