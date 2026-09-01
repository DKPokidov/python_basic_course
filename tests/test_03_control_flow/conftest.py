# tests/test_03_control_flow/conftest.py
"""
Конфигурация тестов для модуля 03_control_flow.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from tests.conftest import run_student_code, get_student_file  # noqa: E402,F401


def get_module04_file(filename):
    """Возвращает путь к файлу студента для модуля 04 (control flow, task1-10)."""
    return get_student_file('module_04', filename)


def get_module05_file(filename):
    """Возвращает путь к файлу студента для модуля 05 (control flow, task11-18)."""
    return get_student_file('module_05', filename)
