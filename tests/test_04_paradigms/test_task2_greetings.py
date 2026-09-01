# tests/test_04_paradigms/test_task2_greetings.py
"""
Тесты для задания 2: Генератор приветствий
"""

import inspect
import importlib.util
from tests.test_04_paradigms.conftest import get_module09_file


def load_student_code(student_file):
    spec = importlib.util.spec_from_file_location("student_module", student_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TestTask2Greetings:
    """Тесты для задания 2: Генератор приветствий"""

    student_file = get_module09_file('task2_greetings.py')

    def test_is_generator(self):
        mod = load_student_code(self.student_file)
        gen = mod.greetings(["Анна"])
        assert inspect.isgenerator(gen)

    def test_two_names(self):
        mod = load_student_code(self.student_file)
        result = list(mod.greetings(["Анна", "Борис"]))
        assert result == ["Привет, Анна!", "Привет, Борис!"]

    def test_one_name(self):
        mod = load_student_code(self.student_file)
        result = list(mod.greetings(["Анна"]))
        assert result == ["Привет, Анна!"]

    def test_empty_list(self):
        mod = load_student_code(self.student_file)
        result = list(mod.greetings([]))
        assert result == []

    def test_multiple_names(self):
        mod = load_student_code(self.student_file)
        result = list(mod.greetings(["Алиса", "Борис", "Вика"]))
        assert result == ["Привет, Алиса!", "Привет, Борис!", "Привет, Вика!"]
