# tests/test_04_paradigms/conftest.py
"""
Конфигурация тестов для модуля 04_paradigms.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from tests.conftest import run_student_code, get_student_file  # noqa: E402,F401


def get_module06_file(filename):
    """Возвращает путь к файлу студента для модуля 06 (functions, task1-6)."""
    return get_student_file('module_06', filename)


def get_module07_file(filename):
    """Возвращает путь к файлу студента для модуля 07 (functions tests, task1-5)."""
    return get_student_file('module_07', filename)


def get_module08_file(filename):
    """Возвращает путь к файлу студента для модуля 08 (OOP, task1-6)."""
    return get_student_file('module_08', filename)


def get_module09_file(filename):
    """Возвращает путь к файлу студента для модуля 09 (iterators, task1-4)."""
    return get_student_file('module_09', filename)
