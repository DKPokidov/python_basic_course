# tests/test_04_paradigms/test_task2_bus_routes.py
"""
Тесты для задания 2: Оптимизация автобусных маршрутов
"""

import importlib.util
from tests.test_04_paradigms.conftest import get_module06_file


def load_student_code(student_file):
    spec = importlib.util.spec_from_file_location("student_module", student_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TestTask2BusRoutes:
    """Тесты для задания 2: Оптимизация автобусных маршрутов"""

    student_file = get_module06_file('task2_bus_routes.py')

    def test_load_per_km_basic(self):
        mod = load_student_code(self.student_file)
        route = {"number": 1, "length": 10.0, "passengers": 3000}
        assert mod.load_per_km(route) == 300.0

    def test_load_per_km_small(self):
        mod = load_student_code(self.student_file)
        route = {"number": 5, "length": 5.0, "passengers": 500}
        assert mod.load_per_km(route) == 100.0

    def test_load_per_km_rounding(self):
        mod = load_student_code(self.student_file)
        route = {"number": 3, "length": 7.0, "passengers": 1000}
        assert mod.load_per_km(route) == 142.9

    def test_needs_review_true(self):
        mod = load_student_code(self.student_file)
        assert mod.needs_review(150) is True

    def test_needs_review_false(self):
        mod = load_student_code(self.student_file)
        assert mod.needs_review(250) is False

    def test_needs_review_boundary(self):
        mod = load_student_code(self.student_file)
        assert mod.needs_review(200) is False
