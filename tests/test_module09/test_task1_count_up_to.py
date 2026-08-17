# tests/test_module09/test_task1_count_up_to.py
"""
Тесты для задания 1: Генератор натуральных чисел
"""

import inspect
import importlib.util
from tests.test_module09.conftest import get_module09_file


def load_student_code(student_file):
    spec = importlib.util.spec_from_file_location("student_module", student_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TestTask1CountUpTo:
    """Тесты для задания 1: Генератор натуральных чисел"""

    student_file = get_module09_file('task1_count_up_to.py')

    def test_is_generator(self):
        mod = load_student_code(self.student_file)
        gen = mod.count_up_to(5)
        assert inspect.isgenerator(gen)

    def test_count_up_to_5(self):
        mod = load_student_code(self.student_file)
        result = list(mod.count_up_to(5))
        assert result == [1, 2, 3, 4, 5]

    def test_count_up_to_1(self):
        mod = load_student_code(self.student_file)
        result = list(mod.count_up_to(1))
        assert result == [1]

    def test_count_up_to_0(self):
        mod = load_student_code(self.student_file)
        result = list(mod.count_up_to(0))
        assert result == []

    def test_count_up_to_3(self):
        mod = load_student_code(self.student_file)
        result = list(mod.count_up_to(3))
        assert result == [1, 2, 3]
