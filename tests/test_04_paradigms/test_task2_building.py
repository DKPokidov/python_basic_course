# tests/test_04_paradigms/test_task2_building.py
"""
Тесты для задания 2: Здание
"""

import importlib.util
from tests.test_04_paradigms.conftest import get_module08_file


def load_student_code(student_file):
    spec = importlib.util.spec_from_file_location("student_module", student_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TestTask2Building:
    """Тесты для задания 2: Здание"""

    student_file = get_module08_file('task2_building.py')

    def test_create_building(self):
        mod = load_student_code(self.student_file)
        b = mod.Building("Бизнес-центр", 50, 2020, "офисный")
        assert b.name == "Бизнес-центр"
        assert b.height == 50
        assert b.year_built == 2020
        assert b.type == "офисный"

    def test_get_info(self):
        mod = load_student_code(self.student_file)
        b = mod.Building("Бизнес-центр", 50, 2020, "офисный")
        assert b.get_info() == "Здание Бизнес-центр, офисный, построено в 2020, высота 50 м"

    def test_residential_building(self):
        mod = load_student_code(self.student_file)
        b = mod.Building("Панелька", 25, 1985, "жилой")
        assert b.get_info() == "Здание Панелька, жилой, построено в 1985, высота 25 м"

    def test_different_types(self):
        mod = load_student_code(self.student_file)
        b1 = mod.Building("ТЦ Мега", 15, 2010, "торговый")
        b2 = mod.Building("Школа №5", 12, 1990, "образовательный")
        assert "торговый" in b1.get_info()
        assert "образовательный" in b2.get_info()
