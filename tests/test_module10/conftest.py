# tests/test_module10/conftest.py
"""
Утилиты для тестов module_10 (05_api, практическое задание по работе с API ЦБ РФ)
"""

import sys
import os
import importlib.util

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.'))

from tests.conftest import get_student_file  # noqa: E402,F401


def load_student_code(student_file):
    """Загружает модуль студента по пути и возвращает его как объект модуля."""
    spec = importlib.util.spec_from_file_location("student_module", student_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

API_TASKS_DIR = os.path.join(_ROOT, '05_api', 'practice', '01_api_tasks')


def get_module10_file(filename):
    """Возвращает путь к файлу студента для module_10 (05_api)."""
    return os.path.join(API_TASKS_DIR, filename)
