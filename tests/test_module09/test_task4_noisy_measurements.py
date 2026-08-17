# tests/test_module09/test_task4_noisy_measurements.py
"""
Тесты для задания 4: Генератор зашумлённых измерений
"""

import random
import inspect
import importlib.util
from tests.test_module09.conftest import get_module09_file


def load_student_code(student_file):
    spec = importlib.util.spec_from_file_location("student_module", student_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TestTask4NoisyMeasurements:
    """Тесты для задания 4: Генератор зашумлённых измерений"""

    student_file = get_module09_file('task4_noisy_measurements.py')

    def test_is_generator(self):
        mod = load_student_code(self.student_file)
        random.seed(42)
        gen = mod.noisy_measurements([10], 0.05)
        assert inspect.isgenerator(gen)

    def test_one_value_three_measurements(self):
        mod = load_student_code(self.student_file)
        random.seed(42)
        result = list(mod.noisy_measurements([10], 0.05))
        assert len(result) == 3

    def test_empty_values(self):
        mod = load_student_code(self.student_file)
        random.seed(42)
        result = list(mod.noisy_measurements([], 0.05))
        assert result == []

    def test_values_within_noise(self):
        mod = load_student_code(self.student_file)
        random.seed(42)
        result = list(mod.noisy_measurements([10], 0.05))
        for val in result:
            assert abs(val - 10) <= 10 * 0.05

    def test_two_values_six_measurements(self):
        mod = load_student_code(self.student_file)
        random.seed(42)
        result = list(mod.noisy_measurements([10, 20], 0.05))
        assert len(result) == 6

    def test_default_noise_level(self):
        mod = load_student_code(self.student_file)
        random.seed(42)
        result = list(mod.noisy_measurements([100]))
        assert len(result) == 3
        for val in result:
            assert abs(val - 100) <= 100 * 0.1
